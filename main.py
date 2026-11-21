"""Write one short relaxing text to /output/entry.txt.

Deterministic: the same bytes on every run. No network, no input.
"""

from pathlib import Path

TEXT = (
    "The tide went out hours ago. The wet sand holds the sky in a mirror, "
    "and the stars lie down in it, shivering as each wave folds over them "
    "and lets go. The water keeps the slow time it kept before anyone was "
    "here. It isn't waiting for anything. Neither are you, anymore."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
