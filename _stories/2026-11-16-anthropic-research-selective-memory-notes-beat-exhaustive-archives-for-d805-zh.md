---
layout: story
lang: zh
date: 2026-11-16 06:00:00 -0500
issue: "2026-11-16"
story_id: "anthropic-research-selective-memory-notes-beat-exhaustive-archives-for-d805"
permalink: "/zh/2026/11/16/anthropic-research-selective-memory-notes-beat-exhaustive-archives-for-d805/"
title: "Anthropic 研究：Agent 记忆关键在于知道该忘什么"
dek: "Anthropic 的一项研究考察 Claude 如何跨会话保留知识，结论是：经过筛选的少量记忆笔记明显优于穷举式存档。"
description: "Anthropic 的一项研究考察 Claude 如何跨会话保留知识，结论是：经过筛选的少量记忆笔记明显优于穷举式存档。"
section: "ai-news"
rank: 9
edition: 0
section_rank: 9
score: 7.0
status: "Demonstrated"
source_name: "The Decoder"
source_url: "https://the-decoder.com/anthropic-says-the-key-to-agent-memory-is-knowing-what-to-forget-not-how-much-to-store/"
via: null
discussion_url: null
published_at: "2026-11-16T15:25:48+00:00"
tags: ["agent memory", "Anthropic", "Claude", "LLM agents", "context management"]
topics: ["agent-memory", "anthropic", "claude", "llm-agents", "context-management"]
order: "20261116-0-990"
image: "/assets/stories/2026-11-16/anthropic-research-selective-memory-notes-beat-exhaustive-archives-for-d805-share.jpg"
art: "/assets/stories/2026-11-16/anthropic-research-selective-memory-notes-beat-exhaustive-archives-for-d805.jpg"
thumb: "/assets/stories/2026-11-16/anthropic-research-selective-memory-notes-beat-exhaustive-archives-for-d805-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g890fea8df3b02edca43bc85d9a4fadc80d29c8a96bdac06144118c66d6852d45e90ecf8ea95b7b3b0da4fa74dd60d8413d60f713148d127345b2cd1f7fdf99a2_1280.jpg", "author": "Akela999", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/data-center-engine-room-2476790/", "provider": "Pixabay", "width": 4096, "height": 2160}
---

{% raw %}
<div class="story-lead" markdown="1">

Anthropic 的一项研究考察 Claude 如何跨会话保留知识，结论是：经过筛选的少量记忆笔记明显优于穷举式存档。据 The Decoder 报道，在《宝可梦 红》测试中，较新的 Claude Fable 5 只保留少量策略文件，进展就达到保留 400 多个文件的旧版 Sonnet 3.7 的四倍。

研究还提出一个名为 "Dreaming" 的流程，可回溯性地修正错误的记忆。由于这是二手报道，论文原文、具体评测方法和产品化计划均未披露。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** 据 The Decoder 报道，Anthropic 研究了 Claude 的跨会话记忆机制，并在《宝可梦 红》测试中得出“选择性笔记优于穷举存档”的结果——较新的 Claude Fable 5 进展约为 Sonnet 3.7 的四倍。
- **尚未证实：** 四倍差距如何测量、各模型分别保留了多少文件、"Dreaming" 纠错流程的技术细节，以及这些方法是否会进入 Claude 产品；报道未提供论文链接、发布时间或任何独立复现结果。

</div>

## 背景

大模型的上下文窗口只在单次会话内有效，跨会话时它不会自动记住之前做过什么，因此智能体通常要把对话记录、任务进度等写入外部文件，供后续会话读取。Anthropic 在关于智能体记忆组件的研究中把记忆组织成多层结构，其中一层是 Claude 自己写下的“记忆笔记”（memory notes，即对关键观察的摘录）；与之配套的还有一个名为“Dreaming”的离线反思过程，让模型在会话之间回看并修正此前的记忆。

## 为什么重要

对构建 agent 的开发者来说，这条结果指向一个具体的工程选择：与其把全部会话历史堆进上下文或记忆库，不如维护少量经过筛选、并定期校正的笔记——报道中四倍的进展差距正来自“只保留少量策略文件”与“保留 400 多个文件”的对比。同时，"Dreaming" 这类纠错步骤意味着记忆系统需要额外的维护环节，而不只是写入和检索。

## 延伸阅读

- [Can Claude dream now? Anthropic explores human-like machine...](https://interestingengineering.com/ai-robotics/anthropic-claude-dreaming-memory-research)
- [The components of agent memory \ Anthropic](https://www.anthropic.com/research/components-of-agent-memory)
- [Anthropic Agent Memory Explained: Architecture, Dreams... - YouTube](https://www.youtube.com/watch?v=RmRfRhLABaU)

{% endraw %}
