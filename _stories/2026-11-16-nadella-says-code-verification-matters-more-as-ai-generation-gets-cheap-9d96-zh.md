---
layout: story
lang: zh
date: 2026-11-16 06:00:00 -0500
issue: "2026-11-16"
story_id: "nadella-says-code-verification-matters-more-as-ai-generation-gets-cheap-9d96"
permalink: "/zh/2026/11/16/nadella-says-code-verification-matters-more-as-ai-generation-gets-cheap-9d96/"
title: "纳德拉访谈：代码生成变便宜后，验证与决策成为关键"
dek: "《The Pragmatic Engineer》作者 Gergely Orosz 发布了一期与微软 CEO 萨提亚·纳德拉的对谈，主题是当 AI 写代码变得廉价之后，软件工程的重心如何转移。"
description: "《The Pragmatic Engineer》作者 Gergely Orosz 发布了一期与微软 CEO 萨提亚·纳德拉的对谈，主题是当 AI 写代码变得廉价之后，软件工程的重心如何转移。"
section: "ai-news"
rank: 205
edition: 2
section_rank: 5
score: 7.0
status: "Available"
source_name: "The Pragmatic Engineer"
source_url: "https://newsletter.pragmaticengineer.com/p/software-engineering-after-code-becomes"
via: "Techmeme"
discussion_url: null
published_at: "2026-11-16T19:15:09+00:00"
tags: ["AI coding", "code verification", "software engineering", "Satya Nadella", "Microsoft"]
topics: ["ai-coding", "code-verification", "software-engineering", "satya-nadella", "microsoft"]
order: "20261116-2-994"
image: "/assets/stories/2026-11-16/nadella-says-code-verification-matters-more-as-ai-generation-gets-cheap-9d96-share.jpg"
art: "/assets/stories/2026-11-16/nadella-says-code-verification-matters-more-as-ai-generation-gets-cheap-9d96.jpg"
thumb: "/assets/stories/2026-11-16/nadella-says-code-verification-matters-more-as-ai-generation-gets-cheap-9d96-640.jpg"
photo_credit: {"url": "https://thumb.wikimedia.org/wikipedia/commons/thumb/3/30/Building92microsoft.jpg/1920px-Building92microsoft.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail", "author": "Coolcaesar", "licence": "CC BY-SA 4.0", "licence_url": "https://creativecommons.org/licenses/by-sa/4.0", "source_url": "https://commons.wikimedia.org/wiki/File:Building92microsoft.jpg", "provider": "Wikimedia Commons", "width": 5184, "height": 3456}
---

{% raw %}
<div class="story-lead" markdown="1">

《The Pragmatic Engineer》作者 Gergely Orosz 发布了一期与微软 CEO 萨提亚·纳德拉的对谈，主题是当 AI 写代码变得廉价之后，软件工程的重心如何转移。纳德拉的核心论点是：代码生成的成本下降，会推高代码验证的价值，同时让“决策模型”——即团队如何判断该做什么、该信什么——变得更重要。

访谈还涉及微软内部的自愿离职（voluntary exit）方案。节目已在 YouTube、Apple 与 Spotify 上线，页面顶部提供逐字稿、底部提供时间戳。

需要说明的是，目前可核实的仅是这期访谈的存在与议题，纳德拉的具体论述细节需以逐字稿为准。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** 据 The Pragmatic Engineer 与 Techmeme 的条目，Gergely Orosz 制作并发布了这期与微软 CEO 萨提亚·纳德拉的问答节目，议题涵盖代码生成廉价化后代码验证的重要性、微软的自愿离职方案以及决策模型；节目在 YouTube、Apple、Spotify 可收听收看，并提供文字稿。
- **尚未证实：** 纳德拉本人的原话、具体数字与微软相关政策的细节，均未在所给摘要中出现；关于自愿离职方案的规模、适用对象与时间表，以及“决策模型”的具体所指，都需要查阅节目逐字稿或微软官方说明后才能确认。

</div>

## 背景

当 Claude Code、Cursor 这类工具把写代码的成本压得很低，瓶颈就从“生成代码”转向“确认代码对不对、安不安全”，纳德拉所说的验证与决策模型正是指这一环节。AI Daily Radar 11 月 15 日的日报曾报道，安全研究机构 crissyfield.de 称用 AI 应用构建器 Lovable 生成的应用泄露了护照信息和 20 多万条私信，Lovable 的安全负责人把原因归结为 Supabase/Postgres 的行级安全规则（RLS，即决定登录用户能读写哪些数据行的权限规则）配置不足。这一事件正是“生成便宜、验证昂贵”的具体案例。

## 为什么重要

如果按纳德拉的论述，瓶颈会从“写得出”转向“验得准”，那么使用 AI 编码工具的团队最该补的就是测试、代码审查与自动化校验环节——否则生成速度提升只会把风险推到下游。同时，“决策模型”的提法意味着团队需要明确谁来判断 AI 产出的结果是否可以合并上线，而不只是比较生成速度。

## 延伸阅读

- [2026-11-15 — Lovable apps exposed passport data and 200K private messages](https://www.crissyfield.de/research/lovable-en/)

{% endraw %}
