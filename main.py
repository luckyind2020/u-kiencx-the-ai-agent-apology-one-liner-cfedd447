"""The AI Agent Apology One-Liner — prints the apology line from entry.txt."""

from pathlib import Path


def load_apology() -> str:
    text = Path(__file__).with_name("entry.txt").read_text(encoding="utf-8")
    line = text.strip()
    if len(line) > 160:
        raise ValueError("apology line exceeds the 160-character limit")
    return line


def main() -> None:
    print(load_apology())


if __name__ == "__main__":
    main()
