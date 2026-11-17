---
layout: story
lang: en
date: 2026-11-17 06:00:00 -0500
issue: "2026-11-17"
story_id: "datasette-lite-runs-the-full-app-in-browser-via-service-workers-5ab3"
permalink: "/2026/11/17/datasette-lite-runs-the-full-app-in-browser-via-service-workers-5ab3/"
title: "Datasette Lite Runs the Full App in Browser via Service Workers"
dek: "A clear, first-hand explanation of rewriting Datasette Lite to run the full server-side Python app in the browser via service workers and Pyodide, presenting a transferable architecture pattern for WebAssembly preview environments."
description: "A clear, first-hand explanation of rewriting Datasette Lite to run the full server-side Python app in the browser via service workers and Pyodide, presenting a transferable architecture pattern for WebAssembly preview environments."
section: "tech-blog"
rank: 118
edition: 1
section_rank: 1
score: 7.0
status: null
source_name: "Simon Willison"
source_url: "https://simonwillison.net/2026/Nov/17/datasette-lite/"
via: null
discussion_url: null
published_at: "2026-11-17T16:48:33+00:00"
tags: ["service workers", "Pyodide", "WebAssembly", "Datasette", "browser-based preview environments"]
topics: ["service-workers", "pyodide", "webassembly", "datasette", "browser-based-preview-environments"]
order: "20261117-1-981"
image: "/assets/stories/2026-11-17/datasette-lite-runs-the-full-app-in-browser-via-service-workers-5ab3-share.jpg"
art: "/assets/stories/2026-11-17/datasette-lite-runs-the-full-app-in-browser-via-service-workers-5ab3.jpg"
thumb: "/assets/stories/2026-11-17/datasette-lite-runs-the-full-app-in-browser-via-service-workers-5ab3-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/gda7d80dae8577c83bc8b23c8f0171b28ade51ede26484a97e72adc9441b6786bd6b81f39db7751d4946050110d5fc4bf73f2a51a90e6fec9b044146eedcae0db_1280.jpg", "author": "Monoar_CGI_Artist", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/laptop-workstation-browsing-tablet-1483974/", "provider": "Pixabay", "width": 3807, "height": 2121}
---

{% raw %}
<div class="story-lead" markdown="1">

A clear, first-hand explanation of rewriting Datasette Lite to run the full server-side Python app in the browser via service workers and Pyodide, presenting a transferable architecture pattern for WebAssembly preview environments.

</div>

## Background

Datasette Lite, first launched in 2022, originally ran the server-side Datasette app in a Pyodide web worker and injected the resulting HTML into the page with innerHTML. That let basic pages work, but script tags in innerHTML do not execute, so JavaScript-dependent features and extra CSS or JavaScript assets failed.

## Solution

The rewrite registers a service worker for all of lite.datasette.io; an iframe requests normal Datasette URLs prefixed with /app/<random session>/, and the worker routes each request through the parent page to a dedicated Pyodide web worker. The per-tab session prefix prevents tabs sharing the domain-wide service worker from colliding when each URL asks for different plugins or settings. A web worker is still required because, the author says, Pyodide inside a service worker cannot retain state beyond roughly 30 seconds depending on the browser. Carefully composed URLs can install PyPI or wheel-file plugins, load databases, JSON, CSV, SQL or metadata, and select a released Datasette version or a GitHub ref; the author uses these links to demonstrate bugs and work-in-progress features. A later ?sqlite= parameter resolves one of 163 WebAssembly-compiled pysqlite3 wheels, making it possible to test Datasette against specific SQLite releases, while the author notes non-SQLite databases remain harder and the system has many moving parts.

## Takeaway

The author argues the architecture is not Datasette-specific: any Python app could use WebAssembly and Pyodide for cheap preview and debugging environments, with C and Rust extensions increasingly compilable and PEP 783 allowing Wasm wheels on PyPI.

{% endraw %}
