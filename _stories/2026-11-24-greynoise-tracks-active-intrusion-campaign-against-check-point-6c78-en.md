---
layout: story
lang: en
date: 2026-11-24 18:24:22 -0500
issue: "2026-11-24"
story_id: "greynoise-tracks-active-intrusion-campaign-against-check-point-6c78"
permalink: "/2026/11/24/greynoise-tracks-active-intrusion-campaign-against-check-point-6c78/"
title: "GreyNoise tracks active intrusion campaign against Check Point management servers"
dek: "GreyNoise says it is tracking an active intrusion campaign against Check Point security management servers, putting the administrative control point of customers' security deployments at the center of the warning."
description: "GreyNoise says it is tracking an active intrusion campaign against Check Point security management servers, putting the administrative control point of customers' security deployments at the center of the warning."
section: "tech-industry"
rank: 214
edition: 2
section_rank: 2
score: 8.0
status: null
source_name: "greynoise.io"
source_url: "https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50630594"
published_at: "2026-11-24T16:32:17+00:00"
tags: ["cybersecurity", "Check Point", "intrusion campaign", "threat intelligence", "vulnerability exploitation"]
topics: ["cybersecurity", "check-point", "intrusion-campaign", "threat-intelligence", "vulnerability-exploitation"]
order: "20261124-2-985"
image: "/assets/stories/2026-11-24/greynoise-tracks-active-intrusion-campaign-against-check-point-6c78-share.jpg"
art: "/assets/stories/2026-11-24/greynoise-tracks-active-intrusion-campaign-against-check-point-6c78.jpg"
thumb: "/assets/stories/2026-11-24/greynoise-tracks-active-intrusion-campaign-against-check-point-6c78-640.jpg"
photo_credit: {"url": "https://upload.wikimedia.org/wikipedia/commons/c/c4/Check_point_hq.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail_unscaled", "author": "דוד שי", "licence": "CC BY-SA 3.0", "licence_url": "https://creativecommons.org/licenses/by-sa/3.0", "source_url": "https://commons.wikimedia.org/wiki/File:Check_point_hq.jpg", "provider": "Wikimedia Commons", "width": 1919, "height": 1454}
---

{% raw %}
<div class="story-lead" markdown="1">

GreyNoise says it is tracking an active intrusion campaign against Check Point security management servers, putting the administrative control point of customers' security deployments at the center of the warning. The threat-intelligence vendor's post has drawn discussion, with readers focusing on how attackers gained initial access and whether affected organizations had exposed their management servers to the internet.

One commenter suggested CVE-2026-16232 as the common link across multiple Check Point customers, but that attribution is not confirmed.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** GreyNoise says it tracked an intrusion campaign against Check Point Security Management Servers, with confirmed activity from October 17 to November 2, 2026, affecting at least 22 organizations globally; Cybersecurity Dive and SecurityWeek relayed the report.
- **Not yet confirmed:** The supplied reports contain no Check Point statement confirming the intrusions, the 22-victim count, or GreyNoise's AI-enabled characterization; the initial access vector is unresolved, with community commenters speculating about an internet-exposed management server and a specific CVE, and SecurityWeek describes the campaign as likely ongoing beyond GreyNoise's confirmed window.

</div>

## Background

Check Point patched CVE-2026-16232 on July 22, 2026, alongside two other flaws in its Security Management platform (CVE-2026-62144 and CVE-2026-62145). CVE-2026-16232 is an authentication bypass affecting SmartConsole security management and multi-domain management deployments, rated 9.3 on the CVSS severity scale, and it was already being exploited in the wild to seize full administrative control of firewall management servers before this campaign was reported.

## Why it matters

For Check Point customers, the management server is the priority exposure: it is the administrative control point for security policy, so an intruder there can alter the protections the organization relies on. Defenders should determine whether those interfaces are reachable from the internet and restrict access while they investigate.

## What to watch

Watch for Check Point's own advisory or confirmation and for independent validation of whether CVE-2026-16232 is the initial access vector; either would give defenders a firmer basis for patching and exposure checks.

## Further reading

- [Critical Check Point Security Management Vulnerabilities Under...](https://labs.beazley.security/advisories/BSL-A1195)
- [Check Point SmartConsole CVE - 2026 - 16232 Authentication... | LinkedIn](https://www.linkedin.com/posts/codedefence_codedefence-checkpoint-smartconsole-activity-7487197195956375552-1pp7)
- [An Active Intrusion Campaign Against Check Point Security ...](https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign)
- [AI-enabled campaign targets Check Point Security Management ...](https://www.cybersecuritydive.com/news/ai-enabled-campaign-targets-check-point-security-management-servers/875622/)
- [Check Point Security Management Servers Hacked - SecurityWeek](https://www.securityweek.com/check-point-security-management-servers-hacked-in-ai-assisted-campaign/)

<div class="community" markdown="1">

## Community discussion: opinion, not evidence

The most useful thread questioned initial access: one reader suggested CVE-2026-16232 was the common link across multiple Check Point customers and asked whether all of them had internet-facing management servers, while others quoted a session-cookie forgery chain that reconstructed the V8 PRNG from Math.random() output. A separate argument held that Math.random() should be secure by default rather than relying on every application to use it correctly.

</div>

{% endraw %}
