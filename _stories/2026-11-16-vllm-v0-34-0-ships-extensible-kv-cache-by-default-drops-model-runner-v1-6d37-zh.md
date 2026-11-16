---
layout: story
lang: zh
date: 2026-11-16 06:00:00 -0500
issue: "2026-11-16"
story_id: "vllm-v0-34-0-ships-extensible-kv-cache-by-default-drops-model-runner-v1-6d37"
permalink: "/zh/2026/11/16/vllm-v0-34-0-ships-extensible-kv-cache-by-default-drops-model-runner-v1-6d37/"
title: "vLLM v0.34.0 发布：KV 缓存扩展默认开启并移除 Model Runner V1"
dek: "vLLM 发布 v0.34.0，面向使用该开源推理引擎部署模型的团队，新增 Mistral Large 4、MiniMax-M3.1-Flash、Nemotron-3.5-Transcribe 等 10 个模型支持…"
description: "vLLM 发布 v0.34.0，面向使用该开源推理引擎部署模型的团队，新增 Mistral Large 4、MiniMax-M3.1-Flash、Nemotron-3.5-Transcribe 等 10 个模型支持…"
section: "ai-news"
rank: 201
edition: 2
section_rank: 1
score: 8.0
status: "Available"
source_name: "GitHub"
source_url: "https://github.com/vllm-project/vllm/releases/tag/v0.34.0"
via: null
discussion_url: null
published_at: "2026-11-16T23:22:00+00:00"
tags: ["vLLM", "open-source", "inference", "model serving", "performance"]
topics: ["vllm", "open-source", "inference", "model-serving", "performance"]
order: "20261116-2-998"
image: "/assets/stories/2026-11-16/vllm-v0-34-0-ships-extensible-kv-cache-by-default-drops-model-runner-v1-6d37-share.jpg"
art: "/assets/stories/2026-11-16/vllm-v0-34-0-ships-extensible-kv-cache-by-default-drops-model-runner-v1-6d37.jpg"
thumb: "/assets/stories/2026-11-16/vllm-v0-34-0-ships-extensible-kv-cache-by-default-drops-model-runner-v1-6d37-640.jpg"
photo_credit: null
---

{% raw %}
<div class="story-lead" markdown="1">

vLLM 发布 v0.34.0，面向使用该开源推理引擎部署模型的团队，新增 Mistral Large 4、MiniMax-M3.1-Flash、Nemotron-3.5-Transcribe 等 10 个模型支持，并默认启用可扩展 KV 缓存：缓存按预热后实际空闲显存确定，发布说明举例称 MiniMax-M3 在 H200 上从 433k 增至 672k tokens。该版本移除了 Model Runner V1，V2 成为唯一 GPU runner，同时列出多项性能提升，例如 Step5 在 4×GB200 上解码最高 1.95×、GLM-5.3-Flash 输出吞吐 1.6×，但这些数字来自发布说明，尚无独立复测。升级前需处理破坏性变更：默认 block size 从 16 改为 64、gpu_memory_utilization 默认 1.0、ROCm 7.2 构建不再发布，并要求 huggingface_hub >= 2.0.0；设置 VLLM_USE_V2_MODEL_RUNNER=0 现在会在启动时失败。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** GitHub 上的 v0.34.0 发布说明由 khluu 发布，列出 1,061 个提交、412 名贡献者、10 个新模型，以及 KV 缓存默认扩展、Model Runner V1 移除和上述升级变更；安装命令覆盖 CUDA 13.0、ROCm 10.0、XPU 及 Docker 镜像。
- **尚未证实：** 1.95× 解码、1.6× 吞吐等加速均为发布说明自报，未附独立基准；各现有部署升级后的兼容性与实际吞吐变化仍需自行验证。发布说明中 XPU 安装行还留有 TODO，称需确认在新内核包索引下是否仍可解析。

</div>

## 背景

vLLM 是广泛用于在生产环境部署大模型的开源推理引擎，其核心机制之一是把注意力计算所需的键值缓存（KV cache，即生成每个 token 时要复用的中间状态）切成固定大小的「块」来管理，这种分页式设计让显存利用率和并发吞吐明显提高。此前 vLLM 按估算值预分配 KV 缓存显存，并同时维护两代「Model Runner」（负责在 GPU 上执行前向计算与采样的那一层封装），v0.34.0 正是针对这两处基础设计做了改动。

## 为什么重要

对已用 vLLM 提供在线服务的团队，升级不是替换镜像即可：默认 block size 和显存利用率改变会改变缓存与并发表现，旧启动参数、V1 logits processor 及 fp_quant 检查点都可能失效，需要先按发布说明逐项迁移并用自身负载复测吞吐与 TPOT。

{% endraw %}
