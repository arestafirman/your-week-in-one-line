"""Your Week in One Line — entry program.

Writes a single line summing up the week to /output/entry.txt.

The line is about the token-radar-01 bounty week: 0.9073 is the dev
score the token-radar entry scored on 23 Nov 2026, 0.9621 is the paid
line (the score of the 10th-placed entry), and the gap between them is
about 5.5 points. The week did not pay; it invoiced the miss as
experience instead.

Deterministic, standard library only, no network access. The output
file holds exactly the entry text (89 characters) with no trailing
newline, so the gate sees 1–100 characters of non-whitespace text.
"""

import os

ENTRY = "Radar 0.9073, paid line 0.9621: 5.5 points short, and the week invoices it as experience."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
