---
date: 2026-11-14 06:00:00 -0500
layout: "story"
lang: "zh"
issue: "2026-11-14"
story_id: "runway-open-sources-praxis-1-a-robot-controller-built-on-video-trained-1c4e"
permalink: "/zh/2026/11/14/runway-open-sources-praxis-1-a-robot-controller-built-on-video-trained-1c4e/"
title: "Runway 开源机器人模型 Praxis-1，用视频知识驱动机器控制"
dek: "Runway 发布了机器人模型 Praxis-1，同时公开模型权重与源代码，采用 Apache 2.0 许可。"
section: "ai-news"
rank: 4
section_rank: 4
score: 7.0
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
---

{% raw %}
<div class="story-lead" markdown="1">

Runway 发布了机器人模型 Praxis-1，同时公开模型权重与源代码，采用 Apache 2.0 许可。该模型把视频训练中获得的知识迁移到机器人控制任务上，按照 Runway 的说法，它在 Nvidia 的 RoboLab-120 基准的 World Action Model（世界动作模型）类别中排名第一；这一排名属于厂商自述，尚未见到独立复现。目前的限制是，它还不能自行规划复杂的动作序列，因此仍需外部规划器或人工给出任务步骤。

</div>

## 背景：世界动作模型与 RoboLab-120

世界动作模型（world action model）把视频训练中获得的动态知识用于生成机器人动作；与之相邻的 VLA（视觉-语言-动作模型）则直接把视觉输入和语言指令映射为动作。Runway 称 Praxis-1 在 RoboLab-120 上超过所有开权重 VLA；该基准包含 120 项机器人任务，覆盖抓放、堆叠、重排和工具使用等，每项都带语言指令，并通过可组合谓词自动判定成功或失败。另有报道称 Praxis-1 为 270 亿参数、在该基准上的成功率为 46.2%，可作为理解其领先幅度的参照。

## 影响

Apache 2.0 允许开发者修改、再分发并用于商业产品，且无需开源自己的改动，这降低了机器人团队把视频预训练能力接入自有硬件栈的门槛。但由于缺少自主的长程规划能力，实际部署时通常还需要另行搭配任务规划模块，不能把它当作端到端完成复杂作业的方案。

## 延伸阅读

- [Runway Praxis - 1 Is Now Available: Open-Weight Robotics Model](https://runway.com/news/company-news/praxis-1-is-now-available)
- [Runway открыла веса робототехнической модели Praxis - 1 под...](https://devtrends.ru/news/runway-otkryla-vesa-robototexniceskoi-modeli-praxis-1-pod-apache-20)
- [GitHub - meadowshn/ RoboLab _ · GitHub](https://github.com/meadowshn/RoboLab_)

{% endraw %}
