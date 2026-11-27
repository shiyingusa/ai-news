---
layout: story
lang: en
date: 2026-11-18 12:26:25 -0500
issue: "2026-11-18"
story_id: "8-000-km-hybrid-qkdpqc-network-links-chicago-amsterdam-and-the-basque-60dc"
permalink: "/2026/11/18/8-000-km-hybrid-qkdpqc-network-links-chicago-amsterdam-and-the-basque-60dc/"
title: "8,000 km Hybrid QKD–PQC Network Links Chicago, Amsterdam and the Basque Country"
dek: "A consortium of research and technology organisations demonstrated an 8,000 km hybrid quantum-safe network spanning Chicago, Amsterdam and the Basque Country at SC26, the Supercomputing Conference 2026."
description: "A consortium of research and technology organisations demonstrated an 8,000 km hybrid quantum-safe network spanning Chicago, Amsterdam and the Basque Country at SC26, the Supercomputing Conference 2026."
section: "chips-compute"
rank: 113
edition: 1
section_rank: 7
score: 7.0
status: "Demonstrated"
source_name: "The Quantum Insider"
source_url: "https://thequantuminsider.com/2026/11/18/8000-km-quantum-safe-network-us-europe-demonstration/"
via: null
discussion_url: null
published_at: "2026-11-18T12:44:46+00:00"
tags: ["quantum key distribution", "post-quantum cryptography", "quantum-safe networking", "optical transport encryption", "quantum networking demonstration"]
topics: ["quantum-key-distribution", "post-quantum-cryptography", "quantum-safe-networking", "optical-transport-encryption", "quantum-networking-demonstration"]
order: "20261118-1-986"
image: "/assets/stories/2026-11-18/8-000-km-hybrid-qkdpqc-network-links-chicago-amsterdam-and-the-basque-60dc-share.jpg"
art: "/assets/stories/2026-11-18/8-000-km-hybrid-qkdpqc-network-links-chicago-amsterdam-and-the-basque-60dc.jpg"
thumb: "/assets/stories/2026-11-18/8-000-km-hybrid-qkdpqc-network-links-chicago-amsterdam-and-the-basque-60dc-640.jpg"
photo_credit: {"url": "https://thumb.wikimedia.org/wikipedia/commons/thumb/c/cc/Alice_in_BBN_laboratory_-_DARPA_Quantum_Network%2C_January_2003.jpg/1920px-Alice_in_BBN_laboratory_-_DARPA_Quantum_Network%2C_January_2003.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail", "author": "Daderot", "licence": "CC0", "licence_url": "http://creativecommons.org/publicdomain/zero/1.0/deed.en", "source_url": "https://commons.wikimedia.org/wiki/File:Alice_in_BBN_laboratory_-_DARPA_Quantum_Network,_January_2003.jpg", "provider": "Wikimedia Commons", "width": 1984, "height": 1488}
---

{% raw %}
<div class="story-lead" markdown="1">

A consortium of research and technology organisations demonstrated an 8,000 km hybrid quantum-safe network spanning Chicago, Amsterdam and the Basque Country at SC26, the Supercomputing Conference 2026. The setup uses five quantum nodes across three locations: two at the Ciena and PCSS booths in Chicago (less than 1 km apart), one with SURF in Amsterdam, and two at University of the Basque Country (EHU) sites in Bilbao and Zamudio linked by a 25 km fibre.

Quantum key distribution (QKD, which derives keys from the laws of quantum mechanics) runs only on those two short links using Luxquanta's Nova lq systems, while post-quantum cryptography (PQC, software algorithms designed to resist quantum attack) carries the roughly 1,200 km Bilbao–Amsterdam and 7,000 km Amsterdam–Chicago hops using the NIST-standard ML-KEM. EHU's QuLore framework orchestrates key selection and relays keys through intermediate sites, and Ciena's optical platforms encrypt at line rate — 1.6 Tb/s (WL6e) in Chicago and 800 Gb/s (WL5e) in Bizkaia — with protection applied at the optical, IPsec tunnel and application layers.

This was a conference demonstration announced in a press release, not a deployed or generally available service, and no independent performance measurement was reported.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** The consortium (EHU, Luxquanta, Ciena, GÉANT, PCSS, RedIRIS and SURF) says it demonstrated the network at SC26 with five nodes in three locations, QKD on the two short links, ML-KEM-based PQC on the long links, and QuLore coordinating keys across Luxquanta, EHU vKMS and SURF eduKMS systems.
- **Not yet confirmed:** Key generation rates, latency, throughput under load, and any independent or peer-reviewed measurement of the setup; the press release also leaves out whether this becomes a production service and on what timeline.

</div>

## Background

Quantum Key Distribution distributes encryption keys whose secrecy rests on physics rather than computational difficulty, but fiber-based QKD is generally limited to metropolitan distances of roughly 100 km, so long-haul links need post-quantum cryptography such as NIST's ML-KEM. QuLore, the adaptive framework from EHU's i2T research group described in an arXiv preprint, was built to choose between those methods per connection and coordinate separate key-management systems.

## Why it matters

The demo targets sites that cannot put QKD hardware everywhere: because QuLore picks QKD or PQC per connection and stitches vendor key-management systems together through a common interface, operators can start quantum-safe migration on mixed infrastructure instead of waiting for end-to-end quantum hardware. The practical constraint is distance — fibre QKD is described as workable only to roughly 100 km, so any long-haul link today depends on ML-KEM and related PQC software, meaning the security of those hops rests on mathematics rather than physics.

## Further reading

- [QuLore : An Adaptive Security Framework to Extend Quantum - Safe ...](https://arxiv.org/html/2511.22416)

{% endraw %}
