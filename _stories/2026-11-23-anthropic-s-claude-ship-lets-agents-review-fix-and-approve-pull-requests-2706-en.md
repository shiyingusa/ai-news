---
layout: story
lang: en
date: 2026-11-23 18:22:43 -0500
issue: "2026-11-23"
story_id: "anthropic-s-claude-ship-lets-agents-review-fix-and-approve-pull-requests-2706"
permalink: "/2026/11/23/anthropic-s-claude-ship-lets-agents-review-fix-and-approve-pull-requests-2706/"
title: "Anthropic's Claude Ship lets agents review, fix and approve pull requests"
dek: "Anthropic announced Claude Ship, a developer product that lets Claude agents review, fix and approve GitHub pull requests, with two new agents — PR Steward and Claude Approvals — launching in beta."
description: "Anthropic announced Claude Ship, a developer product that lets Claude agents review, fix and approve GitHub pull requests, with two new agents — PR Steward and Claude Approvals — launching in beta."
section: "ai-news"
rank: 203
edition: 2
section_rank: 3
score: 7.0
status: "Released"
source_name: "TechCrunch AI"
source_url: "https://techcrunch.com/2026/11/23/anthropic-launches-claude-ship-letting-ai-agents-review-fix-and-approve-code-changes/"
via: null
discussion_url: null
published_at: "2026-11-23T22:05:50+00:00"
tags: ["AI agents", "AI coding", "Anthropic", "developer tools", "code review"]
topics: ["ai-agents", "ai-coding", "anthropic", "developer-tools", "code-review"]
order: "20261123-2-996"
image: "/assets/stories/2026-11-23/anthropic-s-claude-ship-lets-agents-review-fix-and-approve-pull-requests-2706-share.jpg"
art: "/assets/stories/2026-11-23/anthropic-s-claude-ship-lets-agents-review-fix-and-approve-pull-requests-2706.jpg"
thumb: "/assets/stories/2026-11-23/anthropic-s-claude-ship-lets-agents-review-fix-and-approve-pull-requests-2706-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/gf197094dd7ec7811ecc8e63b920a2339599143b705da4f4cd89990cb95a6fd6828642e29c1366631ddca47550465effcf79f68332161577784d3da6cc8de4737_1280.jpg", "author": "Innovalabs", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/software-development-developer-6523979/", "provider": "Pixabay", "width": 7360, "height": 4912}
---

{% raw %}
<div class="story-lead" markdown="1">

Anthropic announced Claude Ship, a developer product that lets Claude agents review, fix and approve GitHub pull requests, with two new agents — PR Steward and Claude Approvals — launching in beta. PR Steward steps in on failing CI checks, merge conflicts, and review feedback from Anthropic's Code Review or from other review tools and team members, while Claude Approvals handles the sign-off step according to team policies, ZDNET reported. The beta is limited to Claude Team and Enterprise tiers, and it builds on Claude's Code Review feature, which Anthropic announced in March and made generally available in October. Anthropic has not disclosed pricing, a general-availability date, or how much autonomy the approval agent is granted.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

Verified: Anthropic announced Claude Ship, with the PR Steward and Claude Approvals agents entering beta today, per The Verge; ZDNET reported the beta covers GitHub pull requests on Claude Team and Enterprise tiers and that approvals follow team policies. Anthropic's earlier Code Review feature was announced in March and reached general availability in October, according to the company's own articles.

</div>

## Background

A pull request is a proposed code change that teammates read, discuss and approve before it merges into the main codebase. Claude already had a Code Review feature, announced in March 2026 and made generally available in October 2026, that commented on pull requests but left the fixing and the sign-off to humans; PR Steward and Claude Approvals are the new pieces that act on those comments rather than only writing them. AI Daily Radar's November 18 digest noted secondary coverage of Harvard researchers' reported conclusion that AI coding agents had moved the developer bottleneck from writing code to reviewing it, which is the gap Anthropic is now selling against.

## Why it matters

Approvals, not reviews, are what Claude Ship changes: Claude Approvals decides which pull requests to approve based on the team's own written policy, so that ruleset rather than an individual reviewer becomes the gate on what merges. Both agents run from Claude Code through a new `/ship` command, and Anthropic says PR Steward fixes failing CI checks, merge conflicts and review feedback but does not approve or merge — teams configuring the workflow should keep fixing and approving as separate steps. Access during the beta is limited to Claude Team and Enterprise tiers.

## What to watch

Watch for Anthropic to publish Claude Ship's pricing and a general-availability date beyond the Team and Enterprise beta, along with documentation of what permissions and guardrails constrain the Claude Approvals agent.

## Coverage of this story

- 2026-11-23 · The Verge AI: [Claude AI can review pull requests and ship fixes on its own now](https://www.theverge.com/ai-artificial-intelligence/1040134/anthropic-claude-ship-ai-pull-requests)
- 2026-11-23 · ZDNET: [Anthropic unveils Claude Ship, letting Claude review, fix, and approve GitHub pull requests based on team policies, in beta for Claude Team and Enterprise tiers (Radhika Rajkumar/ZDNET)](https://www.zdnet.com/innovation/claude-ship-code-how-to-try/)
- 2026-11-23 · TechCrunch AI: [Anthropic launches Claude Ship, letting AI agents review, fix, and approve code changes](https://techcrunch.com/2026/11/23/anthropic-launches-claude-ship-letting-ai-agents-review-fix-and-approve-code-changes/)

## Further reading

- [2026-11-18 — Harvard researchers link AI coding agents to a code-review bottleneck](https://complexdiscovery.com/harvard-researchers-find-ai-coding-agents-shifted-the-bottleneck-to-code-review/)
- [Introducing Claude Ship | Claude by Anthropic](https://claude.com/resources/articles/introducing-claude-ship)
- [Claude Ship | Automate pull requests review and fixes](https://claude.com/product/claude-ship)
- [Anthropic's Claude Ship Lets Claude Approve Pull Requests by ...](https://aiweekly.co/alerts/anthropics-claude-ship-lets-claude-approve-pull-requests-by-policy)

{% endraw %}
