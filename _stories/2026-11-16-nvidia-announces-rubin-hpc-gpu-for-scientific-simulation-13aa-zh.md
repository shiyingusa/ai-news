---
layout: story
lang: zh
date: 2026-11-16 06:00:00 -0500
issue: "2026-11-16"
story_id: "nvidia-announces-rubin-hpc-gpu-for-scientific-simulation-13aa"
permalink: "/zh/2026/11/16/nvidia-announces-rubin-hpc-gpu-for-scientific-simulation-13aa/"
title: "英伟达发布 Rubin HPC GPU：逾 5 万 CUDA 核心，预计 2028 年上市"
dek: "英伟达在 SC26 大会上发布 Rubin HPC，这是 Vera Rubin 平台中面向科学计算的新款 GPU，主攻气候模拟、工程仿真、基因组分析和金融风险等仿真与数据处理负载。"
description: "英伟达在 SC26 大会上发布 Rubin HPC，这是 Vera Rubin 平台中面向科学计算的新款 GPU，主攻气候模拟、工程仿真、基因组分析和金融风险等仿真与数据处理负载。"
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
photo_credit: {"url": "https://pixabay.com/get/g9053a1c3bbef449a7362f898ecdb2080c40f227b9baf1a45223a5fa2bea5752efd86eb63efe9b99283775193b12416e81f7d9c706b8b2b98aea00cc9df8034f6_1280.jpg", "author": "blickpixel", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/it-server-server-cabinet-network-838384/", "provider": "Pixabay", "width": 2682, "height": 1788}
---

{% raw %}
<div class="story-lead" markdown="1">

英伟达在 SC26 大会上发布 Rubin HPC，这是 Vera Rubin 平台中面向科学计算的新款 GPU，主攻气候模拟、工程仿真、基因组分析和金融风险等仿真与数据处理负载。官方给出的关键规格是单颗 GPU 超过 5 万个 CUDA 核心（英伟达称其为纪录），并配有稀疏数据加速能力和第七代 NVLink GPU 互连；英伟达强调这是“计算与数据搬运同步扩展”的均衡设计，让这些核心不至于空等数据。不过该产品目前只是发布，官方写明“预计 2028 年上市”，未公布价格、完整规格，也没有第三方性能数据。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** 英伟达官方博客称 Rubin HPC 属于 Vera Rubin 平台、在 SC26 发布、单 GPU CUDA 核心数超过 5 万个、具备稀疏数据加速与第七代 NVLink，并写明预计 2028 年上市。
- **尚未证实：** 相比上一代产品的实际性能提升幅度、价格、完整规格与功耗，均无数据；所有性能表述都来自英伟达自己的说法，没有独立测试或客户实测。

</div>

## 背景

Vera Rubin 是 NVIDIA 在 2025 年 3 月的 GTC 上公布的下一代数据中心平台：把自研的 Vera CPU 与 Rubin GPU 组合在一起，并给出了延伸到 2027 年 Rubin Ultra、2028 年 Feynman 的路线图。当时公开的 Rubin 规格侧重 AI 推理性能（每颗芯片 50 petaflops 的 FP4 算力），而这次发布的 Rubin HPC 是同一平台下针对科学计算与数据分析的分支，强调 CUDA 核心数量、稀疏数据加速与第七代 NVLink 互联的配合。

## 为什么重要

对高性能计算采购方和科学计算软件开发者来说，这条消息的实际意义是路线图而非当下选项：2028 年才上市意味着现有集群的升级周期需要按这个时间表规划。英伟达同时强调 CUDA-X 库已针对稀疏矩阵、模板计算、排序与归约等仿真常见模式做了优化，这暗示现有 CUDA 代码有望直接受益，而不必重写；但在没有独立基准测试前，加速幅度无法评估。

## 后续看点

关注英伟达在 2028 年上市前是否公布 Rubin HPC 的完整规格（功耗、显存容量与带宽、具体 SKU）以及第三方或客户实测的仿真负载性能数据。

## 延伸阅读

- [Nvidia announces “ Rubin Ultra” and “Feynman” AI... - Ars Technica](https://arstechnica.com/ai/2025/03/nvidia-announces-rubin-ultra-and-feynman-ai-chips-for-2027-and-2028/)
- [Nvidia works on Feynman GPU ..](https://www.eenewseurope.com/en/nvidia-works-on-feynman-gpu/)

{% endraw %}
