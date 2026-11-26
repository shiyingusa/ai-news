---
layout: story
lang: en
date: 2026-11-26 06:27:09 -0500
issue: "2026-11-26"
story_id: "sand-ai-plans-to-open-source-480b-magi-2-video-model-with-0-5-s-api-9fa3"
permalink: "/2026/11/26/sand-ai-plans-to-open-source-480b-magi-2-video-model-with-0-5-s-api-9fa3/"
title: "Sand.ai plans to open-source 480B MAGI-2 video model with ¥0.5/s API pricing"
dek: "On November 25, Sand.ai said it plans to release the full weights of MAGI-2, a unified audio-video generation model with 480B total parameters, \"as soon as possible\" — no release date, license or download terms were given."
description: "On November 25, Sand.ai said it plans to release the full weights of MAGI-2, a unified audio-video generation model with 480B total parameters, \"as soon as possible\" — no release date, license or download terms were given."
section: "ai-news"
rank: 4
edition: 0
section_rank: 4
score: 7.0
status: "Announced"
source_name: "GeekPark (极客公园)"
source_url: "http://www.geekpark.net/news/374532"
via: null
discussion_url: null
published_at: "2026-11-26T08:38:54+00:00"
tags: ["视频生成", "开源模型", "MAGI-2", "Sand.ai", "API 定价"]
topics: ["magi-2", "sand-ai", "api"]
order: "20261126-0-995"
image: "/assets/stories/2026-11-26/sand-ai-plans-to-open-source-480b-magi-2-video-model-with-0-5-s-api-9fa3-share.jpg"
art: "/assets/stories/2026-11-26/sand-ai-plans-to-open-source-480b-magi-2-video-model-with-0-5-s-api-9fa3.jpg"
thumb: "/assets/stories/2026-11-26/sand-ai-plans-to-open-source-480b-magi-2-video-model-with-0-5-s-api-9fa3-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g16cabe354a0f9774970e3d066f56c6bdc0bfecccd4f41016e31a700b0b5d61a4447b9f4f87533dfe28765fac4c44ea83df9e38f9668b7d026db1d2e41f9dca76_1280.jpg", "author": "Elchinator", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/source-code-software-computer-4280758/", "provider": "Pixabay", "width": 3000, "height": 2000}
---

{% raw %}
<div class="story-lead" markdown="1">

On November 25, Sand.ai said it plans to release the full weights of MAGI-2, a unified audio-video generation model with 480B total parameters, "as soon as possible" — no release date, license or download terms were given. The company's published API list price for 1080P output is ¥0.5 per second, which GeekPark reports is less than one tenth of Seedance 2.5 at the same specification; local deployment would remove vendor markup entirely. MAGI-2 uses a mixture-of-experts architecture that activates roughly 28B parameters per inference, natively generates picture and sound together (dialogue with lip sync, foley, ambience, music), supports six aspect ratios, up to 30 seconds of 1080p at 25 fps, and up to 20 mixed reference assets (10 images, 5 videos, 5 audio), and Sand.ai says it has been adapted to run on Hygon and Moore Threads chips. Sand.ai also claims MAGI-2 already ranks first worldwide on Artificial Analysis's image-to-video-with-audio leaderboard, ahead of Seedance 2.5 — a vendor claim GeekPark repeats without independent verification.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** Sand.ai announced on November 25 that it intends to open-source the full weights of MAGI-2, described as a 480B-parameter mixture-of-experts audio-video model activating about 28B parameters per inference, with a 1080P API list price of ¥0.5 per second and existing adaptations for Hygon and Moore Threads chips, GeekPark reported.
- **Not yet confirmed:** that MAGI-2 actually tops Artificial Analysis's image-to-video-with-audio ranking and beats Seedance 2.5 — that comparison, the "under one tenth" cost gap (which depends on Seedance 2.5's own unstated list price), the liblib blind-test result, and the 30-second/20-asset capabilities all rest on Sand.ai's account; the weights have not been published, and no release date, license or independent benchmark has been provided.

</div>

## Background

Sand.ai released a smaller open model, MAGI-2 Preview, in August 2026 with 114B parameters and 10-second clips, and its own announcement says the open-source release and a technical report for the 480B flagship will follow. That flagship is being positioned against Seedance 2.5, the closed model the article describes as the industry's de facto benchmark — Kling 3.0, Wan 3.0 and MiniMax's H3 all publish comparisons against it.

## Why it matters

If the weights ship, video teams get a downloadable SOTA-class model instead of paying per call: GeekPark calculates that at ¥0.5/s, a usable one-second shot costs ¥1.5–2.5 after three to five retries, versus ¥12–20 for closed-source models at ¥4/s list price — roughly eight to ten times more creative iterations on the same budget. The practical caveat is hardware: a 480B MoE model still needs serious GPU capacity and ops skill to self-host, so local deployment mainly suits teams that already have compute, and the API list price is not yet shown to be an available, generally purchasable service.

## What to watch

Watch for Sand.ai to actually publish the MAGI-2 weights along with the license terms, since those determine whether commercial self-hosting is permitted. Independent leaderboard movement on Artificial Analysis's image-to-video-with-audio ranking would also test the claim that it outranks Seedance 2.5.

## Further reading

- [MAGI - 2 : A 480 B Frontier Video Generation Model](https://sand.ai/blog/magi-2/)
- [MAGI - 2 AI Video Generator: 30s 1080p with Sound | YouArt](https://youart.ai/model/magi-2)

{% endraw %}
