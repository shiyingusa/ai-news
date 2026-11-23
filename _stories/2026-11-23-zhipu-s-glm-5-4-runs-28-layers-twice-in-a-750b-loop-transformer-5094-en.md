---
layout: story
lang: en
date: 2026-11-23 13:26:48 -0500
issue: "2026-11-23"
story_id: "zhipu-s-glm-5-4-runs-28-layers-twice-in-a-750b-loop-transformer-5094"
permalink: "/2026/11/23/zhipu-s-glm-5-4-runs-28-layers-twice-in-a-750b-loop-transformer-5094/"
title: "Zhipu's GLM-5.4 runs 28 layers twice in a 750B 'Loop Transformer'"
dek: "Z.ai has published the release note for GLM-5.4, a 750-billion-parameter flagship model built on what the company calls its first \"Loop Transformer\": 28 of its layers are computed twice per token instead of once."
description: "Z.ai has published the release note for GLM-5.4, a 750-billion-parameter flagship model built on what the company calls its first \"Loop Transformer\": 28 of its layers are computed twice per token instead of once."
section: "ai-news"
rank: 1
edition: 0
section_rank: 1
score: 8.0
status: "Released"
source_name: "z.ai"
source_url: "https://z.ai/blog/glm-5.4"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50609685"
published_at: "2026-11-23T10:06:43+00:00"
tags: ["model release", "loop transformers", "Zhipu GLM", "LLM architecture", "inference efficiency"]
topics: ["model-release", "loop-transformers", "zhipu-glm", "llm-architecture", "inference-efficiency"]
order: "20261123-0-998"
image: "/assets/stories/2026-11-23/zhipu-s-glm-5-4-runs-28-layers-twice-in-a-750b-loop-transformer-5094-share.jpg"
art: "/assets/stories/2026-11-23/zhipu-s-glm-5-4-runs-28-layers-twice-in-a-750b-loop-transformer-5094.jpg"
thumb: "/assets/stories/2026-11-23/zhipu-s-glm-5-4-runs-28-layers-twice-in-a-750b-loop-transformer-5094-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g8c2fc366df9e988ccc1f93bd569de4063eaef9871e390d2f155d7b5fadc641478f74c6f520c73e6a3dfca217f77b1a866511c4eb95666f61c3b69ffb402e3f8b_1280.jpg", "author": "Akela999", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/data-center-engine-room-2476790/", "provider": "Pixabay", "width": 4096, "height": 2160}
---

{% raw %}
<div class="story-lead" markdown="1">

Z.ai has published the release note for GLM-5.4, a 750-billion-parameter flagship model built on what the company calls its first "Loop Transformer": 28 of its layers are computed twice per token instead of once. Z.ai says this lets the model match systems with 2 to 3 trillion parameters, but the only benchmark scores released so far come from a smaller 30B test model, not the full flagship. The company is framing GLM-5.4 as the start of "Generalized Coding," in which code generation also produces videos, games, and CAD models. Access is currently gated: commenters report the model is not on OpenRouter or the standard Z.ai API plan, and requires Z.ai's Coding Plan, whose API keys otherwise behave like regular ones.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** Z.ai's release note states that GLM-5.4 is a 750B-parameter model in which 28 layers run twice, that the company positions it as its first Loop Transformer, and that published benchmark scores so far cover only a 30B test model.
- **Not yet confirmed:** the claim that the model matches 2–3-trillion-parameter systems rests on Z.ai's own word with no published full-scale benchmarks or independent evaluation, and the Coding Plan–only availability comes from a user report rather than a documented Z.ai statement.

</div>

## Background

Loop transformers address inference's main physical bottleneck: to generate each token, a conventional model must stream every layer's weights from high-bandwidth memory (HBM) into the compute chip, run that layer once, then swap in the next — so memory bandwidth, not arithmetic, sets the pace. Reusing the same weights for a second pass through a block of layers amortizes that weight movement and trades spare compute for reduced memory traffic. Z.ai is not first to the idea — The Decoder notes the company is following OpenAI into loop transformer territory — but GLM-5.4 is where it becomes the architecture of Zhipu's 750-billion-parameter flagship rather than an experiment.

## Why it matters

Developers who want to try GLM-5.4 today have to subscribe to Z.ai's Coding Plan rather than use a standard API key or OpenRouter, which changes how teams would integrate or price it. The architecture itself targets the memory-bandwidth cost of inference: reusing each layer twice means fewer weight transfers per token, a lever that matters most for large models where moving weights on and off the chip dominates cost.

## What to watch

Watch for benchmark results for the full 750B model rather than the 30B test model, along with independent evaluations, and for GLM-5.4 to appear on the standard Z.ai API or OpenRouter.

## Community discussion

Hacker News commenters welcomed the technical detail Zhipu published, with one calling it a refreshing contrast to the disclosure typical of Western labs, and another explaining loop transformers as a fix for the memory-bandwidth bottleneck of moving each layer on and off the chip. Simon Willison reported that access required switching to the Coding Plan and that GLM-5.4's generated "pelican" images look very different from GLM-5.2's gradient-and-animation-heavy defaults, while another commenter argued that Chinese models' long "marathon thinking" sessions make them slow on simple tasks.

## Coverage of this story

- 2026-11-23 · z.ai: [GLM-5.4: Toward Generalized Coding with Our First Loop Transformer](https://z.ai/blog/glm-5.4)
- 2026-11-23 · The Decoder: [Z.ai follows OpenAI into loop transformer territory with its new 750B flagship model](https://the-decoder.com/z-ai-follows-openai-into-loop-transformer-territory-with-its-new-750b-flagship-model/)

{% endraw %}
