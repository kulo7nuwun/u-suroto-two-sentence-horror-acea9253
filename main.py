#!/usr/bin/env python3
"""Two-Sentence Horror — entry program.

Writes exactly one horror story, in exactly two sentences, to
/output/entry.txt. The story is a single constant so the output is
deterministic; before writing, the program checks the gate the sealed
scorer enforces: UTF-8 text, 1-400 characters, not only whitespace,
exactly two sentences.
"""

import os
import re
import sys

STORY = (
    "Every night at 3 a.m., my baby monitor plays back my own voice "
    "saying words I never said. "
    "Tonight it added a second voice \u2014 small, patient, and learning "
    "to sound exactly like me."
)

OUTPUT_PATH = "/output/entry.txt"


def count_sentences(text: str) -> int:
    """Count sentence terminators that end a sentence.

    A sentence ends at a '.', '!' or '?' followed by whitespace or the
    end of the text. Abbreviations are not a concern here: the story
    contains no mid-sentence periods. Trailing whitespace is stripped
    first so a final terminator at end-of-text still counts.
    """
    terminators = re.findall(r"[.!?](?:\s|$)", text.strip())
    return len(terminators)


def validate(text: str) -> None:
    if not text or not text.strip():
        raise ValueError("story is empty or only whitespace")
    if len(text) > 400:
        raise ValueError(f"story is {len(text)} characters, over the 400 limit")
    sentences = count_sentences(text)
    if sentences != 2:
        raise ValueError(f"story has {sentences} sentences, expected exactly 2")
    text.encode("utf-8")  # raises if not valid UTF-8-encodable text


def main() -> int:
    validate(STORY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(STORY)
    print(f"wrote {len(STORY)} characters, 2 sentences -> {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
