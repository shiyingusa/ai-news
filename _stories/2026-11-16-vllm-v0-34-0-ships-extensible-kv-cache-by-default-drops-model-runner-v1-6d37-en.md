---
layout: story
lang: en
date: 2026-11-16 06:00:00 -0500
issue: "2026-11-16"
story_id: "vllm-v0-34-0-ships-extensible-kv-cache-by-default-drops-model-runner-v1-6d37"
permalink: "/2026/11/16/vllm-v0-34-0-ships-extensible-kv-cache-by-default-drops-model-runner-v1-6d37/"
title: "vLLM v0.34.0 ships extensible KV cache by default, drops Model Runner V1"
dek: "vLLM v0.34.0 is out, publishing CUDA 13.0, ROCm 10.0, CPU and XPU wheels plus matching Docker images."
description: "vLLM v0.34.0 is out, publishing CUDA 13.0, ROCm 10.0, CPU and XPU wheels plus matching Docker images."
section: "ai-news"
rank: 201
edition: 2
section_rank: 1
score: 8.0
status: "Available"
source_name: "GitHub"
source_url: "https://github.com/vllm-project/vllm/releases/tag/v0.34.0"
via: null
discussion_url: null
published_at: "2026-11-16T23:22:00+00:00"
tags: ["vLLM", "open-source", "inference", "model serving", "performance"]
topics: ["vllm", "open-source", "inference", "model-serving", "performance"]
order: "20261116-2-998"
image: "/assets/stories/2026-11-16/vllm-v0-34-0-ships-extensible-kv-cache-by-default-drops-model-runner-v1-6d37-share.jpg"
art: "/assets/stories/2026-11-16/vllm-v0-34-0-ships-extensible-kv-cache-by-default-drops-model-runner-v1-6d37.jpg"
thumb: "/assets/stories/2026-11-16/vllm-v0-34-0-ships-extensible-kv-cache-by-default-drops-model-runner-v1-6d37-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/gd5012ed06ec0118202e430ab5cd24b1f6b0facdcf3bdec495bf52aa69afb48768da57515ae05f1a1129a6a3a7beebf14_1280.jpg", "author": "kewl", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/server-room-datacenter-network-90389/", "provider": "Pixabay", "width": 4818, "height": 3212}
---

{% raw %}
<div class="story-lead" markdown="1">

vLLM v0.34.0 is out, publishing CUDA 13.0, ROCm 10.0, CPU and XPU wheels plus matching Docker images. The headline default change is the extensible KV cache: on CUDA and ROCm, vLLM now sizes the cache from memory actually free after CUDA graph capture and warmup, with `gpu_memory_utilization` defaulting to 1.0 — the release cites MiniMax-M3 on H200 growing from 433k to 672k cached tokens, while warning that per-token decode latency can rise 6–18% on some H200 models at concurrency 128. Model Runner V1 is removed, so setting `VLLM_USE_V2_MODEL_RUNNER=0` now fails at startup, and the default `--block-size` moves from 16 to 64. The release also adds 10 model integrations, including Mistral Large 4 (1T total / 52B active parameters, FP8 and NVFP4), and reports speedups such as up to 1.95× decode for Step5 on 4×GB200 and 1.6× output throughput for GLM-5.3-Flash.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** the vLLM release page itself states that v0.34.0 contains 1,061 commits from 412 contributors, turns extensible KV cache on by default, removes Model Runner V1, changes the default block size to 64, drops ROCm 7.2 artifacts, requires `huggingface_hub >= 2.0.0`, and publishes install commands and image tags for CUDA 13.0, ROCm 10.0, CPU and XPU.
- **Not yet confirmed:** all performance multipliers (1.95× decode, 1.6× throughput, 1.24–1.40× faster TTFT, 1.34–1.59× decode attention) are the project's own benchmarks on specific hardware and configurations, with no independent reproduction supplied; the KV cache capacity example is a single H200 configuration rather than a general guarantee. The release page also carries an unresolved reviewer note questioning whether the XPU install line resolves without an extra index for `vllm_xpu_kernels==0.1.17`.

</div>

## Background

vLLM is an open-source engine for serving large language models, and its central mechanism is the paged KV cache: the key/value tensors computed for every earlier token are kept in GPU memory in fixed-size blocks, letting the engine pack many concurrent requests onto one GPU without recomputing history. Block size and how much GPU memory the cache may claim are therefore the knobs that determine how much context and how many simultaneous users a deployment can hold. Model Runner V2 is vLLM's newer GPU execution path, which until this release shipped alongside the older V1 runner that operators could still select by setting an environment variable.

## Why it matters

Teams upgrading must audit launch flags before deploying: removing `VLLM_USE_V2_MODEL_RUNNER=0`, passing `--block-size 16` or `--gpu-memory-utilization 0.9` to restore prior cache sizing, and migrating V1 logits processors to `vllm.v1.worker.gpu.sample.logits_processor`, or existing serving configs will fail at startup or change throughput and latency behaviour.

## What to watch

Watch whether the next vLLM release resolves the flagged XPU wheel-index question and whether independent benchmarks reproduce the claimed Blackwell and MI355X speedups on workloads other than the cited model/hardware pairs.

{% endraw %}
