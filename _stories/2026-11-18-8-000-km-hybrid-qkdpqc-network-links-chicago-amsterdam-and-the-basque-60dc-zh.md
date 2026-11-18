---
layout: story
lang: zh
date: 2026-11-18 12:26:45 -0500
issue: "2026-11-18"
story_id: "8-000-km-hybrid-qkdpqc-network-links-chicago-amsterdam-and-the-basque-60dc"
permalink: "/zh/2026/11/18/8-000-km-hybrid-qkdpqc-network-links-chicago-amsterdam-and-the-basque-60dc/"
title: "芝加哥至欧洲8000公里混合量子安全网络完成演示"
dek: "一个由高校、科研网络和厂商组成的国际联盟在 2026 年超算大会（SC26）上演示了一条约 8000 公里的混合量子安全网络，连接美国芝加哥、荷兰阿姆斯特丹与西班牙毕尔巴鄂（Bilbao）和 Zamudio，共设 5 个量子节点。"
description: "一个由高校、科研网络和厂商组成的国际联盟在 2026 年超算大会（SC26）上演示了一条约 8000 公里的混合量子安全网络，连接美国芝加哥、荷兰阿姆斯特丹与西班牙毕尔巴鄂（Bilbao）和 Zamudio，共设 5 个量子节点。"
section: "chips-compute"
rank: 113
edition: 1
section_rank: 7
score: 7.0
status: "Demonstrated"
source_name: "The Quantum Insider"
source_url: "https://thequantuminsider.com/2026/11/18/8000-km-quantum-safe-network-us-europe-demonstration/"
via: null
discussion_url: null
published_at: "2026-11-18T12:44:46+00:00"
tags: ["quantum key distribution", "post-quantum cryptography", "quantum-safe networking", "optical transport encryption", "quantum networking demonstration"]
topics: ["quantum-key-distribution", "post-quantum-cryptography", "quantum-safe-networking", "optical-transport-encryption", "quantum-networking-demonstration"]
order: "20261118-1-986"
image: "/assets/stories/2026-11-18/8-000-km-hybrid-qkdpqc-network-links-chicago-amsterdam-and-the-basque-60dc-share.jpg"
art: "/assets/stories/2026-11-18/8-000-km-hybrid-qkdpqc-network-links-chicago-amsterdam-and-the-basque-60dc.jpg"
thumb: "/assets/stories/2026-11-18/8-000-km-hybrid-qkdpqc-network-links-chicago-amsterdam-and-the-basque-60dc-640.jpg"
photo_credit: {"url": "https://thumb.wikimedia.org/wikipedia/commons/thumb/c/cc/Alice_in_BBN_laboratory_-_DARPA_Quantum_Network%2C_January_2003.jpg/1920px-Alice_in_BBN_laboratory_-_DARPA_Quantum_Network%2C_January_2003.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail", "author": "Daderot", "licence": "CC0", "licence_url": "http://creativecommons.org/publicdomain/zero/1.0/deed.en", "source_url": "https://commons.wikimedia.org/wiki/File:Alice_in_BBN_laboratory_-_DARPA_Quantum_Network,_January_2003.jpg", "provider": "Wikimedia Commons", "width": 1984, "height": 1488}
---

{% raw %}
<div class="story-lead" markdown="1">

一个由高校、科研网络和厂商组成的国际联盟在 2026 年超算大会（SC26）上演示了一条约 8000 公里的混合量子安全网络，连接美国芝加哥、荷兰阿姆斯特丹与西班牙毕尔巴鄂（Bilbao）和 Zamudio，共设 5 个量子节点。短链路使用 Luxquanta 的 Nova lq 量子密钥分发（QKD，靠物理定律而非计算难度生成密钥）系统：芝加哥两个展台之间不到 1 公里，毕尔巴鄂与 Zamudio 之间 25 公里；Ciena 的 WL6e（1.6 Tb/s）与 WL5e（800 Gb/s）光传输设备在单对光纤上复用量子信道与加密数据，并在平台内把 QKD 密钥与后量子密码（PQC，抗量子计算的数学算法）混合使用。毕尔巴鄂—阿姆斯特丹约 1200 公里、阿姆斯特丹—芝加哥约 7000 公里的长距离段改用基于美国 NIST ML-KEM 标准的 PQC，由巴斯克大学 i2T 研究组的 QuLore 编排框架按各链路能力选择 QKD 或 PQC 并中继密钥，形成光层、IPsec 网络层和应用层（改造的开源视频通话）三层加密。这是会议现场的演示，而非可订购的商用服务，报道源自主办方新闻稿，没有独立的性能测量或基准数据。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** 主办方新闻稿称，SC26 期间在芝加哥、阿姆斯特丹与毕尔巴鄂/Zamudio 的五节点间搭建了 8000 公里混合网络，使用 Luxquanta Nova lq QKD、Ciena WL6e/WL5e 光层加密、QuLore 编排与 ML-KEM，三层加密在演示中同时运行。
- **尚未证实：** 密钥生成速率、QKD 与 PQC 切换时延、三层加密的实际吞吐等性能说法仅出自新闻稿，无第三方测量或同行评议细节；该架构何时进入生产网络、成本与运维要求也未说明。

</div>

## 背景：QKD 与 PQC 为何要混用

量子密钥分发（QKD）把密钥的安全性建立在物理定律上，但光子信号在光纤中衰减，实际传输距离通常只有约 100 公里，适合城域网；后量子密码（PQC）则是用能抵抗量子计算机的数学算法在软件层协商密钥，距离不受限，两者正好互补。EHU 的 i2T 研究组此前已把 QuLore 作为“扩展量子安全网络的自适应安全框架”发表（arXiv 论文），并演示过用 QKD 生成的密钥在 Ciena 的 DWDM 设备上加密 100 Gbps 业务流；这次演示是把同一思路从单段链路推广到跨三大洲、多厂商密钥管理系统互通的规模。

## 为什么重要

对无法在每个站点部署 QKD 硬件的网络——光纤 QKD 目前大致限于约 100 公里——这次演示给出的答案是编排层：Luxquanta、巴斯克大学的 vKMS 与 SURF 的开源 eduKMS 等不同来源的密钥管理系统通过标准接口互通，QuLore 按两端点与网络实际能力自动选择 QKD 或 PQC 密钥。这意味着运维方不必一次性替换全部链路即可推进量子安全迁移，但需要支持标准密钥管理接口，并接受按链路分级的保护强度：长距离段的安全性此时依赖 ML-KEM 等算法假设，而非物理定律。

## 延伸阅读

- [QuLore : An Adaptive Security Framework to Extend Quantum - Safe ...](https://arxiv.org/html/2511.22416)
- [Smart Quantum Technologies for Everything...](https://i2t.ehu.eus/en/resources/12/smartquant4E)

{% endraw %}
