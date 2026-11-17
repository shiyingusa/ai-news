---
layout: story
lang: zh
date: 2026-11-17 06:00:00 -0500
issue: "2026-11-17"
story_id: "calif-says-gpt-6-cyber-found-java-rce-java4shell-oracle-patches-eb62"
permalink: "/zh/2026/11/17/calif-says-gpt-6-cyber-found-java-rce-java4shell-oracle-patches-eb62/"
title: "Calif称用GPT-6 Cyber发现Java4Shell漏洞，Oracle已发补丁"
dek: "网络安全初创公司 Calif 声称，它使用 GPT-6 Cyber 模型发现了一个 Java 远程代码执行漏洞，并将其命名为“Java4Shell”；Techmeme 转引《纽约时报》的报道称，Oracle 已发布补丁。"
description: "网络安全初创公司 Calif 声称，它使用 GPT-6 Cyber 模型发现了一个 Java 远程代码执行漏洞，并将其命名为“Java4Shell”；Techmeme 转引《纽约时报》的报道称，Oracle 已发布补丁。"
section: "ai-news"
rank: 210
edition: 2
section_rank: 10
score: 7.0
status: "Released"
source_name: "New York Times"
source_url: "https://www.nytimes.com/2026/11/17/us/politics/ai-security-bug-java.html?unlocked_article_code=1.RFE.J4uR.JL0Qv-280ALN"
via: "Techmeme"
discussion_url: null
published_at: "2026-11-17T21:20:04+00:00"
tags: ["AI security", "vulnerability discovery", "Java", "GPT-6 Cyber", "Oracle patch"]
topics: ["ai-security", "vulnerability-discovery", "java", "gpt-6-cyber", "oracle-patch"]
order: "20261117-2-989"
image: "/assets/stories/2026-11-17/calif-says-gpt-6-cyber-found-java-rce-java4shell-oracle-patches-eb62-share.jpg"
art: "/assets/stories/2026-11-17/calif-says-gpt-6-cyber-found-java-rce-java4shell-oracle-patches-eb62.jpg"
thumb: "/assets/stories/2026-11-17/calif-says-gpt-6-cyber-found-java-rce-java4shell-oracle-patches-eb62-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g379888fa9028ed776fbbbf6a09df2f3a9acfbeb801e5e9e2afeb8e05daaa3c09f44cb53838f94a5aae96417c1618d9d3791ee03a8d2c7caf6e57fb84e94212c5_1280.jpg", "author": "Akela999", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/electrical-data-center-2476783/", "provider": "Pixabay", "width": 4096, "height": 2160}
---

{% raw %}
<div class="story-lead" markdown="1">

网络安全初创公司 Calif 声称，它使用 GPT-6 Cyber 模型发现了一个 Java 远程代码执行漏洞，并将其命名为“Java4Shell”；Techmeme 转引《纽约时报》的报道称，Oracle 已发布补丁。报道称，这项发现展示了 AI 在流行软件中找出严重安全漏洞的能力，但公开摘要未给出受影响版本和完整技术细节。社区讨论称，该利用链对网络时延和抖动敏感、利用条件较具体，同时仍有大量主机可能受影响。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** Oracle 已为这一 Java 远程代码执行漏洞发布补丁，Calif 也公开宣称该漏洞由其 GPT-6 Cyber 模型发现——这两点由《纽约时报》报道、经 Techmeme 摘要转述。此前在 2026 年 10 月，Calif 用 GPT-5.6 Sol 找到的 PHP 漏洞曾有 Wiz 独立复现。
- **尚未证实：** 具体 CVE 编号、受影响 Java 版本与触发漏洞所需条件在现有材料中均未出现；“由 AI 模型发现”目前仍只有 Calif 单方说法，所给材料中没有 Oracle 安全公告或第三方独立验证，本次也没有出现像上次那样的独立复现报道；社区中关于漏洞成因（AVX512 版 Base64 解码）及用 -XX:UseAVX=2 参数规避的说法，发帖者本人已标注为未经证实。

</div>

## 背景

远程代码执行（RCE）指攻击者无需本地权限，就能让目标机器运行自己指定的代码；由于 Java 运行时被大量企业后端系统共用，这类漏洞一旦确认，往往意味着大量主机需要尽快打补丁。AI Daily Radar 11 月 16 日的日报曾报道，谷歌威胁情报团队（TIG）记录了首例攻击者用全自动 AI 框架把已发布补丁反向变成利用代码的事件；此次则是同一类模型能力被用在防守一侧，在补丁发布前先把漏洞找出来。

## 为何重要

运行 Java 服务的企业应把这次补丁纳入漏洞响应：评论者指出，利用条件虽具体，但受影响主机可能很多；Semgrep 的 ievans 称已发布免费检测脚本，用于检查 HotSpot 等五类条件。

## 后续看点

后续可关注 Oracle 安全公告中的 CVE 编号与受影响版本，以及独立研究者能否复现该利用链。

## 社区讨论

评论者称该工作令人印象深刻，但指出利用条件很具体；Semgrep 的 ievans 称已发布检测脚本，覆盖 HotSpot 等五类条件。另有评论转述未经证实的说法，称漏洞与 AVX512 Base64 解码有关，并可通过 -XX:UseAVX=2 参数规避。

## 本事件的相关报道

- 2026-11-17 · calif.io: [Java4Shell: RCE in OpenJDK when processing Base64](https://calif.io/java4shell/)
- 2026-11-17 · New York Times: [Cybersecurity startup Calif says it used GPT-6 Cyber to uncover an RCE flaw in Java dubbed "Java4Shell"; Oracle has released a patch (New York Times)](https://www.nytimes.com/2026/11/17/us/politics/ai-security-bug-java.html?unlocked_article_code=1.RFE.J4uR.JL0Qv-280ALN)

## 延伸阅读

- [2026-11-16 — Google TIG reports first observed autonomous AI patch-to-exploit operation](https://www.techmeme.com/261116/p30#a261116p30)
- [A Major Security Flaw Found Using ChatGPT Is... - Business Insider](https://www.businessinsider.com/php-vulnerability-cybersecurity-ai-patch-openai-gpt-calif-wiz-hacking-2026-10)

{% endraw %}
