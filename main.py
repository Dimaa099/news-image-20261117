#!/usr/bin/env python3
"""Deliver the news-image-20261117 entry image to the output directory.

The collage for Tuesday 17 November 2026 is stored in this repository as
``image.jpg`` (a 1024x1024 JPEG, 238218 bytes). The competition judges the
bytes of ``entry.png``, and it reads a PNG or a JPEG by the file's first
bytes, so this program simply places the stored image at
``$MAKEFUN_OUTPUT_DIR/entry.png``.

No network, no randomness, no installed packages: the standard library
alone, so a second run in a fresh container writes the same bytes.
"""

import shutil
import sys
from os import environ
from pathlib import Path

BUNDLED_IMAGE = Path(__file__).resolve().parent / "image.jpg"


def destination() -> Path:
    """Where the entry goes: $MAKEFUN_OUTPUT_DIR, else /output."""
    return Path(environ.get("MAKEFUN_OUTPUT_DIR") or "/output") / "entry.png"


def main() -> int:
    target = destination()
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(BUNDLED_IMAGE, target)
    if target.stat().st_size != BUNDLED_IMAGE.stat().st_size:
        print("entry.png does not match image.jpg", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
