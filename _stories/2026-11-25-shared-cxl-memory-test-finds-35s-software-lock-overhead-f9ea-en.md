---
layout: story
lang: en
date: 2026-11-25 06:28:57 -0500
issue: "2026-11-25"
story_id: "shared-cxl-memory-test-finds-35s-software-lock-overhead-f9ea"
permalink: "/2026/11/25/shared-cxl-memory-test-finds-35s-software-lock-overhead-f9ea/"
title: "Shared CXL memory test finds 3–5µs software lock overhead"
dek: "A real-hardware four-server CXL test by UT Arlington and Intel researchers has quantified the software tax on shared memory pools: because the hardware lacks cross-host cache coherence and atomics…"
description: "A real-hardware four-server CXL test by UT Arlington and Intel researchers has quantified the software tax on shared memory pools: because the hardware lacks cross-host cache coherence and atomics…"
section: "chips-compute"
rank: 7
edition: 0
section_rank: 1
score: 7.0
status: "Demonstrated"
source_name: "Tom's Hardware"
source_url: "https://www.tomshardware.com/pc-components/dram/shared-cxl-memory-pools-come-with-steep-software-tax-that-could-stall-multi-server-scaling-ut-arlington-shares-real-world-test-that-measured-four-servers-sharing-the-same-pool-at-sc26"
via: null
discussion_url: null
published_at: "2026-11-24T11:30:00+00:00"
tags: ["CXL memory", "data center memory", "AI KV cache", "server scaling", "hardware-software co-design"]
topics: ["cxl-memory", "data-center-memory", "ai-kv-cache", "server-scaling", "hardware-software-co-design"]
order: "20261125-0-992"
image: "/assets/stories/2026-11-25/shared-cxl-memory-test-finds-35s-software-lock-overhead-f9ea-share.jpg"
art: "/assets/stories/2026-11-25/shared-cxl-memory-test-finds-35s-software-lock-overhead-f9ea.jpg"
thumb: "/assets/stories/2026-11-25/shared-cxl-memory-test-finds-35s-software-lock-overhead-f9ea-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g343571a038390c62a29b6665f7c547dbdb5af870d522bb12aa109add7a848fedd076bfe15059f333b3f86e6153a80597f1a3e5265ab0b472a2156eb3418aa1f4_1280.jpg", "author": "FreePhotosART", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/information-data-disk-server-1641937/", "provider": "Pixabay", "width": 3450, "height": 2300}
---

{% raw %}
<div class="story-lead" markdown="1">

A real-hardware four-server CXL test by UT Arlington and Intel researchers has quantified the software tax on shared memory pools: because the hardware lacks cross-host cache coherence and atomics, software-enforced locks add 3–5 µs per lock, roughly an order of magnitude above local hardware spin locks. In the SC26 presentation, breadth-first search was 35% slower on four servers than on one (0.74 s versus 0.55 s), while workloads partitioned to avoid shared state scaled—a 95%-read hash table rose from 4.1M to 16.6M ops/s and triangle counting fell from 2.43 s to 0.97 s.

The setup used four 86-core Intel Xeon 6787P servers with 256 GB DRAM each, linked over PCIe 5.0 to one CXL memory box; the switch caps the pool at four hosts, and the researchers had no vendor confirmation that the platform supports CXL 3.0's Back-Invalidate coherence feature.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** The four-server CXL measurements come from a UT Arlington and Intel SC26 presentation reported by Tom's Hardware, using four 86-core Xeon 6787P servers connected over PCIe 5.0 to one CXL memory box; the reported lock overhead, BFS slowdown, and scaling results are the researchers' own figures.
- **Not yet confirmed:** Whether the tested switch supports CXL 3.0 Back-Invalidate (the researchers had no vendor confirmation), whether the four-host cap reflects other commercially available CXL switches, and the separate SK hynix and Micron KV-cache speedups, which are vendor claims not independently measured here.

</div>

## Background

CXL (Compute Express Link) is a PCIe-based interconnect that lets a server attach memory outside its own DIMM slots — up to 16 TB in a single box — and CXL 3.0 adds fabric features intended to let several hosts share one pool. The catch is coherence: CXL 3.0's Back-Invalidate mechanism is meant to keep cached copies consistent across hosts, but as the researchers note, they had no vendor confirmation their platform implements it, so locks must be built in software instead. AI Daily Radar's November 23 digest covered a related SC26 announcement from Penguin Solutions, whose optical CXL appliance adds up to 576 GB of HBM3E and 16 TB of DDR5 to a single AI system, with customer samples expected in 2027; the UT Arlington and Intel test instead probes the harder case of four separate servers contending for one shared pool.

## Why it matters

Developers evaluating CXL pools for multi-server workloads should expect shared-state code—cross-host locks, graph traversal, and fine-grained synchronization—to lose the scaling benefit, while per-host partitioned data such as independent hash buckets can still scale nearly linearly. For KV-cache pooling, the write-once, read-many access pattern is more favorable, but the 3–5 µs lock cost remains a constraint until hardware coherence is confirmed.

## What to watch

Watch for vendor confirmation that shipping CXL 3.0 switches support Back-Invalidate, and for independent benchmarks of SK hynix's and Micron's KV-cache pooling designs rather than vendor-reported speedups.

## Further reading

- [2026-11-23 — Penguin demos photonic memory appliance with 576GB HBM3E over optical CXL at SC26](https://www.tomshardware.com/pc-components/dram/penguin-shows-off-photonic-memory-box-at-sc26-that-can-expand-ai-accelerator-capacity-over-optical-links-device-sports-up-to-576gb-of-hbm3e-customer-samples-expected-in-2027)

{% endraw %}
