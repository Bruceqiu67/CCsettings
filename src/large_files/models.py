"""Data models for the large_files package."""

from dataclasses import dataclass


@dataclass(frozen=True)
class FileEntry:
    """Represents a single file discovered during a scan."""

    path: str
    size_bytes: int
