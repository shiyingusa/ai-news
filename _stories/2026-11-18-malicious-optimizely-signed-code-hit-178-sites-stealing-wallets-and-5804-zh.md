---
layout: story
lang: zh
date: 2026-11-18 06:00:00 -0500
issue: "2026-11-18"
story_id: "malicious-optimizely-signed-code-hit-178-sites-stealing-wallets-and-5804"
permalink: "/zh/2026/11/18/malicious-optimizely-signed-code-hit-178-sites-stealing-wallets-and-5804/"
title: "Optimizely 签名脚本被篡改，178 家网站向访客投毒"
dek: "安全研究机构 ReportURI 称，网站个性化平台 Optimizely 下发的、带有有效数字签名的 JavaScript 被篡改，使 178 个使用该平台的网站——包括 CNN、Zoom、BBC 和 Salesforce…"
description: "安全研究机构 ReportURI 称，网站个性化平台 Optimizely 下发的、带有有效数字签名的 JavaScript 被篡改，使 178 个使用该平台的网站——包括 CNN、Zoom、BBC 和 Salesforce…"
section: "tech-industry"
rank: 12
edition: 0
section_rank: 1
score: 8.0
status: null
source_name: "Ars Technica"
source_url: "https://arstechnica.com/security/2026/11/malicious-code-delivered-through-optimizely-hits-visitors-to-hundreds-of-sites/"
via: null
discussion_url: null
published_at: "2026-11-17T22:32:16+00:00"
tags: ["cybersecurity", "supply chain attack", "malware", "Optimizely", "iOS exploits"]
topics: ["cybersecurity", "supply-chain-attack", "malware", "optimizely", "ios-exploits"]
order: "20261118-0-987"
image: "/assets/stories/2026-11-18/malicious-optimizely-signed-code-hit-178-sites-stealing-wallets-and-5804-share.jpg"
art: "/assets/stories/2026-11-18/malicious-optimizely-signed-code-hit-178-sites-stealing-wallets-and-5804.jpg"
thumb: "/assets/stories/2026-11-18/malicious-optimizely-signed-code-hit-178-sites-stealing-wallets-and-5804-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g2b7f8ce38c058b3b6d880bbeed954572e8cb23300ada1e18c81097f38de262722d8e4cfa02b1418418ca3f2bfe717a78ed5b2e23dd3dbbc58d2bf670a989a6cc_1280.jpg", "author": "MightyFineBros", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/data-center-technology-server-7388620/", "provider": "Pixabay", "width": 4800, "height": 2700}
---

{% raw %}
<div class="story-lead" markdown="1">

安全研究机构 ReportURI 称，网站个性化平台 Optimizely 下发的、带有有效数字签名的 JavaScript 被篡改，使 178 个使用该平台的网站——包括 CNN、Zoom、BBC 和 Salesforce——向访客投递多用途恶意代码。该脚本从 cdn.optimizely.com 加载，攻击者把恶意内容写进客户自定义代码所在的部分；它会替换加密货币钱包地址、窃取支付卡数据、Cookie 和截图，并针对 iPhone/iPad 投递名为 Coruna 和 DarkSword 的漏洞利用套件。

上述发现来自 ReportURI 的单方调查，报道正文的计数是 178 个，标题则称“数百个”。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** ReportURI 称，其在 Optimizely 签发、经 cdn.optimizely.com 以有效证书分发的 JavaScript 中发现了被篡改的代码，共影响 178 个网站，包括 CNN、Zoom、BBC 和 Salesforce；恶意组件会替换加密货币钱包地址、窃取支付卡数据、Cookie 和截图，并在 iPhone/iPad 上投递 Coruna、DarkSword 漏洞利用套件（Ars Technica 引述该报告，Cointelegraph 亦有报道）。
- **尚未证实：** 上述发现目前仅来自 ReportURI 一家安全公司，尚未看到 Optimizely 的说明或第三方独立复现；攻击者具体如何把代码写入客户脚本、是否有访客数据被实际窃取、受影响站点是否已全部清除恶意代码，均未有交代。Cointelegraph 称攻击发生在周一，而 Ars 称研究人员周二披露，两篇报道在时间表述上并不一致。

</div>

## 背景：第三方脚本如何放大风险

Optimizely 是网站个性化平台，客户会在页面中嵌入它提供的 JavaScript “片段”，这段代码可在每个页面运行，并常由 cdn.optimizely.com 统一下发。正因如此，篡改一处第三方脚本就能影响大量站点；而有效证书只证明代码来自该域名，并不等于内容未被注入恶意部分。

## 为什么重要

对把 Optimizely 脚本嵌入所有页面的站点而言，第三方脚本的信任边界就是直接风险：只要客户自定义代码段被写入恶意内容，经签名的 CDN 分发就会让浏览器把它当作可信代码执行，同一页面上的钱包地址、支付卡数据和 Cookie 都可能被窃取。

## 后续看点

后续可关注 Optimizely 是否发布正式调查结论，以及 ReportURI 的 178 个受影响站点名单是否更新。

## 延伸阅读

- [World's Largest Brands Infected With Malware Via Optimizely](https://report-uri.ghost.io/worlds-largest-brands-infected-with-malware-via-optimizely/)
- [Ledger, BBC Among 178 Organizations Hit by Crypto Malware](https://cointelegraph.com/news/hackers-inject-malware-into-178-major-websites)
- [Attackers Used Optimizely to A/B Test Malware on Top Websites ...](https://krebsonsecurity.com/2026/11/attackers-used-optimizely-to-a-b-test-malware-on-top-websites/)

{% endraw %}
