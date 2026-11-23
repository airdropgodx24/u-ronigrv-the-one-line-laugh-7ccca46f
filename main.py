"""The One-Line Laugh entry.

Writes a single original one-liner to /output/entry.txt with no trailing
newline. Standard library only, deterministic, no network.
"""

import os

LINE = "I bought a diary to organise my thoughts, but now it just sits there judging me in my own handwriting."


def main():
    # Gate check: one sentence, 1-200 characters, matching the competition gate.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.count(".") == 1 and LINE.endswith("."), "line must be a single sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
