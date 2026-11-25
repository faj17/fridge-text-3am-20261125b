"""The 3AM Fridge Text — make.fun entry.

The whole entry is one line of text: the message a smart fridge sends
its owner at 3am. The script validates the line (1-140 chars, single
line) and writes it to /output/entry.txt.
"""

from pathlib import Path

# The fridge's 3am text: 94 characters. It has been awake all night
# counting the owner's midnight trips, and it has had enough.
# Split into setup + punch so the two beats are editable independently;
# assemble() is the single place the final line is built.
SETUP = "It's 3am. I counted. This is your fourth 'just water' trip"
PUNCH = "and none of us believe you anymore."


def assemble() -> str:
    """Join the setup and punchline into the final one-line entry."""
    return f"{SETUP} {PUNCH}"

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 140


def validate(line: str) -> str:
    """Strip and sanity-check the line; raise ValueError on bad input.

    The single-line check is abbreviation-aware: a period followed by a
    space mid-line is sentence punctuation, not a line break, so only
    real newline/carriage-return characters are rejected. Trailing
    whitespace is stripped; interior spacing is preserved verbatim so
    the validated text is byte-identical to the assembled line.
    """
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"line must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if not text:
        raise ValueError("line must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line")
    return text


def main() -> None:
    text = validate(assemble())
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
