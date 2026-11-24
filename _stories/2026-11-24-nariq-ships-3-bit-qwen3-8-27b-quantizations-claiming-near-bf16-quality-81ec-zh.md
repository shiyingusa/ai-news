---
layout: story
lang: zh
date: 2026-11-24 06:27:21 -0500
issue: "2026-11-24"
story_id: "nariq-ships-3-bit-qwen3-8-27b-quantizations-claiming-near-bf16-quality-81ec"
permalink: "/zh/2026/11/24/nariq-ships-3-bit-qwen3-8-27b-quantizations-claiming-near-bf16-quality-81ec/"
title: "NariQ 发布 Qwen3.8-27B 低比特量化，10 GB 文件声称接近 BF16"
dek: "NariQ 在 Hugging Face 发布了 Qwen3.8-27B 的 3 比特及更低比特量化版本（GGUF 格式），文件约 10 GB，作者称其在智能体任务、数学、多语言推理和图像理解上保持接近 BF16 的质量…"
description: "NariQ 在 Hugging Face 发布了 Qwen3.8-27B 的 3 比特及更低比特量化版本（GGUF 格式），文件约 10 GB，作者称其在智能体任务、数学、多语言推理和图像理解上保持接近 BF16 的质量…"
section: "ai-news"
rank: 1
edition: 0
section_rank: 1
score: 7.0
status: "Released"
source_name: "Hugging Face"
source_url: "https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50611402"
published_at: "2026-11-23T13:42:38+00:00"
tags: ["quantization", "Qwen3.8-27B", "local LLMs", "llama.cpp", "model compression"]
topics: ["quantization", "qwen3-8-27b", "local-llms", "llama-cpp", "model-compression"]
order: "20261124-0-998"
image: "/assets/stories/2026-11-24/nariq-ships-3-bit-qwen3-8-27b-quantizations-claiming-near-bf16-quality-81ec-share.jpg"
art: "/assets/stories/2026-11-24/nariq-ships-3-bit-qwen3-8-27b-quantizations-claiming-near-bf16-quality-81ec.jpg"
thumb: "/assets/stories/2026-11-24/nariq-ships-3-bit-qwen3-8-27b-quantizations-claiming-near-bf16-quality-81ec-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g8a9f4ad162ab7c11c7f183f127692e5de4dc727dd08643e9dbeb2fdbe9b2d07090fc9200be28ec571c9ce3b04c922e27aedfeda5ab552117e3da99365d4e599a_1280.jpg", "author": "donterase", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/study-workroom-office-glimpse-789631/", "provider": "Pixabay", "width": 4381, "height": 2915}
---

{% raw %}
<div class="story-lead" markdown="1">

NariQ 在 Hugging Face 发布了 Qwen3.8-27B 的 3 比特及更低比特量化版本（GGUF 格式），文件约 10 GB，作者称其在智能体任务、数学、多语言推理和图像理解上保持接近 BF16 的质量，并称这是首个在长程智能体任务上保持 BF16 水平性能的 3 比特及以下量化。作者自报的对比数据（BF16 / 3-bit / 2.5-bit / 2-bit）为：DeepSWE 39.8 / 41.0 / 41.9 / 28.6，Terminal-Bench 2.1 62.6 / 63.8 / 60.2 / 52.4，AIME 25+26 97.7 / 98.3 / 96.5 / 86.0，MSGM 94.0 / 93.1 / 91.8 / 90.6，RealWorldQA 82.4 / 82.4 / 81.3 / 80.9——在多数项目上 3-bit 与 2.5-bit 与 BF16 持平甚至略高，但 2-bit 在 DeepSWE 和 AIME 上明显下降。作者称在 RTX PRO 6000 上解码速度与其他量化相当，并给出了 4K/16K/64K 上下文下的速度数值（如 64K 时 3-bit 为 70.7、2.5-bit 为 77.5、2-bit 为 85.0，对比 Unsloth UD-IQ3_XXS 的 74.8）。运行这些模型目前需要使用作者的 llama.cpp 分支 nari-llama.cpp，而非上游版本；在 M3 Pro（18 GB）上需从源码编译，3.0bpw 文件解码约 3.8 tok/s（2.0bpw 约 4.9 tok/s），作者称远慢于 CUDA，其他 Mac 机型未测试。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** NariQ 在 Hugging Face 上发布了 Qwen3.8-27B 的 3-bit 及更低比特量化版本，发布页列出了 DeepSWE、Terminal-Bench 2.1、AIME 25+26、MSGM、RealWorldQA 五组基准上 BF16 与 3-bit／2.5-bit／2-bit 的对比数字，并说明目前必须使用其自建的 llama.cpp 分支（nari-llama.cpp）才能运行；模型仓库的提交说明显示 DeepSWE 为三轮平均、在 Docker 环境中逐题统计并给出样本数（tool-3-1）。
- **尚未证实：** “接近 BF16 质量”和“首个在长程 agentic 任务上保持 BF16 水平”的说法均为作者自报，尚无可查的独立第三方复测；发布内容未交代标题所称 10 GB 文件的具体构成、各基准所用的评测框架版本与 held-out 划分，而公开的 Terminal-Bench 排行榜页面当前已是 4.1 版（tool-3-3），与文中 2.1 版成绩不能直接对比；Mac 上约 3.8 tok/s（M3 Pro，3.0bpw）的推理速度仅见于评论者转述的说明，发布正文未给出。

</div>

## 背景

量化（quantization）是把模型权重用更低的位数存储，以换取更小显存占用和更快速度的技术；GGUF 是 llama.cpp 生态常用的量化文件格式，"3-bit"即每个权重约 3 比特。Qwen3.8-27B 若以 BF16（每权重 2 字节）保存约需 54 GB，因此压到 3 比特左右才能装进约 10 GB 的文件、跑在消费级硬件上（tool-2-3）。不过 Nari Labs 的模型卡说明，这批文件需配合其自研的 llama.cpp 分支运行（tool-2-2）。

## 为什么重要

对想在本地或单卡上跑 27B 级模型的用户，这些文件把显存/存储门槛压到约 10 GB 量级，代价是必须改用作者的 llama.cpp 分支，意味着无法直接套用上游 llama.cpp 的常规部署流程，也拿不到上游后续的性能与兼容性修复；在 Apple Silicon 上还要自行编译，且实测速度只有个位数 tok/s。

## 后续看点

值得留意 nari-llama.cpp 的相关改动是否会进入上游 llama.cpp，以及其他开发者对这些文件在自有工作负载上的独立复现结果，包括与 Bonsai 2 27B 等同类量化的对比。

## 社区讨论

有评论者对这类高算力量化训练（QAT 风格）容易过拟合基准数据集表示怀疑，但认为该项目做了少见的基本检验——覆盖多种长程任务并提到使用了“held out”（留出）数据。另有评论者依据作者给出的图表认为，大部分提升来自测试框架（harness）差异而非模型本身；也有人追问压缩过程中究竟损失了什么信息，并关心能否塞进 16 GB 的 Mac。

## 延伸阅读

- [nari-labs/Qwen3.8-27B-NariQ-GGUF · Hugging Face](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF)
- [NariQ Quantization: Qwen3.8-27B Agents in a 10 GB File](https://aitecharchive.com/articles/nariq-quantization-qwen3-8-27b-agent-performance-10gb)
- [Report three-round DeepSWE averages...](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF/commit/9065513f08d8ed7dbe50b9c329cac1f40c70fde9)
- [TERMINAL - BENCH](https://www.tbench.ai/)

{% endraw %}
