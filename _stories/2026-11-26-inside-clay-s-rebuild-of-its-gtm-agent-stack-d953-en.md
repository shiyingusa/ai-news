---
layout: story
lang: en
date: 2026-11-26 18:20:28 -0500
issue: "2026-11-26"
story_id: "inside-clay-s-rebuild-of-its-gtm-agent-stack-d953"
permalink: "/2026/11/26/inside-clay-s-rebuild-of-its-gtm-agent-stack-d953/"
title: "Inside Clay's Rebuild of Its GTM Agent Stack"
dek: "A Clay AI leader explains the engineering and product tradeoffs behind its GTM agents, from coding-agent architecture and evals to model routing, post-training timing, and workload scaling."
description: "A Clay AI leader explains the engineering and product tradeoffs behind its GTM agents, from coding-agent architecture and evals to model routing, post-training timing, and workload scaling."
section: "tech-blog"
rank: 206
edition: 2
section_rank: 1
score: 7.0
status: null
source_name: "Latent Space"
source_url: "https://latent.space/p/how-clay-builds-gtm-agents-jeff-barg-head-of-ai/"
via: null
discussion_url: null
published_at: "2026-11-26T23:02:48+00:00"
tags: ["agent architecture", "GTM agents", "model routing", "LLM evaluation", "inference infrastructure"]
topics: ["agent-architecture", "gtm-agents", "model-routing", "llm-evaluation", "inference-infrastructure"]
order: "20261126-2-993"
image: "/assets/stories/2026-11-26/inside-clay-s-rebuild-of-its-gtm-agent-stack-d953-share.jpg"
art: "/assets/stories/2026-11-26/inside-clay-s-rebuild-of-its-gtm-agent-stack-d953.jpg"
thumb: "/assets/stories/2026-11-26/inside-clay-s-rebuild-of-its-gtm-agent-stack-d953-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g796fddadb1cb243a001eaf5bcbdb8c1bb47b24a592f2a2288e53bf203afb97a3eb00a863abdd817b60c8bf154407d6df2b33f01259e15655e9819f069ba70e2c_1280.jpg", "author": "Akela999", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/data-center-engine-room-2476790/", "provider": "Pixabay", "width": 4096, "height": 2160}
---

{% raw %}
<div class="story-lead" markdown="1">

A Clay AI leader explains the engineering and product tradeoffs behind its GTM agents, from coding-agent architecture and evals to model routing, post-training timing, and workload scaling.

</div>

## Background

Clay, a go-to-market platform, is rebuilding its agent stack so that its own agent and outside coding harnesses such as Claude Code can both research companies, qualify leads, and run campaigns against large tables. Jeff Barg, Clay's Head of AI, describes the architectural and economic choices behind that effort.

## Solution

Sculptor began as a carefully prompted tool loop: it was good at adding columns but poor at booking ten qualified meetings, and an LLM judge that checked tool calls missed real-world uses such as analyzing tables or handling enterprise tables with millions of rows. Clay therefore rebuilt Sculptor as a coding agent on the Pi harness, running the Clay CLI in a cloud sandbox, and added Audiences to match CRM and Gong records. Barg says lead-qualification evals have been saturated for about a year, so frontier models now matter mainly for orchestration and deep research—where the best plays can be 10–100x more effective—and Clay will soon route models automatically because customers dislike choosing. He argues post-training is premature before $10M–$100M of inference spend, after which an open-weight model and then a smaller model trained on Clay's tools and queries can approach Opus-level task performance. Clay runs agents on BullMQ rather than Temporal or LangGraph; per-row runs create demand spikes, so it added LangSmith visibility, throttling, pause/resume, and fairness controls. A Jev classifier could score all 40 million companies for about $1,500, though it is not in production; agents still cannot reliably diagnose their own long traces.

## Takeaway

The broader lesson is that agent quality comes less from a universal model or framework than from matching intelligence to the task, exposing the right data, and designing for real usage and spiky operational load.

{% endraw %}
