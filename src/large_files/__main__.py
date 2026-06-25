"""Allow running the CLI via ``python -m large_files``."""

from __future__ import annotations

import sys

from large_files.cli import main

if __name__ == "__main__":
    sys.exit(main())
