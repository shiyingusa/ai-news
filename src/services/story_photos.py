"""Real photographs for story pages, from licensed sources only.

Order of preference:
1. Pexels (free for commercial use, no attribution required) when ``PEXELS_API_KEY`` is set.
2. Wikimedia Commons, limited to public domain, CC0, CC BY and CC BY-SA files.
3. The original radar artwork (``story_images.py``) when nothing suitable is found.

Every photo is stored with its author, licence and source so the story page can
credit it. Queries describe objects and places, not people.
"""

from __future__ import annotations

import html
import io
import logging
import os
import re
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable, Optional, Set

import httpx
from PIL import Image, ImageOps

logger = logging.getLogger(__name__)

USER_AGENT = "AIDailyRadar/1.0 (https://aidailyradar.com; hello@aidailyradar.com)"
W, H = 1200, 675
ALLOWED_LICENCES = re.compile(r"^(public domain|pd|cc0|cc by(-sa)? ?[0-9.]*( [a-z]+)?)$", re.I)
BAD_TITLE = re.compile(
    r"logo|icon|map|diagram|chart|graph|screenshot|portrait|headshot|signature|flag|coat of arms|seal|"
    r"poster|cover|svg|drawing|sketch|painting|stamp|banknote|coin",
    re.I,
)


@dataclass
class Photo:
    url: str
    author: str
    licence: str
    licence_url: str
    source_url: str
    provider: str
    width: int
    height: int

    def credit(self) -> dict:
        return asdict(self)


def _clean(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text or "")
    return html.unescape(" ".join(text.split()))[:120]


def _landscape(width: int, height: int) -> bool:
    return width >= 1000 and height > 0 and 1.2 <= width / height <= 2.4


def _get(client: httpx.Client, url: str, **kwargs) -> httpx.Response:
    """GET with polite pacing and retries on rate limits (Wikimedia asks for both)."""
    delay = 1.5
    for attempt in range(4):
        time.sleep(0.6)
        response = client.get(url, **kwargs)
        if response.status_code not in (429, 503):
            response.raise_for_status()
            return response
        retry_after = response.headers.get("retry-after")
        time.sleep(float(retry_after) if retry_after and retry_after.isdigit() else delay)
        delay *= 2
    response.raise_for_status()
    return response


def search_pexels(client: httpx.Client, query: str, used: Set[str]) -> Optional[Photo]:
    key = os.getenv("PEXELS_API_KEY")
    if not key:
        return None
    response = _get(
        client,
        "https://api.pexels.com/v1/search",
        params={"query": query, "orientation": "landscape", "per_page": 10, "size": "large"},
        headers={"Authorization": key},
    )
    for photo in response.json().get("photos", []):
        url = photo.get("src", {}).get("large2x") or photo.get("src", {}).get("original")
        if not url or url in used or not _landscape(photo.get("width", 0), photo.get("height", 0)):
            continue
        return Photo(
            url=url,
            author=photo.get("photographer") or "Pexels",
            licence="Pexels License",
            licence_url="https://www.pexels.com/license/",
            source_url=photo.get("url") or "https://www.pexels.com/",
            provider="Pexels",
            width=photo["width"],
            height=photo["height"],
        )
    return None


def _relevant(title: str, query: str) -> bool:
    """At least half of the query's distinctive words appear in the file title."""
    words = [w for w in re.findall(r"[a-z0-9]+", query.lower()) if len(w) > 2]
    if not words:
        return True
    name = re.sub(r"[_\-]+", " ", title.lower())
    hits = sum(1 for w in words if w in name)
    return hits >= max(1, (len(words) + 1) // 2)


def search_commons(client: httpx.Client, query: str, used: Set[str]) -> Optional[Photo]:
    response = _get(
        client,
        "https://commons.wikimedia.org/w/api.php",
        params={
            "action": "query",
            "format": "json",
            "generator": "search",
            "gsrsearch": f"filetype:bitmap {query}",
            "gsrnamespace": 6,
            "gsrlimit": 20,
            "prop": "imageinfo",
            "iiprop": "url|size|mime|extmetadata",
            "iiurlwidth": 1600,
        },
    )
    pages = sorted(response.json().get("query", {}).get("pages", {}).values(), key=lambda p: p.get("index", 99))
    for page in pages:
        title = page.get("title", "")
        info = (page.get("imageinfo") or [{}])[0]
        meta = info.get("extmetadata", {})
        licence = _clean(meta.get("LicenseShortName", {}).get("value", ""))
        url = info.get("thumburl") or info.get("url")
        if (
            not url
            or url in used
            or BAD_TITLE.search(title)
            or not _relevant(title, query)
            or info.get("mime") not in {"image/jpeg", "image/png", "image/webp"}
            or not _landscape(info.get("width", 0), info.get("height", 0))
            or not ALLOWED_LICENCES.match(licence)
            or "nc" in licence.lower().split("-")
            or "nd" in licence.lower().split("-")
        ):
            continue
        return Photo(
            url=url,
            author=_clean(meta.get("Artist", {}).get("value", "")) or "Unknown author",
            licence=licence,
            licence_url=_clean(meta.get("LicenseUrl", {}).get("value", "")) or "https://creativecommons.org/licenses/",
            source_url=info.get("descriptionurl") or f"https://commons.wikimedia.org/wiki/{title.replace(' ', '_')}",
            provider="Wikimedia Commons",
            width=info.get("width", 0),
            height=info.get("height", 0),
        )
    return None


def find_photo(queries: Iterable[str], used: Set[str], client: Optional[httpx.Client] = None) -> Optional[Photo]:
    """Try each query on Pexels, then on Commons; returns the first suitable photo."""
    own = client is None
    client = client or httpx.Client(timeout=20, headers={"User-Agent": USER_AGENT}, follow_redirects=True)
    try:
        queries = [q.strip() for q in queries if q and q.strip()]
        for search in (search_pexels, search_commons):
            for query in queries:
                try:
                    photo = search(client, query, used)
                except Exception as exc:  # network or API problems: try the next option
                    logger.info("%s search failed for %r: %s", search.__name__, query, exc)
                    photo = None
                if photo:
                    used.add(photo.url)
                    return photo
        return None
    finally:
        if own:
            client.close()


def save_photo(photo: Photo, out_dir: Path, slug: str, client: Optional[httpx.Client] = None) -> bool:
    """Download, crop to 16:9 and save full-size and thumbnail JPEGs."""
    own = client is None
    client = client or httpx.Client(timeout=30, headers={"User-Agent": USER_AGENT}, follow_redirects=True)
    try:
        data = _get(client, photo.url).content
    except Exception as exc:
        logger.info("Photo download failed for %s: %s", photo.url, exc)
        return False
    finally:
        if own:
            client.close()
    image = ImageOps.exif_transpose(Image.open(io.BytesIO(data))).convert("RGB")
    image = ImageOps.fit(image, (W, H), Image.LANCZOS, centering=(0.5, 0.45))
    out_dir.mkdir(parents=True, exist_ok=True)
    image.save(out_dir / f"{slug}.jpg", "JPEG", quality=84, optimize=True, progressive=True)
    image.resize((560, 315), Image.LANCZOS).save(out_dir / f"{slug}-640.jpg", "JPEG", quality=80, optimize=True, progressive=True)
    return True
