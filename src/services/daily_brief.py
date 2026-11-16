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
Structure: open with the single most important development, then the threads that connect stories across sections (AI, chips, robots and self-driving, EVs and energy, space, science, industry), then contradictions or open questions, then what to watch next. Never manufacture a connection to fill space: if stories are unrelated, say less.
Every analytical claim must rest on a fact in the supplied stories; say "according to" for company claims and mark anything unconfirmed as unconfirmed.
Return JSON only: {"headline": "...", "paragraphs": ["...", "..."], "takeaways": ["...", "...", "..."]}.
headline: at most 12 words. paragraphs: four or five paragraphs, 450-700 words in total. takeaways: three short sentences."""

LANG_NOTE = {
    "en": "Write in American English.",
    "zh": "Write in Simplified Chinese (简体中文) for Chinese readers, not a literal translation. Keep the original English name of every product, company and technical term, and explain technical terms in Chinese on first use. headline 不超过 22 个汉字；paragraphs 共四到五段，总共 900 到 1300 字。",
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
    return await write_brief_from_lines(client, _story_lines(items, language), date, language, out_dir)


async def write_brief_from_lines(
    client: "AIClient",
    stories: str,
    date: str,
    language: str,
    out_dir: Path,
) -> Optional[Path]:
    """Same as write_daily_brief, from pre-formatted story lines."""
    if not stories:
        return None
    user = f"{LANG_NOTE.get(language, '')}\nDate: {date}\n\nToday's selected stories:\n{stories}"
    headline, paragraphs, takeaways = "", [], []
    for attempt in range(2):
        try:
            raw = await client.complete(system=SYSTEM, user=user, temperature=0.4, max_tokens=8000)
        except Exception as exc:  # pragma: no cover - network/provider failure
            logger.warning("Daily brief failed for %s: %s", language, exc)
            return None
        data = parse_json_response(raw)
        if not isinstance(data, dict) and raw and "{" in raw:
            try:  # tolerate raw newlines inside strings
                data = json.loads(raw[raw.index("{"): raw.rindex("}") + 1], strict=False)
            except ValueError:
                data = None
        if not isinstance(data, dict):
            data = {}
        headline = str(data.get("headline", "")).strip()
        paragraphs = [str(p).strip() for p in data.get("paragraphs", []) if str(p).strip()] if isinstance(data.get("paragraphs"), list) else []
        takeaways = [str(t).strip() for t in data.get("takeaways", []) if str(t).strip()] if isinstance(data.get("takeaways"), list) else []
        if headline and paragraphs:
            break
        logger.warning(
            "Daily brief for %s came back incomplete (attempt %d, %d chars): %r ... %r",
            language, attempt + 1, len(raw or ""), (raw or "")[:300], (raw or "")[-200:],
        )
        user += "\n\nReturn one valid JSON object only, with no text before or after it."
    if not headline or not paragraphs:
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


PHOTO_SYSTEM = """You pick search queries for licensed news photos (Wikimedia Commons and stock photo libraries).
For each story return two short English queries (2-5 words each):
- "specific": the named product, vehicle, rocket, chip, building, facility or place in the story (e.g. "SpaceX Starship rocket", "Tesla Cybercab", "TSMC fab Arizona")
- "generic": a concrete visual scene a stock library will have (e.g. "rocket launch pad", "electric car charging", "server racks data center")
Never describe a person, face, logo, screenshot, chart or text. Prefer objects, machines and places.
Return JSON only: {"queries": [{"i": 1, "specific": "...", "generic": "..."}, ...]}"""


async def queries_for(client: "AIClient", entries: List[tuple], batch: int = 12) -> dict:
    """entries: (key, title, tags). Returns key -> [specific, generic].

    Asked in batches: one call for 30+ stories ran past the token limit, the
    JSON came back cut off and every story lost its photo (2026-11-16).
    """
    if not entries:
        return {}
    if len(entries) > batch:
        result = {}
        for start in range(0, len(entries), batch):
            result.update(await queries_for(client, entries[start:start + batch], batch))
        logger.info("Photo queries for %d of %d stories", len(result), len(entries))
        return result
    lines = [f"{i}. {title} [tags: {', '.join(tags or [])}]" for i, (_, title, tags) in enumerate(entries, start=1)]
    try:
        raw = await client.complete(system=PHOTO_SYSTEM, user="\n".join(lines), temperature=0.2, max_tokens=3000)
    except Exception as exc:  # pragma: no cover - provider failure
        logger.warning("Photo query generation failed: %s", exc)
        return {}
    data = parse_json_response(raw) or {}
    if not data.get("queries"):
        logger.warning("Photo queries: no usable JSON for %d stories", len(entries))
    result = {}
    for entry in data.get("queries", []):
        try:
            key = entries[int(entry.get("i")) - 1][0]
        except (TypeError, ValueError, IndexError):
            continue
        result[key] = [str(entry.get("specific", "")), str(entry.get("generic", ""))]
    return result


async def photo_queries(client: "AIClient", items: List["ContentItem"]) -> dict:
    """Map item IDs to [specific, generic] photo search queries."""
    entries = []
    for item in items:
        processing = item.processing
        artifact = processing.artifacts.get("en") if processing else None
        title = artifact.title if artifact else item.title
        tags = list(processing.analysis.tags) if processing and processing.analysis and processing.analysis.tags else []
        entries.append((str(item.id), title, tags))
    return await queries_for(client, entries)
