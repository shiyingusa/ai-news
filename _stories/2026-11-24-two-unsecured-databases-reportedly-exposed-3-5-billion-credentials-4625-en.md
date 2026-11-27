---
layout: story
lang: en
date: 2026-11-24 06:26:49 -0500
issue: "2026-11-24"
story_id: "two-unsecured-databases-reportedly-exposed-3-5-billion-credentials-4625"
permalink: "/2026/11/24/two-unsecured-databases-reportedly-exposed-3-5-billion-credentials-4625/"
title: "Two unsecured databases reportedly exposed 3.5 billion credentials"
dek: "WIRED reports that a pair of unsecured databases exposed 3.5 billion usernames, passwords and documents belonging to hundreds of millions of people — data the outlet says could let attackers \"own\" a victim's digital life."
description: "WIRED reports that a pair of unsecured databases exposed 3.5 billion usernames, passwords and documents belonging to hundreds of millions of people — data the outlet says could let attackers \"own\" a victim's digital life."
section: "tech-industry"
rank: 11
edition: 0
section_rank: 3
score: 7.0
status: null
source_name: "Wired"
source_url: "https://www.wired.com/story/3-billion-usernames-passwords-and-documents-leaked-online/"
via: null
discussion_url: null
published_at: "2026-11-24T11:00:00+00:00"
tags: ["cybersecurity", "data breach", "privacy", "credentials", "unsecured databases"]
topics: ["cybersecurity", "data-breach", "privacy", "credentials", "unsecured-databases"]
order: "20261124-0-988"
image: "/assets/stories/2026-11-24/two-unsecured-databases-reportedly-exposed-3-5-billion-credentials-4625-share.jpg"
art: "/assets/stories/2026-11-24/two-unsecured-databases-reportedly-exposed-3-5-billion-credentials-4625.jpg"
thumb: "/assets/stories/2026-11-24/two-unsecured-databases-reportedly-exposed-3-5-billion-credentials-4625-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/gb488e1f56b2c1c5c65193f316b084dc393da1c21f3df093b0a0e1bde647634881d665553acb3c372a18e675f53f810f0_1280.jpg", "author": "kewl", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/server-room-datacenter-network-90389/", "provider": "Pixabay", "width": 4818, "height": 3212}
---

{% raw %}
<div class="story-lead" markdown="1">

WIRED reports that a pair of unsecured databases exposed 3.5 billion usernames, passwords and documents belonging to hundreds of millions of people — data the outlet says could let attackers "own" a victim's digital life. "Unsecured" means the databases were left reachable without authentication, rather than being broken into.

The report does not name the companies operating the databases, describe how the data was found or by whom, or say whether the exposed records have since been secured or taken offline. The figure of 3.5 billion comes from the reporting itself; no independent verification or sample of the records has been published.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** WIRED reports that two unsecured databases were found holding sensitive information — usernames, passwords and documents — on hundreds of millions of people, including data that could let an attacker take over a victim's accounts.
- **Not yet confirmed:** The 3.5 billion figure appears in the report's headline without an itemized breakdown; the available reporting does not name the affected companies or services, say who discovered the databases, establish that the records are genuine and current rather than compiled from older leaks, or confirm whether the databases have since been secured.

</div>

## Background

Both stores were left unauthenticated — reachable from the open internet with no login or password — a configuration failure rather than an intrusion: anyone who located the storage endpoint could read and download records directly, without exploiting a software flaw. The two exposures are unrelated to each other, according to the findings shared with WIRED, so this is a pair of separate misconfigurations rather than one breached provider.

## Why it matters

Exposed username-and-password pairs are the raw material for credential stuffing, in which attackers replay leaked logins against other services on the assumption that people reuse them — so the practical exposure extends well beyond whatever service held the data. The immediate problem for users is that the report names no affected company, leaving them unable to check whether their accounts were in the set; until the operators are identified, the only defensive step available is the generic one of changing reused passwords and enabling two-factor authentication.

## What to watch

Watch for the databases to be secured or taken offline, and for the identity of their operators or any confirmation from affected companies — the detail that would let users determine whether they are in the exposed set.

## Further reading

- [Database Leaks Expose 3.5 Billion Usernames, Passwords, and ...](https://www.wired.com/story/3-billion-usernames-passwords-and-documents-leaked-online/)
- [Database Leaks Expose 3.5 Billion Usernames, Passwords, and ...](https://imtr.net/article/database-leaks-expose-35-billion-usernames-passwords-and-documents-5900)

{% endraw %}
