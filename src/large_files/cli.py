"""Command-line interface for find-large-files."""

from __future__ import annotations

import argparse
import sys

from large_files.service import format_size, scan_directory


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="find-large-files",
        description="Scan a directory and display the largest files.",
    )
    parser.add_argument("path", help="Directory to scan")
    parser.add_argument(
        "-n",
        type=int,
        default=10,
        help="Number of top files to show (default: 10)",
    )
    parser.add_argument(
        "--human",
        action="store_true",
        help="Print sizes in human-readable format (B/KB/MB/GB/TB)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Entry point for the CLI.

    Returns:
        Exit code (0 for success, non-zero for errors).
    """
    parser = _build_parser()
    args = parser.parse_args(argv)

    try:
        entries = scan_directory(args.path, top_n=args.n)
    except (FileNotFoundError, NotADirectoryError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if not entries:
        print("No files found.")
        return 0

    human = args.human
    if human:
        header = f"{'排名':<6} {'大小':<12} 路径"
        size_col_width = 12
    else:
        header = f"{'排名':<6} {'大小(字节)':<20} 路径"
        size_col_width = 20

    print(header)

    for rank, entry in enumerate(entries, start=1):
        size_str = format_size(entry.size_bytes, human=human)
        print(f"{rank:<6} {size_str:<{size_col_width}} {entry.path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
