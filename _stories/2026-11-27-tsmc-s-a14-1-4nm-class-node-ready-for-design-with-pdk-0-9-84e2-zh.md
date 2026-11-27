---
layout: story
lang: zh
date: 2026-11-27 06:25:44 -0500
issue: "2026-11-27"
story_id: "tsmc-s-a14-1-4nm-class-node-ready-for-design-with-pdk-0-9-84e2"
permalink: "/zh/2026/11/27/tsmc-s-a14-1-4nm-class-node-ready-for-design-with-pdk-0-9-84e2/"
title: "台积电 A14 的 0.9 版 PDK 可供设计导入"
dek: "台积电在 2026 欧洲 OIP 生态研讨会上宣布，A14（1.4 纳米级）制程的 0.9 版 PDK 与设计生态已可供客户设计导入…"
description: "台积电在 2026 欧洲 OIP 生态研讨会上宣布，A14（1.4 纳米级）制程的 0.9 版 PDK 与设计生态已可供客户设计导入…"
section: "chips-compute"
rank: 2
edition: 0
section_rank: 1
score: 8.0
status: "Released"
source_name: "Tom's Hardware"
source_url: "https://www.tomshardware.com/tech-industry/semiconductors/tsmcs-a14-1-4nm-class-node-is-ready-for-chip-design-boost-cells-promise-14-percent-performance-uplift-or-23-percent-power-cut-over-n2p"
via: null
discussion_url: null
published_at: "2026-11-26T13:00:00+00:00"
tags: ["TSMC", "A14", "1.4nm-class", "semiconductor manufacturing", "EDA"]
topics: ["tsmc", "a14", "1-4nm-class", "semiconductor-manufacturing", "eda"]
order: "20261127-0-997"
image: "/assets/stories/2026-11-27/tsmc-s-a14-1-4nm-class-node-ready-for-design-with-pdk-0-9-84e2-share.jpg"
art: "/assets/stories/2026-11-27/tsmc-s-a14-1-4nm-class-node-ready-for-design-with-pdk-0-9-84e2.jpg"
thumb: "/assets/stories/2026-11-27/tsmc-s-a14-1-4nm-class-node-ready-for-design-with-pdk-0-9-84e2-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/gc71646eeda5859b26d4bfef7ef4102303c11284364d5ffb337f7b9a088fd347584d966ddc9e5d2f4f8539458138489b75402055a3f6da5ae94364fab5a65436b_1280.jpg", "author": "aleksaseverina", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/wafer-rolls-food-dessert-cooking-3390181/", "provider": "Pixabay", "width": 4957, "height": 3305}
---

{% raw %}
<div class="story-lead" markdown="1">

台积电在 2026 欧洲 OIP 生态研讨会上宣布，A14（1.4 纳米级）制程的 0.9 版 PDK 与设计生态已可供客户设计导入；Cadence 和 Synopsys 也已在 Arm Cortex-A725 核上完成全流程 EDA 认证。台积电称，借助 NanoFlex Pro 标准单元架构和用于关键路径的 Boost Cells，A14 在相同功耗下比 N2P 提升 14% 性能，或在相同速度下降低 23% 总功耗；相对基线 N2P，台积电还宣称能效提升 50%、逻辑密度提升 23%。

这些仍是厂商对比数据，尚无独立测量或量产芯片验证；A14 计划 2027 年下半年风险生产、2028 年下半年量产，A13 则计划 2029 年下半年进入高量产。西门子 EDA 未完成全部认证，其晶体管级 EM/IR 认证目标在 2026 年第四季度。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** Tom's Hardware 报道，TSMC 在 2026 欧洲 OIP 生态研讨会上宣布 A14 的 0.9 版 PDK 与设计生态可供设计导入，Cadence 与 Synopsys 已在 Arm Cortex-A725 上完成全流程认证，并给出 2027 年下半年风险生产、2028 年下半年量产的日程。
- **尚未证实：** 14% 性能提升、23% 功耗下降、50% 能效提升等数字均为 TSMC 对 N2P 的对比承诺，尚无独立测量或量产芯片数据；Siemens EDA 的晶体管级 EM/IR 认证仍在进行，目标 2026 年第四季度，其认证覆盖也少于另外两家。

</div>

## 背景

在芯片行业里，“1.4nm 级”只是代际命名，并非晶体管的实际物理尺寸，指的是比 2nm 级（N2P）更先进的一代工艺。PDK（process design kit，工艺设计套件）是代工厂交给客户的器件模型、设计规则与参数集合，版本推进到 0.9 通常被业界视为可用于正式设计的成熟度门槛；EDA（电子设计自动化）工具认证则是确认 Cadence、Synopsys 等厂商的布局布线、时序、功耗与签核工具能在这套规则下跑通全流程。台积电已在 N2/N2P 上引入纳米片晶体管，A14 改用第二代纳米片与 NanoFlex Pro 标准单元架构，这也是本次 Boost Cell 与低功耗单元能起作用的基础。

## 为什么重要

对计划采用 A14 的芯片设计团队来说，Cadence 与 Synopsys 的全流程认证意味着可以用两条已验证的工具链启动设计；依赖 Siemens EDA 晶体管级 EM/IR 的团队则要等到 2026 年第四季度。A14 要到 2028 年下半年才量产，从设计导入到可出货仍有约两年，早期项目需要把工具与 IP 风险前置处理。

## 后续看点

首要节点是 Siemens EDA 的 A14 晶体管级 EM/IR 认证是否在 2026 年第四季度按期完成；随后看 A14 能否按计划在 2027 年下半年进入风险生产。

{% endraw %}
