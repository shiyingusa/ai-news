---
layout: story
lang: en
date: 2026-11-27 04:00:00 -0500
issue: "2026-11-26"
story_id: "explainer-hbm-memory"
permalink: "/explainers/hbm-high-bandwidth-memory/"
title: "Why AI chips are really memory problems: HBM, explained"
dek: "High-bandwidth memory decides how fast a large language model can answer. Here is what HBM is, why the newest GPUs carry more of it, and why three companies control the supply."
description: "High-bandwidth memory decides how fast a large language model can answer. What HBM is, why new GPUs carry more of it, and who makes it."
section: "tech-blog"
rank: 290
edition: 2
section_rank: 1
score: null
status: "Explainer"
kind: explainer
source_name: "JEDEC"
source_url: "https://www.hpcwire.com/?p=179974"
via: null
discussion_url: null
published_at: null
tags: ["HBM", "Nvidia", "Memory chips", "SK hynix", "Samsung"]
topics: ["hbm", "nvidia", "memory-chips", "sk-hynix", "samsung"]
order: "20261126-2-990"
image: null
art: null
thumb: null
photo_query: ["High Bandwidth Memory", "HBM memory stack", "DRAM wafer"]
photo_credit: null
---

{% raw %}
<div class="story-lead" markdown="1">

When people talk about the AI chip shortage, they usually mean GPUs. But inside every modern AI accelerator sits a second component that is just as scarce and often decides how fast a model can actually run: high-bandwidth memory, or HBM.

This explainer covers what HBM is, why each new GPU generation carries more of it, and why its supply is concentrated in three companies.

</div>

## What HBM is

Ordinary computer memory sits on separate sticks some distance from the processor. HBM takes a different approach: several DRAM chips are stacked vertically, wired together with tiny vertical connections through the silicon, and placed on the same package as the GPU. Nvidia's B200, for example, has its HBM3E stacks on the same physical package as the GPU itself.

The point of the design is width. Each HBM3E stack talks to the processor over a 1,024-bit interface and delivers more than 1.2 terabytes per second. A graphics card's memory bus is a fraction of that width.

## Why AI models need so much of it

Training a model is mostly arithmetic. Answering a question is different. When a large language model generates text, it produces one token at a time, and for each token it has to read a large share of its weights out of memory. That step, known as decode, is usually limited by how fast data can be moved, not by how fast the chip can multiply. Analysts at SemiAnalysis describe these memory-bandwidth-bound regimes as the ones that dominate LLM decode.

That is why memory figures now headline GPU launches. Nvidia's B200 carries 192 GB of HBM3E with 8 TB/s of bandwidth, up from 141 GB and 4.8 TB/s on the H200, according to IEEE Spectrum. More capacity lets a bigger model, or more users' conversations, fit on one chip; more bandwidth lets each answer come back faster.

## What changes with HBM4

The industry standards body JEDEC published the HBM4 specification (JESD270-4) in April 2025. It doubles the interface to 2,048 bits per stack, supports transfer speeds up to 8 Gb/s per pin for up to 2 TB/s per stack, and doubles the number of independent channels from 16 to 32. A 16-high stack built from 32 Gb layers holds 64 GB.

In plain terms: the next generation of accelerators can get more memory bandwidth from the same number of stacks, or the same bandwidth from fewer, which frees space on the package for compute.

## Why supply is tight

Only three companies make HBM at scale: SK hynix, Samsung and Micron. Stacking a dozen or more thin DRAM dies and connecting them is harder than making ordinary memory, and every stack then has to be packaged next to a GPU, which adds another step where capacity can run short.

The balance between the three is shifting. Counterpoint Research put SK hynix's HBM revenue share at 50% in the second quarter of 2026, down from 64% a year earlier, with Samsung at 33% and Micron at 18%. TrendForce reported in June 2026 that Samsung was the first to complete HBM4 validation and begin shipments for Nvidia's Rubin platform, while SK hynix's HBM4 mass production slipped to the third quarter.

## What to watch

Three things will tell you where AI hardware is heading. First, the memory line on each new accelerator's spec sheet: capacity and bandwidth per chip are now as important as compute. Second, which supplier wins each GPU platform, since a single qualification decision can move market share by double digits in a quarter. Third, HBM4 volumes in 2027, which will decide how many next-generation accelerators can actually ship.

## Further reading

- [JEDEC releases HBM4 standard (HPCwire, press release)](https://www.hpcwire.com/?p=179974)
- [JEDEC officially releases HBM4 memory standard (All About Circuits)](https://www.allaboutcircuits.com/news/jedec-officially-releases-hbm4-memory-standard)
- [HBM3e and HBM4 IC design guide (Siemens)](https://blogs.sw.siemens.com/semiconductor-packaging/2026/04/24/hbm3e-hbm4-ic-design-guide/)
- [Nvidia Blackwell (IEEE Spectrum)](https://spectrum.ieee.org/nvidia-blackwell)
- [Blackwell B200 memory and NVLink (Cornell Virtual Workshop)](https://cvw.cac.cornell.edu/gpu-architecture/horizon-gpus-blackwell-b200/b200_mem_nvlink5)
- [NVIDIA B200 (SemiAnalysis InferenceX)](https://inferencex.semianalysis.com/chips/b200)
- [Global DRAM and HBM market share (Counterpoint Research)](https://counterpointresearch.com/insights/global-dram-and-hbm-market-share)
- [HBM Market Bulletin, June 23, 2026 (TrendForce)](https://www.trendforce.com/research/download/RP260623IP3)

{% endraw %}
