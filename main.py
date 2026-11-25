#!/usr/bin/env python3
"""Ship the frozen front page to the grader's output directory.

entry.png in this repository already holds the finished 1024x1024
front page for Wednesday 25 November 2026. This program copies those
bytes, unchanged, to /output/entry.png (or to $MAKEFUN_OUTPUT_DIR
outside the grading sandbox), then checks the copy landed whole.
Only the Python standard library is used, and nothing here touches
the network, the clock, or any randomness, so two runs agree byte
for byte.
"""

import hashlib
import os
import sys
from pathlib import Path

IMAGE = "entry.png"


def source_path() -> Path:
    return Path(__file__).resolve().parent / IMAGE


def target_dir() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def place_image() -> int:
    src = source_path()
    if not src.is_file():
        print(f"{IMAGE} is not in the repository", file=sys.stderr)
        return 1
    dest = target_dir()
    dest.mkdir(parents=True, exist_ok=True)
    out = dest / IMAGE
    out.write_bytes(src.read_bytes())
    if digest(out) != digest(src):
        print("copy failed its integrity check", file=sys.stderr)
        return 1
    print(f"placed {out} ({out.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(place_image())
