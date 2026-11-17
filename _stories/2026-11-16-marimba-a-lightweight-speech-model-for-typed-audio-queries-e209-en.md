---
layout: story
lang: en
date: 2026-11-16 06:00:00 -0500
issue: "2026-11-16"
story_id: "marimba-a-lightweight-speech-model-for-typed-audio-queries-e209"
permalink: "/2026/11/16/marimba-a-lightweight-speech-model-for-typed-audio-queries-e209/"
title: "Marimba: A Lightweight Speech Model for Typed Audio Queries"
dek: "A new arXiv paper presents Marimba, a lightweight speech model that answers typed yes/no, choice and score queries over an 8-second audio window and returns calibrated probabilities."
description: "A new arXiv paper presents Marimba, a lightweight speech model that answers typed yes/no, choice and score queries over an 8-second audio window and returns calibrated probabilities."
section: "ai-news"
rank: 15
edition: 0
section_rank: 15
score: 7.0
status: "Available"
source_name: "Reddit r/MachineLearning"
source_url: "https://www.reddit.com/r/MachineLearning/comments/1xxsqro/marimba_a_system_one_model_for_speech_r/"
via: null
discussion_url: null
published_at: "2026-11-16T15:47:18+00:00"
tags: ["speech recognition", "audio understanding", "model efficiency", "calibration", "speaker diarization"]
topics: ["speech-recognition", "audio-understanding", "model-efficiency", "calibration", "speaker-diarization"]
order: "20261116-0-984"
image: "/assets/stories/2026-11-16/marimba-a-lightweight-speech-model-for-typed-audio-queries-e209-share.jpg"
art: "/assets/stories/2026-11-16/marimba-a-lightweight-speech-model-for-typed-audio-queries-e209.jpg"
thumb: "/assets/stories/2026-11-16/marimba-a-lightweight-speech-model-for-typed-audio-queries-e209-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g462a1570afc2de752e4e73a98d4e5a9869966075ba336d9d6d43804f68770a4600501db87ac5e360e1e7e8a025f4f936fdb1304cad009569c047b08e9e138263_1280.jpg", "author": "Pexels", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/audio-microphone-1844798/", "provider": "Pixabay", "width": 4928, "height": 3264}
---

{% raw %}
<div class="story-lead" markdown="1">

A new arXiv paper presents Marimba, a lightweight speech model that answers typed yes/no, choice and score queries over an 8-second audio window and returns calibrated probabilities. It uses one frozen Qwen3-ASR-0.6B encoder pass per window, scoring term queries from the decoder's greedy and four beam hypotheses, taking language scores from the ASR model, and adding small readouts on frozen layers for turn-end and speaker tasks. The authors report that on 1,000 public questions it matches or beats Qwen3-Omni (30B-A3B) on 6 of 9 tests, reaches 100% language ID on 300 FLEURS clips and 0.966–0.980 speaker-change AUROC on AMI and VoxConverse, but trails Smart Turn v3.2 on turn-end detection (0.930 vs 0.982 AUROC) and scores at chance on CochlScene scene classification; they also disclose that the turn-end readout was trained on Smart Turn data. Code, Apache-2.0 weights, a demo and a pip-installable `marimba-audio` package are public.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** An arXiv preprint (2611.18330) by the Marimba authors describes a speech interface built on frozen Qwen3-ASR 0.6B features, where lexical term questions are scored zero-shot from ASR transcripts and non-lexical questions use a question-conditioned head plus a separate layer-18 turn-end readout; the author also links Apache-2.0 weights, code and a demo.
- **Not yet confirmed:** All benchmark figures — matching or beating Qwen3-Omni (30B-A3B) on 6 of 9 tests, 100% language ID on 300 FLEURS clips, speaker-change AUROC of 0.966–0.980 on AMI and VoxConverse, and speaker count beating pyannote 3.1 — are author-reported in a non-peer-reviewed preprint with no independent replication; the authors themselves flag that the turn-end readout was trained on Smart Turn data and that all heads fall to chance on unseen CochlScene classification.

</div>

## Background

The post is a follow-up to an earlier r/MachineLearning thread that described the method before a paper existed; this version adds the arXiv writeup, Apache-2.0 weights on Hugging Face, a pip-installable `marimba-audio` package and a demo. Marimba's design rests on encoder probing: rather than fine-tuning a large audio-language model, it runs one frozen Qwen3-ASR-0.6B encoder over each 8-second window and attaches small task-specific "readouts" to intermediate layers (layer 12 for speaker attributes, layer 18 for turn end), so a single forward pass can serve many different typed questions. Its probabilities come from Platt scaling, a standard calibration step that fits a logistic curve mapping raw scores to calibrated probabilities. The "System One" label refers to fast, single-pass, reflex-like inference, as opposed to slower multi-step deliberation in a large omni model.

## Why it matters

Developers can test a single 0.6B frozen ASR encoder for term spotting, language ID, turn-end and speaker tasks via the public `pip install marimba-audio` package, but should treat it as a fixed-task baseline: the authors report chance-level results on unseen scene classification and weaker turn-end detection than Smart Turn v3.2.

## Further reading

- [[2611.18330] Marimba: A System One Model for Speech - arXiv.org](https://arxiv.org/abs/2611.18330)
- [MARIMBA: A System One Model for Speech - arXiv.org](https://arxiv.org/pdf/2611.18330)
- [Marimba: a frozen 0.6B ASR backbone beats 30B… · AGI Hunt](https://agihunt.info/en/p/1a1e51a4fb7e78c93db0a74dac2)

{% endraw %}
