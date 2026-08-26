"""Tests for the large_files package."""

from __future__ import annotations

import os
from pathlib import Path

import pytest

from large_files.cli import main
from large_files.models import FileEntry
from large_files.service import format_size, scan_directory

# ---------------------------------------------------------------------------
# format_size
# ---------------------------------------------------------------------------


class TestFormatSize:
    def test_plain_small(self) -> None:
        assert format_size(42) == "42"

    def test_plain_zero(self) -> None:
        assert format_size(0) == "0"

    def test_plain_large(self) -> None:
        assert format_size(1_000_000) == "1000000"

    def test_human_bytes(self) -> None:
        assert format_size(500, human=True) == "500.0 B"

    def test_human_kilobytes(self) -> None:
        assert format_size(1_500, human=True) == "1.5 KB"

    def test_human_megabytes(self) -> None:
        assert format_size(2_500_000, human=True) == "2.4 MB"

    def test_human_gigabytes(self) -> None:
        assert format_size(2_500_000_000, human=True) == "2.3 GB"

    def test_human_terabytes(self) -> None:
        assert format_size(5_000_000_000_000, human=True) == "4.5 TB"

    def test_human_exact_threshold(self) -> None:
        assert format_size(1024, human=True) == "1.0 KB"

    def test_human_above_threshold(self) -> None:
        assert format_size(1536, human=True) == "1.5 KB"


# ---------------------------------------------------------------------------
# scan_directory
# ---------------------------------------------------------------------------


class TestScanDirectory:
    def test_empty_directory(self, tmp_path: Path) -> None:
        result = scan_directory(str(tmp_path))
        assert result == []

    def test_top_n_limit(self, tmp_path: Path) -> None:
        for i in range(20):
            (tmp_path / f"file_{i}.txt").write_bytes(b"x" * (i + 1))
        result = scan_directory(str(tmp_path), top_n=5)
        assert len(result) == 5

    def test_sorted_descending(self, tmp_path: Path) -> None:
        (tmp_path / "small.txt").write_bytes(b"a")
        (tmp_path / "large.txt").write_bytes(b"b" * 100)
        result = scan_directory(str(tmp_path))
        assert result[0].size_bytes == 100
        assert result[1].size_bytes == 1

    def test_returns_file_entry(self, tmp_path: Path) -> None:
        f = tmp_path / "hello.txt"
        f.write_bytes(b"hello")
        result = scan_directory(str(tmp_path))
        assert len(result) == 1
        assert isinstance(result[0], FileEntry)
        assert result[0].size_bytes == 5
        assert result[0].path == str(f)

    def test_recurses_into_subdirectories(self, tmp_path: Path) -> None:
        sub = tmp_path / "sub"
        sub.mkdir()
        (sub / "inside.txt").write_bytes(b"data")
        (tmp_path / "root.txt").write_bytes(b"root")
        result = scan_directory(str(tmp_path))
        assert len(result) == 2
        paths = {e.path for e in result}
        assert str(tmp_path / "root.txt") in paths
        assert str(sub / "inside.txt") in paths

    def test_nonexistent_path(self) -> None:
        with pytest.raises(FileNotFoundError):
            scan_directory("/nonexistent/path/12345")

    def test_file_instead_of_directory(self, tmp_path: Path) -> None:
        f = tmp_path / "not_a_dir.txt"
        f.write_bytes(b"x")
        with pytest.raises(NotADirectoryError):
            scan_directory(str(f))

    def test_skips_permission_denied(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Files that raise PermissionError on stat are silently skipped."""

        class _FakeStat:
            def __init__(self, size: int) -> None:
                self.st_size = size

        original_stat = os.stat

        def fake_stat(path: str, *args: object, **kwargs: object) -> _FakeStat:
            path_str = str(path)
            if "forbidden" in path_str:
                raise PermissionError("access denied")
            return original_stat(path)

        monkeypatch.setattr(os, "stat", fake_stat)

        (tmp_path / "ok.txt").write_bytes(b"ok")
        (tmp_path / "forbidden.txt").write_bytes(b"forbidden")

        result = scan_directory(str(tmp_path))
        assert len(result) == 1
        assert result[0].path.endswith("ok.txt")

    def test_default_top_n_is_ten(self, tmp_path: Path) -> None:
        for i in range(15):
            (tmp_path / f"f{i}.txt").write_bytes(b"x" * (i + 1))
        result = scan_directory(str(tmp_path))
        assert len(result) == 10

    def test_top_n_zero_returns_empty(self, tmp_path: Path) -> None:
        (tmp_path / "file.txt").write_bytes(b"data")
        result = scan_directory(str(tmp_path), top_n=0)
        assert result == []

    def test_negative_top_n_raises(self, tmp_path: Path) -> None:
        with pytest.raises(ValueError, match="top_n must be non-negative"):
            scan_directory(str(tmp_path), top_n=-1)

    def test_top_n_larger_than_files(self, tmp_path: Path) -> None:
        for i in range(5):
            (tmp_path / f"f{i}.txt").write_bytes(b"x" * (i + 1))
        result = scan_directory(str(tmp_path), top_n=100)
        assert len(result) == 5

    def test_zero_byte_file_included(self, tmp_path: Path) -> None:
        (tmp_path / "empty.txt").write_bytes(b"")
        (tmp_path / "nonempty.txt").write_bytes(b"x")
        result = scan_directory(str(tmp_path))
        assert len(result) == 2
        # Non-empty should be first (larger)
        assert result[0].size_bytes == 1
        assert result[1].size_bytes == 0


# ---------------------------------------------------------------------------
# format_size — additional edge-case tests
# ---------------------------------------------------------------------------


class TestFormatSizeEdgeCases:
    def test_human_zero(self) -> None:
        assert format_size(0, human=True) == "0 B"

    def test_human_exact_tb_threshold(self) -> None:
        assert format_size(1 << 40, human=True) == "1.0 TB"

    def test_negative_raises(self) -> None:
        with pytest.raises(ValueError, match="non-negative"):
            format_size(-1, human=True)


# ---------------------------------------------------------------------------
# CLI integration tests
# ---------------------------------------------------------------------------


class TestCliMain:
    def test_returns_results(self, tmp_path: Path) -> None:
        (tmp_path / "big.txt").write_bytes(b"x" * 500)
        (tmp_path / "small.txt").write_bytes(b"y")
        exit_code = main([str(tmp_path), "-n", "1"])
        assert exit_code == 0

    def test_human_flag(self, tmp_path: Path, capsys) -> None:
        (tmp_path / "file.txt").write_bytes(b"x" * 1024)
        main([str(tmp_path), "--human"])
        captured = capsys.readouterr()
        assert "1.0 KB" in captured.out

    def test_nonexistent_path_returns_error(self, tmp_path: Path, capsys) -> None:
        exit_code = main(["/nonexistent/path/12345"])
        assert exit_code == 1
        captured = capsys.readouterr()
        assert "Error" in captured.err

    def test_no_files_returns_zero(self, tmp_path: Path, capsys) -> None:
        exit_code = main([str(tmp_path)])
        assert exit_code == 0
        captured = capsys.readouterr()
        assert "No files found" in captured.out
