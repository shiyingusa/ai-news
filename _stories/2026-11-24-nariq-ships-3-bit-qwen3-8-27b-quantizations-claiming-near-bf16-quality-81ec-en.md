---
layout: story
lang: en
date: 2026-11-24 06:26:21 -0500
issue: "2026-11-24"
story_id: "nariq-ships-3-bit-qwen3-8-27b-quantizations-claiming-near-bf16-quality-81ec"
permalink: "/2026/11/24/nariq-ships-3-bit-qwen3-8-27b-quantizations-claiming-near-bf16-quality-81ec/"
title: "NariQ ships 3-bit Qwen3.8-27B quantizations claiming near-BF16 quality"
dek: "NariQ has published 3-bit, 2.5-bit and 2-bit GGUF quantizations of Qwen3.8-27B, with the 3-bit file roughly 10 GB and the authors claiming near-BF16 quality across agentic, math, multilingual and image tasks."
description: "NariQ has published 3-bit, 2.5-bit and 2-bit GGUF quantizations of Qwen3.8-27B, with the 3-bit file roughly 10 GB and the authors claiming near-BF16 quality across agentic, math, multilingual and image tasks."
section: "ai-news"
rank: 1
edition: 0
section_rank: 1
score: 7.0
status: "Released"
source_name: "Hugging Face"
source_url: "https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50611402"
published_at: "2026-11-23T13:42:38+00:00"
tags: ["quantization", "Qwen3.8-27B", "local LLMs", "llama.cpp", "model compression"]
topics: ["quantization", "qwen3-8-27b", "local-llms", "llama-cpp", "model-compression"]
order: "20261124-0-998"
image: "/assets/stories/2026-11-24/nariq-ships-3-bit-qwen3-8-27b-quantizations-claiming-near-bf16-quality-81ec-share.jpg"
art: "/assets/stories/2026-11-24/nariq-ships-3-bit-qwen3-8-27b-quantizations-claiming-near-bf16-quality-81ec.jpg"
thumb: "/assets/stories/2026-11-24/nariq-ships-3-bit-qwen3-8-27b-quantizations-claiming-near-bf16-quality-81ec-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g8a9f4ad162ab7c11c7f183f127692e5de4dc727dd08643e9dbeb2fdbe9b2d07090fc9200be28ec571c9ce3b04c922e27aedfeda5ab552117e3da99365d4e599a_1280.jpg", "author": "donterase", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/study-workroom-office-glimpse-789631/", "provider": "Pixabay", "width": 4381, "height": 2915}
---

{% raw %}
<div class="story-lead" markdown="1">

NariQ has published 3-bit, 2.5-bit and 2-bit GGUF quantizations of Qwen3.8-27B, with the 3-bit file roughly 10 GB and the authors claiming near-BF16 quality across agentic, math, multilingual and image tasks. In the release's own benchmark table, 3-bit and 2.5-bit match or slightly beat BF16 on DeepSWE (41.0 and 41.9 vs 39.8) and Terminal-Bench 2.1 (63.8 and 60.2 vs 62.6), while the 2-bit version falls to 28.6 on DeepSWE and 86.0 on AIME 25+26 versus 97.7 for BF16.

The authors say this is the first 3-bit-or-lower quantization to retain BF16-level performance on long-horizon agentic tasks, but running it currently requires NariQ's own llama.cpp fork. Decode speed is described as comparable to other quantizations on an RTX PRO 6000; the results are author-reported and have not been independently verified.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** NariQ's model card publishes BF16, 3-bit, 2.5-bit and 2-bit scores for DeepSWE, Terminal-Bench 2.1, AIME 25+26, MSGM and RealWorldQA, and a commit in the same repository describes the DeepSWE figures as three-round averages with per-cell task counts and Docker-based runs (tool-3-1). The card also states that running these files currently requires NariQ's own llama.cpp fork.
- **Not yet confirmed:** All scores are author-reported with no independent replication, and the release does not say what the 4K–64K context-length numbers (88.9 up to 111.7) actually measure, so the claim that decode speed is comparable to other quants rests on the vendor's word; several 3-bit and 2.5-bit results also come out above the BF16 baseline without explanation, and the Terminal-Bench version cited, 2.1, is not the 4.1 release listed on the benchmark's own site (tool-3-3).

</div>

## Background

Quantization stores a model's weights at fewer bits each — here 3, 2.5 and 2 bits per weight instead of 16-bit BF16 — so a 27B-parameter model fits in a roughly 10 GB GGUF file instead of tens of gigabytes, at the risk of losing accuracy. NariQ's files are built for a custom fork of llama.cpp, the open-source inference runtime that loads GGUF models, so standard llama.cpp builds may not run them. The model card dates the v1 release to Nov 20, 2026 and says the 3-bit and 2.5-bit files match BF16 on long-horizon agent tasks, math and image understanding, while the 2-bit file scores lower.

## Why it matters

For people running models locally, the practical change is that a 27B agentic model can fit in about 10 GB of storage, roughly a fifth of the ~54 GB needed at BF16, bringing it within reach of 16 GB machines and single consumer GPUs, though context length and runtime overhead reduce that headroom. The catch is compatibility: users must build and run nari-llama.cpp rather than mainline llama.cpp, and the release's own numbers show the 2-bit variant losing substantial long-horizon agentic and math accuracy, so the 3-bit file is the one to test first.

## What to watch

The next checkable step is independent benchmarking on consumer hardware and whether the required nari-llama.cpp changes land in upstream llama.cpp; until then, the fork requirement is the main barrier to ordinary use.

## Further reading

- [nari-labs/Qwen3.8-27B-NariQ-GGUF · Hugging Face](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF)
- [NariQ Quantization: Qwen3.8-27B Agents in a 10 GB File](https://aitecharchive.com/articles/nariq-quantization-qwen3-8-27b-agent-performance-10gb)
- [Report three-round DeepSWE averages...](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF/commit/9065513f08d8ed7dbe50b9c329cac1f40c70fde9)
- [TERMINAL - BENCH](https://www.tbench.ai/)

<div class="community" markdown="1">

## Community discussion: opinion, not evidence

Commenters disagree on whether the near-BF16 results reflect the quantization or the evaluation harness: rao-v said the release does the basic checks they want, including multiple long-horizon task types and held-out evaluations, while WithinReason argued from the plots that most gains come from a harness difference rather than the model. A user also reported about 3.8 tok/s decode on an 18 GB M3 Pro with the 3.0-bit file, and others asked what information is lost and how it compares with Bonsai 2 27B.

</div>

{% endraw %}
