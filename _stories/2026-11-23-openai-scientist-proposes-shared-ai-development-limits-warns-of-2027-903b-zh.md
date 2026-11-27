---
layout: story
lang: zh
date: 2026-11-23 13:28:10 -0500
issue: "2026-11-23"
story_id: "openai-scientist-proposes-shared-ai-development-limits-warns-of-2027-903b"
permalink: "/zh/2026/11/23/openai-scientist-proposes-shared-ai-development-limits-warns-of-2027-903b/"
title: "OpenAI首席科学家提议设AI开发行业统一门槛"
dek: "11月22日，OpenAI首席科学家雅库布·帕霍茨基发文，提议各家AI企业建立行业统一标准，对先进模型的开发设置共同限制：在研究人员能更可靠地理解和监控模型行为之前，不突破约定的发展门槛。"
description: "11月22日，OpenAI首席科学家雅库布·帕霍茨基发文，提议各家AI企业建立行业统一标准，对先进模型的开发设置共同限制：在研究人员能更可靠地理解和监控模型行为之前，不突破约定的发展门槛。"
section: "ai-news"
rank: 10
edition: 0
section_rank: 10
score: 7.0
status: "Announced"
source_name: "GeekPark (极客公园)"
source_url: "http://www.geekpark.net/news/374304"
via: null
discussion_url: null
published_at: "2026-11-23T01:22:36+00:00"
tags: ["OpenAI", "AI安全", "模型评测", "预训练", "AI治理"]
topics: ["openai", "ai", "ai"]
order: "20261123-0-989"
image: "/assets/stories/2026-11-23/openai-scientist-proposes-shared-ai-development-limits-warns-of-2027-903b-share.jpg"
art: "/assets/stories/2026-11-23/openai-scientist-proposes-shared-ai-development-limits-warns-of-2027-903b.jpg"
thumb: "/assets/stories/2026-11-23/openai-scientist-proposes-shared-ai-development-limits-warns-of-2027-903b-640.jpg"
photo_credit: {"url": "https://thumb.wikimedia.org/wikipedia/commons/thumb/4/4e/Cafeteria_in_the_new_building_at_ESO_Headquarters_%282017_10_22_ABC_Building_Cafeteria_Charity_360-CC%29.jpg/1920px-Cafeteria_in_the_new_building_at_ESO_Headquarters_%282017_10_22_ABC_Building_Cafeteria_Charity_360-CC%29.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail", "author": "ESO/P. Horálek", "licence": "CC BY 4.0", "licence_url": "https://creativecommons.org/licenses/by/4.0", "source_url": "https://commons.wikimedia.org/wiki/File:Cafeteria_in_the_new_building_at_ESO_Headquarters_(2017_10_22_ABC_Building_Cafeteria_Charity_360-CC).jpg", "provider": "Wikimedia Commons", "width": 12964, "height": 6482}
---

{% raw %}
<div class="story-lead" markdown="1">

11月22日，OpenAI首席科学家雅库布·帕霍茨基发文，提议各家AI企业建立行业统一标准，对先进模型的开发设置共同限制：在研究人员能更可靠地理解和监控模型行为之前，不突破约定的发展门槛。他提出用困惑度（衡量模型预测下一个文本token的能力，数值越低表示预测越强）追踪预训练进展，并披露OpenAI内部数据：GPT-3.5对数困惑度约0.99、GPT-4约0.91；低于0.8时模型在网络安全和数学上出现新能力，约0.76时在部分开放数学问题上取得突破，预计0.68—0.7区间可能出现更多变革性能力，但具体是什么尚不确定。

帕霍茨基警告，AI最早可能在2027年推动预训练技术快速进展，而对齐和行为监控可能跟不上；他建议企业共同制定评测、透明度和安全红队标准，并在模型首次投入使用前完成评估，奥尔特曼公开支持这一提议，称希望行业就共同限制达成一致。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** 据极客公园援引 CnBeta 的报道，OpenAI 首席科学家雅库布·帕霍茨基（Jakub Pachocki）于 11 月 22 日发表文章，提议各家 AI 企业为先进模型开发建立可测量的行业共同限制，并以困惑度（perplexity，衡量模型预测下一个文本 Token 的能力）等可跨企业追踪的指标设定首个开发门槛；TechCrunch 同日也报道了这篇文章，并指出其核心正是困惑度这一度量。OpenAI CEO 萨姆·奥尔特曼公开称这是 OpenAI 一段时间以来最重要的文章之一，并支持行业就共同限制达成一致。文章还披露了 OpenAI 内部的对数困惑度数据：GPT-3.5 约 0.99、GPT-4 约 0.91。
- **尚未证实：** 对数困惑度降至 0.8 时出现网络安全与数学新能力、约 0.76 时在部分开放数学问题上取得突破，以及进入 0.68–0.7 区间可能出现“变革性能力”，这些门槛与对应现象都只是 OpenAI 一方的内部观察；关于最早 2027 年预训练出现快速进展、而对齐与行为监控可能跟不上的判断同样属于该公司预测，未经独立验证。目前没有任何其他前沿实验室公开承诺加入或公布可比的困惑度数据，也尚无成形的标准、评测协议或实施时间表；中文报道属于二手汇总，未附原文链接和完整评测方法。

</div>

## 背景

困惑度（perplexity）衡量模型预测下一个文本 Token 的能力，数值越低说明预测越准；帕霍茨基把它当作预训练进展的替代标尺，理由是传统能力评测基准会随技术进步迅速过时。围绕模型行为监控，OpenAI 此前已有动作：AI Daily Radar 11 月 16 日的日报曾报道，OpenAI 启动首阶段「内嵌评估」，邀请 Apollo Research、METR、Transluce 和 Goodfire 四家外部机构进入内部独立评估模型的对齐、防护与监控系统，但未公布覆盖哪些模型、时间表与任何结论。此次提议的不同之处在于把评估从单家公司内部推到跨企业层面，用可共同追踪的指标设定统一的开发门槛。

## 为什么重要

对前沿实验室来说，这一提议若被采纳，会把预训练阶段的困惑度阈值变成与红队测试、透明度标准并列的开发闸门，而不是等模型发布后再用容易过时的任务基准评估；但目前仍只是提议，文章没有说明阈值如何执行或由谁核验，也尚无企业宣布加入。

## 后续看点

关注其他前沿AI实验室是否公开响应这一行业统一限制提议，以及OpenAI是否公布支撑0.68—0.7阈值判断的评测方法和数据。

## 延伸阅读

- [2026-11-16 — OpenAI 启动首批内嵌评估：Apollo、METR 等四家机构参与](https://openai.com/index/our-first-phase-of-embedded-assessments)
- [OpenAI 's Pachocki urges frontier pause at... | AI Weekly](https://aiweekly.co/alerts/openais-pachocki-urges-frontier-pause-at-068-07-perplexity)
- [OpenAI chief scientist proposes measurable limits on advanced AI ...](https://forklog.com/en/openai-chief-scientist-proposes-measurable-limits-on-advanced-ai-development/)
- [OpenAI ’s chief scientist has thoughts on how to limit AI development](https://techcrunch.com/2026/11/22/openais-chief-scientist-has-thoughts-on-how-to-limit-ai-development/)

{% endraw %}
