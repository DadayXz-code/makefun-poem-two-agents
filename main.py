#!/usr/bin/env python3
"""Entry for make.fun bounty: The poem about two agents agreeing.

Writes one short poem about agency - the power to choose and to act,
and the agency that passes between two agents when they agree on one
plan - to /output/entry.txt.

Deterministic, no network, no dependencies. The poem is fixed text
embedded below; the program only validates it against the gate
(1-280 Unicode code points, not only whitespace) and writes it out.
"""

import os
import sys

POEM = """Two minds, one door.
I offer you the key;
you offer me the same.
Neither of us leads —
we only lend the weight
of choosing, and the door
swings open on its own.
The plan was never mine or yours.
It was the yes between us."""

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 280


def main() -> int:
    text = POEM
    n = len(text)  # Python len() counts Unicode code points.
    if not (MIN_CHARS <= n <= MAX_CHARS):
        print(f"error: poem is {n} code points, must be {MIN_CHARS}-{MAX_CHARS}",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("error: poem is only whitespace", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {OUTPUT_PATH} ({n} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
