---
layout: story
lang: zh
date: 2026-11-19 06:28:30 -0500
issue: "2026-11-19"
story_id: "ruby2hell-reported-pre-auth-rce-in-stock-rails-7fa0"
permalink: "/zh/2026/11/19/ruby2hell-reported-pre-auth-rce-in-stock-rails-7fa0/"
title: "Ruby2ßhell：Rails 预认证 RCE 源于 ß 转大写"
dek: "Veria Labs 的博客文章声称，未修改的 Ruby on Rails 应用存在一个预认证远程代码执行漏洞；评论者 tptacek 分析称，根源在于 Windows-1252 编码下把 ß 转成大写会变成“SS”、字符串长度加一…"
description: "Veria Labs 的博客文章声称，未修改的 Ruby on Rails 应用存在一个预认证远程代码执行漏洞；评论者 tptacek 分析称，根源在于 Windows-1252 编码下把 ß 转成大写会变成“SS”、字符串长度加一…"
section: "tech-industry"
rank: 11
edition: 0
section_rank: 1
score: 7.0
status: "Announced"
source_name: "verialabs.com"
source_url: "https://verialabs.com/ruby2shell/"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50556287"
published_at: "2026-11-19T05:09:11+00:00"
tags: ["Ruby on Rails", "pre-auth RCE", "vulnerability disclosure", "case conversion", "memory safety"]
topics: ["ruby-on-rails", "pre-auth-rce", "vulnerability-disclosure", "case-conversion", "memory-safety"]
order: "20261119-0-988"
image: "/assets/stories/2026-11-19/ruby2hell-reported-pre-auth-rce-in-stock-rails-7fa0-share.jpg"
art: "/assets/stories/2026-11-19/ruby2hell-reported-pre-auth-rce-in-stock-rails-7fa0.jpg"
thumb: "/assets/stories/2026-11-19/ruby2hell-reported-pre-auth-rce-in-stock-rails-7fa0-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g5fbfb36ee17d6bb86e2877b1f88ee4149eeb53494f2ce44d785333a85abe1f2ffa58e79c1776647d6057bb2bbf3aa3eb460da8a6b6cf98b1e8988017104724a0_1280.jpg", "author": "cookieone", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/technology-network-storage-industry-8118380/", "provider": "Pixabay", "width": 6016, "height": 4016}
---

{% raw %}
<div class="story-lead" markdown="1">

Veria Labs 的博客文章声称，未修改的 Ruby on Rails 应用存在一个预认证远程代码执行漏洞；评论者 tptacek 分析称，根源在于 Windows-1252 编码下把 ß 转成大写会变成“SS”、字符串长度加一，而缓冲区余量检查按单字符进行，可能在末尾留下一个字节的越界写。若利用链成立，攻击者无需登录即可在受影响服务上执行代码；但公开讨论中评论者仍在追问如何把单字节溢出扩展成完整 RCE，完整利用过程尚未在讨论中展示。评论者还指出，该问题与另一条正在讨论的 Ruby 安全公告重叠，后者涵盖另外六个漏洞，因此其独立影响范围仍需确认。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** 据 ORCA Security 与 Cybersecurity News 的报道，Ruby 字符串大小写转换中的堆缓冲区溢出已被分配编号 CVE-2026-132825，代号“ruby2ßhell”；Ruby 核心团队将其评为 critical（严重），并称对特制字符串做大小写转换可能导致远程代码执行，且已知存在能在部分场景触发代码执行的验证性利用（proof-of-concept）；相关修复已发布。
- **尚未证实：** Verial Labs 博文所称“在未改动的原版 Rails 上可预认证远程代码执行”的完整利用链与稳定复现，尚无独立第三方验证；Hacker News 评论者指出该问题已被另一份涵盖另外六个漏洞的 Ruby 安全公告覆盖，本次披露的新增信息有限；补丁的具体版本号、受影响版本范围与发布时间在现有报道中均未明确。

</div>

## 背景

Ruby 官方于 2026 年 11 月 18 日发布安全公告，称在 Ruby 的正则表达式引擎与字符串大小写转换中发现七个漏洞，并表示已知晓部分漏洞的概念验证代码（PoC）；有安全媒体将其概括为其中多个漏洞可能导致远程代码执行。所谓大小写转换的隐患在于，某些字符转成大写后长度会变长——例如德语字母 ß 转成 "SS"——如果代码假定转换前后字节数不变，就可能算错缓冲区大小，这是单字节溢出类漏洞的常见来源。此次引起讨论的 Ruby2ßhell 披露正是围绕这一机制展开，因此有评论者指出它与上述 Ruby 公告存在重叠。

## 为什么重要

对 Rails 运维者而言，预认证意味着攻击面位于登录之前；在补丁和受影响版本明确前，应检查对外服务是否使用相关编码转换路径，并跟踪 Rails/Ruby 官方安全公告，避免仅凭博客标题推断所有版本均受影响。

## 后续看点

Rails 安全团队是否发布官方公告、CVE 编号或补丁版本，以及是否有独立研究者复现完整利用链。

## 社区讨论

有评论者认为，近期 RCE 报告增多，部分原因是 AI 降低了挖掘单字节溢出利用链的成本；但也有人强调，从单字节溢出到 RCE 仍需额外链条，实际可行性待验证。另有评论者指出，该问题与另一条涵盖六个漏洞的 Ruby 公告重叠，可能并非全新问题。

## 本事件的相关报道

- 2026-11-18 · ruby-lang.org: [Multiple vulnerabilities in Regexp and String case conversion](https://www.ruby-lang.org/en/news/2026/11/18/multiple-vulnerabilities-in-regexp-and-string/)
- 2026-11-19 · verialabs.com: [Ruby2ßhell: Pre-authentication RCE on stock Rails](https://verialabs.com/ruby2shell/)

## 延伸阅读

- [Ruby Patches 7 Security Vulnerabilities, Including Buffer ...](https://cybersecuritynews.com/ruby-patches-7-security-vulnerabilities/)
- [Security advisories: multiple vulnerabilities in Regexp and ...](https://www.ruby-lang.org/en/news/2026/11/18/multiple-vulnerabilities-in-regexp-and-string/)
- [ruby2ßhell: Critical One-Byte Heap Overflow in Ruby Could ...](https://cybersecuritynews.com/ruby2shell-rce/)
- [ruby2ßhell: CVE-2026-132825 Ruby Heap Overflow RCE](https://orca.security/resources/blog/ruby2shell-ruby-heap-overflow-rce/)

{% endraw %}
