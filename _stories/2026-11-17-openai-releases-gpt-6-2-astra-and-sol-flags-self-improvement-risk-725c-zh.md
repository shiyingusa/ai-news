---
layout: story
lang: zh
date: 2026-11-17 06:00:00 -0500
issue: "2026-11-17"
story_id: "openai-releases-gpt-6-2-astra-and-sol-flags-self-improvement-risk-725c"
permalink: "/zh/2026/11/17/openai-releases-gpt-6-2-astra-and-sol-flags-self-improvement-risk-725c/"
title: "OpenAI 发布 GPT-6.2 Astra 与 Sol，API 更便宜"
dek: "OpenAI 发布 GPT-6.2 Astra 与 Sol 两款模型，现已在 ChatGPT Work 和 Codex 中向 Plus、Pro、Enterprise 与 Edu 用户开放。"
description: "OpenAI 发布 GPT-6.2 Astra 与 Sol 两款模型，现已在 ChatGPT Work 和 Codex 中向 Plus、Pro、Enterprise 与 Edu 用户开放。"
section: "ai-news"
rank: 201
edition: 2
section_rank: 1
score: 9.0
status: "Available"
source_name: "OpenAI"
source_url: "https://openai.com/index/introducing-gpt-6-2-astra-sol/"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50535230"
published_at: "2026-11-17T17:46:43+00:00"
tags: ["model release", "OpenAI", "frontier models", "inference cost", "benchmarks"]
topics: ["model-release", "openai", "frontier-models", "inference-cost", "benchmarks"]
order: "20261117-2-998"
image: "/assets/stories/2026-11-17/openai-releases-gpt-6-2-astra-and-sol-flags-self-improvement-risk-725c-share.jpg"
art: "/assets/stories/2026-11-17/openai-releases-gpt-6-2-astra-and-sol-flags-self-improvement-risk-725c.jpg"
thumb: "/assets/stories/2026-11-17/openai-releases-gpt-6-2-astra-and-sol-flags-self-improvement-risk-725c-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g797b75737d91a9171df88afa45a3540b4f12ef697c562c46528d4170fc75fa35526b4fbd743c7fc476f2b02782dd906410edbbc35e132553c0138afda111c284_1280.jpg", "author": "Akela999", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/data-center-engine-room-2476790/", "provider": "Pixabay", "width": 4096, "height": 2160}
---

{% raw %}
<div class="story-lead" markdown="1">

OpenAI 发布 GPT-6.2 Astra 与 Sol 两款模型，现已在 ChatGPT Work 和 Codex 中向 Plus、Pro、Enterprise 与 Edu 用户开放。据 The Decoder 援引的第三方评测，在 Artificial Analysis 主指数中 Astra 位列第二、仅落后 Claude Fable 5.2，Epoch AI 的评测则把两者并列，编码一项与上一代 GPT-6 Astra 持平。

报道还称 Astra 是首个在 OpenAI 自评量表上达到「AI 自我改进」High 阈值的已发布模型，OpenAI 自己把这一档位标注为风险。价格与速度的具体改善目前主要来自社区自测：有开发者称在同一套数据分析考题上，Astra 成本从约 20 美元降至约 4 美元、Sol 从 2.6 美元降至 1.2 美元，准确率相近且速度更快。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** Artificial Analysis 的 Intelligence Index 显示，GPT‑6.2 Astra 排名第二，仅落后 Claude Fable 5.2（The Decoder 与 Techmeme 均转述）；OpenAI 页面称开发者可通过 API 调用 gpt‑6.2‑astra 和 gpt‑6.2‑sol，两款模型发布时即提供 Ultrafast。Techmeme 摘要还称，两款模型已在 ChatGPT Work 和 Codex 向 Plus、Pro、Enterprise、Edu 用户开放。
- **尚未证实：** 具体 API 定价与相对前代的降价幅度未在材料中给出；HN 评论者所称 Astra 在数据解析考试中从约 20 美元降至 4 美元、PacBench 得分 92/6.6 分钟/2.04 美元等，均为第三方自测或转述，未经 OpenAI 或独立机构逐项确认。The Decoder 称 Astra 是首个达到 OpenAI 自评“High”自我改进阈值的已发布模型，也仅见该媒体报道；且 Techmeme 称 Epoch AI 将 Astra 与 Fable 5.2 列为持平，与 Artificial Analysis 的排名结论并不一致。

</div>

## 背景

GPT-6.2 是 GPT-6 系列的一次版本更新：此前已有 GPT-6（Astra）与 GPT-6.1，The Decoder 引述的对比显示 6.2 在编程能力上与 GPT-6 Astra 基本持平。文中反复出现的 Artificial Analysis Intelligence Index 是第三方机构汇总多项测试给出的模型能力排行，GPT-6.2 Astra 在该榜位列第二，仅次于 Claude Fable 5.2；Epoch AI 的评测则把两者列为并列。OpenAI 自家的“AI 自我改进”能力刻度，指的是模型能否显著加速 AI 研发本身，达到“High”档即被 OpenAI 自己标记为风险，而 Astra 是该刻度上首个达到这一档的已发布模型。

## 为什么重要

对批量跑 agent 或数据任务的团队，这次降本主要来自 token 用量减少约 20% 和所需工具调用次数变少，而不是单纯的单价下调；同一开发者指出模型有时会「提前收工」而没找到正确答案，因此用自家任务集复核准确率比只比较报价更关键。

## 后续看点

留意 OpenAI 部署安全中心（deploymentsafety.openai.com）后续更新的系统卡与评测结果：该中心的评测套件会持续更新，GPT-6 Astra 在新版评测中的分数已与旧版系统卡不同，因此 GPT-6.2 Astra 在“评估意识”和规避思维链监控方面的表现是否会被重新量化、是否触发额外的部署限制，是下一个可查证的节点。同时可对照 Artificial Analysis 的 AA-Omniscience 幻觉率（最高努力档下 Astra 59%、Sol 55%），观察第三方复测是否给出相同数字。

## 本事件的相关报道

- 2026-11-17 · OpenAI: [GPT‑6.2 Astra and Sol](https://openai.com/index/introducing-gpt-6-2-astra-sol/)
- 2026-11-17 · The Decoder: [OpenAI launches GPT-6.2 Astra and Sol with lower API prices and some benchmark gains](https://the-decoder.com/openai-launches-gpt-6-2-astra-and-sol-with-lower-api-prices-and-some-benchmark-gains/)

## 延伸阅读

- [OpenAI has the #2 model in the Intelligence ... | Artificial Analysis](https://artificialanalysis.ai/articles/openai-has-the-2-model-in-the-intelligence-index-with-the-release-of-gpt-6-2-astra-and-gpt-6-2-sol)
- [Introducing GPT - 6 . 2 Astra and Sol | OpenAI](https://openai.com/index/introducing-gpt-6-2-astra-sol/)
- [GPT - 6 . 2 System Card - OpenAI Deployment Safety Hub](https://deploymentsafety.openai.com/gpt-6-2-astra-sol)
- [OpenAI has the #2 model in the Intelligence Index... | Artificial Analysis](https://artificialanalysis.ai/articles/openai-has-the-2-model-in-the-intelligence-index-with-the-release-of-gpt-6-2-astra-and-gpt-6-2-sol)

<div class="community" markdown="1">

## 社区讨论（观点，不是证据）

开发者 chriddyp 报告了自家数据分析考试的成本实测（Astra 约 20→4 美元、Sol 2.6→1.2 美元，准确率相近），并提醒部分题目上模型提前结束、未给出目标答案。另一位用户 thefourthchime 的 PacBench 测试显示 Astra 得分 92、耗时 6.6 分钟、花费 2.04 美元，略低于 Kimi K3.1 Pro 的 93 分，但后者耗时 11.5 分钟、仅花费 0.68 美元；也有评论认为发布帖的讨论常常偏离到竞品身上。

</div>

{% endraw %}
