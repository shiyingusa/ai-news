---
layout: story
lang: zh
date: 2026-11-18 06:00:00 -0500
issue: "2026-11-18"
story_id: "harvard-researchers-link-ai-coding-agents-to-a-code-review-bottleneck-5c44"
permalink: "/zh/2026/11/18/harvard-researchers-link-ai-coding-agents-to-a-code-review-bottleneck-5c44/"
title: "哈佛研究：AI 编码代理把瓶颈从写代码移到代码审查"
dek: "据 ComplexDiscovery 报道，哈佛研究人员得出的结论是：AI 编码代理普及后，开发流程的主要瓶颈已从编写代码转移到审查代码。"
description: "据 ComplexDiscovery 报道，哈佛研究人员得出的结论是：AI 编码代理普及后，开发流程的主要瓶颈已从编写代码转移到审查代码。"
section: "ai-news"
rank: 2
edition: 0
section_rank: 2
score: 7.0
status: "Demonstrated"
source_name: "complexdiscovery.com"
source_url: "https://complexdiscovery.com/harvard-researchers-find-ai-coding-agents-shifted-the-bottleneck-to-code-review/"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50538303"
published_at: "2026-11-17T21:16:12+00:00"
tags: ["AI coding agents", "code review", "software engineering", "developer productivity", "AI research"]
topics: ["ai-coding-agents", "code-review", "software-engineering", "developer-productivity", "ai-research"]
order: "20261118-0-997"
image: "/assets/stories/2026-11-18/harvard-researchers-link-ai-coding-agents-to-a-code-review-bottleneck-5c44-share.jpg"
art: "/assets/stories/2026-11-18/harvard-researchers-link-ai-coding-agents-to-a-code-review-bottleneck-5c44.jpg"
thumb: "/assets/stories/2026-11-18/harvard-researchers-link-ai-coding-agents-to-a-code-review-bottleneck-5c44-640.jpg"
photo_credit: {"url": "https://upload.wikimedia.org/wikipedia/commons/8/83/Chuck_Turner_%28Boston_City_Councilor%29_talks_to_Harvard_University_Police_officer_at_rally_on_May_10%2C_2007_for_the_Harvard_University_AlliedBarton_campus_security_workers_strike_%2869371%29.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail_unscaled", "author": "stand4security on Flickr", "licence": "CC BY 2.0", "licence_url": "https://creativecommons.org/licenses/by/2.0", "source_url": "https://commons.wikimedia.org/wiki/File:Chuck_Turner_(Boston_City_Councilor)_talks_to_Harvard_University_Police_officer_at_rally_on_May_10,_2007_for_the_Harvard_University_AlliedBarton_campus_security_workers_strike_(69371).jpg", "provider": "Wikimedia Commons", "width": 1600, "height": 1066}
---

{% raw %}
<div class="story-lead" markdown="1">

据 ComplexDiscovery 报道，哈佛研究人员得出的结论是：AI 编码代理普及后，开发流程的主要瓶颈已从编写代码转移到审查代码。该报道称这一发现引发了大量从业者讨论，但目前只有二手报道，没有给出论文标题、作者、样本规模、所用模型版本或具体测量指标。报道本身也没有说明这项研究是预印本、同行评审论文，还是尚未公开的内部成果。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** ComplexDiscovery 报道称，哈佛研究人员发现 AI 编码代理把开发者瓶颈推向代码审查环节；Hacker News 上出现了大量从业者就此展开的讨论。
- **尚未证实：** 研究的具体结论强度与适用范围，包括论文标题、作者、发表状态、样本量、所用模型及版本、衡量“瓶颈转移”的指标，以及是否经过独立复现；这些均只见于二手描述，来源未提供可核查细节。

</div>

## 背景

这项结论出自哈佛的 Fiona Chen 与 James Stratton 的一篇工作论文：他们使用工程效能分析平台 Jellyfish 的数据，覆盖约 718 家企业、约 70 万名开发者从 2021 年 1 月到 2026 年 3 月的记录。研究称，AI 编码代理让工程师多写出约 30% 的代码，但一次拉取请求（pull request，代码合入前的评审请求）的评审时间随之上升约 49%，因此企业实际交付的软件量没有同步增长。也就是说，在讨论 AI 编码工具的真实产出时，“评审成为新瓶颈”是这项研究给出的核心前提。

## 为什么重要

如果瓶颈确实落在审查端，团队的约束条件就从“写得够快”变成“看得够快”：有评论者指出，合并请求里的代码量变大，且 AI 倾向给出过度设计的方案，审查者需要更多时间判断是否真的需要这些复杂度。对采用编码代理的团队来说，这意味着要同步投入审查容量与审查工具（例如让多个代理互相审查），否则吞吐量会卡在评审队列上。

## 社区讨论

多位从业者称自己的日常工作已变成审查 AI 写的代码：一位有 25 年经验的开发者表示，AI 写得不比自己差，找问题时甚至更好，但他仍强调审查还有“理解代码”的作用；另一位专职做代码审查的评论者则认为，AI 生成的合并请求代码更多、方案常常过度设计。也有人质疑这类大学研究已经过时，认为学界跟不上实践节奏，另有医疗行业开发者强调仍有人坚持手写代码与测试。

## 延伸阅读

- [Harvard study of 718 firms finds AI coding agents ' output... | Pondero](https://pondero.ai/news/2026-10-12-harvard-jellyfish-code-review-bottleneck/)
- [AI Coding Agents and the Code Review Bottleneck ( 2026 Data)](https://dromeas.ai/blog/ai-coding-agents-code-review-bottleneck)
- [AI Coding Agents Add Code ; Review Is the Bottleneck · SW Architect](https://www.swarchitect.net/en/ai-coding-agents-review-bottleneck-2026-10/)

{% endraw %}
