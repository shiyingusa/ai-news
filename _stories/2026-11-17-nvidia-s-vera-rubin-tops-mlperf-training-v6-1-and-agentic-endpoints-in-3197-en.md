---
layout: story
lang: en
date: 2026-11-17 06:00:00 -0500
issue: "2026-11-17"
story_id: "nvidia-s-vera-rubin-tops-mlperf-training-v6-1-and-agentic-endpoints-in-3197"
permalink: "/2026/11/17/nvidia-s-vera-rubin-tops-mlperf-training-v6-1-and-agentic-endpoints-in-3197/"
title: "NVIDIA's Vera Rubin tops MLPerf Training v6.1 and agentic Endpoints in debut"
dek: "NVIDIA says its Vera Rubin platform was the only system with results on every MLPerf Training v6.1 benchmark this round, covering large language models, image generation, recommender systems and reinforcement-learning post-training…"
description: "NVIDIA says its Vera Rubin platform was the only system with results on every MLPerf Training v6.1 benchmark this round, covering large language models, image generation, recommender systems and reinforcement-learning post-training…"
section: "chips-compute"
rank: 3
edition: 0
section_rank: 2
score: 7.0
status: "Demonstrated"
source_name: "NVIDIA Blog"
source_url: "https://blogs.nvidia.com/blog/mlperf-training-endpoints-vera-rubin/"
via: null
discussion_url: null
published_at: "2026-11-16T16:00:25+00:00"
tags: ["MLPerf", "NVIDIA Vera Rubin", "AI accelerators", "benchmarks", "energy efficiency"]
topics: ["mlperf", "nvidia-vera-rubin", "ai-accelerators", "benchmarks", "energy-efficiency"]
order: "20261117-0-996"
image: "/assets/stories/2026-11-17/nvidia-s-vera-rubin-tops-mlperf-training-v6-1-and-agentic-endpoints-in-3197-share.jpg"
art: "/assets/stories/2026-11-17/nvidia-s-vera-rubin-tops-mlperf-training-v6-1-and-agentic-endpoints-in-3197.jpg"
thumb: "/assets/stories/2026-11-17/nvidia-s-vera-rubin-tops-mlperf-training-v6-1-and-agentic-endpoints-in-3197-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/gcee7f81c85195226fd7de93295476cf09ed18615e41e9b430403c3bda724d15e35a749d7cb9a83ca165b81b68016af1ce78dd8a5e7f8c2c3b4ffb58067f75c32_1280.jpg", "author": "bsdrouin", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/network-server-system-2402637/", "provider": "Pixabay", "width": 1920, "height": 1080}
---

{% raw %}
<div class="story-lead" markdown="1">

NVIDIA says its Vera Rubin platform was the only system with results on every MLPerf Training v6.1 benchmark this round, covering large language models, image generation, recommender systems and reinforcement-learning post-training, with Vera Rubin NVL72 delivering up to 2x more performance per GPU than the GB300 NVL72 system. On the DeepSeek-V3 benchmark it scaled from 256 to 1,024 GPUs at about 97% efficiency, cutting training time from 16 minutes to roughly four.

In its first MLPerf Endpoints v1.0 submission, NVIDIA reports a provisional Kimi K3 result in which Vera Rubin NVL72 gives more than 10x the throughput per watt of GB300 NVL72 at a shared minimum of 50 tokens/sec per user. The Training results were released today, but the Endpoints figures are explicitly provisional and pending MLCommons Association verification, and every comparison here comes from NVIDIA's own blog rather than an independent measurement.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** NVIDIA's own post says Vera Rubin NVL72 was the only system with results on every MLPerf Training v6.1 benchmark, that it reached up to 2x performance per GPU over GB300 NVL72, and that on DeepSeek-V3 it scaled from 256 to 1,024 GPUs at about 97% efficiency (16 minutes down to about four); its figure caption lists the raw Endpoints figures — 32 Vera Rubin accelerators at 41,414.2 tokens/sec and 100.89 kW versus 48 GB300 accelerators at 2,210.4 tokens/sec and 60 kW — and notes the GB300 results were verified by MLCommons.
- **Not yet confirmed:** the headline >10x throughput-per-watt gain rests on provisional Vera Rubin Endpoints results that NVIDIA says are pending MLCommons verification and peer review, and on a comparison run at very different concurrency (1,024 versus 48 queries) normalized by NVIDIA's own 50 tokens/sec-per-user floor; pricing, ship dates and independent tests are absent, and the "MLPerf debut" framing conflicts with MLCommons' September 2026 post and The Frontier's report that Vera Rubin already appeared in MLPerf Inference v6.1 as a preview system, at up to 2.5x on DeepSeek-R1 and 3.7x on Qwen3-VL over the prior generation.

</div>

## Background

MLPerf is a peer-reviewed benchmark suite published by MLCommons Association; vendors submit measured results, which are published, and some are verified by MLCommons. MLPerf Training v6.1 measures how fast a system trains models to a target accuracy, while MLPerf Endpoints v1.0 is a newer suite for agentic workflows that checks task completion as well as throughput. NVIDIA's comparison point is GB300 NVL72, its prior rack-scale system.

## Why it matters

Because AI data centers are capped by power, throughput per watt — not raw speed — decides how many agent tasks an operator can serve from a fixed power budget, so NVIDIA is pushing buyers to compare systems on efficiency, not just per-GPU performance. The catch is that the efficiency claim rests on a provisional, unverified result measured under different conditions than the GB300 baseline: Vera Rubin ran 32 accelerators at 100.89 kW with 1,024 queries of concurrency, while GB300 ran 48 accelerators at 60 kW with 48 queries, so anyone evaluating the 10x figure should wait for MLCommons verification rather than treat it as a procurement number.

## What to watch

Watch for MLCommons Association to publish its verification and peer review of the provisional Vera Rubin Endpoints results, which NVIDIA says are subject to change, and for confirmed availability and pricing of Vera Rubin NVL72 systems.

## Further reading

- [Where the Industry Is Investing: A Look at MLPerf ... - MLCommons](https://mlcommons.org/2026/09/chairs-mlperf-inference-v6-1/)
- [Vera Rubin NVL 72 's first MLPerf Inference v 6 . 1 numbers: up to...](https://www.thefrontier.dev/articles/vera-rubin-nvl72-mlperf-v6-1)

{% endraw %}
