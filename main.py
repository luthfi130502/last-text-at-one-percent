"""Last Text at One Percent - a make.fun entry.

The program writes a single line to /output/entry.txt: the last text
someone sends when their phone battery hits 1 percent, written in the
phone's own dying voice.
"""

from pathlib import Path

ENTRY = (
    "phone's at 1% - if i vanish mid-word, tell my charger i loved it, "
    "tell the group chat the lore dies with me, and tell my mum her 'k' "
    "was received, read, and quietly judged."
)


def main() -> None:
    text = ENTRY.strip()
    assert "\n" not in text, "entry must be exactly one line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
