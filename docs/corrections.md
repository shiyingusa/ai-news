---
lang: en
title: "Corrections"
description: "Corrections made to AI Daily Radar stories."
permalink: /corrections/
---

# Corrections

When we confirm an error in a story, we fix it, note the change on the story, and list it here. How we handle corrections is described in our [editorial standards]({{ '/standards/' | relative_url }}#corrections).

{% assign items = site.data.corrections | where: "lang", "en" %}
{% if items and items.size > 0 %}
{% for c in items reversed %}
- **{{ c.date }}** · [{{ c.title }}]({{ c.url | relative_url }}): {{ c.note }}
{% endfor %}
{% else %}
No corrections have been published yet.
{% endif %}

To report an error, email [{{ site.contact_email }}](mailto:{{ site.contact_email }}).
