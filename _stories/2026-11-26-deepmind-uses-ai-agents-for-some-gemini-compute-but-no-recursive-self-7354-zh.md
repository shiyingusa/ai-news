---
layout: story
lang: zh
date: 2026-11-26 06:28:37 -0500
issue: "2026-11-26"
story_id: "deepmind-uses-ai-agents-for-some-gemini-compute-but-no-recursive-self-7354"
permalink: "/zh/2026/11/26/deepmind-uses-ai-agents-for-some-gemini-compute-but-no-recursive-self-7354/"
title: "DeepMind 用 AI 智能体运行部分 Gemini 实验，称递归自我改进仍远"
dek: "据 The Decoder 报道，Google DeepMind 正让 AI 智能体自主运行部分面向下一代 Gemini 模型的实验，并控制一部分相关算力。"
description: "据 The Decoder 报道，Google DeepMind 正让 AI 智能体自主运行部分面向下一代 Gemini 模型的实验，并控制一部分相关算力。"
section: "ai-news"
rank: 2
edition: 0
section_rank: 2
score: 7.0
status: "Demonstrated"
source_name: "The Decoder"
source_url: "https://the-decoder.com/ai-agents-now-control-part-of-deepminds-compute-for-gemini-experiments-but-recursive-self-improvement-remains-distant/"
via: null
discussion_url: null
published_at: "2026-11-25T13:23:36+00:00"
tags: ["AI agents", "Google DeepMind", "Gemini", "recursive self-improvement", "AI safety"]
topics: ["ai-agents", "google-deepmind", "gemini", "recursive-self-improvement", "ai-safety"]
order: "20261126-0-997"
image: "/assets/stories/2026-11-26/deepmind-uses-ai-agents-for-some-gemini-compute-but-no-recursive-self-7354-share.jpg"
art: "/assets/stories/2026-11-26/deepmind-uses-ai-agents-for-some-gemini-compute-but-no-recursive-self-7354.jpg"
thumb: "/assets/stories/2026-11-26/deepmind-uses-ai-agents-for-some-gemini-compute-but-no-recursive-self-7354-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g0929b2185b6d560a856505846154800f161079a126c5dc1ead8aaedfad439c4c332ebacf58ea3c8d50b10c08812d1df5cdb02218b9ad8606b1e7507763ab75db_1280.jpg", "author": "blickpixel", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/it-server-server-cabinet-network-838379/", "provider": "Pixabay", "width": 3095, "height": 2063}
---

{% raw %}
<div class="story-lead" markdown="1">

据 The Decoder 报道，Google DeepMind 正让 AI 智能体自主运行部分面向下一代 Gemini 模型的实验，并控制一部分相关算力。研究负责人 Koray Kavukcuoglu 表示，该实验室距离递归自我改进（AI 系统持续改进自身能力并加速下一轮改进）仍很远。为便于监督，DeepMind 刻意不训练智能体的内部思维链（模型给出答案前的中间推理文本），使其可被审查；Kavukcuoglu 还说，衡量通用人工智能（AGI）应看日常用户信任，而不是基准分数。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** 据 The Decoder 报道，Koray Kavukcuoglu 表示 Google DeepMind 正用智能体运行部分 Gemini 实验，实验室离递归自我改进仍远，且智能体的思维链被刻意保持未训练以便审查。
- **尚未证实：** 智能体具体控制多少算力、实验覆盖哪些任务、对下一代 Gemini 的性能影响，以及这些说法能否被独立验证，报道均未提供。

</div>

## 背景

递归自我改进（recursive self-improvement）指模型在闭环中持续改进自身、无需人类逐步介入；Kavukcuoglu 称其“仍很遥远”，针对的正是这一目标。思维链（chain of thought）是模型在采取行动前生成的内部推理；DeepMind 有意不在训练阶段奖励智能体的思维链，使其保持自然语言形式、便于外部审查。

## 为什么重要

对用智能体做研发自动化的团队来说，DeepMind 的做法把监督落到一个具体设计上：保留未训练的思维链供人审查，而不是只检查实验的最终结果；若要复制这类流程，应同时保留可读的推理日志和人工复核环节。

## 后续看点

后续可关注 Google 下一代 Gemini 模型的发布，以及 DeepMind 是否会披露智能体参与实验的比例、审查记录或独立评估结果。

## 延伸阅读

- [DeepMind AI Agents Now Control Gemini Experiment Compute](https://emergent.sh/news/deepmind-ai-agents-now-control-gemini)

{% endraw %}
