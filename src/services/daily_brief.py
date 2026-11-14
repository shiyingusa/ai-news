"""The Big Picture: a short original synthesis of the day's selected stories.

One extra model call per language reads the selected headlines and leads and
writes what connects them, so each issue carries analysis of its own on top of
the per-story summaries. Saved as ``docs/_data/briefs/<date>-<lang>.json``.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import TYPE_CHECKING, List, Optional

from ..ai.utils import parse_json_response

if TYPE_CHECKING:  # pragma: no cover
    from ..ai.client import AIClient
    from ..models import ContentItem

logger = logging.getLogger(__name__)

SYSTEM = """You are the editor of AI Daily Radar, a daily briefing on AI and the frontier technology around it (chips, robots and self-driving, EVs and energy, space, science).
Write an original analysis of today's selected stories for smart general readers. Do not summarize stories one by one. Find the two or three threads that connect them, explain why they matter together, and say what to watch next.
Rules: use only facts present in the supplied stories; never invent numbers, quotes or events; attribute claims to the companies or outlets that made them; distinguish announcements from shipped products; no hype, no clichés such as "game-changer" or "marks a major milestone".
Return JSON only: {"headline": "...", "paragraphs": ["...", "..."], "takeaways": ["...", "...", "..."]}.
headline: at most 12 words. paragraphs: two or three paragraphs, 140-220 words in total. takeaways: three short sentences."""

LANG_NOTE = {
    "en": "Write in American English.",
    "zh": "Write in Simplified Chinese (简体中文). Keep product and company names in their usual form. headline 不超过 22 个汉字；paragraphs 总共 250 到 400 字。",
}


def _story_lines(items: List["ContentItem"], language: str, limit: int = 30) -> str:
    lines = []
    for index, item in enumerate(items[:limit], start=1):
        processing = item.processing
        artifact = processing.artifacts.get(language) if processing else None
        if not artifact:
            continue
        primary = next((b for b in artifact.blocks if b.primary), None)
        lead = (primary.content if primary else "")[:600]
        section = processing.classification.profile if processing and processing.classification else ""
        lines.append(f"{index}. [{section}] {artifact.title}\n   {lead}")
    return "\n".join(lines)


async def write_daily_brief(
    client: "AIClient",
    items: List["ContentItem"],
    date: str,
    language: str,
    out_dir: Path,
) -> Optional[Path]:
    """Generate and save the day's brief; returns the path, or None on failure."""
    stories = _story_lines(items, language)
    if not stories:
        return None
    user = f"{LANG_NOTE.get(language, '')}\nDate: {date}\n\nToday's selected stories:\n{stories}"
    try:
        raw = await client.complete(system=SYSTEM, user=user, temperature=0.4, max_tokens=1600)
    except Exception as exc:  # pragma: no cover - network/provider failure
        logger.warning("Daily brief failed for %s: %s", language, exc)
        return None
    data = parse_json_response(raw) or {}
    headline = str(data.get("headline", "")).strip()
    paragraphs = [str(p).strip() for p in data.get("paragraphs", []) if str(p).strip()]
    takeaways = [str(t).strip() for t in data.get("takeaways", []) if str(t).strip()]
    if not headline or not paragraphs:
        logger.warning("Daily brief for %s came back incomplete; skipped", language)
        return None
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{date}-{language}.json"
    path.write_text(
        json.dumps(
            {"date": date, "lang": language, "headline": headline, "paragraphs": paragraphs, "takeaways": takeaways[:4]},
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    return path
