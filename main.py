#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest (make.fun).

Writes the entry -- one short rant about a small everyday annoyance --
to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = 'The office printer has one job, and it performs it with the enthusiasm of a cat being asked to fetch. It jams on page one, blinks a light no manual has ever explained, and then — only once the deadline has passed — prints all seventeen copies at once, warm, smug, and completely useless.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
