---
layout: story
lang: zh
date: 2026-11-17 06:00:00 -0500
issue: "2026-11-17"
story_id: "datasette-lite-runs-the-full-app-in-browser-via-service-workers-5ab3"
permalink: "/zh/2026/11/17/datasette-lite-runs-the-full-app-in-browser-via-service-workers-5ab3/"
title: "用 Service Worker 与 Pyodide 在浏览器运行 Datasette"
dek: "A clear, first-hand explanation of rewriting Datasette Lite to run the full server-side Python app in the browser via…"
description: "A clear, first-hand explanation of rewriting Datasette Lite to run the full server-side Python app in the browser via…"
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

## 背景

Datasette Lite 是作者将服务端 Datasette 移植到浏览器、借 WebAssembly 和 Pyodide 运行的项目。2022 年初版用 innerHTML 注入 Web Worker 生成的 HTML，脚本不会执行、额外 JS/CSS 也加载不了，依赖 JavaScript 的功能因而失效。

## 方案

重写版在 lite.datasette.io 全域名注册 Service Worker，父页面创建 iframe，把页面和静态资源请求改写到 /app/<会话ID>/...，再由 Service Worker 路由到该标签页专用的 Pyodide Web Worker。会话前缀用于隔离共享同一 Service Worker 的多个标签页，避免插件和配置互相污染；仍需 Web Worker，是因为 Pyodide 放在 Service Worker 中约 30 秒后无法保持状态（依浏览器而异）。URL 参数可安装插件、载入数据库和元数据、选 Datasette 发布版或 GitHub 引用，并可从 100 多个 SQLite 版本中选择——背后是 163 个 Wasm 版 pysqlite3 wheel，便于演示新特性和复现 bug，例如用 1.0a42 与 1.0a43 链接对比分页修复。外部数据库需开放 CORS；作者也承认非 SQLite 数据库仍属少走的路，且系统“活动部件很多”。

## 启示

作者的核心论点是：这套架构并非 Datasette 专属，几乎任何 Python 应用都可借 Service Worker 与 Pyodide 搭建廉价的浏览器预览、功能演示和 bug 复现环境；C/Rust 扩展已可编译为 Wasm，并自 2026 年 4 月 PEP 783 起可发布到 PyPI，但非 SQLite 数据库仍是限制。

{% endraw %}
