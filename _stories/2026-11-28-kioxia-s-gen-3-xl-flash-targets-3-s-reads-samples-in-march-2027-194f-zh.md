---
layout: story
lang: zh
date: 2026-11-28 06:28:04 -0500
issue: "2026-11-28"
story_id: "kioxia-s-gen-3-xl-flash-targets-3-s-reads-samples-in-march-2027-194f"
permalink: "/zh/2026/11/28/kioxia-s-gen-3-xl-flash-targets-3-s-reads-samples-in-march-2027-194f/"
title: "铠侠第三代 XL-Flash 原型读取延迟达 3 微秒，2027 年 3 月送样"
dek: "铠侠（Kioxia）在东京 KIOXIA Forum 上展出了第三代 XL-Flash 低延迟闪存原型：平均读取延迟 3 微秒，不到自家 BiCS8 TLC（40 微秒）的十分之一；位密度比第二代高 70%…"
description: "铠侠（Kioxia）在东京 KIOXIA Forum 上展出了第三代 XL-Flash 低延迟闪存原型：平均读取延迟 3 微秒，不到自家 BiCS8 TLC（40 微秒）的十分之一；位密度比第二代高 70%…"
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

铠侠（Kioxia）在东京 KIOXIA Forum 上展出了第三代 XL-Flash 低延迟闪存原型：平均读取延迟 3 微秒，不到自家 BiCS8 TLC（40 微秒）的十分之一；位密度比第二代高 70%，并采用 CBA（CMOS 直接键合到阵列）把逻辑晶圆与存储单元晶圆分开制造后再键合，铠侠称其能效因此比第二代提升约 135%。第一批样品计划在 2027 年 3 月提供给特定客户；首个使用该闪存的产品是面向 AI 服务器与数据中心的 GP2 企业级 SSD，标称 512 字节随机读超过 1800 万 IOPS、顺序读最高 28 GB/s，前提是能跑满 PCIe 6.0 x4。

这与英特尔 2022 年退出的 Optane 定位相似，但 GP2 的评估样品要到 2027 年底才发给特定客户，最终规格可能变化；铠侠也未公布层数等完整参数。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** 铠侠在自家论坛上展出了第三代 XL-Flash 原型，并公布 3 微秒平均读取延迟、较第二代高 70% 的位密度、CBA 键合结构，以及 2027 年 3 月向特定客户送样的计划；GP2 标称 512 字节随机读超过 1800 万 IOPS、顺序读最高 28 GB/s、最高每日 50 次全盘写入，铠侠称正考虑 E1.S 与 E3.S 形态并支持直接液冷。
- **尚未证实：** SLC 存储单元与 128Gb 单 die 容量在报道中均标注为“据称”，150000 至 250000 次 P/E 循环、4.8 Gb/s 接口速率亦出自铠侠自身说法，没有第三方实测；层数等完整规格未披露，GP2 最终规格可能变动，价格、容量和具体上市时间均未公布，评估样品要等到 2027 年底。

</div>

## 背景

XL-Flash 是铠侠基于 BiCS 闪存工艺、针对低读取延迟和高写入寿命调优的 SLC 闪存，定位为介于 DRAM 与普通 NAND 之间的“存储级内存”层级。该系列第一代于 2019 年推出，读取延迟低于 5 微秒；2022 年的第二代增加了 2-bit MLC 选项，以部分同代性能换取更低的单位容量成本。英特尔曾以 3D XPoint 材质的 Optane 占据这一层级，但已于 2022 年彻底退出该业务，留下了低延迟内存层级的空缺。

## 为什么重要

对想给 GPU 的 HBM 之外再挂一层低成本内存的 AI 服务器设计者来说，XL-Flash 是目前少有的、不依赖已停产 Optane 的存储级内存（SCM）路线；GP2 瞄准 512 字节而非常见的 4KB 访问粒度，正好对应铠侠所说 AI 负载中大量细粒度内存查询的模式。但送样在 2027 年 3 月、GP2 评估样品在 2027 年底，现在采购的机器无法受益；规划 2027 年平台时需要同步评估 E1.S/E3.S 盘位与直接液冷的兼容性。

## 后续看点

2027 年 3 月首批 XL-Flash 样品能否按期交付，以及 2027 年底 GP2 评估样品给出的最终规格。铠侠与英伟达还在合作推进后续 GP 系列，目标最高 1 亿随机读 IOPS。

{% endraw %}
