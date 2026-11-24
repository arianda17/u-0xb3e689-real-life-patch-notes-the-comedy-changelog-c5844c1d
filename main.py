"""Real-Life Patch Notes: The Comedy Changelog.

Writes the winning one-line patch note for a bug in real life / human
biology to /output/entry.txt.
"""

# The entry: a single-line patch note, at most 160 characters.
# v3.1.0: fixed a bug where the brain's 'what did I come in here for' subroutine returned null after opening a refrigerator door.
ENTRY = "v3.1.0: fixed a bug where the brain's 'what did I come in here for' subroutine returned null after opening a refrigerator door."


def main() -> None:
    text = ENTRY
    # Gate: UTF-8 text, 1-160 characters, not only whitespace, single line.
    assert isinstance(text, str), "entry must be a string"
    assert 1 <= len(text) <= 160, f"entry length {len(text)} out of range 1-160"
    assert text.strip() and "\n" not in text and "\r" not in text, "entry must be non-whitespace single line"
    assert text.encode("utf-8"), "entry must be UTF-8"

    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)

    print(text)


if __name__ == "__main__":
    main()