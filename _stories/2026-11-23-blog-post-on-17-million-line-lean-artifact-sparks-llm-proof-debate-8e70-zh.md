---
layout: story
lang: zh
date: 2026-11-23 13:28:10 -0500
issue: "2026-11-23"
story_id: "blog-post-on-17-million-line-lean-artifact-sparks-llm-proof-debate-8e70"
permalink: "/zh/2026/11/23/blog-post-on-17-million-line-lean-artifact-sparks-llm-proof-debate-8e70/"
title: "1700 万行 Lean 证明引发可信度争论"
dek: "一篇博客文章分析了一个约 1700 万行的 Lean 证明工件，Hacker News 的讨论随即集中在 LLM 辅助生成的形式化证明是否可信。"
description: "一篇博客文章分析了一个约 1700 万行的 Lean 证明工件，Hacker News 的讨论随即集中在 LLM 辅助生成的形式化证明是否可信。"
section: "ai-news"
rank: 5
edition: 0
section_rank: 5
score: 7.0
status: null
source_name: "micjm.com"
source_url: "https://micjm.com/blog/yes-17m-lines-of-lean-is-a-lot/"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50607668"
published_at: "2026-11-23T05:00:49+00:00"
tags: ["Lean", "formal verification", "LLM-generated proofs", "mathematics", "AI code quality"]
topics: ["lean", "formal-verification", "llm-generated-proofs", "mathematics", "ai-code-quality"]
order: "20261123-0-994"
image: "/assets/stories/2026-11-23/blog-post-on-17-million-line-lean-artifact-sparks-llm-proof-debate-8e70-share.jpg"
art: "/assets/stories/2026-11-23/blog-post-on-17-million-line-lean-artifact-sparks-llm-proof-debate-8e70.jpg"
thumb: "/assets/stories/2026-11-23/blog-post-on-17-million-line-lean-artifact-sparks-llm-proof-debate-8e70-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g8bcd542abf8abc8b60971117f4318976e36ce92b95a96e75bd4b49764e708965ee15e9d46c4806a5db1fb9f1fae78b3a_1280.jpg", "author": "kewl", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/server-room-datacenter-network-90389/", "provider": "Pixabay", "width": 4818, "height": 3212}
---

{% raw %}
<div class="story-lead" markdown="1">

一篇博客文章分析了一个约 1700 万行的 Lean 证明工件，Hacker News 的讨论随即集中在 LLM 辅助生成的形式化证明是否可信。评论者的核心担忧是规模：证明越大，潜在错误点越多，而一个反例就足以推翻结论；也有人担心 LLM 写出的说明和代码难以让未参与生成的人理解。讨论中有人称该证明的行数已从 1700 万降到 1300 万，并可能继续下降，但给出的材料没有独立确认这一数字或证明本身是否正确。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** 该条目指向的博客文章讨论了一个约 1700 万行的 Lean 证明工件，相关 Hacker News 讨论集中在 LLM 辅助证明的正确性风险。
- **尚未证实：** 该证明是否由 LLM 生成、是否包含逻辑错误，以及评论中“已降到 1300 万行”的说法，均未在给出的材料中得到独立确认；博客文章的具体论证也未提供。

</div>

## 背景

黎曼猜想是数学界最著名的未解难题之一。据滑铁卢大学数学家 Michael Rubinstein 的整理页面，Anthropic 的数学家 Levent Alpöge 于 2026 年 11 月 20 日发布一份四页短文，称自己与 Claude 合作，认为已找到黎曼猜想以及 Dirichlet L 函数广义黎曼猜想的证明，但没有配套论文；该证明以 Lean 形式发布，共 175,187 个文件、约 1700 万行。Lean 是一种证明助手（proof assistant），它把每一步推理写成代码，由内核机械校验，因此理论上形式化证明可被机器逐条检查；但当规模达到上千万行时，人工逐行审阅实际上已不可行，Rubinstein 的页面便汇总了他本人及其他人对这份 Lean 证明所做的检查。

## 为什么重要

对 Lean 用户和审阅者来说，最直接的问题是审查成本：上千万行的工件无法靠逐行阅读来建立信任，社区因此把焦点放在缩小证明规模、确认形式化陈述是否忠实于原问题，以及寻找独立复核手段上。

## 后续看点

评论者称该证明已降到 1300 万行，并预测可能降至 1100 万行；关注这一行数变化是否发生，以及博客作者是否更新分析。

## 社区讨论

多位评论者把规模视为风险来源：jandrese 认为证明越大，出错点越多，一个反例就能让整个结果崩塌；lukaslalinsky 则说没人会审阅上千万行 LLM 生成的代码，担心其中藏有次要信息。Arch485 提出另一种可能：问题未必是 Lean 的 bug，而是某个被转换的子证明本身有误；adgjlsfhk1 称行数已降至 1300 万。

## 延伸阅读

- [17 Million Lines Claim to Prove Riemann . We Ran Them. - YouTube](https://www.youtube.com/watch?v=aDl7-MWFLVc)
- [Alpöge/Claude proof of the Generalized Riemann Hypothesis](https://math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/)
- [Yes, 17 m lines of Lean is a lot | micjm](https://micjm.com/blog/yes-17m-lines-of-lean-is-a-lot/)

{% endraw %}
