---
layout: story
lang: zh
date: 2026-11-15 06:00:00 -0500
issue: "2026-11-15"
story_id: "meituan-releases-longcat-2-5-a-1-6t-agent-model-trained-without-nvidia-5ecf"
permalink: "/zh/2026/11/15/meituan-releases-longcat-2-5-a-1-6t-agent-model-trained-without-nvidia-5ecf/"
title: "美团发布 1.6 万亿参数 LongCat-2.5 智能体模型权重"
dek: "美团已发布 LongCat-2.5 的模型权重，这是一个面向 AI 智能体的 1.6 万亿参数模型；据 The Decoder 报道，其训练全程使用中国硬件，示例部署运行在 194 颗华为升腾芯片上，报道未提及英伟达 GPU。"
section: "ai-news"
rank: 1
section_rank: 1
score: 8.0
status: "Released"
source_name: "The Decoder"
source_url: "https://the-decoder.com/meituan-releases-a-1-6-trillion-parameter-agent-model-that-never-touched-an-nvidia-gpu/"
via: null
discussion_url: null
published_at: "2026-11-15T10:06:06+00:00"
tags: ["Meituan", "LongCat-2.5", "agent models", "Huawei Ascend", "open-weight models"]
topics: ["meituan", "longcat-2-5", "agent-models", "huawei-ascend", "open-weight-models"]
order: "20261115-998"
image: "/assets/stories/2026-11-15/meituan-releases-longcat-2-5-a-1-6t-agent-model-trained-without-nvidia-5ecf-share.jpg"
art: "/assets/stories/2026-11-15/meituan-releases-longcat-2-5-a-1-6t-agent-model-trained-without-nvidia-5ecf.jpg"
thumb: "/assets/stories/2026-11-15/meituan-releases-longcat-2-5-a-1-6t-agent-model-trained-without-nvidia-5ecf-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g457faabd7f3d5daf322b2c4115994a30a5ae175479571af3728860c464eb29d41511b052dbd3567cbc39f772c15c49cc1e73fd25e2fea376e3d93395d9397962_1280.jpg", "author": "bsdrouin", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/network-server-system-2402637/", "provider": "Pixabay", "width": 1920, "height": 1080}
---

{% raw %}
<div class="story-lead" markdown="1">

美团已发布 LongCat-2.5 的模型权重，这是一个面向 AI 智能体的 1.6 万亿参数模型；据 The Decoder 报道，其训练全程使用中国硬件，示例部署运行在 194 颗华为升腾芯片上，报道未提及英伟达 GPU。该报道称其在 Terminal Bench 上得分 88.4，仅次于 Claude Opus 5。上述性能与硬件细节目前来自简短转述，尚缺独立复现和完整技术披露。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** 据 The Decoder 报道，美团已发布 LongCat-2.5 的模型权重，这是一个 1.6 万亿参数、面向 AI agent 的模型；报道称其在 Terminal Bench 上得分 88.4，样本部署运行在 194 颗华为升腾芯片上，且美团在材料中未提及使用 Nvidia GPU。
- **尚未证实：** 88.4 的 Terminal Bench 分数与“训练全程未使用 Nvidia GPU”均来自美团自身或单一媒体的转述，没有独立第三方复现或基准测试细节；报道未给出训练算力规模与成本、模型许可证条款、上下文长度，也未列出 Claude Opus 5 在该基准上的具体分数，因此“仅次于 Opus 5”的排名幅度无法核实。

</div>

## 背景

开放权重（open-weight）指模型训练完成后的参数可被外部下载并自行部署，区别于只能通过 API 调用的闭源模型；面向智能体的模型则强调在多步任务中调用工具和执行操作。Terminal Bench 是文中用于评分的终端任务基准，LongCat-2.5 报告的 88.4 分即来自这项测试。

## 为什么重要

对希望自建智能体模型的开发者，开放权重提供了在非英伟达硬件栈上部署的选项，但样例使用 194 颗升腾芯片，实际适配、吞吐与成本仍需自行验证，Terminal Bench 成绩也有待独立复现。

{% endraw %}
