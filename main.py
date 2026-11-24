#!/usr/bin/env python3
"""Entry for make.fun: One-Line Office Joke: 24-Hour Sprint.

Writes a single one-line joke about office life (under 200 characters)
to /output/entry.txt. Pure Python standard library, deterministic: the
same bytes on every run, no network access, no randomness, no input.
"""

import os

JOKE = "I asked for a standing desk; HR gave me a standing meeting instead."

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def main() -> None:
    assert 1 <= len(JOKE) <= 200, f"joke must be 1-200 chars, got {len(JOKE)}"
    assert "\n" not in JOKE, "joke must be a single line"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    entry_path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
