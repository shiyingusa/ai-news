---
layout: story
lang: zh
date: 2026-11-28 06:28:04 -0500
issue: "2026-11-28"
story_id: "google-s-deepcrossattention-claims-up-to-3x-speedup-at-comparable-bcf3"
permalink: "/zh/2026/11/28/google-s-deepcrossattention-claims-up-to-3x-speedup-at-comparable-bcf3/"
title: "Google Research 提出 DeepCrossAttention：质量相当下最高 3 倍提速"
dek: "Google Research 在博客中提出 DeepCrossAttention（DCA）：不改动 transformer 的基本组件，而是改动残差连接（即把每层输入直接加到输出上的那条旁路）…"
description: "Google Research 在博客中提出 DeepCrossAttention（DCA）：不改动 transformer 的基本组件，而是改动残差连接（即把每层输入直接加到输出上的那条旁路）…"
section: "ai-news"
rank: 1
edition: 0
section_rank: 1
score: 7.0
status: "Demonstrated"
source_name: "research.google"
source_url: "https://research.google/blog/supercharging-transformer-residual-connections/"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50672565"
published_at: "2026-11-27T23:06:29+00:00"
tags: ["transformer architecture", "model efficiency", "attention mechanisms", "Google Research", "AI research"]
topics: ["transformer-architecture", "model-efficiency", "attention-mechanisms", "google-research", "ai-research"]
order: "20261128-0-998"
image: "/assets/stories/2026-11-28/google-s-deepcrossattention-claims-up-to-3x-speedup-at-comparable-bcf3-share.jpg"
art: "/assets/stories/2026-11-28/google-s-deepcrossattention-claims-up-to-3x-speedup-at-comparable-bcf3.jpg"
thumb: "/assets/stories/2026-11-28/google-s-deepcrossattention-claims-up-to-3x-speedup-at-comparable-bcf3-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/gdb5f523af4ef192a230a16d55d9d6334e48177613211e117660aab4f14aa2aa93c357fec2d7543671c68c7cabbd3e216235b91032dd7ba111780d7a8ede31901_1280.jpg", "author": "ann_zima", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/data-center-industry-2927337/", "provider": "Pixabay", "width": 4196, "height": 2447}
---

{% raw %}
<div class="story-lead" markdown="1">

Google Research 在博客中提出 DeepCrossAttention（DCA）：不改动 transformer 的基本组件，而是改动残差连接（即把每层输入直接加到输出上的那条旁路），并把注意力从同一层的 token 之间扩展到跨层——每个 token 对之前所有层的表示做一次动态加权的组合。博客称，这一改动在模型质量相当的情况下带来最高 3 倍的提速，并称将 DCA 加装到已预训练好的模型上、再短暂继续训练，在 LM1B 上把困惑度（perplexity，语言模型预测下一个 token 的不确定度，越低越好）降低了 0.19，而同样条件下常规继续训练只降低 0.02。

上述数字均为 Google 自述的实验结果，尚无第三方复现；可得信息中也没有说明 3 倍提速是在多大的模型、什么硬件、与哪个基线对比下测得的。这项结果目前停留在研究阶段。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** Google Research 的博客与 arXiv 论文（ICML 2025）报告，DeepCrossAttention 通过改造 transformer 残差连接、在层间做深度交叉注意力，在 LM1B 语言建模实验中达到同等质量最多快 3 倍，新增参数量可忽略。
- **尚未证实：** 上述加速与质量结论仅来自 Google 自己的论文实验，尚无独立复现或第三方基准；现有公开摘要未说明代码或模型权重是否及何时开放，也未界定可迁移到哪些现有模型。

</div>

## 背景

残差连接是 Transformer 中把每一层的输出直接加到主干表示上的“捷径”，使深层网络更容易训练；但 Google 的 DCA 论文指出，简单相加会稀释前面层的重要信息。DCA 改为让每个 token 对之前各层的表示做带可学习权重的跨层注意力，按需混合历史层的信息，而不是固定求和。

## 为什么重要

对训练模型的人来说，最可操作的线索是 DCA 的“加装”路径：如果 0.19 对 0.02 的困惑度改善能在更大规模上复现，团队也许可以用短时间的继续训练升级已有 checkpoint，而不必从头重训。但这两个数字来自 Google 在 LM1B 上的自测，模型规模远小于当下主力模型；是否提供可用的实现、提速是在什么硬件上测得，目前都不清楚——在据此规划训练预算之前，应先等独立复现或在自身工作负载上的验证。

## 延伸阅读

- [Supercharging transformer residual connections](https://research.google/blog/supercharging-transformer-residual-connections/)
- [DeepCrossAttention : Supercharging Transformer Residual ...](https://arxiv.org/html/2502.06785)
- [Supercharging transformer residual connections - Google Research](https://research.google/blog/supercharging-transformer-residual-connections/)
- [[2502.06785] DeepCrossAttention: Supercharging Transformer ...](https://arxiv.org/abs/2502.06785)

<div class="community" markdown="1">

## 社区讨论（观点，不是证据）

有评论者（londons_explore）认为，在训练中途改动模型的形状与维度并继续训练这条路线很有前景；也有人（pollorollo）批评博客用折线图把本无时间先后的若干方法连起来，应当改用柱状图。另有评论者（amluto）推测跨层注意力或许能缓解模型在字符级计数（例如“strawberry”里有多少个 r）上的著名失败，但这只是猜测，并非博客给出的结论。

</div>

{% endraw %}
