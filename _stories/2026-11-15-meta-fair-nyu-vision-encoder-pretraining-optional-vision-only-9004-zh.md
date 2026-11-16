---
layout: story
lang: zh
date: 2026-11-15 06:00:00 -0500
issue: "2026-11-15"
story_id: "meta-fair-nyu-vision-encoder-pretraining-optional-vision-only-9004"
permalink: "/zh/2026/11/15/meta-fair-nyu-vision-encoder-pretraining-optional-vision-only-9004/"
title: "Meta FAIR/NYU：视觉编码器预训练可省，视觉专用参数不可省"
dek: "Meta FAIR 与 NYU 的研究者从零训练 200 多个多模态大模型，逐项拆开视觉编码器的三个选择：是否单独预训练、是否保留视觉专用参数、以及是否放在 LLM 之前…"
section: "ai-news"
rank: 4
section_rank: 4
score: 7.0
status: "Demonstrated"
source_name: "Reddit r/MachineLearning"
source_url: "https://www.reddit.com/r/MachineLearning/comments/1xx1k2o/meta_fair_nyu_unbundling_multimodal_vision/"
via: null
discussion_url: null
published_at: "2026-11-15T17:38:16+00:00"
tags: ["multimodal learning", "vision encoders", "MLLMs", "model scaling", "AI research"]
topics: ["multimodal-learning", "vision-encoders", "mllms", "model-scaling", "ai-research"]
order: "20261115-995"
image: "/assets/stories/2026-11-15/meta-fair-nyu-vision-encoder-pretraining-optional-vision-only-9004-share.jpg"
art: "/assets/stories/2026-11-15/meta-fair-nyu-vision-encoder-pretraining-optional-vision-only-9004.jpg"
thumb: "/assets/stories/2026-11-15/meta-fair-nyu-vision-encoder-pretraining-optional-vision-only-9004-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/gec1cbe426358881cda567032e3dbfdca1b4bce08c4d6693fdedb6690799d6432c31b39b50bd7ec93fd527a5285d1f9153158849933b82ee802d4e9aa0edcc77c_1280.jpg", "author": "stevepb", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/dumbbells-shoes-sneakers-2465478/", "provider": "Pixabay", "width": 5472, "height": 3648}
description: "Meta FAIR 与 NYU 的研究者从零训练 200 多个多模态大模型，逐项拆开视觉编码器的三个选择：是否单独预训练、是否保留视觉专用参数、以及是否放在 LLM 之前…"
---

{% raw %}
<div class="story-lead" markdown="1">

Meta FAIR 与 NYU 的研究者从零训练 200 多个多模态大模型，逐项拆开视觉编码器的三个选择：是否单独预训练、是否保留视觉专用参数、以及是否放在 LLM 之前；主要比较用 Qwen3-1.7B 和 4B 配置、0.4B 视觉容量，并在 16 个 Cambrian VQA 基准（448 像素）和 12 个语言基准上评测。作者称，在总计算预算相同的情况下，用对比学习、自监督或两种描述目标预训练的编码器最多只能与从零联合训练的编码器表现相当，连“免费”预训练也没有帮助；把 MetaCLIP 预训练延长 6.5 倍，ImageNet 线性探针从 80.4% 升到 84.4%，但 VQA 没有提升。视觉专用参数则不可省：无编码器模型在 0.6B 到 6.4B 各规模上都落后，约需 3 倍计算才能追上；把编码器参数转给 LLM 改善的是文本而非 VQA。放置位置也可变：所谓 in-fusion 在 LLM 前 8 层加入零初始化的视觉专用权重，1.7B 到 6.4B 与独立编码器相当，首 token 时间低约 13%，1.7B 下 VQA 为 45.0，对比编码器的 44.4。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** 预印本《Unbundling Multimodal Vision Encoding》确实已公开（arXiv 编号 2611.17334，标题亦出现在 arXiv cs.CV 最新列表中）；作者之一 /u/trungh98 在 r/MachineLearning 发帖说明，实验用同一份数据从零训练 200 多个多模态大模型，主对比基于 Qwen3-1.7B 与 4B 骨干加 0.4B 视觉参数，评测集为 Cambrian 的 16 个 448px VQA 基准和 12 个语言基准。
- **尚未证实：** 全部结论数字——视觉编码器预训练“最多打平”、无编码器模型需约 3 倍算力追平、in-fusion 降低约 13% 首 token 延迟、1.7B 下 45.0 对 44.4 的 VQA 分数——目前仅出自作者自述的预印本，未经同行评审或第三方复现；帖子本身是摘要，未列出完整基准表，也未交代“免费预训练”对照的具体设置。

</div>

## 背景

多模态大模型（MLLM）要“看图”，通常先由一个视觉编码器（vision encoder，把图像切块并编码成向量序列）处理图像，再把结果送进语言模型；这类编码器往往先在图像数据上单独预训练。业界做法目前并不统一：该帖举例说 Gemma 4 12B 去掉了编码器，Kimi K3 从零训练编码器，Inkling 2 Small 又把它加了回来。问题在于，已发布模型在训练数据、算力以及编码器预训练投入上各不相同，单靠横向比较无法判断究竟是哪一项选择在起作用。

## 为什么重要

对多模态模型构建者，最直接的动作是不要把“有没有预训练视觉编码器”当作架构成败的关键，而要把视觉 token 单独使用的参数保留下来；若选择无编码器路线，作者测得的约 3 倍计算追赶成本应计入预算。in-fusion 的约 13% 首 token 时间优势目前仅来自作者实验，迁移到其他 LLM 或训练配方时需重新验证。

## 延伸阅读

- [Computer Vision and Pattern Recognition](https://arxiv.org/list/cs.CV/recent)

{% endraw %}
