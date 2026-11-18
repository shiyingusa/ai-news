"""Export each selected story as its own page for the Jekyll site.

Every story becomes ``docs/_stories/<date>-<slug>-<lang>.md`` with structured
front matter (section, rank, score, source, dek, tags) and the enriched blocks
as the body. English and Chinese twins share one slug so the site can link
between them.
"""

from __future__ import annotations

import hashlib
import json
import os
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


# Feeds that point at other publishers' stories rather than publishing their own.
AGGREGATOR_FEEDS = ("techmeme", "google news", "hacker news", "reddit", "lobsters")

KNOWN_PUBLISHERS = {
    "reuters.com": "Reuters", "bloomberg.com": "Bloomberg", "wsj.com": "The Wall Street Journal",
    "nytimes.com": "The New York Times", "ft.com": "Financial Times", "cnbc.com": "CNBC",
    "theverge.com": "The Verge", "techcrunch.com": "TechCrunch", "arstechnica.com": "Ars Technica",
    "wired.com": "WIRED", "forbes.com": "Forbes", "axios.com": "Axios", "apnews.com": "AP News",
    "bbc.com": "BBC", "bbc.co.uk": "BBC", "theguardian.com": "The Guardian", "nature.com": "Nature",
    "science.org": "Science", "electrek.co": "Electrek", "insideevs.com": "InsideEVs",
    "spacenews.com": "SpaceNews", "space.com": "Space.com", "tomshardware.com": "Tom's Hardware",
    "anandtech.com": "AnandTech", "semianalysis.com": "SemiAnalysis", "ieee.org": "IEEE Spectrum",
    "technologyreview.com": "MIT Technology Review", "github.com": "GitHub", "arxiv.org": "arXiv",
    "x.com": "X (Twitter)", "twitter.com": "X (Twitter)", "youtube.com": "YouTube",
    "openai.com": "OpenAI", "anthropic.com": "Anthropic", "blog.google": "Google",
    "deepmind.google": "Google DeepMind", "nvidia.com": "NVIDIA", "tesla.com": "Tesla",
    "spacex.com": "SpaceX", "nasa.gov": "NASA", "huggingface.co": "Hugging Face",
    "businessinsider.com": "Business Insider", "engadget.com": "Engadget", "zdnet.com": "ZDNET",
    "venturebeat.com": "VentureBeat", "theregister.com": "The Register", "scmp.com": "South China Morning Post",
    "nikkei.com": "Nikkei Asia", "asia.nikkei.com": "Nikkei Asia", "36kr.com": "36Kr",
}


def _host(url: str) -> str:
    from urllib.parse import urlparse

    host = (urlparse(url).hostname or "").lower()
    return host[4:] if host.startswith("www.") else host


def original_url(item: "ContentItem") -> str:
    meta = item.metadata or {}
    return str(meta.get("original_url") or item.url)


def publisher_name(item: "ContentItem") -> str:
    """Who actually published the story, not the channel we found it on."""
    meta = item.metadata or {}
    if meta.get("publisher"):
        return str(meta["publisher"])
    host = _host(original_url(item))
    feed = str(meta.get("feed_name") or "")
    if feed and not any(a in feed.lower() for a in AGGREGATOR_FEEDS) and item.source_type.value == "rss":
        return feed
    for known, name in KNOWN_PUBLISHERS.items():
        if host == known or host.endswith("." + known):
            return name
    if item.source_type.value == "github" or host == "github.com":
        return "GitHub"
    if item.source_type.value == "reddit" and host in {"reddit.com", "old.reddit.com", "i.redd.it", ""}:
        return f"Reddit r/{meta.get('subreddit')}" if meta.get("subreddit") else "Reddit"
    if item.source_type.value == "hackernews" and host in {"news.ycombinator.com", ""}:
        return "Hacker News"
    return host or feed or SOURCE_TYPE_NAMES.get(item.source_type.value, item.source_type.value)


COMMUNITY_HOSTS = {"reddit.com", "old.reddit.com", "i.redd.it", "news.ycombinator.com", "lobste.rs"}
# Links worth promoting over a community post: the paper, the code, the official page, a real outlet.
PRIMARY_LINK = re.compile(
    r"https?://(?:www\.)?(?:arxiv\.org/(?:abs|pdf)/[\w.\-/]+|github\.com/[\w.\-]+/[\w.\-]+|"
    r"huggingface\.co/[\w.\-/]+|[\w.\-]+\.(?:gov|edu)(?:/[^\s)\]\"'<>]*)?|"
    r"(?:openai\.com|anthropic\.com|blog\.google|deepmind\.google|ai\.meta\.com|nvidia\.com|spacex\.com)(?:/[^\s)\]\"'<>]*)?)",
    re.I,
)


def promote_primary_link(item: "ContentItem") -> None:
    """A Reddit/HN self-post is a discovery channel, not the source: when the post links
    the paper, repository or official page, credit that and keep the community as `via`."""
    meta = item.metadata if item.metadata is not None else {}
    if meta.get("publisher") or _host(original_url(item)) not in COMMUNITY_HOSTS:
        return
    m = PRIMARY_LINK.search(item.content or "")
    if not m:
        return
    via = publisher_name(item)
    link = m.group(0).rstrip(".,;")
    meta["original_url"] = link
    meta.setdefault("discovered_via", via)
    if "arxiv.org" in link:
        meta["publisher"] = "arXiv"
    item.metadata = meta


def discovered_via(item: "ContentItem") -> Optional[str]:
    """The aggregator or community where the story surfaced, if not the publisher."""
    meta = item.metadata or {}
    if meta.get("discovered_via"):
        via = str(meta["discovered_via"])
    elif item.source_type.value == "hackernews":
        via = "Hacker News"
    elif item.source_type.value == "reddit":
        via = f"Reddit r/{meta['subreddit']}" if meta.get("subreddit") else "Reddit"
    elif meta.get("feed_name") and any(a in str(meta["feed_name"]).lower() for a in AGGREGATOR_FEEDS):
        via = str(meta["feed_name"])
    else:
        return None
    return None if via == publisher_name(item) else via


# 0 = the morning issue; 1, 2 = midday and evening updates to the same day.
EDITION = int(os.environ.get("EDITION", "0") or 0)


def _publish_time(date: str) -> str:
    """The real time of publishing (America/New_York) for today's issue, so datePublished
    and the news sitemap match when the story went up; 06:00 for any other day."""
    from datetime import datetime
    from zoneinfo import ZoneInfo

    now = datetime.now(ZoneInfo("America/New_York"))
    if now.strftime("%Y-%m-%d") != date:
        return "06:00:00 -0500"
    return now.strftime("%H:%M:%S %z")


class PublicationHalted(RuntimeError):
    """Too many stories failed the publication gate; publish nothing today."""


BAD_OUTPUT = re.compile(
    r"as an ai\b|i (?:cannot|can't) (?:access|browse)|unable to access the (?:article|link)|"
    r"无法访问|作为(?:一个)?(?:AI|人工智能)|lorem ipsum",
    re.I,
)


# Words from our own pipeline that leaked into stories ("the source item says",
# "the supplied text", "现有材料"). Readers should see "the report", never our plumbing.
PROCESS_TERMS = [
    (re.compile(r"\b(?:the|this) (?:source item|source text|supplied text|provided text|provided excerpt|available excerpt|excerpt|input text|item)\b(?= (?:says|said|states|notes|does|did|is|was|gives|mentions|describes|reports))", re.I), "the report"),
    (re.compile(r"\b(?:the|this) (?:source item|supplied text|provided text|available excerpt|provided excerpt|input text)\b", re.I), "the report"),
    (re.compile(r"\b(?:available|supplied|provided) (?:excerpt|text|material)s?\b", re.I), "available reporting"),
    (re.compile(r"\bsource item\b", re.I), "report"),
    (re.compile(r"(?:现有|所给|提供的|给定的|已有)(?:材料|摘录|文本|素材)"), "现有报道"),
]


def scrub_process_terms(text: str) -> str:
    def keep_case(replacement):
        return lambda m: replacement[:1].upper() + replacement[1:] if m.group(0)[:1].isupper() else replacement
    for pattern, replacement in PROCESS_TERMS:
        text = pattern.sub(keep_case(replacement), text)
    return text


OUTLET_PREFIX = re.compile(
    r"^(WSJ|NYT|FT|Bloomberg|Reuters|The Information|Nikkei|CNBC|Axios|Semafor|The Verge|TechCrunch|"
    r"华尔街日报|纽约时报|金融时报|彭博社?|路透社?|日经)\s*[:：]\s*(.+)$")
OUTLET_ZH = {"WSJ": "《华尔街日报》", "NYT": "《纽约时报》", "FT": "《金融时报》", "Bloomberg": "彭博社",
             "Reuters": "路透社", "Nikkei": "日经", "华尔街日报": "《华尔街日报》", "纽约时报": "《纽约时报》",
             "金融时报": "《金融时报》"}


def fix_outlet_prefix(title: str, language: str) -> str:
    """'WSJ: Nvidia chips…' -> 'Nvidia chips…, WSJ reports' (attribution belongs at the end)."""
    m = OUTLET_PREFIX.match((title or "").strip())
    if not m:
        return title
    outlet, rest = m.group(1), m.group(2).rstrip("。. ")
    if language == "zh":
        return f"{rest}，{OUTLET_ZH.get(outlet, outlet)}报道"
    return f"{rest}, {outlet} reports"


def gate_problems(title: str, lead: str, language: str) -> List[str]:
    """Reasons a story is not fit to publish; empty when it passes."""
    problems = []
    if not title or len(title.strip()) < (4 if language == "zh" else 8):
        problems.append("missing title")
    minimum = 20 if language == "zh" else 40
    if len((lead or "").strip()) < minimum:
        problems.append("summary too short")
    if BAD_OUTPUT.search(f"{title}\n{lead}"):
        problems.append("model failure text")
    return problems


STATUSES = ("Rumored", "Planned", "Announced", "Demonstrated", "Released", "Available")


def story_status(text: str) -> Optional[str]:
    """The one allowed status word in a status block, or None."""
    words = re.findall(r"[A-Za-z]+", text or "")
    for word in words:
        for status in STATUSES:
            if word.lower() == status.lower():
                return status
    return None


def _fact_lines(text: str) -> str:
    """Put the Verified / Not yet confirmed lines on separate list items."""
    text = text.strip()
    parts = re.split(r"\s*(?=(?:Not yet confirmed:|尚未证实：|Verified:|已证实：))", text)
    parts = [p.strip() for p in parts if p.strip()]
    if len(parts) < 2:
        return text
    out = []
    for part in parts:
        match = re.match(r"(Not yet confirmed:|尚未证实：|Verified:|已证实：)\s*(.*)", part, re.S)
        out.append(f"- **{match.group(1)}** {match.group(2)}" if match else f"- {part}")
    return "\n".join(out)


def _coverage(item: "ContentItem") -> List[str]:
    """Markdown lines for every report merged into this story, oldest first."""
    from types import SimpleNamespace

    related = (item.metadata or {}).get("related") or []
    if not related:
        return []
    rows = []
    entries = [{
        "title": item.title, "url": original_url(item), "published_at": item.published_at.isoformat() if item.published_at else None,
        "name": publisher_name(item),
    }]
    for r in related:
        fake = SimpleNamespace(
            metadata={k: r.get(k) for k in ("feed_name", "publisher")} | {"original_url": r.get("url")},
            url=r.get("url"), source_type=SimpleNamespace(value=r.get("source_type") or "rss"),
        )
        entries.append({"title": r.get("title") or r.get("url"), "url": r.get("url"), "published_at": r.get("published_at"), "name": publisher_name(fake)})
    seen = set()
    for e in sorted(entries, key=lambda e: e["published_at"] or ""):
        if not e["url"] or e["url"] in seen:
            continue
        seen.add(e["url"])
        when = (e["published_at"] or "")[:10]
        title = str(e["title"]).replace("[", "(").replace("]", ")")
        rows.append(f"{when + ' · ' if when else ''}{e['name']}: [{title}]({e['url']})")
    return rows if len(rows) > 1 else []


def _source_name(item: "ContentItem") -> str:
    return publisher_name(item)


def export_stories(
    summarizer: "DailySummarizer",
    items: List["ContentItem"],
    date: str,
    language: str,
    out_dir: Path,
    slug_map: Dict[str, str],
    *,
    issue_time: Optional[str] = None,
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

    # Publication gate: drop stories that are not fit to publish, and stop the
    # whole issue (circuit breaker) when failures look systemic.
    rejected: Dict[str, List[str]] = {}
    total = 0
    for group in view.groups:
        for view_item in group.items:
            total += 1
            it = view_item.item
            art = it.processing.artifacts.get(language) if it.processing else None
            if art is None:
                rejected[str(it.id)] = ["no article in this language"]
                continue
            promote_primary_link(it)
            art.title = fix_outlet_prefix(scrub_process_terms(art.title or ""), language)
            for block in art.blocks:
                block.content = scrub_process_terms(block.content or "")
            prim = next((b for b in art.blocks if b.primary), None)
            lead_text = (prim.content if prim else "") or (it.processing.analysis.summary if it.processing.analysis else "")
            problems = gate_problems(art.title or view_item.title or it.title, lead_text, language)
            if problems:
                rejected[str(it.id)] = problems
    if total and (len(rejected) == total or (total >= 8 and len(rejected) / total > 0.4)):
        raise PublicationHalted(f"{len(rejected)} of {total} {language} stories failed the publication gate")

    for group in view.groups:
        for view_item in group.items:
            item = view_item.item
            if str(item.id) in rejected:
                continue
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
            extra_blocks = [b for b in blocks if not b.primary and b.content.strip() and b.id not in ("status", "risk")]
            # One status per story: both languages take the English call, so they never disagree.
            en_art = processing.artifacts.get("en") if processing else None
            status_blocks = en_art.blocks if en_art else blocks
            status = story_status(next((b.content for b in status_blocks if b.id == "status"), ""))
            if status is None:
                status = story_status(next((b.content for b in blocks if b.id == "status"), ""))
            # Product words (Released, Available) make no sense on a crash, a lawsuit or a death.
            from .review import parse_risk
            risk_text = next((b.content for b in status_blocks if b.id == "risk"), "")
            if parse_risk(risk_text).category and status in ("Released", "Available", "Demonstrated"):
                status = None

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
                        queries = (photo_queries or {}).get(item_key) or []
                        photo = find_photo(queries, used_photos, section=group.profile_id)
                        if photo:
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
                f"date: {date} {issue_time or _publish_time(date)}",
                f"issue: {_yaml(date)}",
                f"story_id: {_yaml(slug)}",
                f"permalink: {_yaml(permalink)}",
                f"title: {_yaml(title)}",
                f"dek: {_yaml(make_dek(lead, *((120, 45) if language == 'zh' else (240, 90))))}",
                f"description: {_yaml(make_dek(lead, *((120, 45) if language == 'zh' else (240, 90))))}",
                f"section: {_yaml(group.profile_id)}",
                f"rank: {EDITION * 100 + view_item.global_index}",
                f"edition: {EDITION}",
                f"section_rank: {view_item.index}",
                f"score: {_yaml(score)}",
                f"status: {_yaml(status)}",
                f"source_name: {_yaml(_source_name(item))}",
                f"source_url: {_yaml(original_url(item))}",
                f"via: {_yaml(discovered_via(item))}",
                f"discussion_url: {_yaml(str(discussion) if discussion else None)}",
                f"published_at: {_yaml(item.published_at.isoformat() if item.published_at else None)}",
                f"tags: {_yaml(tags)}",
                f"topics: {_yaml(topic_slugs)}",
                f"order: {_yaml(f'{y}{m}{d}-{EDITION}-{999 - view_item.global_index:03d}')}",
                f"image: {_yaml(share_rel)}",
                f"art: {_yaml(image_rel)}",
                f"thumb: {_yaml(image_rel.replace('.jpg', '-640.jpg') if image_rel else None)}",
                f"photo_credit: {_yaml(credit)}",
                "---",
                "",
            ]

            body: List[str] = ["{% raw %}", '<div class="story-lead" markdown="1">', "", lead.strip(), "", "</div>", ""]
            for block in extra_blocks:
                if block.id == "fact_check":
                    body.extend(['<div class="fact-check" markdown="1">', "", f"## {block.title.strip()}", "", _fact_lines(block.content), "", "</div>", ""])
                    continue
                body.extend([f"## {block.title.strip()}", "", block.content.strip(), ""])
            coverage = _coverage(item)
            if coverage:
                heading = "Coverage of this story" if language == "en" else "本事件的相关报道"
                body.extend([f"## {heading}", ""])
                for entry in coverage:
                    body.append(f"- {entry}")
                body.append("")
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
