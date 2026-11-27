---
layout: story
lang: en
date: 2026-11-23 13:27:17 -0500
issue: "2026-11-23"
story_id: "penguin-demos-photonic-memory-appliance-with-576gb-hbm3e-over-optical-250a"
permalink: "/2026/11/23/penguin-demos-photonic-memory-appliance-with-576gb-hbm3e-over-optical-250a/"
title: "Penguin demos photonic memory appliance with 576GB HBM3E over optical CXL at SC26"
dek: "Penguin Solutions demonstrated a MemoryAI Photonic Appliance at SC26 that adds up to 576 GB of HBM3E and 16 TB of DDR5 to AI systems over optical CXL.mem 3.1 links, targeting the memory-capacity limit of AI accelerators."
description: "Penguin Solutions demonstrated a MemoryAI Photonic Appliance at SC26 that adds up to 576 GB of HBM3E and 16 TB of DDR5 to AI systems over optical CXL.mem 3.1 links, targeting the memory-capacity limit of AI accelerators."
section: "chips-compute"
rank: 11
edition: 0
section_rank: 1
score: 7.0
status: "Demonstrated"
source_name: "Tom's Hardware"
source_url: "https://www.tomshardware.com/pc-components/dram/penguin-shows-off-photonic-memory-box-at-sc26-that-can-expand-ai-accelerator-capacity-over-optical-links-device-sports-up-to-576gb-of-hbm3e-customer-samples-expected-in-2027"
via: null
discussion_url: null
published_at: "2026-11-23T18:00:00+00:00"
tags: ["photonic memory", "HBM3E", "CXL", "AI accelerators", "optical interconnects"]
topics: ["photonic-memory", "hbm3e", "cxl", "ai-accelerators", "optical-interconnects"]
order: "20261123-0-988"
image: "/assets/stories/2026-11-23/penguin-demos-photonic-memory-appliance-with-576gb-hbm3e-over-optical-250a-share.jpg"
art: "/assets/stories/2026-11-23/penguin-demos-photonic-memory-appliance-with-576gb-hbm3e-over-optical-250a.jpg"
thumb: "/assets/stories/2026-11-23/penguin-demos-photonic-memory-appliance-with-576gb-hbm3e-over-optical-250a-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g6bfe2d1092857576dd1009aa756611a1948bcb9cd76032f80bf16f35af5ad0d0e1c7c59763a4554fb8e4ce02bc85679daf096c3242bef8ce448b3217d9a29945_1280.jpg", "author": "Bru-nO", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/fiber-optic-light-waveguide-4393369/", "provider": "Pixabay", "width": 6000, "height": 4000}
---

{% raw %}
<div class="story-lead" markdown="1">

Penguin Solutions demonstrated a MemoryAI Photonic Appliance at SC26 that adds up to 576 GB of HBM3E and 16 TB of DDR5 to AI systems over optical CXL.mem 3.1 links, targeting the memory-capacity limit of AI accelerators. The box is built from eight of Marvell's Photonic Fabric Memory Modules — each with 72 GB of HBM3E cache and a photonic interposer with 16 transmit and 16 receive channels — for an aggregate bidirectional bandwidth target of 7.2 TB/s, or about 3.6 TB/s in each direction.

It supports HBM Direct, HBM-plus-DDR5 cached, and DDR5 Direct modes, and can connect hosts up to 30 meters away. Customer samples are not expected until the second half of 2027, and the appliance delivers full benefit only to hosts that support CXL.mem or integrate Marvell's photonic chiplet, since Nvidia and AMD data-center GPUs generally lack a general-purpose CXL.mem host interface.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** Penguin Solutions showed the MemoryAI Photonic Appliance at SC26 with up to 576 GB of HBM3E plus 16 TB of DDR5, a 7.2 TB/s aggregate bandwidth target, CXL.mem 3.1 over optical links, and customer samples slated for the second half of 2027, according to Tom's Hardware's report from the show.
- **Not yet confirmed:** Actual application performance, the claim of transparent access without application changes, the sub-350ns PF-NIC and sub-200ns chiplet latency figures (which exclude PCIe/CXL overhead), pricing, and where Penguin will source HBM3E in volume around 2028 as the industry moves to HBM4.

</div>

## Background

CXL (Compute Express Link) is an open interconnect standard that lets a processor address memory residing outside its own package as a coherent extension of its own address space; the CXL.mem protocol is the part of the spec that carries those memory reads and writes. HBM3E is the current generation of high-bandwidth memory — DRAM stacked in layers beside an AI accelerator — and its fixed per-chip capacity is one reason developers add or replace accelerators when a model outgrows it. Penguin's appliance is built on Marvell's Photonic Fabric, in which memory modules carry a photonic interposer and connect to hosts over optical links rather than copper.

## Why it matters

System designers evaluating the appliance should first confirm host support: Nvidia and AMD data-center GPUs do not generally expose a CXL.mem host interface, so the full-capacity benefit is limited to CXL-capable CPUs, custom XPUs with Marvell's chiplet, or future accelerators. Even on supported hosts, the 7.2 TB/s is shared across as many as eight accelerators, and Penguin's transparent-access claim depends on memory-management software that treats the external pool as another memory tier.

## What to watch

Customer samples are scheduled for the second half of 2027; watch whether Penguin names host platforms or accelerator partners that support CXL.mem, and whether benchmarks show a gain over simply adding accelerators.

{% endraw %}
