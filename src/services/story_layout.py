"""Reader-facing shape of a story body: short opening paragraphs, empty
sections dropped, community talk kept apart from the facts."""

from __future__ import annotations

import re
from typing import List

# A full stop after these does not end a sentence.
_ABBREV = re.compile(
    r"(?:\b(?:U\.S|U\.K|U\.N|E\.U|Inc|Corp|Co|Ltd|Mr|Mrs|Ms|Dr|St|Jr|Sr|vs|No|Gen|Sen|Rep|Gov|Prof|approx|est|e\.g|i\.e|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)|\b[A-Z])\.$"
)
_EN_BREAK = re.compile(r"(?<=[.!?])([\"”’)]?)\s+(?=[A-Z0-9\"“‘(])")

EMPTY_BLOCK = re.compile(
    r"^\s*(?:n/?a\.?|none\.?|no (?:notable |community )?discussion\b.*|not available\b.*|暂无.*|无。?|没有.{0,10}讨论.*)\s*$",
    re.IGNORECASE | re.DOTALL,
)

COMMUNITY_HEADING = {
    "en": "Community discussion: opinion, not evidence",
    "zh": "社区讨论（观点，不是证据）",
}
COMMUNITY_TITLES = {"community discussion", "社区讨论", COMMUNITY_HEADING["en"].lower(), COMMUNITY_HEADING["zh"]}


def split_sentences(text: str, language: str) -> List[str]:
    text = text.strip()
    if language == "zh":
        parts = re.findall(r"[^。！？]+[。！？]+[”」』）)]*|[^。！？]+$", text.replace("\n", ""))
        return [p.strip() for p in parts if p.strip()]
    text = " ".join(text.split())
    pieces: List[str] = []
    last = 0
    for m in _EN_BREAK.finditer(text):
        pieces.append(text[last:m.start()] + m.group(1))
        last = m.end()
    pieces.append(text[last:])
    out: List[str] = []
    buf = ""
    for piece in pieces:
        buf = f"{buf} {piece}" if buf else piece
        if _ABBREV.search(buf.rstrip("\"”’)")):
            continue
        out.append(buf)
        buf = ""
    if buf:
        out.append(buf)
    return [s for s in out if s]


def split_lead(text: str, language: str, per_paragraph: int = 2) -> str:
    """Break one long opening paragraph into paragraphs of at most two sentences."""
    joiner = "" if language == "zh" else " "
    out: List[str] = []
    for para in re.split(r"\n\s*\n", text.strip()):
        para = para.strip()
        if not para:
            continue
        sentences = split_sentences(para, language)
        if len(sentences) <= per_paragraph:
            out.append(para)
            continue
        out.extend(joiner.join(sentences[i:i + per_paragraph]) for i in range(0, len(sentences), per_paragraph))
    return "\n\n".join(out)


def is_empty_block(content: str) -> bool:
    return not content.strip() or bool(EMPTY_BLOCK.match(content))


def is_community(title: str) -> bool:
    return title.strip().lower() in COMMUNITY_TITLES


def community_section(content: str, language: str) -> List[str]:
    heading = COMMUNITY_HEADING["zh" if language == "zh" else "en"]
    return ['<div class="community" markdown="1">', "", f"## {heading}", "", content.strip(), "", "</div>", ""]


_SECTION = re.compile(r"^## (.+)$", re.M)


def restructure_body(body: str, language: str) -> str:
    """Apply the same shape to a story that was already published."""
    lead = re.search(r'(<div class="story-lead" markdown="1">\n\n)(.*?)(\n\n</div>)', body, re.S)
    if lead:
        body = body[:lead.start(2)] + split_lead(lead.group(2), language) + body[lead.end(2):]
    if 'class="community"' in body:
        return body
    heads = list(_SECTION.finditer(body))
    for i, h in enumerate(heads):
        if not is_community(h.group(1)):
            continue
        end = heads[i + 1].start() if i + 1 < len(heads) else body.index("{% endraw %}")
        content = body[h.end():end].strip()
        body = body[:h.start()] + body[end:]
        tail = body.index("{% endraw %}")
        if not is_empty_block(content):
            body = body[:tail] + "\n".join(community_section(content, language)) + "\n" + body[tail:]
        break
    return body
