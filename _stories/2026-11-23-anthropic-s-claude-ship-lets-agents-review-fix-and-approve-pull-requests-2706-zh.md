---
layout: story
lang: zh
date: 2026-11-23 18:23:03 -0500
issue: "2026-11-23"
story_id: "anthropic-s-claude-ship-lets-agents-review-fix-and-approve-pull-requests-2706"
permalink: "/zh/2026/11/23/anthropic-s-claude-ship-lets-agents-review-fix-and-approve-pull-requests-2706/"
title: "Anthropic 推出 Claude Ship，AI 代理可审查、修复并批准 PR"
dek: "Anthropic 发布名为 Claude Ship 的新产品，让 Claude 能审查、修复并批准 pull request（PR，即代码合并请求）。"
description: "Anthropic 发布名为 Claude Ship 的新产品，让 Claude 能审查、修复并批准 pull request（PR，即代码合并请求）。"
section: "ai-news"
rank: 203
edition: 2
section_rank: 3
score: 7.0
status: "Released"
source_name: "TechCrunch AI"
source_url: "https://techcrunch.com/2026/11/23/anthropic-launches-claude-ship-letting-ai-agents-review-fix-and-approve-code-changes/"
via: null
discussion_url: null
published_at: "2026-11-23T22:05:50+00:00"
tags: ["AI agents", "AI coding", "Anthropic", "developer tools", "code review"]
topics: ["ai-agents", "ai-coding", "anthropic", "developer-tools", "code-review"]
order: "20261123-2-996"
image: "/assets/stories/2026-11-23/anthropic-s-claude-ship-lets-agents-review-fix-and-approve-pull-requests-2706-share.jpg"
art: "/assets/stories/2026-11-23/anthropic-s-claude-ship-lets-agents-review-fix-and-approve-pull-requests-2706.jpg"
thumb: "/assets/stories/2026-11-23/anthropic-s-claude-ship-lets-agents-review-fix-and-approve-pull-requests-2706-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/gf197094dd7ec7811ecc8e63b920a2339599143b705da4f4cd89990cb95a6fd6828642e29c1366631ddca47550465effcf79f68332161577784d3da6cc8de4737_1280.jpg", "author": "Innovalabs", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/software-development-developer-6523979/", "provider": "Pixabay", "width": 7360, "height": 4912}
---

{% raw %}
<div class="story-lead" markdown="1">

Anthropic 发布名为 Claude Ship 的新产品，让 Claude 能审查、修复并批准 pull request（PR，即代码合并请求）。伴随该产品推出的两个新代理——PR Steward 和 Claude Approvals——于发布当天进入 beta：据 The Verge 报道，PR Steward 会在 CI 检查失败、合并冲突，以及来自 Code Review、其他审查工具或团队成员的评审意见出现时介入处理。

ZDNET 称该 beta 面向 Claude Team 与 Enterprise 套餐用户，针对 GitHub 上的 pull request，并按团队既定策略执行批准。代码审查本身并非新能力：Anthropic 的 Code Review 功能于今年 3 月公布、10 月正式可用，此次新增的是自动修复与批准环节。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** Anthropic 发布了 Claude Ship，Claude 现可审查、修复并批准 PR；PR Steward 与 Claude Approvals 两个代理于同日开启 beta（The Verge）；Code Review 功能 3 月公布、10 月正式可用（Anthropic 官方资源页）。ZDNET 报道称 beta 面向 Claude Team 和 Enterprise 套餐、作用于 GitHub PR 并依据团队策略。
- **尚未证实：** 定价、正式开放（GA）时间、代理批准权限的具体边界（例如能否满足分支保护与审计要求）均未披露；也没有独立测试或用户实测结果，实际修复与批准质量仍只有厂商说法。

</div>

## 背景

Claude 的代码审查能力并非全新：据 The Verge 报道，Code Review 功能今年 3 月发布，直到 10 月才正式普遍可用；此次真正的增量是随 Claude Ship 一同进入测试阶段的 PR Steward 与 Claude Approvals 两个代理。AI Daily Radar 11 月 18 日的日报曾提到，哈佛研究人员（经二手报道）认为 AI 编码代理已把开发者的主要瓶颈从写代码转移到审查代码，而这正是 Anthropic 这次想接手的环节。

## 为什么重要

对使用 Claude Code 的团队来说，实际变化是审批权可以按团队策略下放：PR Steward 只介入失败的 CI 检查、合并冲突和评审反馈，不负责批准或合并；真正按策略批准 PR 的是 Claude Approvals，两者都通过 Claude Code 新增的 `/ship` 命令触发。想把例行修复和审批自动化的团队，需要先在策略里写明哪些改动允许代理批准，并注意这项能力目前仍是面向 Team 与 Enterprise 套餐的 beta。

## 后续看点

关注 Anthropic 何时宣布 Claude Ship 与两个代理从 beta 转为正式可用，以及是否公布代理批准与 GitHub 分支保护规则、审计日志的对接方式；这决定团队能否放心让它真正合并代码。

## 本事件的相关报道

- 2026-11-23 · The Verge AI: [Claude AI can review pull requests and ship fixes on its own now](https://www.theverge.com/ai-artificial-intelligence/1040134/anthropic-claude-ship-ai-pull-requests)
- 2026-11-23 · ZDNET: [Anthropic unveils Claude Ship, letting Claude review, fix, and approve GitHub pull requests based on team policies, in beta for Claude Team and Enterprise tiers (Radhika Rajkumar/ZDNET)](https://www.zdnet.com/innovation/claude-ship-code-how-to-try/)
- 2026-11-23 · TechCrunch AI: [Anthropic launches Claude Ship, letting AI agents review, fix, and approve code changes](https://techcrunch.com/2026/11/23/anthropic-launches-claude-ship-letting-ai-agents-review-fix-and-approve-code-changes/)

## 延伸阅读

- [2026-11-18 — Harvard researchers link AI coding agents to a code-review bottleneck](https://complexdiscovery.com/harvard-researchers-find-ai-coding-agents-shifted-the-bottleneck-to-code-review/)
- [Claude AI can review pull requests and ship fixes on its... | The Verge](https://www.theverge.com/ai-artificial-intelligence/1040134/anthropic-claude-ship-ai-pull-requests)
- [Claude Ship | Automate pull requests review and fixes](https://claude.com/product/claude-ship)
- [Anthropic's Claude Ship Lets Claude Approve Pull Requests by ...](https://aiweekly.co/alerts/anthropics-claude-ship-lets-claude-approve-pull-requests-by-policy)

{% endraw %}
