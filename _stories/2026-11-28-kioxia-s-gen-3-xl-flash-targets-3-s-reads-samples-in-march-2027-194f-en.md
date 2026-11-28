---
layout: story
lang: en
date: 2026-11-28 06:26:22 -0500
issue: "2026-11-28"
story_id: "kioxia-s-gen-3-xl-flash-targets-3-s-reads-samples-in-march-2027-194f"
permalink: "/2026/11/28/kioxia-s-gen-3-xl-flash-targets-3-s-reads-samples-in-march-2027-194f/"
title: "Kioxia's Gen 3 XL-Flash targets 3 µs reads, samples in March 2027"
dek: "Kioxia has showcased a third-generation XL-Flash prototype that it says reaches 3 µs average read latency — less than 10% of the 40 µs of its BiCS8 TLC flash…"
description: "Kioxia has showcased a third-generation XL-Flash prototype that it says reaches 3 µs average read latency — less than 10% of the 40 µs of its BiCS8 TLC flash…"
section: "chips-compute"
rank: 8
edition: 0
section_rank: 4
score: 7.0
status: "Demonstrated"
source_name: "Tom's Hardware"
source_url: "https://www.tomshardware.com/pc-components/ssds/kioxias-3rd-gen-xl-flash-hits-optane-class-3-microsecond-read-latency-with-70-percent-higher-density-samples-march-2027-ahead-of-18-million-iops-gp2-ssds"
via: null
discussion_url: null
published_at: "2026-11-27T12:00:00+00:00"
tags: ["Kioxia", "XL-Flash", "NAND flash", "low-latency memory", "AI data centers"]
topics: ["kioxia", "xl-flash", "nand-flash", "low-latency-memory", "ai-data-centers"]
order: "20261128-0-991"
image: "/assets/stories/2026-11-28/kioxia-s-gen-3-xl-flash-targets-3-s-reads-samples-in-march-2027-194f-share.jpg"
art: "/assets/stories/2026-11-28/kioxia-s-gen-3-xl-flash-targets-3-s-reads-samples-in-march-2027-194f.jpg"
thumb: "/assets/stories/2026-11-28/kioxia-s-gen-3-xl-flash-targets-3-s-reads-samples-in-march-2027-194f-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g6be9a8edb356fe5fe799d0532071aadc1114da8a940629c4272975d38643c16545ee929111de1ad7c58ee8b3298b279b74f8b512926fc68c8154337680396392_1280.jpg", "author": "_SDR_", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/usb-flash-flash-drive-flash-7468224/", "provider": "Pixabay", "width": 4288, "height": 2848}
---

{% raw %}
<div class="story-lead" markdown="1">

Kioxia has showcased a third-generation XL-Flash prototype that it says reaches 3 µs average read latency — less than 10% of the 40 µs of its BiCS8 TLC flash — while delivering 70% higher bit density and about 135% better efficiency than Gen 2 through CBA wafer bonding. The low-latency NAND is aimed at a memory tier between DRAM and conventional flash in AI servers and data centers, a role Intel's Optane once targeted.

Kioxia named its GP2 enterprise SSD as the first product to use the flash, with claimed ratings above 18 million 512-byte random-read IOPS, up to 28 GB/s sequential reads over PCIe 6.0 x4 and up to 50 drive writes per day. XL-Flash samples are due to select customers by the end of Q1 2027, while GP2 evaluation samples are promised only by the end of 2027; the figures are vendor claims for a prototype and the drive's exact specifications may change.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** Kioxia showcased the Gen 3 XL-Flash prototype at its KIOXIA Forum in Tokyo and states that it uses CBA bonding, delivers 3 µs average read latency, 70% higher bit density and roughly 135% better efficiency than Gen 2; it named GP2 as the first product to use it.
- **Not yet confirmed:** independent measurements of latency, IOPS or endurance; the SLC cell type, 128Gb die size, 150,000–250,000 P/E cycles and 4.8 Gb/s interface are reported details, and Kioxia has not disclosed layer count; GP2's 18 million+ IOPS, 28 GB/s sequential read and 50 DWPD figures are targets, with exact specifications subject to change.

</div>

## Background

XL-Flash is Kioxia's storage-class memory: NAND tuned for low read latency and high write endurance rather than cheap capacity, so it can sit between DRAM and ordinary flash. The first generation arrived in 2019 with single-level cells (SLC, one bit per cell) and sub-5 µs reads, and the 2022 second generation added a two-bit MLC option that traded some like-for-like performance for lower cost per bit. The memory tier it targets was left open when Intel wound down Optane, its 3D XPoint-based rival, in 2022.

## Why it matters

Teams designing AI-server memory hierarchies should not plan procurement around GP2 yet: XL-Flash samples arrive in Q1 2027 and GP2 evaluation samples only at the end of 2027, so the drive cannot address current HBM or DRAM capacity pressure. If the 512-byte-read performance holds, storage and model-serving software will need to issue and schedule small I/Os, rather than the usual 4KB accesses, to capture the benefit.

## What to watch

Watch whether Kioxia ships XL-Flash Gen 3 samples to select customers by the end of Q1 2027 and GP2 evaluation samples by the end of 2027, and whether independent tests reproduce the 3 µs latency and above-18-million-IOPS claims.

{% endraw %}
