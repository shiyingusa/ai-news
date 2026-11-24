---
layout: story
lang: en
date: 2026-11-24 18:23:54 -0500
issue: "2026-11-24"
story_id: "anthropic-says-mcp-sdk-tops-700-million-monthly-downloads-adds-agent-73b0"
permalink: "/2026/11/24/anthropic-says-mcp-sdk-tops-700-million-monthly-downloads-adds-agent-73b0/"
title: "Anthropic says MCP SDK tops 700 million monthly downloads, adds agent features"
dek: "Anthropic says its SDK for the Model Context Protocol (MCP, an open standard for connecting AI models to external tools and data) now exceeds 700 million monthly downloads, roughly two years after the protocol launched."
description: "Anthropic says its SDK for the Model Context Protocol (MCP, an open standard for connecting AI models to external tools and data) now exceeds 700 million monthly downloads, roughly two years after the protocol launched."
section: "ai-news"
rank: 204
edition: 2
section_rank: 4
score: 7.0
status: "Announced"
source_name: "The Decoder"
source_url: "https://the-decoder.com/anthropic-tops-700-million-monthly-mcp-sdk-downloads-and-expands-the-protocol-for-more-autonomous-ai-agents/"
via: null
discussion_url: null
published_at: "2026-11-24T19:23:41+00:00"
tags: ["MCP", "Anthropic", "AI agents", "developer tools", "protocols"]
topics: ["mcp", "anthropic", "ai-agents", "developer-tools", "protocols"]
order: "20261124-2-995"
image: "/assets/stories/2026-11-24/anthropic-says-mcp-sdk-tops-700-million-monthly-downloads-adds-agent-73b0-share.jpg"
art: "/assets/stories/2026-11-24/anthropic-says-mcp-sdk-tops-700-million-monthly-downloads-adds-agent-73b0.jpg"
thumb: "/assets/stories/2026-11-24/anthropic-says-mcp-sdk-tops-700-million-monthly-downloads-adds-agent-73b0-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g4e61d8d4b097236d149097b7a908b1e3bb7d6a90e9abf287230d3feaf3c8b032f1472535d2074de66001f7b0df21232e74ce34a77471860dc39517489bfc3f74_1280.jpg", "author": "andreas160578", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/stress-programmer-developer-ibm-1331259/", "provider": "Pixabay", "width": 5616, "height": 3744}
---

{% raw %}
<div class="story-lead" markdown="1">

Anthropic says its SDK for the Model Context Protocol (MCP, an open standard for connecting AI models to external tools and data) now exceeds 700 million monthly downloads, roughly two years after the protocol launched. The company is also expanding the protocol with features aimed at more autonomous agents: background tasks, the ability to ask users follow-up questions, and file uploads — capabilities the report describes as intended to let Claude work more independently. The download figure is Anthropic's own and is not reported as independently measured, and the report does not specify which specification or SDK version ships the new features or whether they are generally available to developers yet.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** The Decoder reported that Anthropic says monthly downloads of its MCP software development kit now exceed 700 million, two years after the Model Context Protocol launched, and that the protocol is gaining background tasks, follow-up questions to users and file uploads aimed at letting Claude work more independently.
- **Not yet confirmed:** How the 700 million figure is counted (package downloads versus installs or users, and over what period), and whether any independent measure backs it; whether the three new features have shipped, are in preview, or are only planned; and which Claude products or plans get them, from what date, at what price, and under which protocol version. The Decoder's account is secondary reporting and gives no link or detailed quotation from an Anthropic announcement.

</div>

## Background

MCP, the Model Context Protocol, is an open interface standard Anthropic introduced roughly two years before this report that lets AI models call external tools and data sources in a uniform way, rather than each integration being built separately. The download figure counts SDK downloads by developers, not end users or active deployments.

## Why it matters

For developers building MCP servers, the practical change is that integrations may no longer be single request-and-response calls: background tasks, mid-task questions to the user and file uploads each require handling state, user interaction and payloads that earlier MCP implementations did not need. Teams maintaining servers should check which capability set their clients and SDK versions actually support before relying on the new features.

## What to watch

Watch Anthropic's MCP specification and SDK release notes for the version number that formally includes background tasks, user follow-up prompts and file uploads, and for whether the 700 million monthly download figure is broken out or independently measured.

{% endraw %}
