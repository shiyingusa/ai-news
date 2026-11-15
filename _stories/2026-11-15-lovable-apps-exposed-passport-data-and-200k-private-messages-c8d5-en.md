---
layout: story
lang: en
date: 2026-11-15 06:00:00 -0500
issue: "2026-11-15"
story_id: "lovable-apps-exposed-passport-data-and-200k-private-messages-c8d5"
permalink: "/2026/11/15/lovable-apps-exposed-passport-data-and-200k-private-messages-c8d5/"
title: "Lovable apps exposed passport data and 200K private messages"
dek: "Security research published at crissyfield.de reports that apps built with Lovable, the AI app builder, exposed passport details and more than 200,000 private messages."
section: "ai-news"
rank: 2
section_rank: 2
score: 7.0
status: null
source_name: "crissyfield.de"
source_url: "https://www.crissyfield.de/research/lovable-en/"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50499017"
published_at: "2026-11-14T17:43:10+00:00"
tags: ["AI app builders", "vibe coding", "security", "data exposure", "Supabase"]
topics: ["ai-app-builders", "vibe-coding", "security", "data-exposure", "supabase"]
order: "20261115-997"
image: "/assets/stories/2026-11-15/lovable-apps-exposed-passport-data-and-200k-private-messages-c8d5-share.jpg"
art: "/assets/stories/2026-11-15/lovable-apps-exposed-passport-data-and-200k-private-messages-c8d5.jpg"
thumb: "/assets/stories/2026-11-15/lovable-apps-exposed-passport-data-and-200k-private-messages-c8d5-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g9d59827fd194b7be3e4060d1ed9342b4be4c962f8a920fcfbf63128dabb6ed28c693981535204d0552b746c68da56731574876f347fb1fb9beb8a55ce0b2ce54_1280.jpg", "author": "cookieone", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/technology-network-storage-industry-8118380/", "provider": "Pixabay", "width": 6016, "height": 4016}
---

{% raw %}
<div class="story-lead" markdown="1">

Security research published at crissyfield.de reports that apps built with Lovable, the AI app builder, exposed passport details and more than 200,000 private messages. In the Hacker News thread, Lovable's head of security attributed the exposures to insufficient Row-Level Security (RLS), the Supabase/Postgres rules that decide which rows a signed-in user can read or write when the browser talks directly to the database. Lovable says it scans every app automatically before publishing and offers a free, deeper SAST (static application security testing) scan, with a "Fix" option and background auto-fix for findings. The report does not specify how many apps or users were affected, and the post's author said only that the situation is "fairly self-explanatory."

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** The researcher who wrote the report (HN user neathack, publishing with the Crissy Field team) confirmed authorship in the thread, and the report states that apps built with Lovable exposed passport details and more than 200,000 private messages. Lovable's Head of Security, Igor, responding in the same thread, attributed the exposures to insufficient Row-Level Security in those apps and did not dispute the findings.
- **Not yet confirmed:** The number of affected apps and users, the exposure window and whether all the reported data has been remediated rest on this single research post, whose full text was not supplied. Lovable's claim that its automatic pre-publish scanning and optional auto-fix would catch or resolve such issues is the vendor's own account, and a commenter's assertion that Supabase changed its insecure defaults on October 30 while existing projects keep the old ones is unverified here.

</div>

## Background

Lovable is an AI app builder that generates full-stack web apps, commonly wiring the browser frontend directly to a Supabase (hosted Postgres) backend using a public API key. In that architecture there is no application server in the middle to enforce access checks, so Row-Level Security — Postgres policies that restrict which rows each user may read or write — is the only barrier between one visitor's data and everyone else's. Apps assembled by builders unfamiliar with database permissions can therefore go live with missing or overly permissive policies. Commenters also pointed to a long-running Supabase discussion about permissive defaults for existing projects, a claim attributed to community members rather than established here.

## Why it matters

For teams shipping Lovable apps on Supabase, this is a configuration failure rather than a sophisticated attack: RLS protects nothing until policies are defined for each table, and the affected apps had insufficient policies. Because commenters report that Supabase's newer defaults may not apply to existing projects, the practical action is to audit already-published apps table by table and run the scanner's fixes.

## What to watch

Watch Supabase's GitHub discussion #4547 for confirmation that its changed defaults cover existing projects, and Lovable for published results from the pre-publish scanning it says runs on every app.

## From the comments

Commenters split the blame: yakkomajuri argued that having the frontend talk directly to Supabase with RLS as the only guardrail was always "a minefield," while SOLAR_FIELDS pointed to Supabase's years-old decision to ease onboarding at the cost of security and said existing projects may still run the old defaults. Oras noted that AI-generated apps mainly lower the skill needed to find such exposures.

{% endraw %}
