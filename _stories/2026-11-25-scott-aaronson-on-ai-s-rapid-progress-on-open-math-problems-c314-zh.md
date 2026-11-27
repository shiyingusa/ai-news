---
layout: story
lang: zh
date: 2026-11-25 18:25:55 -0500
issue: "2026-11-25"
story_id: "scott-aaronson-on-ai-s-rapid-progress-on-open-math-problems-c314"
permalink: "/zh/2026/11/25/scott-aaronson-on-ai-s-rapid-progress-on-open-math-problems-c314/"
title: "Aaronson 称 AI 正解决一批开放数学问题，引发争论"
dek: "Scott Aaronson 在博客中称，过去一周出现了一波由 AI 辅助解决的开放数学与理论计算机科学问题，其中一些证明借助 Lean 证明助手完成形式化验证；他把这一刻描述为类似“奇点”的开端。"
description: "Scott Aaronson 在博客中称，过去一周出现了一波由 AI 辅助解决的开放数学与理论计算机科学问题，其中一些证明借助 Lean 证明助手完成形式化验证；他把这一刻描述为类似“奇点”的开端。"
section: "ai-news"
rank: 201
edition: 2
section_rank: 1
score: 8.0
status: "Demonstrated"
source_name: "scottaaronson.blog"
source_url: "https://scottaaronson.blog/?p=10379"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50646108"
published_at: "2026-11-25T19:11:27+00:00"
tags: ["AI for mathematics", "LLMs", "automated theorem proving", "Lean", "research breakthrough"]
topics: ["ai-for-mathematics", "llms", "automated-theorem-proving", "lean", "research-breakthrough"]
order: "20261125-2-998"
image: "/assets/stories/2026-11-25/scott-aaronson-on-ai-s-rapid-progress-on-open-math-problems-c314-share.jpg"
art: "/assets/stories/2026-11-25/scott-aaronson-on-ai-s-rapid-progress-on-open-math-problems-c314.jpg"
thumb: "/assets/stories/2026-11-25/scott-aaronson-on-ai-s-rapid-progress-on-open-math-problems-c314-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g2ad067e13f1f0137bbfe0185f20d9eaaccff81a0cd307e3136ac5066d71bc9fb923698a12849669edb64aa285e04dd6b3ae6686096f956b8e8d88cc475d71746_1280.jpg", "author": "ykaiavu", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/garden-hedge-bush-plants-to-cut-7460988/", "provider": "Pixabay", "width": 7952, "height": 5304}
---

{% raw %}
<div class="story-lead" markdown="1">

Scott Aaronson 在博客中称，过去一周出现了一波由 AI 辅助解决的开放数学与理论计算机科学问题，其中一些证明借助 Lean 证明助手完成形式化验证；他把这一刻描述为类似“奇点”的开端。该文是评论而非模型或论文发布，具体解决了哪些问题、AI 贡献有多大，仍取决于他引用的工作。

文章还链接了一篇声称矩阵乘法指数可达 9/4 的论文，但该结果与 AI 的关系未在现有信息中说明。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** Scott Aaronson 在 11 月 25 日的博文中主张，近期 AI 参与解决多个数学与理论计算机科学开放问题，是他一直想象中的“AI 奇点”开端；博文链接的论文题为《The matrix multiplication exponent is nine fourths》，PDF 存放在 OpenAI 的 math 预印本仓库中（tool-1-3）。矩阵乘法指数是刻画矩阵乘法算法渐近复杂度的核心指标（tool-1-1）。
- **尚未证实：** 这批成果的具体数量、LLM 与 Lean 各自贡献多少、证明是否经过同行评审或独立复核，以及 Lean 形式化与 informal 证明是否存在实质出入，均无独立确认；Aaronson 的“奇点”判断是个人评论，九分之四的指数结论目前也只是一篇预印本（tool-1-2、tool-1-3）。

</div>

## 背景

Lean 是一个交互式定理证明器：证明写成代码后由内核逐步检查，Mathlib 是它的标准数学库；因此“在 Lean 中完成证明”比口头论证更容易被机器验证，但也带来证明体积，以及形式化证明与原始问题是否一致的问题。AI Daily Radar 11 月 23 日的日报曾报道，OpenAI 的 GPT-6.2 Astra 独立给出了 Smoktunowicz 间隙定理的 Lean 证明，并因 Mathlib 缺少关键基础而自行选择证明策略；同一期日报还记录了围绕一份 1700 万行 Lean 证明产物的争论，评论者担心错误可能藏在转换后的子证明或庞大体量中。Aaronson 这篇文章所谈论的，正是这类进展累积后引发的公开讨论。

## 为什么重要

对数学家和形式化证明社区来说，判断一项结果是否成立的门槛正在从“同行评议接受”转向“能否在 Lean 中通过机器检查”，因此这波进展的实际价值取决于每个宣称的证明是否附带可复现的 Lean 工件，以及 Lean 形式化与自然语言陈述是否逐条对应——这正是评论区中一位读者反对把形式化瑕疵当作“琐碎细节”一笔带过的理由。需要注意的是，形式化覆盖仍远未跟上：有报道称 OpenAI 的数学论文仓库中约 42% 已在 Lean 中形式化，这意味着多数 AI 辅助结果在短期内仍需人工核对非形式化部分，读者在引用这类“已解决”问题时，应先确认验证范围而不只是结论。

## 后续看点

后续可关注这些证明能否通过独立复核和同行评审，尤其是 Lean 形式化证明与通俗证明之间是否存在实质差异；相关论文的正式发表将是关键检验。

## 延伸阅读

- [Computational complexity of matrix multiplication - Wikipedia](https://en.wikipedia.org/wiki/Computational_complexity_of_matrix_multiplication)
- [The Matrix Multiplication Exponent Is Nine Fourths | alphaXiv](https://www.alphaxiv.org/abs/2611.matrix-multiplication-exponent-lower-bound)
- [math/preprints/ The - matrix - multiplication - exponent - is ...](https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf)
- [2026-11-23 — GPT-6.2 Astra produces machine-verifiable Lean proof of Smoktunowicz's gap theorem](https://the-decoder.com/gpt-6-2-astra-solved-a-math-theorem-no-other-ai-could-crack-then-invented-its-own-proof-strategy/)
- [2026-11-23 — Blog post on 17-million-line Lean artifact sparks LLM proof debate](https://micjm.com/blog/yes-17m-lines-of-lean-is-a-lot/)
- [OpenAI Math Repository Formalizes About 42% in Lean [ 2026 ]](https://tech-insider.org/openai-math-papers-lean-verification-42-percent-2026/)

<div class="community" markdown="1">

## 社区讨论（观点，不是证据）

评论区围绕两点争论：一是没有 LLM、仅靠 Lean/MathLib 和算力是否也能取得同样进展；二是 Lean 证明与通俗证明之间的细微出入是否应被认真对待，而不是被当作无关紧要的细节。

</div>

{% endraw %}
