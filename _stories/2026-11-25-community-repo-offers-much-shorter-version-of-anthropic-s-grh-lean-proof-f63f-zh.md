---
layout: story
lang: zh
date: 2026-11-25 18:25:55 -0500
issue: "2026-11-25"
story_id: "community-repo-offers-much-shorter-version-of-anthropic-s-grh-lean-proof-f63f"
permalink: "/zh/2026/11/25/community-repo-offers-much-shorter-version-of-anthropic-s-grh-lean-proof-f63f/"
title: "Anthropic 的 GRH Lean 验证出现大幅精简社区版"
dek: "一个名为 grh-lean 的社区仓库在 Hacker News 上受到关注，它发布了 Anthropic 的 GRH Lean 形式化验证的一个据称短得多的版本；一位评论者给出的数字是从约 1700 万行降到约 7.6 万行…"
description: "一个名为 grh-lean 的社区仓库在 Hacker News 上受到关注，它发布了 Anthropic 的 GRH Lean 形式化验证的一个据称短得多的版本；一位评论者给出的数字是从约 1700 万行降到约 7.6 万行…"
section: "ai-news"
rank: 202
edition: 2
section_rank: 2
score: 7.0
status: "Available"
source_name: "GitHub"
source_url: "https://github.com/lsernau/grh-lean"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50648050"
published_at: "2026-11-25T21:48:10+00:00"
tags: ["AI-assisted theorem proving", "Lean", "formal verification", "mathematics", "Anthropic"]
topics: ["ai-assisted-theorem-proving", "lean", "formal-verification", "mathematics", "anthropic"]
order: "20261125-2-997"
image: "/assets/stories/2026-11-25/community-repo-offers-much-shorter-version-of-anthropic-s-grh-lean-proof-f63f-share.jpg"
art: "/assets/stories/2026-11-25/community-repo-offers-much-shorter-version-of-anthropic-s-grh-lean-proof-f63f.jpg"
thumb: "/assets/stories/2026-11-25/community-repo-offers-much-shorter-version-of-anthropic-s-grh-lean-proof-f63f-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g47030052cdb46936216f5189808b09e88dc594570fc85f2d86da72192dd716cad9ffaee1c1d1ea390c619d7afce059733502e54d25ade51f69192dc24f45eb84_1280.jpg", "author": "Pexels", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/coding-programming-css-1853305/", "provider": "Pixabay", "width": 5472, "height": 3648}
---

{% raw %}
<div class="story-lead" markdown="1">

一个名为 grh-lean 的社区仓库在 Hacker News 上受到关注，它发布了 Anthropic 的 GRH Lean 形式化验证的一个据称短得多的版本；一位评论者给出的数字是从约 1700 万行降到约 7.6 万行，降幅 99.56%。评论者还称，这个更易读的版本区分了“已知数学”和“新数学”，并附有人类可读文档，便于研究者消化。但这些行数、可读性和完整性说法都来自社区讨论，尚未独立核验，也不是 Anthropic 官方发布。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** Hacker News 上出现一条提交，指向 lsernau 的 GitHub 仓库 grh-lean，并将其描述为 Anthropic GRH Lean 验证的“短得多”的版本；仓库和讨论链接可公开访问。
- **尚未证实：** 约 1700 万行降至约 7.6 万行、99.56% 降幅、300kloc 的可读版本、“已知数学/新数学”分区与文档，均来自评论者，未获独立核验；评论中 300kloc 与约 7.6 万行两种规模说法也未对齐。Anthropic 是否认可该版本、证明是否完整、人类可读性究竟如何，均无官方说明。

</div>

## 背景

Lean 是交互式定理证明器，证明由小型内核逐条机器检查；大型形式化项目常生成极长、机器可验证但人类难读的脚本，社区因此会重写或压缩以提高可审阅性。

## 为什么重要

对希望复核这项形式化结果的研究者，这个仓库提供了一个规模更小、据称更易读的入口；但由于它不是 Anthropic 官方发布，且行数与可读性主张未经独立验证，使用前应按仓库说明配置 Lean 工具链并自行构建、检查证明是否完整。

## 后续看点

关注 Lean Zulip 上的相关讨论和仓库的 issue/提交，看是否有人独立构建并通过 Lean 内核检查，以及是否出现 Anthropic 的官方回应或官方精简版。

## 社区讨论

评论者称赞精简版按“已知数学/新数学”分区并附文档，认为这有助于消化原始证明；也有人把大幅压缩归因于 Anthropic 投入算力和更强内部模型，而非此前人力反复微调。另有不熟悉 Lean 的读者追问：这种代码对人类来说究竟有多现实可读、可核验。

{% endraw %}
