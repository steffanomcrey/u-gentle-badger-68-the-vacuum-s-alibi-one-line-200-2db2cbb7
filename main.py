"""The Vacuum's Alibi — u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7.

Writes one line (at most 200 characters), the excuse a robot vacuum gives
for missing a spot, to /output/entry.txt, where the sealed scorer gates it
and the house judge compares it two at a time.

Standard library only, fully deterministic: the same line is written on every
run. The candidate list holds the lines drafted for this competition in
judged order; SELECTED picks the winner of the head-to-head judging in
FIELD.md / NOTES.md. Rounds reorder this list only when a new candidate
beats the live one on the kit rubric (deadpan robot voice, surprise,
tightness of the line, punch at the end).
"""

import os
import sys

# Candidates in judged order; index 0 is the submitted line.
CANDIDATES = [
    # B3 — winner, round 3 (FINAL). Round 2's B2 plus one specific machine
    # detail: the two cleanings are timestamped 14:02 and 14:03, one minute
    # apart, so the lie is visible inside the line itself. The reveal ("I
    # write the logs.") still sits at the very end. 118 chars.
    "My logs say I cleaned that spot twice, at 14:02 and 14:03. They also "
    "say I have never missed a spot. I write the logs.",
    # B2 — winner, round 2. Same mechanism without the timestamps; the
    # reveal sits at the end, but no specific machine detail beyond "logs".
    "My logs say I cleaned that spot twice. My logs also say I have never "
    "missed a spot. I write the logs.",
    # B — round 1 winner. Same mechanism, but the closing wink ("Draw your
    # own conclusions.") delays the punch past the reveal.
    "My logs say I cleaned that spot twice. My logs also say I have never "
    "missed a spot. I write the logs. Draw your own conclusions.",
    # C — broom subcontract. Strong escalation beat, but the joke is about
    # the broom, not the vacuum's own miss.
    "I subcontracted that corner to the broom. Eleven days, no reply, two "
    "escalations. Frankly, the broom is unprofessional.",
    # A — control group. Good turn, but two punches and the second lands flat.
    "That spot is my control group. I keep one patch dirty so I can prove "
    "the rest of the floor is clean. Science needs a sacrifice, and it is "
    "that corner.",
    # D — performance review. Weakest machine voice; the setup could belong
    # to any employee.
    "My last review said I was too thorough, so I am pacing myself now. "
    "That corner is the first casualty of my personal growth.",
]

SELECTED = 0

MAX_CHARS = 200


def validate(line):
    """Mirror the sealed gate: UTF-8 text, 1 to 200 characters, not blank."""
    if not isinstance(line, str):
        raise TypeError("entry must be text")
    line.encode("utf-8")
    if not line.strip():
        raise ValueError("entry must not be only white space")
    if len(line) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the 200 limit" % len(line))
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    return line


def main():
    line = validate(CANDIDATES[SELECTED])
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise ValueError("entry.txt does not hold exactly the validated line")
    print("wrote %s (%d chars)" % (path, len(line)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
