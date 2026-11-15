"""Write The Big Picture for published days that do not have one yet.

Runs against a checkout of the gh-pages branch (``--site``).

    uv run python scripts/backfill_briefs.py --site site --days 3
"""

from __future__ import annotations

import argparse
import asyncio
import json
import re
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from dotenv import load_dotenv  # noqa: E402

from src.ai.client import create_ai_client  # noqa: E402
from src.services.daily_brief import write_brief_from_lines  # noqa: E402
from src.storage.manager import StorageManager  # noqa: E402


def front(text: str, key: str):
    match = re.search(rf"^{key}: (.*)$", text, re.M)
    if not match:
        return None
    try:
        return json.loads(match.group(1))
    except json.JSONDecodeError:
        return match.group(1).strip()


def lead_of(text: str) -> str:
    body = text.split("\n---\n", 1)[-1]
    match = re.search(r'<div class="story-lead" markdown="1">\s*(.*?)\s*</div>', body, re.S)
    return " ".join((match.group(1) if match else "").split())[:600]


async def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", default="site")
    parser.add_argument("--days", type=int, default=3)
    parser.add_argument("--config", default="data/config.github.json")
    args = parser.parse_args()
    load_dotenv()
    site = Path(args.site)
    out_dir = site / "_data" / "briefs"
    config = StorageManager(config_path=args.config).load_config()
    client = create_ai_client(config.ai)
    for offset in range(args.days):
        day = (date.today() - timedelta(days=offset)).isoformat()
        for lang in ("en", "zh"):
            if (out_dir / f"{day}-{lang}.json").exists():
                continue
            files = sorted((site / "_stories").glob(f"{day}-*-{lang}.md"))
            stories = []
            for path in files:
                text = path.read_text(encoding="utf-8")
                stories.append((front(text, "score") or 0, front(text, "section") or "", front(text, "title") or "", lead_of(text)))
            stories.sort(key=lambda s: -float(s[0] or 0))
            lines = "\n".join(f"{i}. [{sec}] {title}\n   {lead}" for i, (_, sec, title, lead) in enumerate(stories[:30], 1))
            if not lines:
                continue
            path = await write_brief_from_lines(client, lines, day, lang, out_dir)
            print(f"{day} {lang}: {'written' if path else 'failed'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
