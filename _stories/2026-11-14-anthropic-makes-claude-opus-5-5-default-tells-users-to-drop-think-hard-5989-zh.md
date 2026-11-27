---
date: 2026-11-14 06:00:00 -0500
layout: "story"
lang: "zh"
issue: "2026-11-14"
story_id: "anthropic-makes-claude-opus-5-5-default-tells-users-to-drop-think-hard-5989"
permalink: "/zh/2026/11/14/anthropic-makes-claude-opus-5-5-default-tells-users-to-drop-think-hard-5989/"
title: "Anthropic 将 Claude Opus 5.5 设为付费版默认模型并改推新提示方式"
dek: "Anthropic 已把 Claude Opus 5.5 设为所有付费方案的默认模型，同时发布提示指南，要求用户放弃旧习惯。"
section: "ai-news"
rank: 3
section_rank: 3
score: 7.0
status: "Released"
source_name: "The Decoder"
source_url: "https://the-decoder.com/anthropic-says-outdated-prompting-habits-are-slowing-down-claude-opus-5-5/"
discussion_url: null
published_at: null
tags: ["Anthropic", "Claude Opus 5.5", "prompting", "model defaults", "developer guidance"]
topics: ["anthropic", "claude-opus-5-5", "prompting", "model-defaults", "developer-guidance"]
order: "20261114-996"
image: "/assets/stories/2026-11-14/anthropic-makes-claude-opus-5-5-default-tells-users-to-drop-think-hard-5989-share.jpg"
art: "/assets/stories/2026-11-14/anthropic-makes-claude-opus-5-5-default-tells-users-to-drop-think-hard-5989.jpg"
thumb: "/assets/stories/2026-11-14/anthropic-makes-claude-opus-5-5-default-tells-users-to-drop-think-hard-5989-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g8292de1b20215f8df60d7283bc5f79a63f4d303eae6e88119d5b61af2ba1c4eed7c1a300f26420cef8cd55f624b5121e6549d10fca286309aee676e8d0e66ea0_1280.jpg", "author": "Akela999", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/data-center-engine-room-2476790/", "provider": "Pixabay", "width": 4096, "height": 2160}
description: "Anthropic 已把 Claude Opus 5.5 设为所有付费方案的默认模型，同时发布提示指南，要求用户放弃旧习惯。"
---

{% raw %}
<div class="story-lead" markdown="1">

Anthropic 已把 Claude Opus 5.5 设为所有付费方案的默认模型，同时发布提示指南，要求用户放弃旧习惯。指南的核心建议是：不要再写“think hard”（让模型“努力思考”）这类指令，而是从 Medium effort（中等推理强度）起步。

这一建议来自 Anthropic 自己的说明，The Decoder 的报道只是转述其要点，未给出配套的基准测试或量化数据，因此实际提速幅度尚不清楚。

</div>

## 背景

过去常用的“think hard”等提示，是针对需要手动触发长推理的旧版 Claude 形成的习惯。据 Anthropic 的 Opus 5.5 提示文档和第三方解读，这一版本的思考始终开启，推理投入改由五档 effort 控制，默认档为 Medium；有解读称其 Medium 档的质量已超过 Opus 5 的 High 档，因此用户不必再用文字催促模型“更努力思考”。

## 影响

对使用付费方案的用户和开发者来说，默认模型已切换为 Opus 5.5，原先针对旧模型调好的提示词（尤其是依赖“think hard”等措辞的提示词）需要重新验证；按指南做法，应先用 Medium effort 测试效果，再决定是否提高推理强度。

## 延伸阅读

- [How to Prompt Claude Opus 5.5: What Changed and What to ...](https://betterstack.com/community/guides/ai/claude-opus-55-prompting-guide/)
- [Claude Opus 5.5 Effort Levels: Low to Max Explained](https://www.techgeum.com/blog/ai/claude-opus-5-5-effort-levels)

{% endraw %}
