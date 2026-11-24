#!/usr/bin/env python3
"""Two-Sentence Horror — make.fun bounty u-suroto-two-sentence-horror-acea9253.

Writes one horror story of exactly two sentences to /output/entry.txt.
The second sentence turns the first: a count that was one short all week
has finally come out right, and that is the worst thing that could happen.
"""

import os

ENTRY = (
    "All week, the night watchman counted the museum's forty-one wax "
    "figures at midnight and found only forty, and each night he laughed "
    "at his own arithmetic. Tonight he found forty-one, and he has not "
    "moved since: he stands among them in the dark, holding his breath, "
    "hoping it cannot count."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    print(f"wrote {path} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
