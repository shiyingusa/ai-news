"""Tests for per-story page export used by the website."""

from datetime import datetime, timezone

from src.ai.summarizer import DailySummarizer
from src.models import (
    ArtifactSource,
    ClassificationResult,
    ContentAnalysis,
    ContentArtifact,
    ContentBlock,
    ContentItem,
    ProcessingResult,
    SourceType,
)
from src.services.site_export import export_stories, make_dek, slugify


def _item(idx: int, profile: str, score: float) -> ContentItem:
    def artifact(lang: str) -> ContentArtifact:
        title = f"Example Lab ships Model {idx}" if lang == "en" else f"示例实验室发布模型 {idx}"
        return ContentArtifact(
            language=lang,
            title=title,
            blocks=[
                ContentBlock(id="summary", title="Summary", content="First sentence. Second sentence {{ not liquid }}.", primary=True),
                ContentBlock(id="background", title="Background" if lang == "en" else "背景", content="Context."),
            ],
            sources=[ArtifactSource(id="w1", title="Reference", url="https://example.org/ref")],
        )

    return ContentItem(
        id=f"rss:item-{idx}",
        source_type=SourceType.RSS,
        title=f"Original {idx}",
        url=f"https://example.com/items/{idx}",
        author="tester",
        published_at=datetime(2026, 11, 14, 8, 0, tzinfo=timezone.utc),
        profile=profile,
        metadata={"feed_name": "Example Feed", "discussion_url": "https://news.example.com/1"},
        processing=ProcessingResult(
            classification=ClassificationResult(profile=profile, method="source_override"),
            analysis=ContentAnalysis(score=score, reason="r", summary="s", tags=["ai", "models"]),
            artifacts={"en": artifact("en"), "zh": artifact("zh")},
        ),
    )


def test_slugify_and_dek():
    assert slugify("Tesla's Cybercab: $29,990 orders open!") == "tesla-s-cybercab-29-990-orders-open"
    assert slugify("中文标题") == ""
    assert make_dek("One. Two.") == "One. Two."
    long = "A" * 300
    assert len(make_dek(long)) <= 241


def test_export_writes_twin_pages_with_shared_slug(tmp_path):
    items = [_item(1, "ai-news", 8.0), _item(2, "space", 9.0)]
    summarizer = DailySummarizer(
        profile_names={"ai-news": {"default": "AI"}, "space": {"default": "Space"}},
        profile_order=["ai-news", "space"],
    )
    slugs: dict[str, str] = {}
    images = tmp_path / "img"
    topics = tmp_path / "site" / "topics"
    en = export_stories(summarizer, items, "2026-11-14", "en", tmp_path, slugs, images_root=images, topics_root=topics)
    zh = export_stories(summarizer, items, "2026-11-14", "zh", tmp_path, slugs, images_root=images, topics_root=topics)

    assert len(en) == 2 and len(zh) == 2
    en_text = en[0].read_text(encoding="utf-8")
    assert "layout: story" in en_text
    assert 'section: "ai-news"' in en_text
    assert "rank: 1" in en_text
    assert '"/2026/11/14/example-lab-ships-model-1-' in en_text
    assert "{% raw %}" in en_text and "## Background" in en_text and "## Further reading" in en_text
    assert 'source_name: "Example Feed"' in en_text
    assert 'topics: ["ai", "models"]' in en_text
    assert 'order: "20261114-998"' in en_text
    slug1 = en[0].name[len("2026-11-14-"):-len("-en.md")]
    assert (images / "2026-11-14" / f"{slug1}.jpg").exists()
    assert (images / "2026-11-14" / f"{slug1}-share.jpg").exists()
    assert (images / "2026-11-14" / f"{slug1}-640.jpg").exists()
    assert (topics / "ai.md").exists() and (tmp_path / "site" / "zh" / "topics" / "ai.md").exists()

    zh_text = zh[0].read_text(encoding="utf-8")
    slug = slugs["rss:item-1"]
    assert f'"/zh/2026/11/14/{slug}/"' in zh_text
    assert "## 延伸阅读" in zh_text
    assert en[0].name.replace("-en.md", "") == zh[0].name.replace("-zh.md", "")
