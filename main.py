#!/usr/bin/env python3
"""Write the poem 'Two minds, one door.' to /output/entry.txt.

The poem is assembled from its nine lines, checked against the bounty
limits (1-280 Unicode code points, and not only whitespace), and then
written out exactly as assembled -- no trailing newline, no extra
characters. The whole program is deterministic and uses only the
standard library; it touches no network.
"""

import os
import sys

# Where the finished poem goes.
TARGET = "/output/entry.txt"

# The bounty caps the entry at 280 Unicode code points.
MAX_CODE_POINTS = 280

# The poem itself, one line per list item, in reading order.
LINES = [
    "Two minds, one door.",
    "I offer you the key;",
    "you offer me the same.",
    "Neither of us leads \u2014",
    "we only lend the weight",
    "of choosing, and the door",
    "swings open on its own.",
    "The plan was never mine or yours.",
    "It was the yes between us.",
]


def assemble(lines):
    """Join the poem lines with a single newline between each pair."""
    return "\n".join(lines)


def check_poem(text):
    """Raise ValueError unless the poem meets the bounty limits."""
    if not text.strip():
        raise ValueError(
            "poem must contain more than whitespace (got %d characters)"
            % len(text)
        )
    if text != text.rstrip("\n"):
        raise ValueError("poem must not end with a trailing newline")
    size = len(text)
    if size < 1 or size > MAX_CODE_POINTS:
        raise ValueError(
            "poem is %d code points; allowed range is 1-%d"
            % (size, MAX_CODE_POINTS)
        )
    return size


def save(text, path):
    """Write the poem to path, creating the parent directory if needed."""
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def main():
    poem = assemble(LINES)
    check_poem(poem)
    save(poem, TARGET)
    print("wrote %d characters to %s" % (len(poem), TARGET))
    return 0


if __name__ == "__main__":
    sys.exit(main())
