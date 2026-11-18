"""Replace radar artwork with licensed photos on already-published stories.

Runs against a checkout of the gh-pages branch (``--site``). For each English
story from the last ``--days`` days without a photo credit, asks the model for
search queries, finds a licensed photo, overwrites the artwork files in place
and adds ``photo_credit`` to both the English and Chinese pages.

    uv run python scripts/refresh_photos.py --site site --days 3
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
from src.services.daily_brief import queries_for  # noqa: E402
from src.services.site_export import _date_label  # noqa: E402
from src.services.story_images import make_share_from_photo  # noqa: E402
from src.services.story_photos import find_photo, save_photo  # noqa: E402
from src.storage.manager import StorageManager  # noqa: E402


def front_value(text: str, key: str):
    match = re.search(rf"^{key}: (.*)$", text, re.M)
    if not match:
        return None
    try:
        return json.loads(match.group(1))
    except json.JSONDecodeError:
        return match.group(1).strip()


def set_front(text: str, key: str, value) -> str:
    line = f"{key}: {json.dumps(value, ensure_ascii=False)}"
    if re.search(rf"^{key}: .*$", text, re.M):
        return re.sub(rf"^{key}: .*$", lambda _: line, text, count=1, flags=re.M)
    return text.replace("\n---\n", f"\n{line}\n---\n", 1)


async def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", default="site")
    parser.add_argument("--days", type=int, default=3)
    parser.add_argument("--config", default="data/config.github.json")
    args = parser.parse_args()
    load_dotenv()

    site = Path(args.site)
    since = date.today() - timedelta(days=args.days)
    targets = []
    for path in sorted((site / "_stories").glob("*-en.md")):
        day = path.name[:10]
        if day < since.isoformat():
            continue
        text = path.read_text(encoding="utf-8")
        if front_value(text, "photo_credit"):
            continue
        targets.append((path, text, day))
    print(f"{len(targets)} stories without a photo")
    if not targets:
        return 0

    config = StorageManager(config_path=args.config).load_config()
    client = create_ai_client(config.ai)
    entries = [(str(p), front_value(t, "title") or "", front_value(t, "tags") or []) for p, t, _ in targets]
    queries = await queries_for(client, entries)

    used: set = set()
    for credit_file in (site / "assets" / "stories").glob("*/*.json"):
        try:
            credit = json.loads(credit_file.read_text(encoding="utf-8"))
            used.update(filter(None, (credit.get("url"), credit.get("source_url"))))
        except (OSError, ValueError):
            pass
    updated = 0
    for path, text, day in targets:
        slug = front_value(text, "story_id")
        section = front_value(text, "section") or "ai-news"
        qs = queries.get(str(path)) or []
        if not slug:
            continue
        day_dir = site / "assets" / "stories" / day
        photo = None
        for _ in range(4):  # a candidate can fail the download or the looks-like-a-photo check
            candidate = find_photo(qs, used, section=section)
            if not candidate:
                break
            if save_photo(candidate, day_dir, slug):
                photo = candidate
                break
        if not photo:
            print(f"  no photo: {slug} ({qs})")
            continue
        make_share_from_photo(day_dir / f"{slug}.jpg", day_dir / f"{slug}-share.jpg", front_value(text, "title") or "", section, _date_label(day))
        credit = photo.credit()
        (day_dir / f"{slug}.json").write_text(json.dumps(credit, ensure_ascii=False), encoding="utf-8")
        for lang_path in (path, path.with_name(path.name.replace("-en.md", "-zh.md"))):
            if not lang_path.exists():
                continue
            body = lang_path.read_text(encoding="utf-8")
            body = set_front(body, "photo_credit", credit)
            body = set_front(body, "art", f"/assets/stories/{day}/{slug}.jpg")
            body = set_front(body, "thumb", f"/assets/stories/{day}/{slug}-640.jpg")
            body = set_front(body, "image", f"/assets/stories/{day}/{slug}-share.jpg")
            lang_path.write_text(body, encoding="utf-8")
        updated += 1
        print(f"  photo: {slug} <- {photo.provider} {photo.licence} {photo.source_url}")
    print(f"updated {updated} of {len(targets)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
