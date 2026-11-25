"""Write the entry line for The Funniest Honest Appliance Error.

The program takes no input and needs no network: it drops one deadpan
microwave error message into /output/entry.txt, the file the sealed
scorer reads. The message is honest (the microwave really did reheat
the same coffee four times) and the joke is the machine blaming the
owner instead of itself.
"""

from pathlib import Path

LINE = (
    "I have reheated this coffee four times. "
    "I am not broken. You are the problem. Please drink it."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"


def main() -> None:
    # The gate allows 1-200 characters; the line below is 94, so it
    # passes as written and no trimming or truncation is ever needed.
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
