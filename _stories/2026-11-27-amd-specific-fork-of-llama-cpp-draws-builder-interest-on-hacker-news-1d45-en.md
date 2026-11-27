---
layout: story
lang: en
date: 2026-11-27 06:24:56 -0500
issue: "2026-11-27"
story_id: "amd-specific-fork-of-llama-cpp-draws-builder-interest-on-hacker-news-1d45"
permalink: "/2026/11/27/amd-specific-fork-of-llama-cpp-draws-builder-interest-on-hacker-news-1d45/"
title: "AMD-specific fork of llama.cpp draws builder interest on Hacker News"
dek: "An AMD-targeted fork of llama.cpp has been published and shared on Hacker News, pitched at improving local LLM inference on AMD GPUs."
description: "An AMD-targeted fork of llama.cpp has been published and shared on Hacker News, pitched at improving local LLM inference on AMD GPUs."
section: "ai-news"
rank: 1
edition: 0
section_rank: 1
score: 7.0
status: "Released"
source_name: "devnull.land"
source_url: "https://devnull.land/amd-specific-llama-cpp"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50657265"
published_at: "2026-11-26T17:11:29+00:00"
tags: ["llama.cpp", "AMD", "LLM inference", "open-source", "GPU optimization"]
topics: ["llama-cpp", "amd", "llm-inference", "open-source", "gpu-optimization"]
order: "20261127-0-998"
image: "/assets/stories/2026-11-27/amd-specific-fork-of-llama-cpp-draws-builder-interest-on-hacker-news-1d45-share.jpg"
art: "/assets/stories/2026-11-27/amd-specific-fork-of-llama-cpp-draws-builder-interest-on-hacker-news-1d45.jpg"
thumb: "/assets/stories/2026-11-27/amd-specific-fork-of-llama-cpp-draws-builder-interest-on-hacker-news-1d45-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g9fdc9899e1bfbfaa1d0ce69d3f7a35eb159302a28b71de1b8ccc6449f71029ed819aa3d2ac28cc2055627c5bc37d221614bd32f63f6597cacdcbaf7092f59143_1280.jpg", "author": "blickpixel", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/it-server-server-cabinet-network-838379/", "provider": "Pixabay", "width": 3095, "height": 2063}
---

{% raw %}
<div class="story-lead" markdown="1">

An AMD-targeted fork of llama.cpp has been published and shared on Hacker News, pitched at improving local LLM inference on AMD GPUs. The material available does not include the fork's own benchmarks, the specific AMD GPU generations or ROCm versions it supports, or whether its changes have been proposed upstream to mainline llama.cpp.

The discussion around it is substantive rather than incidental: commenters describe a longer-running, informal effort to tune llama.cpp for AMD hardware, including used gfx906 datacenter cards from around 2018 that pair 32GB of HBM2 memory with roughly 1 TB/s of bandwidth for a few hundred dollars.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** The report is a Hacker News submission dated 26 November 2026 titled "AMD-specific fork of llama.cpp", linking to devnull.land/amd-specific-llama-cpp, and it is presented as an AMD-targeted fork of llama.cpp; the submission itself carries no README, benchmark, version or license text in what was supplied. The comments describe other people's separate AMD-focused forks and tuning work (gfx906 cards, an MI100 ROCm kernel port, an R9700 setup), not the contents of this fork.
- **Not yet confirmed:** What this fork changes relative to upstream llama.cpp, which AMD architectures it targets, any measured speedup, its license, and whether it is installable today. The performance figures in the comments — 2400 tok/s prefill and 150 tok/s decode on an R9700, "1 TB/s" HBM2 datacenter cards for $200, tripled Qwen 3.8 speeds on an M1 port — are commenters' own claims about their own setups and were not independently checked.

</div>

## Background

llama.cpp is an open-source inference engine for running quantized large language models locally on consumer hardware; its default build paths and kernel tuning have historically centered on Nvidia's CUDA, so AMD users depend on the ROCm/HIP backend and on community forks that add hand-tuned kernels for specific card families. The fork discussed here, llama-cpp-rdna-boosts, is one of those projects: its author reports raising token generation from 35 to 55 tokens per second and prefill from 700 to 1,300 tokens per second on his own AMD setup, with results varying by hardware. Commenters in the Hacker News thread said AMD-optimized forks generally outperform vanilla llama.cpp and asked for a branch switchable by environment variable rather than a separate fork pinned to a commit.

## Why it matters

For developers running models locally on AMD GPUs, this is another implementation to weigh against mainline llama.cpp and other ROCm-oriented forks. Because it is a fork rather than an upstream change, anyone adopting it should first confirm which GPU generations and ROCm builds it targets and how closely it tracks upstream commits, since diverging from mainline means carrying patch maintenance themselves.

## Further reading

- [AMD-specific fork of llama.cpp | devnull.land](https://devnull.land/amd-specific-llama-cpp)
- [AMD - specific fork of llama . cpp | Hacker News](https://news.ycombinator.com/item?id=50657265)

<div class="community" markdown="1">

## Community discussion: opinion, not evidence

Commenter rao-v traces the interest to early 2025, when builders noticed that AMD's circa-2018 gfx906 datacenter cards offered large HBM2 memory and very high bandwidth cheaply, and points to their own repository optimizing llama.cpp for those cards, which lack tensor cores and native bf16 support. fiddlerwoaroof reports using Claude to port Nvidia kernels to ROCm on an MI100 and claims a two-to-three-fold speedup on a Qwen model, saying it has been stable and that the ported kernels were validated; these are individual reports, not independent benchmarks of the fork itself.

</div>

{% endraw %}
