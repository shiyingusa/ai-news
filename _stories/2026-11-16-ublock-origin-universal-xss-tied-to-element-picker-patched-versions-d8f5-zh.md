---
layout: story
lang: zh
date: 2026-11-16 06:00:00 -0500
issue: "2026-11-16"
story_id: "ublock-origin-universal-xss-tied-to-element-picker-patched-versions-d8f5"
permalink: "/zh/2026/11/16/ublock-origin-universal-xss-tied-to-element-picker-patched-versions-d8f5/"
title: "uBlock Origin 被曝元素选择器通用 XSS 漏洞"
dek: "一篇安全分析报告称，uBlock Origin 存在通用 XSS（universal XSS，即攻击者可借一个网站影响其他站点的脚本执行）漏洞，问题出在其由网页内容驱动的元素选择器（element picker）上。"
description: "一篇安全分析报告称，uBlock Origin 存在通用 XSS（universal XSS，即攻击者可借一个网站影响其他站点的脚本执行）漏洞，问题出在其由网页内容驱动的元素选择器（element picker）上。"
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
photo_credit: {"url": "https://pixabay.com/get/g294ac28901c67a9d5c056981a02988743965cd6ac3b214d8b99c57e345d82902dad888aa8c16c39f9a5a28e3d13053cc9440c6b41063cf3f79c1f27712989074_1280.jpg", "author": "geralt", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/registration-log-in-keyboard-hand-3938434/", "provider": "Pixabay", "width": 4896, "height": 3264}
---

{% raw %}
<div class="story-lead" markdown="1">

一篇安全分析报告称，uBlock Origin 存在通用 XSS（universal XSS，即攻击者可借一个网站影响其他站点的脚本执行）漏洞，问题出在其由网页内容驱动的元素选择器（element picker）上。评论区读者指出，仍在使用旧版的用户应升级到 uBlock Origin 1.75.4 或 uBO Lite 2026.1110.1816 及以上版本，但这些版本号来自社区评论，所给材料中没有官方公告加以确认。讨论还涉及扩展程序把界面注入网页 DOM 所带来的隐私风险，以及安装广告拦截器后可能反而成为网站识别用户的一种指纹信号。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** 这篇安全文章报告 uBlock Origin 的网站驱动元素选择器存在通用 XSS；项目安全公告 GHSA-cmqw-9r2w-6wv2 将其评为 High，并称 Firefox 与 Chromium MV2 版本受影响，uBO Lite 另有一个较轻问题。
- **尚未证实：** 具体修复版本 uBlock Origin 1.75.4 和 uBO Lite 2026.1110.1816 仅来自评论者；完整受影响版本范围、独立复现测试及利用细节尚未由文章或公告在现有材料中确认。

</div>

## 背景：元素选择器

uBlock Origin 的元素选择器通常由用户右键点击页面元素调出，用来把选中的元素转成一条过滤规则。此次问题在于选择器还能被网页通过特定网址驱动，从而把网站指定的规则送进选择器；项目发布说明把“校验即将在元素选择器中创建的过滤规则”列为修复项。

## 为什么重要

受影响的是 Firefox 上的 MV2 版 uBlock Origin：攻击要成立，需要网页把元素选择器嵌入 iframe，并且当前过滤器列表中存在带 prevent-xhr 或 prevent-fetch 的脚本片段（scriptlet），然后诱导用户在自己页面上点击一下，扩展就会把攻击者指定的过滤器当作“可信”规则加入——这意味着恶意站点能在用户浏览的页面里执行任意代码，而不只是屏蔽失效。厂商在 GitHub 安全公告中确认了该问题并已修复，所以实际处置动作很明确：Firefox MV2 用户应把 uBlock Origin 升级到已修复版本；社区评论提到 uBlock Origin 1.75.4、uBO Lite 2026.1110.1816 为安全下限，但这一版本号来自用户留言而非公告，升级前最好以扩展商店显示的最新版本为准。MV3 的 uBO Lite 也受类似问题影响，按作者说法后果较轻。

## 后续看点

关注 uBlock Origin 维护者是否发布正式安全公告，明确受影响版本范围，并确认修复已进入各扩展商店的稳定版本。

## 社区讨论

有评论者质疑，扩展程序为实现元素选择、密码管理器建议等功能而把界面放进网页 DOM，可能把用户拥有哪些账户等信息暴露给网站；也有人担心安装广告拦截器后暴露的 UUID 会成为稳定的追踪标识。另有读者提出，把创建规则的界面放在浏览器界面层而不是网页 DOM 中，或许能从结构上避免这类问题。

## 延伸阅读

- [Universal XSS in uBlock Origin from website-driven element picker](https://iter.ca/post/ubo-uxss/)
- [Releases · gorhill/ uBlock · GitHub](https://github.com/gorhill/uBlock/releases)
- [uBlock Origin Lite - Microsoft Edge Add-ons GitHub - uBlockOrigin/uBOL-home: uBO Lite home (MV3) uBlock Origin Lite: Install, Filtering Modes & Limitations ... Releases · uBlockOrigin/uBOL-home · GitHub uBlock Origin patches a universal XSS bug in its element ... Releases · gorhill/uBlock · GitHub GitHub - gorhill/uBlock: uBlock Origin - An efficient blocker ...](https://microsoftedge.microsoft.com/addons/detail/ublock-origin-lite/cimighlppcgcoapaliogpjjdehbnofhn)
- [Universal XSS from website-driven element picker](https://github.com/gorhill/uBlock/security/advisories/GHSA-cmqw-9r2w-6wv2)
- [Universal XSS in uBlock Origin from website-driven element picker](https://iter.ca/post/ubo-uxss/)
- [Universal XSS in uBlock Origin from website-driven element picker](https://techbytes.app/posts/universal-xss-in-ublock-origin-from-website-driven-element-picker/)

{% endraw %}
