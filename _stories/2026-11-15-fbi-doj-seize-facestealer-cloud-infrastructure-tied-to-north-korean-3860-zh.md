---
layout: story
lang: zh
date: 2026-11-15 06:00:00 -0500
issue: "2026-11-15"
story_id: "fbi-doj-seize-facestealer-cloud-infrastructure-tied-to-north-korean-3860"
permalink: "/zh/2026/11/15/fbi-doj-seize-facestealer-cloud-infrastructure-tied-to-north-korean-3860/"
title: "FBI查封朝鲜\"FaceStealer\"攻击所用的云基础设施"
dek: "美国联邦调查局（FBI）与司法部（DOJ）首次为朝鲜政府支持的一类社交工程攻击公开命名\"FaceStealer\"，并宣布已查封其使用的云基础设施，其中存有900段针对特定目标人物的视频。"
section: "tech-industry"
rank: 12
section_rank: 1
score: 8.0
status: "Announced"
source_name: "Tom's Hardware"
source_url: "https://www.tomshardware.com/tech-industry/cyber-security/fbi-disrupts-north-korean-facestealer-campaign-behind-usd5-billion-binance-hack-doj-seizes-facestealer-cloud-infrastructure-containing-900-videos-of-tech-workers-hackers-used-ai-deepfakes-to-steal-usd400-million-and-compromise-open-source-software"
via: null
discussion_url: null
published_at: "2026-11-15T16:30:00+00:00"
tags: ["North Korea cybercrime", "cryptocurrency theft", "FBI/DOJ", "deepfake social engineering", "supply chain security"]
topics: ["north-korea-cybercrime", "cryptocurrency-theft", "fbi-doj", "deepfake-social-engineering", "supply-chain-security"]
order: "20261115-987"
image: "/assets/stories/2026-11-15/fbi-doj-seize-facestealer-cloud-infrastructure-tied-to-north-korean-3860-share.jpg"
art: "/assets/stories/2026-11-15/fbi-doj-seize-facestealer-cloud-infrastructure-tied-to-north-korean-3860.jpg"
thumb: "/assets/stories/2026-11-15/fbi-doj-seize-facestealer-cloud-infrastructure-tied-to-north-korean-3860-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/gcdeb7cd2474e11d2f214a2e66e84d95f71172c041c3c94d031bce2fe0d0062b764d79d5d525047457124bd5119b1c1f3230e685a446f8bcd2f6233f55d6a79b0_1280.jpg", "author": "bsdrouin", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/network-server-system-2402637/", "provider": "Pixabay", "width": 1920, "height": 1080}
description: "美国联邦调查局（FBI）与司法部（DOJ）首次为朝鲜政府支持的一类社交工程攻击公开命名\"FaceStealer\"，并宣布已查封其使用的云基础设施，其中存有900段针对特定目标人物的视频。"
---

{% raw %}
<div class="story-lead" markdown="1">

美国联邦调查局（FBI）与司法部（DOJ）首次为朝鲜政府支持的一类社交工程攻击公开命名"FaceStealer"，并宣布已查封其使用的云基础设施，其中存有900段针对特定目标人物的视频。FBI的详细报告称，该行动已持续至少18个月，并认定其盗取的加密货币约4亿美元；而Tom's Hardware称，与该行动相关、金额最大的一起是近期Binance被盗案，涉款逾50亿美元（其中大部分已被冻结或追回），报道未解释这一数字与4亿美元之间如何对应。

FBI还指出，攻击者多次试图渗透开源软件供应链，重点针对JavaScript/NPM模块和Rust crate；报道推测其中包括2026年3月的Axios投毒事件，该库每周下载量约1亿次，被植入远程控制工具数小时。其手法是先通过AI深度伪造、真实聊天记录与人脉关系层层铺垫，再以搭建在攻击者服务器上、域名仿冒的假Zoom/Teams会议，以"技术故障"为由诱导受害者安装所谓"更新"，从而植入恶意软件并窃取浏览器会话与CI/CD凭证。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** 美国司法部发布公告宣布采取行动打击朝鲜以加密货币窃取为目的的计划，联邦调查局（FBI）同步发布 IC3 报告，将该行动命名为“FaceStealer”，并称已查获存放有 900 段目标受害者视频的云端基础设施；FBI 表示该计划造成约 4 亿美元加密货币损失——以上均出自司法部与 FBI 的公开文件，经 Tom's Hardware 转述。
- **尚未证实：** 报道标题与正文所称“超 50 亿美元”的币安被盗规模，以及该案与 FaceStealer 的直接归属关系，目前依赖媒体叙述与币安博文，报道本身也说明其中大部分资金已被冻结或追回，实际净损失未经独立核实；文章把 2026 年 3 月的 Axios npm 包投毒事件“几乎可以肯定”归为同一组织所为，但这是记者推断，FBI 报告并未点名该事件，受害规模与视频数量也没有第三方验证。

</div>

## 背景

这类攻击的关键前置条件是先取得受害者的通讯录和聊天记录：攻击者侵入其通讯软件后，用真实对话与联系人信息伪装成招聘方或投资人，再借深度伪造视频把目标引向假会议。Tom's Hardware 将 2026 年 3 月的 Axios npm 包被植入远程访问工具事件视为同一手法的案例；npm 是 JavaScript 生态最常用的包管理器，Axios 每周下载量约 1 亿次。

## 为什么重要

对开源项目维护者和CI/CD权限持有者来说，这份报告说明攻击入口已从"骗过普通用户"转向"骗过能发布软件包的人"：被冒充CEO的假Slack工作区、假Teams会议和仿冒域名（如"uu01webzoom.us"、"teams.livemeet.us"）足以让维护者亲手在自己的包里放入后门，而下游数百万次下载会把风险放大。实际操作上，收到招聘或投资邀约的开发者应核对会议域名是否与官方域名一致，任何要求安装"会议插件"或"更新"的提示都应拒绝；若已安装，应立即轮换浏览器会话、包管理账号与CI/CD密钥。

## 后续看点

可关注两条可核查的线索：司法部是否对被查封基础设施公布进一步的起诉或资产没收文件，以及FBI IC3是否会更新该报告的通报内容，把Axios npm 投毒事件等具体供应链攻击正式归因到FaceStealer。

{% endraw %}
