---
layout: story
lang: zh
date: 2026-11-27 04:00:00 -0500
issue: "2026-11-26"
story_id: "explainer-hbm-memory"
permalink: "/zh/explainers/hbm-high-bandwidth-memory/"
title: "AI 芯片的瓶颈其实在内存：一文看懂 HBM"
dek: "高带宽内存（HBM）决定了大模型回答问题有多快。HBM 是什么、为什么新一代 GPU 装得越来越多、为什么只有三家公司能造？"
description: "高带宽内存（HBM）决定了大模型回答问题有多快：HBM 是什么、为什么新 GPU 装得越来越多、谁在生产。"
section: "tech-blog"
rank: 290
edition: 2
section_rank: 1
score: null
status: "Explainer"
kind: explainer
source_name: "JEDEC"
source_url: "https://www.hpcwire.com/?p=179974"
via: null
discussion_url: null
published_at: null
tags: ["HBM", "英伟达", "存储芯片", "SK 海力士", "三星"]
topics: ["hbm", "nvidia", "memory-chips", "sk-hynix", "samsung"]
order: "20261126-2-990"
image: null
art: null
thumb: null
photo_query: ["High Bandwidth Memory", "HBM memory stack", "DRAM wafer"]
photo_credit: null
---

{% raw %}
<div class="story-lead" markdown="1">

说到 AI 芯片短缺，大家通常想到的是 GPU。但每一块 AI 加速器里，还有一个同样紧缺、而且常常决定模型实际跑多快的部件：高带宽内存，也就是 HBM。

这篇解读讲三件事：HBM 是什么，为什么每一代 GPU 都装得更多，以及为什么它的供应集中在三家公司手里。

</div>

## HBM 是什么

普通电脑内存是一根根内存条，离处理器有一段距离。HBM 的做法不同：把几颗 DRAM 芯片竖着叠起来，用穿过硅片的微小通道连在一起，再和 GPU 放在同一个封装里。比如英伟达 B200 的 HBM3E 就和 GPU 封装在一起。

这样设计是为了"宽"。每一叠 HBM3E 通过 1024 位的接口和处理器相连，带宽超过每秒 1.2 TB。显卡内存总线的宽度只有它的一小部分。

## 为什么 AI 模型这么需要它

训练模型主要是算术运算，回答问题则不一样。大模型生成文字时一次只出一个词元（token），每出一个都要从内存里读出大量权重。这个阶段叫"解码"，速度通常卡在数据搬运上，而不是芯片算得多快。SemiAnalysis 的分析师就把这种受内存带宽限制的状态称为大模型解码的主要瓶颈。

所以现在 GPU 发布时，内存参数总是排在最前面。据 IEEE Spectrum 报道，英伟达 B200 配备 192 GB HBM3E、带宽每秒 8 TB，上一代 H200 是 141 GB、每秒 4.8 TB。容量越大，一块芯片能装下的模型越大、能同时服务的对话越多；带宽越高，每个回答出来得越快。

## HBM4 带来什么变化

行业标准组织 JEDEC 在 2025 年 4 月发布了 HBM4 标准（JESD270-4）。每叠接口宽度翻倍到 2048 位，每个引脚最高 8 Gb/s，每叠带宽最高每秒 2 TB；独立通道数从 16 个翻倍到 32 个。用 32 Gb 芯片叠 16 层，一叠就有 64 GB。

简单说：下一代加速器用同样数量的内存叠层能拿到更高带宽，或者用更少的叠层拿到同样带宽，省下的封装面积可以留给计算单元。

## 为什么供应紧张

能大规模生产 HBM 的只有三家：SK 海力士、三星和美光。把十几片很薄的 DRAM 叠起来再连通，比做普通内存难得多；每一叠还要和 GPU 封装在一起，这又多了一个可能卡产能的环节。

三家的格局正在变化。Counterpoint Research 的数据显示，2026 年第二季度 SK 海力士的 HBM 营收份额为 50%，一年前是 64%；三星 33%，美光 18%。TrendForce 2026 年 6 月报告称，三星率先完成 HBM4 验证并开始为英伟达 Rubin 平台出货，SK 海力士的 HBM4 量产则推迟到第三季度。

## 后续看什么

想判断 AI 硬件往哪走，可以盯三件事。第一，每款新加速器参数表里的内存一栏：每块芯片的容量和带宽，现在和算力一样重要。第二，每个 GPU 平台最终选了哪家供应商，一次认证结果就能让市场份额一个季度变动十几个百分点。第三，2027 年 HBM4 的出货量，它决定下一代加速器实际能交付多少。

## 延伸阅读

- [JEDEC releases HBM4 standard (HPCwire, press release)](https://www.hpcwire.com/?p=179974)
- [JEDEC officially releases HBM4 memory standard (All About Circuits)](https://www.allaboutcircuits.com/news/jedec-officially-releases-hbm4-memory-standard)
- [HBM3e and HBM4 IC design guide (Siemens)](https://blogs.sw.siemens.com/semiconductor-packaging/2026/04/24/hbm3e-hbm4-ic-design-guide/)
- [Nvidia Blackwell (IEEE Spectrum)](https://spectrum.ieee.org/nvidia-blackwell)
- [Blackwell B200 memory and NVLink (Cornell Virtual Workshop)](https://cvw.cac.cornell.edu/gpu-architecture/horizon-gpus-blackwell-b200/b200_mem_nvlink5)
- [NVIDIA B200 (SemiAnalysis InferenceX)](https://inferencex.semianalysis.com/chips/b200)
- [Global DRAM and HBM market share (Counterpoint Research)](https://counterpointresearch.com/insights/global-dram-and-hbm-market-share)
- [HBM Market Bulletin, June 23, 2026 (TrendForce)](https://www.trendforce.com/research/download/RP260623IP3)

{% endraw %}
