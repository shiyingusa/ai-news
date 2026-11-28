---
layout: story
lang: zh
date: 2026-11-28 06:28:04 -0500
issue: "2026-11-28"
story_id: "semianalysis-benchmarks-aws-trainium3-claims-best-inference-cost-per-e779"
permalink: "/zh/2026/11/28/semianalysis-benchmarks-aws-trainium3-claims-best-inference-cost-per-e779/"
title: "SemiAnalysis 解析 AWS Trainium3：推理性价比对标英伟达"
dek: "SemiAnalysis 发布对 AWS Trainium3 的推理性能与微架构深度分析，称在自建基准平台 InferenceX 上，Trainium3 搭配 PDS 与 vLLM…"
description: "SemiAnalysis 发布对 AWS Trainium3 的推理性能与微架构深度分析，称在自建基准平台 InferenceX 上，Trainium3 搭配 PDS 与 vLLM…"
section: "chips-compute"
rank: 7
edition: 0
section_rank: 3
score: 7.0
status: "Released"
source_name: "SemiAnalysis"
source_url: "https://newsletter.semianalysis.com/p/trainium3-inferencex"
via: null
discussion_url: null
published_at: "2026-11-27T15:54:59+00:00"
tags: ["AWS Trainium", "AI accelerators", "inference", "microarchitecture", "semiconductor supply chain"]
topics: ["aws-trainium", "ai-accelerators", "inference", "microarchitecture", "semiconductor-supply-chain"]
order: "20261128-0-992"
image: "/assets/stories/2026-11-28/semianalysis-benchmarks-aws-trainium3-claims-best-inference-cost-per-e779-share.jpg"
art: "/assets/stories/2026-11-28/semianalysis-benchmarks-aws-trainium3-claims-best-inference-cost-per-e779.jpg"
thumb: "/assets/stories/2026-11-28/semianalysis-benchmarks-aws-trainium3-claims-best-inference-cost-per-e779-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g169443d4ecd6ac40ec324e5398b423d4ab318366c632c673aa33d6bb5f95ecd83d78ae393a8d76094c240b887973d822a26e0f6a07f285b5f21d6963efd32876_1280.jpg", "author": "blickpixel", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/it-server-server-cabinet-network-838379/", "provider": "Pixabay", "width": 3095, "height": 2063}
---

{% raw %}
<div class="story-lead" markdown="1">

SemiAnalysis 发布对 AWS Trainium3 的推理性能与微架构深度分析，称在自建基准平台 InferenceX 上，Trainium3 搭配 PDS 与 vLLM，在“总拥有成本（TCO）对 p90 交互延迟”整条曲线上，每美元推理性能优于除英伟达 Vera Rubin 之外的所有加速器，并与 GB300 互有胜负。该结论基于 SemiAnalysis 自研的 UBenchX 微基准和 AgentX 端到端测试：后者通过回放真实编程智能体（coding agent）会话来测量生产级智能体推理负载。

微架构层面，报告称 Trainium 从零为机器学习负载设计，以 tile 为一等原语，其 Descriptor Generation Engines（DGE，作用类似英伟达 TMA、AMD MI455X 的 TDM）可在较小消息尺寸下达到峰值 HBM 带宽利用率（MBU），报告称这在英伟达 GPU 上无法实现。SemiAnalysis 表示 AWS Annapurna Labs 联合创始人 Nafea Bshara、Trainium 首席架构师 Ron Diamant 等团队成员协助其理解架构并验证了基准实验，但公开摘录未给出任何绝对性能数字或完整测试配置。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** SemiAnalysis 将 Trainium3 纳入其开源的 InferenceX 基准（与 TPUv7、OpenAI Jalapeño、英伟达 Rubin NVL72、AMD 同列），并用 UBenchX 做了周期级 SRAM、机架级带宽与注意力等微基准；AWS Annapurna Labs 团队参与架构讲解与实验验证，这是该机构自己的说明。
- **尚未证实：** 每美元性能“除 Vera Rubin 外全面领先”属 SemiAnalysis 自建基准上的厂商协助验证结果，摘录中未披露具体吞吐、延迟、价格假设与 TCO 计算口径，也无第三方复现；DGE 在小消息尺寸下达峰值 HBM 带宽利用率同样只有该机构的微基准支持。

</div>

## 背景

Trainium 是 AWS 自研的 AI 加速器系列，由旗下 Annapurna Labs 团队设计；Trainium3 是该系列第三代产品，AWS 官方资料称其集成 8 个大核，每核配 Tensor、Vector、Scalar、GPSIMD 四类引擎，MXFP8 算力最高为 Trainium2 的两倍。第三方《AI Accelerator Report 2026》汇总的 AWS 公布数据显示，Trainium3 是 AWS 首款 3nm AI 芯片，单芯片 2.52 PFLOPS FP8 算力、144GB HBM3e 显存，144 颗芯片组成的 Trn3 UltraServer 合计 20.7TB HBM3e 与 706TB/s 带宽。SemiAnalysis 此番强调「微架构」，正是因为英伟达的数据中心 GPU 源自图形渲染管线，历代为补上 AI 瓶颈逐块加装专用硬件（Volta 的 Tensor Core、Hopper 的 TMA、Blackwell 的 Tensor Memory），而 Trainium 从设计之初就以 tile 为一等公民。

## 为什么重要

对正在为智能体类推理负载选型的团队而言，这份分析给出了除英伟达之外的第二个可量化选项：若 Trainium3 的每美元 token 成本优势成立，同等预算下的推理毛利可能更高。但实际迁移的前提是软件栈——报告点名的路径是 vLLM 加 PDS，团队在评估时需要先确认自有模型的算子与注意力实现能否在该栈上跑通，而非仅比较芯片规格。

## 后续看点

InferenceX 的公开排行榜与 GitHub 仓库会持续更新 Trainium3 的配置点与 AgentX 结果，可观察是否有 AWS 之外的一方复现同一组每美元性能曲线。

## 延伸阅读

- [AI Accelerator - AWS Trainium - AWS](https://aws.amazon.com/ai/machine-learning/trainium/)
- [Chapter 11: AWS Trainium3 | AI Accelerator Report 2026](https://sampooni.github.io/ai-accelerator-report-2026/11-aws.html)

{% endraw %}
