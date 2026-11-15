---
lang: zh
title: "更正记录"
description: "AI 每日雷达稿件的更正记录。"
permalink: /zh/corrections/
---

# 更正记录

稿件中的错误一经确认，我们会更正原文、在稿件上注明，并列在这里。更正规则见[编辑标准]({{ '/zh/standards/' | relative_url }}#corrections)。

{% assign items = site.data.corrections | where: "lang", "zh" %}
{% if items and items.size > 0 %}
{% for c in items reversed %}
- **{{ c.date }}** · [{{ c.title }}]({{ c.url | relative_url }})：{{ c.note }}
{% endfor %}
{% else %}
目前还没有发布过更正。
{% endif %}

报告错误，请发邮件到 [{{ site.contact_email }}](mailto:{{ site.contact_email }})。
