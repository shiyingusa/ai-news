---
layout: story
lang: zh
date: 2026-11-15 06:00:00 -0500
issue: "2026-11-15"
story_id: "lovable-apps-exposed-passport-data-and-200k-private-messages-c8d5"
permalink: "/zh/2026/11/15/lovable-apps-exposed-passport-data-and-200k-private-messages-c8d5/"
title: "Lovable 生成应用被曝泄露护照信息与 20 多万条私信"
dek: "安全研究团队 Crissy Field 发布报告称，用 AI 应用构建工具 Lovable 生成的部分应用暴露了护照信息以及超过 20 万条私人消息，原因是数据库的行级安全（Row-Level Security，RLS…"
section: "ai-news"
rank: 2
section_rank: 2
score: 7.0
status: "Demonstrated"
source_name: "crissyfield.de"
source_url: "https://www.crissyfield.de/research/lovable-en/"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50499017"
published_at: "2026-11-14T17:43:10+00:00"
tags: ["AI app builders", "vibe coding", "security", "data exposure", "Supabase"]
topics: ["ai-app-builders", "vibe-coding", "security", "data-exposure", "supabase"]
order: "20261115-997"
image: "/assets/stories/2026-11-15/lovable-apps-exposed-passport-data-and-200k-private-messages-c8d5-share.jpg"
art: "/assets/stories/2026-11-15/lovable-apps-exposed-passport-data-and-200k-private-messages-c8d5.jpg"
thumb: "/assets/stories/2026-11-15/lovable-apps-exposed-passport-data-and-200k-private-messages-c8d5-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g9d59827fd194b7be3e4060d1ed9342b4be4c962f8a920fcfbf63128dabb6ed28c693981535204d0552b746c68da56731574876f347fb1fb9beb8a55ce0b2ce54_1280.jpg", "author": "cookieone", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/technology-network-storage-industry-8118380/", "provider": "Pixabay", "width": 6016, "height": 4016}
---

{% raw %}
<div class="story-lead" markdown="1">

安全研究团队 Crissy Field 发布报告称，用 AI 应用构建工具 Lovable 生成的部分应用暴露了护照信息以及超过 20 万条私人消息，原因是数据库的行级安全（Row-Level Security，RLS，即让数据库按行判断谁能读写的规则）配置不足。Lovable 安全负责人 igorandri 在讨论中确认，问题根源正是 RLS 配置不足，并表示平台会在每次发布前自动扫描应用、向所有用户免费提供更深入的 SAST（静态应用安全测试）扫描，并支持用户点选“修复”、开启后台自动修复以及拦截发布。报告作者 neathack 证实该文两周前曾提交到 Hacker News 但未获关注，此次重新提交后才引发讨论。现有材料未说明受影响应用的具体数量与泄露数据的完整范围。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** 博客作者在讨论中确认文章由其本人撰写并提交至 Hacker News；Lovable 安全负责人 Igor 在公开回复中承认，涉事应用的根因是行级安全（Row-Level Security，RLS，即数据库按行限制谁能读到哪些数据的规则）配置不足，并表示 Lovable 会在每次发布前自动扫描应用、另提供更深入的 SAST（静态应用安全测试）扫描，两项对所有用户免费，用户可点选“修复”或开启后台自动修复。
- **尚未证实：** 护照信息与“超过 20 万条私信”的具体暴露规模目前仅出自该研究者单方报告，素材中未提供原文正文，Lovable 也未确认受影响应用数量、具体数据类型或是否已通知受影响用户；另有评论者称 Supabase 相关默认设置在 10 月 30 日“据称已修复”，但存在既有项目仍沿用旧默认值的说法，这一时间点与生效范围尚无双方一致的确认。

</div>

## 背景

Supabase 是以 Postgres 为核心的后端服务，应用前端可以直接调用其接口读写数据库；行级安全（Row-Level Security，RLS）是 Postgres 在数据库层按用户或角色限制可访问数据行的机制。Lovable 这类 AI 应用构建器生成的应用常采用前端直连 Supabase 的结构，一旦 RLS 策略缺失或设置过宽，数据库就可能把不同用户的数据暴露给任何能访问该应用的人。

## 为什么重要

对用 Lovable 搭配 Supabase 快速搭建应用的开发者来说，前端直连数据库意味着真正的安全边界只剩 RLS 策略本身，因此上线前应逐表启用 RLS 并核对策略，而不是依靠前端隐藏界面或字段。评论者 SOLAR_FIELDS 指出，Supabase 历史上为降低上手门槛而默认不开启 RLS，这一默认值据称已在 10 月 30 日修复，但有反馈称既有项目仍沿用旧默认——这属于社区说法，官方未在本次材料中确认。

## 社区讨论

评论者 yakkomajuri 表示，让前端直接与 Supabase 后端通信再加 RLS 一直是“雷区”，他更愿意把 Supabase 当作普通 Postgres 从自己的后端连接。SOLAR_FIELDS 认为 Supabase 也应承担责任，因为 RLS 默认关闭是其多年前为简化注册流程而做出的主动取舍，并链接 Supabase 的 GitHub 讨论称修复只对新建项目生效；igorandri 则以 Lovable 安全负责人身份回应，强调扫描与自动修复功能免费开放。

{% endraw %}
