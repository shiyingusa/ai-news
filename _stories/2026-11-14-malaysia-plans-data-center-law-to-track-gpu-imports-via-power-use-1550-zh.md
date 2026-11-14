---
date: 2026-11-14 06:00:00 -0500
layout: "story"
lang: "zh"
issue: "2026-11-14"
story_id: "malaysia-plans-data-center-law-to-track-gpu-imports-via-power-use-1550"
permalink: "/zh/2026/11/14/malaysia-plans-data-center-law-to-track-gpu-imports-via-power-use-1550/"
title: "马来西亚拟以用电数据追查 GPU 走私"
dek: "马来西亚计划立法，要求数据中心运营商披露 GPU…"
section: "chips-compute"
rank: 6
section_rank: 2
score: 7.0
source_name: "Tom's Hardware"
source_url: "https://www.tomshardware.com/tech-industry/artificial-intelligence/malaysia-plans-new-law-using-data-center-power-consumption-to-catch-ai-gpu-smugglers-but-real-world-tdp-variance-and-lack-of-physical-audits-could-undermine-it-new-law-also-forces-operators-to-pay-for-unused-electricity-capacity"
discussion_url: null
published_at: null
tags: ["export controls", "AI GPUs", "data centers", "Malaysia", "power consumption"]
topics: ["export-controls", "ai-gpus", "data-centers", "malaysia", "power-consumption"]
order: "20261114-993"
image: "/assets/stories/2026-11-14/malaysia-plans-data-center-law-to-track-gpu-imports-via-power-use-1550-share.jpg"
art: "/assets/stories/2026-11-14/malaysia-plans-data-center-law-to-track-gpu-imports-via-power-use-1550.jpg"
thumb: "/assets/stories/2026-11-14/malaysia-plans-data-center-law-to-track-gpu-imports-via-power-use-1550-640.jpg"
---

{% raw %}
<div class="story-lead" markdown="1">

马来西亚计划立法，要求数据中心运营商披露 GPU 进口数量、用电量（推测为铭牌功耗）、设施实际位置以及运营商和超大规模客户身份，并拟对预留但未使用的电力容量收费；这仍是拟议措施，马来西亚数字部正在审查现行法律能否处理受美国出口限制处理器的转出口。政府希望确保进口的 AI 加速器留在本国使用，并称已批准 117 个数据中心项目、其中 55 个已运营。文章指出，仅凭功耗很难准确推算 GPU 数量：英伟达 H100 和 H200 SXM 标称 700W、B200 SXM 标称 1000W，实际负载功耗并不等于标称值，还需知道服务器配置、CPU/内存/存储/网络功耗及设施电能使用效率（PUE）。若没有现场库存审计或逐个处理器追踪，这类核查仍可能不可靠；部长未说明新法是否要求披露 GPU 型号和序列号，也未说明是否进行现场检查。

</div>

## 背景

美国出口管制禁止向中国出售 Nvidia H100/H200、B200 等高端 AI 加速器，使经第三国转运成为规避管制的主要路径。据搜索结果，马来西亚先是在 2025 年对源自美国的先进 AI 芯片实施出口管制，随后于 2026 年 6 月在吉隆坡查获一起价值近 1300 万美元的 AI 服务器走私未遂案；这些先例正是本次拟议立法要求数据中心披露 GPU 进口数量与用电量的直接背景。

## 影响

对在马来西亚运营或规划数据中心的企业，最直接的成本变化是电力预留不再按实际用电付费：文章举例说，预留 100MW 却只使用 50MW，仍要为剩余 50MW 付费，这会抬高分期建设项目的早期成本，并减少企业提前锁定过多电力容量。与此同时，运营商需持续披露进口和用电数据，而不是只在项目审批阶段说明；但若缺乏型号、序列号和现场核查要求，合规负担增加未必能带来相应的执法确定性。

## 延伸阅读

- [Malaysian Customs Seize $12.1 Million in Smuggled AI Chips at](https://factlen.com/news/malaysian-customs-seize-12-1-million-in-smuggled-ai-chips-at-kuala-lumpur-airpor-38681-96d95b54)

{% endraw %}
