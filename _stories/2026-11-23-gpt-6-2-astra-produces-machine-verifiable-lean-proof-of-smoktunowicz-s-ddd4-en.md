---
layout: story
lang: en
date: 2026-11-23 13:26:56 -0500
issue: "2026-11-23"
story_id: "gpt-6-2-astra-produces-machine-verifiable-lean-proof-of-smoktunowicz-s-ddd4"
permalink: "/2026/11/23/gpt-6-2-astra-produces-machine-verifiable-lean-proof-of-smoktunowicz-s-ddd4/"
title: "GPT-6.2 Astra produces machine-verifiable Lean proof of Smoktunowicz's gap theorem"
dek: "OpenAI's GPT-6.2 Astra independently produced a Lean proof of Smoktunowicz's gap theorem that, according to The Decoder citing the evaluation firm Vals AI, is the first machine-verifiable proof of the result by any AI."
description: "OpenAI's GPT-6.2 Astra independently produced a Lean proof of Smoktunowicz's gap theorem that, according to The Decoder citing the evaluation firm Vals AI, is the first machine-verifiable proof of the result by any AI."
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

OpenAI's GPT-6.2 Astra independently produced a Lean proof of Smoktunowicz's gap theorem that, according to The Decoder citing the evaluation firm Vals AI, is the first machine-verifiable proof of the result by any AI. Because key foundations were missing from Mathlib — Lean's standard library of formalized mathematics — the model chose its own proof strategy instead of assembling existing lemmas.

On Autoform-Hard, a theorem-proving benchmark, Astra now leads the leaderboard with 49 of 56 tasks solved. The report is secondary coverage: it does not say how the model was prompted, whether anyone outside OpenAI and Vals AI has checked the proof, or whether Astra is generally available.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** Vals AI's own write-up states that GPT-6.2 Astra wrote a Lean 4 proof of Smoktunowicz's gap theorem for graded domains in 94 minutes, about 1,800 lines, taking a route that differs from the published proof — building on a new quantity it called "capacity" and working around three deep results absent from Mathlib; The Decoder also reports Astra leading Autoform-Hard with 49 of 56 tasks solved.
- **Not yet confirmed:** the claim that this is the first computer-checkable proof of the theorem and that no other AI could solve it rests on Vals AI's assessment rather than an independent review, and neither OpenAI nor a third party has publicly confirmed the "self-invented strategy" framing, the leaderboard figures, or how much scaffolding and human guidance the 94-minute run involved.

</div>

## Background

Lean is a proof assistant: it checks a proof step by step, so a proof it accepts is machine-verified rather than judged by human readers, and most such proofs lean on Mathlib, Lean's community library of formalized mathematics. Autoform-Hard, as Vals AI describes it, is a 56-task set of Lean 4 formalization problems drawn from graduate- and research-level textbooks, taken from Meta FAIR's AutoformBench. AI Daily Radar's November 19 digest reported that OpenAI released GPT-6.2 Astra on November 18 with a 1.05 million-token context window and a 20% API price cut; the theorem result is this same model's reported showing on that benchmark.

## Why it matters

Because a Lean proof is machine-checkable, mathematicians can test the claim by running it through Lean rather than trusting the 49-of-56 benchmark score; the definitions and lemmas Astra built to replace the missing Mathlib foundations are the parts most likely to conceal an error or a nonstandard assumption, so they deserve checking first.

## What to watch

Whether independent reviewers or the Autoform-Hard maintainers reproduce the Lean proof and the 49-of-56 result, and whether the missing Mathlib foundations are contributed upstream.

## Further reading

- [GPT-6.2 Astra Formalizes Smoktunowicz's Gap Theorem - vals.ai](https://www.vals.ai/blogs/smoktunowicz-gap-theorem)
- [OpenAI's GPT-6.2 Astra Proves a Math Theorem No Computer Ever ...](https://alphasignal.ai/news/openai-s-gpt-6-2-astra-proves-a-math-theorem-no-computer-ever-could)
- [OpenAI's GPT-6.2 Astra Proves a Math Theorem No Computer Ever ...](https://hermes-ai.net/news/openai-s-gpt-6-2-astra-proves-a-math-theorem-no-computer-ever-could/)
- [2026-11-19 — OpenAI ships GPT-6.2 Astra and Sol with a 20% price cut, and developers push back](http://www.geekpark.net/news/374175)
- [AI Benchmarks for Real-World Tasks | Vals AI](https://www.vals.ai/)

{% endraw %}
