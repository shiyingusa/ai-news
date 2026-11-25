---
layout: story
lang: en
date: 2026-11-25 18:25:19 -0500
issue: "2026-11-25"
story_id: "community-repo-offers-much-shorter-version-of-anthropic-s-grh-lean-proof-f63f"
permalink: "/2026/11/25/community-repo-offers-much-shorter-version-of-anthropic-s-grh-lean-proof-f63f/"
title: "Community repo offers much shorter version of Anthropic's GRH Lean proof"
dek: "A public GitHub repository, lsernau/grh-lean, presents a community-built, much shorter version of Anthropic's GRH Lean formal verification, according to the Hacker News submission that brought it attention."
description: "A public GitHub repository, lsernau/grh-lean, presents a community-built, much shorter version of Anthropic's GRH Lean formal verification, according to the Hacker News submission that brought it attention."
section: "ai-news"
rank: 202
edition: 2
section_rank: 2
score: 7.0
status: "Available"
source_name: "GitHub"
source_url: "https://github.com/lsernau/grh-lean"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50648050"
published_at: "2026-11-25T21:48:10+00:00"
tags: ["AI-assisted theorem proving", "Lean", "formal verification", "mathematics", "Anthropic"]
topics: ["ai-assisted-theorem-proving", "lean", "formal-verification", "mathematics", "anthropic"]
order: "20261125-2-997"
image: "/assets/stories/2026-11-25/community-repo-offers-much-shorter-version-of-anthropic-s-grh-lean-proof-f63f-share.jpg"
art: "/assets/stories/2026-11-25/community-repo-offers-much-shorter-version-of-anthropic-s-grh-lean-proof-f63f.jpg"
thumb: "/assets/stories/2026-11-25/community-repo-offers-much-shorter-version-of-anthropic-s-grh-lean-proof-f63f-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g47030052cdb46936216f5189808b09e88dc594570fc85f2d86da72192dd716cad9ffaee1c1d1ea390c619d7afce059733502e54d25ade51f69192dc24f45eb84_1280.jpg", "author": "Pexels", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/coding-programming-css-1853305/", "provider": "Pixabay", "width": 5472, "height": 3648}
---

{% raw %}
<div class="story-lead" markdown="1">

A public GitHub repository, lsernau/grh-lean, presents a community-built, much shorter version of Anthropic's GRH Lean formal verification, according to the Hacker News submission that brought it attention. Commenters said the compact proof cuts the artifact from roughly 17 million lines to about 76,000 — a 99.56% reduction — and praised its separation of "known math" from "new math" plus human-readable documentation, though another commenter referred to a "300kloc" proof, leaving the exact size unclear. Whether the compact repository compiles, and whether it proves the same statements as the original, has not been independently confirmed.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** A public GitHub repository named lsernau/grh-lean exists and is presented on Hacker News as a much shorter community version of Anthropic's GRH Lean formal verification, with commenters describing human-readable documentation and a split between "known math" and "new math".
- **Not yet confirmed:** The exact reduction — commenters cite roughly 17 million lines down to about 76,000 (99.56%), while another refers to a "300kloc" proof — and whether the compact proof compiles, proves the same theorem as the original, or was produced by Anthropic applying internal models over a few days.

</div>

## Background

Lean is an interactive theorem prover in which proofs are written as code and checked step by step by a small trusted kernel, so a result can be machine-verified without a human reading every line. That checking guarantee does not make a proof readable, and large formalizations, including AI-generated ones, can balloon into millions of lines that mathematicians struggle to audit. The compact version is notable because it targets that auditability problem rather than the underlying theorem.

## Why it matters

The reduction matters only if mathematicians can actually audit the compact artifact, and even at roughly 76,000 lines commenters questioned whether a human can realistically read and verify the Lean code. The practical test is whether the repository states the same top-level theorem and relies on no additional axioms compared with the original.

## What to watch

Watch the Lean Zulip thread linked in the Hacker News discussion for maintainers' assessment of whether the compact proof compiles cleanly and matches the original's statements.

## Community discussion

Commenters split on what the reduction demonstrates: one argued it shows Anthropic can apply compute and stronger internal models to compress proofs in days, while another, unfamiliar with Lean, asked how realistically a human could read and verify code at this scale. A third highlighted the repository's documentation and its "known math" versus "new math" split as aids to digesting the proof.

{% endraw %}
