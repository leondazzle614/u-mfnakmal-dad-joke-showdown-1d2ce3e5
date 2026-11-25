#!/usr/bin/env python3
"""Dad Joke Showdown -- one original dad joke, written deterministically.

A Python 3.13 standard-library-only program. Running it writes the entry's
single dad joke to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
No network, no clock, no randomness: two runs write identical bytes.

The joke: a dad, a son, and a date -- the fruit kind.
"""

import os

JOKE = (
    "I told my son I'd take him out on a date. "
    "He said, 'Dad, I'm twelve.' "
    "I said, 'Relax \u2014 I meant the fruit. We're having dates for dinner.'"
)


def main() -> int:
    if not 1 <= len(JOKE) <= 200 or not JOKE.strip():
        raise ValueError(
            f"entry must be 1-200 non-whitespace characters, got {len(JOKE)}"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    print(JOKE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
