---
layout: story
lang: zh
date: 2026-11-18 12:26:45 -0500
issue: "2026-11-18"
story_id: "wiz-reports-pre-auth-rce-in-nginx-http-2-handling-ff0c"
permalink: "/zh/2026/11/18/wiz-reports-pre-auth-rce-in-nginx-http-2-handling-ff0c/"
title: "Wiz 披露 nginx HTTP/2 处理中的免认证远程代码执行漏洞"
dek: "安全公司 Wiz 在一篇研究博客中描述了 nginx HTTP/2 处理环节中的免认证远程代码执行（pre-auth RCE，即攻击者无需登录凭据即可在目标服务器上执行代码）漏洞。"
description: "安全公司 Wiz 在一篇研究博客中描述了 nginx HTTP/2 处理环节中的免认证远程代码执行（pre-auth RCE，即攻击者无需登录凭据即可在目标服务器上执行代码）漏洞。"
section: "tech-industry"
rank: 120
edition: 1
section_rank: 1
score: 8.0
status: "Demonstrated"
source_name: "wiz.io"
source_url: "https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50547374"
published_at: "2026-11-18T15:19:55+00:00"
tags: ["nginx", "http/2", "remote code execution", "vulnerability disclosure", "security"]
topics: ["nginx", "http-2", "remote-code-execution", "vulnerability-disclosure", "security"]
order: "20261118-1-979"
image: "/assets/stories/2026-11-18/wiz-reports-pre-auth-rce-in-nginx-http-2-handling-ff0c-share.jpg"
art: "/assets/stories/2026-11-18/wiz-reports-pre-auth-rce-in-nginx-http-2-handling-ff0c.jpg"
thumb: "/assets/stories/2026-11-18/wiz-reports-pre-auth-rce-in-nginx-http-2-handling-ff0c-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g49aeda4f6dcfa7f3853bb91f3073980ac3584c0b51112bd4c8165808f3013d59241e1ffcb4ea9ef158073d9393caee9b_1280.jpg", "author": "kewl", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/server-room-datacenter-network-90389/", "provider": "Pixabay", "width": 4818, "height": 3212}
---

{% raw %}
<div class="story-lead" markdown="1">

安全公司 Wiz 在一篇研究博客中描述了 nginx HTTP/2 处理环节中的免认证远程代码执行（pre-auth RCE，即攻击者无需登录凭据即可在目标服务器上执行代码）漏洞。据 Forbes 报道，获 DARPA 支持的网络安全公司 Xint 称其借助 GPT 6.1 Sol 与 GPT-6 Luna 发现了 nginx 中的 RCE 漏洞，Wiz 则表示自己也独立发现了同一批缺陷。

该研究目前只是厂商研究博客，并非 F5/nginx 的官方安全公告，也没有证据显示漏洞已被在野利用。Hacker News 上的讨论指出，相关修复已在一周前提交进开源代码库，并在提交信息中注明由 Xint.io 报告。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** Wiz 研究称 nginx 的 HTTP/2 处理存在预认证（pre-auth）远程代码执行漏洞；Forbes 报道 Xint 称其用 GPT 6.1 Sol 和 GPT-6 Luna 独立发现了同一批漏洞，Wiz 表示双方是分别发现。
- **尚未证实：** 漏洞是否已被在野利用、Xint 的 AI 发现说法能否独立复现；两个漏洞的 CVSS 4.0 评分均为 9.2（仅见 Cybersecurity News 报道）、修复版本为 nginx 1.31.9（仅见 FourWeekMBA 报道），以及披露时间线（有评论称修复提交早一周）均未获 nginx 官方确认。

</div>

## 背景

HTTP/2 是 nginx 支持的可选协议层；Wiz 的公告称，CVE-2026-123007 的影响范围可追溯至 2015 年发布的 nginx 1.9.5，且这两个漏洞都要求受影响的服务器启用 HTTP/2 才能触发。Xint 的缓解说明称，在补丁就绪前，在受影响的监听端口关闭 HTTP/2 可以阻断这两个 CVE，但该公司发现的其他三个 nginx 漏洞不受这一措施覆盖。

## 为什么重要

nginx 是部署最广泛的 Web 服务器与反向代理之一，运行受影响版本的运维人员需要立刻核对自身版本，并在无法升级时关闭 HTTP/2 作为临时缓解——评论区多位读者指出，这一临时措施的成本很低，因此披露方与厂商本可以更早发出提醒。

## 后续看点

关注 F5/nginx 是否就这批漏洞发布官方安全公告、分配 CVE 编号，以及修复何时进入稳定发行版与官方镜像。

## 本事件的相关报道

- 2026-11-18 · wiz.io: [Pre-auth RCE in Nginx HTTP/2 handling](https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities)
- 2026-11-18 · Forbes: [Cybersecurity company Xint says it found RCE vulnerabilities in Nginx using GPT 6.1 Sol and GPT-6 Luna; Wiz says it had separately found the same flaws (Thomas Brewster/Forbes)](https://www.forbes.com/sites/thomasbrewster/2026/11/18/ai-finds-major-web-security-flaws/)

## 延伸阅读

- [Unauthenticated Remote Code Execution in NGINX ... | Wiz Blog](https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities)
- [NGINX 2 Root: New Remote Code Execution Vulnerabilities in nginx ...](https://xint.io/blog/nginx2root-remote-code-execution)
- [NGINX 2 Root by Xint — From nginx visitor to root of the server host](https://nginx2root.com/)
- [NGINX HTTP/2 Flaws Could Allow Memory Corruption and Remote ...](https://cybersecuritynews.com/nginx-http-2-vulnerabilities/)
- [nginx Advisories Jump to 26 From 2 as AI Finds Critical RCEs](https://fourweekmba.com/ai-nginx-advisories-jump-to-26-from-2-as-ai-finds-critical-rces/)

<div class="community" markdown="1">

## 社区讨论（观点，不是证据）

Hacker News 上最集中的质疑是披露时序：一位评论者称漏洞一周前就已在开源仓库修复，提交信息甚至写明“Reported by Xint.io”，认为熟悉该团队的攻击者本可利用这段空窗期，而既然关闭 HTTP/2 就能缓解，相关方至少应发布临时关闭建议。也有读者表达了对 AI 大规模挖洞后小型站点无力清理的担忧，另有人反映官方 alpine 镜像的 sha-256 摘要有异常。这些均为个人观点与经验，不构成对漏洞影响范围的证实。

</div>

{% endraw %}
