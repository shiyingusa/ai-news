---
layout: story
lang: zh
date: 2026-11-18 06:00:00 -0500
issue: "2026-11-18"
story_id: "tencent-hy4-flash-draws-mixed-early-tests-on-cost-and-speed-4386"
permalink: "/zh/2026/11/18/tencent-hy4-flash-draws-mixed-early-tests-on-cost-and-speed-4386/"
title: "腾讯 Hy4 Flash 低价模型的数据分析表现引发讨论"
dek: "腾讯发布 Hy4 Flash，作为更便宜、更快的模型，早期用户已可通过 OpenRouter 调用。"
description: "腾讯发布 Hy4 Flash，作为更便宜、更快的模型，早期用户已可通过 OpenRouter 调用。"
section: "ai-news"
rank: 3
edition: 0
section_rank: 3
score: 7.0
status: "Released"
source_name: "hy.tencent.ai"
source_url: "https://hy.tencent.ai/research/hy4-flash"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50538184"
published_at: "2026-11-17T21:06:08+00:00"
tags: ["Tencent", "Hy4 Flash", "AI model release", "low-cost inference", "benchmarks"]
topics: ["tencent", "hy4-flash", "ai-model-release", "low-cost-inference", "benchmarks"]
order: "20261118-0-996"
image: "/assets/stories/2026-11-18/tencent-hy4-flash-draws-mixed-early-tests-on-cost-and-speed-4386-share.jpg"
art: "/assets/stories/2026-11-18/tencent-hy4-flash-draws-mixed-early-tests-on-cost-and-speed-4386.jpg"
thumb: "/assets/stories/2026-11-18/tencent-hy4-flash-draws-mixed-early-tests-on-cost-and-speed-4386-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/gc5cf336d1ab1bd93469b06736f8fa2323a42df10d9b32644523081e81e4a3a3ecfbee53a1e66ee8cd2741495ea75b6283255d716d75ec0baf151f1d35133bb8c_1280.jpg", "author": "blickpixel", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/it-server-server-cabinet-network-838379/", "provider": "Pixabay", "width": 3095, "height": 2063}
---

{% raw %}
<div class="story-lead" markdown="1">

腾讯发布 Hy4 Flash，作为更便宜、更快的模型，早期用户已可通过 OpenRouter 调用。社区成员 chriddyp 称，在 Plotly 的数据分析基准中，它回答 43 道题只花 0.13 美元，而高端前沿模型约需 20 美元，并在“低价且准确”区间优于 GPT-6 Luna。

另有用户称用它替代 DeepSeek Flash 效果良好，但也有用户报告其翻译错误明显多于 DeepSeek 4.1 Flash 1017，显示任务表现并不一致。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** 腾讯在 Hugging Face 模型卡中称 Hy4-flash 总参数 220B（含 64B Engram 参数）、每 token 激活 12B，原生支持文本和图像输入、输出文本，上下文窗口最高 1M tokens；Plotly 的独立测试称该模型在 PlotlyDataAnalyticsBench 上答对 39/43 题、总花费 0.13 美元，并称其为已测最便宜的 A 级模型。
- **尚未证实：** 社区所称“比 DeepSeek 1017 和 Luna 更便宜、更快”缺乏统一口径的独立对比；一位用户称翻译错误多于 DeepSeek 4.1 Flash 1017 仅为单一个例；“开放权重后将成前沿仅有的两个开放模型之一”只是评论者预期，现有材料未说明权重开放时间或许可证。

</div>

## 背景

Hy4 是腾讯自研的模型系列，Flash 是其中定位低成本、低延迟的轻量版本；有评论者提到完整版 Hy4 与 Flash 计划之后开放权重，但现有材料中没有腾讯公布的时间表。在“便宜且快”这一档模型里，DeepSeek 的 Flash 系列是常见的对照基准，多位评论者也把它当作替换对象来比较。

## 为什么重要

对需要大批量运行数据分析问答的团队，社区测得的单次任务成本差距（0.13 美元对约 20 美元）意味着可以用更低成本做批量评测或内部工具；但翻译场景的负面反馈说明基准成绩不能直接外推到所有任务，选型时应按自己的语料复测。

## 后续看点

关注腾讯是否开放 Hy4 Flash 的权重，以及 Plotly 的数据分析基准能否被其他独立测试复现；若权重开放，它才可能成为可自托管的低成本选项。

## 延伸阅读

- [Tencent Hy 4 flash Benchmark Results for Data Analysis](https://plotly.com/blog/hy4-flash-plotly-data-analytics-bench/)
- [tencent / Hy 4 - flash · Hugging Face](https://huggingface.co/tencent/Hy4-flash)

<div class="community" markdown="1">

## 社区讨论（观点，不是证据）

评论区的核心分歧在任务泛化能力：chriddyp 称其在 Plotly 数据分析基准上以极低成本优于 GPT-6 Luna，ddxv 提到其定价低于 DeepSeek 1017 和 Luna，thesurlydev 称经 OpenRouter 替代 DeepSeek Flash 使用效果良好；edtechdev 则报告翻译错误明显多于 DeepSeek 4.1 Flash 1017。上述均为早期用户自测，不能视为独立基准结论。

</div>

{% endraw %}
