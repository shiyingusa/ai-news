"""Send the Morning Brief newsletter through Buttondown.

Runs after the English site export. Needs the ``BUTTONDOWN_API_KEY``
environment variable; without it, nothing is sent.
"""

from __future__ import annotations

import json
import logging
import os
import re
from pathlib import Path
from typing import List, Optional

import httpx

logger = logging.getLogger(__name__)

API = "https://api.buttondown.com/v1/emails"
SITE = "https://aidailyradar.com"


def _front(text: str) -> dict:
    head = text.split("\n---\n", 1)[0]
    data = {}
    for line in head.splitlines():
        match = re.match(r"^([a-z_]+): (.*)$", line)
        if match:
            try:
                data[match.group(1)] = json.loads(match.group(2))
            except json.JSONDecodeError:
                data[match.group(1)] = match.group(2).strip()
    return data


def _date_label(day: str) -> str:
    from datetime import date

    d = date.fromisoformat(day)
    return f"{d:%B} {d.day}, {d.year}"


def build_email(day: str, story_paths: List[Path], brief_path: Optional[Path], limit: int = 10) -> Optional[dict]:
    stories = [_front(p.read_text(encoding="utf-8")) for p in story_paths]
    stories = [s for s in stories if s.get("permalink") and s.get("title")]
    stories.sort(key=lambda s: int(s.get("rank") or 999))
    if not stories:
        return None
    brief = json.loads(brief_path.read_text(encoding="utf-8")) if brief_path and brief_path.exists() else None
    headline = brief["headline"] if brief else stories[0]["title"]
    lines = [
        f"*{_date_label(day)} · [Read on the web]({SITE}/briefing/{day}/) · [中文版]({SITE}/zh/briefing/{day}/)*",
        "",
    ]
    if brief:
        lines += ["## The Big Picture", "", f"**{brief['headline']}**", ""]
        for para in brief.get("paragraphs", []):
            lines += [para, ""]
        if brief.get("takeaways"):
            lines += ["**Key takeaways**", ""]
            lines += [f"- {t}" for t in brief["takeaways"]]
            lines.append("")
    lines += ["## Today's top stories", ""]
    for s in stories[:limit]:
        source = s.get("source_name") or ""
        status = f" · {s['status']}" if s.get("status") else ""
        lines.append(f"**[{s['title']}]({SITE}{s['permalink']})**  ")
        lines.append(f"{s.get('dek') or ''}  ")
        lines.append(f"*{source}{status}*")
        lines.append("")
    if len(stories) > limit:
        lines += [f"[See all {len(stories)} stories in today's briefing]({SITE}/briefing/{day}/)", ""]
    lines += [
        "---",
        "",
        f"AI Daily Radar is written with AI assistance from the sources linked on each story and run by Ying Shi. "
        f"How we work: [editorial standards]({SITE}/standards/). Spotted an error? Reply to this email.",
    ]
    subject = f"{headline} · AI Daily Radar, {_date_label(day)}"
    return {"subject": subject[:200], "body": "\n".join(lines)}


def send_morning_brief(day: str, story_paths: List[Path], brief_path: Optional[Path]) -> Optional[str]:
    """Send today's newsletter; returns the Buttondown email id, or None."""
    key = os.environ.get("BUTTONDOWN_API_KEY", "").strip()
    if not key:
        logger.info("BUTTONDOWN_API_KEY not set; newsletter skipped")
        return None
    email = build_email(day, story_paths, brief_path)
    if not email:
        return None
    status = os.environ.get("NEWSLETTER_STATUS", "about_to_send")
    headers = {
        "Authorization": f"Token {key}",
        "X-Buttondown-Live-Dangerously": "true",
    }
    try:
        with httpx.Client(timeout=30) as client:
            existing = client.get(API, headers=headers, params={"subject": email["subject"]})
            if existing.status_code == 200 and existing.json().get("count"):
                logger.info("Newsletter for %s already exists; not sending again", day)
                return None
            response = client.post(API, headers=headers, json={**email, "status": status})
            response.raise_for_status()
            return str(response.json().get("id"))
    except Exception as exc:  # newsletter is optional; never break the run
        logger.warning("Newsletter send failed: %s", exc)
        return None
