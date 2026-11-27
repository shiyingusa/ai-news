"""One-off: give already-published stories the new body shape.

    python scripts/restructure_stories.py <gh-pages checkout>
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.services.story_layout import restructure_body  # noqa: E402

root = Path(sys.argv[1])
changed = 0
for path in sorted((root / "_stories").glob("*.md")):
    text = path.read_text(encoding="utf-8")
    end = text.index("\n---\n", 4) + 5
    front, body = text[:end], text[end:]
    lang = "zh" if path.name.endswith("-zh.md") else "en"
    new = restructure_body(body, lang)
    if new != body:
        path.write_text(front + new, encoding="utf-8")
        changed += 1
print(f"restructured {changed} stories")
