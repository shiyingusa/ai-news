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


def test_export_uses_licensed_photo_and_records_credit(tmp_path, monkeypatch):
    from PIL import Image

    from src.services import story_photos

    def fake_find(queries, used, client=None):
        assert queries == ["SpaceX Starship rocket", "rocket launch pad"]
        return story_photos.Photo(
            url="https://upload.example/x.jpg", author="Jane Doe", licence="CC BY-SA 4.0",
            licence_url="https://creativecommons.org/licenses/by-sa/4.0", source_url="https://commons.example/File:x.jpg",
            provider="Wikimedia Commons", width=2000, height=1200,
        )

    def fake_save(photo, out_dir, slug, client=None):
        out_dir.mkdir(parents=True, exist_ok=True)
        Image.new("RGB", (1200, 675), (40, 60, 90)).save(out_dir / f"{slug}.jpg")
        Image.new("RGB", (560, 315), (40, 60, 90)).save(out_dir / f"{slug}-640.jpg")
        return True

    monkeypatch.setattr(story_photos, "find_photo", fake_find)
    monkeypatch.setattr(story_photos, "save_photo", fake_save)
    item = _item(1, "space", 9.0)
    summarizer = DailySummarizer(profile_names={"space": {"default": "Space"}}, profile_order=["space"])
    slugs: dict[str, str] = {}
    images = tmp_path / "img"
    queries = {"rss:item-1": ["SpaceX Starship rocket", "rocket launch pad"]}
    en = export_stories(summarizer, [item], "2026-11-14", "en", tmp_path / "s", slugs, images_root=images, photo_queries=queries)
    zh = export_stories(summarizer, [item], "2026-11-14", "zh", tmp_path / "s", slugs, images_root=images, photo_queries=queries)
    for path in (en[0], zh[0]):
        text = path.read_text(encoding="utf-8")
        assert '"author": "Jane Doe"' in text and '"provider": "Wikimedia Commons"' in text
    slug = slugs["rss:item-1"]
    assert (images / "2026-11-14" / f"{slug}-share.jpg").exists()


def test_status_and_gate_and_publisher():
    from types import SimpleNamespace
    from src.services.site_export import story_status, gate_problems, publisher_name, discovered_via, _fact_lines
    assert story_status("Demonstrated.") == "Demonstrated"
    assert story_status("已发布 Released") == "Released"
    assert story_status("unclear") is None
    assert gate_problems("A proper headline here", "x" * 200, "en") == []
    assert "summary too short" in gate_problems("A proper headline here", "short", "en")
    assert "model failure text" in gate_problems("A proper headline here", "As an AI, I cannot access the article. " * 5, "en")
    hn = SimpleNamespace(metadata={"discussion_url": "https://news.ycombinator.com/item?id=1"},
                         url="https://x.com/spacex/status/1", source_type=SimpleNamespace(value="hackernews"))
    assert publisher_name(hn) == "X (Twitter)" and discovered_via(hn) == "Hacker News"
    tm = SimpleNamespace(metadata={"feed_name": "Techmeme", "original_url": "https://www.reuters.com/a/b", "publisher": "Reuters", "discovered_via": "Techmeme"},
                         url="https://www.techmeme.com/261114/p11", source_type=SimpleNamespace(value="rss"))
    assert publisher_name(tm) == "Reuters" and discovered_via(tm) == "Techmeme"
    direct = SimpleNamespace(metadata={"feed_name": "Electrek"}, url="https://electrek.co/x/y", source_type=SimpleNamespace(value="rss"))
    assert publisher_name(direct) == "Electrek" and discovered_via(direct) is None
    lines = _fact_lines("Verified: SpaceX says it caught the ship. Not yet confirmed: reuse timeline.")
    assert lines.count("- **") == 2


def test_techmeme_original_link():
    from src.scrapers.rss import _original_link
    entry = {"link": "https://www.techmeme.com/261114/p18#a", "title": "Investors urge board (Katie Tarasov/CNBC)",
             "summary": '<A HREF="https://www.cnbc.com/2026/11/14/nvidia.html"><IMG SRC="x"></A>'}
    meta = _original_link(entry)
    assert meta == {"original_url": "https://www.cnbc.com/2026/11/14/nvidia.html", "publisher": "CNBC", "discovered_via": "Techmeme"}


def test_newsletter_email(tmp_path):
    import json as _j
    from src.services.newsletter import build_email
    p = tmp_path / "2026-11-15-a-en.md"
    p.write_text('---\nlayout: story\npermalink: "/2026/11/15/a/"\ntitle: "Chip story"\ndek: "Dek."\nrank: 1\nsource_name: "Reuters"\nstatus: "Released"\n---\nbody\n', encoding="utf-8")
    b = tmp_path / "brief.json"
    b.write_text(_j.dumps({"headline": "Big day", "paragraphs": ["P1"], "takeaways": ["T1"]}), encoding="utf-8")
    email = build_email("2026-11-15", [p], b)
    assert email["subject"].startswith("Big day")
    assert "https://aidailyradar.com/2026/11/15/a/" in email["body"] and "Reuters · Released" in email["body"]
