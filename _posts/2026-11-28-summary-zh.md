---
layout: issue
permalink: /zh/briefing/2026-11-28/
title: "AI 新闻简报：2026年11月28日"
date: 2026-11-28
lang: zh
---

> 过去一天共筛查 233 条科技资讯，留下最值得读的 18 条。

---

**人工智能**
1. [Google Research 提出 DeepCrossAttention：质量相当下最高 3 倍提速](#item-ai-news-1) ⭐️ 7.0/10
2. [DeepMind“人类首次考试”：顶尖模型难连续答对 16 题](#item-ai-news-2) ⭐️ 7.0/10
3. [Embo 获 1.1 亿美元种子轮，研发机器人世界模型](#item-ai-news-3) ⭐️ 7.0/10
4. [Dwarkesh 播客：Erdil 与 Kokotajlo 谈 2029 年前智能爆炸概率](#item-ai-news-4) ⭐️ 7.0/10

**芯片与算力**
1. [诉讼文件：美政府施压英特尔交出约 10%股权](#item-chips-compute-1) ⭐️ 8.0/10
2. [MATCH Act 若禁止 ASML 维护中国约 350 台浸没式光刻机，分析称或适得其反](#item-chips-compute-2) ⭐️ 7.0/10
3. [SemiAnalysis 解析 AWS Trainium3：推理性价比对标英伟达](#item-chips-compute-3) ⭐️ 7.0/10
4. [铠侠第三代 XL-Flash 原型读取延迟达 3 微秒，2027 年 3 月送样](#item-chips-compute-4) ⭐️ 7.0/10

**电动车与新能源**
1. [欧盟 10 月电动汽车销量超过汽油车与柴油车之和](#item-ev-energy-1) ⭐️ 8.0/10
2. [德国光伏年发电量首次突破 100 TWh](#item-ev-energy-2) ⭐️ 8.0/10
3. [报道称全球最大电动散货船 BRF Froan 配 23.5 MWh 电池](#item-ev-energy-3) ⭐️ 7.0/10
4. [丰田确认汉兰达 9X 于 2027 年初上市，成为品牌首款增程电动车](#item-ev-energy-4) ⭐️ 7.0/10
5. [美国国会通过电动自行车电池安全立法，自愿标准将转为强制](#item-ev-energy-5) ⭐️ 7.0/10
6. [Arriva 获荷兰北荷兰省约 20 亿欧元电动巴士合同](#item-ev-energy-6) ⭐️ 7.0/10
7. [宁德时代发布 100kWh“30\#”换电电池包，换电不到一分钟](#item-ev-energy-7) ⭐️ 7.0/10

**航天**
1. [Stoke Space 新星一级抵达 SLC-14，目标 2027 年初首飞](#item-space-1) ⭐️ 7.0/10

**科技产业与政策**
1. [SAP 确认 GitHub 安全事件，源代码据报遭复制篡改](#item-tech-industry-1) ⭐️ 7.0/10
2. [AMD 与 Winbond 固件漏洞让 BitLocker PIN 可被快速暴力破解](#item-tech-industry-2) ⭐️ 7.0/10

---

## 人工智能

<a id="item-ai-news-1"></a>
### [Google Research 提出 DeepCrossAttention：质量相当下最高 3 倍提速](https://research.google/blog/supercharging-transformer-residual-connections/) ⭐️ 7.0/10

Google Research 在博客中提出 DeepCrossAttention（DCA）：不改动 transformer 的基本组件，而是改动残差连接（即把每层输入直接加到输出上的那条旁路），并把注意力从同一层的 token 之间扩展到跨层——每个 token 对之前所有层的表示做一次动态加权的组合。博客称，这一改动在模型质量相当的情况下带来最高 3 倍的提速，并称将 DCA 加装到已预训练好的模型上、再短暂继续训练，在 LM1B 上把困惑度（perplexity，语言模型预测下一个 token 的不确定度，越低越好）降低了 0.19，而同样条件下常规继续训练只降低 0.02。上述数字均为 Google 自述的实验结果，尚无第三方复现；可得信息中也没有说明 3 倍提速是在多大的模型、什么硬件、与哪个基线对比下测得的。这项结果目前停留在研究阶段。

Hacker News · ComputedCamp995 · 11月27日 23:06 · [社区讨论](https://news.ycombinator.com/item?id=50672565)

**「已证实与未证实」** 已证实：Google Research 的博客与 arXiv 论文（ICML 2025）报告，DeepCrossAttention 通过改造 transformer 残差连接、在层间做深度交叉注意力，在 LM1B 语言建模实验中达到同等质量最多快 3 倍，新增参数量可忽略。
尚未证实：上述加速与质量结论仅来自 Google 自己的论文实验，尚无独立复现或第三方基准；现有公开摘要未说明代码或模型权重是否及何时开放，也未界定可迁移到哪些现有模型。

**「背景」** 残差连接是 Transformer 中把每一层的输出直接加到主干表示上的“捷径”，使深层网络更容易训练；但 Google 的 DCA 论文指出，简单相加会稀释前面层的重要信息。DCA 改为让每个 token 对之前各层的表示做带可学习权重的跨层注意力，按需混合历史层的信息，而不是固定求和。

**「为什么重要」** 对训练模型的人来说，最可操作的线索是 DCA 的“加装”路径：如果 0.19 对 0.02 的困惑度改善能在更大规模上复现，团队也许可以用短时间的继续训练升级已有 checkpoint，而不必从头重训。但这两个数字来自 Google 在 LM1B 上的自测，模型规模远小于当下主力模型；是否提供可用的实现、提速是在什么硬件上测得，目前都不清楚——在据此规划训练预算之前，应先等独立复现或在自身工作负载上的验证。

**「社区讨论」** 有评论者（londons\_explore）认为，在训练中途改动模型的形状与维度并继续训练这条路线很有前景；也有人（pollorollo）批评博客用折线图把本无时间先后的若干方法连起来，应当改用柱状图。另有评论者（amluto）推测跨层注意力或许能缓解模型在字符级计数（例如“strawberry”里有多少个 r）上的著名失败，但这只是猜测，并非博客给出的结论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.google/blog/supercharging-transformer-residual-connections/">Supercharging transformer residual connections</a></li>
<li><a href="https://arxiv.org/html/2502.06785">DeepCrossAttention : Supercharging Transformer Residual ...</a></li>
<li><a href="https://research.google/blog/supercharging-transformer-residual-connections/">Supercharging transformer residual connections - Google Research</a></li>
<li><a href="https://arxiv.org/abs/2502.06785">[2502.06785] DeepCrossAttention: Supercharging Transformer ...</a></li>

</ul>
</details>

**标签**: `#transformer architecture`, `#model efficiency`, `#attention mechanisms`, `#Google Research`, `#AI research`

---

<a id="item-ai-news-2"></a>
### [DeepMind“人类首次考试”：顶尖模型难连续答对 16 题](https://the-decoder.com/google-deepminds-humanitys-first-exam-shows-top-ai-models-still-fail-simple-everyday-tasks-under-repeated-runs/) ⭐️ 7.0/10

据 The Decoder 报道，Google DeepMind 用名为“Humanity&\#x27;s First Exam”的基准测试了 18 个 AI 模型，发现领先模型几乎每个任务族都至少能答对一次，但在要求连续 16 次答对时仍会失败，OpenAI 的 GPT-6.2 Astra 也在其中。测试中 73% 的错误来自视觉感知，增加计算时间也没有消除这一差距。报道未说明该基准是否公开发布、完整测试方法或是否经过独立复核。

The Decoder · 11月28日 11:12

**「已证实与未证实」** 已证实：Google DeepMind 发布了名为“Humanity&\#x27;s First Exam”的评测，共包含 544 道日常题，并公开了部分数据集（Google 官方博客）；The Decoder 报道称，该评测考察了 18 个模型，关键在于要求模型对同一类任务连续 16 次答对，而不只是答对一次。

尚未证实：哪些模型具体在哪些任务上失败、报道中提到的 GPT-6.2 Astra 等模型的相对位置，“视觉感知占 73% 的错误”和“增加算力时间并不能解决问题”这两项结论，目前都只见于 The Decoder 这一篇二次报道，所给材料未链接 DeepMind 的原始论文、排行榜或完整结果表；另有一条 YouTube 短视频称配套的 Kaggle 竞赛为期三周、截至 12 月 15 日、奖金 5 万美元，也缺少第二个来源佐证。

**「背景」** 这项基准的名称戏仿了「Humanity&\#x27;s Last Exam」（人类最后的考试）——一个以极难著称、用来给 AI 出标准化难题的测试；HFE 则反其道而行，专门考察人类几乎都能答对的简单日常问题。据 Google 官方博客介绍，HFE 在 Kaggle 上发布，共 544 道文字与图像提示，衡量的是前沿模型回答的可靠性而非难度上限，Kaggle 上的公开排行榜也以同样口径记录各模型表现。

**「为什么重要」** 对准备把模型接入日常自动化流程的开发者来说，单次演示成功不能代表可部署性：连续 16 次正确的要求暴露出稳定性缺口，而视觉感知占错误来源的 73%，意味着涉及读图、识别界面的环节更需要额外校验或人工兜底。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/google-deepmind/humanitys-first-exam/">Humanity ’ s First Exam : Testing LLM reliability</a></li>
<li><a href="https://www.theneuron.ai/newsletter/deepmind-s-new-ai-exam/">DeepMind &#x27; s new AI exam | The Neuron</a></li>
<li><a href="https://www.kaggle.com/benchmarks/deepmind/hfe">Humanity &#x27; s First Exam (HFE) Leaderboard | Kaggle</a></li>
<li><a href="https://www.theneuron.ai/newsletter/deepmind-s-new-ai-exam/">DeepMind &#x27; s new AI exam | The Neuron</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/google-deepmind/humanitys-first-exam/">Humanity ’ s First Exam : Testing LLM reliability</a></li>
<li><a href="https://www.youtube.com/shorts/tc3boVX6Sec">Humanity &#x27; s First Exam от Google DeepMind : $50 000 на... - YouTube</a></li>

</ul>
</details>

**标签**: `#AI reliability`, `#benchmark evaluation`, `#Google DeepMind`, `#visual perception`, `#foundation models`

---

<a id="item-ai-news-3"></a>
### [Embo 获 1.1 亿美元种子轮，研发机器人世界模型](https://the-decoder.com/robotics-startup-embo-raises-110-million-in-seed-funding-to-build-world-model-ai-for-robots/) ⭐️ 7.0/10

机器人初创公司 Embo 于 11 月 28 日结束隐身状态，宣布完成 1.1 亿美元种子轮融资，由 a16z 领投。公司称正在构建面向机器人的“下一代前沿 AI 模型”，目标是成为可通用的“机器人大脑”：模型从海量互联网视频中学习物理世界如何运作，并在仿真环境中练习精细动作技能。团队背景包括来自 Google DeepMind、Meta 和 MIT 的研究人员。目前公开的只有融资与路线描述，尚无产品、基准测试结果或可访问的接口。

The Decoder · 11月28日 10:48

**「已证实与未证实」** 已证实：Embo 宣布完成 1.1 亿美元种子轮融资，由 a16z 领投，公司同时结束隐身状态；The Decoder 与 Embo 官方发布页均给出这一金额和领投方，并称团队成员来自 Google DeepMind、Meta 和 MIT。尚未证实：技术路线本身——即“从互联网视频学习物理规律、在仿真中训练动作技能”能否支撑一个通用机器人大脑；报道未给出任何模型规模、演示视频、基准测试或第三方评测，也未披露估值、资金具体用途和产品时间表。

**「背景」** 世界模型（world model）是一类通过学习预测场景接下来会如何变化的 AI，机器人可以借此在真实行动前“预演”后果，而不必完全依赖实机试错。Embo 此前一直处于隐身（stealth）状态，此次融资与公司正式亮相同时公布：据 Dealroom 报道，本轮由 a16z 领投，Khosla Ventures、DST Global 以及英伟达旗下投资部门 NVentures 参投，公司由前 DeepMind 研究员 Danijar Hafner 领导。

**「为什么重要」** 对开发者和机器人团队而言，这条消息的实际含义是：短期内无法基于 Embo 做任何集成，因为它没有发布模型、API 或合作计划；真正值得关注的是资本对技术路线的选择——a16z 以 1.1 亿美元押注“视频预训练＋仿真练技能”，而这一金额在种子阶段通常意味着大额算力和仿真基础设施投入，会加剧该方向对研究人员与 GPU 资源的争夺。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dealroom.co/news/175093-embo-raises-110m-seed-to-build-robot-brains-with-world-models/">Embo raises $110M seed to build robot brains with world models</a></li>
<li><a href="https://aiparabellum.com/embo-raises-110m-seed-robot-brain-world-models/">Embo Raises $110M Seed to Build a Robot Brain on World Models</a></li>
<li><a href="https://embo.com/introducing-embo">Introducing Embo | Embo</a></li>

</ul>
</details>

**标签**: `#robotics`, `#world models`, `#embodied AI`, `#funding`, `#startups`

---

<a id="item-ai-news-4"></a>
### [Dwarkesh 播客：Erdil 与 Kokotajlo 谈 2029 年前智能爆炸概率](https://www.techmeme.com/261127/p13#a261127p13) ⭐️ 7.0/10

Dwarkesh Patel 的播客发布了一期与 AI 研究者 Ege Erdil 和 Daniel Kokotajlo 的对谈，讨论 2029 年之前发生“智能爆炸”的概率、是否应暂停 AI 开发，以及美国与中国对抗的风险。节目以“如果我们现在暂停，人们仍然不会理解利害所在”作为引语，但公开简介没有给出两人各自判断的具体概率数字。这是一场观点交流，不是新的模型、产品发布或政策决定，其中对时间线和暂停的判断应视为研究者意见，而非已验证的预测。

Techmeme · 11月27日 20:15

**「已证实与未证实」** 已证实：Dwarkesh Patel 的播客发布了 Ege Erdil 与 Daniel Kokotajlo 的对谈节目，议题包括智能爆炸的时间表、是否应暂停 AI 以及美国对华政策；主持人在节目页面表示，本以为会是一场辩论，但两人意见一致的程度远超预期（Dwarkesh Patel 本人撰文）。
尚未证实：两人在节目中给出的具体概率与年份判断、各自立场是否发生变化，均只存在于这期播客的讨论中，所提供的材料未给出任何数字或转录原文；此外，Erdil 此前公开表述过 2045 年以后的谨慎时间线、并认为智能爆炸不太可信，本期他是否修正该观点尚无法从现有信息确认。

**「背景」** Ege Erdil 是 Google DeepMind 的研究员，曾与 Tamay Besiroglu 公开主张通用人工智能（AGI）还要约 30 年、时间线在 2045 年之后，认为“智能爆炸”并不现实，但相信经济会以每 1 至 2 年翻一番的速度爆炸式增长。Daniel Kokotajlo 是 AI Futures Project 的作者之一，该机构发布的 AI 2027、AI 2040 情景报告预测，超人类水平的 AI 研究者可能在 2027 年前后出现。两人对时间线的判断相差近二十年，主持人 Dwarkesh Patel 因此把这次对话定位为讨论而非正式辩论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.dwarkesh.com/p/daniel-kokotajlo-ege-erdil">AI researchers debate what we should do next – Daniel Kokotajlo ...</a></li>
<li><a href="https://www.youtube.com/watch?v=WLBsUarvWTw">AGI is still 30 years away — Ege Erdil &amp; Tamay Besiroglu - YouTube</a></li>
<li><a href="https://www.indiatoday.in/technology/news/story/intelligence-explosion-now-expected-in-2027-as-anthropic-ai-progress-doubles-3036529-2026-11-11">Intelligence explosion now expected in 2027 as Anthropic AI ...</a></li>
<li><a href="https://www.dwarkesh.com/p/daniel-kokotajlo-ege-erdil">AI researchers debate what we should do next – Daniel Kokotajlo and...</a></li>
<li><a href="https://www.youtube.com/watch?v=WLBsUarvWTw">AGI is still 30 years away — Ege Erdil &amp; Tamay Besiroglu - YouTube</a></li>

</ul>
</details>

**标签**: `#AI timelines`, `#AI safety`, `#AGI`, `#AI geopolitics`, `#AI policy`

---

## 芯片与算力

<a id="item-chips-compute-1"></a>
### [诉讼文件：美政府施压英特尔交出约 10%股权](https://arstechnica.com/tech-policy/2026/11/intel-faced-a-choice-give-trump-10-or-face-the-consequences/) ⭐️ 8.0/10

据 Ars Technica 转载 Wired 的报道，一份美国联邦诉讼中引用的公司通话笔记显示，美国商务部律师 David Shapiro 在 2025 年 8 月对英特尔首席财务官表示，不要“以为这是一场谈判”，总统预计在周五按这些条件宣布协议；英特尔董事会可以选择拒绝，但“拒绝将带来他无法预测的后果”。报道称，特朗普政府最终获得英特尔约 10% 的股份，而这套施压过程此前未被完整披露。上述对话细节来自诉讼中引用的笔记，并非法院已认定的事实。

Ars Technica · 11月27日 12:05

**「已证实与未证实」** 已证实：据 Ars Technica 转述 WIRED 的报道，一份联邦诉讼中引用的公司通话内部记录显示，美国商务部律师 David Shapiro 于 2025 年 8 月告知英特尔首席财务官，此事“不要误以为是一场谈判”，总统预计当周五按这些条件宣布协议；记录还称他承认董事会可以不接受，但拒绝会带来他无法预测的后果。英特尔最终同意让联邦政府获得约 10% 的股份（The Daily Beast、Yahoo 的报道亦如此表述）。

尚未证实：所谓“后果”具体指什么、是否曾以任何形式付诸行动，现有报道均未说明；上述引语出自诉讼中的内部笔记摘要，而非可公开核对的法庭文件原文，且这篇报道是 WIRED 报道的节选转载，未包含起诉方、案号或英特尔方面的回应。政府持股对英特尔产能与先进制程产出的实际影响，报道也未给出任何数据。

**「背景」** 2025 年 8 月，特朗普政府向英特尔董事会提出由美国政府取得公司约 10% 股权的方案，并按计划在当周的周五对外公布，这一交易本身已不是新闻。此次进入公众视野的是交易背后的施压过程：据 Ars Technica 转述 Wired 的报道，相关细节来自英特尔为董事会准备的内部通话记录，这些记录已被纳入一桩联邦诉讼。英特尔是美国唯一总部设在境内、能够量产最先进逻辑芯片的公司，因此联邦政府直接持股对其产能与供应链具有直接影响。

**「为什么重要」** 对英特尔及其他接受联邦芯片补贴的企业而言，这次披露的具体后果是：政府入股可以在几天内被要求作出决定，而拒绝的代价被官方律师描述为不可预测，董事会可用的谈判空间因此被压缩。

<details><summary>参考链接</summary>
<ul>
<li>Not Just Nvidia: Inside Team Trump&#x27;s Takeover of Intel | WIRED</li>
<li>Trump Team&#x27;s Secret Ultimatum Exposed in Court - Yahoo</li>
<li>Trump Team&#x27;s Secret Ultimatum Exposed in Court - The Daily Beast</li>

</ul>
</details>

**标签**: `#Intel`, `#US industrial policy`, `#semiconductor supply chain`, `#government equity stake`, `#chip policy`

---

<a id="item-chips-compute-2"></a>
### [MATCH Act 若禁止 ASML 维护中国约 350 台浸没式光刻机，分析称或适得其反](https://www.techmeme.com/261127/p16#a261127p16) ⭐️ 7.0/10

LithoWar 的一篇分析文章提出，美国拟议中的 MATCH Act 若禁止 ASML 为其在中国的大约 350 台浸没式（immersion）DUV 光刻机提供维护服务，效果可能适得其反：ASML 一旦退出售后环节，竞争对手就有机会接手这些设备的维保、对其做逆向工程，并从 ASML 挖走技术人员。文章的核心论点是，切断原厂服务在限制设备可用性的同时，也让原厂失去对设备状态的掌握，反而把接触设备的机会让给第三方。需要注意，这是一篇观点性分析而非官方公告，Techmeme 收录的仅为标题与导语，法案的具体条款、适用设备范围、生效时间与立法进度均未获独立核实。

Techmeme · 11月28日 02:00

**「已证实与未证实」** 已证实：LithoWar 发布分析（经 Techmeme 收录）主张，若 MATCH Act 禁止 ASML 为中国境内约 350 台浸没式 DUV 光刻机提供零部件、维保与软件支持，结果可能适得其反，让竞争对手获得承接维保、逆向工程这些设备以及招募 ASML 人员的机会。这是该文的论点，而非已经发生的事实；bits-chips.com 也刊出同向评论，称该法案将禁售所有浸没式光刻机并切断相当一部分已装机队的支持。

尚未证实：法案的立法状态说法不一——有汇总称其已写入参议院国防法案，另有报道称可能在 2026 年 12 月中旬被附加到 2027 财年国防授权法案，本条目未能核实哪种说法准确；“约 350 台”是 LithoWar 的估算，无官方数字佐证；竞争对手接手维保、逆向工程与人才流失均属推演，无实证。据 explainx.ai 汇总，荷兰政府正游说反对，ASML CEO Christophe Fouquet 警告全面断供可能反噬，这些说法源自《亚洲时报》11 月 27 日报道，本条未提供原文佐证。

**「背景」** 浸润式深紫外（DUV）光刻机是 ASML 的主力机型之一，例如 Twinscan NXT 系列；2023 年以来美国和荷兰的出口管制主要针对新机销售，却未能清除已经运进中国的庞大装机量——Tom&\#x27;s Hardware 报道称，中国晶圆厂正在设法给这些旧设备延寿，Zero Hedge 则称中国囤积了约 340 台 ASML 扫描仪。正因如此，售后服务成了华盛顿的新抓手：据 Zero Hedge 报道，美国国会中的对华鹰派正试图把包括 MATCH Act 在内的三四项芯片出口管制法案塞进必须通过的 2027 财年国防授权法案。

**「为什么重要」** 对于依靠 ASML 现场服务维持运转的中国晶圆厂来说，约 350 台浸没式 DUV 设备是产线上的关键生产工具，一旦服务合同被切断，停机时间与良率波动会立刻成为现实问题，而第三方维保与零部件渠道将变成唯一的替代路径。这也正是分析所称的“反噬”机制：管制把原厂挡在门外，却可能为竞争对手创造接触、维修乃至学习这些设备的机会。ASML 方面则面临中国存量机台服务收入与客户关系的直接损失。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://explainx.ai/blog/match-act-asml-immersion-scanners-servicing-backfire-november-2026">MATCH Act ASML: 350 Immersion Scanners at Risk (2026 ...</a></li>
<li><a href="https://bits-chips.com/article/the-match-act-could-hand-china-the-keys-to-advanced-lithography/">The Match Act could hand China the keys to advanced ...</a></li>
<li><a href="https://byte.eco/post/how-the-match-act-could-backfire-by-barring-asml-from-its-350-immersion-scanners-in-china">How the MATCH Act could backfire by barring ASML from its…</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/semiconductors/china-is-squeezing-more-life-out-of-asmls-older-duv-tools-as-chip-controls-tighten">Chinese fabs are reportedly upgrading older ASML ... | Tom&#x27;s Hardware</a></li>
<li><a href="https://www.zerohedge.com/technology/chip-war-goes-nuclear-beijing-hoarded-340-asml-scanners-congress-targets-service-calls">Chip War Goes Nuclear: Beijing Hoarded 340 ASML Scanners ...</a></li>

</ul>
</details>

**标签**: `#export controls`, `#ASML`, `#lithography`, `#China semiconductors`, `#supply chain`

---

<a id="item-chips-compute-3"></a>
### [SemiAnalysis 解析 AWS Trainium3：推理性价比对标英伟达](https://newsletter.semianalysis.com/p/trainium3-inferencex) ⭐️ 7.0/10

SemiAnalysis 发布对 AWS Trainium3 的推理性能与微架构深度分析，称在自建基准平台 InferenceX 上，Trainium3 搭配 PDS 与 vLLM，在“总拥有成本（TCO）对 p90 交互延迟”整条曲线上，每美元推理性能优于除英伟达 Vera Rubin 之外的所有加速器，并与 GB300 互有胜负。该结论基于 SemiAnalysis 自研的 UBenchX 微基准和 AgentX 端到端测试：后者通过回放真实编程智能体（coding agent）会话来测量生产级智能体推理负载。微架构层面，报告称 Trainium 从零为机器学习负载设计，以 tile 为一等原语，其 Descriptor Generation Engines（DGE，作用类似英伟达 TMA、AMD MI455X 的 TDM）可在较小消息尺寸下达到峰值 HBM 带宽利用率（MBU），报告称这在英伟达 GPU 上无法实现。SemiAnalysis 表示 AWS Annapurna Labs 联合创始人 Nafea Bshara、Trainium 首席架构师 Ron Diamant 等团队成员协助其理解架构并验证了基准实验，但公开摘录未给出任何绝对性能数字或完整测试配置。

SemiAnalysis · 11月27日 15:54

**「已证实与未证实」** 已证实：SemiAnalysis 将 Trainium3 纳入其开源的 InferenceX 基准（与 TPUv7、OpenAI Jalapeño、英伟达 Rubin NVL72、AMD 同列），并用 UBenchX 做了周期级 SRAM、机架级带宽与注意力等微基准；AWS Annapurna Labs 团队参与架构讲解与实验验证，这是该机构自己的说明。
尚未证实：每美元性能“除 Vera Rubin 外全面领先”属 SemiAnalysis 自建基准上的厂商协助验证结果，摘录中未披露具体吞吐、延迟、价格假设与 TCO 计算口径，也无第三方复现；DGE 在小消息尺寸下达峰值 HBM 带宽利用率同样只有该机构的微基准支持。

**「背景」** Trainium 是 AWS 自研的 AI 加速器系列，由旗下 Annapurna Labs 团队设计；Trainium3 是该系列第三代产品，AWS 官方资料称其集成 8 个大核，每核配 Tensor、Vector、Scalar、GPSIMD 四类引擎，MXFP8 算力最高为 Trainium2 的两倍。第三方《AI Accelerator Report 2026》汇总的 AWS 公布数据显示，Trainium3 是 AWS 首款 3nm AI 芯片，单芯片 2.52 PFLOPS FP8 算力、144GB HBM3e 显存，144 颗芯片组成的 Trn3 UltraServer 合计 20.7TB HBM3e 与 706TB/s 带宽。SemiAnalysis 此番强调「微架构」，正是因为英伟达的数据中心 GPU 源自图形渲染管线，历代为补上 AI 瓶颈逐块加装专用硬件（Volta 的 Tensor Core、Hopper 的 TMA、Blackwell 的 Tensor Memory），而 Trainium 从设计之初就以 tile 为一等公民。

**「为什么重要」** 对正在为智能体类推理负载选型的团队而言，这份分析给出了除英伟达之外的第二个可量化选项：若 Trainium3 的每美元 token 成本优势成立，同等预算下的推理毛利可能更高。但实际迁移的前提是软件栈——报告点名的路径是 vLLM 加 PDS，团队在评估时需要先确认自有模型的算子与注意力实现能否在该栈上跑通，而非仅比较芯片规格。

**「后续看点」** InferenceX 的公开排行榜与 GitHub 仓库会持续更新 Trainium3 的配置点与 AgentX 结果，可观察是否有 AWS 之外的一方复现同一组每美元性能曲线。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aws.amazon.com/ai/machine-learning/trainium/">AI Accelerator - AWS Trainium - AWS</a></li>
<li><a href="https://sampooni.github.io/ai-accelerator-report-2026/11-aws.html">Chapter 11: AWS Trainium3 | AI Accelerator Report 2026</a></li>

</ul>
</details>

**标签**: `#AWS Trainium`, `#AI accelerators`, `#inference`, `#microarchitecture`, `#semiconductor supply chain`

---

<a id="item-chips-compute-4"></a>
### [铠侠第三代 XL-Flash 原型读取延迟达 3 微秒，2027 年 3 月送样](https://www.tomshardware.com/pc-components/ssds/kioxias-3rd-gen-xl-flash-hits-optane-class-3-microsecond-read-latency-with-70-percent-higher-density-samples-march-2027-ahead-of-18-million-iops-gp2-ssds) ⭐️ 7.0/10

铠侠（Kioxia）在东京 KIOXIA Forum 上展出了第三代 XL-Flash 低延迟闪存原型：平均读取延迟 3 微秒，不到自家 BiCS8 TLC（40 微秒）的十分之一；位密度比第二代高 70%，并采用 CBA（CMOS 直接键合到阵列）把逻辑晶圆与存储单元晶圆分开制造后再键合，铠侠称其能效因此比第二代提升约 135%。第一批样品计划在 2027 年 3 月提供给特定客户；首个使用该闪存的产品是面向 AI 服务器与数据中心的 GP2 企业级 SSD，标称 512 字节随机读超过 1800 万 IOPS、顺序读最高 28 GB/s，前提是能跑满 PCIe 6.0 x4。这与英特尔 2022 年退出的 Optane 定位相似，但 GP2 的评估样品要到 2027 年底才发给特定客户，最终规格可能变化；铠侠也未公布层数等完整参数。

Tom&\#x27;s Hardware · 11月27日 12:00

**「已证实与未证实」** 已证实：铠侠在自家论坛上展出了第三代 XL-Flash 原型，并公布 3 微秒平均读取延迟、较第二代高 70% 的位密度、CBA 键合结构，以及 2027 年 3 月向特定客户送样的计划；GP2 标称 512 字节随机读超过 1800 万 IOPS、顺序读最高 28 GB/s、最高每日 50 次全盘写入，铠侠称正考虑 E1.S 与 E3.S 形态并支持直接液冷。
尚未证实：SLC 存储单元与 128Gb 单 die 容量在报道中均标注为“据称”，150000 至 250000 次 P/E 循环、4.8 Gb/s 接口速率亦出自铠侠自身说法，没有第三方实测；层数等完整规格未披露，GP2 最终规格可能变动，价格、容量和具体上市时间均未公布，评估样品要等到 2027 年底。

**「背景」** XL-Flash 是铠侠基于 BiCS 闪存工艺、针对低读取延迟和高写入寿命调优的 SLC 闪存，定位为介于 DRAM 与普通 NAND 之间的“存储级内存”层级。该系列第一代于 2019 年推出，读取延迟低于 5 微秒；2022 年的第二代增加了 2-bit MLC 选项，以部分同代性能换取更低的单位容量成本。英特尔曾以 3D XPoint 材质的 Optane 占据这一层级，但已于 2022 年彻底退出该业务，留下了低延迟内存层级的空缺。

**「为什么重要」** 对想给 GPU 的 HBM 之外再挂一层低成本内存的 AI 服务器设计者来说，XL-Flash 是目前少有的、不依赖已停产 Optane 的存储级内存（SCM）路线；GP2 瞄准 512 字节而非常见的 4KB 访问粒度，正好对应铠侠所说 AI 负载中大量细粒度内存查询的模式。但送样在 2027 年 3 月、GP2 评估样品在 2027 年底，现在采购的机器无法受益；规划 2027 年平台时需要同步评估 E1.S/E3.S 盘位与直接液冷的兼容性。

**「后续看点」** 2027 年 3 月首批 XL-Flash 样品能否按期交付，以及 2027 年底 GP2 评估样品给出的最终规格。铠侠与英伟达还在合作推进后续 GP 系列，目标最高 1 亿随机读 IOPS。

**标签**: `#Kioxia`, `#XL-Flash`, `#NAND flash`, `#low-latency memory`, `#AI data centers`

---

## 电动车与新能源

<a id="item-ev-energy-1"></a>
### [欧盟 10 月电动汽车销量超过汽油车与柴油车之和](https://insideevs.com/news/817061/eu-ev-sales-october-jump/) ⭐️ 8.0/10

据 InsideEVs 报道，欧盟 10 月电动汽车销量超过了汽油车与柴油车的合计销量。报道称，去年同期汽油车和柴油车合计还领先约 12.7 万辆，而今年 10 月电动汽车反而领先近 7 万辆，相当于一年内约 20 万辆的差距反转。报道未给出具体销量数字、数据发布机构，也未说明“电动汽车”是否包含混动车型，这些统计范围仍待官方新车注册数据核实。

InsideEVs · 11月27日 15:15

**「已证实与未证实」** 已证实：欧洲汽车制造商协会（ACEA）11 月 24 日发布的数据显示，2026 年 10 月欧盟纯电动车注册量为 279,799 辆，同比增长 61.4%；1—10 月纯电动车占欧盟新车注册量的 23.4%，高于去年同期的 16.4%，同期汽油车与柴油车合计份额从 36.5% 降至 27.7%（来源：ACEA）。

尚未证实：InsideEVs 称 10 月单月欧盟电动车销量比汽油车与柴油车合计多出近 7 万辆，而一年前是落后 12.7 万辆；该报道未给出月度分类销量明细，也未说明“电动车”是否只含纯电、是否计入插电混动。ACEA 的年内累计数据仍显示汽油车加柴油车的合计份额（27.7%）高于纯电动车（23.4%），与上述月度反超说法并不直接对应，两套口径的差异报道未作解释。

**「背景」** 欧洲汽车制造商协会（ACEA）11 月下旬公布的数据显示，10 月欧盟纯电动乘用车注册量约 28 万辆，同比增长 61%，占新车注册量近 30%，高于此前数月 25 万辆以上的月度水平。这组数据只统计纯电车型，且未给出分国家、分车型明细，因此“电动车合计反超汽油车与柴油车”的构成仍需以完整注册数据核对。

**「后续看点」** 接下来公布的欧盟月度新车注册数据将检验这是单月波动还是持续趋势，同时也会明确统计范围和具体销量数字。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.electrive.com/2026/11/24/acea-battery-electric-cars-capture-30-per-cent-of-eu-passenger-car-market/">2026-11-24 — Battery-electric cars near 30% of EU new-car market in October, ACEA data shows</a></li>
<li><a href="https://www.acea.auto/pc-registrations/new-car-registrations-5-4-in-october-2026-year-to-date-battery-electric-23-4-market-share/">New car registrations: +5.4% in October 2026 year-to-date ...</a></li>
<li><a href="https://www.acea.auto/files/Press_release_car_registrations_October_2026.pdf">EMBARGOED PRESS RELEASE 6.00 CET (5.00 GMT), 24 November 2026</a></li>
<li><a href="https://theevreport.com/eu-car-registrations-october-2026-battery-electric-share">EU Car Registrations: Battery-Electric Share 23.4% Through ...</a></li>

</ul>
</details>

**标签**: `#EV sales`, `#European Union`, `#market share`, `#gasoline and diesel`, `#EV adoption`

---

<a id="item-ev-energy-2"></a>
### [德国光伏年发电量首次突破 100 TWh](https://www.pv-magazine.com/2026/11/28/germanys-solar-generation-tops-100-twh-in-2026/) ⭐️ 8.0/10

据弗劳恩霍夫太阳能系统研究所（Fraunhofer ISE）Energy-Charts 平台的数据，截至 11 月 27 日上午，德国光伏发电量今年累计达到 100.2 TWh，首次在年度累计口径上突破 100 TWh。其中 80.6 TWh 来自受德国《可再生能源法》（EEG）支持的电站并网发电，其他光伏系统并网 2.6 TWh，自发自用 16.9 TWh。光伏是今年德国第二大净发电来源，仅次于风电的 124.4 TWh，高于燃气电站的 82.1 TWh、褐煤的 63 TWh 和硬煤的 27.2 TWh；煤炭发电合计仍低于光伏。截至同一时点，该数字已比 2025 年全年的 90 TWh 高出 10 TWh，而 2016 年全年仅为 36.8 TWh。

pv magazine · 11月28日 08:00

**「已证实与未证实」** 已证实：pv magazine 援引 Fraunhofer ISE 的 Energy-Charts 数据，确认截至 11 月 27 日上午光伏累计发电 100.2 TWh，并给出 80.6 TWh、2.6 TWh、16.9 TWh 的分项及各类电源的年内发电量排序。
尚未证实：2026 年尚未结束，100.2 TWh 是截至 11 月 27 日的年内累计值而非最终全年数据；德国太阳能与电池经济协会（BSB）11 月中旬称德国“即将达到”该里程碑，同样依据该所数据，未经过第三方独立核算；报道未提供新增装机容量或相关政策变动细节。

**「背景：EEG 补贴与统计口径」** 德国《可再生能源法》（EEG）为光伏发电提供上网电价等支持，因此 Fraunhofer ISE 的 Energy-Charts 在统计太阳能发电量时，会把享受 EEG 补贴的上网电量、其他光伏系统的上网电量以及用户自用电量分开计算。2025 年德国太阳能发电量为 90 TWh，其中 EEG 补贴项目上网 67.9 TWh、其他系统 2.2 TWh、自用电 19.8 TWh；2026 年的 100.2 TWh 是在同一口径上同比增长约 10 TWh。

**「为什么重要」** 褐煤与硬煤合计 90.2 TWh，已低于光伏的 100.2 TWh，这意味着德国电网调度和消纳预案正以光伏为主要变量之一；同时 16.9 TWh 的自发自用不进入电力市场，统计口径和电网规划需要把并网购电与自用部分分开看，否则会低估光伏的实际出力规模。

**「后续看点」** 关注 Energy-Charts 在年末公布的 2026 年全年最终统计，届时 12 月出力才能把全年总量确定下来。

**标签**: `#Germany solar`, `#solar generation`, `#Fraunhofer ISE`, `#renewable energy milestone`, `#Energy-Charts`

---

<a id="item-ev-energy-3"></a>
### [报道称全球最大电动散货船 BRF Froan 配 23.5 MWh 电池](https://electrek.co/2026/11/27/worlds-largest-electric-bulk-cargo-shop-packs-massive-23-5-mwh-battery/) ⭐️ 7.0/10

Electrek 报道称，电动散货船 BRF Froan 搭载 23,500 kWh（23.5 MWh）电池，并称其为全球最大的电动散货船。报道没有给出该船的续航、充电时间、首航日期或运营方，因此这些关键运行细节仍不清楚。“全球最大”是 Electrek 的表述，尚未看到独立验证。

Electrek · 11月27日 19:22

**「已证实与未证实」** 已证实：Electrek 在报道中称，BRF Froan 是一艘新电动散货船，电池容量为 23,500 kWh（23.5 MWh）。尚未证实：“全球最大电动散货船”的说法、实际续航、充电时间、首航日期及运营方均未在报道中说明，也无独立数据。

**「背景」** 电池动力船舶目前大多集中在沿岸和短途航线，因为需要靠港口岸电充电，而远洋散货运输仍主要依赖燃油。据 Interesting Engineering 报道，BRF Froan 全长 129.9 米（426 英尺），正驶往挪威安装这套 23.5 MWh 电池系统；船东 Berge Rederi 的页面称，该船将在两座挂靠港口都配备岸电设施，预计每年岸电充电耗电约 513.3 万千瓦时。

**「为什么重要」** 对散货航运而言，23.5 MWh 电池把岸电充电能力和航线长度推到设计核心：船东需要确认港口能否提供相应电力，否则大电池本身不足以支撑商业运营。

**「后续看点」** 后续可关注船东或港口是否公布 BRF Froan 的运营航线、充电方案和首航时间；这些信息将检验 23.5 MWh 电池在商业散货运输中的实际可用性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://interestingengineering.com/transportation/worlds-largest-electric-bulker-carrier">World’s largest electric cargo ship with 23.5 MWh battery set ...</a></li>
<li><a href="https://www.bergerederi.no/froan">BRF Froan - Berge Rederi AS</a></li>

</ul>
</details>

**标签**: `#electric shipping`, `#batteries`, `#cargo ship`, `#maritime decarbonization`, `#23.5 MWh`

---

<a id="item-ev-energy-4"></a>
### [丰田确认汉兰达 9X 于 2027 年初上市，成为品牌首款增程电动车](https://electrek.co/2026/11/27/toyota-confirms-highlander-9x-first-erev-top-tier-tech/) ⭐️ 7.0/10

丰田确认，汉兰达（Highlander）9X 将于 2027 年初开卖，成为该品牌首款增程式电动车（EREV：车轮由电机驱动，电池可由车内发动机发电补充），并将采用华为和宁德时代（CATL）的新技术。据 Electrek 报道，这是丰田首次把增程车型列入产品线，但官方未公布电池容量、纯电续航、动力参数、售价和具体销售市场。目前关于技术来源的说法只到“来自华为和宁德时代”这一层，哪一方提供电池、电驱或智能座舱、辅助驾驶系统，报道并未说明。

Electrek · 11月27日 17:18

**「已证实与未证实」** 已证实：据 Electrek 报道，丰田确认汉兰达 9X 将于 2027 年初上市，是丰田首款增程式电动车，并使用华为与宁德时代的技术。
尚未证实：电池容量、纯电续航、动力参数、售价、首发市场，以及华为与宁德时代各自供应的具体部件均未公布；也没有第三方测试或量产车验证。

**「背景」** 增程式电动车（EREV）的车轮由电机驱动，车上的汽油发动机主要用于发电、为电池或电机补能，因此驾驶感受接近纯电动车，同时不必完全依赖充电桩。广汽丰田曾在 2025 年 6 月的技术日上表示，下一代汉兰达和赛那将由中方工程师主导开发，并采用增程动力；此次 9X 的确认正是这一计划的延续。

**「为什么重要」** 对考虑三排座家用 SUV 的买家来说，丰田首次进入增程阵营意味着多了一个品牌选项，但要真正比较，还需等官方公布续航与价格。对丰田而言，这款车的电池和关键技术由中国供应商提供，因此该车型的成本与交付节奏将与这些合作方相关。

**「后续看点」** 在 2027 年初开卖前，丰田需要公布汉兰达 9X 的正式参数与售价；届时可对照其纯电续航和增程器效率，判断它与现有增程车型的实际差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://carnewschina.com/2026/11/25/toyota-highlander-erev-expected-to-debut-in-china-on-november-27/">Toyota Highlander EREV expected to debut in China on November 27</a></li>

</ul>
</details>

**标签**: `#Toyota`, `#EREV`, `#Highlander 9X`, `#CATL`, `#Huawei`

---

<a id="item-ev-energy-5"></a>
### [美国国会通过电动自行车电池安全立法，自愿标准将转为强制](https://electrek.co/2026/11/27/congress-just-passed-a-major-e-bike-safety-law-heres-what-it-actually-means/) ⭐️ 7.0/10

Electrek 11 月 27 日报道，美国国会通过了一项立法，把此前在全美基本属于自愿遵守的电动自行车电池安全标准，转变为强制性的联邦要求。报道称这些标准“即将”成为强制规定，说明法案尚未正式生效，目前也没有任何产品层面的合规义务已经落地。报道只给出了这一总体判断，没有说明法案名称、引用的是哪一套具体标准、生效时间表或违规处罚。

Electrek · 11月27日 11:24

**「已证实与未证实」** 已证实：据 Electrek 报道，美国国会通过了一项立法，将把电动自行车电池安全标准从自愿性质改为联邦强制要求。
尚未证实：报道没有披露法案名称与编号、所援引的具体标准（例如具体的技术规范编号）、生效日期、过渡期安排、处罚条款，也没有说明是否已送交总统签署；关于“重大”这一评价以及实际执行力度，目前仅有该媒体的表述，尚无独立核实。

**「背景」** 美国电动自行车锂电池安全此前主要依靠自愿性标准，例如针对整车电气系统的 UL 2849 和针对电池组的 UL 2271，厂商可自行决定是否送检认证。据 BikeTips 报道，美国消费品安全委员会（CPSC）已于 2026 年 6 月 24 日提出 16 CFR Part 1265 拟议规则，拟将锂离子电池安全标准变为对电动自行车等微型出行设备的强制要求；倡导组织 PeopleForBikes 则表示，参议院通过的法案要求 CPSC 在法案生效后 180 天内发布最终规则，把 UL 标准确立为强制性联邦安全标准。

**「为什么重要」** 对在美销售电动自行车的品牌、进口商和零售商而言，合规方式将从“自愿参照标准”变为需要证明符合联邦强制要求，这意味着电池与充电系统的检测、认证和供应链文件将成为准入条件，而非加分项；在具体标准与生效日期公布前，相关企业不宜按现行自愿规范安排明年的产品认证计划。

**「后续看点」** 关注该法案是否完成签署程序并正式成法，以及负责执行的联邦机构后续公布的具体标准编号、生效日期和过渡期安排。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://biketips.com/cpsc-ebike-battery-safety-rule-2026/">New Federal E-Bike Battery Rule: What Riders Should Know</a></li>
<li><a href="https://www.peopleforbikes.org/news/senate-passes-battery-safety-bill">Senate Passes Bill to Strengthen Federal Safety Standards for ...</a></li>

</ul>
</details>

**标签**: `#e-bike safety`, `#battery regulation`, `#federal policy`, `#micromobility`

---

<a id="item-ev-energy-6"></a>
### [Arriva 获荷兰北荷兰省约 20 亿欧元电动巴士合同](https://www.electrive.com/2026/11/28/arriva-secures-two-billion-euro-contract-for-electric-buses-in-north-holland/) ⭐️ 7.0/10

Arriva 赢得了荷兰北荷兰省西北部的一份长期巴士运营合同，金额约 20 亿欧元，内容包括投入 200 多辆电动巴士，并调整该地区的线路网络。据 electrive 报道，这是 Arriva 在荷兰接连拿下多份大合同之后的又一次扩张。报道没有披露合同期限和巴士制造商，也没有说明这 20 亿欧元中有多少用于车辆采购、多少用于日常运营，因此车队何时上路、采用哪家车型目前都无从判断。

Electrive · 11月28日 09:00

**「已证实与未证实」** 已证实：Arriva 官方新闻稿以及 Sustainable Bus、Bus News 的报道均确认，Arriva 赢得荷兰北荷兰省西北部为期 13 年的公交特许经营合同（另有两年续约选项），合同价值约 20 亿欧元，是 Arriva 历史上最大的巴士合同；服务将于 2028 年 7 月启动，届时投入超过 200 辆巴士组成的 100% 纯电车队，并扩充线路、提高班次密度、增加接驳。
尚未证实：20 亿欧元中车辆采购与运营各占多少、其中新购电动巴士有多少辆（“超过 200 辆”包含现有车辆与新增车辆）、电动巴士由哪家厂商供应，目前均无披露；合同是否已完成正式签署，也只有 Arriva 一方的说法。

**「背景」** 在荷兰，公交服务通常由省或区域交通机构以多年期特许经营合同整体招标，中标运营商在合同期内获得指定线路网络的运营权，并按合同要求更新车队。Arriva 此前已在荷兰拿下多份同类公交合同，此次北荷兰合同是其在该国业务扩张的延续。

**「为什么重要」** 对北荷兰省西北部的通勤者来说，最直接的变化是车队电动化与线路重划同时落地：200 多辆电动巴士将替换现有车队，线路网络也随之调整，乘客需要按新线路重新规划换乘。据 GreenYourRoute 的梳理，北荷兰省内另外两个由省政府负责的公交特许经营区分别运营至 2027 年和 2028 年，且已与运营商 Transdev 制定过渡计划，因此 Arriva 这份合同将成为该省零排放公交（指不排尾气的纯电动或氢燃料巴士）转换中规模最大的一块。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sustainable-bus.com/news/arriva-north-holland-new-contract-netherlands/">Arriva wins €2 billion bus contract in the Netherlands, with ...</a></li>
<li><a href="https://news.arriva.co.uk/news/arriva-strengthens-position-in-the-netherlands-with-major-2bn-bus-contract">Arriva strengthens position in the Netherlands with record € ...</a></li>
<li><a href="https://bus-news.com/arriva-awarded-record-e2-billion-contract-for-holland-based-services/">Arriva Awarded Record €2 Billion Contract for Holland-Based ...</a></li>
<li><a href="https://www.greenyourroute.com/zero-emission-buses-holland">Province of Noord- Holland goes for Zero - Emission Buses</a></li>

</ul>
</details>

**标签**: `#electric buses`, `#fleet electrification`, `#public transport`, `#Netherlands`, `#contracts`

---

<a id="item-ev-energy-7"></a>
### [宁德时代发布 100kWh“30\#”换电电池包，换电不到一分钟](https://www.electrive.com/2026/11/27/catl-introduces-100kwh-30-swappable-battery-for-passenger-cars/) ⭐️ 7.0/10

宁德时代在中国面向乘用车推出一款名为“30\#”的换电电池包，容量 100 kWh。据该公司介绍，换电过程可在不到一分钟内完成；该电池包也可以在普通充电站进行快充，并非只能依赖换电站补能。这是一次产品发布，目前还不等于用户已经可以买到：报道没有给出电芯化学体系、适配哪些车型、换电站的部署范围以及价格。

Electrive · 11月27日 14:30

**「已证实与未证实」** 已证实：据 electrive 报道，宁德时代发布面向中国换电体系的“30\#”电池块，容量为 100 kWh，换电时间不到一分钟，也可在常规充电站快充。
尚未证实：99 秒换电、600 kW 峰值放电、3 秒级零百加速、约 700 公里（435 英里）CLTC 续航、锁止机构 27 年理论寿命等说法，都来自其他媒体报道或转述宁德时代的宣称；网络内电池终身质保仅见于单一报道。这些均无独立测试验证，车辆适配、部署时间和价格也未公布。

**「背景」** 换电指车辆在换电站把电量耗尽的电池包整块卸下、换上已充满的电池包，而不是插枪等待充电；其前提是电池包规格标准化，并与特定车型和换电站网络绑定。宁德时代（CATL）在中国已有一套换电生态，“30\#”是加入这一生态的新电池包。报道特别提到，这个可换电的电池包也能在普通充电站快充，也就是说补能并不局限于换电站。

**「为什么重要」** 同一个电池包同时支持换电和常规快充，意味着换电车型在换电站尚未覆盖的地区仍能借助公共快充补能，从而降低对换电网络密度的依赖。但适配车型、上市时间和价格尚未公布，其他品牌的车主目前还无法判断自己的车能否使用这种电池包。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://interestingengineering.com/energy/catl-100kwh-chocolate-battery-435-mile-range">CATL &#x27;s 100 kWh swappable battery offers 435-mile range for EVs</a></li>
<li><a href="https://carnewschina.com/2026/11/27/catl-unveils-30-chocolate-battery-with-a-100-kwh-capacity/">CATL unveils 30# Chocolate swappable battery with a 100 kWh ...</a></li>
<li><a href="https://beyondeastmedia.com/articles/catl-chocolate-battery-30-100kwh-3s-acceleration">CATL Unveils 30# Chocolate Battery with 100 kWh Pack and...</a></li>

</ul>
</details>

**标签**: `#CATL`, `#battery swapping`, `#EV batteries`, `#China`, `#fast charging`

---

## 航天

<a id="item-space-1"></a>
### [Stoke Space 新星一级抵达 SLC-14，目标 2027 年初首飞](https://www.nasaspaceflight.com/2026/11/stoke-nova-booster-slc-14-2027-debut/) ⭐️ 7.0/10

据 NASASpaceflight 报道，Stoke Space 的 Nova Pathfinder 火箭一级于 11 月 22 日经 17 天公路运输，从华盛顿州抵达佛罗里达州卡纳维拉尔角太空军基地的 14 号发射复合体（SLC-14），并已进入该设施的水平总装厂房。接下来它将进行一系列“pad-in-the-loop”湿式演练（WDR，即加注低温推进剂并完整走一遍发射流程的合练），这也是该历史发射台自 1960 年代以来首次有火箭进驻。一级完成合练后需返回总装厂房安装剩余 Zenith 发动机，再回发射台做静态点火；二级则计划 12 月在摩西湖试验场与 Andromeda 发动机对接后静态点火。首飞目标为 2027 年初，目前七台 Zenith 发动机中已有四台通过验收测试，其余三台仍在测试。

NASASpaceflight · 11月27日 14:52

**「已证实与未证实」** 已证实：一级已于 11 月 22 日抵达 SLC-14 并进入水平总装厂房；二级在摩西湖已完成贮箱结构验证（各贮箱加压至设计压力的 110%）和一次以液氢液氧为推进剂的全流程湿式演练；七台 Zenith 发动机中有四台完成验收测试——这些数据来自 Stoke Space 与 NASASpaceflight 的报道。
尚未证实：2027 年初首飞只是目标时间，尚无确定的发射日期；湿式演练与两次静态点火能否按计划通过、剩余三台 Zenith 何时完成验收并运抵佛罗里达，均未得到确认；报道中提到的 Block 2 重型构型与融资细节因原文截断而无法核实。

**「背景」** SLC-14 是卡纳维拉尔角太空军基地的历史发射台；据 NASASpaceflight 报道，自 20 世纪 60 年代以来，这里首次重新有火箭进驻。Nova 是 Stoke Space 正在研制的两级可重复使用轨道火箭，Pathfinder 则是用于首次轨道试飞的试验箭。Stoke 在公司声明中表示，2026 年的测试旨在摸清 Pathfinder 的性能边界，这些数据也将用于后续的 Nova Block 2 重型版本。

**「为什么重要」** 对 Stoke 而言，这轮地面测试是首飞前最后一道关卡：剩余三台 Zenith 发动机必须完成验收并运抵佛罗里达，一级静态点火才能进行，任何延误都会直接压缩 2027 年初首飞的时间窗口。更关键的是二级——Andromeda 把液氢液氧推进系统直接集成进主动冷却的金属热防护罩，以替代烧蚀材料或陶瓷瓦，而该发动机此前只在单机层面累计过 242 次点火，12 月的整级静态点火将是这套方案首次以完整二级形态点火。

**「后续看点」** 12 月在摩西湖试验场进行的 Nova 二级静态点火：届时二级将与已验收的 Andromeda 发动机对接。之后是一级在 SLC-14 的静态点火，以及一二级在总装厂房的对接。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.stokespace.com/news/pathfinder-arrives-at-launch-site">PATHFINDER ARRIVES AT LAUNCH SITE | Stoke Space</a></li>

</ul>
</details>

**标签**: `#Stoke Space`, `#Nova Pathfinder`, `#SLC-14`, `#launch vehicle development`, `#wet dress rehearsal`

---

## 科技产业与政策

<a id="item-tech-industry-1"></a>
### [SAP 确认 GitHub 安全事件，源代码据报遭复制篡改](https://www.techmeme.com/261127/p9#a261127p9) ⭐️ 7.0/10

SAP 确认发现 GitHub 上的可疑活动，构成一起网络安全事件。SecurityWeek 报道称，黑客利用窃取到的 SAP 员工身份认证令牌（可代替密码访问代码仓库的凭据），复制并修改了托管在 GitHub 上的源代码。SAP 的确认目前只覆盖“可疑活动/安全事件”，令牌被盗和代码被改动仍属报道内容，现有报道未披露受影响仓库、代码范围或修复状态。

Techmeme · 11月27日 16:35

**「已证实与尚未证实」** 已证实：SAP 向 SecurityWeek 确认检测到 GitHub 上的可疑活动，并将其定性为一起网络安全事件；SAP 自身的表态是这一确认的依据。
尚未证实：攻击者利用窃取的 SAP 员工认证令牌复制并篡改 GitHub 上的源代码，这一说法目前仅来自《明镜》周刊（DER SPIEGEL）的报道及知情人士转述，SAP 未公开证实；受影响代码的具体范围、是否涉及客户产品、事件时间线以及是否已通知监管机构或客户，现有报道均未说明，也未见独立的第三方取证结论。

**「背景」** GitHub 的访问令牌（token）是替代密码的凭据，携带有效令牌的请求会被 GitHub 视为该员工本人发出，因此攻击者不必攻破 GitHub 平台本身，就能读取或推送代码。SecurityWeek 报道称，此次事件中被盗的员工令牌正是被用来复制并修改 SAP 存放在 GitHub 上的源代码；SAP 确认的是发现可疑活动，令牌与代码改动的细节目前仍来自该媒体报道。

**「为什么重要」** 如果报道属实，关键后果是代码完整性而非单纯泄露：被修改的代码提交是否进入构建或发布流程，决定影响是否延伸到 SAP 的软件交付和客户部署。SAP 需要说明受影响仓库和提交记录，使用其软件的组织则应等待范围说明，再判断是否要检查自身部署或更新依赖。

**「后续看点」** 接下来看 SAP 是否发布正式事件通告，披露受影响仓库、令牌撤销范围以及是否有被改代码进入构建或发布；也可关注 GitHub 安全公告或 SecurityWeek 的后续报道是否给出独立验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.securityweek.com/sap-confirms-cyberattack-source-code-reportedly-compromised/">SAP Confirms Cyberattack, Source Code Reportedly... - SecurityWeek</a></li>
<li><a href="https://cybersecuritynews.com/sap-security-incident/">SAP Confirms Security Incident as Hackers Reportedly Steal ...</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/sap-confirms-security-incident-after-suspicious-github-activity/">SAP confirms security incident after suspicious GitHub activity</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#SAP`, `#source code`, `#GitHub`, `#security incident`

---

<a id="item-tech-industry-2"></a>
### [AMD 与 Winbond 固件漏洞让 BitLocker PIN 可被快速暴力破解](https://www.tomshardware.com/tech-industry/cyber-security/amd-and-winbond-vulnerabilities-let-attackers-brute-force-bitlocker-pins-on-millions-of-pcs-cracking-a-six-digit-pin-drops-from-19-years-to-20-days) ⭐️ 7.0/10

柏林工业大学（Technische Universität Berlin）的研究者在 arXiv 论文中披露，AMD 负责与非易失存储通信的 fTPM 固件，以及 Winbond 支持 RPMC（回滚保护）的 SPI 闪存芯片，都存在缺陷：攻击者只要能够物理接触设备，并加装一块低成本转接板，就能让记录解锁失败次数的计数器不增加，从而绕过“连续 32 次尝试后每次需等待 10 分钟”的限制。按正常机制穷举六位数字 PIN 需要约 19 年；Tom&\#x27;s Hardware 称攻击可把这一时间压缩到数天甚至数小时，其标题给出的六位 PIN 数字为 20 天。研究者在从 Zen 2 到锐龙 AI 5 330 的 AMD 机型上至少验证了其中一种攻击，并推测所有使用 fTPM 的当代 AMD 消费级平台都可能受影响；Winbond 方案则可借电压毛刺读出 HMAC 密钥，该厂商在 SPI 闪存市场约占 25% 份额，因此潜在受影响设备达数百万台。截至报道时，涉事公司均未承诺修复根因漏洞：Winbond 路径只能更换芯片，AMD 路径需通过 AGESA 固件更新、并依赖 OEM 发布 BIOS；微软只是在设置流程中改为建议用户使用六位 PIN 而非四位。

Tom&\#x27;s Hardware · 11月27日 12:30

**「已证实与未证实」** 已证实：柏林工业大学研究团队的论文《Hello Again: Exploiting Replay Protected…》已发布在 arXiv（编号 2611.18126，11 月 13 日），摘要称团队在锁定且加密的真实硬件上完成端到端演示，正常限速下需 69 天才能试出的 4 位 Windows Hello PIN，其装置 40 小时即破解；论文与 Tom&\#x27;s Hardware 的报道都确认，攻击需要接触设备本体。

尚未证实：受影响设备到底有多少，目前只是按 Winbond 约占 SPI 闪存 25% 市场份额推算出的「数百万台」；「所有现代 AMD 平台均可能受影响」也只是推断，实测只覆盖 Zen 2 到 AI 5 330 机型，Winbond 侧只对两款芯片做了故障注入；「无厂商承诺修复根因、微软仅建议改用六位 PIN」出自论文作者说法与媒体转述，尚不见厂商公开回应或第三方复现；CVE-2026-43613 编号只见于二手报道。两处数字口径也不一致：Tom&\#x27;s Hardware 称六位数字 PIN 的破解时间从 19 年缩短到 20 天，论文摘要给出的则是四位 PIN 从 69 天缩短到 40 小时。

**「背景」** 现代 x86 消费级电脑普遍用「固件可信平台模块」（fTPM）代替独立安全芯片：它运行在 CPU 固件里，而记录解锁失败次数的计数器则被加密存放在主板上的 SPI Flash 芯片中（这块芯片同时存放 BIOS 等固件）。按正常设计，BitLocker 允许连续 32 次尝试，之后每次都要等待 10 分钟，因此六位数字 PIN 需约 19 年才能穷举完。TPM 与 SPI 芯片之间的命令靠 HMAC 密钥签名，部分 Winbond 芯片还带有 RPMC 回滚保护，用来防止计数器被篡改或被还原到旧状态——这两道防线正是本次研究攻击的目标。

**「为什么重要」** 这些攻击针对的正是磁盘加密要防范的场景——设备被偷；对已过保修期的 AMD 或 Winbond 机型，修复要走“AGESA 更新 → OEM 发布 BIOS”这条漫长的链条，而参考 Spectre/Meltdown 时期的经验，旧设备常被厂商跳过，所以这些机器可能长期无法修补。对高风险用户而言，现实可行的缓解手段是把 PIN 改为更长的字母数字口令，但这只能拉长破解时间，并不能消除计数器可被绕过的缺陷；同时论文指出，该问题很可能同样适用于 BitLocker 之外其他基于 fTPM 的磁盘加密方案。

**「后续看点」** 接下来值得关注的是 AMD 是否会发布包含该缺陷修复的 AGESA 固件，以及各 OEM 厂商是否、何时为受影响的整机（尤其是已过支持期的旧机型）推送相应 BIOS 更新。另一个可查的节点是微软推荐使用六位 PIN 的策略何时真正落实到 Windows 的安装与设置流程中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2611.18126v1">[2611.18126v1] Hello Again: Exploiting Replay Protected ...</a></li>
<li><a href="https://secnews.co.uk/2026/11/tpm-lockout-reset-rpmc-attack-bitlocker-windows-hello-pins-cve-2026-43613/">Flash chip attack resets TPM lockout to crack BitLocker and ...</a></li>
<li><a href="https://pro-gamer.gg/amd-winbond-cve-2026-43613-bitlocker-pin-20-days-ryzen-pcs/">AMD Ryzen &amp; Winbond Flaws Cut BitLocker Cracking to 20 Days</a></li>

</ul>
</details>

**标签**: `#BitLocker`, `#hardware security`, `#AMD`, `#Winbond`, `#vulnerability research`

---