"""Core logic for scanning directories and formatting file sizes."""

from __future__ import annotations

from pathlib import Path

from large_files.models import FileEntry

_UNITS: list[tuple[str, int]] = [
    ("TB", 1 << 40),
    ("GB", 1 << 30),
    ("MB", 1 << 20),
    ("KB", 1 << 10),
    ("B", 1),
]


def format_size(size_bytes: int, human: bool = False) -> str:
    """Format a byte count as a human-readable string or plain integer.

    Args:
        size_bytes: The size in bytes. Must be non-negative.
        human: If True, convert to the largest appropriate unit (B/KB/MB/GB/TB)
               with one decimal place. If False, return the plain integer string.

    Returns:
        A formatted size string.

    Raises:
        ValueError: If size_bytes is negative.
    """
    if size_bytes < 0:
        raise ValueError("size_bytes must be non-negative")

    if not human:
        return str(size_bytes)

    for unit, threshold in _UNITS:
        if size_bytes >= threshold:
            value = size_bytes / threshold
            return f"{value:.1f} {unit}"

    return "0 B"


def scan_directory(path: str, top_n: int = 10) -> list[FileEntry]:
    """Scan *path* for regular files and return the *top_n* largest.

    Directories are skipped. Permission errors are silently ignored.
    The result is sorted by size descending.

    Args:
        path: Directory path to scan (recursively).
        top_n: Maximum number of entries to return. Must be non-negative.

    Returns:
        A list of :class:`FileEntry` sorted by size descending.

    Raises:
        FileNotFoundError: If *path* does not exist.
        NotADirectoryError: If *path* exists but is not a directory.
        ValueError: If *top_n* is negative.
    """
    if top_n < 0:
        raise ValueError("top_n must be non-negative")

    try:
        root = Path(path).resolve()
    except (RuntimeError, OSError):
        raise FileNotFoundError(f"Path does not exist or is inaccessible: {path}")

    if not root.exists():
        raise FileNotFoundError(f"Path does not exist: {path}")
    if not root.is_dir():
        raise NotADirectoryError(f"Path is not a directory: {path}")

    entries: list[FileEntry] = []

    try:
        for item in root.rglob("*"):
            try:
                if not item.is_file():
                    continue
                size = item.stat().st_size
                entries.append(FileEntry(path=str(item), size_bytes=size))
            except OSError:
                # Permission denied or other OS-level error — skip silently.
                continue
    except RuntimeError:
        # Raised when a symlink cycle is detected during rglob traversal.
        pass

    entries.sort(key=lambda entry: entry.size_bytes, reverse=True)
    return entries[:top_n]
