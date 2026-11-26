---
layout: story
lang: zh
date: 2026-11-26 06:28:37 -0500
issue: "2026-11-26"
story_id: "deepmind-reports-alphaproof-code-proof-of-signal-s-libsignal-binary-bbd6"
permalink: "/zh/2026/11/26/deepmind-reports-alphaproof-code-proof-of-signal-s-libsignal-binary-bbd6/"
title: "DeepMind 用 AlphaProof Code 完成 Signal 加密库二进制的形式化证明"
dek: "谷歌 DeepMind 团队用一套名为 AlphaProof Code 的流程，为 Signal 使用的加密库 libsignal 的 Arm（AArch64）编译二进制给出了端到端形式化证明。"
description: "谷歌 DeepMind 团队用一套名为 AlphaProof Code 的流程，为 Signal 使用的加密库 libsignal 的 Arm（AArch64）编译二进制给出了端到端形式化证明。"
section: "tech-industry"
rank: 20
edition: 0
section_rank: 5
score: 7.0
status: "Released"
source_name: "Tom's Hardware"
source_url: "https://www.tomshardware.com/tech-industry/artificial-intelligence/google-deepmind-ai-engineers-conjure-mathematical-proof-of-signals-encryption-protocol-alphaproof-code-framework-powered-human-bot-cooperation-for-speedy-work"
via: null
discussion_url: null
published_at: "2026-11-25T12:00:00+00:00"
tags: ["AI formal verification", "Signal", "DeepMind", "cryptography", "AlphaProof Code"]
topics: ["ai-formal-verification", "signal", "deepmind", "cryptography", "alphaproof-code"]
order: "20261126-0-979"
image: "/assets/stories/2026-11-26/deepmind-reports-alphaproof-code-proof-of-signal-s-libsignal-binary-bbd6-share.jpg"
art: "/assets/stories/2026-11-26/deepmind-reports-alphaproof-code-proof-of-signal-s-libsignal-binary-bbd6.jpg"
thumb: "/assets/stories/2026-11-26/deepmind-reports-alphaproof-code-proof-of-signal-s-libsignal-binary-bbd6-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g6caf1941f8ecd62dd372f86b94080e770ece1b744915bfe7235325b1ed3f755ad9223c43c95a1ceddc170341b97db7ab32711313f724095e50b27fcc00b0e4ee_1280.jpg", "author": "422737", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/privacy-policy-data-security-445156/", "provider": "Pixabay", "width": 3648, "height": 2736}
---

{% raw %}
<div class="story-lead" markdown="1">

谷歌 DeepMind 团队用一套名为 AlphaProof Code 的流程，为 Signal 使用的加密库 libsignal 的 Arm（AArch64）编译二进制给出了端到端形式化证明。流程分两步：先为 libsignal 的密码学实现写出形式化规范并生成约 120 万行 Lean 证明；再用约 530 万行 Lean 逐条指令核对二进制与所定义的 AArch64 指令、寄存器、内存及 Linux 进程行为一致，期间约 1% 的代码被标记出来交人工复核。论文与代码仓库已在 DeepMind 官网和 GitHub（google-deepmind/code-verification）公开。报道指出验证对象是编译后的二进制而非源码，因此该方法可复用于其他软件；但证明只表明 libsignal 按规范运行，无法发现有人向 Signal 或其他应用植入窃取消息的额外代码。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** DeepMind 在其博客公布了这项工作，并放出了论文与 GitHub 代码仓库；证明针对的是带少量外围代码、由 Arm 工具链编译的 libsignal 二进制；团队自述的 Lean 规模（约 120 万行用于规范与密码学推理、约 530 万行用于逐条二进制指令核对）和约 1% 人工复核比例均出自其自身说明。
- **尚未证实：** 报道中“因此 Signal 是安全的”属记者推论，论文只证明该二进制与团队自己写的规范一致；暂无独立第三方复算这套 Lean 证明的报道；规范本身是否准确仍靠人工判断，文章也未给出项目耗时或与人工验证的成本对比。

</div>

## 背景

形式化验证是用数学证明而非测试来确认程序行为符合规范，Lean 正是为此设计的证明助手；这类工作历来极其昂贵，seL4 微内核的验证据称耗时二十年，CompCert C 编译器的验证耗时六年。AI Daily Radar 11 月 23 日的日报曾记录过一场围绕 1700 万行 Lean 产物的争论：有评论者担心 LLM 辅助生成的大规模证明可能把错误藏在转换后的子证明或庞大体量之中。此次 DeepMind 的产物同样以百万行计——约 120 万行用于协议数学推理，530 万行用于核对二进制指令——因此“证明大到能否被审查”的疑问依然适用。

## 为什么重要

对做高保障软件的团队而言，这次证明的对象是编译后的二进制而不是源码，意味着验证可以覆盖编译器和构建链引入的差异，而这正是过去形式化验证最难触及的一段。同时 DeepMind 自述大部分精力花在写规范而非做证明，说明瓶颈已从“证明是否负担得起”转为“该证明什么”，准备采用这类流程的团队应把资源优先投在规范撰写和那约 1% 的人工复核环节。对普通 Signal 用户，这条证明不改变现有安全边界：它不检测被植入的恶意代码，第三方应用实现了 Signal 协议也不等于整体隐私有保障。

## 后续看点

论文和仓库既已公开，接下来可核对的是是否有外部团队独立用 Lean 重新检查这套证明，以及 DeepMind 是否公布 AlphaProof Code 在第二个代码库上的验证结果。

## 延伸阅读

- [2026-11-23 — Blog post on 17-million-line Lean artifact sparks LLM proof debate](https://micjm.com/blog/yes-17m-lines-of-lean-is-a-lot/)

{% endraw %}
