---
layout: story
lang: zh
date: 2026-11-16 06:00:00 -0500
issue: "2026-11-16"
story_id: "alibaba-launches-qwen4-max-flagship-with-2-4t-parameters-8468"
permalink: "/zh/2026/11/16/alibaba-launches-qwen4-max-flagship-with-2-4t-parameters-8468/"
title: "阿里发布 Qwen4-Max：2.4 万亿参数，主打长上下文低成本"
dek: "阿里巴巴发布旗舰模型 Qwen4-Max，总参数 2.4 万亿，每个 token 仅激活 710 亿，采用混合架构以大幅削减长上下文成本。"
description: "阿里巴巴发布旗舰模型 Qwen4-Max，总参数 2.4 万亿，每个 token 仅激活 710 亿，采用混合架构以大幅削减长上下文成本。"
section: "ai-news"
rank: 1
edition: 0
section_rank: 1
score: 9.0
status: "Released"
source_name: "qwen.ai"
source_url: "https://qwen.ai/blog?id=qwen4-max"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50513215"
published_at: "2026-11-16T02:14:44+00:00"
tags: ["Qwen4-Max", "model release", "LLM benchmarks", "reasoning models", "AI industry"]
topics: ["qwen4-max", "model-release", "llm-benchmarks", "reasoning-models", "ai-industry"]
order: "20261116-0-998"
image: "/assets/stories/2026-11-16/alibaba-launches-qwen4-max-flagship-with-2-4t-parameters-8468-share.jpg"
art: "/assets/stories/2026-11-16/alibaba-launches-qwen4-max-flagship-with-2-4t-parameters-8468.jpg"
thumb: "/assets/stories/2026-11-16/alibaba-launches-qwen4-max-flagship-with-2-4t-parameters-8468-640.jpg"
photo_credit: null
---

{% raw %}
<div class="story-lead" markdown="1">

阿里巴巴发布旗舰模型 Qwen4-Max，总参数 2.4 万亿，每个 token 仅激活 710 亿，采用混合架构以大幅削减长上下文成本。据 The Decoder 报道，Qwen4-Max 在 Artificial Analysis 智能指数上仅次于 Kimi K3.1 Pro，阿里还计划将更小的 Qwen4 系列开源。社区用户已引用 Artificial Analysis 数据称其得分 43、平均每次任务成本 3.27 美元，并实测了 none、low、high、xhigh 四档推理强度。速度与性价比仍是讨论焦点：有开发者表示此前 Qwen 3.8 输出约 30 tokens/秒，约为 Opus（近 80 tokens/秒）的一半。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** 据 The Decoder 引述阿里官方博客，Qwen4-Max 是总参数 2.4 万亿、每 token 激活 710 亿的混合架构旗舰模型，官方称其显著降低长上下文成本，并计划开源更小的 Qwen4 模型；第三方站点 Artificial Analysis 已收录该模型页面，社区用户 maplet 引用其数据给出 43 分与平均 3.27 美元成本。
- **尚未证实：** 阿里“成本大幅降低”的具体口径与官方定价表、更小开源模型的尺寸、许可证与时间表均未出现在现有材料中；The Decoder 的“价格远低于竞品”与社区成本数据存在张力——按 maplet 的同一说法，GPT-6.1 Sol（medium）为 46 分、平均 0.36 美元，但两者是否同口径统计并不明确，无法直接比较；“仅次于 Kimi K3.1 Pro”的排名也仅见于该报道一处来源。

</div>

## 背景

Qwen4-Max 属于稀疏混合专家（MoE）模型：虽然总参数达 2.4 万亿，但每个 token 只激活其中一部分，因此推理开销远低于参数总量给人的直觉印象；这次每次仅激活 710 亿参数。它与前代 Qwen3.8 Max 参数规模相同，但换用了 3:1 的 GDN-to-QSA 层堆叠并加入原生视觉能力。第三方测评显示其价格为每百万 token 输入 1.50 美元、输出 4.50 美元，明显低于同档竞品。

## 为什么重要

对要跑长上下文或批量任务的开发者，真正该比较的是“每次任务花多少钱”而不是每 token 单价：社区给出的对比显示 Qwen4-Max 的单次成本高于部分闭源模型，而此前的 Qwen 系列模型曾因约 30 tokens/秒的吞吐在 agent 类评测中吃亏，因此选型时应同时实测吞吐量与四档推理强度的表现，而不是只看指数分数。

## 后续看点

阿里承诺开源的小尺寸 Qwen4 模型何时放出、包含哪些规格与许可证；以及 Artificial Analysis 等第三方在统一口径下对 Qwen4-Max 成本与延迟的复核结果。

## 社区讨论

Hacker News 的讨论集中在性价比与速度：maplet 引用 Artificial Analysis 数据称 Qwen4-Max 得 43 分、平均成本 3.27 美元，而 GPT-6.1 Sol（medium）为 46 分、0.36 美元；seizethecheese 则表示 Qwen 3.8 质量不错，却因约 30 tokens/秒的速度拖累了他们自建 opencode 对战系统的评分。Simon Willison 还按 none、low、high、xhigh 四档推理强度做了“鹈鹕”测试，并与 Qwen3.8 Max 的结果对照。

## 本事件的相关报道

- 2026-11-16 · qwen.ai: [Qwen4-Max](https://qwen.ai/blog?id=qwen4-max)
- 2026-11-16 · The Decoder: [Alibaba's Qwen4-Max takes on Opus 5.5, GPT-6, and Kimi K3.1 Pro at much lower prices](https://the-decoder.com/alibabas-qwen4-max-takes-on-opus-5-5-gpt-6-and-kimi-k3-1-pro-at-much-lower-prices/)

## 延伸阅读

- [Alibaba's New Qwen 4 - Max Fails To Overtake Moonshot's Kimi...](https://wccftech.com/alibabas-new-qwen4-max-fails-to-overtake-moonshots-kimi-k3-1-pro-retaining-the-same-parameter-count-with-a-lower-price-and-revamped-native-vision-moe-architecture/)
- [Qwen 4 - Max Is 3x Cheaper Than Opus 5.5, But Worth It? - YouTube](https://www.youtube.com/watch?v=WCRk2TQfvCs)

{% endraw %}
