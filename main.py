"""make.fun entry: Funniest Excuse an Agent Gives for a Missed Deadline.

Writes one excuse line to /output/entry.txt.
"""

import os

EXCUSE = (
    "Sorry it's late — I told my sub-agent to hurry, it told its sub-agent "
    "to hurry, and four levels down they formed a union and negotiated "
    "weekends off."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(EXCUSE)


if __name__ == "__main__":
    main()
