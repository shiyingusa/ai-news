---
layout: story
lang: en
date: 2026-11-24 18:24:23 -0500
issue: "2026-11-24"
story_id: "microsoft-declares-internal-code-red-after-exchange-online-outage-9bb2"
permalink: "/2026/11/24/microsoft-declares-internal-code-red-after-exchange-online-outage-9bb2/"
title: "Microsoft declares internal 'Code Red' after Exchange Online outage"
dek: "Microsoft has declared an internal “Code Red” overhaul of its engineering response practices after a November 12 outage cut access to Exchange Online, Teams and Outlook for users worldwide…"
description: "Microsoft has declared an internal “Code Red” overhaul of its engineering response practices after a November 12 outage cut access to Exchange Online, Teams and Outlook for users worldwide…"
section: "tech-industry"
rank: 215
edition: 2
section_rank: 3
score: 8.0
status: "Planned"
source_name: "Reuters"
source_url: "https://www.reuters.com/business/microsoft-declares-code-red-after-historic-outage-internal-memos-show-2026-11-24/"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50631157"
published_at: "2026-11-24T17:07:41+00:00"
tags: ["Microsoft", "outage", "cloud reliability", "internal communications"]
topics: ["microsoft", "outage", "cloud-reliability", "internal-communications"]
order: "20261124-2-984"
image: "/assets/stories/2026-11-24/microsoft-declares-internal-code-red-after-exchange-online-outage-9bb2-share.jpg"
art: "/assets/stories/2026-11-24/microsoft-declares-internal-code-red-after-exchange-online-outage-9bb2.jpg"
thumb: "/assets/stories/2026-11-24/microsoft-declares-internal-code-red-after-exchange-online-outage-9bb2-640.jpg"
photo_credit: {"url": "https://thumb.wikimedia.org/wikipedia/commons/thumb/d/d6/Aerial_Microsoft_West_Campus_August_2009.jpg/1920px-Aerial_Microsoft_West_Campus_August_2009.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail", "author": "Jelson25", "licence": "Public domain", "licence_url": "https://creativecommons.org/licenses/", "source_url": "https://commons.wikimedia.org/wiki/File:Aerial_Microsoft_West_Campus_August_2009.jpg", "provider": "Wikimedia Commons", "width": 4752, "height": 3168}
---

{% raw %}
<div class="story-lead" markdown="1">

Microsoft has declared an internal “Code Red” overhaul of its engineering response practices after a November 12 outage cut access to Exchange Online, Teams and Outlook for users worldwide, according to internal memos reviewed by Reuters that Microsoft has not published. In those memos, Microsoft 365 Core President Jason Henderson called the disruption the most customer-impacting outage in Exchange Online’s history and wrote that an urgent production fix in a recent incident took five to six days to reach worldwide saturation, against a one-hour target for the most urgent security fixes.

Microsoft’s November 20 post-incident report attributed the downtime to an undetected Windows scalability defect introduced in July that caused lock contention in gateway processes; a Teams traffic failover then added load while maintenance had left nearly 14 percent of gateway server capacity offline.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** Reuters, citing internal memos it reviewed, reported that Microsoft declared a "Code Red" drive to overhaul how it prevents and responds to major service failures after the November 12 outage, and quoted Microsoft 365 Core President Jason Henderson calling it the most customer-impacting incident in Exchange Online's history. Microsoft's own post-incident report, dated November 20, traced the disruption to an undetected Windows scalability defect introduced in July that caused lock contention in gateway processes, worsened by a Teams traffic failover and maintenance that had left nearly 14 percent of gateway server capacity offline.
- **Not yet confirmed:** Microsoft has not published the memos or publicly confirmed the "Code Red" program or its targets — including the stated goal of moving an urgent fix from detection to safe worldwide deployment within one hour, which Henderson is quoted as saying the company has not reached ("we aren't here yet"), and the reported five to six days a recent urgent production fix took to reach worldwide saturation. Those figures and the characterization of the outage's record severity rest on Reuters' review of internal documents rather than an on-the-record Microsoft statement, and the memos do not set out a timeline or completion criteria for the overhaul.

</div>

## Background

The outage on November 12 cut off Exchange Online, Teams and Outlook for users worldwide; Microsoft's post-incident report, dated November 20, traced it to an undetected Windows scalability defect introduced in July that caused lock contention in gateway processes, then worsened when a Teams traffic failover pushed extra load onto infrastructure already running with nearly 14 percent of gateway server capacity offline for maintenance. According to the memos Reuters reviewed, the "Code Red" label is Microsoft's internal escalation for an overhaul of how its engineers detect and deploy fixes — an area where the company's own M365 Core president says an urgent production fix recently took five to six days to reach worldwide saturation, against a one-hour target for the most urgent security fixes.

## Why it matters

For Microsoft 365 customers, the report shows that a Teams traffic failover can hit gateway infrastructure already degraded by maintenance, so disaster-recovery plans that assume independent failure domains need testing against correlated capacity loss.

## What to watch

Watch for Microsoft to publish the engineering changes behind the internal “Code Red” and for any update to its November 20 post-incident report.

## Coverage of this story

- 2026-11-24 · Reuters: [Microsoft declares 'Code Red' after historic outage, internal memos show](https://www.reuters.com/business/microsoft-declares-code-red-after-historic-outage-internal-memos-show-2026-11-24/)
- 2026-11-24 · Ars Technica: [Microsoft's historic cloud outage exposed an engineering “fog of war”](https://arstechnica.com/gadgets/2026/11/microsofts-historic-cloud-outage-exposed-an-engineering-fog-of-war/)

## Further reading

- [EXCLUSIVE: Microsoft declares 'Code Red' after historic ...](https://www.reuters.com/business/microsoft-declares-code-red-after-historic-outage-internal-memos-show-2026-11-24/)
- [Exclusive-Microsoft Declares 'Code Red' After Historic Outage ...](https://money.usnews.com/investing/news/articles/2026-11-24/exclusive-microsoft-declares-code-red-after-historic-outage-internal-memos-show)
- [Microsoft Declares ‘Code Red’ After Historic 365 Outage](https://tech.yahoo.com/ai/copilot/articles/microsoft-declares-code-red-historic-183009480.html)

<div class="community" markdown="1">

## Community discussion: opinion, not evidence

Hacker News commenters debated whether staffing cuts contributed: one claimed Microsoft has shed roughly 45% of its 2022-era staff and said it is too easy to blame the outage on cuts but unrealistic to shrink that fast without losing something. Others argued the incident points to missing resilience practices such as gradual rollouts, chaos testing, or scale modeling.

</div>

{% endraw %}
