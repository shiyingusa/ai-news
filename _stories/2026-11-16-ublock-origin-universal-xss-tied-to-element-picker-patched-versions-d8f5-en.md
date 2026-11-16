---
layout: story
lang: en
date: 2026-11-16 06:00:00 -0500
issue: "2026-11-16"
story_id: "ublock-origin-universal-xss-tied-to-element-picker-patched-versions-d8f5"
permalink: "/2026/11/16/ublock-origin-universal-xss-tied-to-element-picker-patched-versions-d8f5/"
title: "uBlock Origin universal XSS tied to element picker; patched versions cited"
dek: "A security write-up reports a universal XSS vulnerability in uBlock Origin involving its website-driven element picker, the tool users invoke to select page elements for blocking."
description: "A security write-up reports a universal XSS vulnerability in uBlock Origin involving its website-driven element picker, the tool users invoke to select page elements for blocking."
section: "tech-industry"
rank: 31
edition: 0
section_rank: 1
score: 7.0
status: "Released"
source_name: "iter.ca"
source_url: "https://iter.ca/post/ubo-uxss/"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50513160"
published_at: "2026-11-16T02:04:48+00:00"
tags: ["uBlock Origin", "browser extension security", "XSS vulnerability", "security disclosure", "ad blocking"]
topics: ["ublock-origin", "browser-extension-security", "xss-vulnerability", "security-disclosure", "ad-blocking"]
order: "20261116-0-968"
image: "/assets/stories/2026-11-16/ublock-origin-universal-xss-tied-to-element-picker-patched-versions-d8f5-share.jpg"
art: "/assets/stories/2026-11-16/ublock-origin-universal-xss-tied-to-element-picker-patched-versions-d8f5.jpg"
thumb: "/assets/stories/2026-11-16/ublock-origin-universal-xss-tied-to-element-picker-patched-versions-d8f5-640.jpg"
photo_credit: null
---

{% raw %}
<div class="story-lead" markdown="1">

A security write-up reports a universal XSS vulnerability in uBlock Origin involving its website-driven element picker, the tool users invoke to select page elements for blocking. Universal XSS is a class of bug that can let a malicious page execute code in other sites' origins instead of being confined to its own. The write-up is not an official vendor advisory, and the item supplies no CVE, affected-version range, or project statement. Commenters say users should update to uBlock Origin 1.75.4 or uBO Lite 2026.1110.1816, or later, but those fixed versions are community-reported here rather than confirmed by the project.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** The write-up describes a universal XSS (cross-site scripting that can run on any site) in uBlock Origin's element picker, the tool that lets a website's page drive element selection; according to search results, the project's advisory GHSA-cmqw-9r2w-6wv2 rates the issue High and says it affected the Firefox and Chromium MV2 builds, with a milder related issue in uBO Lite.
- **Not yet confirmed:** The patched version numbers circulating — uBlock Origin 1.75.4 and uBO Lite 2026.1110.1816 — come from a community comment, not from the advisory text supplied here, and no independent exploit test, CVE identifier or release date is included; claims in the comments that the bug exposes a unique extension UUID usable for fingerprinting, and the reported figure of over 11 million Firefox users, rest on commenter reasoning and a single secondary report rather than the primary disclosure.

</div>

## Background

uBlock Origin's element picker is the feature that lets you right-click a page, click the element you want gone, and have the extension generate a matching filter rule; its overlay is injected into the page's own DOM so it can point at that page's elements. The picker can also be opened and pre-filled through a URL, which lets a website drive it into building a filter of the site's choosing — the mechanism behind the reported universal XSS. The project's release notes for the fix list validation of the filter "about to be created" in the element picker among the changes.

## Why it matters

Until the extension updates, a Firefox user on the MV2 build can be pushed from an ordinary page visit plus a click into accepting an attacker-authored *trusted* filter, and trusted filters are exactly what uBlock Origin uses to inject script — which is why the advisory classes this as universal XSS rather than a single-site bug. The practical step is to check that uBlock Origin has actually updated rather than assume it will: a commenter in the thread reported still running the vulnerable build, which is common when extensions update on a browser's own schedule. The MV3 build, uBO Lite, carries a related but less severe version of the issue, so it needs the same check.

## What to watch

Watch for an official uBlock Origin advisory or release note confirming the affected version range, the fixed builds, and whether the element-picker issue is fully resolved.

## Community discussion

Commenters focused on the architecture that places extension UI inside the page's DOM: one argued this can expose a password manager's suggested accounts to the site, and another asked why the rule-creation UI cannot live in browser chrome instead. A separate commenter raised whether a leaked UUID could become a stable fingerprint for ad-blocker users; these are opinions and hypotheses, not confirmed findings.

## Further reading

- [Universal XSS in uBlock Origin from website-driven element picker](https://iter.ca/post/ubo-uxss/)
- [Releases · gorhill/ uBlock · GitHub](https://github.com/gorhill/uBlock/releases)
- [uBlock Origin Lite - Microsoft Edge Add-ons GitHub - uBlockOrigin/uBOL-home: uBO Lite home (MV3) uBlock Origin Lite: Install, Filtering Modes & Limitations ... Releases · uBlockOrigin/uBOL-home · GitHub uBlock Origin patches a universal XSS bug in its element ... Releases · gorhill/uBlock · GitHub GitHub - gorhill/uBlock: uBlock Origin - An efficient blocker ...](https://microsoftedge.microsoft.com/addons/detail/ublock-origin-lite/cimighlppcgcoapaliogpjjdehbnofhn)
- [Universal XSS from website-driven element picker](https://github.com/gorhill/uBlock/security/advisories/GHSA-cmqw-9r2w-6wv2)
- [Universal XSS in uBlock Origin from website-driven element picker](https://iter.ca/post/ubo-uxss/)
- [Universal XSS in uBlock Origin from website-driven element picker](https://techbytes.app/posts/universal-xss-in-ublock-origin-from-website-driven-element-picker/)

{% endraw %}
