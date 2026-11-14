"""Original artwork for story pages: no third-party photos, no licensing risk.

Each story gets two images drawn from a seed of its slug:
- ``<slug>.jpg``: 1200x675 radar-style art in the section colour (cards, story hero)
- ``<slug>-share.jpg``: the same art with the headline (Open Graph, Google Discover)
"""

from __future__ import annotations

import hashlib
import math
import random
from pathlib import Path
from typing import Tuple

from PIL import Image, ImageDraw, ImageFilter, ImageFont

FONT_DIR = Path(__file__).resolve().parent.parent / "assets" / "fonts"
W, H = 1200, 675

SECTION_COLOURS = {
    "ai-news": "#e5571f",
    "chips-compute": "#2f74d0",
    "robotics-autonomy": "#13908f",
    "ev-energy": "#2f9a4f",
    "space": "#4a6fa5",
    "science-bio": "#c0436a",
    "tech-industry": "#c08a1e",
    "tech-blog": "#7a7f88",
}
SECTION_LABELS = {
    "ai-news": "AI",
    "chips-compute": "CHIPS & COMPUTING",
    "robotics-autonomy": "ROBOTS & SELF-DRIVING",
    "ev-energy": "EVS & ENERGY",
    "space": "SPACE",
    "science-bio": "SCIENCE & BIOTECH",
    "tech-industry": "TECH INDUSTRY & POLICY",
    "tech-blog": "DEEP DIVES",
}
INK = (18, 19, 23)
PAPER = (246, 244, 239)


def _rgb(hex_colour: str) -> Tuple[int, int, int]:
    hex_colour = hex_colour.lstrip("#")
    return tuple(int(hex_colour[i : i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]


def _mix(a, b, t: float):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def _font(name: str, size: int, weight: int):
    font = ImageFont.truetype(str(FONT_DIR / name), size)
    try:
        axes = font.get_variation_axes()
        values = []
        for axis in axes:
            tag = axis.get("name", b"")
            tag = tag.decode() if isinstance(tag, bytes) else str(tag)
            if "eight" in tag.lower():
                values.append(weight)
            elif "ptical" in tag.lower():
                values.append(min(axis["maximum"], max(axis["minimum"], 72)))
            else:
                values.append(axis.get("default", axis["minimum"]))
        font.set_variation_by_axes(values)
    except Exception:  # static font or no variation support
        pass
    return font


def draw_art(seed_text: str, section: str) -> Image.Image:
    """Deterministic radar-style artwork for one story."""
    rng = random.Random(int(hashlib.sha1(seed_text.encode()).hexdigest()[:12], 16))
    accent = _rgb(SECTION_COLOURS.get(section, "#e5571f"))
    base = _mix(INK, accent, 0.10)
    img = Image.new("RGB", (W, H), base)
    draw = ImageDraw.Draw(img)

    # fine grid
    grid = _mix(base, PAPER, 0.06)
    step = rng.choice([40, 48, 56])
    for x in range(0, W, step):
        draw.line([(x, 0), (x, H)], fill=grid, width=1)
    for y in range(0, H, step):
        draw.line([(0, y), (W, y)], fill=grid, width=1)

    # radar rings around an off-centre origin
    cx = rng.randint(int(W * 0.55), int(W * 0.9))
    cy = rng.randint(int(H * 0.25), int(H * 0.75))
    ring = _mix(base, PAPER, 0.22)
    for r in range(90, 1100, rng.choice([90, 110, 130])):
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=ring, width=2)

    # sweep wedge
    sweep = Image.new("L", (W, H), 0)
    sd = ImageDraw.Draw(sweep)
    start = rng.uniform(0, 360)
    span = rng.uniform(28, 55)
    for i in range(24):
        alpha = int(150 * (1 - i / 24))
        sd.pieslice([cx - 1100, cy - 1100, cx + 1100, cy + 1100], start + span * i / 24, start + span * (i + 1) / 24, fill=alpha)
    sweep = sweep.filter(ImageFilter.GaussianBlur(6))
    img.paste(Image.new("RGB", (W, H), accent), (0, 0), sweep.point(lambda v: int(v * 0.45)))

    # blips
    draw = ImageDraw.Draw(img)
    for _ in range(rng.randint(5, 9)):
        angle = math.radians(rng.uniform(0, 360))
        dist = rng.uniform(80, 620)
        bx, by = cx + dist * math.cos(angle), cy + dist * math.sin(angle)
        size = rng.uniform(5, 13)
        glow = Image.new("L", (W, H), 0)
        ImageDraw.Draw(glow).ellipse([bx - size * 3, by - size * 3, bx + size * 3, by + size * 3], fill=120)
        glow = glow.filter(ImageFilter.GaussianBlur(10))
        img.paste(Image.new("RGB", (W, H), accent), (0, 0), glow)
        draw = ImageDraw.Draw(img)
        draw.ellipse([bx - size, by - size, bx + size, by + size], fill=_mix(accent, PAPER, 0.35))
    # origin
    draw.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], fill=PAPER)
    return img


def _wrap(draw: ImageDraw.ImageDraw, text: str, font, max_width: int, max_lines: int):
    words, lines, line = text.split(), [], ""
    for word in words:
        trial = f"{line} {word}".strip()
        if draw.textlength(trial, font=font) <= max_width:
            line = trial
        else:
            lines.append(line)
            line = word
            if len(lines) == max_lines:
                break
    if len(lines) < max_lines and line:
        lines.append(line)
    if len(lines) == max_lines and " ".join(lines) != text:
        last = lines[-1]
        while last and draw.textlength(last + "…", font=font) > max_width:
            last = last.rsplit(" ", 1)[0]
        lines[-1] = last + "…"
    return lines


def draw_share(art: Image.Image, title: str, section: str, date_label: str) -> Image.Image:
    """Headline card for social sharing, drawn over the story art."""
    img = art.copy()
    shade = Image.new("L", (W, H), 0)
    sd = ImageDraw.Draw(shade)
    for x in range(W):
        sd.line([(x, 0), (x, H)], fill=int(235 * max(0.0, 1 - x / (W * 0.95)) ** 0.8))
    img.paste(Image.new("RGB", (W, H), INK), (0, 0), shade)
    draw = ImageDraw.Draw(img)
    accent = _rgb(SECTION_COLOURS.get(section, "#e5571f"))
    kicker = _font("PublicSans.ttf", 26, 650)
    head = _font("Newsreader.ttf", 64, 640)
    small = _font("PublicSans.ttf", 24, 550)
    x = 72
    draw.rectangle([x, 72, x + 44, 78], fill=accent)
    draw.text((x, 96), SECTION_LABELS.get(section, "NEWS"), font=kicker, fill=accent)
    y = 150
    for line in _wrap(draw, title, head, 860, 4):
        draw.text((x, y), line, font=head, fill=PAPER)
        y += 76
    draw.ellipse([x, H - 92, x + 26, H - 66], outline=PAPER, width=3)
    draw.ellipse([x + 15, H - 91, x + 24, H - 82], fill=accent)
    draw.text((x + 40, H - 95), "AI Daily Radar", font=small, fill=PAPER)
    draw.text((x + 40 + draw.textlength("AI Daily Radar", font=small) + 18, H - 95), "·  " + date_label, font=small, fill=_mix(PAPER, INK, 0.35))
    return img


def make_story_images(out_dir: Path, slug: str, title: str, section: str, date_label: str) -> Tuple[Path, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    art = draw_art(slug, section)
    art_path = out_dir / f"{slug}.jpg"
    share_path = out_dir / f"{slug}-share.jpg"
    art.save(art_path, "JPEG", quality=82, optimize=True, progressive=True)
    art.resize((560, 315), Image.LANCZOS).save(out_dir / f"{slug}-640.jpg", "JPEG", quality=80, optimize=True, progressive=True)
    draw_share(art, title, section, date_label).save(share_path, "JPEG", quality=85, optimize=True, progressive=True)
    return art_path, share_path
