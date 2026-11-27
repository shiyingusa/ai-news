---
layout: story
lang: en
date: 2026-11-25 06:28:44 -0500
issue: "2026-11-25"
story_id: "anthropic-gave-a-company-24-hours-to-disprove-distillation-poster-says-bbef"
permalink: "/2026/11/25/anthropic-gave-a-company-24-hours-to-disprove-distillation-poster-says-bbef/"
title: "Anthropic gave a company 24 hours to disprove distillation, poster says"
dek: "A developer posting on Hacker News says Anthropic flagged their company's API usage as model distillation and gave the company 24 hours to prove it was not doing so."
description: "A developer posting on Hacker News says Anthropic flagged their company's API usage as model distillation and gave the company 24 hours to prove it was not doing so."
section: "ai-news"
rank: 4
edition: 0
section_rank: 4
score: 7.0
status: null
source_name: "Hacker News"
source_url: "https://news.ycombinator.com/item?id=50630809"
via: null
discussion_url: null
published_at: "2026-11-24T16:45:44+00:00"
tags: ["Anthropic", "model distillation", "API policy enforcement", "AI developer platform", "Hacker News discussion"]
topics: ["anthropic", "model-distillation", "api-policy-enforcement", "ai-developer-platform", "hacker-news-discussion"]
order: "20261125-0-995"
image: "/assets/stories/2026-11-25/anthropic-gave-a-company-24-hours-to-disprove-distillation-poster-says-bbef-share.jpg"
art: "/assets/stories/2026-11-25/anthropic-gave-a-company-24-hours-to-disprove-distillation-poster-says-bbef.jpg"
thumb: "/assets/stories/2026-11-25/anthropic-gave-a-company-24-hours-to-disprove-distillation-poster-says-bbef-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g6e146d65942a96c732f018ca275b5646b22a1ec2a70ba94ee26a6c6163e21ec5c6a393908a0512696227f1b946543a3f37d9e423660dc05aedf890c63766ff00_1280.jpg", "author": "Innovalabs", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/software-development-developer-6523979/", "provider": "Pixabay", "width": 7360, "height": 4912}
---

{% raw %}
<div class="story-lead" markdown="1">

A developer posting on Hacker News says Anthropic flagged their company's API usage as model distillation and gave the company 24 hours to prove it was not doing so. The poster, weli, says the company does not train its own models and that the only usage likely to look suspicious is automated regression benchmarking run whenever AI settings change.

They are asking how to rebut the accusation without exposing user data; Anthropic has not publicly confirmed the account in the thread.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** A Hacker News user posting as "weli" says their company was accused by Anthropic of using its API to distill Claude models and was given 24 hours to prove otherwise; the poster denies training models and says the only pattern that could look like distillation is automated regression benchmarking when AI settings change (the author's own account on Hacker News). Anthropic has publicly levelled similar distillation accusations at other developers, including DeepSeek and Moonshot AI, per DeepLearning.AI's The Batch.
- **Not yet confirmed:** That Anthropic actually sent such a notice, which policy clause it cites, and whether the flag is a false positive — no copy of the notice, date, or company identity was provided, and Anthropic has not commented publicly. Commenters' accounts — an OpenAI case traced to a compromised API key, advice to route Anthropic models through AWS Bedrock — are individual anecdotes, not evidence about this case.

</div>

## Background

Model distillation is the practice of training a model on another model's outputs, and API providers police it through usage terms and monitoring of account activity. Anthropic's Usage Policy applies to anyone who submits inputs to its products, including developers and businesses using its API, and Anthropic says it updated the policy on Oct. 8, 2026. The poster says their automated regression benchmarks are permitted under that policy.

## Why it matters

For teams running automated evaluations against Anthropic's API, the practical consequence is that they may need to produce evidence—benchmark code, its git history and request metadata—on very short notice to avoid losing access.

## What to watch

Whether Anthropic responds publicly to the thread or the poster reports the outcome after the 24-hour deadline is the next checkable step.

## Further reading

- [2026 Usage Policy update \ Anthropic](https://www.anthropic.com/news/2026-usage-policy-update)
- [Usage Policy - assets.claude.com](https://assets.claude.com/88cf16e8b7d203be16d2c726bcd28a6ec7c7f5c8.pdf)
- [Anthropic Accuses DeepSeek and Chinese AI Firms of Claude Model ...](https://explore.n1n.ai/blog/anthropic-accuses-deepseek-claude-model-distillation-2026-02-24)
- [Anthropic 's Accounts of Distillation , Gray-Market Transfer Stations...](https://www.deeplearning.ai/the-batch/some-kimi-and-deepseek-users-were-served-claude-instead-anthropic-says)

<div class="community" markdown="1">

## Community discussion: opinion, not evidence

Commenters advised preserving the benchmark code and git history and even submitting the same evidence to Claude to test whether it looks sufficient, while one reported a similar OpenAI flag that turned out to involve a compromised API key used for actual distillation. Others argued the episode is a reason to move to a provider with human account support, such as Bedrock, or to switch vendors entirely.

</div>

{% endraw %}
