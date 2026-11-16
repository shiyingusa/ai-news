---
layout: story
lang: en
date: 2026-11-15 06:00:00 -0500
issue: "2026-11-15"
story_id: "meta-fair-nyu-vision-encoder-pretraining-optional-vision-only-9004"
permalink: "/2026/11/15/meta-fair-nyu-vision-encoder-pretraining-optional-vision-only-9004/"
title: "Meta FAIR/NYU: vision encoder pretraining optional, vision-only parameters required"
dek: "A Meta FAIR and NYU team trained more than 200 multimodal LLMs from scratch on identical data to separate three choices that standard vision encoders bundle: separate pretraining, vision-only parameters, and placement before the LLM."
section: "ai-news"
rank: 4
section_rank: 4
score: 7.0
status: "Demonstrated"
source_name: "Reddit r/MachineLearning"
source_url: "https://www.reddit.com/r/MachineLearning/comments/1xx1k2o/meta_fair_nyu_unbundling_multimodal_vision/"
via: null
discussion_url: null
published_at: "2026-11-15T17:38:16+00:00"
tags: ["multimodal learning", "vision encoders", "MLLMs", "model scaling", "AI research"]
topics: ["multimodal-learning", "vision-encoders", "mllms", "model-scaling", "ai-research"]
order: "20261115-995"
image: "/assets/stories/2026-11-15/meta-fair-nyu-vision-encoder-pretraining-optional-vision-only-9004-share.jpg"
art: "/assets/stories/2026-11-15/meta-fair-nyu-vision-encoder-pretraining-optional-vision-only-9004.jpg"
thumb: "/assets/stories/2026-11-15/meta-fair-nyu-vision-encoder-pretraining-optional-vision-only-9004-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/gec1cbe426358881cda567032e3dbfdca1b4bce08c4d6693fdedb6690799d6432c31b39b50bd7ec93fd527a5285d1f9153158849933b82ee802d4e9aa0edcc77c_1280.jpg", "author": "stevepb", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/dumbbells-shoes-sneakers-2465478/", "provider": "Pixabay", "width": 5472, "height": 3648}
description: "A Meta FAIR and NYU team trained more than 200 multimodal LLMs from scratch on identical data to separate three choices that standard vision encoders bundle: separate pretraining, vision-only parameters, and placement before the LLM."
---

{% raw %}
<div class="story-lead" markdown="1">

A Meta FAIR and NYU team trained more than 200 multimodal LLMs from scratch on identical data to separate three choices that standard vision encoders bundle: separate pretraining, vision-only parameters, and placement before the LLM. In matched-compute comparisons using Qwen3 1.7B and 4B configurations with 0.4B vision parameters, a 0.6B–6.4B scaling ladder, 16 Cambrian VQA benchmarks at 448 px, and 12 language benchmarks, the authors report that separate encoder pretraining is optional: four pretraining objectives (contrastive, self-supervised, and two captioning variants) at best tied a from-scratch encoder, and pretraining MetaCLIP 6.5× longer raised ImageNet linear-probe accuracy from 80.4% to 84.4% without improving VQA. Vision-only parameters were required: encoder-free models trailed at every size and needed about 3× the compute to catch up, while giving the LLM the encoder’s parameters improved text but not VQA. Placement before the LLM was also optional: an “in-fusion” design adding zero-initialized vision-only weights to the first eight layers, unused by text tokens, matched the encoder from 1.7B to 6.4B with about 13% lower time to first token; at 1.7B it reached 45.0 VQA versus 44.4 for the encoder, 42.3 when text shared the branches, and 35.1 when vision branches sat in the last eight layers.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** The poster, /u/trungh98, discloses that he is one of the study's authors and links a paper (alphaxiv 2611.17334), a project blog/FAQ and author X threads; an arXiv cs.CV recent-submissions listing independently shows a paper titled "Unbundling Multimodal Vision Encoding" (tool-2-1). The post itself states the experimental design: 200+ MLLMs trained from scratch on identical data with encoder pretraining charged to the same compute budget, main comparisons at Qwen3-1.7B/4B with 0.4B vision parameters, a 0.6B–6.4B scaling ladder, and evaluation on 16 Cambrian VQA benchmarks at 448 px plus 12 language benchmarks.
- **Not yet confirmed:** Every quantitative result — pretrained encoders only tying from-scratch ones, encoder-free models needing ~3x compute, 45.0 vs 44.4 VQA for in-fusion vs encoder at 1.7B, ~13% lower time to first token, and the 80.4%→84.4% ImageNet gain from 6.5x longer MetaCLIP pretraining — rests solely on the authors' own summary, with no independent replication or peer-review outcome given; the Reddit post is also truncated, so per-benchmark breakdowns and the claimed gaps between Gemma 4 12B, Kimi K3 and Inkling 2 Small cannot be checked from the supplied material.

</div>

## Background

Most multimodal LLMs pair a separately pretrained image encoder—often trained with contrastive image-text objectives—with a language model, so a standard encoder bundles three choices: extra pretraining, parameters reserved for vision tokens, and placement before the LLM. Published models rarely control for data, compute, or encoder pretraining, making architectural differences hard to attribute. Recent models have diverged on this default, with some dropping the encoder and others training it from scratch.

## Why it matters

For teams designing multimodal LLMs under a fixed compute budget, the practical implication is to allocate parameters to vision-specific capacity rather than to a separately pretrained encoder; the authors’ in-fusion variant matched encoder VQA while cutting time to first token by about 13% in their controlled 1.7B–6.4B tests. The caveat is that these are matched-compute experiments with one data pipeline and benchmark set, not production deployments, so teams should re-check the placement and compute trade-off against their own latency and accuracy targets.

## Further reading

- [Computer Vision and Pattern Recognition](https://arxiv.org/list/cs.CV/recent)

{% endraw %}
