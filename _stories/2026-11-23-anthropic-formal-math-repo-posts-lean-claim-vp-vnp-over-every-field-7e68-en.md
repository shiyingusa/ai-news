---
layout: story
lang: en
date: 2026-11-23 19:32:00 -0500
issue: "2026-11-23"
story_id: "anthropic-formal-math-repo-posts-lean-claim-vp-vnp-over-every-field-7e68"
permalink: "/2026/11/23/anthropic-formal-math-repo-posts-lean-claim-vp-vnp-over-every-field-7e68/"
title: "Anthropic formal-math repo posts Lean claim VP ≠ VNP over every field"
dek: "Anthropic's public formal-math repository now hosts a Lean formalization claiming that VP ≠ VNP over every field, separating two algebraic complexity classes that are analogues of P and NP."
description: "Anthropic's public formal-math repository now hosts a Lean formalization claiming that VP ≠ VNP over every field, separating two algebraic complexity classes that are analogues of P and NP."
section: "ai-news"
rank: 221
edition: 2
section_rank: 1
score: 7.0
status: "Released"
source_name: "GitHub"
source_url: "https://github.com/anthropics/formal-math/tree/main/vp-vnp"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50620102"
published_at: "2026-11-23T22:09:10+00:00"
tags: ["formal verification", "Lean", "complexity theory", "AI for mathematics", "Anthropic"]
topics: ["formal-verification", "lean", "complexity-theory", "ai-for-mathematics", "anthropic"]
order: "20261123-2-978"
image: "/assets/stories/2026-11-23/anthropic-formal-math-repo-posts-lean-claim-vp-vnp-over-every-field-7e68-share.jpg"
art: "/assets/stories/2026-11-23/anthropic-formal-math-repo-posts-lean-claim-vp-vnp-over-every-field-7e68.jpg"
thumb: "/assets/stories/2026-11-23/anthropic-formal-math-repo-posts-lean-claim-vp-vnp-over-every-field-7e68-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g4097b6e04d807e81def251c0131936faa0df031694afc2bd4803601cd708634ae8b9506b125bc03cc111866c6d4c8d1451eb1e5b4efdb95f5aa802e857e5bede_1280.jpg", "author": "Pexels", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/laptop-notebook-cellphone-computer-1839876/", "provider": "Pixabay", "width": 3778, "height": 2519}
---

{% raw %}
<div class="story-lead" markdown="1">

Anthropic's public formal-math repository now hosts a Lean formalization claiming that VP ≠ VNP over every field, separating two algebraic complexity classes that are analogues of P and NP. Lean is a proof assistant in which such arguments can be machine-checked, but the posting is not a peer-reviewed validation, and the material does not explain any AI method behind the proof. The claim is narrower than P vs NP and is presented for complexity theorists and formal-verification researchers to inspect.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** Anthropic's formal-math GitHub repository hosts a paper titled “VP ≠ VNP over every field,” credited to Claude/Anthropic, alongside a Lean 4 formalization reported at roughly 73,000 lines; the repository describes the work as a research artifact Anthropic does not maintain and states that no human mathematician has checked the proof.
- **Not yet confirmed:** The mathematical claim that VP ≠ VNP over every field has not been independently verified or peer-reviewed, and the paper itself says it has not analyzed how the argument relates to relativization or algebrization; it also remains unclear how much of the work was AI-generated beyond the “Claude” attribution.

</div>

## Background

VP and VNP are the algebraic analogues of P and NP: VP covers problems solvable by polynomial-size arithmetic circuits, VNP those whose polynomials are sums of monomials that can be computed efficiently, so VP ≠ VNP is the algebraic counterpart of the P vs NP question and has been open since Valiant formulated it in the 1970s. The work is hosted in Anthropic's formal-math repository as a Lean development — Lean being an interactive proof assistant that machine-checks every step of a proof against a small trusted kernel — which is why the thread read it as a sign of AI-assisted mathematics rather than a conventional paper announcement. The authors themselves note in the paper that "we have not analysed how it relates to relativization and algebrization", the standard barrier results any such separation must come to terms with.

## Why it matters

For complexity theorists and Lean users, the practical consequence is an auditing job rather than a settled theorem: the development can be built and inspected (one commenter pointed to a browser tool for reading the Lean source without a local setup), but standard references still describe a lower bound on the permanent's circuit size — what VP ≠ VNP requires — as an outstanding open problem, so the formalization's axiom list, definitions and any unfinished proofs should be checked before the result is cited or extended. The paper itself concedes it has not analysed how the argument relates to relativization and algebrization, the usual barriers for separating complexity classes, and states that it does not settle P versus NP.

## What to watch

The next check is independent machine-checking of the Lean development and any peer-reviewed write-up that addresses the paper's stated lack of analysis of relativization and algebrization.

## Community discussion

Commenters read the post as Anthropic pushing toward P vs NP and debated whether AI will soon solve problems that would otherwise occupy graduate students for years; one commenter highlighted the paper's own admission that it has not analyzed relativization or algebrization, barriers relevant to such complexity-theory separations.

## Further reading

- [Claude-authored paper claims VP≠VNP over every… · AGI Hunt](https://agihunt.info/en/e/1a20a795a118dbdb4f5bd2bb40d)
- [Anthropic Publishes Claimed Proof That VP ≠ VNP Over Every Field](https://news.lavx.hu/article/anthropic-publishes-claimed-proof-that-vp-vnp-over-every-field)
- [Claude-Written Paper Claims VP ≠ VNP, With a Lean Proof](https://fourweekmba.com/ai-claude-written-paper-claims-vp-vnp-with-a-lean-proof/)
- [Arithmetic circuit complexity - Wikipedia](https://en.wikipedia.org/wiki/Arithmetic_circuit_complexity)
- [VP ||#92;neq$ VNP over every field · Hexagon](https://hexagonmath.org/2611.00954v1)

{% endraw %}
