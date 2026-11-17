---
layout: story
lang: en
date: 2026-11-17 06:00:00 -0500
issue: "2026-11-17"
story_id: "bfl-s-case-for-visual-intelligence-and-multimodal-training-86b9"
permalink: "/2026/11/17/bfl-s-case-for-visual-intelligence-and-multimodal-training-86b9/"
title: "BFL's Case for Visual Intelligence and Multimodal Training"
dek: "A concise Latent Space episode recap that captures BFL's arguments for multimodal visual intelligence and a few practical engineering lessons, but without enough technical depth or evidence to be more than a useful niche overview."
description: "A concise Latent Space episode recap that captures BFL's arguments for multimodal visual intelligence and a few practical engineering lessons, but without enough technical depth or evidence to be more than a useful niche overview."
section: "tech-blog"
rank: 18
edition: 0
section_rank: 2
score: 6.0
status: null
source_name: "Latent Space"
source_url: "https://latent.space/p/bfl/"
via: null
discussion_url: null
published_at: "2026-11-16T21:38:03+00:00"
tags: ["video generation", "multimodal training", "temporal consistency", "latent diffusion", "model training strategy"]
topics: ["video-generation", "multimodal-training", "temporal-consistency", "latent-diffusion", "model-training-strategy"]
order: "20261117-0-981"
image: "/assets/stories/2026-11-17/bfl-s-case-for-visual-intelligence-and-multimodal-training-86b9-share.jpg"
art: "/assets/stories/2026-11-17/bfl-s-case-for-visual-intelligence-and-multimodal-training-86b9.jpg"
thumb: "/assets/stories/2026-11-17/bfl-s-case-for-visual-intelligence-and-multimodal-training-86b9-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g55ebfdeab599ea1620a492333c4fb1604180b82794ba6495e4dd9ea679466f37c4d45a14402eeba7d4205a13ce60c1deddb0053b01f98a821e1b127a0f87195a_1280.jpg", "author": "cookieone", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/internet-information-service-system-8097838/", "provider": "Pixabay", "width": 6000, "height": 4000}
---

{% raw %}
<div class="story-lead" markdown="1">

A concise Latent Space episode recap that captures BFL's arguments for multimodal visual intelligence and a few practical engineering lessons, but without enough technical depth or evidence to be more than a useful niche overview.

</div>

## Background

Black Forest Labs, formed by key figures behind Stable Diffusion and SDXL, is moving beyond still-image generation into video and world models. Andreas Blattmann and Dustin Podell explain the technical case for that shift.

## Solution

Their central argument is that visual intelligence requires learning from stills, video, and audio together, as BFL does in FLUX 3: a still shows where a ball is, video shows how it got there, and impact sound supplies timing even when the camera misses contact. Blattmann uses the example of catching a ball—your hand moves before you can consciously calculate the trajectory—to describe tacit physical knowledge, though the episode does not settle whether models truly understand physics. A moving camera offers a stronger test than a single convincing frame, because the model must render occluded views such as the back of a person's head. An engineering example makes temporal consistency concrete: independently upscaling each frame can produce shimmer when the upscaler makes slightly different choices, so BFL derives its video upscaler from the same FLUX 3 backbone. On compute strategy, Podell and Blattmann weigh autoregression, which can learn from all tokens at once, against diffusion's ability to distill long sampling into few steps—the better tradeoff depends on whether cost lies in training or waiting for output. A small Kontext prototype that learned to place a logo on a shirt in a few hours justified months of data and model work.

## Takeaway

BFL treats video and audio not as separate product lines but as additional evidence for the same visual model, while practical gains depend on consistency across frames and disciplined prototyping before large training investments.

{% endraw %}
