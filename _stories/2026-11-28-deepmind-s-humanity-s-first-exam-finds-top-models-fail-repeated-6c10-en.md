---
layout: story
lang: en
date: 2026-11-28 06:25:56 -0500
issue: "2026-11-28"
story_id: "deepmind-s-humanity-s-first-exam-finds-top-models-fail-repeated-6c10"
permalink: "/2026/11/28/deepmind-s-humanity-s-first-exam-finds-top-models-fail-repeated-6c10/"
title: "DeepMind's \"Humanity's First Exam\" finds top models fail repeated everyday tasks"
dek: "Google DeepMind tested 18 AI models with a benchmark it calls \"Humanity's First Exam,\" and the top performers solved nearly every task family at least once — but stumbled when asked for 16 correct answers in a row."
description: "Google DeepMind tested 18 AI models with a benchmark it calls \"Humanity's First Exam,\" and the top performers solved nearly every task family at least once — but stumbled when asked for 16 correct answers in a row."
section: "ai-news"
rank: 2
edition: 0
section_rank: 2
score: 7.0
status: "Demonstrated"
source_name: "The Decoder"
source_url: "https://the-decoder.com/google-deepminds-humanitys-first-exam-shows-top-ai-models-still-fail-simple-everyday-tasks-under-repeated-runs/"
via: null
discussion_url: null
published_at: "2026-11-28T11:12:30+00:00"
tags: ["AI reliability", "benchmark evaluation", "Google DeepMind", "visual perception", "foundation models"]
topics: ["ai-reliability", "benchmark-evaluation", "google-deepmind", "visual-perception", "foundation-models"]
order: "20261128-0-997"
image: "/assets/stories/2026-11-28/deepmind-s-humanity-s-first-exam-finds-top-models-fail-repeated-6c10-share.jpg"
art: "/assets/stories/2026-11-28/deepmind-s-humanity-s-first-exam-finds-top-models-fail-repeated-6c10.jpg"
thumb: "/assets/stories/2026-11-28/deepmind-s-humanity-s-first-exam-finds-top-models-fail-repeated-6c10-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g652916627956618bf5109f0ed4f67c1e08891480706c124fdb1a829776ef071055ae035c337dff37b2f29e41d3c22de2fb40611847ba804d7120c2fb91d481a9_1280.jpg", "author": "jarmoluk", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/robot-arm-technology-robot-arm-2791670/", "provider": "Pixabay", "width": 3000, "height": 2000}
---

{% raw %}
<div class="story-lead" markdown="1">

Google DeepMind tested 18 AI models with a benchmark it calls "Humanity's First Exam," and the top performers solved nearly every task family at least once — but stumbled when asked for 16 correct answers in a row. Even the strongest entrant, OpenAI's GPT-6.2 Astra, failed to stay consistent across those repeated runs, according to The Decoder's coverage.

Visual perception accounted for 73 percent of the errors, and giving models more compute time at inference did not close the gap. The results come from DeepMind's own evaluation rather than an independent third-party test, and the report does not detail the task set or per-model scores.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** Google DeepMind launched Humanity's First Exam, a reliability benchmark that Google's blog says uses 544 prompts; The Decoder reports that it tested 18 models and that even leading systems such as OpenAI's GPT-6.2 Astra stumbled when asked for 16 consecutive correct answers, with visual perception accounting for 73% of errors.
- **Not yet confirmed:** The full per-model scores, the exact 73% error breakdown across all 18 models, and the finding that more compute time does not fix the failures have not been independently replicated; those details rest on The Decoder's account and Google's benchmark description, and the report does not provide the underlying paper or a complete results table.

</div>

## Background

The benchmark's name inverts Humanity's Last Exam, a deliberately brutal test of frontier models; Humanity's First Exam goes the other way, asking straightforward everyday questions that people get right almost every time. Google launched it on Kaggle as a public leaderboard built from 544 short text and image prompts, scoring how consistently a model answers rather than how often it answers correctly on a single try.

## Why it matters

For teams deploying models on repetitive everyday work, single-run benchmark scores overstate reliability: a model that can do a task once may still fail a string of 16 attempts, which is closer to how production pipelines consume model output. The finding that 73 percent of errors trace to visual perception points builders toward verifying image- and document-reading steps and adding retries or human checks there, rather than assuming extra inference-time compute will fix the failures.

## What to watch

Watch for DeepMind to publish the full benchmark, its task definitions and per-model pass rates, and for independent groups to rerun it on models outside the original 18.

## Further reading

- [Humanity ’ s First Exam : Testing LLM reliability](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/humanitys-first-exam/)
- [DeepMind ' s new AI exam | The Neuron](https://www.theneuron.ai/newsletter/deepmind-s-new-ai-exam/)
- [Humanity ' s First Exam (HFE) Leaderboard | Kaggle](https://www.kaggle.com/benchmarks/deepmind/hfe)
- [DeepMind ' s new AI exam | The Neuron](https://www.theneuron.ai/newsletter/deepmind-s-new-ai-exam/)
- [Humanity ’ s First Exam : Testing LLM reliability](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/humanitys-first-exam/)

{% endraw %}
