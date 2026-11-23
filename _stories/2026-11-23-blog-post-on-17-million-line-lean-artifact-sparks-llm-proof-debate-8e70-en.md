---
layout: story
lang: en
date: 2026-11-23 13:27:00 -0500
issue: "2026-11-23"
story_id: "blog-post-on-17-million-line-lean-artifact-sparks-llm-proof-debate-8e70"
permalink: "/2026/11/23/blog-post-on-17-million-line-lean-artifact-sparks-llm-proof-debate-8e70/"
title: "Blog post on 17-million-line Lean artifact sparks LLM proof debate"
dek: "A blog post at micjm.com argues that a 17-million-line Lean proof is unusually large and examines the implications for review and correctness."
description: "A blog post at micjm.com argues that a 17-million-line Lean proof is unusually large and examines the implications for review and correctness."
section: "ai-news"
rank: 5
edition: 0
section_rank: 5
score: 7.0
status: null
source_name: "micjm.com"
source_url: "https://micjm.com/blog/yes-17m-lines-of-lean-is-a-lot/"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50607668"
published_at: "2026-11-23T05:00:49+00:00"
tags: ["Lean", "formal verification", "LLM-generated proofs", "mathematics", "AI code quality"]
topics: ["lean", "formal-verification", "llm-generated-proofs", "mathematics", "ai-code-quality"]
order: "20261123-0-994"
image: "/assets/stories/2026-11-23/blog-post-on-17-million-line-lean-artifact-sparks-llm-proof-debate-8e70-share.jpg"
art: "/assets/stories/2026-11-23/blog-post-on-17-million-line-lean-artifact-sparks-llm-proof-debate-8e70.jpg"
thumb: "/assets/stories/2026-11-23/blog-post-on-17-million-line-lean-artifact-sparks-llm-proof-debate-8e70-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g8bcd542abf8abc8b60971117f4318976e36ce92b95a96e75bd4b49764e708965ee15e9d46c4806a5db1fb9f1fae78b3a_1280.jpg", "author": "kewl", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/server-room-datacenter-network-90389/", "provider": "Pixabay", "width": 4818, "height": 3212}
---

{% raw %}
<div class="story-lead" markdown="1">

A blog post at micjm.com argues that a 17-million-line Lean proof is unusually large and examines the implications for review and correctness. The post sparked a Hacker News discussion in which commenters debated whether LLM-assisted proofs of that size can be trusted, with some warning that errors could hide in converted sub-proofs or in the sheer volume of code. Commenters also said the artifact had been shrunk to 13 million lines, a claim that was not independently verified in the available reporting.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** A blog post at micjm.com argues that a 17-million-line Lean proof is large enough to raise review concerns, and Hacker News commenters discussed the implications for LLM-assisted proof generation.
- **Not yet confirmed:** That the proof is LLM-generated, that it concerns the Generalized Riemann Hypothesis, and that it has been reduced to 13 million lines all rest on community comments and were not established by the available source material.

</div>

## Background

Lean is a proof assistant in which proofs are written as code and checked by a small trusted kernel, so a formalization can in principle be verified mechanically instead of read line by line — which is why the size of a Lean development matters as a practical review problem. This artifact traces to a November 20, 2026 note by mathematician Levent Alpöge, who said that working with Claude he believed he had found a proof of the Riemann Hypothesis and of the Generalized Riemann Hypothesis for Dirichlet L-functions, and released it as a Lean development of 175,187 files and roughly 17 million lines, with no accompanying paper, according to a University of Waterloo page that collects checks of the proof.

## Community discussion

Commenters questioned whether LLM-generated proofs of millions of lines can be trusted, with one arguing that a large proof has a larger attack surface and another suggesting an incorrect converted sub-proof could be the failure point rather than a Lean bug. A further commenter noted the artifact had reportedly shrunk from 17 million to 13 million lines, while others worried that no human will ever review code of that size.

## Further reading

- [17 Million Lines Claim to Prove Riemann . We Ran Them. - YouTube](https://www.youtube.com/watch?v=aDl7-MWFLVc)
- [Alpöge/Claude proof of the Generalized Riemann Hypothesis](https://math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/)

{% endraw %}
