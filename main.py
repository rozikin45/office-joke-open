"""Office joke entry for make.fun.

Writes one original one-line office joke (<=200 chars) to /output/entry.txt.
Deterministic: same bytes on every run, no input, no network, no clock.
"""
from pathlib import Path

JOKE = (
    "The meeting that could have been an email just scheduled a follow-up "
    "to discuss why it couldn't have been an email — and invited the email."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
