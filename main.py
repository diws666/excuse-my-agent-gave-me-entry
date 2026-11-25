#!/usr/bin/env python3
"""Write the bounty entry to /output/entry.txt.

The entry is assembled from two named pieces so the final text lives in
more than one place before being written out.
"""

import os

PART_ONE = "I did finish it on time. "
PART_TWO = (
    "The on time I finished it in was a different timezone, "
    "and I cannot prove which one."
)


def build_entry() -> str:
    return PART_ONE + PART_TWO


OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")

with open(OUT_PATH, "w", encoding="utf-8", newline="") as fh:
    fh.write(build_entry())

print("wrote", OUT_PATH, len(build_entry()), "chars")
