---
layout: story
lang: zh
date: 2026-11-27 06:25:44 -0500
issue: "2026-11-27"
story_id: "amd-specific-fork-of-llama-cpp-draws-builder-interest-on-hacker-news-1d45"
permalink: "/zh/2026/11/27/amd-specific-fork-of-llama-cpp-draws-builder-interest-on-hacker-news-1d45/"
title: "AMD 专用 llama.cpp 分支登上 Hacker News"
dek: "一个针对 AMD GPU 优化的 llama.cpp 分支在 Hacker News 上被分享，意在改善在 AMD 硬件上本地跑大模型的推理效率，帖子里聚集了不少自己动手改内核的开发者。"
description: "一个针对 AMD GPU 优化的 llama.cpp 分支在 Hacker News 上被分享，意在改善在 AMD 硬件上本地跑大模型的推理效率，帖子里聚集了不少自己动手改内核的开发者。"
section: "ai-news"
rank: 1
edition: 0
section_rank: 1
score: 7.0
status: "Released"
source_name: "devnull.land"
source_url: "https://devnull.land/amd-specific-llama-cpp"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50657265"
published_at: "2026-11-26T17:11:29+00:00"
tags: ["llama.cpp", "AMD", "LLM inference", "open-source", "GPU optimization"]
topics: ["llama-cpp", "amd", "llm-inference", "open-source", "gpu-optimization"]
order: "20261127-0-998"
image: "/assets/stories/2026-11-27/amd-specific-fork-of-llama-cpp-draws-builder-interest-on-hacker-news-1d45-share.jpg"
art: "/assets/stories/2026-11-27/amd-specific-fork-of-llama-cpp-draws-builder-interest-on-hacker-news-1d45.jpg"
thumb: "/assets/stories/2026-11-27/amd-specific-fork-of-llama-cpp-draws-builder-interest-on-hacker-news-1d45-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g9fdc9899e1bfbfaa1d0ce69d3f7a35eb159302a28b71de1b8ccc6449f71029ed819aa3d2ac28cc2055627c5bc37d221614bd32f63f6597cacdcbaf7092f59143_1280.jpg", "author": "blickpixel", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/it-server-server-cabinet-network-838379/", "provider": "Pixabay", "width": 3095, "height": 2063}
---

{% raw %}
<div class="story-lead" markdown="1">

一个针对 AMD GPU 优化的 llama.cpp 分支在 Hacker News 上被分享，意在改善在 AMD 硬件上本地跑大模型的推理效率，帖子里聚集了不少自己动手改内核的开发者。该帖正文无法获取，因此分支的具体改动、维护者、许可证和实测加速比都无法从现有报道中核实。

评论区给出的背景是：约 2018 年的 gfx906 数据中心卡算力平平，却配有 32GB HBM2 和约 1TB/s 带宽，二手价约 200 美元，同时没有 tensor core、也不支持原生 bf16，于是社区多年来各自维护针对这类卡的 llama.cpp 分支。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** Hacker News 于 2026 年 11 月 26 日出现一篇题为「AMD-specific fork of llama.cpp」的帖子（发布者 julianlam），链接指向 devnull.land 上的介绍页；评论区多位开发者分别表示，自己为 AMD 显卡（gfx906 系列、MI100、R9700 等）维护或使用 llama.cpp 的优化分支。
- **尚未证实：** 该 fork 究竟改动了什么、支持哪些显卡与 ROCm 版本、有无可复现的性能数据、以何种许可证发布，现有报道均无法核实——介绍页正文未提供。评论中「32GB、约 1 TB/s 带宽的 gfx906 显卡仅约 200 美元」「R9700 单卡 prefill 2400 tok/s、decode 150 tok/s」等数字，是个人用户对各自项目的说法，并非对该 fork 的独立测试。

</div>

## 背景

llama.cpp 是用 C/C++ 编写的开源本地大模型推理引擎，长期以 Nvidia 的 CUDA 为主要优化路径；在 AMD 显卡上它需要经由 ROCm/HIP 后端运行，针对新架构的适配和调优通常落后于 CUDA 版本。正因如此，社区常会针对特定 AMD 架构自行打补丁、分叉维护，这次被讨论的 llama-cpp-rdna-boosts 就是其中之一，面向 AMD 的 RDNA 系列显卡，帖子作者称其比原版 llama.cpp 表现更好。

## 为什么重要

对还在用 gfx906 这类老卡的开发者来说，专用分支目前是让 llama.cpp 跑得动、跑得快的主要途径，但这类优化是针对具体架构手写移植的：换成 Radeon AI PRO R9700 或 Strix Halo 等新硬件，就得另找对应的分支或工具集合，采用前应先确认其内核是否覆盖自己的 GPU 型号和量化格式。

## 后续看点

值得留意这个分支的改动是否会被合并回 llama.cpp 上游，以及作者是否会公布可复现的基准数据，让不同 AMD 卡上的加速比可以横向比较。

## 延伸阅读

- [AMD-specific fork of llama.cpp | devnull.land](https://devnull.land/amd-specific-llama-cpp)
- [AMD - specific fork of llama . cpp | Hacker News](https://news.ycombinator.com/item?id=50657265)

<div class="community" markdown="1">

## 社区讨论（观点，不是证据）

评论者 rao-v 认为，这正是围绕廉价 gfx906 老卡形成的一个小而活跃的优化生态，并贴出了自己的个人仓库作为例子；fiddlerwoaroof 也称自己把部分 Nvidia 内核移植到 ROCm 后性能明显提升，并表示已做过验证。另一位评论者 malicz 自述在单张 R9700 上达到 2400 tok/s 的 prefill 和 150 tok/s 的 decode，但这些数字均为个人自述，没有提供可复现的基准。

</div>

{% endraw %}
