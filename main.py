#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes one sentence to ``entry.txt`` in the output directory
(``$MAKEFUN_OUTPUT_DIR``, default ``/output``) and prints exactly that
sentence to stdout, nothing else.

The sentence explains the modern internet to someone from 1800 using
only things they already know -- a post office, a road, light, towns
that talk -- and no word coined after their time.

Deterministic, offline, no input read.
"""

import os

ENTRY = (
    "Think of a post office that holds any letter, book, or song you ask "
    "for, and a road of light that brings it to your hand before you can "
    "blink, while all the towns of the world talk at once."
)

MAX_CHARS = 200


def validate(text: str) -> None:
    """The gate only accepts UTF-8 text of 1 to 200 characters, not only
    whitespace, as a single sentence. Fail loudly here instead of
    shipping an entry the judge never sees."""
    assert isinstance(text, str)
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} chars, must be 1-{MAX_CHARS}"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"


def main() -> None:
    validate(ENTRY)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
