---
layout: story
lang: zh
date: 2026-11-23 13:28:10 -0500
issue: "2026-11-23"
story_id: "penguin-demos-photonic-memory-appliance-with-576gb-hbm3e-over-optical-250a"
permalink: "/zh/2026/11/23/penguin-demos-photonic-memory-appliance-with-576gb-hbm3e-over-optical-250a/"
title: "Penguin 展出光子外置内存：最高 576GB HBM3E，2027 下半年送样"
dek: "Penguin Solutions 在 SC26 超算展上展出了 MemoryAI Photonic Appliance…"
description: "Penguin Solutions 在 SC26 超算展上展出了 MemoryAI Photonic Appliance…"
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

Penguin Solutions 在 SC26 超算展上展出了 MemoryAI Photonic Appliance——一台通过光纤链路挂在主机之外的 AI 内存扩展设备：最高 576GB HBM3E 加 16TB DDR5，整机聚合带宽目标 7.2 TB/s（双向各约 3.6 TB/s），走 CXL.mem 3.1 协议、最远 30 米。它基于 Marvell 的 Photonic Fabric 架构，用 8 个 Photonic Fabric 内存模块（PFMM），每模块含 72GB HBM3E 缓存和一个 16 发 16 收、每通道 224 Gbps 的光互连中介层；主机侧可选 PCIe 6.0/CXL 3.1 的光子网卡（PF-NIC，单口最高 2 Tbps、延迟低于 350ns，不含 PCIe/CXL 开销），或把光子 chiplet 直接集成进 XPU（最高 14.4 Tbps、延迟低于 200ns）。

Penguin 称应用无需修改即可透明访问外部内存，但客户样品要到 2027 年下半年，且目前没有任何实测性能数据。一个关键限制是：Nvidia 与 AMD 的数据中心 GPU 普遍不支持通用 CXL.mem 主机接口，因此这套方案现阶段只能服务支持 CXL.mem 的 CPU、定制 XPU 或集成 Marvell 光子 chiplet 的加速器。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** Penguin Solutions 在 SC26 展出了该设备，Tom's Hardware 报道其 576GB HBM3E／16TB DDR5 容量、7.2 TB/s 聚合带宽目标、三种内存访问模式（HBM 直连、HBM 作 DDR5 写穿缓存、DDR5 直连）以及基于 Marvell PFMM 与 PF-NIC 的架构细节。
- **尚未证实：** 透明访问无需改应用、低于 350ns／200ns 的延迟（前者尚未计入 PCIe/CXL 开销）、2027 年下半年送样能否如期，以及多加速器共享后每张卡实际分到多少带宽——这些均无独立测试或第三方验证。

</div>

## 背景

HBM（高带宽内存）是直接封装在 AI 加速器旁的堆叠内存，容量有限，往往成为运行大模型时的硬瓶颈；过去开发者只能通过增加或更换加速器来扩充内存。CXL 是基于 PCIe 的互连标准，其 CXL.mem 子协议允许处理器用普通的 load/store 指令访问外部内存，把远端内存当作本地内存的一个层级使用，CPU 已普遍支持这一扩展方式。Penguin 的方案在此之上叠加了 Marvell 的光子互连，把外部内存池的访问距离延伸到最长 30 米。

## 为什么重要

对采购者而言，真正决定能否用的是主机兼容性而非容量：由于主流 Nvidia、AMD GPU 不支持通用 CXL.mem，现有集群无法直接受益；若绕道支持 CXL.mem 的 CPU 访问，延迟将远超宣传的 350ns，可能吃掉扩容带来的收益。有兴趣的团队应优先确认目标主机是否在硬件与内存管理软件两层支持外部内存映射，并等待实测数据。

## 后续看点

2027 年下半年客户样品是否如期交付，以及届时 Penguin 与 Marvell 是否公布实测延迟、八卡分摊后的单卡带宽和支持主机清单。另一个悬而未决的问题是：2028 年行业转向 HBM4／HBM4E 后，Penguin 计划从哪里获得 HBM3E 的批量供应。

{% endraw %}
