---
layout: story
lang: zh
date: 2026-11-17 06:00:00 -0500
issue: "2026-11-17"
story_id: "bfl-s-case-for-visual-intelligence-and-multimodal-training-86b9"
permalink: "/zh/2026/11/17/bfl-s-case-for-visual-intelligence-and-multimodal-training-86b9/"
title: "Black Forest Labs：从图像走向多模态视觉智能"
dek: "A concise Latent Space episode recap that captures BFL's arguments for multimodal visual intelligence and a few…"
description: "A concise Latent Space episode recap that captures BFL's arguments for multimodal visual intelligence and a few…"
section: "tech-blog"
rank: 18
edition: 0
section_rank: 2
score: 6.0
status: null
source_name: "Latent Space"
source_url: "https://latent.space/p/bfl/"
via: null
discussion_url: null
published_at: "2026-11-16T21:38:03+00:00"
tags: ["video generation", "multimodal training", "temporal consistency", "latent diffusion", "model training strategy"]
topics: ["video-generation", "multimodal-training", "temporal-consistency", "latent-diffusion", "model-training-strategy"]
order: "20261117-0-981"
image: "/assets/stories/2026-11-17/bfl-s-case-for-visual-intelligence-and-multimodal-training-86b9-share.jpg"
art: "/assets/stories/2026-11-17/bfl-s-case-for-visual-intelligence-and-multimodal-training-86b9.jpg"
thumb: "/assets/stories/2026-11-17/bfl-s-case-for-visual-intelligence-and-multimodal-training-86b9-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g55ebfdeab599ea1620a492333c4fb1604180b82794ba6495e4dd9ea679466f37c4d45a14402eeba7d4205a13ce60c1deddb0053b01f98a821e1b127a0f87195a_1280.jpg", "author": "cookieone", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/internet-information-service-system-8097838/", "provider": "Pixabay", "width": 6000, "height": 4000}
---

{% raw %}
<div class="story-lead" markdown="1">

A concise Latent Space episode recap that captures BFL's arguments for multimodal visual intelligence and a few practical engineering lessons, but without enough technical depth or evidence to be more than a useful niche overview.

</div>

## 背景

Black Forest Labs（BFL）由 Stable Diffusion 核心成员在 Stability AI 动荡后创立，先以 FLUX 图像模型立足。本次访谈讨论他们为何从图像生成进一步转向视频、音频乃至世界模型。

## 方案

Andreas Blattmann 用接球解释其“视觉智能”：静态图告诉你在哪里，视频展示它如何到达，声音则提示撞击发生的时刻，即使画面没有拍到。BFL 据此在 FLUX 3 上联合训练这三种信号。移动镜头从人物正面转向背面时，模型必须补出后脑勺；作者认为二维视频包含大量关于其他视角的证据，这虽不能证明模型理解物理，却比判断单帧是否逼真更有意义。工程上，逐帧独立放大可能让每帧都清晰，播放时细节却闪烁，因此 BFL 的视频超分器复用 FLUX 3 骨干以维持时间一致性。训练算力如何分配也有权衡：自回归可一次学习样本中的所有 token，扩散模型则能把长采样蒸馏为少步，关键看成本落在训练还是等待生成。Dustin Podell 的 Kontext 原型只用少量带关系标签的照片训练数小时，便能让模型把 logo 放到衬衫上，效果粗糙但足以支撑团队随后投入数月改进数据和模型。

## 启示

BFL 的核心论点是，视觉智能不只是生成更漂亮的单帧，而是从视频与音频中学习运动、时间连续性和跨视角一致性；工程上则应以低成本原型判断何时值得加大训练与数据投入。

{% endraw %}
