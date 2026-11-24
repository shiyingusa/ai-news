---
layout: story
lang: en
date: 2026-11-24 18:23:48 -0500
issue: "2026-11-24"
story_id: "prismml-s-ternary-bonsai-2-5-27b-runs-locally-at-2230-tokens-s-users-ca7e"
permalink: "/2026/11/24/prismml-s-ternary-bonsai-2-5-27b-runs-locally-at-2230-tokens-s-users-ca7e/"
title: "PrismML's Ternary Bonsai 2.5 27B runs locally at ~22–30 tokens/s, users report"
dek: "PrismML's Ternary Bonsai 2.5 27B — a 27-billion-parameter model with ternary-quantized weights, meaning most values are compressed to -1, 0 or +1…"
description: "PrismML's Ternary Bonsai 2.5 27B — a 27-billion-parameter model with ternary-quantized weights, meaning most values are compressed to -1, 0 or +1…"
section: "ai-news"
rank: 202
edition: 2
section_rank: 2
score: 7.0
status: "Released"
source_name: "prismml.com"
source_url: "https://prismml.com/news/bonsai-2-5-27b"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50633922"
published_at: "2026-11-24T20:08:03+00:00"
tags: ["ternary quantization", "model release", "local LLM inference", "AI community discussion"]
topics: ["ternary-quantization", "model-release", "local-llm-inference", "ai-community-discussion"]
order: "20261124-2-997"
image: "/assets/stories/2026-11-24/prismml-s-ternary-bonsai-2-5-27b-runs-locally-at-2230-tokens-s-users-ca7e-share.jpg"
art: "/assets/stories/2026-11-24/prismml-s-ternary-bonsai-2-5-27b-runs-locally-at-2230-tokens-s-users-ca7e.jpg"
thumb: "/assets/stories/2026-11-24/prismml-s-ternary-bonsai-2-5-27b-runs-locally-at-2230-tokens-s-users-ca7e-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g16368496c2918f02134f91a1946178d3b1339400054a124e64ab3c7df27e5a8f5d954303f03fcdefedab336fb0dbf4b8d46e251745b9017535151fe9a7607927_1280.jpg", "author": "blickpixel", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/it-server-server-cabinet-network-838379/", "provider": "Pixabay", "width": 3095, "height": 2063}
---

{% raw %}
<div class="story-lead" markdown="1">

PrismML's Ternary Bonsai 2.5 27B — a 27-billion-parameter model with ternary-quantized weights, meaning most values are compressed to -1, 0 or +1 — is being run locally by Hacker News users, who report roughly 22–30 tokens/s generation and enough memory headroom for 128k context on a 24GB Apple Silicon Mac using a Q2 GGUF build (a heavily compressed file format for local runners such as llama.cpp). One commenter says agentic tool calls have been "solid" and rates it above a Q4 build of a smaller model, while another claims it matches Opus 4.6 on SWE-bench Verified, a software-engineering benchmark. Those benchmark claims and the model's evaluation methodology are not backed by any primary source here: the release page provided no specification, licence, pricing or independent test results.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** PrismML's site carries a release post titled "Ternary Bonsai 2.5 27B," and commenters say they have actually run the weights locally — one reports 22.3 tokens/s generation and 222.9 tokens/s prompt processing on a Mac Mini M5 Pro (24GB RAM) using a Q2 GGUF, with a 128k context fitting in memory. Third-party comparison pages list an earlier "Ternary Bonsai 2 27B" with a mathematics category score of 45.5/100, ranking it #73 of 125 models in that category.
- **Not yet confirmed:** The post's own text was not available to this briefing, so parameter count claims, license, file sizes, pricing, and download links rest on the title and commenters rather than a primary technical document. The headline performance claims come from Hacker News anecdotes with no posted methodology — the asserted SWE-bench Verified parity with Opus 4.6 (a commenter's own hedge: "unless I'm totally mistaken") and the reported ~30 tokens/s via Unsloth Studio have not been independently measured, and no one has shown whether ternary weights get hardware acceleration outside FPGAs. The sources also conflict on naming and deployment: commenters discuss "2.5" as a local GGUF, while the aggregator pages describe a "2" model as a hosted production API model dated September 2026 — the briefing cannot reconcile whether these are the same lineage.

</div>

## Background

Ternary quantization stores each model weight at one of three levels (roughly −1, 0 and +1) instead of a 16-bit floating-point number, which shrinks the memory a model needs and lets larger models run on consumer hardware. PrismML's earlier Bonsai 2 27B used this approach to fit into 8.60 GB in total — a 7.67 GB ternary language model plus a 0.92 GB FP16 vision tower carried over unmodified from Qwen3.8-27B. The 2.5 release is positioned as keeping the same 5.9 GB footprint while improving agentic coding, multi-turn tool use and multi-step task execution.

## Why it matters

If the reported numbers hold, a 27B model that fits comfortably in 24GB of unified memory with 128k context puts agentic coding workloads on a single desktop machine rather than a server — but because the SWE-bench parity claim comes from a commenter rather than PrismML or an independent evaluator, teams should benchmark it on their own tasks and confirm their runner supports the Q2 GGUF format before relying on it.

## What to watch

Watch for independent SWE-bench Verified runs and head-to-head tests against comparably small Qwen models, and for any PrismML documentation of hardware acceleration for ternary weights beyond FPGAs.

## Community discussion

Commenters report ~22–25 tokens/s on a Mac Mini M5 Pro with 24GB RAM (222.9 tok/s prompt processing, 2.12s to first token) and ~30 tokens/s generation through Unsloth Studio on a MacBook, with one saying the agentic calls beat a Q4 build of a smaller model. Others push back on the benchmark framing: one asks whether the SWE-bench result reflects real capability, benchmark drift or tuning to the test, another wants direct comparisons with equivalently sized models, and a third asks whether ternary weights have any hardware acceleration outside FPGAs.

## Further reading

- [PrismML — Introducing Ternary Bonsai 2 . 5 27 B : Powering Agentic...](https://prismml.com/news/bonsai-2-5-27b)
- [Ternary - Bonsai - 2 - 27 B : A 27 B Model That Fits in 8.6GB | MindStudio](https://www.mindstudio.ai/blog/ternary-bonsai-2-27b-ternary-quantization)
- [Claude Opus 4.6 vs Ternary Bonsai 2 27B: Benchmarks & Cost](https://benchlm.ai/compare/claude-opus-4-6-vs-ternary-bonsai-2-27b)
- [Ternary Bonsai 2 27B Benchmarks & Context (November 2026)](https://benchlm.ai/models/ternary-bonsai-2-27b)
- [Claude Opus 4.6 vs Ternary Bonsai 2 27B - anotherwrapper.com](https://anotherwrapper.com/tools/llm-pricing/claude-opus-4-6/ternary-bonsai-2-27b)

{% endraw %}
