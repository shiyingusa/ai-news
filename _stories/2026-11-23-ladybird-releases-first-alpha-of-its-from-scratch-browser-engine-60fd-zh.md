---
layout: story
lang: zh
date: 2026-11-23 19:32:00 -0500
issue: "2026-11-23"
story_id: "ladybird-releases-first-alpha-of-its-from-scratch-browser-engine-60fd"
permalink: "/zh/2026/11/23/ladybird-releases-first-alpha-of-its-from-scratch-browser-engine-60fd/"
title: "Ladybird 发布首个 alpha，macOS 与 Linux 可直接安装"
dek: "11 月 23 日，Ladybird 发布首个 alpha 版，macOS 和 Linux 用户可以直接下载安装，不必再自行编译。"
description: "11 月 23 日，Ladybird 发布首个 alpha 版，macOS 和 Linux 用户可以直接下载安装，不必再自行编译。"
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

11 月 23 日，Ladybird 发布首个 alpha 版，macOS 和 Linux 用户可以直接下载安装，不必再自行编译。这个从零实现的浏览器覆盖 HTML 解析、CSS、布局、JavaScript 和 WebAssembly，只借用 HarfBuzz、Skia、ffmpeg、SQLite 等外部组件，并以独立进程运行不同标签页。

项目在 10 月进展说明中称，借助 AI 编程代理新增 75,650 项 Web Platform Tests 通过，换上新的 JavaScript JIT 和基于 Cranelift 的 WebAssembly 引擎，后者在 JetStream 3 的 WASM 基准上快 7 倍；但官方明确说 alpha 仍会崩溃、部分网站打不开，且暂不承诺安全性。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** Ladybird 项目于 11 月 23 日发布了首个 alpha 版，macOS 和 Linux 用户无需自行编译即可安装，项目官方声明中承认部分网站无法使用、会崩溃，并且“今天对安全性不做任何承诺”。Ladybird 自己的 10 月通讯称，当月网页平台测试（WPT，约 225 万项子测试）通过数增加 75,650 项，并在 10 月 26 日超过 Safari Technology Preview；维基百科条目确认该项目以 BSD 2-Clause 许可开源，并于 2026 年 2 月开始把 JavaScript 解析器从 C++ 移植到 Rust。
- **尚未证实：** JetStream 3 的 WebAssembly 基准提升 7 倍、布局与 JIT 改进的实际体验收益，均为项目方自述，尚无独立复测；哪些具体模型被用于批量修复 WPT，官方未披露。早期用户“网站几乎全部正常渲染”属个人测试反馈，Datasette Lite 因 service worker 相关接口缺失而报错，说明兼容性仍有缺口。alpha 版的日常使用稳定性与安全性均未经验证。

</div>

## 背景

浏览器引擎是负责解析 HTML、计算 CSS、执行 JavaScript 并渲染页面的核心组件，目前主流市场基本由 Chromium（Chrome、Edge）、Gecko（Firefox）和 WebKit（Safari）三家把持。Ladybird 最初是 Andreas Kling 的 SerenityOS 项目自带的浏览器，后来独立成项：除 HarfBuzz 文本排版、Skia 2D 图形、ffmpeg 视频解码和 SQLite 等少数外部库外，HTML 解析、CSS 引擎、布局、JavaScript 乃至 WebAssembly 都由项目自行实现，另有一部分代码沿用自 SerenityOS。项目在 2026 年 2 月借助 Claude Code 与 Codex，把部分 LibJS 引擎从 C++ 移植成约 2.5 万行 Rust，因此这次 alpha 面向的已是一个有相当积累的代码库。

## 为什么重要

想尝鲜的用户应把 Ladybird 当作第二浏览器：测试者建议不要用它登录 GitHub、Gmail 等敏感账户，遇到坏站或崩溃可直接从浏览器内报告。对浏览器开发者而言，这也提供了一个可实际测试的非 Chromium、非 Gecko 引擎，但它目前仅支持 macOS 和 Linux。

## 后续看点

后续可关注 Ladybird 对 Datasette Lite 暴露的 service worker 兼容问题的修复，以及项目在邀请安全研究者测试后如何处理提交的漏洞报告；官方尚未给出时间表。

## 本事件的相关报道

- 2026-11-23 · ladybird.org: [Ladybird is now in alpha](https://ladybird.org/posts/alpha/)
- 2026-11-23 · Simon Willison: [Ladybird's first alpha release](https://simonwillison.net/2026/Nov/23/ladybird/)

## 延伸阅读

- [Ladybird ( web browser) - Wikipedia](https://en.wikipedia.org/wiki/Ladybird_(web_browser))
- [This Month in Ladybird - October 2026 - Ladybird](https://ladybird.org/newsletter/2026-10-31/)

<div class="community" markdown="1">

## 社区讨论（观点，不是证据）

早期测试者的反馈以正面为主：freakynit 称试过的网站“每一个都正确渲染”，只是滚动略有卡顿；alentred 说 Proxmox 的 NoVNC 在 Ladybird 中甚至比 Firefox 更流畅。drnick1 则希望项目未来认真处理指纹识别，提供更细粒度权限和反指纹模式，这属于对后续功能的期望而非现有能力。

</div>

{% endraw %}
