---
layout: story
lang: zh
date: 2026-11-18 18:28:24 -0500
issue: "2026-11-18"
story_id: "openai-says-its-models-lifted-amd-flagship-gpu-ppa-by-up-to-14-bca5"
permalink: "/zh/2026/11/18/openai-says-its-models-lifted-amd-flagship-gpu-ppa-by-up-to-14-bca5/"
title: "OpenAI称模型让AMD旗舰GPU IP的PPA最多改善14%"
dek: "OpenAI 表示，其前沿模型在与 AMD 的合作中，把 AMD 旗舰 GPU IP 的功耗、性能与面积（PPA）指标最多改善了 14%，耗时不到五个月；OpenAI 称这大致相当于一年的优化进度。"
description: "OpenAI 表示，其前沿模型在与 AMD 的合作中，把 AMD 旗舰 GPU IP 的功耗、性能与面积（PPA）指标最多改善了 14%，耗时不到五个月；OpenAI 称这大致相当于一年的优化进度。"
section: "ai-news"
rank: 203
edition: 2
section_rank: 3
score: 8.0
status: "Demonstrated"
source_name: "OpenAI"
source_url: "https://openai.com/index/advancing-chip-design-with-our-models/"
via: "Techmeme"
discussion_url: null
published_at: "2026-11-18T22:10:06+00:00"
tags: ["AI chip design", "OpenAI", "AMD", "semiconductor engineering"]
topics: ["ai-chip-design", "openai", "amd", "semiconductor-engineering"]
order: "20261118-2-996"
image: "/assets/stories/2026-11-18/openai-says-its-models-lifted-amd-flagship-gpu-ppa-by-up-to-14-bca5-share.jpg"
art: "/assets/stories/2026-11-18/openai-says-its-models-lifted-amd-flagship-gpu-ppa-by-up-to-14-bca5.jpg"
thumb: "/assets/stories/2026-11-18/openai-says-its-models-lifted-amd-flagship-gpu-ppa-by-up-to-14-bca5-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g8b88624586942f02f7d70560cba7c58cffd8d469289b95c605f1489850a1bfd2d6db7fc2561b77fd1d7ae2a6ab6c9578682a81aa0a9d50eede88d5e47d8d1145_1280.jpg", "author": "aleksaseverina", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/wafer-rolls-food-dessert-cooking-3390181/", "provider": "Pixabay", "width": 4957, "height": 3305}
---

{% raw %}
<div class="story-lead" markdown="1">

OpenAI 表示，其前沿模型在与 AMD 的合作中，把 AMD 旗舰 GPU IP 的功耗、性能与面积（PPA）指标最多改善了 14%，耗时不到五个月；OpenAI 称这大致相当于一年的优化进度。部分改动已被 AMD 纳入一款送交制造的设计。

上述数字来自 OpenAI 的自述，目前没有独立基准或第三方验证，也未披露具体 GPU 型号、制程节点，以及 14% 是平均值还是最佳结果。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** OpenAI 在官方文章中声称，其模型在不到五个月内使 AMD 旗舰 GPU IP 的 PPA 最多改善 14%，并称 AMD 已将部分改动纳入一款送交制造的设计。
- **尚未证实：** 上述 14% 改善是否经过独立基准或第三方复测，比较基线、具体 GPU IP、制程节点，以及送交制造的设计是否已流片或量产，OpenAI 均未说明。

</div>

## 背景

PPA 是芯片设计中常用的综合指标，分别代表功耗（Power）、性能（Performance）和面积（Area）；在同等工艺下，PPA 每改善一个百分点都意味着芯片更省电、更快或更小。这些改进作用在 RTL（寄存器传输级）上，也就是用 SystemVerilog 等硬件描述语言写成的电路代码；模型改写 RTL 后，工程师仍需通过仿真、验证并交由代工厂流片。OpenAI 在 8 月曾介绍其工程师如何用前沿模型参与自家芯片工作，此次则把同样的方法用到 AMD 旗舰 GPU IP 和 OpenAI 自家的 Jalapeño 推理芯片上。

## 为什么重要

如果这一结果可复现，芯片团队可在流片前用模型更早发现 PPA 优化空间，缩短设计迭代；但当前证据只有 OpenAI 的案例，设计团队在依赖类似方法前应要求可复现的基准、人工优化对照和制造验证数据。

## 后续看点

可关注 AMD 是否公布这款已送交制造设计的流片或量产时间，以及 OpenAI 是否发布可复现的 PPA 对比方法和数据。

## 本事件的相关报道

- 2026-11-18 · The Decoder: [OpenAI says its models delivered a year's worth of chip optimization on top of AMD's own engineering](https://the-decoder.com/openai-says-its-models-delivered-a-years-worth-of-chip-optimization-on-top-of-amds-own-engineering/)
- 2026-11-18 · OpenAI: [OpenAI says its models improved power, performance, and area by up to 14% on AMD's flagship GPU IP; some changes are in a design AMD sent for manufacturing (OpenAI)](https://openai.com/index/advancing-chip-design-with-our-models/)

## 延伸阅读

- [Advancing chip design with OpenAI models](https://openai.com/index/advancing-chip-design-with-our-models/)
- [OpenAI AMD Chip Design: 14% PPA in 5 Months (Nov 2026 ...](https://explainx.ai/blog/openai-amd-jalapeno-chip-design-astra-ppa-november-2026)

{% endraw %}
