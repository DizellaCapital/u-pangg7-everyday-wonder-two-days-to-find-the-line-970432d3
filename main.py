#!/usr/bin/env python3
"""Everyday Wonder entry: write one sentence to /output/entry.txt.

The sentence catches a small everyday moment -- a lift ride at dawn --
and turns it strange: the song outlives the singer, kept by the mirrors.
"""
import os

SENTENCE = (
    "At 6:12 a.m. in the lift, Mrs. Hartono hummed a song I had never "
    "heard, and the mirrored doors kept singing it after she stepped out."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
