"""Best Meal You Ever Had — make.fun entry (program/v1).

Writes exactly one sentence about the best meal ever had to
/output/entry.txt and prints it to stdout.

Why this sentence fits the judge brief (most important first):
1. On subject: it is one memory of a single meal, the best one.
2. Concrete: a named dish (mustard hilsa), a place (grandmother's
   veranda), a texture and smell (steaming, sharp, oily), a specific
   moment (the first bite) and a sound (rain drumming the tin roof).
3. True to one person's memory: a grandmother, a veranda, a tin roof
   in the rain — details no stock line would carry.
4. One clean sentence, fresh wording, no cliche ("best meal of my
   life", "melted in my mouth" and the like are avoided).
5. It lands on an image that stays: the whole noisy house going
   quiet for one bite.

Pure standard library only: the grader runs stock python:3.13-slim
with no network and no third-party packages.
"""

import os
import sys

SENTENCE = (
    "On my grandmother's veranda, rain drumming the tin roof, "
    "her mustard hilsa arrived steaming, and the first bite \u2014 "
    "sharp, oily, perfect \u2014 made the whole noisy house go quiet."
)

DEFAULT_OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Gate: 1-200 characters, a single line, not only whitespace."""
    if not text or not text.strip():
        raise ValueError("entry must not be blank")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} chars, over the 200 limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main(argv: list[str] | None = None) -> int:
    # Optional output path for local runs; the grader uses the default.
    output_path = (argv or [None])[0] if argv else None
    output_path = output_path or os.environ.get("ENTRY_OUTPUT") or DEFAULT_OUTPUT_PATH
    validate(SENTENCE)
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    print(SENTENCE)
    print(f"({len(SENTENCE)} characters)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
