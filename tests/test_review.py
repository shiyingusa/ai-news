"""Tests for the high-risk story rule."""

from datetime import datetime, timezone

from src.models import (
    ClassificationResult,
    ContentAnalysis,
    ContentArtifact,
    ContentBlock,
    ContentItem,
    ProcessingResult,
    SourceType,
)
from src.services.review import assess, parse_risk, split_held


def _item(risk: str, title_en: str, title_zh: str = "示例标题", related=None) -> ContentItem:
    def art(lang, title):
        return ContentArtifact(
            language=lang,
            title=title,
            blocks=[
                ContentBlock(id="summary", title="Summary", content="One. Two.", primary=True),
                ContentBlock(id="risk", title="Risk", content=risk),
            ],
            sources=[],
        )

    return ContentItem(
        id=f"rss:{abs(hash(title_en))}",
        source_type=SourceType.RSS,
        title=title_en,
        url="https://www.reuters.com/a",
        published_at=datetime(2026, 11, 16, tzinfo=timezone.utc),
        profile="tech-industry",
        metadata={"feed_name": "Reuters", "related": related or []},
        processing=ProcessingResult(
            classification=ClassificationResult(profile="tech-industry", method="source_override"),
            analysis=ContentAnalysis(score=8, reason="r", summary="s"),
            artifacts={"en": art("en", title_en), "zh": art("zh", title_zh)},
        ),
    )


def test_parse_risk():
    assert parse_risk("allegation | primary").category == "allegation"
    assert parse_risk("allegation | primary").sourcing == "primary"
    assert parse_risk("none").category is None
    assert parse_risk("").category is None


def test_ordinary_story_publishes():
    assert assess(_item("none", "Meituan releases LongCat-2.5")) is None


def test_single_source_casualty_is_held():
    held = assess(_item("casualty | single", "Factory fire kills three, Reuters reports"))
    assert held and held.category == "casualty"


def test_two_publishers_casualty_publishes():
    related = [{"url": "https://apnews.com/b", "title": "Fire", "feed_name": "AP News"}]
    assert assess(_item("casualty | single", "Factory fire kills three", related=related)) is None


def test_primary_allegation_needs_attribution_in_both_headlines():
    assert assess(_item("allegation | primary", "SEC charges startup with fraud", "美国证交会指控初创公司欺诈")) is None
    held = assess(_item("allegation | primary", "Startup committed fraud", "初创公司欺诈"))
    assert held and len(held.reasons) == 2


def test_split_held():
    ok = _item("none", "Plain news")
    bad = _item("accident | single", "Rocket explodes on pad")
    publish, held_items, held = split_held([ok, bad])
    assert publish == [ok] and held_items == [bad] and str(bad.id) in held
