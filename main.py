#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — make.fun entry.

Writes one line of last words a phone says as its battery hits 1 percent
to /output/entry.txt (UTF-8, 1-199 chars, single line).
"""

import os

LINE = (
    "Dying now, so here it is: your screen time is 11 hours a day, "
    "your password is your dog's name, and the Wi-Fi password "
    "dies with me."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 199, f"line is {len(text)} chars"
    assert "\n" not in text, "must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
