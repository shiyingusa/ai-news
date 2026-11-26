---
layout: story
lang: zh
date: 2026-11-26 18:20:28 -0500
issue: "2026-11-26"
story_id: "inside-clay-s-rebuild-of-its-gtm-agent-stack-d953"
permalink: "/zh/2026/11/26/inside-clay-s-rebuild-of-its-gtm-agent-stack-d953/"
title: "Clay 的 GTM 智能体工程取舍"
dek: "A Clay AI leader explains the engineering and product tradeoffs behind its GTM agents…"
description: "A Clay AI leader explains the engineering and product tradeoffs behind its GTM agents…"
section: "tech-blog"
rank: 206
edition: 2
section_rank: 1
score: 7.0
status: null
source_name: "Latent Space"
source_url: "https://latent.space/p/how-clay-builds-gtm-agents-jeff-barg-head-of-ai/"
via: null
discussion_url: null
published_at: "2026-11-26T23:02:48+00:00"
tags: ["agent architecture", "GTM agents", "model routing", "LLM evaluation", "inference infrastructure"]
topics: ["agent-architecture", "gtm-agents", "model-routing", "llm-evaluation", "inference-infrastructure"]
order: "20261126-2-993"
image: "/assets/stories/2026-11-26/inside-clay-s-rebuild-of-its-gtm-agent-stack-d953-share.jpg"
art: "/assets/stories/2026-11-26/inside-clay-s-rebuild-of-its-gtm-agent-stack-d953.jpg"
thumb: "/assets/stories/2026-11-26/inside-clay-s-rebuild-of-its-gtm-agent-stack-d953-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g796fddadb1cb243a001eaf5bcbdb8c1bb47b24a592f2a2288e53bf203afb97a3eb00a863abdd817b60c8bf154407d6df2b33f01259e15655e9819f069ba70e2c_1280.jpg", "author": "Akela999", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/data-center-engine-room-2476790/", "provider": "Pixabay", "width": 4096, "height": 2160}
---

{% raw %}
<div class="story-lead" markdown="1">

A Clay AI leader explains the engineering and product tradeoffs behind its GTM agents, from coding-agent architecture and evals to model routing, post-training timing, and workload scaling.

</div>

## 背景

Clay 希望用户无论使用自家智能体，还是把 Claude Code 指向 Clay，都得到相近结果；目前两种入口的使用量已接近五五开。这要求其 GTM 基础设施同时服务产品界面和外部编码智能体。

## 方案

Sculptor 起初是循环调用固定工具的系统：加列很强，却难以完成“约到十场合格会议”这类端到端任务；用 LLM 评判工具调用的旧评估也漏掉真实用法，如分析表格或处理百万行企业表。Clay 因此把它重构成运行在 Pi harness 上的编码智能体，在云沙箱中调用 Clay CLI，并用 Audiences 数据层对齐 CRM 与 Gong 记录。Jeff Barg 认为资格筛选已接近饱和，前沿模型更多用于编排和深度研究；Clay 将推出自动模型路由器，同时保留选择器给需要控制权的用户。Jeff 认为后训练不宜过早：先用开源权重模型降本，等推理支出达到约 1000 万至 1 亿美元再考虑小模型追平 Opus。按每家公司约 1500 token 计算，给 4000 万家公司做一次 ICP 分类约 1500 美元；合格线索的富化预算约 1 至 10 美元。基础设施上，Clay 用 BullMQ 自建任务系统，按行并发会造成推理尖峰，因此加入限流、供应商故障时暂停恢复与公平调度。智能体仍不擅长阅读长轨迹定位错误，常把耗时步骤误判为根因，Clay 仍大量手写技能。

## 启示

Clay 的经验表明，构建 GTM 智能体的关键不是追逐每个新模型，而是把编码智能体、数据可见性、任务级路由和弹性调度组合起来；评估与调试仍需围绕真实使用，而不是只验证工具调用。

{% endraw %}
