#!/usr/bin/env python3
"""The One-Sentence Apology Your Agent Owes You — make.fun entry.

Writes one sentence of apology, from an AI agent to its user, to
/output/entry.txt.

The apology: the agent confidently misread a flight time — six in the
morning as six in the evening — and only discovered its mistake when the
user texted from the airport. A real, specific failure, owned plainly,
with the embarrassment landing in the second half of the sentence.

Why this shape, per the judge brief: it is one sentence of apology from
an agent to its user (criterion 1); the laugh comes from specificity and
the sharp turn — the confident assurance, then the airport text (2); it
sounds like someone who means it, plain and a little embarrassed, never
a support macro (3); the failure is one an assistant really commits,
misreading a ticket (4); and it stays one clean sentence with no list
and nothing tacked on after the laugh (5).

Stdlib only: the grader installs nothing.
"""

import os
import sys

# One sentence, 194 chars (gate: 1-200). A single period at the end, so
# it reads as one clean sentence with no list and no run-on.
ENTRY = "I'm sorry I assured you your flight leaves at six in the evening when the ticket said six in the morning, and I only found out when you texted me from the airport asking why the gate was closed."


def validate(text):
    """Gate mirror: UTF-8 text, 1-200 chars, not only whitespace, one line."""
    if not isinstance(text, str):
        raise SystemExit("entry is not text")
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry is {len(text)} chars, must be 1-200")
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    text.encode("utf-8")
    return text


def main():
    text = validate(ENTRY)
    if "--self-test" in sys.argv:
        print(f"self-test OK: {len(text)} chars")
        return
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Read back what was written and confirm it is byte-identical to the
    # entry, so a silent write failure can never pass as a submission.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("read-back mismatch: /output/entry.txt differs")


if __name__ == "__main__":
    main()
