#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — a make.fun one-line entry.

The program writes the entry text to /output/entry.txt, where the
competition's sealed scorer reads it.
"""

from pathlib import Path

ENTRY = "The office printer has one job, and it has chosen violence: it jams on page one, claims it is out of toner it had yesterday, and then prints my document in the middle of someone else's meeting notes."

OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    """Write the entry text to the output path."""
    text = ENTRY.strip()
    assert text, "entry text must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
