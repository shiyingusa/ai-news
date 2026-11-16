---
layout: story
lang: zh
date: 2026-11-16 06:00:00 -0500
issue: "2026-11-16"
story_id: "anthropic-says-claude-mythos-preview-cut-amd-mi355x-onboarding-to-three-851a"
permalink: "/zh/2026/11/16/anthropic-says-claude-mythos-preview-cut-amd-mi355x-onboarding-to-three-851a/"
title: "Anthropic 称 Mythos 三天完成 AMD MI355X 内核适配"
dek: "Anthropic 在 IPO 路演中告诉投资者，Claude Mythos Preview 在“几乎无人工干预”下…"
description: "Anthropic 在 IPO 路演中告诉投资者，Claude Mythos Preview 在“几乎无人工干预”下…"
section: "chips-compute"
rank: 18
edition: 0
section_rank: 3
score: 7.0
status: "Demonstrated"
source_name: "Tom's Hardware"
source_url: "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-says-claude-mythos-slashed-software-work-to-onboard-amd-gpus-from-up-to-12-months-to-around-three-days-writing-almost-100-percent-of-kernels-autonomously-chips-away-at-nvidias-cuda-moat"
via: null
discussion_url: null
published_at: "2026-11-16T15:00:00+00:00"
tags: ["AI compute", "AMD GPUs", "CUDA moat", "kernel automation", "Anthropic"]
topics: ["ai-compute", "amd-gpus", "cuda-moat", "kernel-automation", "anthropic"]
order: "20261116-0-981"
image: "/assets/stories/2026-11-16/anthropic-says-claude-mythos-preview-cut-amd-mi355x-onboarding-to-three-851a-share.jpg"
art: "/assets/stories/2026-11-16/anthropic-says-claude-mythos-preview-cut-amd-mi355x-onboarding-to-three-851a.jpg"
thumb: "/assets/stories/2026-11-16/anthropic-says-claude-mythos-preview-cut-amd-mi355x-onboarding-to-three-851a-640.jpg"
photo_credit: null
---

{% raw %}
<div class="story-lead" markdown="1">

Anthropic 在 IPO 路演中告诉投资者，Claude Mythos Preview 在“几乎无人工干预”下，约三天完成了让一个 Anthropic 模型在 AMD MI355X 上以可用性能运行提示处理（prompt processing）所需的软件工作，并移植或编写了近 100% 的 GPU 内核；而过去这类工作据称需要 6 到 12 个月、数十名工程师。该数字仅覆盖一个模型和提示处理，且来自公司自述，尚无独立基准。Anthropic 今年首次使用 AMD GPU，并已签下最高 2 吉瓦的 AMD Instinct GPU 协议，其招股书称能“以过去一小部分时间”接入新芯片平台。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** Anthropic 在 IPO 路演视频中向投资者作出该表述，幻灯片脚注将三天限定为一个模型的提示处理；Tom's Hardware 报道了路演内容。
- **尚未证实：** 6–12 个月的旧基准来自 Anthropic 的“历史经验”，“几乎 100% 内核”“基本无人工干预”和实际性能均未独立复现，也未说明训练或其他模型是否同样适用。

</div>

## 背景

Kernel（内核）是直接跑在某一款芯片上的底层计算代码，模型性能能不能发挥，很大程度取决于它；英伟达的 CUDA 平台已近二十年，AMD 的对应平台是 ROCm，编程层为 HIP，为 CUDA 写的代码要经过 HIPify 等工具转换才能在 AMD 卡上运行，这层转换成本长期被视作 CUDA 护城河的一部分。Anthropic 此前已同时使用英伟达与 AMD 的 GPU，以及 Google TPU 和 AWS Trainium，并与 AMD 签有最高 2 吉瓦的 Instinct GPU 供货协议。这一时间对比之所以在此刻出现，是因为它属于 IPO 路演材料：11 月 15 日的日报曾报道，公司 CEO Dario Amodei 在 IPO 前几天把购买算力称为公司「最深的商业困境」，并提到近 9010 亿美元的算力承诺（tool-1-2），因此多芯片路线能否省下工程成本，对投资者而言是可核查的具体问题。

## 为什么重要

如果该方法可复现，采购 AMD 等非 Nvidia 加速器的软件迁移成本会从以年计降到以天计，CUDA 的锁定效应随之减弱；但企业在下单前仍应要求第三方复现和端到端基准，而不能把厂商自述当作可用性保证。

## 后续看点

Anthropic 的 IPO 预计在下周进行，招股书和路演材料可能补充多芯片部署与成本细节；之后关注是否有独立团队复现 MI355X 上的内核生成和端到端性能。

## 延伸阅读

- [2026-11-15 — Amodei calls compute Anthropic's "deepest business dilemma" before IPO](https://the-decoder.com/anthropic-ceo-amodei-admits-theres-a-huge-uncertainty-in-whats-going-to-happen-next-year-days-before-a-record-ipo/)

{% endraw %}
