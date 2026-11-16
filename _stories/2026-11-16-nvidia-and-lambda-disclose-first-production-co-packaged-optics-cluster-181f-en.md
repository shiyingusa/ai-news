---
layout: story
lang: en
date: 2026-11-16 06:00:00 -0500
issue: "2026-11-16"
story_id: "nvidia-and-lambda-disclose-first-production-co-packaged-optics-cluster-181f"
permalink: "/2026/11/16/nvidia-and-lambda-disclose-first-production-co-packaged-optics-cluster-181f/"
title: "NVIDIA and Lambda disclose first production co-packaged optics cluster"
dek: "NVIDIA and Lambda disclosed what the report calls the first production co-packaged optics (CPO) cluster, with Lambda saying it has CPO deployed in a cluster of more than 10,000 GPUs."
description: "NVIDIA and Lambda disclosed what the report calls the first production co-packaged optics (CPO) cluster, with Lambda saying it has CPO deployed in a cluster of more than 10,000 GPUs."
section: "chips-compute"
rank: 207
edition: 2
section_rank: 1
score: 8.0
status: "Released"
source_name: "ServeTheHome"
source_url: "https://www.servethehome.com/nvidia-and-lambda-disclose-first-production-co-packaged-optics-cluster-it-is-finally-real/"
via: null
discussion_url: null
published_at: "2026-11-16T21:24:47+00:00"
tags: ["co-packaged optics", "NVIDIA", "Lambda", "AI data centers", "networking"]
topics: ["co-packaged-optics", "nvidia", "lambda", "ai-data-centers", "networking"]
order: "20261116-2-992"
image: "/assets/stories/2026-11-16/nvidia-and-lambda-disclose-first-production-co-packaged-optics-cluster-181f-share.jpg"
art: "/assets/stories/2026-11-16/nvidia-and-lambda-disclose-first-production-co-packaged-optics-cluster-181f.jpg"
thumb: "/assets/stories/2026-11-16/nvidia-and-lambda-disclose-first-production-co-packaged-optics-cluster-181f-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g5742ff3a01a0edf2aa7896a2bc86d503a459baf4cdfca6e6c4af185839d396a52c9c800c69b3614bbc75714483d066bd5340c59c2508b048cab5c491d00496f9_1280.jpg", "author": "Lucent_Designs_dinoson20", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/fiber-cable-wire-connection-4814456/", "provider": "Pixabay", "width": 5184, "height": 3456}
---

{% raw %}
<div class="story-lead" markdown="1">

NVIDIA and Lambda disclosed what the report calls the first production co-packaged optics (CPO) cluster, with Lambda saying it has CPO deployed in a cluster of more than 10,000 GPUs. The report does not specify which NVIDIA switch or GPU models are used, the optical port speeds, or when the deployment became operational. The claim rests on Lambda's disclosure; no independent measurement or third-party verification is included.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** Lambda disclosed on November 16 that it has deployed NVIDIA Photonics co-packaged optics (CPO — optics moved inside the switch package rather than in pluggable modules) connecting more than 10,000 Blackwell Ultra GPUs at its Québec campus, as reported by Converge Digest and ServeTheHome.
- **Not yet confirmed:** That this is the world's first production CPO cluster at this scale rests on Lambda's own disclosure and the absence of comparable announcements from other operators, not on independent verification. The sources also give no port counts, bandwidth or error-rate figures, no comparison against pluggable-optics deployments, and no third-party test of the cluster's operation.

</div>

## Background

Co-packaged optics (CPO) moves the optical transceivers that convert electrical signals to light out of pluggable modules at the face of a switch and onto the same package as the switch chip itself. Shortening that electrical path is meant to cut the power and signal loss of linking thousands of GPUs across a cluster, which is why CPO has been treated as a next step for AI data-center networking rather than an off-the-shelf option. Lambda, the operator of this cluster, rents GPU compute to outside customers. The report does not say which NVIDIA switch or optics components were used, how the optics are cooled or serviced, or how the deployment was verified beyond Lambda's own disclosure.

## Why it matters

Lambda’s disclosure gives AI cloud operators a named production reference for co-packaged optics rather than only a lab demo or roadmap. Because NVIDIA had said CPO-based switching would reach its Quantum-X InfiniBand platforms starting in early 2026, prospective buyers should press both companies on which switch hardware, optical-engine supplier and measured power savings are actually behind the 10,000-plus-GPU deployment before treating CPO as a deployable option.

## Further reading

- [NVIDIA and Lambda Disclose First Production Co-Packaged ...](https://www.servethehome.com/nvidia-and-lambda-disclose-first-production-co-packaged-optics-cluster-it-is-finally-real/)
- [Lambda Deploys NVIDIA Co-Packaged Optics for 10,000 ...](https://convergedigest.com/lambda-nvidia-cpo-10000-blackwell-ultra-gpus/)
- [Nvidia outlines plans for using light for communication between AI ...](https://www.tomshardware.com/networking/nvidia-outlines-plans-for-using-light-for-communication-between-ai-gpus-by-2026-silicon-photonics-and-co-packaged-optics-may-become-mandatory-for-next-gen-ai-data-centers)

{% endraw %}
