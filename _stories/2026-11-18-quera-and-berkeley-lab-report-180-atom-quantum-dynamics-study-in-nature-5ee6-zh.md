---
layout: story
lang: zh
date: 2026-11-18 12:26:45 -0500
issue: "2026-11-18"
story_id: "quera-and-berkeley-lab-report-180-atom-quantum-dynamics-study-in-nature-5ee6"
permalink: "/zh/2026/11/18/quera-and-berkeley-lab-report-180-atom-quantum-dynamics-study-in-nature-5ee6/"
title: "QuEra 与伯克利实验室在《Nature》发表 180 原子量子动力学研究"
dek: "QuEra Computing 与劳伦斯伯克利国家实验室下属的国家能源研究科学计算中心（NERSC）在《Nature》发表研究，用 QuEra 的模拟式中性原子量子计算机 Aquila 观测量子系统在突变之后如何演化…"
description: "QuEra Computing 与劳伦斯伯克利国家实验室下属的国家能源研究科学计算中心（NERSC）在《Nature》发表研究，用 QuEra 的模拟式中性原子量子计算机 Aquila 观测量子系统在突变之后如何演化…"
section: "chips-compute"
rank: 112
edition: 1
section_rank: 6
score: 7.0
status: "Demonstrated"
source_name: "The Quantum Insider"
source_url: "https://thequantuminsider.com/2026/11/18/quera-berkeley-lab-study-quantum-dynamics-aquila/"
via: null
discussion_url: null
published_at: "2026-11-18T17:03:12+00:00"
tags: ["quantum computing", "neutral atoms", "QuEra", "Nature study", "quantum simulation"]
topics: ["quantum-computing", "neutral-atoms", "quera", "nature-study", "quantum-simulation"]
order: "20261118-1-987"
image: "/assets/stories/2026-11-18/quera-and-berkeley-lab-report-180-atom-quantum-dynamics-study-in-nature-5ee6-share.jpg"
art: "/assets/stories/2026-11-18/quera-and-berkeley-lab-report-180-atom-quantum-dynamics-study-in-nature-5ee6.jpg"
thumb: "/assets/stories/2026-11-18/quera-and-berkeley-lab-report-180-atom-quantum-dynamics-study-in-nature-5ee6-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g0b5b24776bfa417809bacabc0293b6db7b22afabcfd64df1beae9568d312b65cae2c9c123602534b8c10c4768fbc9b27636f4ac24076de872adc6e4b1fb58b92_1280.jpg", "author": "TheDigitalArtist", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/quantum-computer-processor-computer-3679893/", "provider": "Pixabay", "width": 3500, "height": 1969}
---

{% raw %}
<div class="story-lead" markdown="1">

QuEra Computing 与劳伦斯伯克利国家实验室下属的国家能源研究科学计算中心（NERSC）在《Nature》发表研究，用 QuEra 的模拟式中性原子量子计算机 Aquila 观测量子系统在突变之后如何演化，实验规模从最长 52 个原子的一维链到最高 180 个原子的二维阵列。团队报告了三项结果：系统并非平滑地趋于稳定，而是维持远超预期的稳定中间图案，即“预热化”（prethermalization）；这些图案在可预测的临界点发生“共振熔化”；二维情况下系统响应出现随阵列增大而更锐利的突变，作者将其认定为一阶动力学相变，并称它在平衡态相图中没有直接对应物。NERSC 用 Perlmutter 超算和 QuEra 开源软件 Bloqade 对小规模系统做精确经典计算，以此校验 Aquila 的结果，Aquila 本身则通过亚马逊云科技的 Amazon Braket 服务访问。这是一项经同行评审的模拟量子计算科学成果，而非通用可编程或容错量子计算能力的展示。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** QuEra 与劳伦斯伯克利国家实验室（LBNL）团队的论文已发表于《Nature》，Nature 官网条目（2026 年 11 月 4 日上线）确认该研究使用可编程中性原子量子模拟器，在最多 180 个量子比特的二维阵列（及最长 52 原子的链）上观测到预热化（prethermalization）动力学相变与共振熔化现象；NERSC 团队通过 Amazon Braket 访问 Aquila，并用 Perlmutter 超级计算机做小规模精确经典计算以校验实验结果——以上均有 Nature 条目、QuEra 新闻稿及 HPCwire 报道相互印证。
- **尚未证实：** 预热带化寿命、共振熔化位置以及“二维一阶动力学相变没有平衡态对应物”这一物理解释，目前仅出自论文作者自身的分析与 QuEra 新闻稿表述，尚无独立团队复现或第三方基准评测；Aquila 结果在 180 原子规模下已无法用经典计算逐一校验（经典精确计算仅覆盖小规模探测系统），因此大尺度结论依赖作者对器件可信度的论证；此外新闻稿中“中性原子量子计算领导者”为公司自述，文中提及的下一代机器 Libra 的细节在报道中被截断，其能力、时间表与容错路线均未获证实。另需注意日期口径：Nature 页面显示论文 2026 年 11 月 4 日上线，而新闻稿与媒体报道的发布日为 11 月 18 日，两者分别指论文上线与对外发布，并非同一事件。

</div>

## 背景

Aquila 属于“模拟型”中性原子量子计算机：它把原子排成阵列，用激光场整体驱动原子演化，再逐比特测量，而不是像通用量子计算机那样运行由逻辑门组成的纠错程序。据 thequantuminsider 报道，Aquila 自 2022 年起通过亚马逊云 AWS 的量子服务 Amazon Braket 对外提供，是该平台上首台中性原子量子计算机。这类实验之所以需要真实量子硬件，是因为随着演化时间增加，量子纠缠增长很快，经典计算机难以模拟大系统的这类动力学；本次研究因此用 NERSC 的 Perlmutter 超算仅做小规模精确计算，用来校验 Aquila 的结果。

## 为什么重要

对使用 Aquila 的研究者，这项结果的可操作含义是：先用 Bloqade 在小规模系统上做精确经典计算、确认硬件结果可信，再扩展到 180 原子阵列；二维转变随阵列增大而变得更陡，说明更大阵列正是模拟器能提供新增信息的地方。Aquila 仍是面向特定模型的模拟量子计算机，而非通用门级机器；QuEra 路线图中的容错机型 Libra 计划 2028 年通过 Amazon Braket 提供，因此当前开发应把模拟专用任务与未来容错应用分开规划。

## 后续看点

值得关注的是其他研究组能否在 Aquila 或别的平台上独立复现这次报告的动力学相变，以及 QuEra 表示要把 Aquila 的建造与运营经验带入的后续机器 Libra 何时公布可检验的时间表。

## 延伸阅读

- [Observation of prethermal dynamical phase transitions and ...](https://www.nature.com/articles/s41586-026-11225-9)
- [QuEra Computing and Lawrence Berkeley National Laboratory ...](https://www.prnewswire.com/news-releases/quera-computing-and-lawrence-berkeley-national-laboratory-publish-nature-study-of-quantum-dynamics-on-up-to-180-qubits-302943182.html)
- [QuEra and Berkeley Lab Publish Nature Study of Quantum ...](https://www.hpcwire.com/off-the-wire/quera-and-berkeley-lab-publish-nature-study-of-quantum-dynamics-on-up-to-180-qubits/)
- [Libra, QuEra's first fault tolerant quantum computer](https://www.quera.com/libra)
- [QuEra Updates Neutral-Atom Quantum Roadmap with 2028 Fault ...](https://quantumcomputingreport.com/quera-updates-neutral-atom-quantum-roadmap-with-2028-fault-tolerant-launch-on-amazon-braket/)

{% endraw %}
