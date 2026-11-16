#!/usr/bin/env python3
"""Review queue for high-risk stories held by src/services/review.py.

  open    --site docs --date D --edition E   open one GitHub issue per run's held list
  publish --site . --issue N                 move the stories named in issue N into _stories
  expire  --site . [--hours 24]              drop held stories older than the limit

Run `open` from the main checkout after deploy, `publish` and `expire` from a
gh-pages checkout. Needs the gh CLI with GH_TOKEN set.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

LABEL = "held-story"
MARK = re.compile(r"<!-- manifest: (_review/\d{4}-\d{2}-\d{2}/held-e\d\.json) -->")
CATEGORY_ZH = {"casualty": "伤亡", "accident": "重大事故", "allegation": "指控"}


def gh(*args: str, check: bool = True) -> str:
    out = subprocess.run(["gh", *args], capture_output=True, text=True)
    if check and out.returncode != 0:
        sys.exit(f"gh {' '.join(args[:2])} failed: {out.stderr.strip()}")
    return out.stdout


def cmd_open(args) -> None:
    rel = f"_review/{args.date}/held-e{args.edition}.json"
    path = Path(args.site) / rel
    if not path.exists():
        print("Nothing held this run.")
        return
    data = json.loads(path.read_text(encoding="utf-8"))
    stories = data.get("stories") or []
    if not stories:
        return
    lines = [
        f"本次发布（{args.date}，第 {args.edition} 版）有 {len(stories)} 条高风险新闻没有自动发布，按规则等你决定。",
        "",
        "- 要发布：给这个 issue 加上 **publish** 标签，几分钟内上线。",
        "- 不发布：直接关闭，或不处理，24 小时后自动放弃。",
        "",
    ]
    for s in stories:
        lines += [
            f"### {s['title']}",
            f"类别：{CATEGORY_ZH.get(s['category'], s['category'])} · 来源：[{s['source']}]({s['url']})",
            "未通过的原因：" + "；".join(s["reasons"]),
            "稿件：" + "、".join(f"`{f}`" for f in s["files"]),
            "",
        ]
    lines.append(f"<!-- manifest: {rel} -->")
    gh("label", "create", LABEL, "--color", "B60205", "--description", "High-risk story waiting for review", "--force")
    gh("label", "create", "publish", "--color", "0E8A16", "--description", "Publish the held stories in this issue", "--force")
    title = f"待审：{args.date} 第 {args.edition} 版 {len(stories)} 条高风险新闻"
    url = gh("issue", "create", "--title", title, "--body", "\n".join(lines), "--label", LABEL).strip()
    print(f"Opened {url}")


def _manifest_from_issue(number: str) -> str:
    body = json.loads(gh("issue", "view", number, "--json", "body"))["body"]
    m = MARK.search(body or "")
    if not m:
        sys.exit("Issue has no manifest marker.")
    return m.group(1)


def cmd_publish(args) -> None:
    site = Path(args.site)
    rel = _manifest_from_issue(args.issue)
    manifest = site / rel
    if not manifest.exists():
        gh("issue", "comment", args.issue, "--body", "这些稿件已过期或已处理，无法发布。")
        gh("issue", "close", args.issue)
        return
    day_dir = manifest.parent
    moved = []
    for s in json.loads(manifest.read_text(encoding="utf-8"))["stories"]:
        for name in s["files"]:
            src = day_dir / name
            if src.exists():
                shutil.move(str(src), str(site / "_stories" / name))
                moved.append(name)
    manifest.unlink()
    if not any(day_dir.iterdir()):
        day_dir.rmdir()
    print("\n".join(moved))
    note = f"已发布 {len(moved)} 个页面。" if moved else "没有找到可发布的稿件。"
    gh("issue", "comment", args.issue, "--body", note)
    gh("issue", "close", args.issue)


def cmd_expire(args) -> None:
    site = Path(args.site)
    cutoff = datetime.now(timezone.utc) - timedelta(hours=args.hours)
    expired = set()
    for manifest in sorted(site.glob("_review/*/held-e*.json")):
        data = json.loads(manifest.read_text(encoding="utf-8"))
        held_at = datetime.fromisoformat(data["held_at"])
        if held_at > cutoff:
            continue
        for s in data.get("stories") or []:
            for name in s["files"]:
                (manifest.parent / name).unlink(missing_ok=True)
        manifest.unlink()
        if not any(manifest.parent.iterdir()):
            manifest.parent.rmdir()
        expired.add(str(manifest.relative_to(site)))
        print(f"Expired {manifest}")
    if not expired:
        return
    issues = json.loads(gh("issue", "list", "--label", LABEL, "--state", "open", "--json", "number,body"))
    for issue in issues:
        m = MARK.search(issue.get("body") or "")
        if m and m.group(1) in expired:
            gh("issue", "comment", str(issue["number"]), "--body", "超过 24 小时未处理，这些稿件已自动放弃，没有发布。")
            gh("issue", "close", str(issue["number"]), "--reason", "not planned")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    o = sub.add_parser("open"); o.add_argument("--site", default="docs"); o.add_argument("--date", required=True); o.add_argument("--edition", default="0")
    pb = sub.add_parser("publish"); pb.add_argument("--site", default="."); pb.add_argument("--issue", required=True)
    e = sub.add_parser("expire"); e.add_argument("--site", default="."); e.add_argument("--hours", type=float, default=24)
    args = p.parse_args()
    {"open": cmd_open, "publish": cmd_publish, "expire": cmd_expire}[args.cmd](args)


if __name__ == "__main__":
    main()
