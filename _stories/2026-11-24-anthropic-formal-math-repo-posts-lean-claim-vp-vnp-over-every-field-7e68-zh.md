---
layout: story
lang: zh
date: 2026-11-24 06:00:00 -0500
issue: "2026-11-24"
story_id: "anthropic-formal-math-repo-posts-lean-claim-vp-vnp-over-every-field-7e68"
permalink: "/zh/2026/11/24/anthropic-formal-math-repo-posts-lean-claim-vp-vnp-over-every-field-7e68/"
title: "Anthropic formal-math 仓库公开 VP ≠ VNP 的 Lean 形式化"
dek: "Anthropic 的 formal-math 仓库公开了一份 Lean 形式化，声称证明代数复杂度类 VP 与 VNP 不相等，且该结论对所有域成立；代码位于 GitHub，提交 11b6c7e3c927d…，可通过仓库查看。"
description: "Anthropic 的 formal-math 仓库公开了一份 Lean 形式化，声称证明代数复杂度类 VP 与 VNP 不相等，且该结论对所有域成立；代码位于 GitHub，提交 11b6c7e3c927d…，可通过仓库查看。"
section: "ai-news"
rank: 1
edition: 0
section_rank: 1
score: 7.0
status: "Released"
source_name: "GitHub"
source_url: "https://github.com/anthropics/formal-math/tree/main/vp-vnp"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50620102"
published_at: "2026-11-23T22:09:10+00:00"
tags: ["formal verification", "Lean", "complexity theory", "AI for mathematics", "Anthropic"]
topics: ["formal-verification", "lean", "complexity-theory", "ai-for-mathematics", "anthropic"]
order: "20261124-0-998"
image: "/assets/stories/2026-11-24/anthropic-formal-math-repo-posts-lean-claim-vp-vnp-over-every-field-7e68-share.jpg"
art: "/assets/stories/2026-11-24/anthropic-formal-math-repo-posts-lean-claim-vp-vnp-over-every-field-7e68.jpg"
thumb: "/assets/stories/2026-11-24/anthropic-formal-math-repo-posts-lean-claim-vp-vnp-over-every-field-7e68-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g4097b6e04d807e81def251c0131936faa0df031694afc2bd4803601cd708634ae8b9506b125bc03cc111866c6d4c8d1451eb1e5b4efdb95f5aa802e857e5bede_1280.jpg", "author": "Pexels", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/laptop-notebook-cellphone-computer-1839876/", "provider": "Pixabay", "width": 3778, "height": 2519}
---

{% raw %}
<div class="story-lead" markdown="1">

Anthropic 的 formal-math 仓库公开了一份 Lean 形式化，声称证明代数复杂度类 VP 与 VNP 不相等，且该结论对所有域成立；代码位于 GitHub，提交 11b6c7e3c927d…，可通过仓库查看。Lean 是用于机器检查证明的证明助手，因此这份材料把论证变成了可编译、可审阅的代码，而非仅靠文字陈述。需要保留的限制是：条目本身没有说明该证明是否经过独立审阅，也没有交代 Claude 或 AI 在推导中的具体作用；目前能确认的是公开仓库与形式化声明，而非已被同行评审确认的定理。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** Anthropic 的 formal-math 仓库中确实存在一个 vp-vnp 目录，内含署名「Claude / Anthropic」、题为《VP ≠ VNP over every field》的论文以及 Lean 4 形式化代码；仓库自述该证明尚无人类数学家审阅，属于研究性产物，Anthropic 不予维护（据仓库本身及 AGI Hunt、lavx.hu 等报道）。论文本身也承认「尚未分析其与相对化、代数化的关系」。
- **尚未证实：** 证明的数学正确性，以及 Lean 形式化是否完整（有无 sorry、额外公理），均无独立验证；「Claude 为唯一作者」只是论文署名，尚无第三方核实其生成方式；论文篇幅（约 70 页）与形式化规模（约 7.3 万行 Lean）出自二手报道，不同来源表述不完全一致。

</div>

## 背景

VP 与 VNP 是 Leslie Valiant 在 1979 年提出的代数复杂度类，用算术电路规模来对应 P 与 NP：行列式属于 VP，而积和式（permanent）是 VNP 完全问题，因此「VP ≠ VNP」等价于说积和式无法被多项式大小的算术电路计算。它与 P ≠ NP 一样是悬而未决的猜想，也是代数复杂性理论的核心目标。Lean 是交互式定理证明器，用 Lean 写出的证明可由机器逐条检查，所以这类仓库的关键在于形式化本身能否在 Lean 中通过验证，而不只是文字论证是否可信。

## 为什么重要

如果这份 Lean 形式化能够无残留公设地通过编译，它解决的将是代数复杂性中长期悬而未决的 VP 与 VNP 分离问题——即“永久式是否没有多项式规模的算术电路”这一公开难题（据维基百科的条目，该问题此前仍未解决）。但论文摘要本身明确说明，VP ≠ VNP 只是 P ≠ NP 的代数类比，并不解决 P ≠ NP；因此读者应把这条消息视为待独立检验的预印本主张，实际可做的下一步是审查并编译该 Lean 开发，而不是当作已确立的结论。

## 后续看点

后续可检查该 Lean 项目能否通过独立构建与审阅，以及作者是否补充论文自述中尚未分析的相对化（relativization）与代数化（algebrization）问题。

## 社区讨论

评论者把这项工作解读为 Anthropic 在 P vs NP 方向上的阶段性推进，并争论 AI 是否会让研究生可做的问题迅速减少；也有人引用论文自述指出尚未分析相对化与代数化，另有用户推荐用 slim 工具浏览 Lean 源码。

## 延伸阅读

- [Claude-authored paper claims VP≠VNP over every… · AGI Hunt](https://agihunt.info/en/e/1a20a795a118dbdb4f5bd2bb40d)
- [Anthropic Publishes Claimed Proof That VP ≠ VNP Over Every Field](https://news.lavx.hu/article/anthropic-publishes-claimed-proof-that-vp-vnp-over-every-field)
- [Claude-Written Paper Claims VP ≠ VNP, With a Lean Proof](https://fourweekmba.com/ai-claude-written-paper-claims-vp-vnp-with-a-lean-proof/)
- [Arithmetic circuit complexity - Wikipedia](https://en.wikipedia.org/wiki/Arithmetic_circuit_complexity)
- [VP ||#92;neq$ VNP over every field · Hexagon](https://hexagonmath.org/2611.00954v1)

{% endraw %}
