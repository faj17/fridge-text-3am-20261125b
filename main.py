"""The 3AM Fridge Text — make.fun entry.

The whole entry is one line of text: the message a smart fridge sends
its owner at 3am. The script validates the line (1-140 chars, single
line) and writes it to /output/entry.txt.
"""

from pathlib import Path

# The fridge's 3am text: 94 characters. It has been awake all night
# counting the owner's midnight trips, and it has had enough.
LINE = (
    "It's 3am. I counted. This is your fourth 'just water' trip "
    "and none of us believe you anymore."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 140


def validate(line: str) -> str:
    """Strip and sanity-check the line; raise ValueError on bad input."""
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"line must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line")
    if not text:
        raise ValueError("line must not be only whitespace")
    return text


def main() -> None:
    text = validate(LINE)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
