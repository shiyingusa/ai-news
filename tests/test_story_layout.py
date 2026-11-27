from src.services.story_layout import restructure_body, split_lead, split_sentences


def test_split_keeps_abbreviations():
    s = split_sentences("The U.S. Commerce Dept. said so. Nvidia agreed. Shares rose 3%.", "en")
    assert s == ["The U.S. Commerce Dept. said so.", "Nvidia agreed.", "Shares rose 3%."]


def test_split_lead_two_per_paragraph():
    out = split_lead("One. Two. Three. Four. Five.", "en")
    assert out == "One. Two.\n\nThree. Four.\n\nFive."
    assert split_lead("Short. Lead.", "en") == "Short. Lead."


def test_split_lead_chinese():
    out = split_lead("第一句。第二句。第三句！", "zh")
    assert out == "第一句。第二句。\n\n第三句！"


def test_restructure_moves_community_to_end():
    body = (
        '{% raw %}\n<div class="story-lead" markdown="1">\n\nOne here. Two here. Three here.\n\n</div>\n\n'
        "## Background\n\nbg\n\n## Community discussion\n\nPeople argue.\n\n## Further reading\n\n- x\n\n{% endraw %}\n"
    )
    out = restructure_body(body, "en")
    assert "One here. Two here.\n\nThree here." in out
    assert out.index("Further reading") < out.index("opinion, not evidence")
    assert out.count("Community discussion") == 1
    assert restructure_body(out, "en") == out
