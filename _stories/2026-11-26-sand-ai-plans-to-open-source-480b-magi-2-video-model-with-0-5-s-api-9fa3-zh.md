---
layout: story
lang: zh
date: 2026-11-26 06:28:37 -0500
issue: "2026-11-26"
story_id: "sand-ai-plans-to-open-source-480b-magi-2-video-model-with-0-5-s-api-9fa3"
permalink: "/zh/2026/11/26/sand-ai-plans-to-open-source-480b-magi-2-video-model-with-0-5-s-api-9fa3/"
title: "Sand.ai 计划开源 480B 参数 MAGI-2，API 定价 0.5 元/秒"
dek: "11 月 25 日，Sand.ai 宣布计划尽快开源 MAGI-2 的全量权重：这是一个 480B 总参数的 MoE（混合专家）架构音视频统一模型，单次推理仅激活约 28B 参数。"
description: "11 月 25 日，Sand.ai 宣布计划尽快开源 MAGI-2 的全量权重：这是一个 480B 总参数的 MoE（混合专家）架构音视频统一模型，单次推理仅激活约 28B 参数。"
section: "ai-news"
rank: 4
edition: 0
section_rank: 4
score: 7.0
status: "Announced"
source_name: "GeekPark (极客公园)"
source_url: "http://www.geekpark.net/news/374532"
via: null
discussion_url: null
published_at: "2026-11-26T08:38:54+00:00"
tags: ["视频生成", "开源模型", "MAGI-2", "Sand.ai", "API 定价"]
topics: ["magi-2", "sand-ai", "api"]
order: "20261126-0-995"
image: "/assets/stories/2026-11-26/sand-ai-plans-to-open-source-480b-magi-2-video-model-with-0-5-s-api-9fa3-share.jpg"
art: "/assets/stories/2026-11-26/sand-ai-plans-to-open-source-480b-magi-2-video-model-with-0-5-s-api-9fa3.jpg"
thumb: "/assets/stories/2026-11-26/sand-ai-plans-to-open-source-480b-magi-2-video-model-with-0-5-s-api-9fa3-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g16cabe354a0f9774970e3d066f56c6bdc0bfecccd4f41016e31a700b0b5d61a4447b9f4f87533dfe28765fac4c44ea83df9e38f9668b7d026db1d2e41f9dca76_1280.jpg", "author": "Elchinator", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/source-code-software-computer-4280758/", "provider": "Pixabay", "width": 3000, "height": 2000}
---

{% raw %}
<div class="story-lead" markdown="1">

11 月 25 日，Sand.ai 宣布计划尽快开源 MAGI-2 的全量权重：这是一个 480B 总参数的 MoE（混合专家）架构音视频统一模型，单次推理仅激活约 28B 参数。公司同时公布官方 API 刊例价，1080P 下为 0.5 元/秒，不到 Seedance 2.5 同规格约 4 元/秒的十分之一。Sand.ai 称该模型支持最长 30 秒、1080p 25fps 输出，可混合最多 20 份参考素材（10 张图、5 段视频、5 段音频），并在 Artificial Analysis 图生视频（含音频）维度超过 Seedance 2.5，位居第一。不过权重尚未实际发布，开源日期与许可证条款均未公布，性能对标和成本优势目前都只有公司自己的说法支持。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** 据极客公园报道，Sand.ai 于 11 月 25 日宣布计划尽快开源 MAGI-2 全量权重；该模型为 480B 总参数 MoE 架构、单次推理激活约 28B，官方 API 刊例价为 1080P 每秒 0.5 元。
- **尚未证实：** 权重何时发布、采用何种许可证、“全量”具体涵盖哪些组件均未说明；“AA 榜单第一”出自公司提供的截图与 liblib 盲测对比，并非独立复核结果；0.5 元/秒的计费细则、并发配额，以及本地私有化部署后的真实成本，也都没有第三方验证。

</div>

## 背景

Sand.ai 并非首次开放视频模型：据 YouArt 的模型资料，公司在 2026 年 8 月已释出 MAGI-2 Preview，参数量 114B、单次可生成 10 秒片段，定位是较小的开源版本；而 480B 的旗舰版则在此前以研究预览形式亮相。Sand.ai 在自己的 MAGI-2 博客中表示，随后会跟进开源发布，并给出涵盖完整架构规格、系统细节与评测的技术报告，因此这次宣布的开源仍处于「即将发布」而非已交付的状态。

## 为什么重要

对短剧、信息流广告这类“批量试错、用数量赌概率”的团队来说，成本结构会直接改变：报道给出的闭源工业级价位约 4 元/秒，按行业常见的 3 到 5 次重试率折算，一条可用镜头的单秒全链路成本在 12 到 20 元；若 0.5 元/秒的刊例价成立，同样的钱能测的创意数量约扩大 8 到 10 倍。需要注意的是，千亿参数级模型本地部署仍需相当的算力与运维能力，Sand.ai 称已完成海光、摩尔线程等国产芯片适配，但实际的显存占用与推理吞吐尚未公开。

## 后续看点

接下来要看两件事：MAGI-2 权重实际放出的时间与许可证条款，以及 Artificial Analysis 等第三方榜单能否独立复现其宣称的图生视频（含音频）第一。

## 延伸阅读

- [MAGI - 2 : A 480 B Frontier Video Generation Model](https://sand.ai/blog/magi-2/)
- [MAGI - 2 AI Video Generator: 30s 1080p with Sound | YouArt](https://youart.ai/model/magi-2)

{% endraw %}
