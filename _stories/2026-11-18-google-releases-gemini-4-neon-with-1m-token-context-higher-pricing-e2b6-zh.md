---
layout: story
lang: zh
date: 2026-11-18 18:28:24 -0500
issue: "2026-11-18"
story_id: "google-releases-gemini-4-neon-with-1m-token-context-higher-pricing-e2b6"
permalink: "/zh/2026/11/18/google-releases-gemini-4-neon-with-1m-token-context-higher-pricing-e2b6/"
title: "谷歌发布 Gemini 4 Neon：百万 token 上下文，定价高于前代"
dek: "谷歌发布新一代前沿模型 Gemini 4 Neon，面向复杂软件工程、知识工作和科学工作流，支持文本、图像、视频、音频和 PDF 输入，上下文窗口为 100 万 token。"
description: "谷歌发布新一代前沿模型 Gemini 4 Neon，面向复杂软件工程、知识工作和科学工作流，支持文本、图像、视频、音频和 PDF 输入，上下文窗口为 100 万 token。"
section: "ai-news"
rank: 201
edition: 2
section_rank: 1
score: 9.0
status: "Released"
source_name: "Google"
source_url: "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50552424"
published_at: "2026-11-18T21:34:07+00:00"
tags: ["Gemini 4 Neon", "Google", "frontier model release", "model naming", "AI model comparison"]
topics: ["gemini-4-neon", "google", "frontier-model-release", "model-naming", "ai-model-comparison"]
order: "20261118-2-998"
image: "/assets/stories/2026-11-18/google-releases-gemini-4-neon-with-1m-token-context-higher-pricing-e2b6-share.jpg"
art: "/assets/stories/2026-11-18/google-releases-gemini-4-neon-with-1m-token-context-higher-pricing-e2b6.jpg"
thumb: "/assets/stories/2026-11-18/google-releases-gemini-4-neon-with-1m-token-context-higher-pricing-e2b6-640.jpg"
photo_credit: {"url": "https://thumb.wikimedia.org/wikipedia/commons/thumb/b/b3/Google_Servers.jpg/1920px-Google_Servers.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail", "author": "Wesley Nitsckie", "licence": "CC BY-SA 2.0", "licence_url": "https://creativecommons.org/licenses/by-sa/2.0", "source_url": "https://commons.wikimedia.org/wiki/File:Google_Servers.jpg", "provider": "Wikimedia Commons", "width": 4288, "height": 2848}
---

{% raw %}
<div class="story-lead" markdown="1">

谷歌发布新一代前沿模型 Gemini 4 Neon，面向复杂软件工程、知识工作和科学工作流，支持文本、图像、视频、音频和 PDF 输入，上下文窗口为 100 万 token。该模型已通过 API、Antigravity 和 Gemini 应用上线，定价为每百万输入 token 3 美元、每百万输出 token 15 美元，高于此前几款 Gemini 4 模型。The Decoder 称这是谷歌一个月内发布的第四款新 Gemini 模型。谷歌对能力的描述是“快速完成端到端任务”，但公布的博客摘要中没有给出基准测试分数或与竞品的对比数据。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** 谷歌博客（作者 Koray Kavukcuoglu）称 Gemini 4 Neon 已面向编程、知识工作和科学场景在 API、Antigravity 和 Gemini 应用中推出；The Decoder 报道其上下文窗口为 100 万 token，支持文本、图像、视频、音频和 PDF，输入/输出定价为每百万 token 3 美元/15 美元，并称这是一个月内第四款新 Gemini 模型。
- **尚未证实：** 谷歌未公布独立或自测基准成绩，“快速完成端到端任务”属厂商说法；社区提到的 Artificial Analysis 指数、与 Carbon 的 CritPt 得分对比、与 Anthropic Opus 5.5 的实际体验差距，均来自 Hacker News 评论者个人使用印象，而非官方或第三方评测数据；各地区的开放范围和速率限制也未说明。

</div>

## 背景

Gemini 4 是谷歌当前的一代模型系列，按 The Decoder 的说法，Neon 是该系列一个月内推出的第四款新模型；评论者提到的同代产品还包括 Argon、Carbon 和 Hydrogen，其中 Carbon 被描述为面向“长时程”任务的型号。在这种密集发版节奏下，Neon 的定位需要与同代其它型号区分开来理解，而不只是看它是否“更强”。

## 为什么重要

对开发者而言，实际成本不只看单价：Neon 的每 token 价格已高于此前的 Gemini 4 型号，而一位评论者称，在生成演示 demo 的同类任务中，Carbon、Hydrogen 和 Neon 的 token 消耗约为 Argon 的 3 到 4 倍。若这一经验在更大范围内成立，完成同一任务的总花费会比单价差距更大，接入前应按自己的任务实测 token 用量再决定是否从旧型号迁移。

## 后续看点

值得关注 Artificial Analysis 等独立评测平台把 Neon 与 Carbon 放在同一量表上的结果，尤其是 CritPt 这类研究级推理评测中的得分变化，以判断“总分更高、特定前沿任务更弱”的定位是否成立。

## 社区讨论

Hacker News 上最集中的抱怨是命名混乱：评论者称业界同时存在 Sol、Astra、Neon、Carbon、Opus、Fable、Mythos、Haiku 等名字，普通用户很难把它们对应到具体用途，希望厂商尽快固定一套命名。另有人认为 Neon 综合分虽高，但 Carbon 仍被定位为长时程模型，在 CritPt 类研究型评测上得分反而更低；也有人表示实际使用中谷歌模型仍不如 Opus 5.5“像同事”，这些均为个人主观体验。

## 本事件的相关报道

- 2026-11-18 · The Decoder: [Google ships Gemini 4 Neon, its fourth new Gemini model in a month](https://the-decoder.com/google-ships-gemini-4-neon-its-fourth-new-gemini-model-in-a-month/)
- 2026-11-18 · Google: [Gemini 4 Neon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)
- 2026-11-18 · Google DeepMind: [Introducing Gemini 4 Neon](https://deepmind.google/blog/introducing-gemini-4-neon/)

{% endraw %}
