---
layout: issue
permalink: /zh/briefing/2026-11-24/
title: "AI 新闻简报：2026年11月24日"
date: 2026-11-24
lang: zh
---

> 过去一天共筛查 296 条科技资讯，留下最值得读的 12 条。

---

**人工智能**
1. [NariQ 发布 Qwen3.8-27B 低比特量化，10 GB 文件声称接近 BF16](#item-ai-news-1) ⭐️ 7.0/10
2. [Google AI 模式接入 Drive、Wallet 与 Gemini 应用](#item-ai-news-2) ⭐️ 7.0/10
3. [Meta 在英国向成年人推出个人 AI 代理 Muse](#item-ai-news-3) ⭐️ 7.0/10
4. [AWS 推出 Strands Decider v2：五个基于 Gemma 4 的开放决策模型](#item-ai-news-4) ⭐️ 7.0/10

**芯片与算力**
1. [美国将阿里巴巴新加坡子公司 Apex 与 Megaspeed 列入实体清单](#item-chips-compute-1) ⭐️ 7.0/10

**电动车与新能源**
1. [大众 ID. Polo 与 Cupra Raval 供不应求，部分等待近两年](#item-ev-energy-1) ⭐️ 7.0/10
2. [ACEA：欧盟 10 月纯电动车占乘用车市场近 30%](#item-ev-energy-2) ⭐️ 7.0/10
3. [研究：日本住宅光伏使高温相关超额死亡年降约 8%](#item-ev-energy-3) ⭐️ 7.0/10

**科技产业与政策**
1. [消息称 SpaceX 与特斯拉洽谈 3.5 万亿美元全股票合并，《金融时报》报道](#item-tech-industry-1) ⭐️ 8.0/10
2. [消息人士：谷歌因以色列施压撤回谷歌地图约旦河西岸关键改动](#item-tech-industry-2) ⭐️ 7.0/10
3. [两个未设防数据库泄露 35 亿条用户名、密码与文件](#item-tech-industry-3) ⭐️ 7.0/10
4. [Ladybird 自研浏览器引擎开启 alpha 测试](#item-tech-industry-4) ⭐️ 7.0/10

---

## 人工智能

<a id="item-ai-news-1"></a>
### [NariQ 发布 Qwen3.8-27B 低比特量化，10 GB 文件声称接近 BF16](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF) ⭐️ 7.0/10

NariQ 在 Hugging Face 发布了 Qwen3.8-27B 的 3 比特及更低比特量化版本（GGUF 格式），文件约 10 GB，作者称其在智能体任务、数学、多语言推理和图像理解上保持接近 BF16 的质量，并称这是首个在长程智能体任务上保持 BF16 水平性能的 3 比特及以下量化。作者自报的对比数据（BF16 / 3-bit / 2.5-bit / 2-bit）为：DeepSWE 39.8 / 41.0 / 41.9 / 28.6，Terminal-Bench 2.1 62.6 / 63.8 / 60.2 / 52.4，AIME 25+26 97.7 / 98.3 / 96.5 / 86.0，MSGM 94.0 / 93.1 / 91.8 / 90.6，RealWorldQA 82.4 / 82.4 / 81.3 / 80.9——在多数项目上 3-bit 与 2.5-bit 与 BF16 持平甚至略高，但 2-bit 在 DeepSWE 和 AIME 上明显下降。作者称在 RTX PRO 6000 上解码速度与其他量化相当，并给出了 4K/16K/64K 上下文下的速度数值（如 64K 时 3-bit 为 70.7、2.5-bit 为 77.5、2-bit 为 85.0，对比 Unsloth UD-IQ3\_XXS 的 74.8）。运行这些模型目前需要使用作者的 llama.cpp 分支 nari-llama.cpp，而非上游版本；在 M3 Pro（18 GB）上需从源码编译，3.0bpw 文件解码约 3.8 tok/s（2.0bpw 约 4.9 tok/s），作者称远慢于 CUDA，其他 Mac 机型未测试。

Hacker News · toebee · 11月23日 13:42 · [社区讨论](https://news.ycombinator.com/item?id=50611402)

**「已证实与未证实」** 已证实：NariQ 在 Hugging Face 上发布了 Qwen3.8-27B 的 3-bit 及更低比特量化版本，发布页列出了 DeepSWE、Terminal-Bench 2.1、AIME 25+26、MSGM、RealWorldQA 五组基准上 BF16 与 3-bit／2.5-bit／2-bit 的对比数字，并说明目前必须使用其自建的 llama.cpp 分支（nari-llama.cpp）才能运行；模型仓库的提交说明显示 DeepSWE 为三轮平均、在 Docker 环境中逐题统计并给出样本数（tool-3-1）。

尚未证实：“接近 BF16 质量”和“首个在长程 agentic 任务上保持 BF16 水平”的说法均为作者自报，尚无可查的独立第三方复测；发布内容未交代标题所称 10 GB 文件的具体构成、各基准所用的评测框架版本与 held-out 划分，而公开的 Terminal-Bench 排行榜页面当前已是 4.1 版（tool-3-3），与文中 2.1 版成绩不能直接对比；Mac 上约 3.8 tok/s（M3 Pro，3.0bpw）的推理速度仅见于评论者转述的说明，发布正文未给出。

**「背景」** 量化（quantization）是把模型权重用更低的位数存储，以换取更小显存占用和更快速度的技术；GGUF 是 llama.cpp 生态常用的量化文件格式，&quot;3-bit&quot;即每个权重约 3 比特。Qwen3.8-27B 若以 BF16（每权重 2 字节）保存约需 54 GB，因此压到 3 比特左右才能装进约 10 GB 的文件、跑在消费级硬件上（tool-2-3）。不过 Nari Labs 的模型卡说明，这批文件需配合其自研的 llama.cpp 分支运行（tool-2-2）。

**「为什么重要」** 对想在本地或单卡上跑 27B 级模型的用户，这些文件把显存/存储门槛压到约 10 GB 量级，代价是必须改用作者的 llama.cpp 分支，意味着无法直接套用上游 llama.cpp 的常规部署流程，也拿不到上游后续的性能与兼容性修复；在 Apple Silicon 上还要自行编译，且实测速度只有个位数 tok/s。

**「后续看点」** 值得留意 nari-llama.cpp 的相关改动是否会进入上游 llama.cpp，以及其他开发者对这些文件在自有工作负载上的独立复现结果，包括与 Bonsai 2 27B 等同类量化的对比。

**「社区讨论」** 有评论者对这类高算力量化训练（QAT 风格）容易过拟合基准数据集表示怀疑，但认为该项目做了少见的基本检验——覆盖多种长程任务并提到使用了“held out”（留出）数据。另有评论者依据作者给出的图表认为，大部分提升来自测试框架（harness）差异而非模型本身；也有人追问压缩过程中究竟损失了什么信息，并关心能否塞进 16 GB 的 Mac。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF">nari-labs/Qwen3.8-27B-NariQ-GGUF · Hugging Face</a></li>
<li><a href="https://aitecharchive.com/articles/nariq-quantization-qwen3-8-27b-agent-performance-10gb">NariQ Quantization: Qwen3.8-27B Agents in a 10 GB File</a></li>
<li><a href="https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF/commit/9065513f08d8ed7dbe50b9c329cac1f40c70fde9">Report three-round DeepSWE averages...</a></li>
<li><a href="https://www.tbench.ai/">TERMINAL - BENCH</a></li>

</ul>
</details>

**标签**: `#quantization`, `#Qwen3.8-27B`, `#local LLMs`, `#llama.cpp`, `#model compression`

---

<a id="item-ai-news-2"></a>
### [Google AI 模式接入 Drive、Wallet 与 Gemini 应用](https://techcrunch.com/2026/11/23/google-searchs-ai-mode-can-now-tap-into-drive-and-wallet-for-more-personalized-responses/) ⭐️ 7.0/10

TechCrunch 11 月 23 日报道，Google 搜索的对话式 AI 模式（AI Mode）现在可以接入 Google Drive、Google Wallet 和 Gemini 应用中的个人数据，通过 AI 模式里的“Personal Intelligence”（个人智能）让回答更个性化。报道称，这是把 Personal Intelligence 扩展到上述服务，但没有说明上线地区、适用账户、授权流程或隐私控制。信息来自单一报道，且没有独立测试；实际会调用哪些数据类型、用户如何关闭连接仍不明确。

TechCrunch AI · 11月23日 19:14

**「已证实与尚未证实」** 已证实：Google 在其官方博客中表示，用户可主动选择加入（opt-in），将 Google Wallet、Drive 和 Gemini 应用接入 AI Mode 的 Personal Intelligence；TechCrunch 报道该消息于周一公布；Android Authority 称 Wallet 支持最先上线，而 Gemini 连接此前本月早些时候已经推出。

尚未证实：报道未说明完整推送时间表、覆盖的国家与地区、哪些账号类型可用，也没有给出隐私与数据处理的具体细节；个性化回答是否准确、是否可靠，目前只有 Google 自己的描述，没有独立测试，报道中也未提及收费是否变化。

**「背景」** Personal Intelligence 是 Google 在搜索 AI Mode 中提供的可选功能：用户主动授权后，AI Mode 的回答可以调用自己 Google 账号里的个人数据，而不是只依赖公开网页。据 Digital Trends 报道，此次 Wallet 接入采用用户主动开启、只读的方式，正在陆续推送；Drive 和 Gemini 应用的接入则要等到未来几周。Google 官方博客同样将这三项接入描述为需要用户自行选择加入（opt-in）。

**「为什么重要」** 对把文档放在 Drive、把信息放在 Wallet 的用户，AI 模式的回答可能开始引用这些账户内容，个人数据进入搜索回答的范围因此扩大；报道没有说明这是否需要用户逐项授权，也没有给出关闭入口，用户应核对账户中的相关设置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/products-and-platforms/products/search/google-search-personal-intelligence-apps/">Tailored Google Search with Personal Intelligence apps</a></li>
<li><a href="https://www.digitaltrends.com/computing/google-is-connecting-wallet-to-ai-mode-in-search-and-drive-and-the-gemini-app-come-next/">Google is connecting Wallet to AI Mode in Search, and Drive ...</a></li>
<li><a href="https://blog.google/products-and-platforms/products/search/google-search-personal-intelligence-apps/">Tailored Google Search with Personal Intelligence apps</a></li>
<li><a href="https://techcrunch.com/2026/11/23/google-searchs-ai-mode-can-now-tap-into-drive-and-wallet-for-more-personalized-responses/">Google Search&#x27;s AI Mode can now tap into Drive and Wallet for ...</a></li>
<li><a href="https://www.androidauthority.com/personal-intelligence-ai-mode-3738563/">Google expands Personal Intelligence in AI Mode for Search</a></li>

</ul>
</details>

**标签**: `#Google AI Mode`, `#personalization`, `#Google Drive`, `#Google Wallet`, `#privacy`

---

<a id="item-ai-news-3"></a>
### [Meta 在英国向成年人推出个人 AI 代理 Muse](https://www.techmeme.com/261124/p4#a261124p4) ⭐️ 7.0/10

据 Politico 报道，Meta 已向英国成年人推出个人 AI 代理 Muse，用于协助处理日常任务。报道称，Meta 是首家在英国推出 AI 代理的大型科技公司；英国监管机构此前已就这类代理发出警告，并将密切关注此次上线。报道未说明 Muse 的具体功能、收费方式，以及是否覆盖英国所有成年人。

Techmeme · 11月24日 07:50

**「已证实与未证实」** 已证实：Politico 报道，Meta 已向英国成年人推出 Muse，并将其描述为首家在英国推出 AI 代理的大型科技公司。
尚未证实：Muse 的具体能力、价格、完整覆盖范围及独立测试结果均未在报道中披露；英国监管机构是否已对 Muse 采取正式行动也尚无消息。

**「背景」** AI 代理（agent）指能代替用户连续执行多步操作、调用其他应用或服务的 AI 系统，而不只是生成对话。AI Daily Radar 11 月 23 日的日报曾报道，沃尔玛的 Agent Gateway 把 Meta 的 Muse 列为首个购物代理，可在 Sparky 助手中搜索并购买黑五商品，并在“Agent Profiles”中设置消费限额、审批购买和查看记录；此次则是 Muse 面向英国成年公众的整体上线。

**「为什么重要」** 对英国成年人而言，Muse 的上线让他们可以使用一家大型科技公司的个人 AI 代理处理日常任务；对监管机构而言，这是英国首个可供实际审视的大厂 AI 代理产品，监管机构将能依据实际产品检验此前的警告是否成立。

**「后续看点」** 英国监管机构是否会就 Muse 上线发表声明、启动正式问询，或发布针对 AI 代理的具体指引。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theverge.com/ai-artificial-intelligence/1039874/walmart-agent-gateway-meta-muse-black-friday">2026-11-23 — Walmart lets Meta&#x27;s Muse agent buy Black Friday deals via Agent Gateway</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#Meta`, `#UK regulation`, `#consumer AI`, `#Big Tech`

---

<a id="item-ai-news-4"></a>
### [AWS 推出 Strands Decider v2：五个基于 Gemma 4 的开放决策模型](https://www.techmeme.com/261123/p55#a261123p55) ⭐️ 7.0/10

AWS 于周一发布 Strands Decider v2，这是一组五个“决策模型”（decision models，即针对智能体中的选择、路由一类判断任务调优的模型），全部基于 Google 的 Gemma 4 构建，参数规模从 2B 到 31B，采用 Apache 2.0 许可。据 The New Stack 记者 Frederic Lardinois 报道，此次发布距离 Strands Labs 的上一次发布仅七周。报道只给出了模型家族的数量、底座、参数区间和许可证，没有披露各尺寸的基准成绩、训练数据，也未说明这些模型在 AWS 自家产品中如何分发或托管。

Techmeme · 11月24日 04:25

**「已证实与未证实」** 已证实：Strands Labs 的博客（tool-3-1）称 Strands Decider v2 是基于 Gemma 4 的五个模型，参数规模从 E2B 到 31B，采用 Apache 2.0 许可，模型权重已发布在 Hugging Face，v2 支持已进入开源的 Strands Decider 仓库；VentureBeat（tool-3-2）和 explainx.ai（tool-3-3）的报道与这一描述一致。据该博客所述，Decider 属于“system one”模型：它不生成文本，而是在一次前向传播中从给定选项里选择，并为每个选项返回一个概率。
尚未证实：模型的决策准确率、概率校准质量与延迟等性能主张目前仅出自公司自己的博客，没有独立评测或第三方复现；各尺寸模型的具体硬件要求、是否通过 AWS 托管服务提供以及定价，均未在报道中说明。

**「背景」** Strands Decider 属于所谓&quot;系统一&quot;（system one）模型：它不做长篇推理，而是针对需要快速、反射式判断的环节，例如智能体（agent）在分叉路口选择下一步走向，并以带校准的概率输出结果。据 The New Stack 报道，这次发布距离 Strands Labs 上一次发布只有七周，v2 是在上一代基础上的迭代版本。它沿用了 Google 的开放模型系列 Gemma 4 作为底座，并延续开源权重路线，把权重放在 Hugging Face 上、在开源 Strands Decider 代码库中提供 v2 支持。

**「为什么重要」** Apache 2.0 允许修改和再分发，因此团队可以把这套模型自托管、微调后嵌入自有产品，而不必依赖按调用量计费的托管 API；2B 到 31B 的尺寸阶梯也让开发者能在延迟敏感的场景选小模型、在复杂判断上选大模型。需要注意的是，报道没有给出任何性能数字，选型前应等待模型卡或独立评测。

**「后续看点」** 关注 AWS 是否公布五个尺寸各自的模型卡与评测结果，以及第三方基准何时把这些“决策模型”与通用小模型做同口径对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://strandsagents.com/blog/introducing-strands-decider-v2/">Introducing Strands Decider v2: open, calibrated system one ...</a></li>
<li><a href="https://explainx.ai/blog/aws-strands-decider-v2-gemma4-november-2026">Strands Decider v2: 5 Open Models (Apache 2.0) | explainx.ai Blog</a></li>
<li><a href="https://strandsagents.com/blog/introducing-strands-decider-v2/">Introducing Strands Decider v2: open, calibrated system one ...</a></li>
<li><a href="https://venturebeat.com/data/awss-strands-decider-v2-targets-the-agent-decisions-that-hinge-on-a-single-detail">AWS&#x27;s Strands Decider v2 targets the agent decisions that ...</a></li>
<li><a href="https://explainx.ai/blog/aws-strands-decider-v2-gemma4-november-2026">Strands Decider v2: 5 Open Models (Apache 2.0) | explainx.ai Blog</a></li>

</ul>
</details>

**标签**: `#AWS`, `#open models`, `#Gemma 4`, `#Apache 2.0`, `#model release`

---

## 芯片与算力

<a id="item-chips-compute-1"></a>
### [美国将阿里巴巴新加坡子公司 Apex 与 Megaspeed 列入实体清单](https://www.techmeme.com/261124/p10#a261124p10) ⭐️ 7.0/10

据彭博报道的一份文件，美国商务部已将阿里巴巴的新加坡子公司 Apex Enterprise Solutions 列入实体清单，同批被列入的还有 Megaspeed 及其五家关联公司。被列入实体清单后，美国供应商向这些实体出口芯片、软件和技术通常需要事先取得商务部许可，但报道没有说明具体的许可审批标准，也没有交代 Apex 的实际业务范围与受影响程度。同一天彭博的另一篇报道称，新加坡总理黄循财表示不希望新加坡被用作规避美国芯片出口管制的通道，当地当局正在调查 Megaspeed 的英伟达芯片采购。

Techmeme · 11月24日 11:10

**「已证实与未证实」** 已证实：依据一份申报文件，美国商务部将阿里巴巴的新加坡子公司 Apex Enterprise Solutions，连同 Megaspeed 及另外五家关联公司，一并列入实体清单；Bloomberg 报道了该消息，《海峡时报》和 kursiv.media 的报道也确认 Apex 在列。
尚未证实：阿里巴巴是否经 Apex 转售受美国出口管制的芯片。阿里巴巴否认相关指控，称 Apex 从未转运受美国出口限制的芯片，并将采取法律措施；新加坡当局正在调查 Megaspeed 采购 Nvidia 芯片一事，目前未提出指控。报道未说明列入清单的具体理由、生效细节及五家关联公司的完整名单。

**「背景」** 实体清单（Entity List）是美国商务部的出口管制名单：被列入的实体若要获得受美国出口管制管辖的物项——包括先进 AI 芯片——必须先申请许可，而清单说明指出这类申请通常按“推定拒绝”原则审查（据 AI Stock Wire 对本次列名的梳理）。这一轮行动有更早的线索：新加坡当局此前正在调查 Megaspeed 的英伟达芯片采购，新加坡总理黄循财于 11 月 24 日表示，不希望新加坡被用作规避美国芯片出口管制的通道。此次 Apex 正是与 Megaspeed 及另外几家实体一同被列入，属于对经新加坡转口渠道审查的延续。

**「为什么重要」** 对与美国有业务往来的供应商来说，向 Apex、Megaspeed 及其五家关联公司出口芯片或技术前，必须先核查清单范围并申请许可，合规审查会直接拖慢相关交付。清单一次覆盖多个关联实体，说明限制并不只针对单一主体；与之有交易的企业需要一并排查交易对手，而不能只看 Apex 一家。

**「后续看点」** 值得关注美国商务部工业与安全局（BIS）在《联邦公报》发布的正式条目，其中会写明各实体的具体许可要求和生效细节；Megaspeed 英伟达芯片采购调查的进展同样值得跟进。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aistockwire.com/blog/alibaba-baba-apex-enterprise-solutions-singapore-entity-list-megaspeed-november-2026">Alibaba&#x27;s Singapore unit Apex added to the US entity list</a></li>
<li><a href="https://finance.biggo.com/news/08efff2b-9db3-42cd-a898-3de9de55df3c">US Adds Alibaba&#x27;s Singapore Unit to Entity List, Alibaba Vows ...</a></li>
<li><a href="https://www.straitstimes.com/world/united-states/us-blacklists-megaspeed-chip-firm-linked-to-nvidia-scandal">US blacklists Megaspeed , Alibaba unit amid Nvidia... | The Straits Times</a></li>
<li><a href="https://uz.kursiv.media/en/2026-11-24/us-blacklist-megaspeed-alice-huang/">US blacklists Megaspeed , once led by China spy suspect Alice Huang</a></li>

</ul>
</details>

**标签**: `#export controls`, `#Entity List`, `#Alibaba`, `#AI compute`, `#US-China tech`

---

## 电动车与新能源

<a id="item-ev-energy-1"></a>
### [大众 ID. Polo 与 Cupra Raval 供不应求，部分等待近两年](https://insideevs.com/news/816560/vw-id-polo-cupra-raval-skoda-epiq-demand-high-wait-times/) ⭐️ 7.0/10

据 InsideEVs 报道，大众集团在西班牙 Martorell 工厂组装的 ID. Polo 和 Cupra Raval 日产量已达 1,000 辆，但仍供不应求：部分车型交付等待接近两年，ID. Polo 有时需等一年多，另外三款同家族车型也需长时间等待。大众计划加快西班牙工厂的扩产，但电池电芯短缺正在拖慢生产。

InsideEVs · 11月24日 08:43

**「已证实与未证实」** 已证实：据 InsideEVs 援引 electrive 的报道，位于西班牙马托雷利的工厂同时组装大众 ID. Polo 与 Cupra Raval，目前日产量约 1,000 辆；报道称大众将加快扩产步伐，同时电池电芯短缺正在拖慢生产。
尚未证实：报道正文只说 ID. Polo 部分客户需等待“一年以上”，标题所称“接近两年”在文中没有给出依据，两处说法并不一致；大众尚未公开确认具体等车时长，也未说明包括斯柯达 Epiq 在内的其余三款车型各自的排期，以及扩产的具体时间表和产能目标。

**「背景」** 大众集团把这条小型电动车产品线放在西班牙马托雷尔的工厂生产，ID. Polo、Cupra Raval 等共四款车型共用该厂的产能，定位是相对平价的电动车。可作对照的是，11 月 23 日的 AI Daily Radar 日报曾报道，大众计划到 2030 年每年从中国出口约 30 万辆汽车，同时推进接近 100 万辆的年产能削减，背景是大众销量下滑、中国品牌的平价电动车正进入西方市场。也就是说，在集团整体收缩产能的同时，这条小型车产品线反而遇到产能吃紧的问题。

**「为什么重要」** 对欧洲下订小型电动车的买家来说，交付周期已成为实际门槛：报道指出 ID. Polo 有时要等一年以上，同平台的另外三款车型同样需要长时间等待，而马丁内尔工厂即便达到日产 1,000 辆仍不足以消化订单。报道给出的关键制约是电池电芯供应短缺，而大众集团旗下电池公司 PowerCo 已将西班牙瓦伦西亚列为三处电芯生产基地之一（另两处为德国萨尔茨吉特和加拿大圣托马斯），这意味着产能扩张的节奏取决于电芯而非整车装配线。打算下单的消费者在下订前应先向经销商确认具体交付时间，而非依赖官方公布的名义产能。

**「后续看点」** 关注 Martorell 工厂扩产后的日产量变化，以及 ID. Polo 等车型的交付等待时间是否缩短。电池电芯短缺能否缓解，将决定扩产能否按计划推进。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://electrek.co/2026/11/23/if-you-cant-beat-em-vw-to-export-300000-chinese-built-cars-per-year-by-2030/">2026-11-23 — VW plans 300,000 China-built car exports a year by 2030</a></li>
<li><a href="https://www.volkswagen-group.com/en/volkswagen-group-sites-17481">Volkswagen Group sites | Volkswagen Group</a></li>

</ul>
</details>

**标签**: `#Volkswagen ID. Polo`, `#Cupra Raval`, `#EV demand`, `#production capacity`, `#wait times`

---

<a id="item-ev-energy-2"></a>
### [ACEA：欧盟 10 月纯电动车占乘用车市场近 30%](https://www.electrive.com/2026/11/24/acea-battery-electric-cars-capture-30-per-cent-of-eu-passenger-car-market/) ⭐️ 7.0/10

欧洲汽车制造商协会（ACEA）的注册数据显示，2026 年 10 月欧盟新注册纯电动乘用车（BEV）约 28 万辆，同比增长 61%，占当月乘用车注册总量的近 30%。据 electrive 报道，欧盟纯电动车单月注册量目前已稳定在 25 万辆以上。这是注册量口径的统计，不含产量或订单数据；报道没有披露当月乘用车市场的总规模、各成员国的拆分情况，也没有给出具体车型的表现。

Electrive · 11月24日 10:30

**「已验证与未确认」** 已验证：据 electrive 援引欧洲汽车制造商协会（ACEA）的数据，10 月欧盟新注册纯电动汽车 28 万辆，同比增长 61%，约占欧盟乘用车市场的 30%。ACEA 是代表欧洲 17 家主要汽车、卡车、厢式车和客车制造商的行业协会。

尚未确认：报道只给出“近 30%”这一约数，未给出精确市场份额，也未给出当月欧盟乘用车总注册量；报道也没有说明该统计范围是否仅限欧盟，而 ACEA 通常把 EFTA 和英国的数据单独列出。上述数字均来自 electrive 对 ACEA 数据的转述，没有直接引用 ACEA 的原始新闻稿加以核对。

**「背景」** ACEA（欧洲汽车制造商协会）每月按动力类型公布欧盟新乘用车注册量，注册数据通常被当作销量代理指标，因为车辆在登记上牌时计数，而非下单时。10 月的 61% 同比增长是与去年同月相比，这一同比口径剔除了季节波动，因此近 30% 的纯电份额反映的是实际渗透水平，而非单月偶发波动。

**「为什么重要」** 单月新增逾 25 万辆纯电动车，意味着公共充电桩与电网接入的需求正以相同量级累积，充电运营商和配电规划者需要按月度新增注册量、而不是年度总量来安排扩容节奏。报道没有提供同期充电桩建设速度的对照数据，因此充电供给能否跟上这一增速，仅凭这组注册数字无法判断。

**「后续看点」** ACEA 下一期月度注册数据将检验近 30%的份额能否延续，还是只是单月波动；同时可关注其年度累计份额的更新，以确认 2026 年全年的水平。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.acea.auto/">ACEA - European Automobile Manufacturers&#x27; Association</a></li>

</ul>
</details>

**标签**: `#EV adoption`, `#EU passenger car market`, `#ACEA data`, `#battery-electric vehicles`, `#market share`

---

<a id="item-ev-energy-3"></a>
### [研究：日本住宅光伏使高温相关超额死亡年降约 8%](https://www.pv-magazine.com/2026/11/24/residential-solar-linked-to-reduced-health-risks-from-extreme-temperatures/) ⭐️ 7.0/10

一项发表于《Social Science &amp; Medicine》的同行评审研究，把日本 2011 年大地震后核电停运、电价最高上涨 38%与全国住宅光伏补贴并行的时期作为自然实验，发现住宅光伏降低了极端高温导致的死亡风险。亚洲成长研究所的 Yi-Chun Ko 与同志社大学的 Shinsuke Uchida 合并 2009 至 2014 年 44 个都道府县的月度死亡率、天气和官方光伏安装数据，并用工具变量法（借助外部冲击分离因果效应）排除其他因素；按研究期内光伏安装的年均增速估算，高温相关超额死亡每年减少约 8.2%，65 岁及以上人群减少约 8.5%。这种保护效应在更温暖的地区、震后电价涨幅更大的地区以及节能目标更严的地区更强，在低温条件下则没有可比效应。作者称这是“首个因果证据”，表明家庭光伏可通过改善能源可负担性发挥公共卫生干预作用；但研究同时指出，光伏普及偏向高收入地区，健康收益可能分配不均。

pv magazine · 11月24日 09:18

**「已证实与未证实」** 已证实：这篇论文题为《Climate resilience through residential solar energy: Reducing health risks from extreme temperatures》，作者为亚洲成长研究所的 Yi-Chun Ko 与日本同志社大学的 Shinsuke Uchida，刊于《Social Science &amp; Medicine》第 410 卷（2026 年），ScienceDirect 与 RePEc 的文献记录均与其一致；研究以 2011 年东日本大地震后核电停运、电价最高上涨 38% 并同期推行住宅光伏补贴为自然实验，将 2009—2014 年 44 个都道府县的月度死亡率数据、天气数据与官方光伏装机数据结合，用工具变量法分离光伏 adopt 的影响，结论是极端高温相关超额死亡年均减少约 8.2%，65 岁及以上人群约 8.5%，低温下未见类似效应。

尚未证实：8.2% 与 8.5% 是作者按研究期内光伏装机年均增速推算的模型估计值，并非实测的死亡人数下降，尚无独立复现或第三方评估；作者所称这是“首个证明户用光伏可作为公共卫生干预手段的因果证据”，属于作者自我评价，未获外部确认；研究结论基于日本特定电价冲击与补贴环境，能否外推到其他市场、其他电价机制尚不清楚；论文也自认光伏 adoption 偏向高收入地区，健康收益分配可能不均，这一点尚无量化数据支撑。

**「背景」** 2011 年东日本大地震后，日本核电站相继停运，电力价格上涨幅度最高达 38%；与此同时，日本通过全国性补贴计划推广住宅光伏。这一电价冲击与补贴推广同时出现的局面，使研究者可以把地震后的时段当作“自然实验”，并借助工具变量方法，将光伏采用带来的影响与收入、气候等其他因素区分开。此前，住宅光伏的评估多集中在减排和电费节省上，其能否通过改善能源可负担性来影响健康，一直缺乏因果层面的证据。

**「为什么重要」** 对政策制定者而言，这项研究提供了把分布式光伏纳入高温适应和公共卫生投入的具体依据：如果补贴按收入水平或高温脆弱性定向设计，就可能同时减轻老年家庭的制冷电费负担并降低热死亡风险。作者警告，若延续目前偏向高收入家庭的普及路径，健康收益会更多流向本已具备适应能力的地区，从而扩大气候相关的健康差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0277953626010105">Climate resilience through residential solar energy: Reducing ...</a></li>
<li><a href="https://ifp.nyu.edu/2026/journal-article-abstracts/s0277953626010105/">Climate resilience through residential solar energy: Reducing ...</a></li>
<li><a href="https://ideas.repec.org/a/eee/socmed/v410y2026ics0277953626010105.html">Climate resilience through residential solar energy: Reducing ...</a></li>

</ul>
</details>

**标签**: `#residential solar`, `#public health`, `#extreme heat`, `#energy affordability`, `#climate resilience`

---

## 科技产业与政策

<a id="item-tech-industry-1"></a>
### [消息称 SpaceX 与特斯拉洽谈 3.5 万亿美元全股票合并，《金融时报》报道](https://www.techmeme.com/261124/p8#a261124p8) ⭐️ 8.0/10

《金融时报》援引未具名消息人士报道，SpaceX 与特斯拉正在洽谈以全股票方式合并，交易规模约 3.5 万亿美元，若达成将是史上最大的并购。报道称，两家公司把这件事交给两个特别委员会共五名董事处理，这些董事被描述为与交易“无利害关系”（disinterested），但都与埃隆·马斯克有关联。这目前只是谈判中的方案，并非已签署的协议，两家公司也未公开确认；报道没有给出时间表、换股比例或委员会成员名单。

Techmeme · 11月24日 10:50

**「已证实与未证实」** 已证实：据《金融时报》报道，SpaceX 与特斯拉已将这笔潜在合并的条款谈判交给五名董事，并力争在年底前完成交易；《纽约时报》2026 年 10 月 21 日的报道称，马斯克本人公开表示两家公司正在探讨合并。

尚未证实：交易能否最终达成、3.5 万亿美元估值、全股票交易结构以及“年底前完成”的时间表，目前仅来自《金融时报》援引的匿名消息人士；两家公司均未公开确认，协议的具体条款、这五名董事为何被视为“无利害关系”以及他们的表决安排也都没有披露。Yahoo Finance 报道的投资者 Gary Black 对潜在股权稀释的批评，同样属于外部评论而非交易细节。

**「背景」** 特斯拉是上市公司，SpaceX 尚未上市；两家公司由同一位首席执行官马斯克掌管，并且他在两家公司都持有大量股份。这类双方共用管理层和控股股东的交易属于关联交易，通常的做法是由不涉及直接利益的独立董事组成特别委员会，负责谈条款和审批，以便在程序上隔离利益冲突。所谓全股票交易，是指不支付现金，而是把 SpaceX 按约定估值折算成特斯拉新发行的股票；若交易达成，这类合并通常还需提交特斯拉股东投票。

**「为什么重要」** 对特斯拉股东而言，真正决定得失的不是报道中的 3.5 万亿美元估值，而是换股比例——它决定原特斯拉股东在合并后公司里占多少股份。SpaceX 未上市、没有市场价格可对照，这一比例将由报道所说的两个特别委员会谈定，而五位把关董事都与马斯克有关联，股东能获得多少独立制衡因此存疑；交易若推进，最终仍需特斯拉股东表决。

**「后续看点」** 值得关注的是特斯拉是否就此向美国证券交易委员会提交文件、或两家公司正式确认谈判，以及两个特别委员会的具体成员与投票安排是否公开。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ft.com/content/2585e45e-9133-4215-a2d8-e1275e1033b9?syn-25a6b1a6=1">SpaceX - Tesla : the directors negotiating the biggest merger ever</a></li>
<li><a href="https://www.nytimes.com/2026/10/21/business/elon-musk-spacex-tesla-merger.html">Elon Musk Says SpaceX and Tesla Are Exploring a Merger - The New...</a></li>
<li><a href="https://finance.yahoo.com/markets/stocks/articles/tesla-bulls-could-burned-gary-223005762.html">Tesla Bulls Could Get Burned? Gary Black Sees Trouble With SpaceX ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Elon_Musk">Elon Musk - Wikipedia</a></li>
<li><a href="https://www.nytimes.com/2026/10/21/business/elon-musk-spacex-tesla-merger.html">Elon Musk Says SpaceX and Tesla Are Exploring a Merger - The New...</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#Tesla`, `#Elon Musk`, `#mergers and acquisitions`, `#corporate governance`

---

<a id="item-tech-industry-2"></a>
### [消息人士：谷歌因以色列施压撤回谷歌地图约旦河西岸关键改动](https://www.techmeme.com/261123/p53#a261123p53) ⭐️ 7.0/10

《连线》（Wired）报道称，据匿名消息人士透露，一名谷歌产品经理多年致力于改善谷歌地图对约旦河西岸巴勒斯坦人的服务，重点是把以色列检查站准确标注在这款全球最常用的导航应用上；但谷歌后来在以色列方面施压后撤回了其中关键部分。报道没有说明哪些改动曾实际上线、哪些被删除，也没有给出施压的具体形式或时间。报道同样未包含谷歌的回应。上述核心说法目前仅来自匿名消息人士，谷歌方面尚未公开确认。

Techmeme · 11月24日 04:00

**「已证实与未证实」** 已证实：Wired 发表了这项调查，报道援引匿名消息人士称，一名谷歌产品经理多年推动在谷歌地图上准确标注约旦河西岸的以色列检查站，公司后来撤销了其中关键部分；Wired 在 2024 年 12 月也曾报道，巴勒斯坦居民长期抱怨当地地图数据缺失或过时，导致出行困难。
尚未证实：目前可见的报道摘要未提及谷歌的回应或官方说法；具体哪些改动曾上线、何时被撤销、以及撤销是否确因以色列方面施压，都只出自匿名消息源，尚无独立证实。

**「背景」** Google 地图在约旦河西岸等争议地区的道路、地名与边界如何显示，长期由公司内部的标注政策决定；其数据来源混合了商业采购的地图数据、卫星影像和用户贡献的修改，因此单一区域的改动往往需要产品、法务与公共政策团队共同审核。据 Wired 报道，一名 Google 产品经理用数年时间试图把以色列在西岸设置的检查站准确画进这款全球使用最广的导航应用中，因为这些实体路障直接决定巴勒斯坦居民的通行路线；报道称，公司在以色列方面施压后撤回了其中关键部分。

**「为什么重要」** 如果报道属实，直接影响的是依赖谷歌地图在约旦河西岸出行的用户：检查站位置是否标注、标注得多细，决定了导航路线能否反映实际通行限制，被撤回的数据会让这类路况信息重新变得不完整。对这些用户而言，更稳妥的做法是把谷歌地图的结果与当地实时路况信息交叉核对，而不是把它当作唯一依据。

**「后续看点」** 接下来值得关注谷歌是否就《连线》的报道作出公开回应，以及被指撤回的检查站数据是否会出现任何恢复或更正。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.wired.com/story/inside-googles-failure-to-make-google-maps-work-for-palestinians/">Inside Google’s Failure to Make Google Maps Work for ...</a></li>
<li><a href="https://www.wired.com/story/google-maps-west-bank/">How Google Maps Makes It Harder for Palestinians to ... - WIRED</a></li>

</ul>
</details>

**标签**: `#google-maps`, `#platform-policy`, `#censorship`, `#west-bank`, `#investigative-reporting`

---

<a id="item-tech-industry-3"></a>
### [两个未设防数据库泄露 35 亿条用户名、密码与文件](https://www.wired.com/story/3-billion-usernames-passwords-and-documents-leaked-online/) ⭐️ 7.0/10

据《连线》（WIRED）报道，两个未设置访问保护的数据库在网上暴露，涉及约 35 亿条用户名、密码和文件，受影响人数达数亿。报道称，这些数据足以让攻击者“接管”受害者的数字生活——即利用同一套账号密码登录其他服务。报道未点名涉事公司或数据来源平台，也未说明数据库目前是否已被关闭、是否已通知受影响用户。

Wired · 11月24日 11:00

**「已证实与未证实」** 已证实：《连线》（WIRED）报道称，两个未设防护的数据库暴露了数亿人的敏感信息，其中包含可让攻击者“接管”受害者数字生活的数据；文章标题给出的规模是 35 亿条用户名、密码和文档记录，与正文“数亿人受影响”并不矛盾（记录数远多于人数）。

尚未证实：数据库归谁所有、涉及哪些公司或服务、数据是否真实且非重复、数据库目前是否仍在线、是否已通知监管机构或受影响用户，以及是否有独立安全机构复核过这批数据；报道摘录未说明发现者和发现方式，35 亿这一数字目前仅出自该报道。

**「背景」** 所谓“未设防数据库”，通常指没有开启身份验证、可从公网直接访问的数据库或存储服务；任何人只要知道地址就能读取其中内容，无需攻破任何系统。这类暴露在数据泄露事件中反复出现，维基百科的泄露事件清单只收录 3 万条记录以上的案例，而此次两起互不相关的数据库合计暴露了超过 35 亿条用户名、密码、身份证件号码和文档。

**「为什么重要」** 由于报道没有披露涉事服务名称，受影响用户无法针对性修改密码，实际可采取的做法是对所有重复使用同一密码的账号统一更换密码，并为邮箱、支付等关键账号开启双因素认证；对企业而言，这一事件再次说明未加认证的数据库一旦可公网访问，暴露规模会迅速放大到数亿人级别。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/List_of_data_breaches">List of data breaches - Wikipedia</a></li>
<li><a href="https://imtr.net/article/database-leaks-expose-35-billion-usernames-passwords-and-documents-5900">Database Leaks Expose 3.5 Billion Usernames, Passwords, and ...</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#data breach`, `#privacy`, `#credentials`, `#unsecured databases`

---

<a id="item-tech-industry-4"></a>
### [Ladybird 自研浏览器引擎开启 alpha 测试](https://www.theverge.com/tech/1040872/ladybird-indie-browser-engine-alpha-testing) ⭐️ 7.0/10

开发者 Andreas Kling 于周一宣布，采用从零编写引擎的独立浏览器 Ladybird 已在 macOS 和 Linux 上进入 alpha 测试阶段，此前项目已开发四年多。当前主流浏览器基本依赖三个引擎——Gecko（Firefox）、Blink（Chrome）和 WebKit（Safari），Ladybird 因此成为多年来首个带着全新引擎面世的项目。alpha 属于早期测试版本，Windows 版本要等到项目的“后期阶段”才会推出。

The Verge · 11月23日 22:38

**「已证实与未证实」** 已证实：Kling 在 ladybird.org 发布公告，宣布 alpha 版面向 macOS 与 Linux 推出，项目已开发四年多（据 The Verge 报道）。
尚未证实：稳定性、网页兼容性与性能均无第三方测试数据；Windows 版本仅表示在“后期阶段”推出，没有日期；报道也未说明具体获取方式与硬件要求。

**「背景」** 目前主流浏览器几乎都建立在三个引擎之上：Mozilla Firefox 使用的 Gecko（2000 年随 Netscape 6 出现）、苹果 Safari 使用的 WebKit（2003 年由 KDE 的 KHTML 分支而来），以及谷歌此后从 WebKit 分叉出的 Blink。Ladybird 的官方公告强调其引擎“完全从零构建、并非分支”，这也是它被视为多年来首个全新浏览器引擎的原因。据维基百科条目，Linux 与 macOS 是 2026 年 alpha 版和计划中 2027 年 beta 版的开发目标，原生 Windows 版本并非优先事项，官方也称 alpha 版面向“不介意 bug、愿意帮忙报告问题”的早期用户。

**「为什么重要」** 对网页开发者和愿意尝鲜的用户来说，这是少数可以亲手验证一个非 Blink/WebKit/Gecko 引擎渲染与兼容性表现的机会；但 alpha 意味着功能不全、稳定性未知，不适合作为日常浏览器，而 Windows 用户目前完全用不上。

**「后续看点」** 留意 Ladybird 项目后续公告中 Windows 版本与进入 beta 阶段的时间表，以及 alpha 测试者在真实网站上的兼容性反馈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ladybird_%28web_browser%29">Ladybird (web browser) - Wikipedia</a></li>
<li><a href="https://ladybird.org/posts/alpha/">Ladybird is now in alpha - Ladybird</a></li>
<li><a href="https://ladybird.org/">Ladybird Ladybird (web browser) - Wikipedia Ladybird browser releases its first alpha for macOS and Linux Ladybird Browser is now officially available in alpha for ... First Ladybird Browser Alpha for macOS and Linux Ladybird Browser Alpha Launches for macOS and Linux: Windows ...</a></li>

</ul>
</details>

**标签**: `#browser engines`, `#Ladybird`, `#open source`, `#software release`, `#web platform`

---