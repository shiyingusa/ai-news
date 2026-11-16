---
layout: story
lang: en
date: 2026-11-16 06:00:00 -0500
issue: "2026-11-16"
story_id: "alibaba-launches-qwen4-max-flagship-with-2-4t-parameters-8468"
permalink: "/2026/11/16/alibaba-launches-qwen4-max-flagship-with-2-4t-parameters-8468/"
title: "Alibaba launches Qwen4-Max flagship with 2.4T parameters"
dek: "Alibaba has launched Qwen4-Max, a flagship model with 2.4 trillion total parameters that activates 71 billion per token, using a hybrid architecture that Alibaba says sharply cuts costs on long contexts."
description: "Alibaba has launched Qwen4-Max, a flagship model with 2.4 trillion total parameters that activates 71 billion per token, using a hybrid architecture that Alibaba says sharply cuts costs on long contexts."
section: "ai-news"
rank: 1
edition: 0
section_rank: 1
score: 9.0
status: "Available"
source_name: "qwen.ai"
source_url: "https://qwen.ai/blog?id=qwen4-max"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50513215"
published_at: "2026-11-16T02:14:44+00:00"
tags: ["Qwen4-Max", "model release", "LLM benchmarks", "reasoning models", "AI industry"]
topics: ["qwen4-max", "model-release", "llm-benchmarks", "reasoning-models", "ai-industry"]
order: "20261116-0-998"
image: "/assets/stories/2026-11-16/alibaba-launches-qwen4-max-flagship-with-2-4t-parameters-8468-share.jpg"
art: "/assets/stories/2026-11-16/alibaba-launches-qwen4-max-flagship-with-2-4t-parameters-8468.jpg"
thumb: "/assets/stories/2026-11-16/alibaba-launches-qwen4-max-flagship-with-2-4t-parameters-8468-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g18c9d70763f0b955152c9690da618c0952099e8b944a25fc788fb821b938302bca34a5fcee05d228e5ec210ffaa37d15d0f4722a4ce3e44c9a71c068033f9315_1280.jpg", "author": "geralt", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/web-network-technology-developer-3963945/", "provider": "Pixabay", "width": 5150, "height": 2716}
---

{% raw %}
<div class="story-lead" markdown="1">

Alibaba has launched Qwen4-Max, a flagship model with 2.4 trillion total parameters that activates 71 billion per token, using a hybrid architecture that Alibaba says sharply cuts costs on long contexts. It lands just behind Kimi K3.1 Pro on the Artificial Analysis Intelligence Index, and Alibaba plans to release smaller Qwen4 models as open source. The supplied material does not give API pricing, context-window size or a date for the open-source releases.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** The supplied report states that Alibaba launched Qwen4-Max with 2.4 trillion total parameters, 71 billion active per token, and a hybrid architecture, and that it ranks just behind Kimi K3.1 Pro on the Artificial Analysis Intelligence Index.
- **Not yet confirmed:** The size of the long-context cost reduction, the model's exact index score, API price and availability terms, and the date, license and parameter sizes of the planned open-source Qwen4 models; the $3.27 average cost cited in discussion rests on one commenter's Artificial Analysis link.

</div>

## Background

Qwen4-Max is a sparse mixture-of-experts model: of its 2.4 trillion total parameters, only 71 billion are active for each token, which is the design choice that keeps per-token compute and cost down. Its predecessor, Qwen3.8 Max, carried the same 2.4 trillion parameter count, so as Wccftech describes it the generational change is architectural — a 3:1 GDN-to-QSA layer stack plus native vision — rather than a jump in raw scale.

## Why it matters

For builders choosing a frontier API, Qwen4-Max adds a 2.4T-parameter option positioned near the top of a third-party intelligence index, but the supplied material does not establish throughput or latency, and only smaller Qwen4 models are slated for open weights. Teams should not assume Qwen4-Max itself can be self-hosted or that its lower advertised cost translates into a lower cost per completed task.

## What to watch

Alibaba has promised smaller open-source Qwen4 models but not dated them; watch for the license, parameter sizes and independent benchmark results.

## Community discussion

Commenters focused on the cost-quality trade-off: one, citing Artificial Analysis, put Qwen4-Max at a score of 43 and average cost of $3.27, against 46 and $0.36 for GPT-6.1 Sol at medium reasoning. Another tester exercised four reasoning settings including a new "none" option, while a builder cited speed as the weakness of the prior Qwen 3.8 model, at about 30 tokens per second versus roughly 80 for Opus.

## Coverage of this story

- 2026-11-16 · qwen.ai: [Qwen4-Max](https://qwen.ai/blog?id=qwen4-max)
- 2026-11-16 · The Decoder: [Alibaba's Qwen4-Max takes on Opus 5.5, GPT-6, and Kimi K3.1 Pro at much lower prices](https://the-decoder.com/alibabas-qwen4-max-takes-on-opus-5-5-gpt-6-and-kimi-k3-1-pro-at-much-lower-prices/)

## Further reading

- [Alibaba's New Qwen 4 - Max Fails To Overtake Moonshot's Kimi...](https://wccftech.com/alibabas-new-qwen4-max-fails-to-overtake-moonshots-kimi-k3-1-pro-retaining-the-same-parameter-count-with-a-lower-price-and-revamped-native-vision-moe-architecture/)

{% endraw %}
