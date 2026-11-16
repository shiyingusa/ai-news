"""Event objects: one JSON record per story, shared by both languages.

The record carries what the new templates need and what readers are promised:
the status ladder step, a rule-based confidence level, sources sorted into
tiers, the verified / unconfirmed facts in each language, and the reports
merged into the story. It is built from the published story files, so the
same code backfills old stories and records new ones:

    python -m src.services.events docs          # after a pipeline run
    python -m src.services.events /path/to/gh-pages --all

Records go to <site>/_data/events/<story_id>.json (site.data.events in Jekyll).
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional
from urllib.parse import urlparse

LADDER = ("rumored", "reported", "announced", "released", "demonstrated", "verified")

# Existing status words -> (ladder step, planned flag)
STATUS_TO_LADDER = {
    "rumored": ("rumored", False),
    "planned": ("announced", True),
    "announced": ("announced", False),
    "released": ("released", False),
    "available": ("released", False),
    "demonstrated": ("demonstrated", False),
}

# The claimant's own record: official sites, filings, code, papers, posts.
PRIMARY_HOSTS = {
    "github.com", "arxiv.org", "huggingface.co", "x.com", "twitter.com", "sec.gov",
    "openai.com", "anthropic.com", "blog.google", "deepmind.google", "nvidia.com", "tesla.com",
    "spacex.com", "nasa.gov", "eff.org", "europa.eu", "courtlistener.com", "meta.com",
    "ai.meta.com", "microsoft.com", "apple.com", "amazon.com", "aboutamazon.com", "fbi.gov",
    "justice.gov", "federalregister.gov", "congress.gov", "esa.int",
}
PRIMARY_SUFFIXES = (".gov", ".mil", ".edu", ".gov.uk", ".gov.cn", ".europa.eu", ".int")
COMMUNITY_HOSTS = {
    "news.ycombinator.com", "reddit.com", "old.reddit.com", "youtube.com", "youtu.be",
    "lobste.rs", "v2ex.com", "weibo.com", "zhihu.com",
}

VERIFIED = re.compile(r"^\s*-\s*\*\*(?:Verified:|已证实：)\*\*\s*(.+)$", re.M)
UNCONFIRMED = re.compile(r"^\s*-\s*\*\*(?:Not yet confirmed:|尚未证实：)\*\*\s*(.+)$", re.M)
COVERAGE = re.compile(r"^-\s*(?:(\d{4}-\d{2}-\d{2})\s*·\s*)?([^:\n]+?):\s*\[([^\]]*)\]\((https?://[^)\s]+)\)\s*$", re.M)


def _host(url: str) -> str:
    host = (urlparse(url or "").hostname or "").lower()
    return host[4:] if host.startswith("www.") else host


def source_tier(url: str) -> str:
    """primary, independent or community, judged from the link's host."""
    host = _host(url)
    if not host:
        return "independent"
    if host in COMMUNITY_HOSTS or any(host.endswith("." + h) for h in COMMUNITY_HOSTS):
        return "community"
    if host in PRIMARY_HOSTS or any(host.endswith("." + h) for h in PRIMARY_HOSTS) or host.endswith(PRIMARY_SUFFIXES):
        return "primary"
    return "independent"


def confidence(sources: List[Dict], ladder_step: Optional[str]) -> Dict[str, str]:
    """High / medium / low from source diversity alone; never from a model."""
    primary = any(s["tier"] == "primary" for s in sources)
    independent = {s["name"].strip().lower() for s in sources if s["tier"] == "independent"}
    if ladder_step == "rumored":
        return {"level": "low", "reason": "rumor"}
    if (primary and independent) or len(independent) >= 2:
        level = "high"
    elif primary or len(independent) == 1:
        level = "medium"
    else:
        level = "low"
    reason = f"{'primary + ' if primary else ''}{len(independent)} independent"
    return {"level": level, "reason": reason}


def _front_matter(text: str) -> Dict:
    if not text.startswith("---"):
        return {}
    head = text.split("\n---", 1)[0][3:]
    data = {}
    for line in head.splitlines():
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if not m:
            continue
        key, raw = m.group(1), m.group(2).strip()
        try:
            data[key] = json.loads(raw) if raw else None
        except json.JSONDecodeError:
            data[key] = raw
    # redirect_from may be a YAML list on following lines
    lst = re.search(r"^redirect_from:\s*\n((?:\s+-\s+.+\n)+)", head + "\n", re.M)
    if lst:
        data["redirect_from"] = [re.sub(r"^\s+-\s+", "", l).strip().strip('"') for l in lst.group(1).splitlines()]
    return data


def _facts(body: str) -> Dict[str, List[str]]:
    return {
        "verified": [m.strip() for m in VERIFIED.findall(body)],
        "unconfirmed": [m.strip() for m in UNCONFIRMED.findall(body)],
    }


def build_event(files: Dict[str, Path]) -> Optional[Dict]:
    """One event record from a story's language files ({'en': path, 'zh': path})."""
    parsed = {}
    for lang, path in files.items():
        text = path.read_text(encoding="utf-8")
        parsed[lang] = (_front_matter(text), text.split("\n---", 1)[-1])
    if not parsed:
        return None
    lead_lang = "en" if "en" in parsed else next(iter(parsed))
    fm, body = parsed[lead_lang]
    story_id = fm.get("story_id")
    if not story_id:
        return None

    sources: List[Dict] = []
    seen = set()

    def add(name: Optional[str], url: Optional[str], tier: Optional[str] = None) -> None:
        if not url or url in seen:
            return
        seen.add(url)
        sources.append({"tier": tier or source_tier(url), "name": name or _host(url), "url": url})

    add(fm.get("source_name"), fm.get("source_url"))
    for _when, name, _title, url in COVERAGE.findall(body):
        add(name.strip(), url)
    if fm.get("discussion_url"):
        add(fm.get("via") or _host(fm["discussion_url"]), fm["discussion_url"], "community")

    status = str(fm.get("status") or "").strip().lower()
    step, planned = STATUS_TO_LADDER.get(status, (None, False))
    if step is None:
        step = "announced" if any(s["tier"] == "primary" for s in sources) else "reported"

    facts = {lang: _facts(b) for lang, (_f, b) in parsed.items()}
    return {
        "event_id": story_id,
        "issue": fm.get("issue"),
        "section": fm.get("section"),
        "published_at": fm.get("published_at"),
        "updated": fm.get("updated"),
        "status": step,
        "status_step": LADDER.index(step) + 1,
        "planned": planned,
        "status_label": fm.get("status"),
        "confidence": confidence(sources, step),
        "radar_score": fm.get("score"),
        "sources": sources,
        "discovered_via": fm.get("via"),
        "facts": facts,
        "has_fact_check": any(f["verified"] or f["unconfirmed"] for f in facts.values()),
        "languages": sorted(parsed),
        "titles": {lang: f.get("title") for lang, (f, _b) in parsed.items()},
        "permalinks": {lang: f.get("permalink") for lang, (f, _b) in parsed.items()},
        "merged_urls": fm.get("redirect_from") or [],
        "corrected": "correction-note" in body,
    }


def group_story_files(stories_dir: Path) -> Dict[str, Dict[str, Path]]:
    """story file stem without the language suffix -> {lang: path}."""
    groups: Dict[str, Dict[str, Path]] = {}
    for path in sorted(stories_dir.glob("*.md")):
        m = re.match(r"(.+)-(en|zh)$", path.stem)
        if m:
            groups.setdefault(m.group(1), {})[m.group(2)] = path
    return groups


def write_events(site: Path) -> List[Path]:
    out_dir = site / "_data" / "events"
    out_dir.mkdir(parents=True, exist_ok=True)
    written = []
    for files in group_story_files(site / "_stories").values():
        event = build_event(files)
        if not event:
            continue
        path = out_dir / f"{event['event_id']}.json"
        path.write_text(json.dumps(event, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        written.append(path)
    return written


if __name__ == "__main__":  # pragma: no cover
    site = Path(sys.argv[1] if len(sys.argv) > 1 else "docs")
    paths = write_events(site)
    print(f"Wrote {len(paths)} event records to {site / '_data' / 'events'}")
