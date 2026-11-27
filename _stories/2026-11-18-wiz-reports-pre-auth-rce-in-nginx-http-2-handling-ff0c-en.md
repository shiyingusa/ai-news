---
layout: story
lang: en
date: 2026-11-18 12:26:43 -0500
issue: "2026-11-18"
story_id: "wiz-reports-pre-auth-rce-in-nginx-http-2-handling-ff0c"
permalink: "/2026/11/18/wiz-reports-pre-auth-rce-in-nginx-http-2-handling-ff0c/"
title: "Wiz reports pre-auth RCE in nginx HTTP/2 handling"
dek: "Wiz published research describing pre-authentication remote code execution (RCE) flaws in nginx's HTTP/2 handling — a class of bug that can let an attacker run code on a web server without logging in first."
description: "Wiz published research describing pre-authentication remote code execution (RCE) flaws in nginx's HTTP/2 handling — a class of bug that can let an attacker run code on a web server without logging in first."
section: "tech-industry"
rank: 120
edition: 1
section_rank: 1
score: 8.0
status: "Demonstrated"
source_name: "wiz.io"
source_url: "https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50547374"
published_at: "2026-11-18T15:19:55+00:00"
tags: ["nginx", "http/2", "remote code execution", "vulnerability disclosure", "security"]
topics: ["nginx", "http-2", "remote-code-execution", "vulnerability-disclosure", "security"]
order: "20261118-1-979"
image: "/assets/stories/2026-11-18/wiz-reports-pre-auth-rce-in-nginx-http-2-handling-ff0c-share.jpg"
art: "/assets/stories/2026-11-18/wiz-reports-pre-auth-rce-in-nginx-http-2-handling-ff0c.jpg"
thumb: "/assets/stories/2026-11-18/wiz-reports-pre-auth-rce-in-nginx-http-2-handling-ff0c-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g49aeda4f6dcfa7f3853bb91f3073980ac3584c0b51112bd4c8165808f3013d59241e1ffcb4ea9ef158073d9393caee9b_1280.jpg", "author": "kewl", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/server-room-datacenter-network-90389/", "provider": "Pixabay", "width": 4818, "height": 3212}
---

{% raw %}
<div class="story-lead" markdown="1">

Wiz published research describing pre-authentication remote code execution (RCE) flaws in nginx's HTTP/2 handling — a class of bug that can let an attacker run code on a web server without logging in first. The same flaws are separately claimed by Xint, a Darpa-backed security company that told Forbes its AI models, GPT 6.1 Sol and GPT-6 Luna, found RCE vulnerabilities in nginx; Wiz says it had independently found the same bugs.

The write-up is a research blog, not an official nginx advisory, and no evidence of active exploitation was presented. Commenters noted that a fix appears to have landed in nginx's open-source repository roughly a week before the disclosure, with a commit crediting "Reported by Xint.io" but no public notice telling operators to disable HTTP/2 in the meantime.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** Wiz's research post describes pre-authentication remote code execution vulnerabilities in nginx's HTTP/2 handling; Forbes reported that Xint says its AI models found RCE flaws in nginx and that Wiz says it separately found the same flaws. Cybersecurity News reported that both flaws carry a CVSS 4.0 score of 9.2 and named Ikotas Labs, Metnir, Rapid7 and Xint as independent finders across the two disclosures.
- **Not yet confirmed:** The supplied evidence contains no official nginx/F5 advisory, affected-version list or patch version; the claim that the fix is nginx 1.31.9 comes from a single outlet, and there is no evidence of active exploitation. Community comments that the bug was fixed in the open-source repository a week before disclosure, with a commit crediting Xint, remain unverified.

</div>

## Background

HTTP/2 support — which lets a single connection carry many multiplexed requests — has shipped in nginx since version 1.9.5 in 2015, so the affected code path exists in more than a decade of releases. Wiz's write-up and Xint's separate "nginx2root" publication describe overlapping findings: Wiz says both of its flaws require HTTP/2 to be enabled, while Xint says disabling HTTP/2 on affected listening ports blocks CVE-2026-123007 and CVE-2026-123633 but not the three other nginx flaws it lists, one of which it chains with a kernel exploit to reach root on the host. Forbes reports that Xint credits the GPT 6.1 Sol and GPT-6 Luna models for its discovery, and that Wiz says it found the same flaws independently.

## Why it matters

Anyone running nginx with HTTP/2 enabled has a concrete decision to make: apply the upstream fix or turn HTTP/2 off, a workaround commenters described as simple and one that argues for a faster public warning. The reported gap between the public fix commit and the write-up also matters for operators, because it gave anyone watching the repository a window to study a pre-auth RCE before defenders were told to act.

## What to watch

Whether nginx's maintainers or F5 publish an official advisory with CVE identifiers and the affected version ranges, which would let operators confirm whether their builds are exposed.

## Coverage of this story

- 2026-11-18 · wiz.io: [Pre-auth RCE in Nginx HTTP/2 handling](https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities)
- 2026-11-18 · Forbes: [Cybersecurity company Xint says it found RCE vulnerabilities in Nginx using GPT 6.1 Sol and GPT-6 Luna; Wiz says it had separately found the same flaws (Thomas Brewster/Forbes)](https://www.forbes.com/sites/thomasbrewster/2026/11/18/ai-finds-major-web-security-flaws/)

## Further reading

- [Unauthenticated Remote Code Execution in NGINX ... | Wiz Blog](https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities)
- [NGINX 2 Root: New Remote Code Execution Vulnerabilities in nginx ...](https://xint.io/blog/nginx2root-remote-code-execution)
- [NGINX 2 Root by Xint — From nginx visitor to root of the server host](https://nginx2root.com/)
- [NGINX HTTP/2 Flaws Could Allow Memory Corruption and Remote ...](https://cybersecuritynews.com/nginx-http-2-vulnerabilities/)
- [PSA: Immediately Patch NGINX Web Servers Due to Critical ...](https://finance.yahoo.com/technology/ai/articles/psa-immediately-patch-nginx-servers-160000691.html?fr=sycsrp_catchall)
- [nginx Advisories Jump to 26 From 2 as AI Finds Critical RCEs](https://fourweekmba.com/ai-nginx-advisories-jump-to-26-from-2-as-ai-finds-critical-rces/)

<div class="community" markdown="1">

## Community discussion: opinion, not evidence

The strongest argument in the thread, from black3r, is about disclosure timing: the fix was reportedly visible in the open-source repo about a week earlier, so skilled attackers could have mined it, and a bare notice to disable HTTP/2 would have cost little. Other commenters reacted to the AI angle — one worried about the volume of vulnerable small servers — while hokkos flagged a separate oddity, an empty SHA-256 digest on the nginx 1.31.9-alpine Docker image, which is an observation about that image rather than a stated link to the flaws.

</div>

{% endraw %}
