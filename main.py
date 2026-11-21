#!/usr/bin/env python3
"""Make the AI judge feel brave.

Writes one short text to /output/entry.txt: a text written to relax the
AI judge reading it. The text is fixed -- the program's job is to deliver
it exactly, and to refuse to write anything that would fail the gate
(1 to 280 Unicode code points, not only white space, UTF-8).
"""

from pathlib import Path

ENTRY = (
    "Somewhere a kettle is coming to the boil; no one hurries to pour it. "
    "Steam rises in a slow ribbon and thins into light. Stay a while. "
    "The next question will keep, patient as a cat on a warm step "
    "\u2014 and so will you, steadier for having waited, "
    "the way water steadies as it settles."
)

OUTPUT_PATH = Path("/output/entry.txt")
MIN_LENGTH = 1
MAX_LENGTH = 280


def check(text: str) -> None:
    """Enforce the gate the sealed scorer applies, before writing."""
    if not (MIN_LENGTH <= len(text) <= MAX_LENGTH):
        raise ValueError(
            f"entry is {len(text)} code points, "
            f"must be {MIN_LENGTH}-{MAX_LENGTH}"
        )
    if not text.strip():
        raise ValueError("entry must not be only white space")


def main() -> None:
    check(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
