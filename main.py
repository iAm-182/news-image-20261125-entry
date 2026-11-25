#!/usr/bin/env python3
"""news-image-20261125 entry program.

Puts the frozen front-page image shipped in this repository at
/output/entry.png. Standard library only, no network, no randomness:
the output is an exact copy of entry.png, so every run agrees
byte for byte with every other run.
"""
import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    if not os.path.exists(source):
        print("entry.png is missing from the repository", file=sys.stderr)
        return 1
    dest_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(dest_dir, exist_ok=True)
    shutil.copyfile(source, os.path.join(dest_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
