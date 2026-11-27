---
layout: story
lang: zh
date: 2026-11-18 06:00:00 -0500
issue: "2026-11-18"
story_id: "quad9-withdraws-from-france-over-dns-blocking-pressure-797d"
permalink: "/zh/2026/11/18/quad9-withdraws-from-france-over-dns-blocking-pressure-797d/"
title: "Quad9 退出法国：DNS 强制屏蔽的早期警示"
dek: "Cloudflare 博客称，公共 DNS 解析器 Quad9 因法国的 DNS 屏蔽要求退出法国，并将此视为强制过滤对互联网基础设施的早期警示。"
description: "Cloudflare 博客称，公共 DNS 解析器 Quad9 因法国的 DNS 屏蔽要求退出法国，并将此视为强制过滤对互联网基础设施的早期警示。"
section: "tech-industry"
rank: 13
edition: 0
section_rank: 2
score: 7.0
status: null
source_name: "blog.cloudflare.com"
source_url: "https://blog.cloudflare.com/quad9-withdrawal-from-france/"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50538994"
published_at: "2026-11-17T22:13:34+00:00"
tags: ["DNS", "internet governance", "content blocking", "France", "privacy"]
topics: ["dns", "internet-governance", "content-blocking", "france", "privacy"]
order: "20261118-0-986"
image: "/assets/stories/2026-11-18/quad9-withdraws-from-france-over-dns-blocking-pressure-797d-share.jpg"
art: "/assets/stories/2026-11-18/quad9-withdraws-from-france-over-dns-blocking-pressure-797d.jpg"
thumb: "/assets/stories/2026-11-18/quad9-withdraws-from-france-over-dns-blocking-pressure-797d-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/gd743113e800d6f683207d953960447b573766eb227bede6bfa4ffd51c492110c18113d6acaa206cf9d069c343b2057fbd3d1f3da6aed0fa371700d16fcf9d19d_1280.jpg", "author": "Akela999", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/electrical-data-center-2476783/", "provider": "Pixabay", "width": 4096, "height": 2160}
---

{% raw %}
<div class="story-lead" markdown="1">

Cloudflare 博客称，公共 DNS 解析器 Quad9 因法国的 DNS 屏蔽要求退出法国，并将此视为强制过滤对互联网基础设施的早期警示。DNS 解析器负责把域名转换为 IP 地址，Quad9 的退出意味着法国用户少了一个可选的公共解析服务，也显示合规压力可能直接改变 DNS 服务的可用范围。

现有材料未给出相关裁决、退出时间表或替代安排；Quad9 首席技术官在 Hacker News 评论中称，其立场在 IETF 127 获得广泛支持，并对 DNS 治理走向表示担忧。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** Quad9 于 10 月 22 日宣布，因巴黎法院 5 月 13 日就 beIN Sports 提起的盗版站点屏蔽案作出裁决、要求其采取屏蔽措施，将于 11 月 24 日停止为法国用户提供服务；Quad9 称法院已将罚款从 58 万欧元降至每日 1000 欧元。TorrentFreak 报道称，Quad9 是第二家退出法国的 DNS 解析器。
- **尚未证实：** 上诉能否推翻该裁决、Quad9 是否会在 11 月 24 日前改变计划，以及退出对法国用户解析成功率的具体影响，均无独立测量或后续确认。

</div>

## 背景

公共 DNS 解析器（如 Quad9）负责把域名翻译成 IP 地址，是几乎所有上网请求的第一跳。一旦监管机构要求解析器在解析环节屏蔽特定域名，内容管控就从网站端下移到基础设施层：使用该解析器的所有用户都无法访问被列出的站点，而解析器运营方必须自行判断这份名单是否合法、是否过度，并承担误拦的代价。这正是 DNS 中立性长期争议的核心——解析器究竟应像公路一样原样转发，还是应承担过滤责任。

## 为什么重要

对法国的 Quad9 用户来说，最直接的后果是失去这层恶意软件与钓鱼域名拦截，得另换一个公共解析器；对其他公共解析器（如 Cloudflare、Google）而言，beIN Sports 在巴黎法庭寻求的每日最高 58 万欧元罚款则是一个可复制的先例：要么按要求对递归解析器执行屏蔽，要么退出该市场。ICANN 安全与稳定咨询委员会（SSAC）2025 年的报告指出，通过递归解析器做 DNS 屏蔽只在用户确实使用该解析器时有效，换个解析器即可绕过，因此把合规成本压在少数几家公共解析器身上，实际屏蔽效果很大程度上取决于这些服务商的市场集中度。

## 延伸阅读

- [Quad9 plans France withdrawal over beIN site-blocking orders](https://disputeindex.com/cases/quad9-france-bein-dns-blocking-withdrawal)
- [DNS Resolver Quad9 Will Leave France After Court Orders ...](https://torrentfreak.com/dns-resolver-quad9-will-leave-france-after-court-orders-piracy-blocking-penalty/)
- [Farewell, France | Quad9](https://quad9.net/news/blog/au-revoir-france/)
- [DNS Resolver Quad 9 Rejects French Piracy Blocks ... * TorrentFreak](https://torrentfreak.com/dns-resolver-quad9-rejects-french-piracy-blocks-weighs-exit-as-bein-seeks-up-to-e580k-a-day/)
- [sac127_ dns _ blocking _revisited](https://itp.cdn.icann.org/en/files/security-and-stability-advisory-committee-ssac-reports/sac127-dns-blocking-revisited-16-05-2025-en.pdf)

<div class="community" markdown="1">

## 社区讨论（观点，不是证据）

Quad9 首席技术官在评论中称，IETF 127 上同行几乎一致支持 Quad9 的立场，并对 DNS 领域的走向感到担忧；他把反对声音主要归于“版权产业”的雇员。另一名评论者认为，要求互联网基础设施像道路一样保持“中立”的假设已经过时，因为互联网已承载所有人；还有人批评 Cloudflare 只表达反对，却没有承诺在类似不利裁决下采取具体行动。

</div>

{% endraw %}
