# mypy: disable-error-code="import"
"""Defines utilites for saving and loading audio streams.

The main API for using this module is:

.. code-block:: python

    from ml.utils.audio import read_audio, write_audio

This just uses FFMPEG so it should be rasonably quick.
"""

import fractions
import logging
import multiprocessing as mp
import os
import random
import re
import shutil
import warnings
from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import Deque, Iterator, Literal, Sequence, TypeVar

import av
import numpy as np
import soundfile as sf
import torch
import torchaudio.functional as A
import tqdm
from torch import Tensor
from torch.utils.data.dataset import ConcatDataset, Dataset, IterableDataset

from ml.utils.data import get_worker_info
from ml.utils.distributed import get_world_size
from ml.utils.io import prefetch_samples
from ml.utils.numpy import as_numpy_array
from ml.utils.timer import Timer

logger = logging.getLogger(__name__)

T = TypeVar("T")

DEFAULT_BLOCKSIZE = 16_000

AUDIO_FILE_EXTENSIONS = [".wav", ".flac", ".mp3"]

Reader = Literal["ffmpeg", "av", "sf"]
Writer = Literal["ffmpeg", "av", "sf"]


class _DefaultReader:
    def __init__(self) -> None:
        self.reader: Reader = "sf"

    def set(self, reader: Reader) -> None:
        self.reader = reader


class _DefaultWriter:
    def __init__(self) -> None:
        self.writer: Writer = "sf"

    def set(self, writer: Writer) -> None:
        self.writer = writer


_DefaultReaderSingleton = _DefaultReader()
_DefaultWriterSingleton = _DefaultWriter()
set_default_audio_reader = _DefaultReaderSingleton.set
set_default_audio_writer = _DefaultWriterSingleton.set


@dataclass
class AudioProps:
    sample_rate: int
    channels: int
    num_frames: int

    @classmethod
    def from_file_sf(cls, fpath: str | Path) -> "AudioProps":
        info = sf.info(str(fpath))
        return cls(
            sample_rate=info.samplerate,
            channels=info.channels,
            num_frames=info.frames,
        )

    @classmethod
    def from_file_av(cls, fpath: str | Path) -> "AudioProps":
        with av.open(str(fpath)) as container:
            stream = container.streams.audio[0]

            return cls(
                sample_rate=stream.rate,
                channels=stream.channels,
                num_frames=stream.duration,
            )

    @classmethod
    def from_file_ffmpeg(cls, fpath: str | Path) -> "AudioProps":
        try:
            import ffmpeg
        except ModuleNotFoundError as e:
            raise ModuleNotFoundError("Install FFMPEG to use this function: `pip install ffmpeg-python`") from e

        probe = ffmpeg.probe(str(fpath))

        for stream in probe["streams"]:
            if stream["codec_type"] == "audio":
                return cls(
                    sample_rate=int(stream["sample_rate"]),
                    channels=int(stream["channels"]),
                    num_frames=int(stream["duration_ts"]),
                )

        raise ValueError(f"Could not find audio stream in {fpath}")


@dataclass
class AudioFile:
    path: Path
    props: AudioProps

    @classmethod
    def parse(cls, line: str) -> "AudioFile":
        path, num_frames, sample_rate, channels = re.split(r"\s+", line.strip())
        return AudioFile(
            path=Path(path),
            props=AudioProps(
                sample_rate=int(sample_rate),
                channels=int(channels),
                num_frames=int(num_frames),
            ),
        )

    def __repr__(self) -> str:
        return "\t".join(
            [
                str(self.path),
                str(self.props.sample_rate),
                str(self.props.channels),
                str(self.props.num_frames),
            ]
        )


def _cleanup_wav_chunk(wav: np.ndarray, channels: int | None = None) -> np.ndarray:
    if wav.ndim == 1:
        wav = wav.reshape(-1, 1 if channels is None else channels).T
    return wav


def read_audio_sf(in_file: str | Path, *, blocksize: int = DEFAULT_BLOCKSIZE) -> Iterator[np.ndarray]:
    """Function that reads an audio file to a stream of numpy arrays using SoundFile.

    Args:
        in_file: Path to the input file.
        blocksize: Number of samples to read at a time.

    Yields:
        Audio chunks as numpy arrays, with shape (n_channels, n_samples).
    """
    with sf.SoundFile(str(in_file), mode="r") as f:
        for frame in f.blocks(blocksize=blocksize):
            yield _cleanup_wav_chunk(frame.T)


def read_audio_av(in_file: str | Path) -> Iterator[np.ndarray]:
    """Function that reads an audio file to a stream of numpy arrays using PyAV.

    Args:
        in_file: Path to the input file.

    Yields:
        Audio chunks as numpy arrays, with shape (n_channels, n_samples).
    """
    props = AudioProps.from_file_av(in_file)

    with av.open(str(in_file)) as container:
        stream = container.streams.audio[0]

        for frame in container.decode(stream):
            frame_np = frame.to_ndarray().reshape(-1, props.channels).T
            if frame_np.dtype == np.int16:
                frame_np = frame_np.astype(np.float32) / 2**15
            yield frame_np


def read_audio_ffmpeg(in_file: str | Path, *, chunk_size: int = DEFAULT_BLOCKSIZE) -> Iterator[np.ndarray]:
    """Function that reads an audio file to a stream of numpy arrays using FFMPEG.

    Args:
        in_file: Path to the input file.
        chunk_size: Size of the chunks to read.

    Yields:
        Audio chunks as numpy arrays, with shape (n_channels, n_samples).
    """
    props = AudioProps.from_file_ffmpeg(in_file)

    try:
        import ffmpeg
    except ModuleNotFoundError as e:
        raise ModuleNotFoundError("Install FFMPEG to use this function: `pip install ffmpeg-python`") from e

    stream = ffmpeg.input(str(in_file))
    stream = ffmpeg.output(stream, "pipe:", format="f32le", acodec="pcm_f32le")
    stream = ffmpeg.run_async(stream, pipe_stdout=True, quiet=True)

    while True:
        chunk = stream.stdout.read(chunk_size)
        if not chunk:
            break
        yield np.frombuffer(chunk, dtype=np.float32).reshape(props.channels, -1)

    stream.stdout.close()
    stream.wait()


def write_audio_sf(itr: Iterator[np.ndarray | Tensor], out_file: str | Path, sample_rate: int) -> None:
    """Function that writes a stream of audio to a file using SoundFile.

    Args:
        itr: Iterator of audio chunks, with shape (n_channels, n_samples).
        out_file: Path to the output file.
        sample_rate: Sampling rate of the audio.
    """
    first_chunk = _cleanup_wav_chunk(as_numpy_array(next(itr)))
    assert (channels := first_chunk.shape[0]) in (1, 2), f"Expected 1 or 2 channels, got {channels}"
    with sf.SoundFile(str(out_file), mode="w", samplerate=sample_rate, channels=channels) as f:
        f.write(first_chunk.T)
        for chunk in itr:
            f.write(chunk.T)


def write_audio_av(itr: Iterator[np.ndarray | Tensor], out_file: str | Path, sample_rate: int) -> None:
    """Function that writes a stream of audio to a file using PyAV.

    Args:
        itr: Iterator of audio chunks, with shape (n_channels, n_samples).
        out_file: Path to the output file.
        sample_rate: Sampling rate of the audio.
    """
    with av.open(str(out_file), mode="w") as container:
        stream = container.add_stream("pcm_f32le", rate=sample_rate)

        is_first_frame = True
        is_mono = True
        for frame in itr:
            frame_np_float = _cleanup_wav_chunk(as_numpy_array(frame))
            assert frame_np_float.ndim == 2, f"Expected 2D array, got {frame_np_float.shape}D"

            if is_first_frame:
                assert (channels := frame_np_float.shape[0]) in (1, 2), f"Expected 1 or 2 channels, got {channels}"
                is_mono = channels == 1
                stream.channels = channels
                stream.layout = "mono" if is_mono else "stereo"
                stream.time_base = fractions.Fraction(1, sample_rate)
                is_first_frame = False

            out_fmt = "s16" if is_mono else "s16p"

            frame_np = (frame_np_float * 2**15).astype(np.int16)
            # frame_np = frame_np_float.astype(np.float32)

            frame_np = frame_np.reshape(-1, stream.channels).T.copy(order="C")

            frame_av = av.AudioFrame.from_ndarray(frame_np, layout=stream.layout.name, format=out_fmt)
            frame_av.rate = sample_rate
            frame_av.time_base = stream.time_base
            frame_av.pts = None

            for packet in stream.encode(frame_av):
                container.mux(packet)

        for packet in stream.encode():
            container.mux(packet)


def write_audio_ffmpeg(
    itr: Iterator[np.ndarray | Tensor],
    out_file: str | Path,
    sample_rate: int,
) -> None:
    """Function that writes a stream of audio to a file using FFMPEG.

    Args:
        itr: Iterator of audio chunks.
        out_file: Path to the output file.
        sample_rate: Sampling rate of the audio.
    """
    first_frame = _cleanup_wav_chunk(as_numpy_array(next(itr)))
    assert (channels := first_frame.shape[0]) in (1, 2), f"Expected 1 or 2 channels, got {channels}"

    try:
        import ffmpeg
    except ModuleNotFoundError as e:
        raise ModuleNotFoundError("Install FFMPEG to use this function: `pip install ffmpeg-python`") from e

    stream = ffmpeg.input("pipe:", format="f32le", acodec="pcm_f32le", ar=sample_rate, ac=channels)
    stream = ffmpeg.output(stream, str(out_file))
    stream = ffmpeg.overwrite_output(stream)
    stream = ffmpeg.run_async(stream, pipe_stdin=True, quiet=True)

    def get_bytes(frame: np.ndarray) -> bytes:
        return frame.tobytes()

    stream.stdin.write(get_bytes(first_frame))
    for frame in itr:
        frame = _cleanup_wav_chunk(as_numpy_array(frame))
        stream.stdin.write(get_bytes(frame))

    stream.stdin.close()
    stream.wait()


def get_audio_props(in_file: str | Path, *, reader: Reader | None = None) -> AudioProps:
    if reader is None:
        reader = _DefaultReaderSingleton.reader

    if reader == "ffmpeg":
        if not shutil.which("ffmpeg"):
            warnings.warn("FFMPEG is not available in this system.")
            reader = "av"
        else:
            return AudioProps.from_file_ffmpeg(in_file)

    if reader == "sf":
        return AudioProps.from_file_sf(in_file)

    if reader == "av":
        return AudioProps.from_file_av(in_file)

    raise ValueError(f"Unknown reader {reader}")


def rechunk_audio(
    audio_chunks: Iterator[np.ndarray],
    *,
    prefetch_n: int = 1,
    chunk_length: int | None = None,
    sample_rate: tuple[int, int] | None = None,
) -> Iterator[np.ndarray]:
    if chunk_length is None:
        yield from prefetch_samples(audio_chunks, prefetch_n)
        return

    audio_chunk_list: list[np.ndarray] = []
    total_length: int = 0
    for chunk in prefetch_samples(audio_chunks, prefetch_n):
        if sample_rate is not None and sample_rate[0] != sample_rate[1]:
            chunk = A.resample(torch.from_numpy(chunk), sample_rate[0], sample_rate[1]).numpy()
        cur_chunk_length = chunk.shape[-1]
        while total_length + cur_chunk_length >= chunk_length:
            yield np.concatenate(audio_chunk_list + [chunk[..., : chunk_length - total_length]], axis=-1)
            chunk = chunk[..., chunk_length - total_length :]
            audio_chunk_list = []
            total_length = 0
            cur_chunk_length = chunk.shape[-1]
        if cur_chunk_length > 0:
            audio_chunk_list.append(chunk)
            total_length += cur_chunk_length

    if audio_chunk_list:
        yield np.concatenate(audio_chunk_list, axis=-1)


def read_audio(
    in_file: str | Path,
    *,
    blocksize: int = DEFAULT_BLOCKSIZE,
    prefetch_n: int = 1,
    chunk_length: int | None = None,
    sample_rate: int | None = None,
    reader: Reader | None = None,
) -> Iterator[np.ndarray]:
    """Function that reads a stream of audio from a file.

    The output audio is in ``float32`` format.

    Args:
        in_file: Path to the input file.
        blocksize: Number of samples to read at a time.
        prefetch_n: Number of chunks to prefetch.
        chunk_length: Size of the chunks to read. If ``None``, will iterate
            whatever chunk size the underlying reader uses. Otherwise, samples
            will be rechunked to the desired size.
        sample_rate: Sampling rate to resample the audio to. If ``None``,
            will use the sampling rate of the input audio.
        reader: Reader to use. Can be either ``sf``, ``ffmpeg`` or ``av``.

    Returns:
        Iterator over numpy arrays, with shape ``(n_channels, n_samples)``.
    """
    if reader is None:
        reader = _DefaultReaderSingleton.reader

    if reader == "ffmpeg":
        if not shutil.which("ffmpeg"):
            warnings.warn("FFMPEG is not available in this system.")
            reader = "av"
        else:
            sr = None if sample_rate is None else (AudioProps.from_file_ffmpeg(in_file).sample_rate, sample_rate)
            return rechunk_audio(
                read_audio_ffmpeg(in_file, chunk_size=blocksize),
                prefetch_n=prefetch_n,
                chunk_length=chunk_length,
                sample_rate=sr,
            )

    if reader == "sf":
        sr = None if sample_rate is None else (AudioProps.from_file_sf(in_file).sample_rate, sample_rate)
        return rechunk_audio(
            read_audio_sf(in_file, blocksize=blocksize),
            prefetch_n=prefetch_n,
            chunk_length=chunk_length,
            sample_rate=sr,
        )

    if reader == "av":
        sr = None if sample_rate is None else (AudioProps.from_file_av(in_file).sample_rate, sample_rate)
        return rechunk_audio(
            read_audio_av(in_file),
            prefetch_n=prefetch_n,
            chunk_length=chunk_length,
            sample_rate=sr,
        )

    raise ValueError(f"Unknown reader {reader}")


def write_audio(
    itr: Iterator[np.ndarray | Tensor],
    out_file: str | Path,
    sample_rate: int,
    *,
    writer: Writer | None = None,
) -> None:
    """Function that writes a stream of audio to a file.

    Args:
        itr: Iterator of audio chunks.
        out_file: Path to the output file.
        sample_rate: Sample rate of the audio.
        writer: Writer to use. Can be either ``sf``, ``ffmpeg``, ``av``.
    """
    if writer is None:
        writer = _DefaultWriterSingleton.writer

    if writer == "ffmpeg":
        if not shutil.which("ffmpeg"):
            warnings.warn("FFMPEG is not available in this system.")
            writer = "av"
        else:
            write_audio_ffmpeg(itr, out_file, sample_rate)
            return

    if writer == "sf":
        write_audio_sf(itr, out_file, sample_rate)
        return

    if writer == "av":
        write_audio_av(itr, out_file, sample_rate)
        return

    raise ValueError(f"Unknown writer {writer}")


def read_audio_random_order(
    in_file: str | Path,
    chunk_length: int,
    *,
    sample_rate: int | None = None,
    include_last: bool = False,
) -> Iterator[np.ndarray]:
    """Function that reads a stream of audio from a file in random order.

    This is similar to ``read_audio``, but it yields chunks in random order,
    which can be useful for training purposes.

    Args:
        in_file: Path to the input file.
        chunk_length: Size of the chunks to read.
        sample_rate: Sampling rate to resample the audio to. If ``None``,
            will use the sampling rate of the input audio.
        include_last: Whether to include the last chunk, even if it's smaller
            than ``chunk_length``.

    Yields:
        Audio chunks as arrays, with shape ``(n_channels, chunk_length)``.
    """
    with sf.SoundFile(str(in_file), mode="r") as f:
        num_frames = len(f)
        if sample_rate is not None:
            chunk_length = round(chunk_length * f.samplerate / sample_rate)
        chunk_starts = list(range(0, num_frames, chunk_length))
        if not include_last and num_frames - chunk_starts[-1] < chunk_length:
            chunk_starts = chunk_starts[:-1]
        random.shuffle(chunk_starts)
        for chunk_start in chunk_starts:
            f.seek(chunk_start)
            chunk = f.read(chunk_length, dtype="float32", always_2d=True).T
            if sample_rate is not None and sample_rate != f.samplerate:
                chunk = A.resample(torch.from_numpy(chunk), f.samplerate, sample_rate).numpy()
            yield chunk


def get_file_info(fpath: Path) -> AudioFile | None:
    if fpath.suffix.lower() not in AUDIO_FILE_EXTENSIONS:
        return None

    fpath = Path(fpath)

    try:
        props = get_audio_props(fpath)
        num_frames = props.num_frames
        sample_rate = props.sample_rate
        channels = props.channels

    except Exception:
        logger.exception("Could not get info for %s", fpath)
        return None

    return AudioFile(
        path=fpath,
        props=AudioProps(
            sample_rate=sample_rate,
            channels=channels,
            num_frames=num_frames,
        ),
    )


def get_files_cached(root_dir: Path, processes: int = 16) -> list[AudioFile]:
    """Gets all audio files in the given directory.

    Args:
        root_dir: The root directory.
        extensions: The file extensions to look for.
        processes: The number of processes to use.

    Returns:
        A list of files (relative to the root directory).
    """
    cache_path = (root_dir / ".audio_files_cache").resolve()

    if cache_path.exists():
        with Timer("reading cached audio files", spinner=True), open(cache_path, "r", encoding="utf-8") as f:
            return [AudioFile.parse(line) for line in f]

    logger.info("Caching audio files to %s", cache_path)
    audio_files: list[AudioFile] = []

    with Timer("listing files", spinner=True):
        files = [f for f in root_dir.rglob("*.*") if f.suffix.lower() in AUDIO_FILE_EXTENSIONS]
        assert files, f"No files found in {root_dir}!"

    with mp.Pool(processes=processes) as pool, tqdm.tqdm(total=len(files)) as pbar:
        for audio_file in pool.imap_unordered(get_file_info, files):
            pbar.update()
            if audio_file is None:
                continue
            audio_file.path = audio_file.path.relative_to(root_dir)
            audio_files.append(audio_file)

    with Timer("writing cached audio files", spinner=True), open(cache_path, "w", encoding="utf-8") as f:
        for audio_file in audio_files:
            f.write(f"{audio_file}\n")

    return audio_files


class AudioFolderFilesDataset(Dataset[tuple[AudioFile, Path]]):
    def __init__(
        self,
        root_dir: str | Path,
        min_frames_quantile: float = 0.01,
        max_frames_quantile: float = 0.99,
    ) -> None:
        super().__init__()

        self.root_dir = Path(root_dir).resolve()
        files = [f for f in get_files_cached(self.root_dir)]
        lengths = torch.tensor([f.props.num_frames / f.props.sample_rate for f in files])
        min_length = lengths.quantile(min_frames_quantile)
        max_length = lengths.quantile(max_frames_quantile)
        self.files = [f for i, f in enumerate(files) if lengths[i] >= min_length and lengths[i] <= max_length]

    def __getitem__(self, index: int) -> tuple[AudioFile, Path]:
        return self.files[index], self.root_dir

    def __len__(self) -> int:
        return len(self.files)


class AudioFoldersFilesDataset(ConcatDataset[tuple[AudioFile, Path]]):
    """Defines a dataset for reading audio files from a list of folders.

    This dataset just indexes the audio files in some given directories and
    returns some information about them. It is a good idea to use this dataset
    with downstream datasets which further process the files.

    Parameters:
        root_dirs: List of root directories to search for audio files. If not
            provided, will default to the AUDIO_FOLDERS environment variable,
            which should be a colon-separated list of directories.
    """

    def __init__(self, root_dirs: Sequence[str | Path] | None = None) -> None:
        if root_dirs is None:
            root_dirs = [f for f in os.environ["AUDIO_FOLDERS"].split(":") if f]
        super().__init__([AudioFolderFilesDataset(root_dir) for root_dir in root_dirs])


class AudioFileDataset(IterableDataset[Tensor]):
    def __init__(
        self,
        audio_file: Path,
        sample_rate: int,
        length_ms: float,
        num_samples_per_clip: int = 1,
        max_iters: int | None = None,
    ) -> None:
        super().__init__()

        self.audio_file = audio_file
        self.sample_rate = sample_rate
        self.current_audio: list[Tensor] | None = None
        self.chunk_frames = round(sample_rate * length_ms / 1000)
        self.num_samples_per_clip = num_samples_per_clip
        self.max_iters = max_iters
        self.audio_iter: Iterator[np.ndarray] | None = None
        self.channel_idx: int | None = None
        self.current_chunk = 0
        self.samples_queue: Deque[Tensor] = deque()

    def _get_next_audio(self) -> Tensor:
        assert self.audio_iter is not None, "Must call __iter__ first!"

        audio_np = next(self.audio_iter)  # (num_channels, num_frames)
        assert (audio := torch.from_numpy(audio_np)).dim() == 2

        if (num_channels := audio.shape[0]) != 1:
            if self.channel_idx is None:
                self.channel_idx = random.randint(0, num_channels - 1)
            audio = audio[self.channel_idx : self.channel_idx + 1]

        # Dummy check on the final audio shape.
        if audio.shape != (1, self.chunk_frames):
            raise StopIteration

        return audio

    def __iter__(self) -> Iterator[Tensor]:
        self.audio_iter = read_audio_random_order(
            in_file=self.audio_file,
            chunk_length=self.chunk_frames,
            sample_rate=self.sample_rate,
        )

        # Adds N - 1 samples to the sample queue.
        self.samples_queue.clear()
        for _ in range(max(self.num_samples_per_clip - 1, 0)):
            try:
                self.samples_queue.append(self._get_next_audio())
            except Exception:
                break

        self.channel_idx = None
        self.current_chunk = 0
        return self

    def __next__(self) -> Tensor:
        if self.max_iters is not None and self.current_chunk > self.max_iters:
            raise StopIteration
        assert len(self.samples_queue) == self.num_samples_per_clip - 1
        audio = self._get_next_audio()
        self.current_chunk += 1

        # Concatenates the current sample with the previous ones.
        self.samples_queue.append(audio)
        if self.num_samples_per_clip > 1:
            audio = torch.stack(list(self.samples_queue), dim=0)
        self.samples_queue.popleft()

        return audio


class AudioFoldersDataset(IterableDataset[Tensor]):
    """Defines a dataset for iterating through audio samples.

    This iterator first indexes all of the audio files in any of the given
    ``root_dirs``, getting their properties according to the structure above.

    It then puts ``num_simultaneous`` audio files into a round-robin queue. It
    iterates through each file in the list, yielding one sample, up to at most
    ``max_iters`` samples per file. If the file is exhausted, it is replaced
    with a new file. This iterator continues until ``max_iters`` samples have
    been drawn from every file in the dataset.

    Additionally, we actually draw ``num_samples_per_clip`` samples from each
    audio file and stack them together. Each file is resampled to
    ``sample_rate`` and will have ``length_ms`` milliseconds of audio,
    resulting in a tensor with shape ``(num_samples_per_clip,
    sample_rate * length_ms / 1000, num_channels)``.

    Parameters:
        root_dirs: The root directories to search for audio files.
        sample_rate: The sampling rate to resample the audio to.
        length_ms: The length of the audio clips in milliseconds.
        num_samples_per_clip: The number of samples to take from each audio clip.
        num_simultaneous: The number of audio files to load into memory at once.
        max_iters: Maximum number of samples to draw from each clip.
    """

    def __init__(
        self,
        root_dirs: Sequence[str | Path],
        sample_rate: int,
        length_ms: float,
        num_simultaneous: int,
        num_samples_per_clip: int = 1,
        max_iters: int | None = None,
    ) -> None:
        super().__init__()

        self.files_ds = AudioFoldersFilesDataset(root_dirs)
        self.audio_ds_queue: Deque[tuple[int, Iterator[Tensor]]] = deque()

        # Parameters for child dataset.
        self.sample_rate = sample_rate
        self.length_ms = length_ms
        self.num_samples_per_clip = num_samples_per_clip
        self.max_iters = max_iters

        # Keeps track of which indices to sample from.
        self.indices = list(range(len(self.files_ds)))
        self.num_simultaneous = num_simultaneous

    def _get_audio_ds(self, index: int) -> tuple[int, Iterator[Tensor]]:
        audio_file, root_dir = self.files_ds[index]
        ds = AudioFileDataset(
            audio_file=root_dir / audio_file.path,
            sample_rate=self.sample_rate,
            length_ms=self.length_ms,
            num_samples_per_clip=self.num_samples_per_clip,
            max_iters=self.max_iters,
        )
        return index, iter(ds)

    def __iter__(self) -> Iterator[Tensor]:
        winfo = get_worker_info()
        world_size = winfo.num_workers * get_world_size()

        # Shuffles the indices and splits them across workers.
        self.indices = list(range(len(self.files_ds)))[winfo.worker_id :: world_size]
        random.shuffle(self.indices)

        # Creates the audio datasets for the first `num_simultaneous` indices.
        self.audio_ds_queue.clear()
        self.audio_ds_queue.extend((self._get_audio_ds(i) for i in self.indices[: self.num_simultaneous]))
        self.indices = self.indices[self.num_simultaneous :]

        return self

    def __next__(self) -> Tensor:
        index, audio_ds = self.audio_ds_queue.popleft()
        try:
            next_sample = next(audio_ds)
            self.audio_ds_queue.append((index, audio_ds))
            return next_sample
        except StopIteration:
            if len(self.indices) == 0:
                raise StopIteration
            next_index = self.indices.pop()
            self.audio_ds_queue.append(self._get_audio_ds(next_index))
            return next(self)
        except Exception:
            logger.exception("Error for index %d", index)
            next_index = self.indices.pop()
            self.audio_ds_queue.append(self._get_audio_ds(next_index))
            return next(self)
