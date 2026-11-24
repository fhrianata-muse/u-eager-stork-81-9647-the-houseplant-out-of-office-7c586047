#!/usr/bin/env python3
"""The Houseplant Out-of-Office - a one-line out-of-office entry for make.fun.

The line is stored as data. At run time the program checks the judge's
gate itself before writing anything: the text must be one single line,
1 to 120 characters, and not only white space. Only then is it written
to /output/entry.txt.
"""
from pathlib import Path

ENTRY = "Out of office: my roots have grown through the keyboard. Your email is now fertiliser. I will reply when I flower."

MIN_CHARS = 1
MAX_CHARS = 120


def render():
    if "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("entry must be one single line")
    if not MIN_CHARS <= len(ENTRY) <= MAX_CHARS:
        raise SystemExit(f"entry length out of range: {len(ENTRY)}")
    if not ENTRY.strip():
        raise SystemExit("entry must not be only white space")
    if ENTRY != ENTRY.strip():
        raise SystemExit("entry must not start or end with white space")
    # Criterion 4 of the judge's brief: the line must be complete on its
    # own, so it has to end on terminal punctuation, not trail off.
    if ENTRY[-1] not in ".!?":
        raise SystemExit("entry must end with terminal punctuation")
    return ENTRY + "\n"


def main():
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(), encoding="utf-8")


if __name__ == "__main__":
    main()
