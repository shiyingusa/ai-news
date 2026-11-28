---
layout: story
lang: zh
date: 2026-11-28 06:28:04 -0500
issue: "2026-11-28"
story_id: "deepmind-s-humanity-s-first-exam-finds-top-models-fail-repeated-6c10"
permalink: "/zh/2026/11/28/deepmind-s-humanity-s-first-exam-finds-top-models-fail-repeated-6c10/"
title: "DeepMind“人类首次考试”：顶尖模型难连续答对16题"
dek: "据 The Decoder 报道，Google DeepMind 用名为“Humanity's First Exam”的基准测试了 18 个 AI 模型，发现领先模型几乎每个任务族都至少能答对一次，但在要求连续 16 次答对时仍会失败…"
description: "据 The Decoder 报道，Google DeepMind 用名为“Humanity's First Exam”的基准测试了 18 个 AI 模型，发现领先模型几乎每个任务族都至少能答对一次，但在要求连续 16 次答对时仍会失败…"
section: "ai-news"
rank: 2
edition: 0
section_rank: 2
score: 7.0
status: "Demonstrated"
source_name: "The Decoder"
source_url: "https://the-decoder.com/google-deepminds-humanitys-first-exam-shows-top-ai-models-still-fail-simple-everyday-tasks-under-repeated-runs/"
via: null
discussion_url: null
published_at: "2026-11-28T11:12:30+00:00"
tags: ["AI reliability", "benchmark evaluation", "Google DeepMind", "visual perception", "foundation models"]
topics: ["ai-reliability", "benchmark-evaluation", "google-deepmind", "visual-perception", "foundation-models"]
order: "20261128-0-997"
image: "/assets/stories/2026-11-28/deepmind-s-humanity-s-first-exam-finds-top-models-fail-repeated-6c10-share.jpg"
art: "/assets/stories/2026-11-28/deepmind-s-humanity-s-first-exam-finds-top-models-fail-repeated-6c10.jpg"
thumb: "/assets/stories/2026-11-28/deepmind-s-humanity-s-first-exam-finds-top-models-fail-repeated-6c10-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g652916627956618bf5109f0ed4f67c1e08891480706c124fdb1a829776ef071055ae035c337dff37b2f29e41d3c22de2fb40611847ba804d7120c2fb91d481a9_1280.jpg", "author": "jarmoluk", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/robot-arm-technology-robot-arm-2791670/", "provider": "Pixabay", "width": 3000, "height": 2000}
---

{% raw %}
<div class="story-lead" markdown="1">

据 The Decoder 报道，Google DeepMind 用名为“Humanity's First Exam”的基准测试了 18 个 AI 模型，发现领先模型几乎每个任务族都至少能答对一次，但在要求连续 16 次答对时仍会失败，OpenAI 的 GPT-6.2 Astra 也在其中。测试中 73% 的错误来自视觉感知，增加计算时间也没有消除这一差距。

报道未说明该基准是否公开发布、完整测试方法或是否经过独立复核。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** Google DeepMind 发布了名为“Humanity's First Exam”的评测，共包含 544 道日常题，并公开了部分数据集（Google 官方博客）；The Decoder 报道称，该评测考察了 18 个模型，关键在于要求模型对同一类任务连续 16 次答对，而不只是答对一次。
- **尚未证实：** 哪些模型具体在哪些任务上失败、报道中提到的 GPT-6.2 Astra 等模型的相对位置，“视觉感知占 73% 的错误”和“增加算力时间并不能解决问题”这两项结论，目前都只见于 The Decoder 这一篇二次报道，现有报道未链接 DeepMind 的原始论文、排行榜或完整结果表；另有一条 YouTube 短视频称配套的 Kaggle 竞赛为期三周、截至 12 月 15 日、奖金 5 万美元，也缺少第二个来源佐证。

</div>

## 背景

这项基准的名称戏仿了「Humanity's Last Exam」（人类最后的考试）——一个以极难著称、用来给 AI 出标准化难题的测试；HFE 则反其道而行，专门考察人类几乎都能答对的简单日常问题。据 Google 官方博客介绍，HFE 在 Kaggle 上发布，共 544 道文字与图像提示，衡量的是前沿模型回答的可靠性而非难度上限，Kaggle 上的公开排行榜也以同样口径记录各模型表现。

## 为什么重要

对准备把模型接入日常自动化流程的开发者来说，单次演示成功不能代表可部署性：连续 16 次正确的要求暴露出稳定性缺口，而视觉感知占错误来源的 73%，意味着涉及读图、识别界面的环节更需要额外校验或人工兜底。

## 延伸阅读

- [Humanity ’ s First Exam : Testing LLM reliability](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/humanitys-first-exam/)
- [DeepMind ' s new AI exam | The Neuron](https://www.theneuron.ai/newsletter/deepmind-s-new-ai-exam/)
- [Humanity ' s First Exam (HFE) Leaderboard | Kaggle](https://www.kaggle.com/benchmarks/deepmind/hfe)
- [DeepMind ' s new AI exam | The Neuron](https://www.theneuron.ai/newsletter/deepmind-s-new-ai-exam/)
- [Humanity ’ s First Exam : Testing LLM reliability](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/humanitys-first-exam/)
- [Humanity ' s First Exam от Google DeepMind : $50 000 на... - YouTube](https://www.youtube.com/shorts/tc3boVX6Sec)

{% endraw %}
