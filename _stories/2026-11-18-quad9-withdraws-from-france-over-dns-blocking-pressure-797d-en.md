---
layout: story
lang: en
date: 2026-11-18 06:00:00 -0500
issue: "2026-11-18"
story_id: "quad9-withdraws-from-france-over-dns-blocking-pressure-797d"
permalink: "/2026/11/18/quad9-withdraws-from-france-over-dns-blocking-pressure-797d/"
title: "Quad9 withdraws from France over DNS blocking pressure"
dek: "Quad9, a public DNS resolver that translates domain names into IP addresses, has withdrawn from France…"
description: "Quad9, a public DNS resolver that translates domain names into IP addresses, has withdrawn from France…"
section: "tech-industry"
rank: 13
edition: 0
section_rank: 2
score: 7.0
status: null
source_name: "blog.cloudflare.com"
source_url: "https://blog.cloudflare.com/quad9-withdrawal-from-france/"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50538994"
published_at: "2026-11-17T22:13:34+00:00"
tags: ["DNS", "internet governance", "content blocking", "France", "privacy"]
topics: ["dns", "internet-governance", "content-blocking", "france", "privacy"]
order: "20261118-0-986"
image: "/assets/stories/2026-11-18/quad9-withdraws-from-france-over-dns-blocking-pressure-797d-share.jpg"
art: "/assets/stories/2026-11-18/quad9-withdraws-from-france-over-dns-blocking-pressure-797d.jpg"
thumb: "/assets/stories/2026-11-18/quad9-withdraws-from-france-over-dns-blocking-pressure-797d-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/gd743113e800d6f683207d953960447b573766eb227bede6bfa4ffd51c492110c18113d6acaa206cf9d069c343b2057fbd3d1f3da6aed0fa371700d16fcf9d19d_1280.jpg", "author": "Akela999", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/electrical-data-center-2476783/", "provider": "Pixabay", "width": 4096, "height": 2160}
---

{% raw %}
<div class="story-lead" markdown="1">

Quad9, a public DNS resolver that translates domain names into IP addresses, has withdrawn from France, according to a Cloudflare blog post that frames the move as an early warning about DNS-blocking mandates and their effect on internet infrastructure. The supplied item does not include the full post or the specific French legal or regulatory measure, so the precise scope of the withdrawal is not established here.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** Quad9's own announcement states that a Paris court ruling in beIN's favor requires it to block recursive DNS resolution for certain domains for users in France, and that the court reduced the penalty from €580,000 to €1,000 per day. TorrentFreak reports the withdrawal takes effect on November 24.
- **Not yet confirmed:** the exact domain list and the court's full reasoning are absent from the supplied material; the November 24 date and the claim that Quad9 is the second DNS resolver to quit France come from TorrentFreak, not Quad9's post. Cloudflare's article text is not supplied, so its specific commitments are unverified.

</div>

## Background

Public recursive DNS resolvers such as Quad9 and Cloudflare's 1.1.1.1 answer domain lookups for users who prefer not to rely on their ISP's resolver. The dispute concerns French requirements to enforce site blocking at the DNS layer, which puts a neutral public resolver in conflict with blocking mandates; withdrawal means French users lose Quad9 as an option unless they switch to another resolver.

## Why it matters

For French users, the practical cost is loss of a resolver they may have deliberately chosen for its malware filtering; for other public DNS operators, the precedent is that a court can attach per-day non-compliance penalties to a global resolver's refusal to block, which is what Quad9 faces in broadcaster beIN Sports' request for up to €580,000 a day in a Paris court. It also cuts against the stated purpose of such orders: ICANN's Security and Stability Advisory Committee argued in its May 2025 SAC127 report that blocking through recursive resolvers is effective only to the extent users stay on the resolver where the blocking is implemented, so mandates push traffic toward unblocked or foreign resolvers rather than removing access to the content.

## Further reading

- [Quad9 plans France withdrawal over beIN site-blocking orders](https://disputeindex.com/cases/quad9-france-bein-dns-blocking-withdrawal)
- [DNS Resolver Quad9 Will Leave France After Court Orders ...](https://torrentfreak.com/dns-resolver-quad9-will-leave-france-after-court-orders-piracy-blocking-penalty/)
- [Farewell, France | Quad9](https://quad9.net/news/blog/au-revoir-france/)
- [DNS Resolver Quad 9 Rejects French Piracy Blocks ... * TorrentFreak](https://torrentfreak.com/dns-resolver-quad9-rejects-french-piracy-blocks-weighs-exit-as-bein-seeks-up-to-e580k-a-day/)
- [sac127_ dns _ blocking _revisited](https://itp.cdn.icann.org/en/files/security-and-stability-advisory-committee-ssac-reports/sac127-dns-blocking-revisited-16-05-2025-en.pdf)

<div class="community" markdown="1">

## Community discussion: opinion, not evidence

Quad9's CTO said its position had "100% support" so far at IETF 127 and described "general dread" about DNS policy, while another commenter argued that a neutral Internet is unrealistic now that everyone is online. Others pressed Cloudflare to commit to withdrawing from affected countries if it loses its appeal; these are commenter opinions, not evidence of consensus.

</div>

{% endraw %}
