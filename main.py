#!/usr/bin/env python3
"""One-line office joke entry for make.fun.

Writes a single-line joke about office life to ``entry.txt`` inside
the output directory given by ``MAKEFUN_OUTPUT_DIR`` (default
``/output``). Deterministic, standard library only, no network access.

The joke: HR answers a question about work-life balance by doing the
most office thing possible - booking a meeting about it.
"""

import os

JOKE = (
    "I asked HR about work-life balance, so they booked me a "
    "30-minute meeting titled 'Balance'."
)


def validate(line: str) -> bytes:
    """Runtime validation: exactly one line, 1-200 chars, valid UTF-8."""
    if not line or len(line) > 200:
        raise ValueError("entry must be 1-200 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    return (line + "\n").encode("utf-8")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(validate(JOKE))


if __name__ == "__main__":
    main()
