---
layout: story
lang: en
date: 2026-11-15 06:00:00 -0500
issue: "2026-11-15"
story_id: "meituan-releases-longcat-2-5-a-1-6t-agent-model-trained-without-nvidia-5ecf"
permalink: "/2026/11/15/meituan-releases-longcat-2-5-a-1-6t-agent-model-trained-without-nvidia-5ecf/"
title: "Meituan releases LongCat-2.5, a 1.6T agent model trained without Nvidia GPUs"
dek: "Meituan has published the weights of LongCat-2.5, a 1.6-trillion-parameter model built for agent tasks, and says it was trained entirely on Chinese hardware with no Nvidia GPUs involved."
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

Meituan has published the weights of LongCat-2.5, a 1.6-trillion-parameter model built for agent tasks, and says it was trained entirely on Chinese hardware with no Nvidia GPUs involved. Meituan reports a score of 88.4 on Terminal Bench, a benchmark for command-line agent work, placing it just behind Claude Opus 5. The published sample deployment runs on 194 Huawei Ascend chips, according to The Decoder's report, which does not give the exact Opus 5 score, the size or duration of the training run, or the license terms attached to the weights.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** The Decoder reports that Meituan published the weights for LongCat-2.5, a 1.6-trillion-parameter model designed for AI agents, and that Meituan's reported Terminal Bench score is 88.4; the article also states the sample deployment runs on 194 Huawei Ascend chips and that Meituan's materials make no mention of Nvidia GPUs.
- **Not yet confirmed:** The 88.4 Terminal Bench figure and the claim that it lands "just behind Claude Opus 5" come from Meituan's own reporting, with no independent benchmark run or methodology details (harness version, number of trials, pass criteria) cited. The assertion that training used only Chinese hardware rests on Meituan's account, which the article does not detail — total chip count, training compute, and whether any non-Chinese accelerators were involved in development are all unstated. The item also omits the model's license terms, context length, and where the weights can be downloaded.

</div>

## Background

Open-weight releases publish a model's weights so developers can download, run, and fine-tune it themselves, unlike closed models available only through an API. Agent models are built for multi-step tasks in which the model calls tools and carries out actions rather than only answering a single prompt. Meituan's release is notable in that context because the source says the model was trained entirely on Chinese hardware and the sample deployment runs on 194 Huawei Ascend chips, with no mention of Nvidia GPUs.

## Why it matters

For teams building agents, LongCat-2.5 is a frontier-scale open-weight option whose training and reference serving setup depend on Huawei Ascend rather than Nvidia, giving a concrete configuration (194 chips) to compare against for anyone evaluating a non-CUDA inference stack. The practical limit is scale: a 1.6-trillion-parameter model still requires a multi-node cluster to serve, so this is a datacenter-scale choice rather than something a small team can run locally, and moving tooling onto Huawei's software ecosystem carries its own porting cost.

## What to watch

Watch for an independent run of LongCat-2.5 on Terminal Bench or a public leaderboard entry, since the 88.4 figure currently rests on Meituan's own reporting, and for the release of full training-hardware and licensing details.

{% endraw %}
