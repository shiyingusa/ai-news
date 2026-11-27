---
layout: story
lang: zh
date: 2026-11-19 06:28:30 -0500
issue: "2026-11-19"
story_id: "java4shell-critical-openjdk-flaw-allows-rce-on-avx-512-servers-3797"
permalink: "/zh/2026/11/19/java4shell-critical-openjdk-flaw-allows-rce-on-avx-512-servers-3797/"
title: "Java4Shell：OpenJDK Base64 优化缺陷可致未认证远程代码执行"
dek: "据发现该漏洞的 Calif Research 披露，OpenJDK 中一段手写的 Base64 解码汇编优化漏掉了边界检查：攻击者只需输入 64 个“A”加一个“=”填充符，就能越界改写相邻内存并据此实现远程代码执行。"
description: "据发现该漏洞的 Calif Research 披露，OpenJDK 中一段手写的 Base64 解码汇编优化漏掉了边界检查：攻击者只需输入 64 个“A”加一个“=”填充符，就能越界改写相邻内存并据此实现远程代码执行。"
section: "tech-industry"
rank: 15
edition: 0
section_rank: 5
score: 7.0
status: "Released"
source_name: "Tom's Hardware"
source_url: "https://www.tomshardware.com/tech-industry/cyber-security/critical-java-vulnerability-puts-millions-of-sites-services-and-devices-at-risk-of-remote-code-execution-triggers-with-64-as-and-an-sign-openjdk-optimization-bug-lets-an-attacker-trigger-it-just-by-inputting-repeated-text"
via: null
discussion_url: null
published_at: "2026-11-19T10:30:00+00:00"
tags: ["Java", "remote code execution", "security vulnerability", "Oracle", "CVE-2026-114938"]
topics: ["java", "remote-code-execution", "security-vulnerability", "oracle", "cve-2026-114938"]
order: "20261119-0-984"
image: "/assets/stories/2026-11-19/java4shell-critical-openjdk-flaw-allows-rce-on-avx-512-servers-3797-share.jpg"
art: "/assets/stories/2026-11-19/java4shell-critical-openjdk-flaw-allows-rce-on-avx-512-servers-3797.jpg"
thumb: "/assets/stories/2026-11-19/java4shell-critical-openjdk-flaw-allows-rce-on-avx-512-servers-3797-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g035d58e886eeb7ec49ac0b875dfb25855e6f29d1616992ce128fc111ce676a34350144196d5f42cbae2fbd1f404fc4ed3f6ca6b571ee34b2291b28d9ed7eb708_1280.jpg", "author": "Akela999", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/electrical-data-center-2476783/", "provider": "Pixabay", "width": 4096, "height": 2160}
---

{% raw %}
<div class="story-lead" markdown="1">

据发现该漏洞的 Calif Research 披露，OpenJDK 中一段手写的 Base64 解码汇编优化漏掉了边界检查：攻击者只需输入 64 个“A”加一个“=”填充符，就能越界改写相邻内存并据此实现远程代码执行。漏洞编号 CVE-2026-114938，Calif 按较新的 CVSS 4.0 给出 9.2 分，Oracle、Red Hat 等厂商各自评级在 8 至 9.8 之间，口径并不一致。

触发有条件限制：目标须运行在支持 AVX-512 VBMI 扩展的 x86-64 CPU 上，实际对应 2021 年前后的 Intel Ice Lake 和 2022 年的 AMD Zen 4 服务器型号，更老的芯片因不含这段优化而不受影响。Oracle 表示已修复并发布更新版本，但 Calif 称披露时 Keycloak、Jira、Confluence、Jenkins、PingFederate 存在无需登录的完整 RCE，Apache Kafka Broker、Solr、Elasticsearch、Gerrit、Spinnaker 则可在认证后被利用，IBM、Red Hat、Siemens、Broadcom 以及大量内嵌 Java 的容器镜像都需要各自跟进。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** CVE-2026-114938（代号“Java4Shell”）于 2026 年 11 月 17 日公开披露，是 OpenJDK 中 Base64 解码优化实现的内存破坏漏洞；Oracle 已发布修复版本，Sophos、Censys 等厂商也发布了安全公告；触发该漏洞需要 Java 实例运行在支持 AVX-512 VBMI 的 x86-64 处理器上（如 Intel Ice Lake、AMD Zen 4）。
- **尚未证实：** 评分口径存在分歧——Oracle 按 CVSS 3.1 评为 8.1（高危），发现方 Calif Research 按 CVSS 4.0 评为 9.2（严重）；“数百万站点与服务受影响”的规模估计、Keycloak/Jira/Confluence/Jenkins/PingFederate 等具体应用清单、该漏洞由消耗 200 美元 token 的 AI 机器人发现的说法，以及各 Linux 发行版与第三方厂商的补丁覆盖情况，均未见独立验证，报道也未给出任何野外已遭利用的证据。

</div>

## 背景

Java 的绝大多数发行版——无论 Oracle 官方 JDK 还是第三方实现——都从 OpenJDK 派生，因此上游库的一处缺陷会同时出现在各厂商的 JDK、打包了 Java 运行时的应用以及大量容器镜像里。这次出问题的是 Base64 解码优化：Base64 用于把二进制数据转成纯文本，常见于在 HTML 中内嵌图片、邮件附件和证书指纹等场景，几乎所有语言都依赖它。据安全厂商整理，受影响的是 OpenJDK 17.0.6 及之后版本、Java 21、25、27 在 2026 年 11 月 17 日修复前的版本，以及 Oracle Java SE 8 Enterprise Performance Pack 8u511b33-perf，ARM64 平台不在影响范围内。

## 为什么重要

这条漏洞的实际后果是：只给 Oracle JDK 打补丁并不够，因为 Keycloak、Jira、Confluence、JFrog Artifactory、Jenkins、PingFederate 等应用会各自内置一份 Java 运行时。根据 Qualys、Check Point 和 The Hacker News 的报道，在默认配置下，攻击者无需登录即可实现远程代码执行（RCE）；Kafka Broker、Solr、Elasticsearch、Gerrit、Spinnaker 则需要在登录后才能利用。运维团队应优先排查 CPU 是否支持 AVX-512 VBMI（Intel Ice Lake、AMD Zen 4 及之后的服务器芯片）以确认暴露面：不支持该扩展的旧 CPU 不受该代码路径影响，但仍需按厂商公告升级各自内嵌的 Java。

## 后续看点

接下来可关注 IBM、Red Hat、Siemens、Broadcom 等厂商的补丁公告，以及 Jira、Confluence、Jenkins、Keycloak 等受影响应用与相关容器镜像的升级、重建进度。另一个可核查的信号是该 CVE 是否出现公开利用代码，或被列入 CISA 的已知被利用漏洞目录。

## 延伸阅读

- [Advisory: OpenJDK Base64 Vulnerability - Java4Shell (CVE-2026 ...](https://www.sophos.com/en-us/security-advisories/sophos-sa-20261118-java4shell)
- [Nov 18 Advisory: OpenJDK Remote Code Execution (Java4Shell ...](https://censys.com/advisory/cve-2026-114938/)
- [Java4Shell CVE-2026-114938: Patch Vulnerable OpenJDK ...](https://computingforgeeks.com/java4shell-cve-2026-114938/)
- [Java 4 Shell CVE-2026-114938: Affected Versions & Mitigation](https://orca.security/resources/research/java4shell-critical-openjdk-base64-decoder-flaw-could-allow-unauthenticated-remote-code-execution/)
- [Java 4 Shell (CVE-2026-114938): Affected Versions , Fix, Workaround](https://www.cyberkendra.com/2026/11/cve-2026-114938-pre-auth-rce-flaw-in-java-17-puts-servers-at-risk.html)
- [Java 4 Shell (CVE-2026-114938): OpenJDK RCE Vulnerability FAQ](https://www.tenable.com/blog/java4shell-cve-2026-114938-frequently-asked-questions-about-openjdk-rce-vulnerability)
- [How to Find, Mitigate, and Patch the Critical Java4Shell Flaw ...](https://blog.qualys.com/vulnerabilities-threat-research/2026/11/17/how-to-find-mitigate-and-patch-the-critical-java4shell-flaw-cve-2026-114938-now)
- [Java4Shell CVE-2026-114938: What You Need to Know](https://blog.checkpoint.com/security/java4shell-cve-2026-114938-check-your-java-services-now/)
- [Java4Shell Flaw (CVE-2026-114938) Enables Pre-Auth RCE in ...](https://thehackernews.com/2026/11/java4shell-cve-2026-114938-enables-pre.html)

{% endraw %}
