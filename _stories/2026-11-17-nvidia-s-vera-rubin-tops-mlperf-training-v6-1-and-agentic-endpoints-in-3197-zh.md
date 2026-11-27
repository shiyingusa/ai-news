---
layout: story
lang: zh
date: 2026-11-17 06:00:00 -0500
issue: "2026-11-17"
story_id: "nvidia-s-vera-rubin-tops-mlperf-training-v6-1-and-agentic-endpoints-in-3197"
permalink: "/zh/2026/11/17/nvidia-s-vera-rubin-tops-mlperf-training-v6-1-and-agentic-endpoints-in-3197/"
title: "英伟达称 Vera Rubin 首登 MLPerf 即领先"
dek: "英伟达在博客中称，Vera Rubin 首次参加 MLPerf 就横扫 MLPerf Training v6.1 全部基准，并在首份 MLPerf Endpoints（v1.0）提交中…"
description: "英伟达在博客中称，Vera Rubin 首次参加 MLPerf 就横扫 MLPerf Training v6.1 全部基准，并在首份 MLPerf Endpoints（v1.0）提交中…"
section: "chips-compute"
rank: 3
edition: 0
section_rank: 2
score: 7.0
status: "Demonstrated"
source_name: "NVIDIA Blog"
source_url: "https://blogs.nvidia.com/blog/mlperf-training-endpoints-vera-rubin/"
via: null
discussion_url: null
published_at: "2026-11-16T16:00:25+00:00"
tags: ["MLPerf", "NVIDIA Vera Rubin", "AI accelerators", "benchmarks", "energy efficiency"]
topics: ["mlperf", "nvidia-vera-rubin", "ai-accelerators", "benchmarks", "energy-efficiency"]
order: "20261117-0-996"
image: "/assets/stories/2026-11-17/nvidia-s-vera-rubin-tops-mlperf-training-v6-1-and-agentic-endpoints-in-3197-share.jpg"
art: "/assets/stories/2026-11-17/nvidia-s-vera-rubin-tops-mlperf-training-v6-1-and-agentic-endpoints-in-3197.jpg"
thumb: "/assets/stories/2026-11-17/nvidia-s-vera-rubin-tops-mlperf-training-v6-1-and-agentic-endpoints-in-3197-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/gcee7f81c85195226fd7de93295476cf09ed18615e41e9b430403c3bda724d15e35a749d7cb9a83ca165b81b68016af1ce78dd8a5e7f8c2c3b4ffb58067f75c32_1280.jpg", "author": "bsdrouin", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/network-server-system-2402637/", "provider": "Pixabay", "width": 1920, "height": 1080}
---

{% raw %}
<div class="story-lead" markdown="1">

英伟达在博客中称，Vera Rubin 首次参加 MLPerf 就横扫 MLPerf Training v6.1 全部基准，并在首份 MLPerf Endpoints（v1.0）提交中，于智能体工作负载上实现超过 10 倍于 GB300 NVL72 的每瓦吞吐量。训练方面，Vera Rubin NVL72 每 GPU 性能最高为 GB300 NVL72 的 2 倍；在 DeepSeek-V3 上从 256 个 GPU 扩展到 1,024 个 GPU 仍保持约 97% 效率，训练时间从 16 分钟降到约 4 分钟。

推理侧的 10 倍数字来自 Kimi K3 的临时结果，比较的是 32 加速器、100.89 kW 的 Vera Rubin NVL72 与 48 加速器、60 kW 的 GB300 NVL72，在双方至少 50 tokens/s/用户的交互速度下按每千瓦吞吐量计算。该 Endpoints 结果尚待 MLCommons 验证、可能变化；GB300 的结果已由 MLCommons 验证。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** 据英伟达官方博客及其引用、标注来源于 MLCommons 结果库（results.mlcommons.org，2026 年 11 月 16 日）的数据，Vera Rubin NVL72 在本轮 MLPerf Training v6.1 中每 GPU 性能最高为 GB300 NVL72 的 2 倍；在 DeepSeek-V3 基准上从 256 颗扩展到 1,024 颗 GPU 仍保持约 97% 的扩展效率，训练时间由 16 分钟缩短到约 4 分钟；英伟达是唯一在所有训练基准上都有提交结果的公司。图文注释同时显示，Kimi K3 的 MLPerf Endpoints（v1.0，2026 年 11 月 9 日发布）对比中，Vera Rubin NVL72 用 32 个加速器、100.89 kW 运行功率取得 41,414.2 tokens/秒，GB300 NVL72 用 48 个加速器、60 kW 取得 2,210.4 tokens/秒。
- **尚未证实：** “横扫全部训练基准”“每瓦吞吐超过 10 倍”均为英伟达自己对结果的解读；其 Endpoints 结果明确标注为 provisional（暂定），尚待 MLCommons 协会验证与同行评审，可能变更（GB300 结果已获验证）。对比条件也有保留：两者是在“端到端平均交互速度不低于 50 tokens/秒/用户”的共同口径下比较，而 GB300 的该项实测为 56.2 tokens/秒/用户、首 token 延迟 P90 为 2,305.1 毫秒，优于 Vera Rubin 的 4,673.9 毫秒，即吞吐/能效优势伴随更差的响应延迟。此外价格、正式上市时间、完整配置均未披露；此前 9 月 MLPerf Inference v6.1 首秀的 2.5 倍/3.7 倍提升同样出自英伟达口径（tool-2-1）。

</div>

## 背景

MLPerf 由 MLCommons 管理，是一套同行评议式的基准测试：MLPerf Training 衡量系统把各类模型训练到目标精度所需的时间，而今年新推出的 MLPerf Endpoints v1.0 则用真实智能体编程与企业工作流来测试系统，并核对智能体是否仍正确完成任务。英伟达此次的对照基线是上一代 GB300 NVL72（Blackwell Ultra 一代系统），Vera Rubin NVL72 是其继任平台；文中引用的 Endpoints 数据发布于 11 月 9 日，Vera Rubin 一侧为临时结果，尚待 MLCommons 验证与同行评议，GB300 结果则已由 MLCommons 验证。

## 为什么重要

对准备采购智能体推理集群的团队，能效比峰值吞吐更直接决定同一功率预算能跑多少智能体任务；但 Vera Rubin 的 10 倍数字仍是临时结果，采购前应等 MLCommons 验证，并核对交互延迟（如 TTFT P90）和并发条件，而不是只比系统 tokens/s。

## 后续看点

MLCommons 对 Vera Rubin Endpoints 临时结果的验证和最终发布；验证后 10 倍每瓦吞吐量数字是否保持不变。

## 延伸阅读

- [Where the Industry Is Investing: A Look at MLPerf ... - MLCommons](https://mlcommons.org/2026/09/chairs-mlperf-inference-v6-1/)

{% endraw %}
