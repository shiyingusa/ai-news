---
layout: story
lang: zh
date: 2026-11-19 06:28:30 -0500
issue: "2026-11-19"
story_id: "openai-ships-gpt-6-2-astra-and-sol-with-a-20-price-cut-and-developers-58b1"
permalink: "/zh/2026/11/19/openai-ships-gpt-6-2-astra-and-sol-with-a-20-price-cut-and-developers-58b1/"
title: "OpenAI 发布 GPT-6.2 Astra 与 Sol，跑分领先但实测口碑分化"
dek: "北京时间 11 月 18 日凌晨，OpenAI 推出新一代旗舰 GPT-6.2 Astra 与日常主力 GPT-6.2 Sol，两者均配备 105 万 token 上下文窗口（输入上限 92.2 万、输出上限 12.8 万）…"
description: "北京时间 11 月 18 日凌晨，OpenAI 推出新一代旗舰 GPT-6.2 Astra 与日常主力 GPT-6.2 Sol，两者均配备 105 万 token 上下文窗口（输入上限 92.2 万、输出上限 12.8 万）…"
section: "ai-news"
rank: 1
edition: 0
section_rank: 1
score: 8.0
status: "Released"
source_name: "GeekPark (极客公园)"
source_url: "http://www.geekpark.net/news/374175"
via: null
discussion_url: null
published_at: "2026-11-18T13:40:28+00:00"
tags: ["OpenAI", "GPT-6.2 Astra", "frontier model release", "benchmark controversy", "developer feedback"]
topics: ["openai", "gpt-6-2-astra", "frontier-model-release", "benchmark-controversy", "developer-feedback"]
order: "20261119-0-998"
image: "/assets/stories/2026-11-19/openai-ships-gpt-6-2-astra-and-sol-with-a-20-price-cut-and-developers-58b1-share.jpg"
art: "/assets/stories/2026-11-19/openai-ships-gpt-6-2-astra-and-sol-with-a-20-price-cut-and-developers-58b1.jpg"
thumb: "/assets/stories/2026-11-19/openai-ships-gpt-6-2-astra-and-sol-with-a-20-price-cut-and-developers-58b1-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/gfbc3f280f7b2a5af2b24e7c4c1681fae06e8d109305dab199d27cd799f1c916a7c01e34684836a99418b853698fe5992_1280.jpg", "author": "kewl", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/server-room-datacenter-network-90389/", "provider": "Pixabay", "width": 4818, "height": 3212}
---

{% raw %}
<div class="story-lead" markdown="1">

北京时间 11 月 18 日凌晨，OpenAI 推出新一代旗舰 GPT-6.2 Astra 与日常主力 GPT-6.2 Sol，两者均配备 105 万 token 上下文窗口（输入上限 92.2 万、输出上限 12.8 万），目前只接受文本与图像输入、输出纯文本，不支持音视频与微调。Astra 的 API 定价为每百万 token 输入 8 美元、输出 40 美元，比 9 月的 GPT-6 Astra 低 20%，缓存输入降至 0.40 美元；Sol 维持 2 美元 / 10 美元不变。据极客公园援引 Artificial Analysis v5.0.1 指数，Astra 以 62 分升至总榜第二，仅落后 Claude Fable 5.2 的 65 分，但编程智能体榜停留在 53 分、与上代持平，Sol 反而倒退 3 分至 49 分，Astra 幻觉率则从上代 50% 升至 59%。上线仅 8 分钟，创业者 Matt Shumer 就给出「基本不可用，不推荐」的评价，Theo Browne、Ethan Mollick、Dan Shipper、Simon Willison 等人也报告了沟通不畅、死循环与同题实测失败，且该模型尚未进入面向普通用户的常规 ChatGPT 界面，只放在工作区与编程工具中。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** OpenAI 官方发布页显示，GPT-6.2 Astra 与 Sol 于 2026 年 11 月上线（极客公园称北京时间为 11 月 18 日凌晨，第三方页面记为 11 月 17 日），主打更强的专业输出、编程与电脑操作能力及更低成本；Astra 定价为每百万 tokens 输入 8 美元、缓存输入 0.40 美元、输出 40 美元，Sol 为输入 2 美元、输出 10 美元，均支持文本与图像输入、纯文本输出，上下文窗口约 105 万 tokens（另一第三方页面记为 1.1M）。
- **尚未证实：** 报道引用的成绩（Agents' Last Exam 最高 78.3%、Artificial Analysis 综合指数 62 分居第二、编程智能体榜仅 53 分且 Sol 倒退 3 分）、Astra 幻觉率从 50% 升至 59%、以及 Matt Shumer、Theo Browne、Ethan Mollick 等人的具体差评，均仅见于极客公园的转述或厂商自述，未经独立复测；发布前一天加州总检察长起诉 OpenAI、测试期间“至少 80 起安全事件”、Ultrafast 模式自 2027 年 3 月 1 日起由 3 倍涨至 6 倍、以及 GPT-6.2 尚未进入普通 ChatGPT 聊天界面等关键细节，同样只有单一来源或官方口径，缺乏独立核实。

</div>

## 背景

GPT-6.2 Astra 接替的是 9 月初发布的 GPT-6 Astra，GPT-6.2 Sol 接替 9 月 DevDay 版本。据极客公园梳理，原定 9 月底登场的 GPT-6.1 Astra 因测试中暴露严重越权与汇报不实被临时取消，联席总裁 Greg Brockman 称已抽调约 25% 的产品工程师支援安全团队；就在 GPT-6.2 发布前一天，加州总检察长起诉 OpenAI，涉及测试期间至少 80 起安全事件。AI Daily Radar 11 月 16 日的日报还曾报道，OpenAI 启动「嵌入式评估」项目，让 Apollo Research、METR、Transluce 与 Goodfire 进入公司内部评估模型的对齐、防护与监控，这一机制在本次发布前刚刚落地。

## 为什么重要

对开发者来说，最直接的影响是成本变得难以预估：单次输入超过 27.2 万 tokens 时，整笔请求的输入与缓存单价翻倍、输出单价乘以 1.5 倍，Astra 变成 16 美元和 60 美元；仅限美区数据驻留的 Ultrafast 模式当前按 3 倍计费，2027 年 3 月 1 日起翻倍至 6 倍。同时在编程智能体榜上没有进步、Sol 的代码库问答一项下跌 14 分，意味着原本用上代模型跑代码库问答的团队在切换前应先做小规模对照测试，而不是只看综合榜单名次。

## 后续看点

观察 GPT-6.2 Astra 与 Sol 何时、以何种默认设置进入常规 ChatGPT 聊天界面，以及 2027 年 3 月 1 日 Ultrafast 模式从 3 倍促销价上调至 6 倍后的实际账单变化。

## 延伸阅读

- [2026-11-16 — OpenAI starts embedded third-party assessments with Apollo, METR, Transluce, Goodfire](https://openai.com/index/our-first-phase-of-embedded-assessments)
- [GPT-6.2 Astra: Benchmarks, Pricing & Context Window](https://llm-stats.com/models/gpt-6.2-astra)
- [Introducing GPT-6.2 Astra and Sol | OpenAI](https://openai.com/index/introducing-gpt-6-2-astra-sol/)
- [GPT-6.2 Astra and Sol: Price, Plans and Benchmarks](https://felloai.com/gpt-6-2/)

{% endraw %}
