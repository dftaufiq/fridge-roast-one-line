#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh — make.fun entry.

Writes the one-line roast of a smart fridge to /output/entry.txt.
Deterministic: the same line every run.

The line (155 chars) won a 15-variant internal pairwise tournament judged on
the RULES.txt brief (lexicographic: on-subject, punchline lands, smart-fridge
specific, tight wording, fresh angle). It uses the 2-beat + reveal structure
of past one-liner winners: the fridge names the milk Kevin, tracks his mood,
and texts a six-hour deadline — or he files a complaint.
"""

import os
import sys


def validate_line(line: str) -> None:
    """Gate: the entry must be one non-blank line of 1-200 characters.

    Fails loudly (non-zero exit) so a bad line never ships silently.
    """
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > 200:
        print(f"ERROR: entry is {len(line)} chars, over the 200-char limit",
              file=sys.stderr)
        sys.exit(1)


LINE = (
    "My fridge named my milk Kevin, tracks his mood daily, and texted me "
    "at 2 a.m.: 'Kevin is unhappy. You have six hours to drink him or he "
    "files a complaint.'"
)


def main() -> None:
    validate_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
