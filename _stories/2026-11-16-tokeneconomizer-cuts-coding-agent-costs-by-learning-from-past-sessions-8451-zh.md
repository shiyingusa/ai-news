---
layout: story
lang: zh
date: 2026-11-16 06:00:00 -0500
issue: "2026-11-16"
story_id: "tokeneconomizer-cuts-coding-agent-costs-by-learning-from-past-sessions-8451"
permalink: "/zh/2026/11/16/tokeneconomizer-cuts-coding-agent-costs-by-learning-from-past-sessions-8451/"
title: "微软开源 TokenEconomizer：编码智能体成本降 18.4%–30.9%"
dek: "微软研究院与加州大学伯克利分校、微软安全团队联合发布 TokenEconomizer，一个开源插件：它读取编码智能体在同一代码仓库中过往会话的日志，把经验转成后续会话可用的提示，从而在不修改智能体及其底层模型的前提下减少 token 消耗。"
description: "微软研究院与加州大学伯克利分校、微软安全团队联合发布 TokenEconomizer，一个开源插件：它读取编码智能体在同一代码仓库中过往会话的日志，把经验转成后续会话可用的提示，从而在不修改智能体及其底层模型的前提下减少 token 消耗。"
section: "ai-news"
rank: 6
edition: 0
section_rank: 6
score: 7.0
status: "Released"
source_name: "Microsoft Research"
source_url: "https://www.microsoft.com/en-us/research/blog/tokeneconomizer-learning-from-experience-to-make-ai-coding-agents-more-efficient/"
via: null
discussion_url: null
published_at: "2026-11-16T17:01:35+00:00"
tags: ["AI coding agents", "agent efficiency", "Microsoft Research", "tool pruning", "failure-loop intervention"]
topics: ["ai-coding-agents", "agent-efficiency", "microsoft-research", "tool-pruning", "failure-loop-intervention"]
order: "20261116-0-993"
image: "/assets/stories/2026-11-16/tokeneconomizer-cuts-coding-agent-costs-by-learning-from-past-sessions-8451-share.jpg"
art: "/assets/stories/2026-11-16/tokeneconomizer-cuts-coding-agent-costs-by-learning-from-past-sessions-8451.jpg"
thumb: "/assets/stories/2026-11-16/tokeneconomizer-cuts-coding-agent-costs-by-learning-from-past-sessions-8451-640.jpg"
photo_credit: null
---

{% raw %}
<div class="story-lead" markdown="1">

微软研究院与加州大学伯克利分校、微软安全团队联合发布 TokenEconomizer，一个开源插件：它读取编码智能体在同一代码仓库中过往会话的日志，把经验转成后续会话可用的提示，从而在不修改智能体及其底层模型的前提下减少 token 消耗。作者称在 277 个真实 bug 修复任务上，多种编码智能体的成本下降 18.4%–30.9%，所测试的每个仓库成本都下降，任务成功率“基本持平”（帖文未给出具体数字）。插件通过三项机制生效：把仓库特定知识压成一句话“微技能”笔记、裁剪历史显示用不到的工具、在智能体反复撞上同一失败时注入换思路的提示；若提示后仍卡住，开源版只提醒开发者，而不自行终止任务。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** 微软研究院博客称，TokenEconomizer 以开源插件形式发布，仅通过智能体已有接口介入、不改动模型；在 277 个真实 bug 修复任务上，多种编码智能体的成本下降 18.4%–30.9%，且每个测试仓库的成本均下降。这一点由作者团队自己报告。
- **尚未证实：** 成功率“基本持平”没有公布具体数字；18.4%–30.9% 属作者自测，帖文未提供第三方独立复现；也未说明测试了哪些智能体的具体版本、插件代码仓库地址与许可证，以及“裁判模型”是哪一款。

</div>

## 背景

SWE-Bench 是收录真实开源 Python 项目 bug 修复任务的基准。作者先用 Claude Code 在其 60 个任务上做剖析：当某仓库累计完成 5 个以上任务后，30% 的工具调用重复了同仓库此前任务中的动作，仅 7% 命中其他仓库的历史；每一轮下发 23 个工具描述，其中 16 个从未被调用；17% 的失败任务消耗了 32% 的花费。作者还测试了三个流行的开源省成本插件，它们都基于固定策略，只在部分仓库降低开销，这促使作者转向按仓库自适应的方案。

## 为什么重要

对长期在同一代码仓库上反复使用编码智能体的团队，这类“经验层”无需更换模型或改写工作流就能削减账单；但它的收益依赖完整可读的会话日志，且“微技能”笔记要经多次会话确认才会写进起始上下文，因此对一次性任务或全新仓库帮助有限。

## 后续看点

论文中按智能体与仓库拆分的成本、成功率明细是否会公开，以及是否有第三方在自有仓库上复现 18.4%–30.9% 的降幅。

{% endraw %}
