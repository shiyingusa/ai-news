"""Export each selected story as its own page for the Jekyll site.

Every story becomes ``docs/_stories/<date>-<slug>-<lang>.md`` with structured
front matter (section, rank, score, source, dek, tags) and the enriched blocks
as the body. English and Chinese twins share one slug so the site can link
between them.
"""

from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from pathlib import Path
from typing import TYPE_CHECKING, Dict, List, Optional

from ..storage.manager import safe_output_path

if TYPE_CHECKING:  # pragma: no cover
    from ..ai.summarizer import DailySummarizer
    from ..models import ContentItem

SOURCE_TYPE_NAMES = {
    "hackernews": "Hacker News",
    "google_news": "Google News",
    "reddit": "Reddit",
    "github": "GitHub",
}



def slugify(text: str, max_len: int = 72) -> str:
    """ASCII URL slug; empty when the text has no Latin characters."""
    normalized = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", normalized).strip("-").lower()
    if len(slug) > max_len:
        slug = slug[:max_len].rsplit("-", 1)[0]
    return slug


def _short_hash(value: str) -> str:
    return hashlib.sha1(value.encode("utf-8")).hexdigest()[:8]


_ABBREV = re.compile(
    r"(?:\b(?:[A-Z]\.){1,3}|\b(?:Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec|Mr|Mrs|Ms|Dr|St|Inc|Corp|Co|Ltd|vs|No|approx|est)\.)$"
)


def _sentences(text: str) -> List[str]:
    """Split into sentences without breaking on abbreviations such as "Nov." or "U.S."."""
    parts, start = [], 0
    for match in re.finditer(r"[.!?。！？](?=\s+[A-Z0-9\"“‘(]|\s*$|(?<=[。！？]))", text):
        end = match.end()
        chunk = text[start:end]
        if match.group(0) == "." and _ABBREV.search(chunk.rstrip()):
            continue
        parts.append(chunk.strip())
        start = end
    tail = text[start:].strip()
    if tail:
        parts.append(tail)
    return [p for p in parts if p]


def make_dek(text: str, limit: int = 240, minimum: int = 90) -> str:
    """Opening sentence(s) of the lead for cards and meta descriptions."""
    text = " ".join(text.split())
    if len(text) <= limit:
        return text
    dek = ""
    for sentence in _sentences(text):
        candidate = f"{dek} {sentence}".strip() if dek and not dek.endswith(("。", "！", "？")) else f"{dek}{sentence}" if dek else sentence
        if len(candidate) > limit:
            break
        dek = candidate
        if len(dek) >= minimum:
            break
    if not dek:
        cut = text[: limit - 1]
        for mark in ("; ", " — ", "—", ", ", "，", "；"):
            pos = cut.rfind(mark)
            if pos >= minimum:
                cut = cut[:pos]
                break
        else:
            cut = cut.rsplit(" ", 1)[0] if " " in cut else cut
        dek = cut.rstrip(",;，；— ") + "…"
    return dek


def _date_label(date: str) -> str:
    from datetime import date as _date

    d = _date.fromisoformat(date)
    return f"{d:%b} {d.day}, {d.year}"


def topic_slug(tag: str) -> str:
    return slugify(str(tag), max_len=48)


def write_topic_stub(topics_root: Path, tag: str, slug: str) -> None:
    """One English and one Chinese topic page per tag; the layout lists the stories."""
    for lang, prefix in (("en", ""), ("zh", "/zh")):
        folder = topics_root if lang == "en" else topics_root.parent / "zh" / topics_root.name
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / f"{slug}.md"
        if path.exists():
            continue
        path.write_text(
            "---\n"
            "layout: topic\n"
            f"lang: {lang}\n"
            f"topic: {_yaml(slug)}\n"
            f"title: {_yaml(str(tag))}\n"
            f"permalink: {_yaml(f'{prefix}/topics/{slug}/')}\n"
            "---\n",
            encoding="utf-8",
        )


def _yaml(value) -> str:
    """JSON is valid YAML; it quotes and escapes safely."""
    return json.dumps(value, ensure_ascii=False)


def _source_name(item: "ContentItem") -> str:
    meta = item.metadata or {}
    if meta.get("feed_name"):
        return str(meta["feed_name"])
    if meta.get("subreddit"):
        return f"Reddit r/{meta['subreddit']}"
    source_type = item.source_type.value
    base = SOURCE_TYPE_NAMES.get(source_type, source_type)
    if item.author and source_type in {"github"}:
        return f"{base} · {item.author}"
    return base


def export_stories(
    summarizer: "DailySummarizer",
    items: List["ContentItem"],
    date: str,
    language: str,
    out_dir: Path,
    slug_map: Dict[str, str],
    *,
    issue_time: str = "06:00:00 -0500",
    images_root: Optional[Path] = None,
    topics_root: Optional[Path] = None,
    slug_titles: Optional[Dict[str, str]] = None,
    photo_queries: Optional[Dict[str, List[str]]] = None,
    used_photos: Optional[set] = None,
) -> List[Path]:
    """Write one Markdown page per story; returns the written paths.

    ``slug_map`` maps item IDs to slugs. Call the English pass first so the
    Chinese twin reuses the English slug.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    slug_titles = slug_titles if slug_titles is not None else {}
    used_photos = used_photos if used_photos is not None else set()
    view = summarizer.build_view(items, language)
    written: List[Path] = []
    y, m, d = date.split("-")

    for group in view.groups:
        for view_item in group.items:
            item = view_item.item
            processing = item.processing
            artifact = processing.artifacts.get(language) if processing else None
            analysis = processing.analysis if processing else None

            title = (artifact.title if artifact else None) or view_item.title or item.title
            item_key = str(item.id)
            slug = slug_map.get(item_key)
            if not slug:
                slug = slugify(title) if language == "en" else ""
                if not slug:
                    slug = slugify(item.title) or f"story-{_short_hash(str(item.url))}"
                slug = f"{slug}-{_short_hash(str(item.url))[:4]}"
                slug_map[item_key] = slug

            blocks = artifact.blocks if artifact else []
            primary = next((b for b in blocks if b.primary), None)
            lead = (primary.content if primary else "") or (analysis.summary if analysis else "")
            extra_blocks = [b for b in blocks if not b.primary and b.content.strip()]

            meta = item.metadata or {}
            discussion = meta.get("discussion_url")
            if discussion and str(discussion) == str(item.url):
                discussion = None
            score = analysis.score if analysis and analysis.score is not None else None
            tags = list(analysis.tags) if analysis and analysis.tags else []

            prefix = "" if language == "en" else "/zh"
            permalink = f"{prefix}/{y}/{m}/{d}/{slug}/"

            # Licensed photo when one fits, otherwise the original radar artwork.
            # Drawn once per story (the English pass runs first); credit kept in a sidecar.
            image_rel = f"/assets/stories/{date}/{slug}.jpg"
            share_rel = f"/assets/stories/{date}/{slug}-share.jpg"
            credit = None
            if images_root is not None:
                day_dir = images_root / date
                art_file = day_dir / f"{slug}.jpg"
                credit_file = day_dir / f"{slug}.json"
                share_title = title if language == "en" else (slug_titles.get(item_key) or title)
                if not art_file.exists():
                    try:
                        from .story_images import make_share_from_photo, make_story_images
                        from .story_photos import find_photo, save_photo

                        photo = None
                        queries = (photo_queries or {}).get(item_key)
                        if queries:
                            photo = find_photo(queries, used_photos)
                            if photo and not save_photo(photo, day_dir, slug):
                                photo = None
                        if photo:
                            make_share_from_photo(art_file, day_dir / f"{slug}-share.jpg", share_title, group.profile_id, _date_label(date))
                            credit_file.write_text(json.dumps(photo.credit(), ensure_ascii=False), encoding="utf-8")
                        else:
                            make_story_images(day_dir, slug, share_title, group.profile_id, _date_label(date))
                    except Exception:  # images are optional
                        image_rel = share_rel = None
                if credit_file.exists():
                    credit = json.loads(credit_file.read_text(encoding="utf-8"))
            if language == "en":
                slug_titles[item_key] = title

            topic_slugs = [t for t in (topic_slug(tag) for tag in tags) if t]
            if topics_root is not None:
                for tag, tslug in zip(tags, topic_slugs):
                    write_topic_stub(topics_root, tag, tslug)
            front = [
                "---",
                "layout: story",
                f"lang: {language}",
                f"date: {date} {issue_time}",
                f"issue: {_yaml(date)}",
                f"story_id: {_yaml(slug)}",
                f"permalink: {_yaml(permalink)}",
                f"title: {_yaml(title)}",
                f"dek: {_yaml(make_dek(lead, *((120, 45) if language == 'zh' else (240, 90))))}",
                f"section: {_yaml(group.profile_id)}",
                f"rank: {view_item.global_index}",
                f"section_rank: {view_item.index}",
                f"score: {_yaml(score)}",
                f"source_name: {_yaml(_source_name(item))}",
                f"source_url: {_yaml(str(item.url))}",
                f"discussion_url: {_yaml(str(discussion) if discussion else None)}",
                f"published_at: {_yaml(item.published_at.isoformat() if item.published_at else None)}",
                f"tags: {_yaml(tags)}",
                f"topics: {_yaml(topic_slugs)}",
                f"order: {_yaml(f'{y}{m}{d}-{999 - view_item.global_index:03d}')}",
                f"image: {_yaml(share_rel)}",
                f"art: {_yaml(image_rel)}",
                f"thumb: {_yaml(image_rel.replace('.jpg', '-640.jpg') if image_rel else None)}",
                f"photo_credit: {_yaml(credit)}",
                "---",
                "",
            ]

            body: List[str] = ["{% raw %}", '<div class="story-lead" markdown="1">', "", lead.strip(), "", "</div>", ""]
            for block in extra_blocks:
                body.extend([f"## {block.title.strip()}", "", block.content.strip(), ""])
            sources = artifact.sources if artifact else []
            if sources:
                heading = "Further reading" if language == "en" else "延伸阅读"
                body.extend([f"## {heading}", ""])
                for source in sources:
                    body.append(f"- [{source.title.strip() or source.url}]({source.url})")
                body.append("")
            body.append("{% endraw %}")

            path = safe_output_path(out_dir, f"{date}-{slug}-{language}.md")
            path.write_text("\n".join(front + body) + "\n", encoding="utf-8")
            written.append(path)
    return written
