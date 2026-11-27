---
date: 2026-11-14 06:00:00 -0500
layout: "story"
lang: "en"
issue: "2026-11-14"
story_id: "ggml-the-tensor-library-under-llama-cpp-reaches-v1-0-0-6c41"
permalink: "/2026/11/14/ggml-the-tensor-library-under-llama-cpp-reaches-v1-0-0-6c41/"
title: "GGML, the tensor library under llama.cpp, reaches v1.0.0"
dek: "GGML, the open-source C tensor library that sits underneath llama.cpp and many other local-inference tools, has tagged version 1.0.0 — its first 1.x release."
section: "ai-news"
rank: 1
section_rank: 1
score: 8.0
status: "Released"
updated: "2026-11-15"
source_name: "GitHub"
source_url: "https://github.com/ggml-org/ggml/releases/tag/v1.0.0"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50493062"
published_at: null
tags: ["open-source AI", "local inference", "llama.cpp", "GGML", "model runtime"]
topics: ["open-source-ai", "local-inference", "llama-cpp", "ggml", "model-runtime"]
order: "20261114-998"
image: "/assets/stories/2026-11-14/ggml-the-tensor-library-under-llama-cpp-reaches-v1-0-0-6c41-share.jpg"
art: "/assets/stories/2026-11-14/ggml-the-tensor-library-under-llama-cpp-reaches-v1-0-0-6c41.jpg"
thumb: "/assets/stories/2026-11-14/ggml-the-tensor-library-under-llama-cpp-reaches-v1-0-0-6c41-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g67fb18791f507108591ce73165a86cf68105975b320ca9dee091b5280e33b195a76bcf56164c19e992c6cc5f3bbfd38845f3eeecf362e35b8984ee8bdfe716ea_1280.jpg", "author": "blickpixel", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/it-server-server-cabinet-network-838379/", "provider": "Pixabay", "width": 3095, "height": 2063}
description: "GGML, the open-source C tensor library that sits underneath llama.cpp and many other local-inference tools, has tagged version 1.0.0 — its first 1.x release."
---

{% raw %}
<p class="correction-note"><strong>Correction, Nov 15, 2026:</strong> An earlier version of this summary said no release notes were available, which contradicted the background section, and attributed a memory-offloading feature for MoE models to this release based only on user comments. The summary now reflects the published release notes and labels user reports as such.</p>
<div class="story-lead" markdown="1">

GGML, the open-source C tensor library that sits underneath llama.cpp and many other local-inference tools, has tagged version 1.0.0, its first 1.x release, on GitHub. Release coverage and a SourceForge mirror of the release notes describe the tag as the project's move to formal semantic versioning, with deprecated public APIs and legacy DIAG_MASK operators removed and FP8 support and configurable YaRN truncation added; we could not confirm those notes against the GitHub release page itself.

Users in the discussion describe steady gains rather than a single leap, with one reporting 5 to 10 percent speed improvements from monthly upgrades.

</div>

## Background

GGML is the C tensor library that supplies the low-level math kernels and hardware backends that llama.cpp and other local-inference tools call to run models. Release coverage reports that the v1.0.0 tag arrives about three and a half years after the project's inception and marks its move to formal semantic versioning, while the release notes listed on a SourceForge mirror describe pruning the deprecated public API and legacy DIAG_MASK operators alongside new FP8 support and configurable YaRN truncation.

## What changes for local inference

Users report that for builders whose mixture-of-experts model slightly exceeds VRAM, keeping less-used experts in host memory (a feature they discuss alongside this release, not one the release notes list) means the model loads and runs instead of failing — but the payoff is conditional: it depends on expert weights sitting in pinned host memory (Windows pinning limits can stop the cache from activating), on PCIe bandwidth, and on having enough cache slots to avoid thrashing, and an independent test on a PCIe 3.0 system found it roughly tied with the merged cache. Because ggml reaches hardware through dedicated backends, users on non-CUDA cards, such as Vulkan-only AMD GPUs, remain covered by the same release.

## Further reading

- [ggml - Browse /v1.0.0 at SourceForge.net](https://sourceforge.net/projects/ggml.mirror/files/v1.0.0/)
- [ggml-org Releases llama.cpp v1.0.0 and ggml v1.0.0 with ...](https://af.net/realtime/ggml-org-releases-llama-cpp-v1-0-0-and-ggml-v1-0-0-with-strict-semantic-versioning/)
- [llama . cpp Just Made Huge MoE Models 4× Faster - YouTube](https://www.youtube.com/watch?v=ohp15NcKDhA)
- [llama . cpp v 1 . 0 . 0 : A stronger foundation for the local AI ecosystem](https://huggingface.co/blog/ggml-org/llama-cpp-v1)

<div class="community" markdown="1">

## Community discussion: opinion, not evidence

Commenters frame the project as the quiet infrastructure of local AI: one user reports that a 50K-token prompt benchmark improved from 4:22 to 3:59 after upgrading, attributing much of the gain to faster prefill with the remainder in token generation, while another praises that GGML-based software remains usable on an older AMD card limited to Vulkan. A third user highlights the practical memory behavior for MoE models that slightly exceed GPU capacity, describing expert offloading to host memory as a load-saving fallback rather than a guarantee of speed.

</div>

{% endraw %}
