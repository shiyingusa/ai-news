"""Tell IndexNow search engines (Bing, Yandex, Seznam, Naver...) about new pages.

Reads today's story permalinks from a gh-pages checkout (or the docs folder)
and submits them together with the home pages and today's briefing.

    python scripts/indexnow.py --site docs --date 2026-11-15
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

HOST = "aidailyradar.com"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", default="docs")
    parser.add_argument("--date", required=True)
    parser.add_argument("--wait", type=int, default=0, help="seconds to wait for the deploy first")
    args = parser.parse_args()
    site = Path(args.site)
    key = re.search(r"^indexnow_key: (\S+)", (Path("docs/_config.yml")).read_text(), re.M).group(1)
    urls = [f"https://{HOST}/", f"https://{HOST}/zh/",
            f"https://{HOST}/briefing/{args.date}/", f"https://{HOST}/zh/briefing/{args.date}/"]
    for path in sorted((site / "_stories").glob(f"{args.date}-*.md")):
        match = re.search(r"^permalink: (.*)$", path.read_text(encoding="utf-8"), re.M)
        if match:
            urls.append(f"https://{HOST}{json.loads(match.group(1))}")
    if args.wait:
        time.sleep(args.wait)
    body = json.dumps({"host": HOST, "key": key, "keyLocation": f"https://{HOST}/{key}.txt", "urlList": urls}).encode()
    request = urllib.request.Request("https://api.indexnow.org/indexnow", data=body,
                                     headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            print(f"IndexNow: submitted {len(urls)} URLs, HTTP {response.status}")
    except Exception as exc:  # never fail the daily run over this
        print(f"IndexNow submission failed: {exc}")
    baidu_push(urls)
    return 0


def baidu_push(urls):
    """Baidu's own push API, for the Chinese pages (needs BAIDU_PUSH_TOKEN)."""
    import os

    token = os.environ.get("BAIDU_PUSH_TOKEN", "").strip()
    # New sites without an ICP licence get a tiny daily quota (about 10),
    # so send only the Chinese home page, today's briefing and top stories.
    zh = [u for u in urls if "/zh/" in u][: int(os.environ.get("BAIDU_DAILY_LIMIT", "10"))]
    if not token or not zh:
        return
    endpoint = f"http://data.zz.baidu.com/urls?site=https://{HOST}&token={token}"
    request = urllib.request.Request(endpoint, data="\n".join(zh).encode(), headers={"Content-Type": "text/plain"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            print(f"Baidu push: {response.read().decode()[:200]}")
    except Exception as exc:
        print(f"Baidu push failed: {exc}")


if __name__ == "__main__":
    sys.exit(main())
