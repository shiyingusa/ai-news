---
layout: story
lang: en
date: 2026-11-18 06:00:00 -0500
issue: "2026-11-18"
story_id: "tencent-hy4-flash-draws-mixed-early-tests-on-cost-and-speed-4386"
permalink: "/2026/11/18/tencent-hy4-flash-draws-mixed-early-tests-on-cost-and-speed-4386/"
title: "Tencent Hy4 Flash draws mixed early tests on cost and speed"
dek: "Tencent's Hy4 Flash is a low-cost, fast model that early users are trying through OpenRouter, a service that routes requests to multiple model providers, with mixed task-level results."
description: "Tencent's Hy4 Flash is a low-cost, fast model that early users are trying through OpenRouter, a service that routes requests to multiple model providers, with mixed task-level results."
section: "ai-news"
rank: 3
edition: 0
section_rank: 3
score: 7.0
status: "Available"
source_name: "hy.tencent.ai"
source_url: "https://hy.tencent.ai/research/hy4-flash"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50538184"
published_at: "2026-11-17T21:06:08+00:00"
tags: ["Tencent", "Hy4 Flash", "AI model release", "low-cost inference", "benchmarks"]
topics: ["tencent", "hy4-flash", "ai-model-release", "low-cost-inference", "benchmarks"]
order: "20261118-0-996"
image: "/assets/stories/2026-11-18/tencent-hy4-flash-draws-mixed-early-tests-on-cost-and-speed-4386-share.jpg"
art: "/assets/stories/2026-11-18/tencent-hy4-flash-draws-mixed-early-tests-on-cost-and-speed-4386.jpg"
thumb: "/assets/stories/2026-11-18/tencent-hy4-flash-draws-mixed-early-tests-on-cost-and-speed-4386-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/gc5cf336d1ab1bd93469b06736f8fa2323a42df10d9b32644523081e81e4a3a3ecfbee53a1e66ee8cd2741495ea75b6283255d716d75ec0baf151f1d35133bb8c_1280.jpg", "author": "blickpixel", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/it-server-server-cabinet-network-838379/", "provider": "Pixabay", "width": 3095, "height": 2063}
---

{% raw %}
<div class="story-lead" markdown="1">

Tencent's Hy4 Flash is a low-cost, fast model that early users are trying through OpenRouter, a service that routes requests to multiple model providers, with mixed task-level results. In a Plotly data-analytics benchmark cited by commenter chriddyp, it beat GPT-6 Luna on the cheap-and-accurate end and cost $0.13 to answer 43 questions, versus about $20 for high-end frontier models.

Commenters also describe its pricing as cheaper than DeepSeek 1017 and GPT-6 Luna, but one user reports more translation errors than DeepSeek 4.1 Flash 1017. These figures and comparisons come from users, not an independent evaluation or a Tencent specification.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** Plotly's independent benchmark reports Hy4 Flash answered 39 of 43 data-analytics questions for $0.13, making it the cheapest model it has rated A-grade (tool-2-1); Tencent's Hugging Face model card lists 220B total parameters (64B of them "Engram" parameters), 12B active per token, text-and-image input, and a context window of up to 1M tokens (tool-2-2).
- **Not yet confirmed:** that the weights are or will be open — a commenter writes "once they open the weights," so no open-weights release is documented in the supplied evidence; the claim that Hy4 Flash is "faster" than DeepSeek 1017 and GPT-6 Luna, which no independent speed measurement here supports; the roughly $20 cost cited for frontier models; and the report that translation quality lagged DeepSeek 4.1 Flash, which rests on one user's experience. The Plotly benchmark and the model card are separate sources and do not contradict each other on the $0.13 figure or the architecture.

</div>

## Background

A "Flash"-style release is a vendor's cheaper, lower-latency tier rather than its largest model, and Tencent's Hy4 Flash is being judged on that basis against the incumbent budget options commenters name: DeepSeek 4.1 Flash 1017 and GPT-6 Luna. Several commenters describe reaching it through the third-party router OpenRouter, which is how a model from a Chinese provider becomes usable to developers outside its home market without a direct account. One commenter also anticipates that Tencent will release the weights for Hy4 Flash and a standard Hy4 — an expectation stated in the discussion, not something the supplied material confirms.

## Why it matters

For developers running high-volume analytics or other narrow tasks, the reported $0.13 for 43 questions makes Hy4 Flash worth benchmarking against incumbent cheap models before switching; the translation complaint shows quality can vary by task, so teams should test on their own data rather than rely on a single benchmark.

## What to watch

Whether Tencent releases Hy4 Flash's weights: commenter chriddyp says that would make it and regular Hy4 the only open models on the analytics exam he runs.

## Further reading

- [Tencent Hy 4 flash Benchmark Results for Data Analysis](https://plotly.com/blog/hy4-flash-plotly-data-analytics-bench/)
- [tencent / Hy 4 - flash · Hugging Face](https://huggingface.co/tencent/Hy4-flash)

<div class="community" markdown="1">

## Community discussion: opinion, not evidence

The most detailed positive report is chriddyp's Plotly benchmark, which claims strong cheap-and-accurate performance; edtechdev's translation errors and ddxv's price comparison frame the debate as task-specific quality versus cost. Another commenter reports using Hy4 Flash through OpenRouter in place of DeepSeek Flash with good results, but these are individual experiences, not a consensus.

</div>

{% endraw %}
