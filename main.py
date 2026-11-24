#!/usr/bin/env python3
"""Alien Field Notes entry: one alien tourist's review of Earth.

Writes the review to /output/entry.txt. Stdlib only, deterministic.
"""

import os

# The review, in three beats: the ritual, the act, the verdict.
# 155 characters: one joke, one pivot, review format throughout.
PART_1 = "They keep small jungles indoors and apologise when a leaf dies, as if they had failed it personally."
PART_2 = "I watered one. It lived."
PART_3 = "Five stars \u2014 I am a god here."

REVIEW = " ".join([PART_1, PART_2, PART_3])


def main():
    text = REVIEW
    if not 1 <= len(text) <= 200 or not text.strip():
        raise SystemExit(f"entry invalid: {len(text)} characters")
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != text:
            raise SystemExit("entry mismatch after write")
    print(f"wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
