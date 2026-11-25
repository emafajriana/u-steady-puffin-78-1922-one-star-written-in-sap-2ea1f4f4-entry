#!/usr/bin/env python3
"""One Star, Written in Sap — make.fun entry.

Writes a single-line one-star review, in the voice of a houseplant
reviewing its human owner, to entry.txt.
Stdlib only: the grader runs python3 -P -s in stock python:3.13-slim.
"""

import os
from pathlib import Path

ENTRY = (
    "One star. He moved me to the 'better light' — a shelf above the "
    "radiator — and now I spend my days photosynthesizing regret."
)


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    text = ENTRY.strip()
    # Gate per RULES.txt: UTF-8 text, 1-279 chars, not only whitespace,
    # a single line.
    assert text, "entry is empty"
    assert 1 <= len(text) <= 279, f"entry length {len(text)} out of gate"
    assert "\n" not in text, "entry must be a single line"
    target.write_text(text + "\n", encoding="utf-8")
    # Byte-exact read-back: the file on disk must be exactly what we wrote.
    written = target.read_bytes()
    assert written == (text + "\n").encode("utf-8"), "read-back mismatch"
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
