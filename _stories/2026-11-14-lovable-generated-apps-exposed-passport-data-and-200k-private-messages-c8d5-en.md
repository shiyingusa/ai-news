---
date: 2026-11-14 06:00:00 -0500
layout: "story"
lang: "en"
issue: "2026-11-14"
story_id: "lovable-generated-apps-exposed-passport-data-and-200k-private-messages-c8d5"
permalink: "/2026/11/14/lovable-generated-apps-exposed-passport-data-and-200k-private-messages-c8d5/"
title: "Lovable-generated apps exposed passport data and 200K private messages via default keys"
dek: "Security research on Lovable, an AI app builder, found that many apps it generated exposed sensitive user data—including passport details and more than 200,000 private messages—through publicly shipped read-only API keys and permissive…"
section: "ai-news"
rank: 2
section_rank: 2
score: 7.0
source_name: "Hacker News · armcat"
source_url: "https://www.crissyfield.de/research/lovable-en/"
discussion_url: "https://news.ycombinator.com/item?id=50499017"
published_at: null
tags: ["AI app builders", "security vulnerability", "Lovable", "Supabase", "data exposure"]
topics: ["ai-app-builders", "security-vulnerability", "lovable", "supabase", "data-exposure"]
order: "20261114-997"
image: "/assets/stories/2026-11-14/lovable-generated-apps-exposed-passport-data-and-200k-private-messages-c8d5-share.jpg"
art: "/assets/stories/2026-11-14/lovable-generated-apps-exposed-passport-data-and-200k-private-messages-c8d5.jpg"
thumb: "/assets/stories/2026-11-14/lovable-generated-apps-exposed-passport-data-and-200k-private-messages-c8d5-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g8abbaab63028c6a3f1462da0a56e12db7387b450b4a1cbaf24905e418332f5ba642e5edc73f9ed6e39062b3691662e9af6f789216a423925e461b8209f9aee58_1280.jpg", "author": "Alexas_Fotos", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/handyman-construction-site-workers-3094035/", "provider": "Pixabay", "width": 5851, "height": 3567}
---

{% raw %}
<div class="story-lead" markdown="1">

Security research on Lovable, an AI app builder, found that many apps it generated exposed sensitive user data—including passport details and more than 200,000 private messages—through publicly shipped read-only API keys and permissive Supabase defaults. The issue affects people using those generated apps, not a failure of the underlying model, and centers on Supabase, the hosted database and authentication service many such apps rely on. The write-up's author confirmed the post on Hacker News, but the available account does not specify how many apps were affected or whether the exposed data has been secured.

</div>

## Context

Lovable is an AI app builder that generates full web applications and can connect them to Supabase, a hosted Postgres backend with authentication and auto-generated APIs. Such apps ship a read-only Supabase API key in the browser, so that key is public by design; what it can read is supposed to be limited by row-level security, the per-table rules that filter database rows. A commenter on the item argued that Supabase chose permissive defaults years ago to ease onboarding and that existing projects may still retain them.

## Check your Supabase defaults

Builders who shipped Lovable apps on stock Supabase settings should assume the public anon key bundled in their client code can read more than intended: a Supabase maintainer discussion notes that under default settings it is "quite easy" for anonymous users to probe an API, with the caveat that requests still need a valid JWT. The practical remediation is to enable row-level security and restrict the anon role's access rather than relying on the key being labeled read-only.

## Community discussion

Commenters debated whether the exposure should be called a breach: one argued that reading data made public by a shipped read-only API key is not hacking and that the publication itself is the leak, while another blamed Supabase's permissive defaults and said an October 30 fix may not cover existing projects. Others described AI-generated apps as easy, numerous targets whose users often do not understand the risk, and called for deny-by-default databases, least-privilege APIs, and automated authentication tests.

## Further reading

- [Connect to Supabase - Lovable Documentation](https://docs.lovable.dev/integrations/supabase)
- [Option to disable anon key access to database · supabase ...](https://github.com/orgs/supabase/discussions/4547)

{% endraw %}
