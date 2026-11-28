---
layout: story
lang: zh
date: 2026-11-28 06:28:04 -0500
issue: "2026-11-28"
story_id: "sap-confirms-github-incident-report-says-stolen-tokens-allowed-source-d060"
permalink: "/zh/2026/11/28/sap-confirms-github-incident-report-says-stolen-tokens-allowed-source-d060/"
title: "SAP 确认 GitHub 安全事件，源代码据报遭复制篡改"
dek: "SAP 确认发现 GitHub 上的可疑活动，构成一起网络安全事件。SecurityWeek 报道称，黑客利用窃取到的 SAP 员工身份认证令牌（可代替密码访问代码仓库的凭据），复制并修改了托管在 GitHub 上的源代码。"
description: "SAP 确认发现 GitHub 上的可疑活动，构成一起网络安全事件。SecurityWeek 报道称，黑客利用窃取到的 SAP 员工身份认证令牌（可代替密码访问代码仓库的凭据），复制并修改了托管在 GitHub 上的源代码。"
section: "tech-industry"
rank: 17
edition: 0
section_rank: 1
score: 7.0
status: "Announced"
source_name: "SecurityWeek"
source_url: "https://www.securityweek.com/sap-confirms-cyberattack-source-code-reportedly-compromised/"
via: "Techmeme"
discussion_url: null
published_at: "2026-11-27T16:35:08+00:00"
tags: ["cybersecurity", "SAP", "source code", "GitHub", "security incident"]
topics: ["cybersecurity", "sap", "source-code", "github", "security-incident"]
order: "20261128-0-982"
image: "/assets/stories/2026-11-28/sap-confirms-github-incident-report-says-stolen-tokens-allowed-source-d060-share.jpg"
art: "/assets/stories/2026-11-28/sap-confirms-github-incident-report-says-stolen-tokens-allowed-source-d060.jpg"
thumb: "/assets/stories/2026-11-28/sap-confirms-github-incident-report-says-stolen-tokens-allowed-source-d060-640.jpg"
photo_credit: {"url": "https://thumb.wikimedia.org/wikipedia/commons/thumb/8/83/SAP_AG_headquarter_Walldorf_building_1.jpg/1920px-SAP_AG_headquarter_Walldorf_building_1.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail", "author": "Vladislav Bezrukov from Walldorf, Germany", "licence": "CC BY 2.0", "licence_url": "https://creativecommons.org/licenses/by/2.0", "source_url": "https://commons.wikimedia.org/wiki/File:SAP_AG_headquarter_Walldorf_building_1.jpg", "provider": "Wikimedia Commons", "width": 3008, "height": 2000}
---

{% raw %}
<div class="story-lead" markdown="1">

SAP 确认发现 GitHub 上的可疑活动，构成一起网络安全事件。SecurityWeek 报道称，黑客利用窃取到的 SAP 员工身份认证令牌（可代替密码访问代码仓库的凭据），复制并修改了托管在 GitHub 上的源代码。

SAP 的确认目前只覆盖“可疑活动/安全事件”，令牌被盗和代码被改动仍属报道内容，现有报道未披露受影响仓库、代码范围或修复状态。

</div>

<div class="fact-check" markdown="1">

## 已证实与尚未证实

- **已证实：** SAP 向 SecurityWeek 确认检测到 GitHub 上的可疑活动，并将其定性为一起网络安全事件；SAP 自身的表态是这一确认的依据。
- **尚未证实：** 攻击者利用窃取的 SAP 员工认证令牌复制并篡改 GitHub 上的源代码，这一说法目前仅来自《明镜》周刊（DER SPIEGEL）的报道及知情人士转述，SAP 未公开证实；受影响代码的具体范围、是否涉及客户产品、事件时间线以及是否已通知监管机构或客户，现有报道均未说明，也未见独立的第三方取证结论。

</div>

## 背景

GitHub 的访问令牌（token）是替代密码的凭据，携带有效令牌的请求会被 GitHub 视为该员工本人发出，因此攻击者不必攻破 GitHub 平台本身，就能读取或推送代码。SecurityWeek 报道称，此次事件中被盗的员工令牌正是被用来复制并修改 SAP 存放在 GitHub 上的源代码；SAP 确认的是发现可疑活动，令牌与代码改动的细节目前仍来自该媒体报道。

## 为什么重要

如果报道属实，关键后果是代码完整性而非单纯泄露：被修改的代码提交是否进入构建或发布流程，决定影响是否延伸到 SAP 的软件交付和客户部署。SAP 需要说明受影响仓库和提交记录，使用其软件的组织则应等待范围说明，再判断是否要检查自身部署或更新依赖。

## 后续看点

接下来看 SAP 是否发布正式事件通告，披露受影响仓库、令牌撤销范围以及是否有被改代码进入构建或发布；也可关注 GitHub 安全公告或 SecurityWeek 的后续报道是否给出独立验证。

## 延伸阅读

- [SAP Confirms Cyberattack, Source Code Reportedly... - SecurityWeek](https://www.securityweek.com/sap-confirms-cyberattack-source-code-reportedly-compromised/)
- [SAP Confirms Security Incident as Hackers Reportedly Steal ...](https://cybersecuritynews.com/sap-security-incident/)
- [SAP confirms security incident after suspicious GitHub activity](https://www.bleepingcomputer.com/news/security/sap-confirms-security-incident-after-suspicious-github-activity/)

{% endraw %}
