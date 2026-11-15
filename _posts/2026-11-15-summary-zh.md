---
layout: issue
permalink: /zh/briefing/2026-11-15/
title: "AI 新闻简报：2026年11月15日"
date: 2026-11-15
lang: zh
---

> 过去一天共筛查 119 条科技资讯，留下最值得读的 13 条。

---

**人工智能**
1. [美团发布 1.6 万亿参数 LongCat-2.5 智能体模型权重](#item-ai-news-1) ⭐️ 8.0/10
2. [Lovable 生成应用被曝泄露护照信息与 20 多万条私信](#item-ai-news-2) ⭐️ 7.0/10
3. [Amodei 称买算力是最大难题，Anthropic 近 9010 亿美元承诺临近 IPO](#item-ai-news-3) ⭐️ 7.0/10
4. [Meta FAIR/NYU：视觉编码器预训练可省，视觉专用参数不可省](#item-ai-news-4) ⭐️ 7.0/10

**芯片与算力**
1. [WSJ：英伟达 AI 芯片经东南亚数据中心流向中企](#item-chips-compute-1) ⭐️ 8.0/10
2. [纽约时报：卢特尼克推动收窄涉及其前公司客户的芯片管制](#item-chips-compute-2) ⭐️ 7.0/10
3. [台积电拟设 5 亿美元基金投资芯片初创与上游伙伴](#item-chips-compute-3) ⭐️ 7.0/10

**机器人与自动驾驶**
1. [Nidus 融资 3000 万美元，开发国防制造机器人 AI 技术](#item-robotics-autonomy-1) ⭐️ 7.0/10

**电动车与新能源**
1. [东风日产 NX7 插混开启预订：40 kWh 电池、纯电续航近 200 英里](#item-ev-energy-1) ⭐️ 7.0/10
2. [特斯拉 Model Y 后驱版 EPA 续航升至 348 英里，价格不变](#item-ev-energy-2) ⭐️ 7.0/10

**航天**
1. [SpaceX 首次用发射塔接住从轨道返回的星舰](#item-space-1) ⭐️ 10.0/10

**科技产业与政策**
1. [FBI 查封朝鲜&quot;FaceStealer&quot;攻击所用的云基础设施](#item-tech-industry-1) ⭐️ 8.0/10
2. [EFF 请求上诉法院为车牌识别数据库查询设立搜查令要求](#item-tech-industry-2) ⭐️ 7.0/10

---

## 人工智能

<a id="item-ai-news-1"></a>
### [美团发布 1.6 万亿参数 LongCat-2.5 智能体模型权重](https://the-decoder.com/meituan-releases-a-1-6-trillion-parameter-agent-model-that-never-touched-an-nvidia-gpu/) ⭐️ 8.0/10

美团已发布 LongCat-2.5 的模型权重，这是一个面向 AI 智能体的 1.6 万亿参数模型；据 The Decoder 报道，其训练全程使用中国硬件，示例部署运行在 194 颗华为升腾芯片上，报道未提及英伟达 GPU。该报道称其在 Terminal Bench 上得分 88.4，仅次于 Claude Opus 5。上述性能与硬件细节目前来自简短转述，尚缺独立复现和完整技术披露。

The Decoder · 11月15日 10:06

**「已证实与未证实」** 已证实：据 The Decoder 报道，美团已发布 LongCat-2.5 的模型权重，这是一个 1.6 万亿参数、面向 AI agent 的模型；报道称其在 Terminal Bench 上得分 88.4，样本部署运行在 194 颗华为升腾芯片上，且美团在材料中未提及使用 Nvidia GPU。
尚未证实：88.4 的 Terminal Bench 分数与“训练全程未使用 Nvidia GPU”均来自美团自身或单一媒体的转述，没有独立第三方复现或基准测试细节；报道未给出训练算力规模与成本、模型许可证条款、上下文长度，也未列出 Claude Opus 5 在该基准上的具体分数，因此“仅次于 Opus 5”的排名幅度无法核实。

**「背景」** 开放权重（open-weight）指模型训练完成后的参数可被外部下载并自行部署，区别于只能通过 API 调用的闭源模型；面向智能体的模型则强调在多步任务中调用工具和执行操作。Terminal Bench 是文中用于评分的终端任务基准，LongCat-2.5 报告的 88.4 分即来自这项测试。

**「为什么重要」** 对希望自建智能体模型的开发者，开放权重提供了在非英伟达硬件栈上部署的选项，但样例使用 194 颗升腾芯片，实际适配、吞吐与成本仍需自行验证，Terminal Bench 成绩也有待独立复现。

**标签**: `#Meituan`, `#LongCat-2.5`, `#agent models`, `#Huawei Ascend`, `#open-weight models`

---

<a id="item-ai-news-2"></a>
### [Lovable 生成应用被曝泄露护照信息与 20 多万条私信](https://www.crissyfield.de/research/lovable-en/) ⭐️ 7.0/10

安全研究团队 Crissy Field 发布报告称，用 AI 应用构建工具 Lovable 生成的部分应用暴露了护照信息以及超过 20 万条私人消息，原因是数据库的行级安全（Row-Level Security，RLS，即让数据库按行判断谁能读写的规则）配置不足。Lovable 安全负责人 igorandri 在讨论中确认，问题根源正是 RLS 配置不足，并表示平台会在每次发布前自动扫描应用、向所有用户免费提供更深入的 SAST（静态应用安全测试）扫描，并支持用户点选“修复”、开启后台自动修复以及拦截发布。报告作者 neathack 证实该文两周前曾提交到 Hacker News 但未获关注，此次重新提交后才引发讨论。现有材料未说明受影响应用的具体数量与泄露数据的完整范围。

Hacker News · armcat · 11月14日 17:43 · [社区讨论](https://news.ycombinator.com/item?id=50499017)

**「已证实与未证实」** 已证实：博客作者在讨论中确认文章由其本人撰写并提交至 Hacker News；Lovable 安全负责人 Igor 在公开回复中承认，涉事应用的根因是行级安全（Row-Level Security，RLS，即数据库按行限制谁能读到哪些数据的规则）配置不足，并表示 Lovable 会在每次发布前自动扫描应用、另提供更深入的 SAST（静态应用安全测试）扫描，两项对所有用户免费，用户可点选“修复”或开启后台自动修复。

尚未证实：护照信息与“超过 20 万条私信”的具体暴露规模目前仅出自该研究者单方报告，素材中未提供原文正文，Lovable 也未确认受影响应用数量、具体数据类型或是否已通知受影响用户；另有评论者称 Supabase 相关默认设置在 10 月 30 日“据称已修复”，但存在既有项目仍沿用旧默认值的说法，这一时间点与生效范围尚无双方一致的确认。

**「背景」** Supabase 是以 Postgres 为核心的后端服务，应用前端可以直接调用其接口读写数据库；行级安全（Row-Level Security，RLS）是 Postgres 在数据库层按用户或角色限制可访问数据行的机制。Lovable 这类 AI 应用构建器生成的应用常采用前端直连 Supabase 的结构，一旦 RLS 策略缺失或设置过宽，数据库就可能把不同用户的数据暴露给任何能访问该应用的人。

**「为什么重要」** 对用 Lovable 搭配 Supabase 快速搭建应用的开发者来说，前端直连数据库意味着真正的安全边界只剩 RLS 策略本身，因此上线前应逐表启用 RLS 并核对策略，而不是依靠前端隐藏界面或字段。评论者 SOLAR\_FIELDS 指出，Supabase 历史上为降低上手门槛而默认不开启 RLS，这一默认值据称已在 10 月 30 日修复，但有反馈称既有项目仍沿用旧默认——这属于社区说法，官方未在本次材料中确认。

**「社区讨论」** 评论者 yakkomajuri 表示，让前端直接与 Supabase 后端通信再加 RLS 一直是“雷区”，他更愿意把 Supabase 当作普通 Postgres 从自己的后端连接。SOLAR\_FIELDS 认为 Supabase 也应承担责任，因为 RLS 默认关闭是其多年前为简化注册流程而做出的主动取舍，并链接 Supabase 的 GitHub 讨论称修复只对新建项目生效；igorandri 则以 Lovable 安全负责人身份回应，强调扫描与自动修复功能免费开放。

**标签**: `#AI app builders`, `#vibe coding`, `#security`, `#data exposure`, `#Supabase`

---

<a id="item-ai-news-3"></a>
### [Amodei 称买算力是最大难题，Anthropic 近 9010 亿美元承诺临近 IPO](https://the-decoder.com/anthropic-ceo-amodei-admits-theres-a-huge-uncertainty-in-whats-going-to-happen-next-year-days-before-a-record-ipo/) ⭐️ 7.0/10

距可能成为史上最大规模 IPO 仅剩数天，Anthropic CEO Dario Amodei 称购买算力是公司面临的“最深的商业难题”（deepest business dilemma），公司相关承诺总额已接近 9010 亿美元，而未来收入能否覆盖这些成本仍远不明朗。据 The Decoder 报道，此次 IPO 在很大程度上被定位为对冲这一不确定性的资金缓冲。Amodei 还表示“明年会发生什么存在巨大的不确定性”。需要说明的是，这是一篇简短转述报道，未点名原始采访或发言场合，也未披露这近 9010 亿美元承诺的构成、期限，以及 IPO 的具体估值与日期。

The Decoder · 11月14日 19:05

**「已证实与未证实」** 已证实：据 The Decoder 报道，Anthropic CEO Dario Amodei 将购买算力称作公司面临的“最深刻的商业困境”，并承认“明年会发生什么存在巨大不确定性”；报道还称公司即将启动一桩可能创纪录的 IPO，并把这次上市视为应对上述不确定性的财务缓冲。以上均为该媒体的转述，文中未给出发言原文、场合或 Anthropic 的一手声明。

尚未证实：承诺总额存在明显矛盾——The Decoder 称接近 9010 亿美元，而其他媒体引述的 IPO 文件显示为 5180 亿美元（tool-1-2、tool-1-3），两者相差近 4000 亿美元，无法判断哪一个准确；IPO 的募资规模、估值与具体日期同样没有在本文中给出可核对数字，“史上最大 IPO”仍属待验证说法，另有报道称其规模与估值口径不一（tool-1-1），高盛关于 2030 年年收入超 6000 亿美元的预测则是投行估算而非公司指引（tool-1-1）。

**「背景」** 在 AI 行业，算力承诺通常指企业通过多年期合同提前锁定云服务和芯片产能，这类支出往往在收入兑现之前就已确定，因而会形成长期的财务义务。报道提到，Anthropic 的承诺总额接近 9010 亿美元，而计划中的 IPO 被描述为应对未来收入不确定性的资金缓冲。

**「为什么重要」** 对准备参与此次 IPO 的投资者来说，真正需要核对的不是发行规模，而是承诺的结构：报道没有说明这近 9010 亿美元中有多少属于不可撤销的长期算力采购合同、多少随实际用量浮动；这些条款一旦在招股书中披露，将决定上市后成本风险由公司还是由公开市场股东承担。

**「后续看点」** 据 Cleus 截至 11 月 3 日 的梳理，Anthropic 尚未确定发行价区间或 IPO 日期；接下来值得关注的是公开版 S-1 招股书何时披露，以及其中是否会把近 9010 亿美元的算力承诺与对应营收预期并列列出，供投资者自行判断。定价区间一旦公布，将是检验市场是否接受这一承诺规模的首个硬指标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.zerohedge.com/markets/anthropic-launches-100-billion-ipo-worth-14-trillion-or-10-trillion-depending-whos-counting">Anthropic Launches $100 Billion IPO Worth $1.4 Trillion... | ZeroHedge</a></li>
<li><a href="https://www.martincid.com/business/anthropic-ipo-dario-amodei-no-hedge-on-earth-compute/">Anthropic IPO Filing Puts CEO Dario Amodei ’s ‘No Hedge on Earth...</a></li>
<li><a href="https://www.thestreet.com/technology/anthropic-ipo-filing-reveals-518-billion-ai-investment-dario-amodei">Anthropic &#x27;s IPO filing reveals a staggering AI bet - TheStreet</a></li>
<li><a href="https://cleus.ai/blog/anthropic-ipo-filing-s1-explained">Anthropic IPO Filing : $17B Revenue, $23B Loss... | Cleus Blog</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#AI business`, `#IPO`, `#compute costs`, `#AI infrastructure`

---

<a id="item-ai-news-4"></a>
### [Meta FAIR/NYU：视觉编码器预训练可省，视觉专用参数不可省](https://www.reddit.com/r/MachineLearning/comments/1xx1k2o/meta_fair_nyu_unbundling_multimodal_vision/) ⭐️ 7.0/10

Meta FAIR 与 NYU 的研究者从零训练 200 多个多模态大模型，逐项拆开视觉编码器的三个选择：是否单独预训练、是否保留视觉专用参数、以及是否放在 LLM 之前；主要比较用 Qwen3-1.7B 和 4B 配置、0.4B 视觉容量，并在 16 个 Cambrian VQA 基准（448 像素）和 12 个语言基准上评测。作者称，在总计算预算相同的情况下，用对比学习、自监督或两种描述目标预训练的编码器最多只能与从零联合训练的编码器表现相当，连“免费”预训练也没有帮助；把 MetaCLIP 预训练延长 6.5 倍，ImageNet 线性探针从 80.4% 升到 84.4%，但 VQA 没有提升。视觉专用参数则不可省：无编码器模型在 0.6B 到 6.4B 各规模上都落后，约需 3 倍计算才能追上；把编码器参数转给 LLM 改善的是文本而非 VQA。放置位置也可变：所谓 in-fusion 在 LLM 前 8 层加入零初始化的视觉专用权重，1.7B 到 6.4B 与独立编码器相当，首 token 时间低约 13%，1.7B 下 VQA 为 45.0，对比编码器的 44.4。

Reddit · r/MachineLearning · /u/trungh98 · 11月15日 17:38

**「已证实与未证实」** 已证实：预印本《Unbundling Multimodal Vision Encoding》确实已公开（arXiv 编号 2611.17334，标题亦出现在 arXiv cs.CV 最新列表中）；作者之一 /u/trungh98 在 r/MachineLearning 发帖说明，实验用同一份数据从零训练 200 多个多模态大模型，主对比基于 Qwen3-1.7B 与 4B 骨干加 0.4B 视觉参数，评测集为 Cambrian 的 16 个 448px VQA 基准和 12 个语言基准。
尚未证实：全部结论数字——视觉编码器预训练“最多打平”、无编码器模型需约 3 倍算力追平、in-fusion 降低约 13% 首 token 延迟、1.7B 下 45.0 对 44.4 的 VQA 分数——目前仅出自作者自述的预印本，未经同行评审或第三方复现；帖子本身是摘要，未列出完整基准表，也未交代“免费预训练”对照的具体设置。

**「背景」** 多模态大模型（MLLM）要“看图”，通常先由一个视觉编码器（vision encoder，把图像切块并编码成向量序列）处理图像，再把结果送进语言模型；这类编码器往往先在图像数据上单独预训练。业界做法目前并不统一：该帖举例说 Gemma 4 12B 去掉了编码器，Kimi K3 从零训练编码器，Inkling 2 Small 又把它加了回来。问题在于，已发布模型在训练数据、算力以及编码器预训练投入上各不相同，单靠横向比较无法判断究竟是哪一项选择在起作用。

**「为什么重要」** 对多模态模型构建者，最直接的动作是不要把“有没有预训练视觉编码器”当作架构成败的关键，而要把视觉 token 单独使用的参数保留下来；若选择无编码器路线，作者测得的约 3 倍计算追赶成本应计入预算。in-fusion 的约 13% 首 token 时间优势目前仅来自作者实验，迁移到其他 LLM 或训练配方时需重新验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/list/cs.CV/recent">Computer Vision and Pattern Recognition</a></li>

</ul>
</details>

**标签**: `#multimodal learning`, `#vision encoders`, `#MLLMs`, `#model scaling`, `#AI research`

---

## 芯片与算力

<a id="item-chips-compute-1"></a>
### [WSJ：英伟达 AI 芯片经东南亚数据中心流向中企](https://www.techmeme.com/261115/p1#a261115p1) ⭐️ 8.0/10

《华尔街日报》一篇调查报道称，英伟达 AI 芯片正通过东南亚的大型数据中心流向中国公司：这些设施利用了美国制裁的缺口，为中国企业提供关键算力，并为涉嫌的芯片走私提供掩护。报道标题称黄仁勋建立了一项规模达数十亿美元的业务来促成这类访问，但 Techmeme 只转引了标题和一句摘要，未交代涉及的国家、芯片型号、金额构成或英伟达的回应。相关指控尚未在现有材料中获得独立证实。

Techmeme · 11月15日 05:55

**「已证实与未证实」** 已证实：据《华尔街日报》调查报道（记者 Jon Emont、Stu Woo、Patricia Kowsmann、Raffaele Huang），东南亚的多座大型数据中心利用了美国制裁中的一处缺口，为中国企业提供关键算力，并成为涉嫌芯片走私的掩护；这是该报的调查结论，并非监管机构或法院的认定。
尚未证实：报道标题所称这是黄仁勋打造的“数十亿美元生意”，他本人是否知情或主导，以及走私的具体规模与路径，目前都只来自这一篇报道；素材中没有 Nvidia 或黄仁勋方面的回应，也没有官方指控或独立核实。相关公司 Megaspeed 据《纽约时报》报道正因涉嫌非法对华走私芯片接受美国政府调查，但尚无结论；各媒体对黄仁勋离任的性质说法也不一致，CNN 称其“承认婚外情后辞职”，彭博则用“ouster”（被赶下台）描述。

**「背景」** 美国自 2022 年起对输华先进 AI 芯片实施出口管制，Nvidia 一方面为中国市场提供降规产品，一方面由黄仁勋本人游说华盛顿放松限制（据 CNN 报道）。这类管制的边界是「向中国出口」：芯片只要不运进中国，而是装在中国周边（例如东南亚）的数据中心，再以云算力形式租给中国企业，在规则上就属于另一回事——这正是报道所指缺口的由来。此事曝光时，Nvidia 正处在领导层动荡之中：据 CNN 报道，黄仁勋近日辞去 CEO 职务；The Verge 则把这一辞职放在 10 月 29 日《纽约时报》有关他疑似成为中国情报目标的报道之后；美国财政部长 Bessent 已要求公司在 10 天内说明是否推动了「看似非法」的对华芯片销售。

**「为什么重要」** 如果这一路径成立，美国出口管制的实际边界就不只取决于芯片的直接出口目的地，还取决于对东南亚数据中心最终客户的审查；在东南亚运营或出租算力的公司可能面临更严格的合规追问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tovima.com/wsj/before-his-ouster-jensen-huang-belittled-the-executive-replacing-him/">Before His Ouster, Jensen Huang Belittled the Executive... - tovima.com</a></li>
<li><a href="https://www.nytimes.com/2026/11/15/us/politics/trump-lutnick-ai-chips-cantor-fitzgerald.html">Lutnick Pushed to Weaken Chip Rules That Overlap With His Family...</a></li>
<li><a href="https://edition.cnn.com/2026/11/14/tech/china-megaspeed-nvidia-scandal-hnk-intl">How the Nvidia scandal lifted the curtain on a loophole that’s giving...</a></li>
<li><a href="https://edition.cnn.com/2026/11/14/tech/china-megaspeed-nvidia-scandal-hnk-intl">How the Nvidia scandal lifted the curtain on a loophole that’s giving...</a></li>

</ul>
</details>

**标签**: `#export controls`, `#Nvidia`, `#AI data centers`, `#chip smuggling`, `#Southeast Asia`

---

<a id="item-chips-compute-2"></a>
### [纽约时报：卢特尼克推动收窄涉及其前公司客户的芯片管制](https://www.techmeme.com/261115/p9#a261115p9) ⭐️ 7.0/10

《纽约时报》11 月 15 日发表调查报道称，美国商务部长霍华德·卢特尼克（Howard Lutnick）推动收窄部分芯片出口管制规则的适用范围，而这些规则会影响东南亚的数据中心，其中一些正是其前公司坎托·菲茨杰拉德（Cantor Fitzgerald）的客户；报道称其中一处位于马来西亚的数据中心可能为腾讯提供服务。报道称，卢特尼克本人正在起草这些涉及东南亚数据中心的新规。材料没有披露具体规则条文、涉及哪些芯片或算力门槛、规则是否已定稿或生效，也没有给出商务部或坎托·菲茨杰拉德的回应。

Techmeme · 11月15日 16:10

**「已证实与未证实」** 已证实：据 Techmeme 转述，《纽约时报》于 11 月 15 日刊发调查报道，称美国商务部长霍华德·卢特尼克（Howard Lutnick）在起草新的芯片出口规则，这些规则将影响部分东南亚数据中心，而其中一些数据中心是其前律所／公司 Cantor Fitzgerald 的客户；报道还提到，马来西亚一处数据中心可能为腾讯提供服务。

尚未证实：所给材料仅为 Techmeme 的标题与一句摘要，未包含《纽约时报》原文的证据链，因此卢特尼克具体推动了哪些规则收窄、是否已生效、该马来西亚数据中心与腾讯的关系是否属实、Cantor Fitzgerald 目前与这些客户是否仍有业务往来，以及卢特尼克本人或商务部的回应，均未得到独立确认。

**「背景」** 坎托·菲茨杰拉德（Cantor Fitzgerald）是一家提供固定收益、股票资本市场、投行与资产管理等服务的金融服务公司，卢特尼克在进入政府任职前曾执掌该机构。美国商务部负责起草芯片出口管制规则；据《纽约时报》这篇调查，正在拟定的新规把约束范围延伸到东南亚的数据中心，也就是要处理「芯片经第三国机房最终服务中国客户」这一类路径。报道称，受影响的部分数据中心客户正是坎托·菲茨杰拉德的客户，其中一个位于马来西亚的设施可能为腾讯提供服务。

**「为什么重要」** 如果新规如报道所述被收窄，东南亚数据中心获取受控美国芯片的路径就可能改变，在该地区运营或租用算力的公司需要重新评估采购与合规安排；同时，由主管官员起草与其前公司客户直接相关的规则，这一情况可能引来利益冲突层面的审查，并影响规则最终以何种形式落地。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cantor.com/">Home - Cantor</a></li>

</ul>
</details>

**标签**: `#chip export controls`, `#AI data centers`, `#Malaysia`, `#Tencent`, `#policy influence`

---

<a id="item-chips-compute-3"></a>
### [台积电拟设 5 亿美元基金投资芯片初创与上游伙伴](https://www.techmeme.com/261115/p4#a261115p4) ⭐️ 7.0/10

据《日经亚洲》专访报道，台积电计划设立一只规模 5 亿美元的基金，用于投资有潜力的芯片初创公司、供应商及其他上游合作伙伴。报道引述台积电的说法称，公司“也想支持未来的英伟达”。目前公开的信息只有基金规模和大致投资方向；报道没有给出启动时间、投资阶段、单笔金额，也没有说明注资是否附带产能或供货安排，台积电尚未就此发布正式公告。Techmeme 的条目只是对这篇专访开头段落的转述，并非台积电的原始发布。

Techmeme · 11月15日 06:45

**「已证实与未证实」** 已证实：日经亚洲（Nikkei Asia）记者郑婷芳（Cheng Ting-Fang）的采访报道称，台积电计划设立一只规模 5 亿美元的风险基金，用于支持有潜力的芯片初创公司、供应商及其他上游合作伙伴，并引述台积电方面的话说“我们也想支持未来的英伟达”。这是目前唯一的一手表述来源，Techmeme 只是转载了该报道的摘要。

尚未证实：台积电官方尚未就此发布公告，报道也未说明基金名称、正式启动时间、具体的投资标的与单笔规模、由哪个部门管理，以及是否已获董事会批准；由于转载摘要被截断，5 亿美元这一数字之外的具体条款均无法从现有材料核实。

**「背景」** 台积电目前是全球最大的晶圆代工厂，以纯代工模式为苹果、英伟达等客户制造芯片，自身不销售自有品牌芯片。此次设立创投基金，是其以资本方式延伸至上游初创企业与供应商生态，与此前主要依靠产能和制程技术绑定客户的做法有所不同。

**「为什么重要」** 对于芯片初创公司和台积电的上游供应商来说，这意味着多了一个由全球最大代工厂主导的资金来源，在风险资本高度集中于 AI 的当下提供了另一条融资渠道。但报道并未说明投资是否与产能分配、供货优先权或采购协议挂钩，因此有意接洽的企业应先弄清基金的投资架构、决策流程和条款，而不应把获得注资等同于锁定代工产能。

**「后续看点」** 台积电是否正式公告这只基金的设立、投资架构与首批投资标的。

**标签**: `#TSMC`, `#semiconductor supply chain`, `#venture funding`, `#chip startups`, `#foundry`

---

## 机器人与自动驾驶

<a id="item-robotics-autonomy-1"></a>
### [Nidus 融资 3000 万美元，开发国防制造机器人 AI 技术](https://www.techmeme.com/261115/p5#a261115p5) ⭐️ 7.0/10

Nidus 在种子前轮（pre-seed）和种子轮中合计融资 3000 万美元，投资方包括 Kleiner Perkins 和 Costanoa。这家公司为美国国防工业企业的制造机器人开发 AI 技术，并称在四个月内从国防工业客户获得“七位数”美元订单额。报道未披露客户名称、产品是否已实际部署、订单交付时间或技术细节，因此这些数字目前仅为公司说法。

Techmeme · 11月15日 06:50

**「已证实与未证实」** 已证实：据 Upstarts Media 记者 Alex Konrad 报道，Nidus 在 pre-seed（种子前）和 seed（种子轮）两轮融资中合计筹集 3000 万美元，投资方包括 Kleiner Perkins 和 Costanoa。

尚未证实：所谓“四个月内与国防工业客户达成七位数（数百万美元）订单”仅是 Nidus 公司自己的说法；报道没有给出客户名称、合同金额或任何第三方核实，也没有披露两轮融资各自的具体金额、估值，以及相关机器人技术实际部署的规模。

**「背景」** “国防工业基础”指为美国军方供货的承包商及其各级供应商，Nidus 的技术面向这类工厂中的制造机器人。pre-seed（种子前轮）与 seed（种子轮）是创业公司最早的两轮融资，Nidus 将两轮合并募集，合计 3000 万美元。报道提到的投资方之一是 Kleiner Perkins，一家位于硅谷门洛帕克沙丘路的风险投资机构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kleinerperkins.com/">Home | Kleiner Perkins</a></li>

</ul>
</details>

**标签**: `#robotics`, `#manufacturing automation`, `#defense tech`, `#venture funding`, `#AI`

---

## 电动车与新能源

<a id="item-ev-energy-1"></a>
### [东风日产 NX7 插混开启预订：40 kWh 电池、纯电续航近 200 英里](https://electrek.co/2026/11/14/20k-nissan-nx7-phev-goes-on-sale-with-nearly-200-miles-of-electric-range/) ⭐️ 7.0/10

东风日产于 11 月 13 日开启 NX7 插电混动车型的早期订单，宣称搭载 40 kWh 磷酸铁锂（LFP）电池，纯电续航最高 320 公里（约 198 英里），售价约 2 万美元。这些数字均来自厂方宣传，Electrek 的简短报道没有说明续航所采用的测试工况（例如中国常用的 CLTC）、对应哪个配置版本，也未给出正式上市与交付时间。因此这是一次价格与产品定位的发布信号，而不是已交付或经独立验证的续航成绩。

Electrek · 11月14日 21:26

**「已证实与未证实」** 已证实：据 Electrek 报道，东风日产已于 11 月 13 日开启 NX7 插混版的早期预订，并对外宣传 40 kWh LFP 电池、最高 320 km 纯电续航和约 2 万美元的价格。尚未证实：320 km 续航与 2 万美元售价均未经过独立测试或第三方核实，报道也未交代续航测试标准、具体配置差异、最终成交价以及首批交付时间。

**「背景」** 插电式混合动力车（PHEV）同时搭载可外接充电的电池电机与燃油发动机：电量充足时以纯电行驶，电量耗尽后转为用油驱动。市面上多数 PHEV 的电池容量在 10–20 kWh 区间，纯电续航通常只有几十公里；NX7 采用的是 40 kWh 磷酸铁锂（LFP）电池，容量已接近小型纯电动车，这是厂方得以宣称近 200 英里（320 公里）纯电续航的原因。东风日产是日产在中国设立的合资公司，这款车目前处于早期预订阶段，而不是批量交付。

**「为什么重要」** 如果价格与续航在实际配置上成立，NX7 会把“日常通勤基本靠电、长途用油”的插混门槛压到约 2 万美元区间，直接对标中国市场上主打低价长续航的自主品牌插混车型。对潜在买家而言，关键动作是核对官方公布的续航测试工况与对应配置价格，因为低价版本未必配 40 kWh 电池。

**「后续看点」** 关注东风日产随后公布的完整配置与价格表及 CLTC 续航数据，以及首批车主交付时间的官方确认。

**标签**: `#Nissan NX7`, `#PHEV`, `#LFP battery`, `#EV range`, `#China auto market`

---

<a id="item-ev-energy-2"></a>
### [特斯拉 Model Y 后驱版 EPA 续航升至 348 英里，价格不变](https://www.notateslaapp.com/news/5017/tesla-model-y-rwd-gets-increased-range-at-same-price) ⭐️ 7.0/10

特斯拉已将其美国市场 Model Y 后驱版的 EPA 预估续航提高 8.5%，达到 348 英里，起售价仍为 39,990 美元。此次调整针对美国消费者，属于现有车型的续航与能效更新，而非新车型或新平台。上述信息由专注特斯拉的媒体 Not a Tesla App 转报，现有材料中尚未包含特斯拉官方配置器或 EPA 文件的独立确认。

Not a Tesla App · 11月14日 22:06

**「已证实与未证实」** 已证实：Not a Tesla App 报道称，特斯拉将 Model Y 后轮驱动版的 EPA 预估续航提高 8.5% 至 348 英里，同时美国起售价维持 39,990 美元不变。

尚未证实：上述数字目前仅来自这一家专注特斯拉的媒体报道，尚未见到特斯拉官网配置器页面或 EPA 官方备案数据作为独立佐证；报道也未说明续航提升的具体技术原因（如电池、电控或轮胎/空气动力学调整）、适用于哪些生产批次，以及新规格何时开始交付。

**「背景」** EPA 续航是美国环保署给出的估算值，用来在同一口径下比较不同车型的能耗表现；车厂在改动电池、电机或空气动力学设定后，可以重新申报这一数字。Model Y RWD 是 Model Y 系列中的后驱配置版本，此次调整针对的就是这一入门配置，而非新增车型或平台换代。

**「为什么重要」** 对计划购买该车型的美国消费者，同样的 39,990 美元起售价对应更高的 EPA 预估续航；但 EPA 数字是标准化估算，高速、低温和载重条件下的实际续航仍需独立测试验证。

**「后续看点」** 后续可查看特斯拉美国官网配置器是否将 Model Y 后驱版标注为 348 英里，以及 EPA 官方数据或第三方实测是否确认这一提升。

**标签**: `#Tesla`, `#Model Y`, `#EV range`, `#pricing`, `#EPA range`

---

## 航天

<a id="item-space-1"></a>
### [SpaceX 首次用发射塔接住从轨道返回的星舰](https://www.teslarati.com/spacex-catches-starship-first/) ⭐️ 10.0/10

SpaceX 在第 15 次星舰试飞中首次用发射塔机械臂接住从轨道返回的上面级飞船 Ship 42；飞船在轨约 22.5 小时、绕地球 14 圈后返回，并部署了全部 26 颗 Starlink V3 卫星。这次回收使星舰上面级首次回到发射场，而不是像此前每次那样溅落海中或丢失；三颗带相机的卫星拍摄的热防护图像被 SpaceX 用于判断再入状态。但同一任务中，超重助推器 Booster 22 在返场途中因制导、导航与控制问题中止捕获，最终在墨西哥湾上空触发飞行终止系统落水；马斯克称发动机推力略低造成推进剂不足，计划用 Raptor V3.2 和提前约 1 秒关机修正。SpaceX 未给出 Ship 42 复用时间，马斯克仅表示助推器损失不影响其实现高频完全复用星舰的时间表。

Teslarati · 11月14日 21:40

**「已证实与未证实」** 已证实：SpaceX 在 X 上发布“Pad and tower systems are go for catch”，随后 Teslarati、Ars Technica 和 The Verge 均报道 Ship 42 被发射塔机械臂捕获；报道一致称其在轨约 22.5 小时并部署 26 颗 Starlink V3 卫星。
尚未证实：热防护的实际损伤程度、复用前的检修成本和周转时间没有独立数据；Booster 22 因“发动机推力略低”导致推进剂不足只是马斯克的单方面解释，SpaceX 也未公布 Ship 42 的复飞日期。

**「背景」** 星舰是两级火箭：巨大的超重型助推器负责第一段上升，上面级飞船则继续入轨。SpaceX 的猎鹰 9 号虽能常规回收一级助推器，却每次都丢弃上面级；星舰的目标是两级都回收。此次之前，SpaceX 已三次用发射塔机械臂接住超重型助推器（最近一次在 2025 年 3 月），但所有飞船上面级都以落海或丢失告终；9 月那次试飞虽进入轨道，却因部分发动机熄火在约三小时后溅落太平洋。

**「为什么重要」** 如果飞船经检查后能快速复飞，星舰才可能以可承受的成本批量部署 Starlink V3，并支撑 NASA Artemis 着陆方案所需的在轨推进剂加注；本次只证明“接得住”，热防护检查与翻修周转能否压缩，才决定复用是否真的降低成本。

**「后续看点」** 接下来要看 Ship 42 返回后的热防护检查结果，以及 SpaceX 是否再次尝试同时捕获助推器和飞船。马斯克称星舰将在 2027 年上半年达到每周发射节奏，这一目标能否兑现，将直接检验本次捕获带来的复用价值。

**「社区讨论」** Hacker News 评论者 Zigurd 认为，这是自航天飞机以来首次展示可复用轨道上面级，但他提醒航天飞机虽技术可行却因翻修昂贵、发射频率低而难以为继；small\_model 则把热防护能否承受再入视为关键，认为下一步要完成双捕获和同一艘飞船复飞，入轨成本才会明显下降。ChuckMcM 指出助推器只差少量推进剂就可能同时被接住，并称星舰最终入轨质量比仍待观察。

**标签**: `#SpaceX`, `#Starship`, `#reusable launch`, `#orbital catch`, `#Starbase`

---

## 科技产业与政策

<a id="item-tech-industry-1"></a>
### [FBI 查封朝鲜&quot;FaceStealer&quot;攻击所用的云基础设施](https://www.tomshardware.com/tech-industry/cyber-security/fbi-disrupts-north-korean-facestealer-campaign-behind-usd5-billion-binance-hack-doj-seizes-facestealer-cloud-infrastructure-containing-900-videos-of-tech-workers-hackers-used-ai-deepfakes-to-steal-usd400-million-and-compromise-open-source-software) ⭐️ 8.0/10

美国联邦调查局（FBI）与司法部（DOJ）首次为朝鲜政府支持的一类社交工程攻击公开命名&quot;FaceStealer&quot;，并宣布已查封其使用的云基础设施，其中存有 900 段针对特定目标人物的视频。FBI 的详细报告称，该行动已持续至少 18 个月，并认定其盗取的加密货币约 4 亿美元；而 Tom&\#x27;s Hardware 称，与该行动相关、金额最大的一起是近期 Binance 被盗案，涉款逾 50 亿美元（其中大部分已被冻结或追回），报道未解释这一数字与 4 亿美元之间如何对应。FBI 还指出，攻击者多次试图渗透开源软件供应链，重点针对 JavaScript/NPM 模块和 Rust crate；报道推测其中包括 2026 年 3 月的 Axios 投毒事件，该库每周下载量约 1 亿次，被植入远程控制工具数小时。其手法是先通过 AI 深度伪造、真实聊天记录与人脉关系层层铺垫，再以搭建在攻击者服务器上、域名仿冒的假 Zoom/Teams 会议，以&quot;技术故障&quot;为由诱导受害者安装所谓&quot;更新&quot;，从而植入恶意软件并窃取浏览器会话与 CI/CD 凭证。

Tom&\#x27;s Hardware · 11月15日 16:30

**「已证实与未证实」** 已证实：美国司法部发布公告宣布采取行动打击朝鲜以加密货币窃取为目的的计划，联邦调查局（FBI）同步发布 IC3 报告，将该行动命名为“FaceStealer”，并称已查获存放有 900 段目标受害者视频的云端基础设施；FBI 表示该计划造成约 4 亿美元加密货币损失——以上均出自司法部与 FBI 的公开文件，经 Tom&\#x27;s Hardware 转述。

尚未证实：报道标题与正文所称“超 50 亿美元”的币安被盗规模，以及该案与 FaceStealer 的直接归属关系，目前依赖媒体叙述与币安博文，报道本身也说明其中大部分资金已被冻结或追回，实际净损失未经独立核实；文章把 2026 年 3 月的 Axios npm 包投毒事件“几乎可以肯定”归为同一组织所为，但这是记者推断，FBI 报告并未点名该事件，受害规模与视频数量也没有第三方验证。

**「背景」** 这类攻击的关键前置条件是先取得受害者的通讯录和聊天记录：攻击者侵入其通讯软件后，用真实对话与联系人信息伪装成招聘方或投资人，再借深度伪造视频把目标引向假会议。Tom&\#x27;s Hardware 将 2026 年 3 月的 Axios npm 包被植入远程访问工具事件视为同一手法的案例；npm 是 JavaScript 生态最常用的包管理器，Axios 每周下载量约 1 亿次。

**「为什么重要」** 对开源项目维护者和 CI/CD 权限持有者来说，这份报告说明攻击入口已从&quot;骗过普通用户&quot;转向&quot;骗过能发布软件包的人&quot;：被冒充 CEO 的假 Slack 工作区、假 Teams 会议和仿冒域名（如&quot;uu01webzoom.us&quot;、&quot;teams.livemeet.us&quot;）足以让维护者亲手在自己的包里放入后门，而下游数百万次下载会把风险放大。实际操作上，收到招聘或投资邀约的开发者应核对会议域名是否与官方域名一致，任何要求安装&quot;会议插件&quot;或&quot;更新&quot;的提示都应拒绝；若已安装，应立即轮换浏览器会话、包管理账号与 CI/CD 密钥。

**「后续看点」** 可关注两条可核查的线索：司法部是否对被查封基础设施公布进一步的起诉或资产没收文件，以及 FBI IC3 是否会更新该报告的通报内容，把 Axios npm 投毒事件等具体供应链攻击正式归因到 FaceStealer。

**标签**: `#North Korea cybercrime`, `#cryptocurrency theft`, `#FBI/DOJ`, `#deepfake social engineering`, `#supply chain security`

---

<a id="item-tech-industry-2"></a>
### [EFF 请求上诉法院为车牌识别数据库查询设立搜查令要求](https://www.eff.org/deeplinks/2026/11/were-asking-appeals-court-require-warrant-alpr-searches) ⭐️ 7.0/10

EFF 表示已向上诉法院提交意见书（brief），请求法院裁定警方查询联网车牌识别（ALPR，automatic license plate recognition，自动记录过往车辆车牌与位置的摄像头网络）数据库属于美国宪法第四修正案意义上的“搜查”，因而需要搜查令。EFF 称该意见书详述了全美范围内相互连接、持续追踪驾驶者的 ALPR 网络如何运作。这属于倡导性法律行动而非法院裁决：现有材料中没有受理法院名称、案件名、案号或庭审排期，也没有任何法官对该主张作出裁定。

Hacker News · nobody9999 · 11月15日 02:00 · [社区讨论](https://news.ycombinator.com/item?id=50503255)

**「已证实与未证实」** 已证实：EFF 在其官网文章中称已提交该意见书，并引述意见书内容，主张联网 ALPR 的持续追踪构成第四修正案下的“搜查”，应受搜查令约束。
尚未证实：受理法院、案件名称与案号、庭审或裁决时间表均未在现有材料中出现；这项法律主张能否被法院接受、以及所需门槛（如“可能事由”）的具体标准，目前仅有 EFF 一方的论述。

**「背景」** 自动车牌识别系统（ALPR）由警方或商业运营商沿道路架设摄像头，自动记录经过车辆的车牌、时间与位置，汇集成可供跨机构检索的历史行驶轨迹数据库。美国宪法第四修正案禁止“无理搜查”，争点在于：警方检索这类由第三方或商业供应商持有的历史位置数据，是否构成需要搜查令的“搜查”。这一争点此前已进入诉讼：圣何塞警方被指进行数十万次无搜查令的 ALPR 检索而遭起诉（tool-2-1）；EFF 也曾请求加州上诉法院推翻下级法院判决，认定警方使用 ALPR 数据属于需要搜查令的搜查（tool-2-3）。

**「为什么重要」** 若上诉法院采纳 EFF 的主张，执法机构在调取历史车牌位置记录前将需先取得搜查令，这直接改变警局与商业 ALPR 网络运营商之间的查询流程、数据保留期限与合同条款；若法院驳回，现行无需搜查令即可回溯查询车辆轨迹的做法将维持不变。使用这类系统的城市与警察局应关注判决后其内部政策与采购合同是否需要改写。

**「社区讨论」** 评论者普遍支持 EFF 的立场，但多位读者认为方案应更进一步：hedora 和 largbae 主张只应保留与有效搜查令相关的车牌数据，hedora 同时提出应兼顾受害者权益，使这些数据能真正用于侦查。petcat 举出新罕布什尔州法律作为现成模板——只采集车牌、三分钟内删除未命中的图像、禁止将未命中图像上传离开设备——但补充说仍应要求搜查令才能访问数据。topshelf 则质疑“身处公共空间即放弃第四修正案保护”的前提。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://briefly.co/tag/fourth-amendment"># fourth - amendment tag - Briefly</a></li>
<li><a href="https://www.pressreleasepoint.com/hearing-thursday-eff-urges-appeals-court-curb-police-access-alpr-databases">Hearing Thursday: EFF Urges Appeals Court to... | PressReleasePoint</a></li>

</ul>
</details>

**标签**: `#ALPR`, `#surveillance`, `#privacy`, `#Fourth Amendment`, `#EFF`

---