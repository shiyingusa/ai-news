---
layout: story
lang: en
date: 2026-11-23 19:32:00 -0500
issue: "2026-11-23"
story_id: "ladybird-releases-first-alpha-of-its-from-scratch-browser-engine-60fd"
permalink: "/2026/11/23/ladybird-releases-first-alpha-of-its-from-scratch-browser-engine-60fd/"
title: "Ladybird releases first alpha of its from-scratch browser engine"
dek: "The Ladybird project released its first alpha on 23 November 2026, so macOS and Linux users can now install the browser without compiling it themselves."
description: "The Ladybird project released its first alpha on 23 November 2026, so macOS and Linux users can now install the browser without compiling it themselves."
section: "tech-industry"
rank: 227
edition: 2
section_rank: 1
score: 7.0
status: "Released"
source_name: "ladybird.org"
source_url: "https://ladybird.org/posts/alpha/"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50614249"
published_at: "2026-11-23T16:13:12+00:00"
tags: ["browsers", "open source", "web standards", "software releases", "privacy"]
topics: ["browsers", "open-source", "web-standards", "software-releases", "privacy"]
order: "20261123-2-972"
image: "/assets/stories/2026-11-23/ladybird-releases-first-alpha-of-its-from-scratch-browser-engine-60fd-share.jpg"
art: "/assets/stories/2026-11-23/ladybird-releases-first-alpha-of-its-from-scratch-browser-engine-60fd.jpg"
thumb: "/assets/stories/2026-11-23/ladybird-releases-first-alpha-of-its-from-scratch-browser-engine-60fd-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g26b80ec4dac2aa9e750c4633ed621739b73e20fb64a0af6cf7c971cd16aad691667c1bf5261a24ac29527daf0d6521fc9a0b363d5c3c77303235f60cbbd1fc0d_1280.jpg", "author": "Monoar_CGI_Artist", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/laptop-workstation-browsing-tablet-1483974/", "provider": "Pixabay", "width": 3807, "height": 2121}
---

{% raw %}
<div class="story-lead" markdown="1">

The Ladybird project released its first alpha on 23 November 2026, so macOS and Linux users can now install the browser without compiling it themselves. The engine implements its own HTML parsing, CSS, layout, JavaScript and WebAssembly, borrowing external components only for text shaping (HarfBuzz), 2D graphics (Skia), video (ffmpeg) and SQLite, and it runs separate tabs in separate processes. The project warns that some sites will not work and that it makes "no promises about security today", inviting security researchers to attack it and users to file crash and broken-site reports from inside the browser. One early tester reported that most sites he tried rendered correctly, including ffmpeg compiled to WebAssembly and a Pyodide Python REPL, though Datasette Lite failed on a missing `navigator.serviceWorker.startMessages` function.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** The Ladybird project published its first alpha on 23 November 2026, installable on macOS and Linux without compiling it yourself; the project's own October newsletter reported that it passed Safari Technology Preview on the Web Platform Tests suite on 26 October, after gaining roughly 75,650 passes in five days (Ladybird).
- **Not yet confirmed:** That the alpha is usable as a daily browser — the project itself warns that some sites will not work and that it will crash sometimes, and explicitly makes "no promises about security today." The 7x JetStream 3 WebAssembly speedup and the scale of coding-agent contributions are the project's own figures rather than independent measurements, and the smooth-rendering reports come from a handful of individual commenters and one blogger's testing, not a broad compatibility study.

</div>

## Background

Ladybird began inside SerenityOS, Andreas Kling's from-scratch operating system, where developers wrote their own browser instead of embedding Chromium, Gecko or WebKit; it later became a standalone project with its own HTML parser, CSS engine, layout and JavaScript implementation. Independent engines are scarce — in practice Chromium, WebKit and Gecko — which is why a new engine that renders real websites draws attention. In February 2026 Kling described porting parts of the LibJS JavaScript engine from C++ to 25,000 lines of Rust in two weeks with AI coding agents, and the project has kept using such agents to fill gaps in the web-platform-tests suite; until this alpha, anyone who wanted to try the browser had to compile it themselves.

## Why it matters

For anyone who wants to test a browser engine that is not Chromium, Gecko or WebKit, this is the first build that requires no toolchain, and the tester's process listing shows tab-level process isolation already in place. The same release notes argue against using it for real accounts: the project says it will crash sometimes and has not been hardened, so testing should stay on throwaway logins and use the built-in broken-site reporter rather than a primary Gmail or GitHub session.

## What to watch

Watch whether the filed Datasette Lite failure, caused by the missing service-worker `startMessages` API, is fixed, and what the project's next monthly "This Month in Ladybird" update reports on web-platform-tests passes and crash volume now that outside users are running the alpha.

## From the comments

Testers were enthusiastic: one said every site he tried rendered correctly and complained only of slightly jerky scrolling, while another reported that ProxMox's NoVNC remote console felt snappier than in Firefox. Others pushed for more than rendering parity — one commenter wants a non-compliant JavaScript mode that spoofs or randomizes fingerprinting values, plus finer-grained permissions — and another noted that swapping in production-grade libraries such as SQLite and Skia drove much of the improvement.

## Coverage of this story

- 2026-11-23 · ladybird.org: [Ladybird is now in alpha](https://ladybird.org/posts/alpha/)
- 2026-11-23 · Simon Willison: [Ladybird's first alpha release](https://simonwillison.net/2026/Nov/23/ladybird/)

## Further reading

- [This Month in Ladybird - October 2026 - Ladybird](https://ladybird.org/newsletter/2026-10-31/)

{% endraw %}
