---
layout: story
lang: en
date: 2026-11-16 06:00:00 -0500
issue: "2026-11-16"
story_id: "anthropic-says-claude-mythos-preview-cut-amd-mi355x-onboarding-to-three-851a"
permalink: "/2026/11/16/anthropic-says-claude-mythos-preview-cut-amd-mi355x-onboarding-to-three-851a/"
title: "Anthropic says Claude Mythos Preview cut AMD MI355X onboarding to three days"
dek: "Anthropic told IPO investors that its Claude Mythos Preview model needed about three days and “basically no human intervention” to get one of its models running on AMD MI355X GPUs for prompt processing…"
description: "Anthropic told IPO investors that its Claude Mythos Preview model needed about three days and “basically no human intervention” to get one of its models running on AMD MI355X GPUs for prompt processing…"
section: "chips-compute"
rank: 18
edition: 0
section_rank: 3
score: 7.0
status: "Announced"
source_name: "Tom's Hardware"
source_url: "https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-says-claude-mythos-slashed-software-work-to-onboard-amd-gpus-from-up-to-12-months-to-around-three-days-writing-almost-100-percent-of-kernels-autonomously-chips-away-at-nvidias-cuda-moat"
via: null
discussion_url: null
published_at: "2026-11-16T15:00:00+00:00"
tags: ["AI compute", "AMD GPUs", "CUDA moat", "kernel automation", "Anthropic"]
topics: ["ai-compute", "amd-gpus", "cuda-moat", "kernel-automation", "anthropic"]
order: "20261116-0-981"
image: "/assets/stories/2026-11-16/anthropic-says-claude-mythos-preview-cut-amd-mi355x-onboarding-to-three-851a-share.jpg"
art: "/assets/stories/2026-11-16/anthropic-says-claude-mythos-preview-cut-amd-mi355x-onboarding-to-three-851a.jpg"
thumb: "/assets/stories/2026-11-16/anthropic-says-claude-mythos-preview-cut-amd-mi355x-onboarding-to-three-851a-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g30b02215d4dcdf185f240b3760f24beae43f16d2fb6dcf3d0f75dee023e5c38cd68d8788a2923b9854af56b188112a990e9e264dced42179d4109906a18d948e_1280.jpg", "author": "cookieone", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/internet-information-service-system-8097838/", "provider": "Pixabay", "width": 6000, "height": 4000}
---

{% raw %}
<div class="story-lead" markdown="1">

Anthropic told IPO investors that its Claude Mythos Preview model needed about three days and “basically no human intervention” to get one of its models running on AMD MI355X GPUs for prompt processing, versus six to 12 months of work by dozens of engineers using traditional methods. Tom Brown, Anthropic’s co-founder and chief compute officer, said Mythos ported or wrote “almost 100% of the kernels,” the low-level code that adapts a model to specific chips. The figures are Anthropic’s own and have not been independently verified; they cover prompt processing for one model at “a useful level of performance,” not training or broader workloads. Anthropic’s prospectus says only that it can onboard new chip platforms “in a fraction of the time it once took,” without a number.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** Anthropic, through co-founder Tom Brown in a Nov. 10 IPO roadshow video, stated that Claude Mythos Preview brought up one model on AMD MI355X GPUs for prompt processing in about three days with basically no human intervention and wrote or ported almost 100% of kernels; the prospectus repeats a qualitative version.
- **Not yet confirmed:** independent tests of the three-day time, near-100% kernel figure, or resulting performance; the scope is prompt processing for one model, and the six-to-12-month baseline is Anthropic’s historical estimate.

</div>

## Background

Kernels are the low-level routines that bind a model's operations to a particular chip, and Nvidia's nearly two-decade-old CUDA platform is the accumulated library of them that has kept developers on its hardware; AMD's equivalent is ROCm, with HIP as its programming layer and HIPify as its CUDA-conversion tool. AMD's own earlier attempt at automated kernel writing, the GEAK agent published in August 2025, got 19 of 30 expert-written kernels right at 0.92 times the experts' speed on average, which shows where the technique stood before this claim. The disclosure also lands just before Anthropic's IPO: AI Daily Radar's November 15 digest reported CEO Dario Amodei calling compute purchases the company's "deepest business dilemma," with commitments totaling nearly $901 billion.

## Why it matters

For teams choosing AI accelerators, the claimed result targets the main switching cost—CUDA-specific kernel work—rather than AMD hardware itself. But because it covers one model and prompt processing and is unverified, buyers should still budget for porting, validation, and performance testing before treating AMD GPUs as a drop-in substitute.

## What to watch

Anthropic’s IPO, which the article says is due next week, is the next checkpoint. Independent kernel benchmarks or a technical write-up covering training and more than one model would test the claim.

## Further reading

- [2026-11-15 — Amodei calls compute Anthropic's "deepest business dilemma" before IPO](https://the-decoder.com/anthropic-ceo-amodei-admits-theres-a-huge-uncertainty-in-whats-going-to-happen-next-year-days-before-a-record-ipo/)

{% endraw %}
