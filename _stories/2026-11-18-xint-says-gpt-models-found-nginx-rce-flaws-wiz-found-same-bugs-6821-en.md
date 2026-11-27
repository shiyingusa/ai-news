---
layout: story
lang: en
date: 2026-11-18 18:28:03 -0500
issue: "2026-11-18"
story_id: "xint-says-gpt-models-found-nginx-rce-flaws-wiz-found-same-bugs-6821"
permalink: "/2026/11/18/xint-says-gpt-models-found-nginx-rce-flaws-wiz-found-same-bugs-6821/"
title: "Xint says GPT models found Nginx RCE flaws; Wiz found same bugs"
dek: "Xint, a DARPA-backed cybersecurity company, says its AI models—GPT 6.1 Sol and GPT-6 Luna—found remote code execution (RCE) vulnerabilities in Nginx, the widely used web server, Forbes reported."
description: "Xint, a DARPA-backed cybersecurity company, says its AI models—GPT 6.1 Sol and GPT-6 Luna—found remote code execution (RCE) vulnerabilities in Nginx, the widely used web server, Forbes reported."
section: "ai-news"
rank: 209
edition: 2
section_rank: 9
score: 7.0
status: "Announced"
source_name: "Forbes"
source_url: "https://www.forbes.com/sites/thomasbrewster/2026/11/18/ai-finds-major-web-security-flaws/"
via: "Techmeme"
discussion_url: null
published_at: "2026-11-18T16:25:01+00:00"
tags: ["AI security", "vulnerability discovery", "Nginx", "cybersecurity", "GPT models"]
topics: ["ai-security", "vulnerability-discovery", "nginx", "cybersecurity", "gpt-models"]
order: "20261118-2-990"
image: "/assets/stories/2026-11-18/xint-says-gpt-models-found-nginx-rce-flaws-wiz-found-same-bugs-6821-share.jpg"
art: "/assets/stories/2026-11-18/xint-says-gpt-models-found-nginx-rce-flaws-wiz-found-same-bugs-6821.jpg"
thumb: "/assets/stories/2026-11-18/xint-says-gpt-models-found-nginx-rce-flaws-wiz-found-same-bugs-6821-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/gc7b5dcc9c6d79872eab79e6dcd3c3aa5e2288fec477994fb63d59cfe4d35aa3f8a2e511f63d3908a1750ed925e6534588a40b8aae917867ec1b7768daaf3481f_1280.jpg", "author": "blickpixel", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/it-server-server-cabinet-network-838384/", "provider": "Pixabay", "width": 2682, "height": 1788}
---

{% raw %}
<div class="story-lead" markdown="1">

Xint, a DARPA-backed cybersecurity company, says its AI models—GPT 6.1 Sol and GPT-6 Luna—found remote code execution (RCE) vulnerabilities in Nginx, the widely used web server, Forbes reported. Wiz says it separately found the same flaws, giving a second company account that the bugs exist but not verifying that Xint's AI discovered them or how.

The report names no CVE identifiers, affected Nginx versions, or patches, so operators cannot yet assess exposure from the account alone.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** Forbes reported that Xint, a Darpa-backed cybersecurity company, says its AI using GPT 6.1 Sol and GPT-6 Luna found remote code execution vulnerabilities in Nginx, and Wiz said it independently found the same flaws; Wiz's advisory names CVE-2026-123633 and CVE-2026-123007 as critical flaws in Nginx itself.
- **Not yet confirmed:** the full CVE list and severity — Wiz rates two flaws Critical with a CVSS 4.0 score of 9.2, while a separate "nginx 2root" advisory says scores are not yet published and describes five Nginx RCE flaws plus a Linux kernel SCTP bug; also unconfirmed are the affected and patched Nginx versions, and how much of the discovery was done autonomously by the models rather than by Xint's researchers.

</div>

## Background

Nginx is a widely used open-source web server and reverse proxy that fronts a large share of high-traffic sites, so a remote code execution (RCE) bug — one an attacker can trigger over the network without prior access to the machine — carries outsized weight for anyone running it. AI-assisted vulnerability hunting has been moving from research demos into named programmes: AI Daily Radar's November 17 digest reported OpenAI saying it was working with NATO and allied cyber agencies on using AI to find vulnerabilities, test fixes and protect critical systems, though it named no agencies, models, access terms or timeline. GPT-6.1 Sol, one of the two models Xint cites, is an OpenAI model positioned below the flagship GPT-6 Astra in the GPT-6 series.

## Why it matters

For organizations running Nginx, the report is not yet actionable for triage: without CVE identifiers, affected version ranges, or a patch, teams cannot determine whether their deployments are exposed from this account alone.

## What to watch

Watch for CVE identifiers, affected Nginx version ranges, and a patch or technical write-up from Xint or Wiz, which would allow operators to verify the finding and check their exposure.

## Further reading

- [GPT - 6 . 1 Sol - API Pricing & Benchmarks | OpenRouter](https://openrouter.ai/openai/gpt-6.1-sol)
- [2026-11-17 — OpenAI works with NATO, allied cyber agencies on AI vulnerability discovery](https://openai.com/index/strengthening-nato-allied-cyber-defences-ai)
- [Unauthenticated Remote Code Execution in NGINX ... | Wiz Blog](https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities)
- [nginx 2root: Five nginx RCE Flaws and a Kernel Bug...](https://www.getastra.com/blog/security-advisory/nginx2root/)
- [Remote code execution in NGINX HTTP/2 ( CVE - 2026 -123633...)](https://nginx2shell.com/)

{% endraw %}
