---
layout: story
lang: zh
date: 2026-11-16 06:00:00 -0500
issue: "2026-11-16"
story_id: "nvidia-and-lambda-disclose-first-production-co-packaged-optics-cluster-181f"
permalink: "/zh/2026/11/16/nvidia-and-lambda-disclose-first-production-co-packaged-optics-cluster-181f/"
title: "NVIDIA 与 Lambda 披露首个生产级共封装光学集群，规模逾 1 万 GPU"
dek: "据 ServeTheHome 报道，Lambda 披露其一个生产集群已部署共封装光学（co-packaged optics，CPO，即把光引擎与交换芯片封装在同一基板上，替代可插拔光模块），GPU 规模超过 1 万块…"
description: "据 ServeTheHome 报道，Lambda 披露其一个生产集群已部署共封装光学（co-packaged optics，CPO，即把光引擎与交换芯片封装在同一基板上，替代可插拔光模块），GPU 规模超过 1 万块…"
section: "chips-compute"
rank: 207
edition: 2
section_rank: 1
score: 8.0
status: "Released"
source_name: "ServeTheHome"
source_url: "https://www.servethehome.com/nvidia-and-lambda-disclose-first-production-co-packaged-optics-cluster-it-is-finally-real/"
via: null
discussion_url: null
published_at: "2026-11-16T21:24:47+00:00"
tags: ["co-packaged optics", "NVIDIA", "Lambda", "AI data centers", "networking"]
topics: ["co-packaged-optics", "nvidia", "lambda", "ai-data-centers", "networking"]
order: "20261116-2-992"
image: "/assets/stories/2026-11-16/nvidia-and-lambda-disclose-first-production-co-packaged-optics-cluster-181f-share.jpg"
art: "/assets/stories/2026-11-16/nvidia-and-lambda-disclose-first-production-co-packaged-optics-cluster-181f.jpg"
thumb: "/assets/stories/2026-11-16/nvidia-and-lambda-disclose-first-production-co-packaged-optics-cluster-181f-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g5742ff3a01a0edf2aa7896a2bc86d503a459baf4cdfca6e6c4af185839d396a52c9c800c69b3614bbc75714483d066bd5340c59c2508b048cab5c491d00496f9_1280.jpg", "author": "Lucent_Designs_dinoson20", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/fiber-cable-wire-connection-4814456/", "provider": "Pixabay", "width": 5184, "height": 3456}
---

{% raw %}
<div class="story-lead" markdown="1">

据 ServeTheHome 报道，Lambda 披露其一个生产集群已部署共封装光学（co-packaged optics，CPO，即把光引擎与交换芯片封装在同一基板上，替代可插拔光模块），GPU 规模超过 1 万块，NVIDIA 同时被列为该部署的相关方，报道称这是业界首个公开披露的 CPO 生产集群。报道的表述重点是「首个披露」，即此前没有运营商公开承认在量产环境中使用 CPO，而不是说这是首台可用的 CPO 设备。

该报道未给出交换平台型号、端口速率、功耗对比或故障率等技术数据，也没有第三方测试或 NVIDIA、Lambda 之外的独立核实。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** 据 ServeTheHome、Converge Digest 与 ico-optics 一致引述，Lambda 于 11 月 16 日宣布其魁北克园区部署了 NVIDIA 的共封装光学（CPO，把光引擎与交换芯片封装在一起的交换机技术）交换机，连接超过 10,000 块 Blackwell Ultra GPU；这是 Lambda 自己发布的部署声明。
- **尚未证实：** 所谓“全球首个大规模 CPO 部署”的定位目前只有 Lambda 与 NVIDIA 一方的说法，没有第三方独立核实；报道也未给出交换机型号、端口速率或总带宽、部署完成时间、集群实测性能与可靠性数据。原始报道本身仅有两句话加一个链接，技术细节仍需 NVIDIA 或 Lambda 的完整技术披露来补足。

</div>

## 背景

共封装光学（co-packaged optics，CPO）指的是把光引擎与交换芯片封装在同一基板上，让高速信号在封装内部完成电光转换，而不是像传统方案那样经由面板上的可插拔光模块（pluggable optics）走较长电路。支持者认为这样可以降低每比特功耗、提升带宽密度，因此 CPO 长期被视为大规模 AI 集群网络互连的下一步；但此前公开披露的多为样品、演示或路线图。此次 Lambda 称其生产集群已采用该方案，是目前唯一可参照的公开说法。

## 为什么重要

对正在搭建万卡级集群的运营方来说，CPO 把电光转换从可插拔光模块搬到交换机封装上，按业界对这条路线的一贯描述，可降低功耗、改善信号完整性并提升可靠性。Lambda 的披露意味着这种形态已进入生产集群，而不只是路线图；打算跟进的数据中心因此需要提前规划：沿用可插拔光模块的采购、备件更换和现场故障排查流程将不再适用，需向交换机厂商确认光引擎与激光器的可维护性和供货节奏（NVIDIA 此前计划 2026 年初先推出 Quantum-X InfiniBand 的 CPO 交换机）。

## 后续看点

关注 NVIDIA 或 Lambda 是否补充公布该集群的交换平台、端口速率与功耗数据，以及其他大型 GPU 集群运营商是否随之披露类似的 CPO 生产部署。

## 延伸阅读

- [NVIDIA and Lambda Disclose First Production Co-Packaged ...](https://www.servethehome.com/nvidia-and-lambda-disclose-first-production-co-packaged-optics-cluster-it-is-finally-real/)
- [NVIDIA and Lambda Launch First Production CPO Cluster](https://www.ico-optics.org/nvidia-and-lambda-launch-first-production-cpo-cluster/)
- [Lambda Deploys NVIDIA Co-Packaged Optics for 10,000 ...](https://convergedigest.com/lambda-nvidia-cpo-10000-blackwell-ultra-gpus/)
- [Nvidia outlines plans for using light for communication between AI ...](https://www.tomshardware.com/networking/nvidia-outlines-plans-for-using-light-for-communication-between-ai-gpus-by-2026-silicon-photonics-and-co-packaged-optics-may-become-mandatory-for-next-gen-ai-data-centers)
- [How AI factories need co - packaged optics for better networking](https://www.linkedin.com/posts/andrii-drok-479921244_nvidia-ai-networkengineer-activity-7363538718349025282-OVaM)
- [The AI Datacenter Optical Interconnect Boom – Ben Pouladian](https://benpouladian.com/the-ai-datacenter-optical-interconnect/)

{% endraw %}
