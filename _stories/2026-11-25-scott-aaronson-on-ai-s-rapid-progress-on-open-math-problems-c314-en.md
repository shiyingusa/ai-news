---
layout: story
lang: en
date: 2026-11-25 18:25:15 -0500
issue: "2026-11-25"
story_id: "scott-aaronson-on-ai-s-rapid-progress-on-open-math-problems-c314"
permalink: "/2026/11/25/scott-aaronson-on-ai-s-rapid-progress-on-open-math-problems-c314/"
title: "Scott Aaronson on AI's rapid progress on open math problems"
dek: "For mathematicians and theoretical computer scientists, Scott Aaronson argues that a recent wave of AI-assisted work has solved dozens of long-open problems, a shift he frames as a major moment for the field."
description: "For mathematicians and theoretical computer scientists, Scott Aaronson argues that a recent wave of AI-assisted work has solved dozens of long-open problems, a shift he frames as a major moment for the field."
section: "ai-news"
rank: 201
edition: 2
section_rank: 1
score: 8.0
status: "Demonstrated"
source_name: "scottaaronson.blog"
source_url: "https://scottaaronson.blog/?p=10379"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50646108"
published_at: "2026-11-25T19:11:27+00:00"
tags: ["AI for mathematics", "LLMs", "automated theorem proving", "Lean", "research breakthrough"]
topics: ["ai-for-mathematics", "llms", "automated-theorem-proving", "lean", "research-breakthrough"]
order: "20261125-2-998"
image: "/assets/stories/2026-11-25/scott-aaronson-on-ai-s-rapid-progress-on-open-math-problems-c314-share.jpg"
art: "/assets/stories/2026-11-25/scott-aaronson-on-ai-s-rapid-progress-on-open-math-problems-c314.jpg"
thumb: "/assets/stories/2026-11-25/scott-aaronson-on-ai-s-rapid-progress-on-open-math-problems-c314-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g2ad067e13f1f0137bbfe0185f20d9eaaccff81a0cd307e3136ac5066d71bc9fb923698a12849669edb64aa285e04dd6b3ae6686096f956b8e8d88cc475d71746_1280.jpg", "author": "ykaiavu", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/garden-hedge-bush-plants-to-cut-7460988/", "provider": "Pixabay", "width": 7952, "height": 5304}
---

{% raw %}
<div class="story-lead" markdown="1">

For mathematicians and theoretical computer scientists, Scott Aaronson argues that a recent wave of AI-assisted work has solved dozens of long-open problems, a shift he frames as a major moment for the field. The post points to a paper titled "The matrix multiplication exponent is nine fourths" and discusses LLMs and the Lean proof assistant. The evidence is commentary and linked papers, not a released system; independent verification of the Lean proofs remains the key caveat.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** A paper titled "The Matrix Multiplication Exponent Is Nine Fourths," dated November 24, 2026, is posted in OpenAI's public math preprints repository on GitHub, and an abstract for it appears on alphaXiv. Scott Aaronson's November 25 blog post argues that a run of solutions to long-open problems in mathematics and theoretical computer science amounts to a remarkable moment, and the post drew heavy Hacker News discussion. Wikipedia's entry on the complexity of matrix multiplication confirms that the exponent ω has a decades-long history of successively improved bounds.
- **Not yet confirmed:** That LLM or generative-AI systems specifically produced these results, rather than a combination of Lean, MathLib and large-scale compute — a question commenter utopiah raises directly — and which named systems were involved. Also unconfirmed: independent verification of the claimed nine-fourths bound on ω, and the completeness and faithfulness of any Lean formalizations, since commenter onetimeusename notes that gaps between Lean and informal proofs have been a recurring problem with machine-generated proofs. Aaronson's characterization of the moment as singular is his assessment, not an established finding.

</div>

## Background

Lean is a proof assistant: it mechanically checks every step of a proof, so a formalized result is verified by software rather than by referees, and Mathlib is its shared library of already-formalized mathematics. AI Daily Radar's November 23 digest reported that OpenAI's GPT-6.2 Astra had produced a machine-verifiable Lean proof of Smoktunowicz's gap theorem — the first by any AI, according to the evaluation firm Vals AI — and led the Autoform-Hard theorem-proving benchmark with 49 of 56 tasks. The same digest covered a Hacker News argument over a 17-million-line Lean artifact, where commenters questioned whether LLM-assisted proofs of that size can be reviewed at all.

## Why it matters

For working mathematicians, the constraint moves from producing an argument to checking one: the scarce skill becomes reading a Lean formalization and confirming it proves the informal statement that was claimed. That gap is the live objection — Aaronson pre-empts complaints about "a minor discrepancy between the Lean and informal proofs," and commenters pushed back that such mismatches have long been a failure mode of machine-generated proofs and code. Formalization has lagged proof generation — a 2026 report found only about 42% of one OpenAI math repository had been formalized in Lean — so each "solved" announcement should be treated as provisional until the formal statement and the informal claim are shown to match.

## What to watch

Independent verification of the Lean proofs and peer review of the claimed results, including the matrix multiplication exponent paper.

## Community discussion

Commenters debated whether the progress owes more to LLMs or to years of work on Lean and MathLib plus compute, and some argued that discrepancies between Lean and informal proofs are a substantive concern rather than a triviality. Others hoped the impact stays confined to verifiable math tasks.

## Further reading

- [Computational complexity of matrix multiplication - Wikipedia](https://en.wikipedia.org/wiki/Computational_complexity_of_matrix_multiplication)
- [The Matrix Multiplication Exponent Is Nine Fourths | alphaXiv](https://www.alphaxiv.org/abs/2611.matrix-multiplication-exponent-lower-bound)
- [math/preprints/ The - matrix - multiplication - exponent - is ...](https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf)
- [2026-11-23 — GPT-6.2 Astra produces machine-verifiable Lean proof of Smoktunowicz's gap theorem](https://the-decoder.com/gpt-6-2-astra-solved-a-math-theorem-no-other-ai-could-crack-then-invented-its-own-proof-strategy/)
- [2026-11-23 — Blog post on 17-million-line Lean artifact sparks LLM proof debate](https://micjm.com/blog/yes-17m-lines-of-lean-is-a-lot/)
- [OpenAI Math Repository Formalizes About 42% in Lean [ 2026 ]](https://tech-insider.org/openai-math-papers-lean-verification-42-percent-2026/)

{% endraw %}
