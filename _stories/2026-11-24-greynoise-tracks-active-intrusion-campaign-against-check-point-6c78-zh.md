---
layout: story
lang: zh
date: 2026-11-24 18:24:23 -0500
issue: "2026-11-24"
story_id: "greynoise-tracks-active-intrusion-campaign-against-check-point-6c78"
permalink: "/zh/2026/11/24/greynoise-tracks-active-intrusion-campaign-against-check-point-6c78/"
title: "GreyNoise 称 Check Point 安全管理服务器正遭活跃入侵"
dek: "GreyNoise 发布博客称，一场针对 Check Point 安全管理服务器（Security Management Server，企业用来集中下发策略、查看日志的管理组件）的入侵活动正在进行，这一说法在安全社区引发较多讨论。"
description: "GreyNoise 发布博客称，一场针对 Check Point 安全管理服务器（Security Management Server，企业用来集中下发策略、查看日志的管理组件）的入侵活动正在进行，这一说法在安全社区引发较多讨论。"
section: "tech-industry"
rank: 214
edition: 2
section_rank: 2
score: 8.0
status: "Demonstrated"
source_name: "greynoise.io"
source_url: "https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50630594"
published_at: "2026-11-24T16:32:17+00:00"
tags: ["cybersecurity", "Check Point", "intrusion campaign", "threat intelligence", "vulnerability exploitation"]
topics: ["cybersecurity", "check-point", "intrusion-campaign", "threat-intelligence", "vulnerability-exploitation"]
order: "20261124-2-985"
image: "/assets/stories/2026-11-24/greynoise-tracks-active-intrusion-campaign-against-check-point-6c78-share.jpg"
art: "/assets/stories/2026-11-24/greynoise-tracks-active-intrusion-campaign-against-check-point-6c78.jpg"
thumb: "/assets/stories/2026-11-24/greynoise-tracks-active-intrusion-campaign-against-check-point-6c78-640.jpg"
photo_credit: {"url": "https://upload.wikimedia.org/wikipedia/commons/c/c4/Check_point_hq.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail_unscaled", "author": "דוד שי", "licence": "CC BY-SA 3.0", "licence_url": "https://creativecommons.org/licenses/by-sa/3.0", "source_url": "https://commons.wikimedia.org/wiki/File:Check_point_hq.jpg", "provider": "Wikimedia Commons", "width": 1919, "height": 1454}
---

{% raw %}
<div class="story-lead" markdown="1">

GreyNoise 发布博客称，一场针对 Check Point 安全管理服务器（Security Management Server，企业用来集中下发策略、查看日志的管理组件）的入侵活动正在进行，这一说法在安全社区引发较多讨论。现有可见信息中的技术细节很有限：讨论主要集中在攻击者如何取得初始访问权限上，有评论者推测入口是 CVE-2026-16232，并追问受影响的机构是否都把管理服务器直接暴露在互联网上。

可见报道没有给出受影响的版本、修复版本、受影响组织数量或攻击者归属。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** GreyNoise 报告称，2026 年 10 月 17 日至 11 月 2 日期间确认存在针对 Check Point 安全管理服务器（Security Management Server）的攻击活动，全球至少 22 家不同机构受影响；上述结论来自 GreyNoise 自行发布的博客，SecurityWeek 与 Cybersecurity Dive 均转述了这份报告。
- **尚未证实：** 攻击者的身份、所谓“AI 赋能/AI 辅助”的具体程度、初始入口是否为 CVE-2026-16232、以及攻击活动目前是否仍在持续，均只有 GreyNoise 一家之说；目前未见 Check Point 的确认或回应，也没有独立机构复现攻击，或公布受影响机构名单。

</div>

## 背景

这次攻击针对的是 Check Point 防火墙的管理平面。据安全厂商 Beazley 实验室的公告归档，Check Point 于 2026 年 7 月 22 日修复了 Security Management 平台上的三个漏洞（CVE-2026-16232、CVE-2026-62144、CVE-2026-62145），其中 CVE-2026-16232 是一个 CVSS 评分 9.3 的认证绕过漏洞，影响 SmartConsole 安全管理与多域管理架构；公告称该漏洞在修复时已被用于在野攻击，可夺取防火墙管理服务器的完全管理员权限。在讨论中，有读者指出目前尚不清楚攻击者的初始入口，但多家 Check Point 客户同时受影响，可能正说明这些机构的 Security Management Server 暴露在互联网上。

## 为什么重要

对运行 Check Point 安全管理服务器的企业来说，最直接的行动点是核查管理界面能否从公网访问，并排查是否存在异常的管理员会话。评论者正是从多家 Check Point 客户同时受影响这一现象，推断出管理面暴露于互联网的问题，但这一推断目前只是社区推测，未经厂商确认。

## 后续看点

关注 Check Point 是否就此事发布安全公告，明确受影响的版本范围与需要升级到的修复版本。

## 延伸阅读

- [Critical Check Point Security Management Vulnerabilities Under...](https://labs.beazley.security/advisories/BSL-A1195)
- [Check Point CVE - 2026 - 16232 Under Active... | The CyberSec Guru](https://thecybersecguru.com/news/check-point-cve-2026-16232-authentication-bypass-active-exploitation/)
- [Check Point SmartConsole CVE - 2026 - 16232 Authentication... | LinkedIn](https://www.linkedin.com/posts/codedefence_codedefence-checkpoint-smartconsole-activity-7487197195956375552-1pp7)
- [An Active Intrusion Campaign Against Check Point Security ...](https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign)
- [AI-enabled campaign targets Check Point Security Management ...](https://www.cybersecuritydive.com/news/ai-enabled-campaign-targets-check-point-security-management-servers/875622/)
- [Check Point Security Management Servers Hacked - SecurityWeek](https://www.securityweek.com/check-point-security-management-servers-hacked-in-ai-assisted-campaign/)

<div class="community" markdown="1">

## 社区讨论（观点，不是证据）

有评论者指出，报告并未说清攻击者的初始访问方式，并推测 CVE-2026-16232 可能是入口，同时质疑这些机构是否都让管理服务器可从公网访问。另有评论引用了另一则关于 HFS 服务器会话 cookie 的分析，其中攻击者通过连续登录采集 JavaScript Math.random() 的输出、重建 V8 引擎伪随机数生成器的内部状态，从而伪造管理员会话；该评论者据此主张应从根本上修复不安全的随机数生成器，而不是逐个修补误用它的应用。

</div>

{% endraw %}
