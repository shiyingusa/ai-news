---
layout: story
lang: en
date: 2026-11-16 06:00:00 -0500
issue: "2026-11-16"
story_id: "nvidia-announces-rubin-hpc-gpu-for-scientific-simulation-13aa"
permalink: "/2026/11/16/nvidia-announces-rubin-hpc-gpu-for-scientific-simulation-13aa/"
title: "NVIDIA Announces Rubin HPC GPU for Scientific Simulation"
dek: "At SC26, NVIDIA announced Rubin HPC, a new GPU in its Vera Rubin data-center platform aimed at simulation and data processing for science, engineering and analytics workloads."
description: "At SC26, NVIDIA announced Rubin HPC, a new GPU in its Vera Rubin data-center platform aimed at simulation and data processing for science, engineering and analytics workloads."
section: "chips-compute"
rank: 16
edition: 0
section_rank: 1
score: 7.0
status: "Announced"
source_name: "NVIDIA Blog"
source_url: "https://blogs.nvidia.com/blog/rubin-hpc/"
via: null
discussion_url: null
published_at: "2026-11-16T16:00:01+00:00"
tags: ["NVIDIA", "Rubin HPC", "GPUs", "HPC", "AI compute"]
topics: ["nvidia", "rubin-hpc", "gpus", "hpc", "ai-compute"]
order: "20261116-0-983"
image: "/assets/stories/2026-11-16/nvidia-announces-rubin-hpc-gpu-for-scientific-simulation-13aa-share.jpg"
art: "/assets/stories/2026-11-16/nvidia-announces-rubin-hpc-gpu-for-scientific-simulation-13aa.jpg"
thumb: "/assets/stories/2026-11-16/nvidia-announces-rubin-hpc-gpu-for-scientific-simulation-13aa-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/gb348523c3a621152ef239eb3fa3f1643c98ec0c5b18fefdb9283d617d4fb2b98f4995ebd7711cc5e07623238a897207452108b07984a8eae0fbc32116af1da26_1280.jpg", "author": "cookieone", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/internet-information-service-system-8097838/", "provider": "Pixabay", "width": 6000, "height": 4000}
---

{% raw %}
<div class="story-lead" markdown="1">

At SC26, NVIDIA announced Rubin HPC, a new GPU in its Vera Rubin data-center platform aimed at simulation and data processing for science, engineering and analytics workloads. NVIDIA says the chip carries more than 50,000 CUDA cores on a single GPU — which it calls a record — plus a "sparse data acceleration" capability meant to keep those cores fed during irregular memory access patterns common in sparse matrix, stencil, sorting and reduction operations, and seventh-generation NVLink for GPU-to-GPU connectivity. The pitch is that AI agents exploring candidate materials, molecules and designs will drive more simulation demand, so faster simulation shortens the discovery loop. NVIDIA states Rubin HPC is "expected to be available in 2028"; no pricing, memory capacity, bandwidth, power figures or independent benchmark results were disclosed.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** NVIDIA's own announcement states the GPU is part of the Vera Rubin platform, has more than 50,000 CUDA cores, includes sparse data acceleration and seventh-generation NVLink, and is targeted at HPC and analytics workloads, with availability expected in 2028.
- **Not yet confirmed:** the "record number of CUDA cores" claim (no comparison part is given), any performance gain from the sparse data acceleration or the balanced compute/memory design, and all specifications beyond core count — memory size, bandwidth, power draw, form factor and price — plus any independent benchmark; NVIDIA provided no measured results.

</div>

## Background

Rubin HPC sits inside NVIDIA's Vera Rubin platform, which Jensen Huang detailed at GTC 2025 as a pairing of a Vera CPU — 88 custom dual-thread Arm cores reportedly based on Neoverse V3 — with a Rubin GPU package carrying two GPU dies that deliver 50 petaflops of FP4 inference performance per chip, with Rubin Ultra and Feynman planned as follow-on generations. Where those earlier descriptions emphasized inference throughput for agentic and reasoning workloads, Rubin HPC is positioned specifically around simulation and data-processing patterns such as sparse matrix operations, stencil computations, sorting and reductions.

## Why it matters

For teams planning HPC cluster refreshes, the concrete takeaway is timing rather than performance: a 2028 availability target means Rubin HPC cannot inform a 2026–2027 procurement, and the absence of memory, bandwidth and power specifications makes it impossible to size against current accelerators. The design detail that matters most for buyers is the emphasis on data movement and sparse-data throughput rather than raw compute alone — the bottleneck NVIDIA is naming is the irregular-access pattern behind sparse solvers, genomics and risk analytics, and customers should ask for evidence on those kernels rather than dense-FLOP numbers.

## What to watch

Watch for NVIDIA to publish memory capacity, bandwidth, power and pricing for Rubin HPC ahead of the stated 2028 availability, most likely at a future GTC or SC. The more decisive signal will be third-party benchmark results on sparse solvers and stencil codes, since none were included in the announcement.

## Further reading

- [Nvidia announces “ Rubin Ultra” and “Feynman” AI... - Ars Technica](https://arstechnica.com/ai/2025/03/nvidia-announces-rubin-ultra-and-feynman-ai-chips-for-2027-and-2028/)
- [Infrastructure for Scalable AI Reasoning | NVIDIA Vera Rubin Platform](https://www.nvidia.com/en-us/data-center/technologies/rubin/)
- [Nvidia works on Feynman GPU ..](https://www.eenewseurope.com/en/nvidia-works-on-feynman-gpu/)

{% endraw %}
