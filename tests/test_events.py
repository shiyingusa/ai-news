"""Tests for event records built from story files."""

from pathlib import Path

from src.services.events import build_event, confidence, source_tier

STORY = """---
layout: story
lang: {lang}
issue: "2026-11-14"
story_id: "spacex-catch-73d9"
permalink: "/2026/11/14/spacex-catch-73d9/"
title: "SpaceX catches Starship"
section: "space"
score: 9.0
status: "Demonstrated"
source_name: "X (Twitter)"
source_url: "https://x.com/SpaceX/status/1"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=1"
published_at: "2026-11-14T10:00:00+00:00"
redirect_from:
  - /2026/11/14/old-one/
---

- **Verified:** Ship 42 was caught.
- **Not yet confirmed:** Why the booster aborted.

## Coverage of this story

- 2026-11-14 · Ars Technica: [Flight 15 reaches orbit](https://arstechnica.com/a)
- 2026-11-14 · Space.com: [Booster aborts](https://www.space.com/b)
"""


def test_source_tiers():
    assert source_tier("https://www.nasa.gov/x") == "primary"
    assert source_tier("https://github.com/ggml-org/ggml") == "primary"
    assert source_tier("https://www.reuters.com/x") == "independent"
    assert source_tier("https://news.ycombinator.com/item?id=1") == "community"


def test_confidence_rule():
    p = {"tier": "primary", "name": "SpaceX"}
    a = {"tier": "independent", "name": "Ars"}
    b = {"tier": "independent", "name": "Space.com"}
    c = {"tier": "community", "name": "HN"}
    assert confidence([p, a], "demonstrated")["level"] == "high"
    assert confidence([a, b], "reported")["level"] == "high"
    assert confidence([p], "released")["level"] == "medium"
    assert confidence([a], "reported")["level"] == "medium"
    assert confidence([c], "reported")["level"] == "low"
    assert confidence([p, a, b], "rumored")["level"] == "low"


def test_build_event(tmp_path: Path):
    files = {}
    for lang in ("en", "zh"):
        path = tmp_path / f"2026-11-14-spacex-catch-73d9-{lang}.md"
        path.write_text(STORY.format(lang=lang), encoding="utf-8")
        files[lang] = path
    event = build_event(files)
    assert event["event_id"] == "spacex-catch-73d9"
    assert event["status"] == "demonstrated" and event["status_step"] == 5
    assert event["confidence"]["level"] == "high"
    assert [s["tier"] for s in event["sources"]] == ["primary", "independent", "independent", "community"]
    assert event["facts"]["en"]["verified"] == ["Ship 42 was caught."]
    assert event["merged_urls"] == ["/2026/11/14/old-one/"]
    assert event["languages"] == ["en", "zh"]
