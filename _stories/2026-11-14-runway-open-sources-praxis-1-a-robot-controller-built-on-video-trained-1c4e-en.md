---
date: 2026-11-14 06:00:00 -0500
layout: "story"
lang: "en"
issue: "2026-11-14"
story_id: "runway-open-sources-praxis-1-a-robot-controller-built-on-video-trained-1c4e"
permalink: "/2026/11/14/runway-open-sources-praxis-1-a-robot-controller-built-on-video-trained-1c4e/"
title: "Runway open-sources Praxis-1, a robot controller built on video-trained models"
dek: "Runway released Praxis-1, a robotics model published with open weights and source code under the Apache 2.0 license, which the company says adapts knowledge learned from video training into robot control."
section: "ai-news"
rank: 4
section_rank: 4
score: 7.0
status: "Released"
source_name: "The Decoder"
source_url: "https://the-decoder.com/runways-open-source-praxis-1-turns-video-ai-into-a-robot-controller/"
discussion_url: null
published_at: null
tags: ["Runway", "Praxis-1", "open-source AI", "robotics", "video models"]
topics: ["runway", "praxis-1", "open-source-ai", "robotics", "video-models"]
order: "20261114-995"
image: "/assets/stories/2026-11-14/runway-open-sources-praxis-1-a-robot-controller-built-on-video-trained-1c4e-share.jpg"
art: "/assets/stories/2026-11-14/runway-open-sources-praxis-1-a-robot-controller-built-on-video-trained-1c4e.jpg"
thumb: "/assets/stories/2026-11-14/runway-open-sources-praxis-1-a-robot-controller-built-on-video-trained-1c4e-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g61eeec6b493560003ba42173f02e5aa498f5eb4a036de01430680e7f5d1563b1164608733825b6a56445f3ffd20c5fe243686c3c3fa835ba1ab84e4e0463c984_1280.png", "author": "kalhh", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/robotic-arm-mechanics-technology-2658318/", "provider": "Pixabay", "width": 2560, "height": 1600}
description: "Runway released Praxis-1, a robotics model published with open weights and source code under the Apache 2.0 license, which the company says adapts knowledge learned from video training into robot control."
---

{% raw %}
<div class="story-lead" markdown="1">

Runway released Praxis-1, a robotics model published with open weights and source code under the Apache 2.0 license, which the company says adapts knowledge learned from video training into robot control. According to the report, Praxis-1 leads the World Action Model category on Nvidia's RoboLab-120 benchmark. The stated limitation is that the model cannot yet plan complex action sequences on its own, so it acts as a controller rather than an autonomous task planner. The Decoder's coverage is brief and the benchmark placement is attributed to the release rather than described as an independent evaluation.

</div>

## What a world action model is

Praxis-1 belongs to a category Runway calls "world action models" (WAMs), which learn control from video rather than only from paired robot-action recordings; Runway says it is the top-performing WAM on Nvidia's RoboLab-120 leaderboard and beats every open-weight vision-language-action (VLA) model, the competing family that maps camera images plus text instructions directly to motor commands. RoboLab-120, the benchmark behind that claim, is an Nvidia set of 120 tasks spanning pick-and-place, stacking, rearrangement and tool use, each with language instructions and automated success/failure detection. A secondary report puts the released model at 27 billion parameters with a 46.2% success rate on that benchmark.

## Impact

Because Praxis-1 ships under Apache 2.0 with both weights and source code, developers can inspect, modify, and deploy it without copyleft obligations or a vendor API, which matters for teams that need on-premise or custom robot stacks. The acknowledged lack of independent multi-step planning means users would still need to supply a higher-level planner or scripted task decomposition to drive it through longer sequences.

## Further reading

- [Runway Praxis - 1 Is Now Available: Open-Weight Robotics Model](https://runway.com/news/company-news/praxis-1-is-now-available)
- [Runway открыла веса робототехнической модели Praxis - 1 под...](https://devtrends.ru/news/runway-otkryla-vesa-robototexniceskoi-modeli-praxis-1-pod-apache-20)
- [GitHub - meadowshn/ RoboLab _ · GitHub](https://github.com/meadowshn/RoboLab_)

{% endraw %}
