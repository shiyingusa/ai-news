---
layout: story
lang: zh
date: 2026-11-25 06:30:31 -0500
issue: "2026-11-25"
story_id: "shared-cxl-memory-test-finds-35s-software-lock-overhead-f9ea"
permalink: "/zh/2026/11/25/shared-cxl-memory-test-finds-35s-software-lock-overhead-f9ea/"
title: "四台服务器共享 CXL 内存：软件锁开销 3–5 微秒，Tom's Hardware 报道"
dek: "得克萨斯大学阿灵顿分校与英特尔的研究人员在 SC26 上报告了四台服务器共享一个 CXL 内存池的实测：四台 86 核英特尔至强 6787P 服务器（各 256GB DRAM）通过 PCIe 5.0 连接同一台 CXL 内存箱…"
description: "得克萨斯大学阿灵顿分校与英特尔的研究人员在 SC26 上报告了四台服务器共享一个 CXL 内存池的实测：四台 86 核英特尔至强 6787P 服务器（各 256GB DRAM）通过 PCIe 5.0 连接同一台 CXL 内存箱…"
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

得克萨斯大学阿灵顿分校与英特尔的研究人员在 SC26 上报告了四台服务器共享一个 CXL 内存池的实测：四台 86 核英特尔至强 6787P 服务器（各 256GB DRAM）通过 PCIe 5.0 连接同一台 CXL 内存箱，而该平台没有跨主机缓存一致性和硬件原子操作。锁因此只能由软件用普通读写和显式刷新实现，每次加锁带来 3–5 微秒开销；无争用时锁延迟中位数为 3.7 微秒，多台服务器争用同一把锁时第 95 百分位达 132 微秒。广度优先搜索（BFS）从一台增至四台反而由 0.55 秒增至 0.74 秒，三角形计数耗时从 2.43 秒降至 0.97 秒，哈希表吞吐从 410 万次/秒升至 1660 万次/秒，表明池化收益高度依赖访问模式。研究人员称其交换机仅支持四台服务器，CXL 3.0 的 Back-Invalidate 硬件修复尚未获得厂商确认；这直接影响把 CXL 池用于 AI KV cache 的部署评估，SK 海力士和 Micron 虽在 SC26 展示了池化设计并给出性能提升声明，但四机实测显示跨主机同步频繁的负载不会自动随服务器数量扩展。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** 据 Tom's Hardware 对 SC26 展示的报道，UT Arlington 与英特尔研究人员在四台至强 6787P 服务器加一台 CXL 内存箱的真实硬件上测得每次软件锁 3–5 微秒开销，并报告 BFS、三角形计数和哈希表的具体扩展数据。
- **尚未证实：** 该测试的完整方法、原始数据和独立复现结果尚未公开；CXL 3.0 Back-Invalidate 是否受其平台支持仍未获厂商确认；SK 海力士的 2.6 倍首 token 时间、3.0 倍 P99 延迟改善和 Micron 的 10–30 倍代理式 AI 提升均为厂商声明，未见独立验证。

</div>

## 背景

CXL（Compute Express Link）是建立在 PCIe 之上的互联标准，让服务器在自身内存插槽之外挂接共享内存池，从而突破单机 DRAM 容量上限；本次测试即用四台 Xeon 6787P 服务器经 PCIe 5.0 共享一个 CXL 内存机箱。难点在缓存一致性：同一台服务器内，CPU 硬件会自动同步各核缓存并完成原子操作，而跨主机的 CXL 共享池没有这层硬件保障，锁和数据刷新只能由软件用普通读写实现，这正是 3–5 微秒开销的来源；CXL 3.0 规范中的 Back-Invalidate 机制本可在硬件层解决缓存问题，但研究者未获厂商确认其平台支持该功能。同类产品正在密集出现：11 月 23 日的日报曾报道 Penguin Solutions 在 SC26 展示光互连内存机箱，可通过 Optical CXL 3.1 为 AI 系统增加最高 576GB HBM3E 和 16TB DDR5，说明硬件供给已先行，而跨主机软件路径的实际代价才刚开始被量化。

## 为什么重要

对计划用 CXL 内存池扩展 AI KV cache 或图分析内存的团队，这次实测给出的直接约束是：按桶或分片独立访问、写少读多的负载（如哈希表）能随主机数扩展，而频繁跨主机同步的负载（如 BFS）可能越加机器越慢。部署前应确认平台是否支持 CXL 3.0 的 Back-Invalidate 和硬件原子操作；若只能依赖软件锁，需把每锁 3–5 微秒的开销和争用时 132 微秒级的尾部延迟计入容量与延迟预算。

## 后续看点

后续可核对交换机或服务器厂商是否正式确认该四主机平台支持 CXL 3.0 Back-Invalidate 与硬件原子操作，以及是否有独立团队复现这组四机共享内存基准。

## 延伸阅读

- [2026-11-23 — Penguin demos photonic memory appliance with 576GB HBM3E over optical CXL at SC26](https://www.tomshardware.com/pc-components/dram/penguin-shows-off-photonic-memory-box-at-sc26-that-can-expand-ai-accelerator-capacity-over-optical-links-device-sports-up-to-576gb-of-hbm3e-customer-samples-expected-in-2027)

{% endraw %}
