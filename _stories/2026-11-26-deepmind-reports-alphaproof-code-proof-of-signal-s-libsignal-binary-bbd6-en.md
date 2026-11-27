---
layout: story
lang: en
date: 2026-11-26 06:28:00 -0500
issue: "2026-11-26"
story_id: "deepmind-reports-alphaproof-code-proof-of-signal-s-libsignal-binary-bbd6"
permalink: "/2026/11/26/deepmind-reports-alphaproof-code-proof-of-signal-s-libsignal-binary-bbd6/"
title: "DeepMind reports AlphaProof Code proof of Signal's libsignal binary"
dek: "Google DeepMind released a paper and GitHub repository describing AlphaProof Code, a framework it says produced a complete formal proof that an Arm-compiled AArch64 (64-bit Arm) binary of Signal's libsignal library…"
description: "Google DeepMind released a paper and GitHub repository describing AlphaProof Code, a framework it says produced a complete formal proof that an Arm-compiled AArch64 (64-bit Arm) binary of Signal's libsignal library…"
section: "tech-industry"
rank: 20
edition: 0
section_rank: 5
score: 7.0
status: "Released"
source_name: "Tom's Hardware"
source_url: "https://www.tomshardware.com/tech-industry/artificial-intelligence/google-deepmind-ai-engineers-conjure-mathematical-proof-of-signals-encryption-protocol-alphaproof-code-framework-powered-human-bot-cooperation-for-speedy-work"
via: null
discussion_url: null
published_at: "2026-11-25T12:00:00+00:00"
tags: ["AI formal verification", "Signal", "DeepMind", "cryptography", "AlphaProof Code"]
topics: ["ai-formal-verification", "signal", "deepmind", "cryptography", "alphaproof-code"]
order: "20261126-0-979"
image: "/assets/stories/2026-11-26/deepmind-reports-alphaproof-code-proof-of-signal-s-libsignal-binary-bbd6-share.jpg"
art: "/assets/stories/2026-11-26/deepmind-reports-alphaproof-code-proof-of-signal-s-libsignal-binary-bbd6.jpg"
thumb: "/assets/stories/2026-11-26/deepmind-reports-alphaproof-code-proof-of-signal-s-libsignal-binary-bbd6-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g6caf1941f8ecd62dd372f86b94080e770ece1b744915bfe7235325b1ed3f755ad9223c43c95a1ceddc170341b97db7ab32711313f724095e50b27fcc00b0e4ee_1280.jpg", "author": "422737", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/privacy-policy-data-security-445156/", "provider": "Pixabay", "width": 3648, "height": 2736}
---

{% raw %}
<div class="story-lead" markdown="1">

Google DeepMind released a paper and GitHub repository describing AlphaProof Code, a framework it says produced a complete formal proof that an Arm-compiled AArch64 (64-bit Arm) binary of Signal's libsignal library, plus minimal scaffolding, matches a revised specification. The work used Lean, generating about 1.2 million lines of proofs for the cryptographic protocol and 5.3 million lines to show each binary instruction matched formal models of AArch64, CPU and Linux process behavior; agents flagged 1% of the codebase for human review.

The result covers libsignal's cryptographic engine as compiled for Arm, not the Signal app as a whole, and the article reports no independent validation of the proof.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** Google DeepMind published a paper and GitHub repository for AlphaProof Code and reported a complete Lean proof of an Arm-compiled AArch64 libsignal binary.
- **Not yet confirmed:** independent replication of the proof and DeepMind's claim that the method generalizes to other software at practical cost.

</div>

## Background

Formal verification means proving in machine-checked logic that an implementation matches a written specification; it has historically been so labor-intensive that the seL4 microkernel's proof reportedly took about 20 years and the CompCert C compiler's about six. The proofs in this effort are written in Lean, the same proof assistant AI systems have recently used for mathematics: AI Daily Radar's November 23 digest reported that OpenAI's GPT-6.2 Astra produced a machine-verifiable Lean proof of Smoktunowicz's gap theorem. AlphaProof Code shifts that approach from proving mathematical theorems to proving that a compiled AArch64 binary of libsignal matches a specification.

## Why it matters

Developers of security-critical software can inspect a public workflow for proving a compiled binary against a specification, including Lean models of AArch64 instructions, registers, memory and Linux processes; the assurance stops at libsignal's cryptographic engine, so it is not a whole-app security audit.

## What to watch

Watch for independent review or replication of the public Lean proof, or a second binary verified with AlphaProof Code; the report gives no timeline for either.

## Further reading

- [2026-11-23 — GPT-6.2 Astra produces machine-verifiable Lean proof of Smoktunowicz's gap theorem](https://the-decoder.com/gpt-6-2-astra-solved-a-math-theorem-no-other-ai-could-crack-then-invented-its-own-proof-strategy/)

{% endraw %}
