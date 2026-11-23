---
layout: story
lang: zh
date: 2026-11-23 13:28:10 -0500
issue: "2026-11-23"
story_id: "zhipu-s-glm-5-4-runs-28-layers-twice-in-a-750b-loop-transformer-5094"
permalink: "/zh/2026/11/23/zhipu-s-glm-5-4-runs-28-layers-twice-in-a-750b-loop-transformer-5094/"
title: "智谱发布 GLM-5.4：首个 Loop Transformer，28 层各跑两遍"
dek: "智谱（Z.ai）发布旗舰模型 GLM-5.4，采用“循环”（loop）架构：28 个层在推理时各执行两遍，模型总参数 7500 亿。"
description: "智谱（Z.ai）发布旗舰模型 GLM-5.4，采用“循环”（loop）架构：28 个层在推理时各执行两遍，模型总参数 7500 亿。"
section: "ai-news"
rank: 1
edition: 0
section_rank: 1
score: 8.0
status: "Released"
source_name: "z.ai"
source_url: "https://z.ai/blog/glm-5.4"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50609685"
published_at: "2026-11-23T10:06:43+00:00"
tags: ["model release", "loop transformers", "Zhipu GLM", "LLM architecture", "inference efficiency"]
topics: ["model-release", "loop-transformers", "zhipu-glm", "llm-architecture", "inference-efficiency"]
order: "20261123-0-998"
image: "/assets/stories/2026-11-23/zhipu-s-glm-5-4-runs-28-layers-twice-in-a-750b-loop-transformer-5094-share.jpg"
art: "/assets/stories/2026-11-23/zhipu-s-glm-5-4-runs-28-layers-twice-in-a-750b-loop-transformer-5094.jpg"
thumb: "/assets/stories/2026-11-23/zhipu-s-glm-5-4-runs-28-layers-twice-in-a-750b-loop-transformer-5094-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g8c2fc366df9e988ccc1f93bd569de4063eaef9871e390d2f155d7b5fadc641478f74c6f520c73e6a3dfca217f77b1a866511c4eb95666f61c3b69ffb402e3f8b_1280.jpg", "author": "Akela999", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/data-center-engine-room-2476790/", "provider": "Pixabay", "width": 4096, "height": 2160}
---

{% raw %}
<div class="story-lead" markdown="1">

智谱（Z.ai）发布旗舰模型 GLM-5.4，采用“循环”（loop）架构：28 个层在推理时各执行两遍，模型总参数 7500 亿。公司称这一设计可对标 2 万亿至 3 万亿参数级别的模型，但据 The Decoder 报道，目前公开的基准分数只来自一个 300 亿参数的测试用小模型，7500 亿参数的正式模型尚无自家跑分。智谱把 GLM-5.4 定位为“广义编程”（Generalized Coding）的起点，即代码不仅生成程序，还能产出视频、游戏和 CAD 模型。可用性上，该模型目前不在 OpenRouter 或 Z.ai 常规 API 套餐中提供，开发者需改用其 Coding Plan，所获 API key 与常规 key 用法一致，但可访问新模型。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** 智谱在自家发布说明中称 GLM-5.4 为 7500 亿参数、28 层循环执行两次的架构；The Decoder 报道了该架构细节及“对标 2–3 万亿参数模型”的公司说法；开发者 Simon Willison 实测确认该模型只能通过 Coding Plan 获取，且该套餐的 API key 与常规 key 用法相同。
- **尚未证实：** 7500 亿参数模型本体没有任何公开基准分数，仅有 300B 测试模型的数据；“以一半层数达到 2–3 万亿参数模型水平”目前只是公司自述，缺少独立评测；价格、完整开放日期以及是否会进入常规 API 或 OpenRouter 均未说明。

</div>

## 背景

在主流 Transformer 推理中，每生成一个 token 都要把每一层的权重从显存（HBM）搬到芯片上算一次，权重搬运的内存带宽因此长期是推理速度的头号瓶颈。所谓 Loop Transformer，是让同一批权重在一次前向中被重复计算多遍——用一个“循环”代替堆叠更多独立层，从而在不增加权重读取量的前提下增加有效计算深度。作为参照，阿里在 11 月 16 日的发布中把旗舰 Qwen4-Max 做到 2.4 万亿总参数、每 token 激活 710 亿，而 Z.ai 称 GLM-5.4 仅以 7500 亿参数、28 层跑两遍即可对标 2 万亿至 3 万亿参数级别的模型。

## 为什么重要

循环架构针对的是推理中最硬的瓶颈：生成每个 token 都要把整层权重从 HBM 内存搬到芯片上算一次，内存带宽因此长期是推理速度的第一限制；让同一批权重留在片上算两遍，可以减少搬运开销。对开发者的直接后果在接入方式而非算法：想调用 GLM-5.4 必须订阅 Coding Plan，走原有常规 API 套餐或 OpenRouter 的调用会拿不到该模型，迁移前需先确认计费与配额。

## 后续看点

值得关注智谱何时公布 7500 亿参数正式模型自身的基准成绩，以及第三方对循环架构在同等显存带宽下实际吞吐的独立测试结果。

## 社区讨论

Hacker News 讨论中，有评论者认为智谱给出的技术细节相当透明，并称循环 Transformer 是显而易见的方向、只是仍有工程问题待解；另一位评论者从 HBM 带宽角度解释了循环层为何能省下权重搬运开销。开发者 Simon Willison 则记录了实测经历：为拿到 GLM-5.4 不得不切换到 Coding Plan，并对比称 GLM-5.2 生成同一“鹈鹕”测试题时默认使用渐变与动画，风格明显不同。也有用户抱怨部分中国模型“马拉松式思考”，在最简单的任务上反复自我怀疑、完成时间远高于前沿模型。

## 本事件的相关报道

- 2026-11-23 · z.ai: [GLM-5.4: Toward Generalized Coding with Our First Loop Transformer](https://z.ai/blog/glm-5.4)
- 2026-11-23 · The Decoder: [Z.ai follows OpenAI into loop transformer territory with its new 750B flagship model](https://the-decoder.com/z-ai-follows-openai-into-loop-transformer-territory-with-its-new-750b-flagship-model/)

## 延伸阅读

- [2026-11-16 — Alibaba launches Qwen4-Max flagship with 2.4T parameters](https://qwen.ai/blog?id=qwen4-max)

{% endraw %}
