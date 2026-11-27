---
layout: story
lang: zh
date: 2026-11-24 18:24:23 -0500
issue: "2026-11-24"
story_id: "prismml-s-ternary-bonsai-2-5-27b-runs-locally-at-2230-tokens-s-users-ca7e"
permalink: "/zh/2026/11/24/prismml-s-ternary-bonsai-2-5-27b-runs-locally-at-2230-tokens-s-users-ca7e/"
title: "PrismML 发布三值量化模型 Ternary Bonsai 2.5 27B"
dek: "PrismML 发布了 Ternary Bonsai 2.5 27B，这是一个 27B 参数、采用三值量化（权重只取三种取值，从而大幅压缩模型体积与显存占用）的模型；公告页没有给出训练细节、许可证或官方基准数据。"
description: "PrismML 发布了 Ternary Bonsai 2.5 27B，这是一个 27B 参数、采用三值量化（权重只取三种取值，从而大幅压缩模型体积与显存占用）的模型；公告页没有给出训练细节、许可证或官方基准数据。"
section: "ai-news"
rank: 202
edition: 2
section_rank: 2
score: 7.0
status: "Released"
source_name: "prismml.com"
source_url: "https://prismml.com/news/bonsai-2-5-27b"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50633922"
published_at: "2026-11-24T20:08:03+00:00"
tags: ["ternary quantization", "model release", "local LLM inference", "AI community discussion"]
topics: ["ternary-quantization", "model-release", "local-llm-inference", "ai-community-discussion"]
order: "20261124-2-997"
image: "/assets/stories/2026-11-24/prismml-s-ternary-bonsai-2-5-27b-runs-locally-at-2230-tokens-s-users-ca7e-share.jpg"
art: "/assets/stories/2026-11-24/prismml-s-ternary-bonsai-2-5-27b-runs-locally-at-2230-tokens-s-users-ca7e.jpg"
thumb: "/assets/stories/2026-11-24/prismml-s-ternary-bonsai-2-5-27b-runs-locally-at-2230-tokens-s-users-ca7e-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g16368496c2918f02134f91a1946178d3b1339400054a124e64ab3c7df27e5a8f5d954303f03fcdefedab336fb0dbf4b8d46e251745b9017535151fe9a7607927_1280.jpg", "author": "blickpixel", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/it-server-server-cabinet-network-838379/", "provider": "Pixabay", "width": 3095, "height": 2063}
---

{% raw %}
<div class="story-lead" markdown="1">

PrismML 发布了 Ternary Bonsai 2.5 27B，这是一个 27B 参数、采用三值量化（权重只取三种取值，从而大幅压缩模型体积与显存占用）的模型；公告页没有给出训练细节、许可证或官方基准数据。Hacker News 用户报告称，Q2 GGUF 版本在 24GB 内存的 Mac Mini M5 Pro 上生成速度约 22–25 tokens/s、提示处理约 223 tokens/s，128k 上下文可完整放入内存。

另一位用户通过 Unsloth Studio 试用，速度与 MacBook 上的 Inkling 2 mini Q4 相近（约 300 tokens/s 预填充、30 tokens/s 生成），并称其智能体调用表现“可用”。有评论者称该模型在 SWE-bench verified 上与 2026 年 2 月发布的 Opus 4.6 得分相当，但这只是个人判断，目前没有官方或独立评测支持。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** Hacker News 上关于 PrismML 的 Bonsai 2.5 27B 的讨论中，多位评论者称已在本机运行该模型的三值量化版本（Q2 GGUF）：一人在 Mac Mini M5 Pro（24GB 内存、512GB SSD）上测得生成速度约 22.3 tok/s、首字延迟约 2.12 秒、提示处理约 222.9 tok/s，并表示可轻松装下 128k 上下文；另一人通过 Unsloth Studio 在 MacBook 上测得约 300 tok/s 预填充、30 tok/s 生成，并称其智能体调用“稳定”。以上均为用户自测数据，不是厂商基准。
- **尚未证实：** PrismML 官方给出的参数量、量化方案、基准分数、许可证与发布范围在可得材料中均未出现；“在 SWE-bench Verified 上与 Opus 4.6 相当”仅是一位评论者的推测，他本人也质疑其中有多少是“刷榜”、多少是基准本身变化；benchlm.ai 与 anotherwrapper.com 的第三方对比页把该模型与 Claude Opus 4.6 并列，但其中一页标注日期早于本次发布，不能视为独立验证。其在真实智能体编码任务中的表现，以及三值权重除 FPGA 外是否存在硬件加速，同样未得到证实。

</div>

## 背景

三值量化（ternary quantization）把模型权重的取值限定在三个值上，每个权重约 1.58 比特，因此 27B 规模的模型可以压到几 GB，跑在消费级硬件上。PrismML 的前代 Ternary Bonsai 2 27B 就是这个思路的产物：7.67 GB 的三值语言模型，加上从 Qwen3.8-27B 原样沿用、未作改动的 0.92 GB FP16 视觉塔，打包共约 8.6 GB。据 PrismML 的发布说明，2.5 版本维持 5.9 GB 的体积，重点转向智能体编码（agentic coding）、多轮工具调用和多步任务执行，并已在 Hugging Face 以 Q2_0 GGUF 格式提供，同时附有 vLLM 部署说明。

## 为什么重要

对只有 24GB 统一内存的 Mac 用户而言，一个 27B 模型能以 20 tokens/s 以上运行并容纳 128k 上下文，使本地运行智能体式编程任务从勉强可用变为现实可行；不过这些数字依赖 Q2 GGUF 这类量化格式，且有评论者追问除 FPGA 外是否存在针对三值权重的专用硬件加速，该问题目前尚无答案。

## 后续看点

值得关注的是独立第三方能否复现其 SWE-bench verified 成绩，以及与同等规模 Q1/Q2 量化模型（如 Qwen 系列）的直接速度与质量对比。

## 延伸阅读

- [PrismML — Introducing Ternary Bonsai 2 . 5 27 B : Powering Agentic...](https://prismml.com/news/bonsai-2-5-27b)
- [prism - ml / Ternary - Bonsai - 2 . 5 - 27 B -GGUF · Hugging Face](https://huggingface.co/prism-ml/Ternary-Bonsai-2.5-27B-GGUF)
- [Ternary - Bonsai - 2 - 27 B : A 27 B Model That Fits in 8.6GB | MindStudio](https://www.mindstudio.ai/blog/ternary-bonsai-2-27b-ternary-quantization)
- [Claude Opus 4.6 vs Ternary Bonsai 2 27B: Benchmarks & Cost](https://benchlm.ai/compare/claude-opus-4-6-vs-ternary-bonsai-2-27b)
- [Ternary Bonsai 2 27B Benchmarks & Context (November 2026)](https://benchlm.ai/models/ternary-bonsai-2-27b)
- [Claude Opus 4.6 vs Ternary Bonsai 2 27B - anotherwrapper.com](https://anotherwrapper.com/tools/llm-pricing/claude-opus-4-6/ternary-bonsai-2-27b)

<div class="community" markdown="1">

## 社区讨论（观点，不是证据）

多位用户报告了在 Mac 上的实测吞吐，并认为其智能体调用质量超出预期；一位评论者则怀疑这一成绩有多少来自“刷榜”、基准本身的变化，或小模型追赶前沿的普遍滞后，并直言 SWE-bench verified 代表性有限。另有用户希望看到与同参数量级量化模型的直接对比，而不是与前沿闭源模型比较。

</div>

{% endraw %}
