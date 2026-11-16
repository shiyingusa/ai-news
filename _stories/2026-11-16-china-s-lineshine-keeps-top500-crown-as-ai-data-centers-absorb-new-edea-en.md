---
layout: story
lang: en
date: 2026-11-16 06:00:00 -0500
issue: "2026-11-16"
story_id: "china-s-lineshine-keeps-top500-crown-as-ai-data-centers-absorb-new-edea"
permalink: "/2026/11/16/china-s-lineshine-keeps-top500-crown-as-ai-data-centers-absorb-new-edea/"
title: "China's LineShine keeps Top500 crown as AI data centers absorb new hardware"
dek: "China's LineShine remains the world's fastest supercomputer on the 68th Top500 list, published at SC26 in Chicago, sustaining 2.198 FP64 exaflops on the High Performance Linpack benchmark at 42.22 MW."
description: "China's LineShine remains the world's fastest supercomputer on the 68th Top500 list, published at SC26 in Chicago, sustaining 2.198 FP64 exaflops on the High Performance Linpack benchmark at 42.22 MW."
section: "chips-compute"
rank: 208
edition: 2
section_rank: 2
score: 7.0
status: "Released"
source_name: "Tom's Hardware"
source_url: "https://www.tomshardware.com/tech-industry/supercomputers/china-retains-fastest-supercomputer-in-the-world-crown-as-ai-data-centers-soak-up-new-hardware-top500-records-fewest-new-systems-in-33-years"
via: null
discussion_url: null
published_at: "2026-11-16T22:17:02+00:00"
tags: ["supercomputers", "Top500", "AI data centers", "HPC", "China"]
topics: ["supercomputers", "top500", "ai-data-centers", "hpc", "china"]
order: "20261116-2-991"
image: "/assets/stories/2026-11-16/china-s-lineshine-keeps-top500-crown-as-ai-data-centers-absorb-new-edea-share.jpg"
art: "/assets/stories/2026-11-16/china-s-lineshine-keeps-top500-crown-as-ai-data-centers-absorb-new-edea.jpg"
thumb: "/assets/stories/2026-11-16/china-s-lineshine-keeps-top500-crown-as-ai-data-centers-absorb-new-edea-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g6fa95f884118875b425c9bd78270394e50d995906d14446ce484fd3d923274e3a3cd64a0680cd438e58e53de929dc4b997315b6bd03cbbab95c732ca62f7430e_1280.jpg", "author": "cookieone", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/internet-information-service-system-8097838/", "provider": "Pixabay", "width": 6000, "height": 4000}
---

{% raw %}
<div class="story-lead" markdown="1">

China's LineShine remains the world's fastest supercomputer on the 68th Top500 list, published at SC26 in Chicago, sustaining 2.198 FP64 exaflops on the High Performance Linpack benchmark at 42.22 MW. The machine at the National Supercomputer Center in Shenzhen is CPU-only, built on the homegrown LingKun platform with 304-core Arm-based LX2 processors at 1.55 GHz (13,789,440 cores total) and a proprietary LingQi interconnect. Neither the top 10 nor the 10 most energy-efficient systems changed position since June, and only 27 machines (5.4%) are new entries — the fewest since the ranking began in 1993 — which the Top500 authors attribute to new hardware going to AI data centers rather than traditional supercomputers. Aggregate HPL performance rose 4.4% to 19.57 exaflops, while the entry threshold climbed 7.3% to 2.857 petaflops.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** According to the 68th Top500 list, released at SC26 in Chicago, China's LineShine at the National Supercomputer Center in Shenzhen remains No. 1 at 2.198 FP64 ExaFLOPS on the HPL benchmark at 42.22 MW, and the top 10 is unchanged since June. The list records only 27 new entrants (5.4%), the fewest since the project began in 1993, and aggregate HPL performance of 19.57 FP64 ExaFLOPS, up 4.4% in six months; the most powerful newcomer is South Korea's Hanggang, 12th at 342.6 PFLOPS.
- **Not yet confirmed:** The claim that AI data centers are absorbing the hardware is an interpretation resting on Epoch AI estimates cited by the list's authors — about 15 million H100-equivalents of installed global AI compute (Epoch AI, January) and five US hyperscalers holding roughly 71% of it as of Q4 2025 — not on a measured attribution of specific missing systems, and the article offers no figures on hardware diverted to AI clusters. All performance, core-count and power numbers come from the systems' Top500 submissions; the outlet reports no independent benchmark of LineShine, and no price or delivery details are given for any machine.

</div>

## Background

The Top500 is a twice-yearly ranking of supercomputers by sustained 64-bit floating-point (FP64) throughput on the High Performance Linpack (HPL) benchmark, a dense linear-algebra test rather than an AI workload. One exaflop equals 10^18 floating-point operations per second, so the exascale-class systems at the top are clustered around 1–2 exaflops. The list counts machines that are newly ranked, which is why a low number of entrants signals slowing replacement and expansion of traditional supercomputers, not a lack of total compute demand.

## Why it matters

For anyone sizing or buying HPC capacity, the list shows the bar for entry rising faster than total capacity: the cutoff for the 500th slot rose 7.3% in six months while aggregate performance grew 4.4%, and accelerator-equipped systems now number 291 of 500. LineShine's CPU-only design also gains just 3.6x from FP64 to mixed precision — well below accelerator-based exascale machines — so its lead is specific to double-precision scientific workloads rather than AI training, where the newer hardware is being deployed. Power efficiency is a separate gap: El Capitan reaches 1.809 FP64 exaflops at 29.69 MW versus LineShine's 2.198 exaflops at 42.22 MW, and Jupiter Booster at Jülich is the most efficient exascale system at 1.0 exaflops for 15.79 MW.

## What to watch

The next Top500 edition, which the project publishes twice a year at the ISC (June) and SC (November) conferences, will show whether the entry threshold keeps rising and whether any new exascale system displaces the unchanged top 10.

## Further reading

- [Five hyperscalers now own over two-thirds of global AI compute](https://epoch.ai/data-insights/hyperscalers-control-most-compute)
- [Global AI Compute Hits 15 Million H100 Equivalents as Nvidia ...](https://aihola.com/article/global-ai-compute-15-million-h100-equivalents-epoch-ai)

{% endraw %}
