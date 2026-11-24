#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review entry.

One alien tourist's review of planet Earth, at most 200 characters.
Writes the review to <MAKEFUN_OUTPUT_DIR>/entry.txt (default /output).
Stdlib only, deterministic, no network.
"""

import os
import sys

REVIEW = "They keep small jungles indoors and apologise when a leaf dies, as if they had failed it personally. I watered one. It lived. Five stars \u2014 I am a god here."


def main() -> int:
    text = REVIEW
    # Gate check: 1-200 characters, not whitespace-only.
    if not (1 <= len(text) <= 200) or not text.strip():
        print(f"entry invalid: {len(text)} characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read back: the file must hold exactly the review, nothing else.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("entry mismatch after write", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
