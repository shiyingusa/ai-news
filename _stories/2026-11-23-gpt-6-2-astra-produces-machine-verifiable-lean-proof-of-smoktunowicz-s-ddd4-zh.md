---
layout: story
lang: zh
date: 2026-11-23 13:28:10 -0500
issue: "2026-11-23"
story_id: "gpt-6-2-astra-produces-machine-verifiable-lean-proof-of-smoktunowicz-s-ddd4"
permalink: "/zh/2026/11/23/gpt-6-2-astra-produces-machine-verifiable-lean-proof-of-smoktunowicz-s-ddd4/"
title: "GPT-6.2 Astra 给出 Smoktunowicz 间隙定理的可机器验证 Lean 证明"
dek: "The Decoder 报道，OpenAI 的 GPT-6.2 Astra 独立给出了 Smoktunowicz 间隙定理（gap theorem）的 Lean 形式化证明，且该证明可由机器逐步核验；Lean 是交互式定理证明器…"
description: "The Decoder 报道，OpenAI 的 GPT-6.2 Astra 独立给出了 Smoktunowicz 间隙定理（gap theorem）的 Lean 形式化证明，且该证明可由机器逐步核验；Lean 是交互式定理证明器…"
section: "ai-news"
rank: 3
edition: 0
section_rank: 3
score: 8.0
status: "Demonstrated"
source_name: "The Decoder"
source_url: "https://the-decoder.com/gpt-6-2-astra-solved-a-math-theorem-no-other-ai-could-crack-then-invented-its-own-proof-strategy/"
via: null
discussion_url: null
published_at: "2026-11-23T12:17:01+00:00"
tags: ["AI math", "theorem proving", "Lean", "model evaluation", "OpenAI"]
topics: ["ai-math", "theorem-proving", "lean", "model-evaluation", "openai"]
order: "20261123-0-996"
image: "/assets/stories/2026-11-23/gpt-6-2-astra-produces-machine-verifiable-lean-proof-of-smoktunowicz-s-ddd4-share.jpg"
art: "/assets/stories/2026-11-23/gpt-6-2-astra-produces-machine-verifiable-lean-proof-of-smoktunowicz-s-ddd4.jpg"
thumb: "/assets/stories/2026-11-23/gpt-6-2-astra-produces-machine-verifiable-lean-proof-of-smoktunowicz-s-ddd4-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g471bc68681c746727c88e96b01cbdae7d70fd4af97fbcff856b56c6ac743d92d62b0781dc8ef904ecfc360a1312c8dd1da015e2bed7f11786c84596d9f73dc8b_1280.jpg", "author": "Pexels", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/code-coding-computer-data-1839406/", "provider": "Pixabay", "width": 3543, "height": 2365}
---

{% raw %}
<div class="story-lead" markdown="1">

The Decoder 报道，OpenAI 的 GPT-6.2 Astra 独立给出了 Smoktunowicz 间隙定理（gap theorem）的 Lean 形式化证明，且该证明可由机器逐步核验；Lean 是交互式定理证明器，证明写成代码后能由机器检查，不依赖审稿人的信任，据 Vals AI 称这是同类任务中的首次。报道称，由于 Lean 的数学库 Mathlib 缺少关键基础，模型没有沿用现成路径，而是自行选择了证明策略。

在形式化数学基准 Autoform-Hard 上，Astra 以 56 题解出 49 题位居榜首。这些说法目前来自 The Decoder 的二手报道与 Vals AI 的表述，材料中没有 OpenAI 的原始公告、证明文件或独立数学家的复核结果。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** Vals AI 发布了评测说明与带注释的证明，称 GPT-6.2 Astra 用 94 分钟、约 1800 行 Lean 4 代码给出了代数家 Agata Smoktunowicz 间隙定理（graded domains 情形）的可机器验证形式化证明，且所走路线与已发表的证明不同；另外两家媒体转述了相同的时间和代码行数。The Decoder 报道称 Astra 以 56 项中解出 49 项领跑 Autoform-Hard 榜单。
- **尚未证实：** “首个此类证明”目前只是 Vals AI 的说法（另一家媒体写作“被认为是首个”），没有独立第三方复核该证明或 Autoform-Hard 成绩；该定理此前已有正式发表的数学证明，Astra 完成的是形式化，而非提出新定理，标题中“解出无其他 AI 能解的定理”应在此意义下理解；它自创的“capacity”量及绕开 Mathlib 缺失引理的具体做法，细节也未获独立评估。现有报道中未见 OpenAI 的官方声明。

</div>

## 背景

GPT-6.2 Astra 是 OpenAI 于 11 月 18 日发布的模型；AI Daily Radar 11 月 19 日的日报曾报道，其 API 定价为每百万输入 token 8 美元、输出 40 美元，上下文窗口为 105 万 token。此次排行榜所在的 Autoform-Hard 由评测机构 Vals AI 推出，含 56 道取自研究生与科研级教材的 Lean 4 形式化任务，题目源自 Meta FAIR 的 AutoformBench。

## 为什么重要

对形式化数学和模型评测的使用者来说，这条消息的分量取决于那份 Lean 证明本身能否被第三方编译核验，以及 Mathlib 是否真的缺少所需基础；在看到证明文件并独立跑通之前，「首个」和「自创证明策略」应视为 Vals AI 一侧的说法。关注 Autoform-Hard 的人也应看逐题结果而非仅看 49/56 的总数，因为这个分数只说明该模型在这一套 56 道题上的表现。

## 后续看点

接下来可查的是该 Lean 证明是否公开发布并能被他人在本地编译通过，以及 Astra 能否解出 Autoform-Hard 剩余未完成的 7 道题。

## 延伸阅读

- [GPT-6.2 Astra Formalizes Smoktunowicz's Gap Theorem - vals.ai](https://www.vals.ai/blogs/smoktunowicz-gap-theorem)
- [OpenAI's GPT-6.2 Astra Proves a Math Theorem No Computer Ever ...](https://alphasignal.ai/news/openai-s-gpt-6-2-astra-proves-a-math-theorem-no-computer-ever-could)
- [OpenAI's GPT-6.2 Astra Proves a Math Theorem No Computer Ever ...](https://hermes-ai.net/news/openai-s-gpt-6-2-astra-proves-a-math-theorem-no-computer-ever-could/)
- [2026-11-19 — OpenAI ships GPT-6.2 Astra and Sol with a 20% price cut, and developers push back](http://www.geekpark.net/news/374175)
- [AI Benchmarks for Real-World Tasks | Vals AI](https://www.vals.ai/)

{% endraw %}
