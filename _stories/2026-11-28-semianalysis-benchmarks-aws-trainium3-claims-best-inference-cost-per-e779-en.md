---
layout: story
lang: en
date: 2026-11-28 06:26:13 -0500
issue: "2026-11-28"
story_id: "semianalysis-benchmarks-aws-trainium3-claims-best-inference-cost-per-e779"
permalink: "/2026/11/28/semianalysis-benchmarks-aws-trainium3-claims-best-inference-cost-per-e779/"
title: "SemiAnalysis benchmarks AWS Trainium3, claims best inference cost-per-token after Nvidia Vera Rubin"
dek: "SemiAnalysis published a microarchitecture deep dive on AWS's Trainium3 accelerator, placing it on its InferenceX leaderboard alongside Google TPUv7, OpenAI's Jalapeño, AMD parts and Nvidia's GB300 and Rubin NVL72."
description: "SemiAnalysis published a microarchitecture deep dive on AWS's Trainium3 accelerator, placing it on its InferenceX leaderboard alongside Google TPUv7, OpenAI's Jalapeño, AMD parts and Nvidia's GB300 and Rubin NVL72."
section: "chips-compute"
rank: 7
edition: 0
section_rank: 3
score: 7.0
status: "Released"
source_name: "SemiAnalysis"
source_url: "https://newsletter.semianalysis.com/p/trainium3-inferencex"
via: null
discussion_url: null
published_at: "2026-11-27T15:54:59+00:00"
tags: ["AWS Trainium", "AI accelerators", "inference", "microarchitecture", "semiconductor supply chain"]
topics: ["aws-trainium", "ai-accelerators", "inference", "microarchitecture", "semiconductor-supply-chain"]
order: "20261128-0-992"
image: "/assets/stories/2026-11-28/semianalysis-benchmarks-aws-trainium3-claims-best-inference-cost-per-e779-share.jpg"
art: "/assets/stories/2026-11-28/semianalysis-benchmarks-aws-trainium3-claims-best-inference-cost-per-e779.jpg"
thumb: "/assets/stories/2026-11-28/semianalysis-benchmarks-aws-trainium3-claims-best-inference-cost-per-e779-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g169443d4ecd6ac40ec324e5398b423d4ab318366c632c673aa33d6bb5f95ecd83d78ae393a8d76094c240b887973d822a26e0f6a07f285b5f21d6963efd32876_1280.jpg", "author": "blickpixel", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/it-server-server-cabinet-network-838379/", "provider": "Pixabay", "width": 3095, "height": 2063}
---

{% raw %}
<div class="story-lead" markdown="1">

SemiAnalysis published a microarchitecture deep dive on AWS's Trainium3 accelerator, placing it on its InferenceX leaderboard alongside Google TPUv7, OpenAI's Jalapeño, AMD parts and Nvidia's GB300 and Rubin NVL72. The firm says Trainium3 running vLLM with PDS sits on a better throughput-per-TCO (total cost of ownership) frontier than every listed accelerator except Nvidia's Vera Rubin across the curve of cost versus p90 interactivity, and that it trades blows with or beats GB300 on cost to generate tokens.

SemiAnalysis attributes part of the gain to design choices rather than Amazon's supply chain alone: its Trainium Descriptor Generation Engines (DGE), the counterpart of Nvidia's TMA tile-movement unit, let the chip hit peak HBM bandwidth utilization at small message sizes, which the firm says is not possible on Nvidia GPUs. The results come from SemiAnalysis's own UBenchX microbenchmarks and an AgentX test that replays real coding-agent sessions against a Trainium3 server, with AWS Annapurna Labs engineers helping validate the experiments; the excerpt published no absolute throughput, price or instance-availability figures.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** SemiAnalysis measured Trainium3 on its InferenceX and UBenchX suites, ran an end-to-end agentic coding workload against a Trainium3 server, and says AWS Annapurna Labs co-founder Nafea Bshara and Trainium chief architect Ron Diamant helped validate the experiments.
- **Not yet confirmed:** the specific claims that Trainium3 beats or matches Nvidia GB300 on cost per token and reaches peak HBM bandwidth utilization at small message sizes rest on SemiAnalysis's own benchmarks and charts, and the report gives no absolute performance numbers, instance pricing, general-availability date or independent replication.

</div>

## Background

Trainium is AWS's in-house AI accelerator family, designed by Annapurna Labs; AWS says Trainium3 has eight large cores, each with Tensor, Vector, Scalar and GPSIMD engines, and up to twice the MXFP8 compute throughput of Trainium2. Nvidia's data-center GPUs began as graphics processors and have added AI-specific hardware generation by generation—Tensor Cores in Volta, TMA for tile data movement in Hopper—whereas Trainium was designed from the ground up for machine learning with tiles as a first-class primitive, a contrast that shapes how inference workloads map onto the chip.

## Why it matters

For teams choosing inference hardware, the practical claim is that Trainium3's cost advantage depends on a specific software path — vLLM with PDS on Neuron — so a real migration means validating that stack against the framework and kernels a team already runs, not just comparing chip specifications; the headline numbers also come from the benchmark vendor whose suite is being cited, and the underlying data lives in charts the report does not reproduce.

## What to watch

Watch for AWS to publish Trainium3 instance pricing and general-availability terms, and for third parties to reproduce the cost-per-token results on InferenceX rather than relying on the benchmark author's own run.

## Further reading

- [AI Accelerator - AWS Trainium - AWS](https://aws.amazon.com/ai/machine-learning/trainium/)

{% endraw %}
