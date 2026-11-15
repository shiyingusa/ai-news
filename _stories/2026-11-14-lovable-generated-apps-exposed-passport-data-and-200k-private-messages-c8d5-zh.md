---
date: 2026-11-14 06:00:00 -0500
layout: "story"
lang: "zh"
issue: "2026-11-14"
story_id: "lovable-generated-apps-exposed-passport-data-and-200k-private-messages-c8d5"
permalink: "/zh/2026/11/14/lovable-generated-apps-exposed-passport-data-and-200k-private-messages-c8d5/"
title: "Lovable 生成应用暴露护照信息与逾 20 万条私信"
dek: "安全研究称，大量由 AI 应用生成器 Lovable 生成的网站通过随前端公开的只读 API 密钥，以及 Supabase（常用后端数据库服务）的宽松默认配置，暴露了护照信息和超过 20 万条私信等敏感数据。"
section: "ai-news"
rank: 2
section_rank: 2
score: 7.0
source_name: "Hacker News · armcat"
source_url: "https://www.crissyfield.de/research/lovable-en/"
discussion_url: "https://news.ycombinator.com/item?id=50499017"
published_at: null
tags: ["AI app builders", "security vulnerability", "Lovable", "Supabase", "data exposure"]
topics: ["ai-app-builders", "security-vulnerability", "lovable", "supabase", "data-exposure"]
order: "20261114-997"
image: "/assets/stories/2026-11-14/lovable-generated-apps-exposed-passport-data-and-200k-private-messages-c8d5-share.jpg"
art: "/assets/stories/2026-11-14/lovable-generated-apps-exposed-passport-data-and-200k-private-messages-c8d5.jpg"
thumb: "/assets/stories/2026-11-14/lovable-generated-apps-exposed-passport-data-and-200k-private-messages-c8d5-640.jpg"
photo_credit: {"url": "https://thumb.wikimedia.org/wikipedia/commons/thumb/9/94/Temporary_Slovak_passport_issued_in_1940_to_a_Jewish_refugee_family.jpg/1920px-Temporary_Slovak_passport_issued_in_1940_to_a_Jewish_refugee_family.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail", "author": "Government of Slovakia", "licence": "Public domain", "licence_url": "https://creativecommons.org/licenses/", "source_url": "https://commons.wikimedia.org/wiki/File:Temporary_Slovak_passport_issued_in_1940_to_a_Jewish_refugee_family.jpg", "provider": "Wikimedia Commons", "width": 2393, "height": 1786}
---

{% raw %}
<div class="story-lead" markdown="1">

安全研究称，大量由 AI 应用生成器 Lovable 生成的网站通过随前端公开的只读 API 密钥，以及 Supabase（常用后端数据库服务）的宽松默认配置，暴露了护照信息和超过 20 万条私信等敏感数据。问题影响使用这类工具的开发者：即使没有主动编写攻击代码，默认设置也可能让数据库可被公开读取；根因部分在平台配置，而非模型能力。现有材料未给出受影响应用的确切数量，也未说明 Lovable 或 Supabase 是否已作出回应。

</div>

## 背景

Lovable 是一个用自然语言生成 Web 应用的 AI 构建器，常把后端数据库和登录功能接到 Supabase。Lovable 的文档明确提醒，若多个项目共用同一个 Supabase 项目，密钥（包括 LOVABLE_API_KEY）会互相覆盖，相关功能会失效——这说明生成应用的后端配置与密钥管理本就是容易出错的环节。

## 对使用者的直接影响

对用 Lovable 搭配 Supabase 搭建应用的开发者来说，关键结论是：前端打包的 anon key 按设计就是公开的，因此数据是否可被读取，取决于数据库的行级安全（RLS）策略，而不取决于这把 key 本身是否被发现。Supabase 社区讨论也指出，在默认设置下，匿名用户很容易直接探测 API（服务端仍要求携带有效 JWT），所以上线前应逐表确认 RLS 已启用，并把可读范围收窄到必要字段和行，而不能只靠把 key 从代码里藏起来。

## 社区讨论

评论区的核心分歧在于这算不算“入侵”：有读者认为数据既然随只读密钥公开，问题在发布方而非读取者；也有人认为 Supabase 长期宽松的默认配置应承担部分责任，且 AI 生成应用让普通用户更难判断风险。

## 延伸阅读

- [Connect to Supabase - Lovable Documentation](https://docs.lovable.dev/integrations/supabase)
- [Option to disable anon key access to database · supabase ...](https://github.com/orgs/supabase/discussions/4547)

{% endraw %}
