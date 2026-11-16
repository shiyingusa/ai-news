"""High-risk stories: publish only when sourced and worded safely, else hold.

A story is high-risk when the enrichment `risk` block names a category:
casualty (deaths or injuries), accident (crash, explosion, launch failure)
or allegation (fraud, crime or financial misconduct against a named party).

It publishes automatically when it rests on a primary source or on at least
two independent publishers, and, for allegations, when the headline
attributes the accusation. Otherwise it is held in docs/_review/<date>/
(Jekyll does not publish underscore folders) and a GitHub issue asks the
owner to approve it. Held stories expire after 24 hours.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Dict, List, Optional, Tuple

if TYPE_CHECKING:  # pragma: no cover
    from ..models import ContentItem

CATEGORIES = ("casualty", "accident", "allegation")
SOURCINGS = ("primary", "multiple", "single")

# Words that make an accusation attributed rather than asserted.
ATTRIBUTION = re.compile(
    r"\b(?:alleg\w*|accus\w*|charg\w*|su(?:e|es|ed|ing)|lawsuit|indict\w*|claims?|says?|said|"
    r"prosecutors?|regulators?|probe|investigat\w*|fine[sd]?|complaint)\b|"
    r"指控|起诉|涉嫌|称|据|调查|罚款|诉讼|控告|认定",
    re.I,
)


@dataclass
class RiskCall:
    category: Optional[str] = None
    sourcing: Optional[str] = None


@dataclass
class Held:
    item_id: str
    category: str
    reasons: List[str] = field(default_factory=list)


def parse_risk(text: str) -> RiskCall:
    """Read 'allegation | primary' style text; unknown words count as none."""
    words = re.findall(r"[a-z]+", (text or "").lower())
    category = next((w for w in words if w in CATEGORIES), None)
    sourcing = next((w for w in words if w in SOURCINGS), None)
    return RiskCall(category, sourcing)


def _risk_block(item: "ContentItem") -> str:
    arts = item.processing.artifacts if item.processing else {}
    for lang in ("en", *arts.keys()):
        art = arts.get(lang)
        if art is None:
            continue
        for block in art.blocks:
            if block.id == "risk":
                return block.content or ""
    return ""


def independent_publishers(item: "ContentItem") -> int:
    """Distinct publishers behind the story: the lead report plus merged ones."""
    from types import SimpleNamespace

    from .site_export import publisher_name

    names = {publisher_name(item).strip().lower()}
    for r in (item.metadata or {}).get("related") or []:
        fake = SimpleNamespace(
            metadata={k: r.get(k) for k in ("feed_name", "publisher")} | {"original_url": r.get("url")},
            url=r.get("url"), source_type=SimpleNamespace(value=r.get("source_type") or "rss"),
        )
        names.add(publisher_name(fake).strip().lower())
    names.discard("")
    return len(names)


def assess(item: "ContentItem") -> Optional[Held]:
    """None when the story may publish; a Held record when it must wait."""
    call = parse_risk(_risk_block(item))
    if not call.category:
        return None
    reasons: List[str] = []
    if call.sourcing != "primary" and independent_publishers(item) < 2:
        reasons.append("没有一手来源，独立报道也不足 2 家")
    if call.category == "allegation":
        arts = item.processing.artifacts if item.processing else {}
        for lang, art in arts.items():
            if art and art.title and not ATTRIBUTION.search(art.title):
                reasons.append(("中文" if lang == "zh" else "英文") + "标题把指控写成了事实")
    if not reasons:
        return None
    return Held(str(item.id), call.category, reasons)


def split_held(items: List["ContentItem"]) -> Tuple[List["ContentItem"], List["ContentItem"], Dict[str, Held]]:
    """Separate stories that may publish from those held for review."""
    publish, held_items, held = [], [], {}
    for item in items:
        record = assess(item)
        if record is None:
            publish.append(item)
        else:
            held_items.append(item)
            held[record.item_id] = record
    return publish, held_items, held


def write_manifest(review_dir, held_items: List["ContentItem"], held: Dict[str, Held], slugs: Dict[str, str],
                   titles: Dict[str, str], edition: int) -> Optional[str]:
    """Record what this run held, for the issue and the approval workflow."""
    import json
    from datetime import datetime, timezone
    from pathlib import Path

    from .site_export import original_url, publisher_name

    if not held_items:
        return None
    review_dir = Path(review_dir)
    rows = []
    for item in held_items:
        slug = slugs.get(str(item.id))
        if not slug:
            continue
        files = sorted(p.name for p in review_dir.glob(f"*-{slug}-*.md"))
        if not files:
            continue
        record = held[str(item.id)]
        rows.append({
            "slug": slug,
            "title": titles.get(str(item.id)) or item.title,
            "category": record.category,
            "reasons": record.reasons,
            "source": publisher_name(item),
            "url": original_url(item),
            "files": files,
        })
    if not rows:
        return None
    path = review_dir / f"held-e{edition}.json"
    path.write_text(json.dumps({
        "held_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "stories": rows,
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    return str(path)
