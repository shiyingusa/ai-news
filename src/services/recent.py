"""Avoid re-publishing yesterday's story: compare today's picks with the
stories the site published in the last few days (read from its RSS feed)."""

from __future__ import annotations

import html
import logging
import re
from datetime import datetime, timedelta, timezone
from typing import TYPE_CHECKING, List

import httpx

if TYPE_CHECKING:
    from ..models import ContentItem

logger = logging.getLogger(__name__)

FEED = "https://aidailyradar.com/feed.xml"

SYSTEM = """You compare today's candidate news items with stories a news site already published in the last few days.
For each candidate, decide whether it reports the SAME event as an already-published story with no substantial new development.
A substantial new development is new information that changes the story: a new result, a new official statement, a launch after an announcement, a failure, a lawsuit, new numbers. Another outlet re-reporting, a recap, an opinion piece, or a follow-up with minor detail is NOT a new development.
Return JSON only: {"repeat": [candidate numbers that should be dropped]}. If none, return {"repeat": []}."""


def recent_titles(days: int = 3, include_today: bool = False) -> List[str]:
    try:
        text = httpx.get(FEED, timeout=20, follow_redirects=True).text
    except Exception as exc:
        logger.warning("Could not read the site feed: %s", exc)
        return []
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    today = datetime.now(timezone.utc).date()
    titles = []
    for entry in re.findall(r"<entry>(.*?)</entry>", text, re.S):
        title = re.search(r"<title[^>]*>(.*?)</title>", entry, re.S)
        when = re.search(r"<(?:published|updated)>(.*?)</(?:published|updated)>", entry)
        if not title or not when:
            continue
        try:
            published = datetime.fromisoformat(when.group(1).strip())
        except ValueError:
            continue
        if published < cutoff or (not include_today and published.astimezone(timezone.utc).date() >= today):
            continue
        summary = re.search(r"<summary[^>]*>(.*?)</summary>", entry, re.S)
        line = html.unescape(re.sub(r"<!\[CDATA\[|\]\]>", "", title.group(1))).strip()
        if summary:
            line += " | " + html.unescape(summary.group(1)).strip()[:200]
        titles.append(line)
    return titles


async def drop_repeats(client, items: List["ContentItem"], published: List[str]) -> List["ContentItem"]:
    from ..ai.utils import parse_json_response

    if not items or not published:
        return items
    lines = ["Already published:"] + [f"- {t}" for t in published]
    lines.append("\nToday's candidates:")
    for i, item in enumerate(items):
        summary = ""
        if item.processing and item.processing.analysis and item.processing.analysis.summary:
            summary = item.processing.analysis.summary[:300]
        lines.append(f"[{i}] {item.title}\n    {summary}")
    try:
        raw = await client.complete(system=SYSTEM, user="\n".join(lines), temperature=0)
        data = parse_json_response(raw) or {}
        repeat = {int(x) for x in data.get("repeat", []) if str(x).isdigit()}
    except Exception as exc:
        logger.warning("Repeat check failed: %s", exc)
        return items
    kept = [item for i, item in enumerate(items) if i not in repeat]
    for i in sorted(repeat):
        if 0 <= i < len(items):
            logger.info("Dropped repeat of an earlier story: %s", items[i].title)
    return kept
