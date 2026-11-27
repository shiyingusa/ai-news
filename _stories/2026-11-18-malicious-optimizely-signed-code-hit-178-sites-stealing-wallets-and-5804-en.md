---
layout: story
lang: en
date: 2026-11-18 06:00:00 -0500
issue: "2026-11-18"
story_id: "malicious-optimizely-signed-code-hit-178-sites-stealing-wallets-and-5804"
permalink: "/2026/11/18/malicious-optimizely-signed-code-hit-178-sites-stealing-wallets-and-5804/"
title: "Malicious Optimizely-signed code hit 178 sites, stealing wallets and card data"
dek: "ReportURI said Tuesday it identified 178 websites — including CNN, Zoom, the BBC and Salesforce — that served visitors malicious JavaScript delivered from Optimizely's content delivery domain, cdn.optimizely.com."
description: "ReportURI said Tuesday it identified 178 websites — including CNN, Zoom, the BBC and Salesforce — that served visitors malicious JavaScript delivered from Optimizely's content delivery domain, cdn.optimizely.com."
section: "tech-industry"
rank: 12
edition: 0
section_rank: 1
score: 8.0
status: "Released"
source_name: "Ars Technica"
source_url: "https://arstechnica.com/security/2026/11/malicious-code-delivered-through-optimizely-hits-visitors-to-hundreds-of-sites/"
via: null
discussion_url: null
published_at: "2026-11-17T22:32:16+00:00"
tags: ["cybersecurity", "supply chain attack", "malware", "Optimizely", "iOS exploits"]
topics: ["cybersecurity", "supply-chain-attack", "malware", "optimizely", "ios-exploits"]
order: "20261118-0-987"
image: "/assets/stories/2026-11-18/malicious-optimizely-signed-code-hit-178-sites-stealing-wallets-and-5804-share.jpg"
art: "/assets/stories/2026-11-18/malicious-optimizely-signed-code-hit-178-sites-stealing-wallets-and-5804.jpg"
thumb: "/assets/stories/2026-11-18/malicious-optimizely-signed-code-hit-178-sites-stealing-wallets-and-5804-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g2b7f8ce38c058b3b6d880bbeed954572e8cb23300ada1e18c81097f38de262722d8e4cfa02b1418418ca3f2bfe717a78ed5b2e23dd3dbbc58d2bf670a989a6cc_1280.jpg", "author": "MightyFineBros", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/data-center-technology-server-7388620/", "provider": "Pixabay", "width": 4800, "height": 2700}
---

{% raw %}
<div class="story-lead" markdown="1">

ReportURI said Tuesday it identified 178 websites — including CNN, Zoom, the BBC and Salesforce — that served visitors malicious JavaScript delivered from Optimizely's content delivery domain, cdn.optimizely.com. The code carried a valid certificate for that domain and had been inserted into the portion of each customer's Optimizely snippet, the personalized JavaScript that runs on every page a customer serves.

The payloads swapped cryptocurrency wallet addresses in visitors' browsers, skimmed payment card data, stole cookies and screenshots, and served iOS exploit kits named Coruna and DarkSword to iPhones and iPads. Optimizely has not publicly described how the code was written into customer snippets; the researchers' figures come from their own scanning, not from the company.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** ReportURI said it identified 178 websites — Ars Technica names CNN, Zoom, the BBC and Salesforce as examples — serving JavaScript carrying a valid certificate for cdn.optimizely.com that had been modified to swap visitors' cryptocurrency wallet addresses for the attackers', skim payment card data, steal cookies and screenshots, and deliver the Coruna and DarkSword iOS exploit kits (tool-2-1). Krebs on Security, citing ReportURI, reported that 68 of the affected sites had no Content Security Policy at all and only 24 (15 percent) had one that fully blocked the payload (tool-2-3).
- **Not yet confirmed:** How the attackers wrote their code into each affected customer's snippet — the source says only that this happened "somehow" — and whether Optimizely's own systems were breached; the sources carry no attribution and no on-record Optimizely response, and the number of visitors actually infected is unknown. Reports also differ on details: Cointelegraph dates the injection to Monday and lists Ledger, BBC and IKEA among affected brands, while Ars Technica says researchers disclosed the finding Tuesday and names CNN, Zoom, the BBC and Salesforce (tool-2-2).

</div>

## Background

Optimizely is a website experimentation and personalization platform: customers embed a JavaScript "snippet" that the service serves — often from cdn.optimizely.com — and it runs on every page those customers publish, mixing Optimizely's own code with code each customer supplies. That arrangement makes the vendor a single, trusted distribution point for code on hundreds of unrelated sites, the classic setup for a supply-chain attack in which compromising one third-party script reaches every site that loads it, with the added reach that a valid certificate for the vendor's domain vouches for whatever is served.

## Why it matters

Because an Optimizely snippet executes on every page a customer serves, a single altered script exposed visitors across all 178 sites at once, and anyone who entered card details or used a crypto wallet on those pages should treat credentials and wallet addresses as compromised. Site owners running Optimizely should review what code is currently served from cdn.optimizely.com, check their snippet contents against their own repository, and audit for unauthorized changes rather than assuming the platform's signature vouches for the code.

## What to watch

Watch for Optimizely's own incident disclosure explaining how customer snippets were modified and what remediation it is applying, and for ReportURI's published list of the 178 affected domains so site owners can check whether they appear on it.

## Further reading

- [World's Largest Brands Infected With Malware Via Optimizely](https://report-uri.ghost.io/worlds-largest-brands-infected-with-malware-via-optimizely/)
- [Ledger, BBC Among 178 Organizations Hit by Crypto Malware](https://cointelegraph.com/news/hackers-inject-malware-into-178-major-websites)
- [Attackers Used Optimizely to A/B Test Malware on Top Websites ...](https://krebsonsecurity.com/2026/11/attackers-used-optimizely-to-a-b-test-malware-on-top-websites/)

{% endraw %}
