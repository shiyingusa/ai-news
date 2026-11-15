---
date: 2026-11-14 06:00:00 -0500
layout: "story"
lang: "zh"
issue: "2026-11-14"
story_id: "ggml-the-tensor-library-under-llama-cpp-reaches-v1-0-0-6c41"
permalink: "/zh/2026/11/14/ggml-the-tensor-library-under-llama-cpp-reaches-v1-0-0-6c41/"
title: "GGML 张量库发布 v1.0.0，llama.cpp 本地推理底座迎来首个正式版本"
dek: "支撑 llama.cpp 及大量本地 AI 工具的张量库 GGML 在 GitHub 上打出了 v1.0.0 版本标签，这是该项目首次跨入 1.0 版本号。"
section: "ai-news"
rank: 1
section_rank: 1
score: 8.0
status: "Released"
updated: "2026-11-15"
source_name: "GitHub"
source_url: "https://github.com/ggml-org/ggml/releases/tag/v1.0.0"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50493062"
published_at: null
tags: ["open-source AI", "local inference", "llama.cpp", "GGML", "model runtime"]
topics: ["open-source-ai", "local-inference", "llama-cpp", "ggml", "model-runtime"]
order: "20261114-998"
image: "/assets/stories/2026-11-14/ggml-the-tensor-library-under-llama-cpp-reaches-v1-0-0-6c41-share.jpg"
art: "/assets/stories/2026-11-14/ggml-the-tensor-library-under-llama-cpp-reaches-v1-0-0-6c41.jpg"
thumb: "/assets/stories/2026-11-14/ggml-the-tensor-library-under-llama-cpp-reaches-v1-0-0-6c41-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g67fb18791f507108591ce73165a86cf68105975b320ca9dee091b5280e33b195a76bcf56164c19e992c6cc5f3bbfd38845f3eeecf362e35b8984ee8bdfe716ea_1280.jpg", "author": "blickpixel", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/it-server-server-cabinet-network-838379/", "provider": "Pixabay", "width": 3095, "height": 2063}
---

{% raw %}
<p class="correction-note"><strong>更正（2026 年 11 月 15 日）：</strong>本文早先版本称没有发布说明，与背景部分矛盾；还仅凭用户评论，把 MoE 模型的显存外溢功能归到这个版本。现已按公开的发布说明改写摘要，并把用户说法标明为用户说法。</p>
<div class="story-lead" markdown="1">

支撑 llama.cpp 及大量本地 AI 工具的开源 C 语言张量库 GGML 在 GitHub 上打出 v1.0.0 标签，这是它第一个 1.x 版本。据相关报道和 SourceForge 上的发布说明镜像，这个版本标志着项目开始正式采用语义化版本号（semantic versioning），移除了已弃用的公共 API 和旧的 DIAG_MASK 算子，并新增 FP8 支持和可配置的 YaRN 截断；这些说明我们未能在 GitHub 发布页上直接核对。讨论区用户的体验是持续小幅提升，而不是一次飞跃，有用户说每月升级通常能带来 5% 到 10% 的速度提升。

</div>

## 背景

GGML 是一个用 C 写的张量计算库，llama.cpp 以及大量在本地运行模型的工具都构建在它之上；它负责在 CPU、CUDA、Metal、Vulkan 等不同硬件上完成矩阵运算与内存管理，用户感受到的本地推理速度很大程度上由它决定。据 SourceForge 上的发布说明，v1.0.0 移除了已废弃的公共 API 和旧的 DIAG_MASK 算子，新增 FP8 支持与可配置的 YaRN 截断，并在 CUDA、Metal、Vulkan、SYCL、OpenCL、WebGPU、Hexagon 等后端做了性能工作（如少行量化矩阵乘、MoE 融合、Vulkan 预填充 FlashAttention）；有报道称，这次发布与 llama.cpp v1.0.0 同步进行，意味着项目在启动约三年半后首次转向正式的语义化版本号。

## 对本地部署的实际影响

对显存预算略超的 MoE 模型，用户可以把不常用的专家权重缓存到主机内存，而不是直接加载失败；但这一机制需要专家权重位于锁页主机内存（pinned host memory，不会被换出到磁盘的内存），并高度依赖 PCIe 带宽，Windows 的锁页限制可能导致缓存无法启用，且有独立测试在 PCIe 3.0 平台上测得该缓存与合并缓存方案大致持平。GGML 通过为各类硬件编写专用后端来覆盖几乎任何硬件，包括只支持 Vulkan 的 AMD 显卡，因此上述内存与带宽条件直接决定了旧卡或小显存机器上能跑多大的模型。此外，llama.cpp 服务端仍需用 --tensor-split 和 --main-gpu 手工指定多卡切分比例与主卡，说明跨 GPU 的负载分配目前仍要用户自行配置。

## 社区讨论

长期用户 jacquesm 称该项目和 llama.cpp 的亮点在于持续在同一硬件上压榨性能，他每月升级通常能获得 5% 到 10% 的速度提升，并按自己的方式做了验证：在 5 万 token 的长提示词上，升级后运行时间从 4 分 22 秒降到 3 分 59 秒，其中预填充占相当比重，其余为逐 token 生成。另一位用户 thisisauserid 表示，当 MoE 模型略微超出显存预算时，llama.cpp 与 ggml v1.0.0 可以把不常用的专家缓存在主机内存中，而不是直接加载失败——这是用户体验层面的说法，并非发布说明中的官方描述。

## 延伸阅读

- [ggml - Browse /v1.0.0 at SourceForge.net](https://sourceforge.net/projects/ggml.mirror/files/v1.0.0/)
- [ggml-org Releases llama.cpp v1.0.0 and ggml v1.0.0 with ...](https://af.net/realtime/ggml-org-releases-llama-cpp-v1-0-0-and-ggml-v1-0-0-with-strict-semantic-versioning/)
- [llama . cpp /tools/server/README.md at master · ggml -org/ llama . cpp](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)
- [llama . cpp Just Made Huge MoE Models 4× Faster - YouTube](https://www.youtube.com/watch?v=ohp15NcKDhA)
- [llama . cpp v 1 . 0 . 0 : A stronger foundation for the local AI ecosystem](https://huggingface.co/blog/ggml-org/llama-cpp-v1)

{% endraw %}
