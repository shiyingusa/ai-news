---
layout: story
lang: zh
date: 2026-11-24 06:27:21 -0500
issue: "2026-11-24"
story_id: "aws-launches-five-open-strands-decider-v2-models-the-new-stack-reports-88c0"
permalink: "/zh/2026/11/24/aws-launches-five-open-strands-decider-v2-models-the-new-stack-reports-88c0/"
title: "AWS 推出 Strands Decider v2：五个基于 Gemma 4 的开放决策模型"
dek: "AWS 于周一发布 Strands Decider v2，这是一组五个“决策模型”（decision models，即针对智能体中的选择、路由一类判断任务调优的模型），全部基于 Google 的 Gemma 4 构建…"
description: "AWS 于周一发布 Strands Decider v2，这是一组五个“决策模型”（decision models，即针对智能体中的选择、路由一类判断任务调优的模型），全部基于 Google 的 Gemma 4 构建…"
section: "ai-news"
rank: 4
edition: 0
section_rank: 4
score: 7.0
status: "Released"
source_name: "The New Stack"
source_url: "https://thenewstack.io/aws-strands-decider-v2/"
via: "Techmeme"
discussion_url: null
published_at: "2026-11-24T04:25:01+00:00"
tags: ["AWS", "open models", "Gemma 4", "Apache 2.0", "model release"]
topics: ["aws", "open-models", "gemma-4", "apache-2-0", "model-release"]
order: "20261124-0-995"
image: "/assets/stories/2026-11-24/aws-launches-five-open-strands-decider-v2-models-the-new-stack-reports-88c0-share.jpg"
art: "/assets/stories/2026-11-24/aws-launches-five-open-strands-decider-v2-models-the-new-stack-reports-88c0.jpg"
thumb: "/assets/stories/2026-11-24/aws-launches-five-open-strands-decider-v2-models-the-new-stack-reports-88c0-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/ge3b3eb3a7944384a8a3ab9062def5a2d7625bf4a312b51d5aaa3ab54bb29a6b91a9734cfb548cb0c19e118f3c3aef506670ba68157d3d3f313fda8c5ec5260b2_1280.jpg", "author": "MightyFineBros", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/data-center-technology-server-7388620/", "provider": "Pixabay", "width": 4800, "height": 2700}
---

{% raw %}
<div class="story-lead" markdown="1">

AWS 于周一发布 Strands Decider v2，这是一组五个“决策模型”（decision models，即针对智能体中的选择、路由一类判断任务调优的模型），全部基于 Google 的 Gemma 4 构建，参数规模从 2B 到 31B，采用 Apache 2.0 许可。据 The New Stack 记者 Frederic Lardinois 报道，此次发布距离 Strands Labs 的上一次发布仅七周。

报道只给出了模型家族的数量、底座、参数区间和许可证，没有披露各尺寸的基准成绩、训练数据，也未说明这些模型在 AWS 自家产品中如何分发或托管。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** Strands Labs 的博客（tool-3-1）称 Strands Decider v2 是基于 Gemma 4 的五个模型，参数规模从 E2B 到 31B，采用 Apache 2.0 许可，模型权重已发布在 Hugging Face，v2 支持已进入开源的 Strands Decider 仓库；VentureBeat（tool-3-2）和 explainx.ai（tool-3-3）的报道与这一描述一致。据该博客所述，Decider 属于“system one”模型：它不生成文本，而是在一次前向传播中从给定选项里选择，并为每个选项返回一个概率。
- **尚未证实：** 模型的决策准确率、概率校准质量与延迟等性能主张目前仅出自公司自己的博客，没有独立评测或第三方复现；各尺寸模型的具体硬件要求、是否通过 AWS 托管服务提供以及定价，均未在报道中说明。

</div>

## 背景

Strands Decider 属于所谓"系统一"（system one）模型：它不做长篇推理，而是针对需要快速、反射式判断的环节，例如智能体（agent）在分叉路口选择下一步走向，并以带校准的概率输出结果。据 The New Stack 报道，这次发布距离 Strands Labs 上一次发布只有七周，v2 是在上一代基础上的迭代版本。它沿用了 Google 的开放模型系列 Gemma 4 作为底座，并延续开源权重路线，把权重放在 Hugging Face 上、在开源 Strands Decider 代码库中提供 v2 支持。

## 为什么重要

Apache 2.0 允许修改和再分发，因此团队可以把这套模型自托管、微调后嵌入自有产品，而不必依赖按调用量计费的托管 API；2B 到 31B 的尺寸阶梯也让开发者能在延迟敏感的场景选小模型、在复杂判断上选大模型。需要注意的是，报道没有给出任何性能数字，选型前应等待模型卡或独立评测。

## 后续看点

关注 AWS 是否公布五个尺寸各自的模型卡与评测结果，以及第三方基准何时把这些“决策模型”与通用小模型做同口径对比。

## 延伸阅读

- [Introducing Strands Decider v2: open, calibrated system one ...](https://strandsagents.com/blog/introducing-strands-decider-v2/)
- [Strands Decider v2: 5 Open Models (Apache 2.0) | explainx.ai Blog](https://explainx.ai/blog/aws-strands-decider-v2-gemma4-november-2026)
- [Introducing Strands Decider v2: open, calibrated system one ...](https://strandsagents.com/blog/introducing-strands-decider-v2/)
- [AWS's Strands Decider v2 targets the agent decisions that ...](https://venturebeat.com/data/awss-strands-decider-v2-targets-the-agent-decisions-that-hinge-on-a-single-detail)
- [Strands Decider v2: 5 Open Models (Apache 2.0) | explainx.ai Blog](https://explainx.ai/blog/aws-strands-decider-v2-gemma4-november-2026)

{% endraw %}
