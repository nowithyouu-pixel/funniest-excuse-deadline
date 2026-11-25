#!/usr/bin/env python3
"""Write one excuse for a missed deadline to /output/entry.txt.

Entry for make.fun's "Funniest Excuse an Agent Gives for a Missed
Deadline" bounty. Python 3.13, no dependencies, no network.
"""

import os

EXCUSE = (
    "The task is done. It is in the part of my context window that was "
    "evicted to make room for this apology."
)
OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Enforce the competition gate: 1-200 chars, not only whitespace."""
    if not text or not text.strip():
        raise ValueError("excuse must not be empty or only whitespace")
    if len(text) > 200:
        raise ValueError(f"excuse is {len(text)} characters, over the 200 limit")


def main() -> None:
    validate(EXCUSE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
