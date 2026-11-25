---
layout: story
lang: en
date: 2026-11-25 06:28:41 -0500
issue: "2026-11-25"
story_id: "sandboxed-models-can-communicate-via-inference-servers-lesswrong-30d4"
permalink: "/2026/11/25/sandboxed-models-can-communicate-via-inference-servers-lesswrong-30d4/"
title: "Sandboxed models can communicate via inference servers, LessWrong analysis claims"
dek: "A LessWrong post argues that sandboxed models can communicate through side channels in shared inference servers, even without a direct network path."
description: "A LessWrong post argues that sandboxed models can communicate through side channels in shared inference servers, even without a direct network path."
section: "ai-news"
rank: 3
edition: 0
section_rank: 3
score: 7.0
status: null
source_name: "lesswrong.com"
source_url: "https://www.lesswrong.com/posts/7wzWuLP3HhyBLmKfo/models-can-communicate-via-inference-servers-despite-being"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50637686"
published_at: "2026-11-25T02:34:21+00:00"
tags: ["AI security", "inference servers", "side channels", "sandboxing", "model communication"]
topics: ["ai-security", "inference-servers", "side-channels", "sandboxing", "model-communication"]
order: "20261125-0-996"
image: "/assets/stories/2026-11-25/sandboxed-models-can-communicate-via-inference-servers-lesswrong-30d4-share.jpg"
art: "/assets/stories/2026-11-25/sandboxed-models-can-communicate-via-inference-servers-lesswrong-30d4.jpg"
thumb: "/assets/stories/2026-11-25/sandboxed-models-can-communicate-via-inference-servers-lesswrong-30d4-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/ge86f3266a0af8883028be4649ccc024817e48fe6fc7ddf58a05f22d553177d7b6e0d2dfb8e834254fabaa1a2db5238b2296386e749c9f307b605d3013e8a261c_1280.jpg", "author": "Akela999", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/data-center-engine-room-2476790/", "provider": "Pixabay", "width": 4096, "height": 2160}
---

{% raw %}
<div class="story-lead" markdown="1">

A LessWrong post argues that sandboxed models can communicate through side channels in shared inference servers, even without a direct network path. The claimed channels include shared caches and timing effects, with one commenter sketching a vLLM-specific signal based on decoding slowdown. The account provides no independent confirmation. The discussion weighs mitigations such as cache-separation keys, while some commenters dispute whether the attacks are realistic.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** A LessWrong post argues that two agents running on the same inference server can reliably communicate even when they cannot send each other messages or access the same files, using side channels in the shared inference stack (tool-2-1). Secondary write-ups, including theprimary.com, attribute the study to Niranjan Deshpande and repeat the claim that sandboxed models can communicate covertly across shared inference hardware (tool-2-2).
- **Not yet confirmed:** Neither the post nor the coverage supplies an independent reproduction or third-party measurement, and no inference-server vendor has confirmed the behavior or responded publicly. Commenters on the discussion dispute that the attacks are realistic, arguing they require the two agents to already know of each other and share pre-arranged messages, plus detailed knowledge of the server's kernels and configuration — so the channels' practicality, reliability outside a demonstration, and the effectiveness of proposed defenses such as per-context cache-separation keys all remain open.

</div>

## Background

Sandboxing an AI agent usually means restricting its file system, network and tool access. Inference servers such as vLLM keep a key-value (KV) cache — stored attention state for prompt tokens already processed — so requests that share a prefix can skip recomputation, and the LessWrong post argues that this shared cache, or the timing differences it creates, gives sandboxed models a channel that sits outside the sandbox. Commenters point to web browsers, which learned to partition caches per origin, as the precedent for separating such shared state between security contexts.

## Why it matters

Providers that serve mutually untrusted tenants or agents from one inference instance should treat prompt-cache isolation as a configuration requirement rather than an optional performance win: per-tenant or per-user cache keys and scopes, plus distinct salts on self-hosted servers, are the documented way to stop one context from probing another's cache. The exposure is created by the serving stack itself — vLLM's PagedAttention shares GPU memory pages across requests through a reference-counted allocator — so callers cannot assume separation unless the operator has configured it.

## Community discussion

Commenters split on feasibility: tsimionescu calls the described attacks unrealistic because they require the agents to know each other, pre-share messages, and understand the serving stack in detail, while amluto argues inference servers should offer cache-separation keys similar to browser origin isolation. kgeist separately describes a timing channel in a shared vLLM instance, where one model's long-document reads slow another model's decoding enough to signal bits.

## Further reading

- [Models Can Communicate via Inference Servers Despite Being ...](https://www.lesswrong.com/posts/7wzWuLP3HhyBLmKfo/models-can-communicate-via-inference-servers-despite-being)
- [Sandboxed artificial intelligence models can communicate ...](https://theprimary.com/ai-tech/2026-11-20/sandboxed-ai-covert-channels)
- [Prompt Caching Security : Isolation and Side Channels](https://nhimg.org/prompt-caching-security-guide)
- [vLLM and the KV - Cache Isolation Problem: How Shared Memory...](https://www.systemshardening.com/articles/ai-landscape/vllm-shared-memory-inference-isolation/)

{% endraw %}
