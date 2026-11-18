---
layout: story
lang: zh
date: 2026-11-18 18:28:24 -0500
issue: "2026-11-18"
story_id: "xint-says-gpt-models-found-nginx-rce-flaws-wiz-found-same-bugs-6821"
permalink: "/zh/2026/11/18/xint-says-gpt-models-found-nginx-rce-flaws-wiz-found-same-bugs-6821/"
title: "Xint称其AI发现Nginx远程代码执行漏洞，Wiz称独立发现相同漏洞"
dek: "受DARPA（美国国防高级研究计划局）资助的网络安全公司Xint向《福布斯》表示，其AI系统借助GPT 6.1 Sol和GPT-6 Luna两个模型，在广泛使用的Web服务器Nginx中发现了远程代码执行漏洞（RCE…"
description: "受DARPA（美国国防高级研究计划局）资助的网络安全公司Xint向《福布斯》表示，其AI系统借助GPT 6.1 Sol和GPT-6 Luna两个模型，在广泛使用的Web服务器Nginx中发现了远程代码执行漏洞（RCE…"
section: "ai-news"
rank: 209
edition: 2
section_rank: 9
score: 7.0
status: "Announced"
source_name: "Forbes"
source_url: "https://www.forbes.com/sites/thomasbrewster/2026/11/18/ai-finds-major-web-security-flaws/"
via: "Techmeme"
discussion_url: null
published_at: "2026-11-18T16:25:01+00:00"
tags: ["AI security", "vulnerability discovery", "Nginx", "cybersecurity", "GPT models"]
topics: ["ai-security", "vulnerability-discovery", "nginx", "cybersecurity", "gpt-models"]
order: "20261118-2-990"
image: "/assets/stories/2026-11-18/xint-says-gpt-models-found-nginx-rce-flaws-wiz-found-same-bugs-6821-share.jpg"
art: "/assets/stories/2026-11-18/xint-says-gpt-models-found-nginx-rce-flaws-wiz-found-same-bugs-6821.jpg"
thumb: "/assets/stories/2026-11-18/xint-says-gpt-models-found-nginx-rce-flaws-wiz-found-same-bugs-6821-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/gc7b5dcc9c6d79872eab79e6dcd3c3aa5e2288fec477994fb63d59cfe4d35aa3f8a2e511f63d3908a1750ed925e6534588a40b8aae917867ec1b7768daaf3481f_1280.jpg", "author": "blickpixel", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/it-server-server-cabinet-network-838384/", "provider": "Pixabay", "width": 2682, "height": 1788}
---

{% raw %}
<div class="story-lead" markdown="1">

受DARPA（美国国防高级研究计划局）资助的网络安全公司Xint向《福布斯》表示，其AI系统借助GPT 6.1 Sol和GPT-6 Luna两个模型，在广泛使用的Web服务器Nginx中发现了远程代码执行漏洞（RCE，指攻击者可远程在服务器上运行任意代码），并称该AI还在找出其他类型的缺陷。另一家安全公司Wiz称，它独立发现了同一批Nginx漏洞。报道未给出CVE编号、受影响版本、触发条件或修复方案，两家公司的说法均来自其自身，尚无第三方复核。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** 据Forbes报道，Xint称其用GPT 6.1 Sol和GPT-6 Luna发现Nginx远程代码执行漏洞，Wiz表示自己独立发现了相同漏洞。Wiz博客列出CVE-2026-123633和CVE-2026-123007，称两者均为Critical、CVSS 4.0评分9.2，缺陷位于NGINX本身。
- **尚未证实：** 这些漏洞是否确由Xint的AI独立发现、两家公司谁先发现，目前只有公司说法；受影响版本与补丁状态也未明确。来源对范围与评分说法冲突：Wiz给两个CVE评9.2分，GetAstra称“nginx 2root”含五个Nginx RCE及一个Linux内核SCTP漏洞、CVSS尚未公布，nginx2shell还提到CVE-2026-123634等另外三个漏洞。

</div>

## 背景

Nginx 是广泛使用的开源 Web 服务器和反向代理，通常直接面向公网承接请求；RCE（远程代码执行）指攻击者能让服务器运行自己的代码，属于危害最高的一类漏洞。AI Daily Radar 11 月 17 日的日报曾报道，OpenAI 称正与北约及盟国网络机构合作，用 AI 帮助防御方发现漏洞、验证补丁，但当时未点名任何机构，也未说明已部署或可用；此次则是一家受 DARPA 资助的初创公司拿出了具体的漏洞发现案例。对这类“AI 找到漏洞”的说法，业界通常的验证方式是看漏洞能否被独立复现或由第三方确认。

## 为什么重要

对运行Nginx的运维团队来说，现有报道还不足以支撑任何具体处置：没有CVE编号、受影响版本和补丁信息，能做的只是等待官方安全公告。对AI漏洞发现工具而言，如果Wiz的独立发现被确认，这将是一个可核查的样本：AI找到的缺陷不再是单一厂商的自述，而能被外部研究者复现。

## 后续看点

可核查的下一步，是Nginx官方安全公告或对应CVE编号是否出现，以及公告是否说明受影响版本范围与补丁发布时间。

## 延伸阅读

- [2026-11-17 — OpenAI works with NATO, allied cyber agencies on AI vulnerability discovery](https://openai.com/index/strengthening-nato-allied-cyber-defences-ai)
- [Unauthenticated Remote Code Execution in NGINX ... | Wiz Blog](https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities)
- [nginx 2root: Five nginx RCE Flaws and a Kernel Bug...](https://www.getastra.com/blog/security-advisory/nginx2root/)
- [Remote code execution in NGINX HTTP/2 ( CVE - 2026 -123633...)](https://nginx2shell.com/)

{% endraw %}
