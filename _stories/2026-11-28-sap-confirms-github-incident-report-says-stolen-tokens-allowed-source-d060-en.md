---
layout: story
lang: en
date: 2026-11-28 06:26:43 -0500
issue: "2026-11-28"
story_id: "sap-confirms-github-incident-report-says-stolen-tokens-allowed-source-d060"
permalink: "/2026/11/28/sap-confirms-github-incident-report-says-stolen-tokens-allowed-source-d060/"
title: "SAP confirms GitHub incident; report says stolen tokens allowed source-code changes, SecurityWeek reports"
dek: "SAP has confirmed a cybersecurity incident after detecting suspicious activity on GitHub, the code-hosting platform where it keeps source code."
description: "SAP has confirmed a cybersecurity incident after detecting suspicious activity on GitHub, the code-hosting platform where it keeps source code."
section: "tech-industry"
rank: 17
edition: 0
section_rank: 1
score: 7.0
status: "Announced"
source_name: "SecurityWeek"
source_url: "https://www.securityweek.com/sap-confirms-cyberattack-source-code-reportedly-compromised/"
via: "Techmeme"
discussion_url: null
published_at: "2026-11-27T16:35:08+00:00"
tags: ["cybersecurity", "SAP", "source code", "GitHub", "security incident"]
topics: ["cybersecurity", "sap", "source-code", "github", "security-incident"]
order: "20261128-0-982"
image: "/assets/stories/2026-11-28/sap-confirms-github-incident-report-says-stolen-tokens-allowed-source-d060-share.jpg"
art: "/assets/stories/2026-11-28/sap-confirms-github-incident-report-says-stolen-tokens-allowed-source-d060.jpg"
thumb: "/assets/stories/2026-11-28/sap-confirms-github-incident-report-says-stolen-tokens-allowed-source-d060-640.jpg"
photo_credit: {"url": "https://thumb.wikimedia.org/wikipedia/commons/thumb/8/83/SAP_AG_headquarter_Walldorf_building_1.jpg/1920px-SAP_AG_headquarter_Walldorf_building_1.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail", "author": "Vladislav Bezrukov from Walldorf, Germany", "licence": "CC BY 2.0", "licence_url": "https://creativecommons.org/licenses/by/2.0", "source_url": "https://commons.wikimedia.org/wiki/File:SAP_AG_headquarter_Walldorf_building_1.jpg", "provider": "Wikimedia Commons", "width": 3008, "height": 2000}
---

{% raw %}
<div class="story-lead" markdown="1">

SAP has confirmed a cybersecurity incident after detecting suspicious activity on GitHub, the code-hosting platform where it keeps source code. According to SecurityWeek, attackers obtained authentication tokens belonging to SAP employees and used them to copy and alter source code stored there.

SAP has not publicly said which repositories or products were affected, how many accounts were involved, or whether altered code reached any software it ships. The company's confirmation covers the suspicious GitHub activity itself; the token theft and code alteration rest on the outlet's reporting.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** SAP confirmed an IT security incident and said it detected suspicious activity on GitHub, according to SecurityWeek and BleepingComputer.
- **Not yet confirmed:** That attackers stole SAP employees' authentication tokens and used them to copy and alter source code rests on DER SPIEGEL reporting and insider sources cited by BleepingComputer; SAP has not confirmed which repositories were affected, whether altered code reached products, how many tokens were involved, or when the activity occurred.

</div>

## Background

GitHub access tokens — including personal access tokens and OAuth tokens issued to developer tools — are long-lived credentials that let a user or script act on repositories without re-entering a password. Because they authenticate directly to the API, they can bypass password checks and often multi-factor prompts, which is why stolen tokens are a common route into code hosting accounts. For a vendor like SAP, whose enterprise products are built and shipped from its repositories, unauthorized changes to source code raise questions about build integrity and not just data exposure.

## Why it matters

For SAP customers and developers, the concern is code integrity rather than uptime: if employee tokens were enough to modify repositories, then pulled code should be checked against expected commits and signed releases rather than trusted because it sits in SAP's GitHub organisation. Until SAP names the affected repositories, teams cannot tell whether anything they build on was touched.

## What to watch

Watch for SAP's own incident statement or a SecurityWeek follow-up specifying which repositories and how many accounts were involved, and whether any altered code reached a released product.

## Further reading

- [SAP Confirms Cyberattack, Source Code Reportedly... - SecurityWeek](https://www.securityweek.com/sap-confirms-cyberattack-source-code-reportedly-compromised/)
- [SAP Confirms Security Incident as Hackers Reportedly Steal ...](https://cybersecuritynews.com/sap-security-incident/)
- [SAP confirms security incident after suspicious GitHub activity](https://www.bleepingcomputer.com/news/security/sap-confirms-security-incident-after-suspicious-github-activity/)

{% endraw %}
