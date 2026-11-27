---
layout: story
lang: en
date: 2026-11-24 06:26:29 -0500
issue: "2026-11-24"
story_id: "aws-launches-five-open-strands-decider-v2-models-the-new-stack-reports-88c0"
permalink: "/2026/11/24/aws-launches-five-open-strands-decider-v2-models-the-new-stack-reports-88c0/"
title: "AWS launches five open Strands Decider v2 models, The New Stack reports"
dek: "AWS on Monday launched Strands Decider v2, a family of five open “decision models” that The New Stack reports are built on Google’s Gemma 4 and released under the Apache 2.0 license."
description: "AWS on Monday launched Strands Decider v2, a family of five open “decision models” that The New Stack reports are built on Google’s Gemma 4 and released under the Apache 2.0 license."
section: "ai-news"
rank: 4
edition: 0
section_rank: 4
score: 7.0
status: "Released"
source_name: "The New Stack"
source_url: "https://thenewstack.io/aws-strands-decider-v2/"
via: "Techmeme"
discussion_url: null
published_at: "2026-11-24T04:25:01+00:00"
tags: ["AWS", "open models", "Gemma 4", "Apache 2.0", "model release"]
topics: ["aws", "open-models", "gemma-4", "apache-2-0", "model-release"]
order: "20261124-0-995"
image: "/assets/stories/2026-11-24/aws-launches-five-open-strands-decider-v2-models-the-new-stack-reports-88c0-share.jpg"
art: "/assets/stories/2026-11-24/aws-launches-five-open-strands-decider-v2-models-the-new-stack-reports-88c0.jpg"
thumb: "/assets/stories/2026-11-24/aws-launches-five-open-strands-decider-v2-models-the-new-stack-reports-88c0-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/ge3b3eb3a7944384a8a3ab9062def5a2d7625bf4a312b51d5aaa3ab54bb29a6b91a9734cfb548cb0c19e118f3c3aef506670ba68157d3d3f313fda8c5ec5260b2_1280.jpg", "author": "MightyFineBros", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/data-center-technology-server-7388620/", "provider": "Pixabay", "width": 4800, "height": 2700}
---

{% raw %}
<div class="story-lead" markdown="1">

AWS on Monday launched Strands Decider v2, a family of five open “decision models” that The New Stack reports are built on Google’s Gemma 4 and released under the Apache 2.0 license. The models span 2 billion to 31 billion parameters, giving AI builders a single permissively licensed family across small and large sizes.

The report does not include benchmark results or explain what the models do beyond the decision-model label, so the capability claims remain unverified.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** Strands Labs' own announcement says Strands Decider v2 is a family of five decision models built on Gemma 4, spanning 2B to 31B parameters under Apache 2.0, with weights published on Hugging Face and v2 support in the open-source Strands Decider repository; the models do not generate text but pick from a supplied list of options, returning a probability for each in a single forward pass, and VentureBeat independently describes the release the same way. The New Stack dates the launch to "Monday," consistent with third-party coverage placing it on Nov 23, 2026.
- **Not yet confirmed:** the accuracy and calibration of the returned probabilities at each model size rest so far on the vendor's description, with no independent benchmark supplied; throughput, latency and how the five sizes compare in real agent-routing workloads are also unverified, and the item offers no detail on what changed from the earlier Strands Labs release seven weeks prior.

</div>

## Background

Strands Decider is a family of "system one" models — the term for fast, intuitive decisions rather than the slower step-by-step deliberation of reasoning models — which AWS's Strands Labs positions for tasks like agent routing, where a model picks which tool or path an agent should take. The official release notes say v2 ships five such models built on Google's Gemma 4, spanning E2B to 31B parameters, with weights published on Hugging Face and v2 support added to the open-source Strands Decider repository. The New Stack notes the launch came only about seven weeks after the previous Strands Labs release.

## Why it matters

For AI builders, the practical change is a permissively licensed family that covers both small and large models, so teams can test a lightweight variant for constrained deployments and a 31B variant for heavier workloads without separate license terms. The report provides no independent performance data, so teams should validate quality before standardizing on it.

## What to watch

Watch for independent benchmark results across the five sizes, especially the 31B variant, which would test whether the larger models deliver enough gain to justify their size.

## Further reading

- [Introducing Strands Decider v2: open, calibrated system one ...](https://strandsagents.com/blog/introducing-strands-decider-v2/)
- [Strands Decider v2: 5 Open Models (Apache 2.0) | explainx.ai Blog](https://explainx.ai/blog/aws-strands-decider-v2-gemma4-november-2026)
- [Introducing Strands Decider v2: open, calibrated system one ...](https://strandsagents.com/blog/introducing-strands-decider-v2/)
- [AWS's Strands Decider v2 targets the agent decisions that ...](https://venturebeat.com/data/awss-strands-decider-v2-targets-the-agent-decisions-that-hinge-on-a-single-detail)
- [Strands Decider v2: 5 Open Models (Apache 2.0) | explainx.ai Blog](https://explainx.ai/blog/aws-strands-decider-v2-gemma4-november-2026)

{% endraw %}
