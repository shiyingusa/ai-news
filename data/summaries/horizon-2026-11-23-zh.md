# AI 每日雷达 - 2026-11-23

> 过去一天共筛查 232 条科技资讯，留下最值得读的 22 条。

---

**人工智能**
1. [智谱发布 GLM-5.4：首个 Loop Transformer，28 层各跑两遍](#item-ai-news-1) ⭐️ 8.0/10
2. [亚马逊据报以 75 亿美元收购 Decart 优化技术及研究团队](#item-ai-news-2) ⭐️ 8.0/10
3. [GPT-6.2 Astra 给出 Smoktunowicz 间隙定理的可机器验证 Lean 证明](#item-ai-news-3) ⭐️ 8.0/10
4. [两州起诉马斯克旗下公司，指 Grok 防护不足](#item-ai-news-4) ⭐️ 8.0/10
5. [1700 万行 Lean 证明引发可信度争论](#item-ai-news-5) ⭐️ 7.0/10
6. [Sierra 完成 17.5 亿美元 F 轮融资，估值据报六个月内翻倍至 300 亿美元](#item-ai-news-6) ⭐️ 7.0/10
7. [沃尔玛开放 Agent Gateway，Meta Muse 可代用户抢购黑五商品](#item-ai-news-7) ⭐️ 7.0/10
8. [马斯克称 SpaceX 在 AI 上落后，出租算力比自用更赚钱，《纽约时报》报道](#item-ai-news-8) ⭐️ 7.0/10
9. [METR 更新 AI 时间跨度图：判断类任务进展落后于编程](#item-ai-news-9) ⭐️ 7.0/10
10. [OpenAI 首席科学家提议设 AI 开发行业统一门槛](#item-ai-news-10) ⭐️ 7.0/10

**芯片与算力**
1. [Penguin 展出光子外置内存：最高 576GB HBM3E，2027 下半年送样](#item-chips-compute-1) ⭐️ 7.0/10
2. [AI 服务器签约后涨价最高 45%，内存短缺推高节点成本](#item-chips-compute-2) ⭐️ 7.0/10

**电动车与新能源**
1. [大众计划到 2030 年每年从中国出口约 30 万辆汽车](#item-ev-energy-1) ⭐️ 7.0/10
2. [荷兰法院临时裁定：比亚迪 Ti7 因外观近似捷豹路虎卫士被禁在欧盟销售](#item-ev-energy-2) ⭐️ 7.0/10
3. [欧盟理事会倾向把企业车队电动车配额降为自愿目标](#item-ev-energy-3) ⭐️ 7.0/10
4. [宝马 iX4 在德布勒森工厂投产，与 iX3 共线](#item-ev-energy-4) ⭐️ 7.0/10
5. [美参议院通过许可改革法案，允许太阳能开发商起诉联邦机构](#item-ev-energy-5) ⭐️ 7.0/10
6. [纽约州公布先进核能总体规划，目标新增 5 吉瓦](#item-ev-energy-6) ⭐️ 7.0/10

**航天**
1. [星舰飞船完成轨道级回收验证](#item-space-1) ⭐️ 9.0/10
2. [中国公布载人登月详细路线图：三次无人任务先行](#item-space-2) ⭐️ 8.0/10

**科技产业与政策**
1. [美司法部寻求没收朝鲜关联黑客从币安窃取的逾 10 亿美元加密资产](#item-tech-industry-1) ⭐️ 8.0/10
2. [IBM 停止部分美国签证与绿卡担保，转而提供海外调动](#item-tech-industry-2) ⭐️ 7.0/10

---

## 人工智能

<a id="item-ai-news-1"></a>
### [智谱发布 GLM-5.4：首个 Loop Transformer，28 层各跑两遍](https://z.ai/blog/glm-5.4) ⭐️ 8.0/10

智谱（Z.ai）发布旗舰模型 GLM-5.4，采用“循环”（loop）架构：28 个层在推理时各执行两遍，模型总参数 7500 亿。公司称这一设计可对标 2 万亿至 3 万亿参数级别的模型，但据 The Decoder 报道，目前公开的基准分数只来自一个 300 亿参数的测试用小模型，7500 亿参数的正式模型尚无自家跑分。智谱把 GLM-5.4 定位为“广义编程”（Generalized Coding）的起点，即代码不仅生成程序，还能产出视频、游戏和 CAD 模型。可用性上，该模型目前不在 OpenRouter 或 Z.ai 常规 API 套餐中提供，开发者需改用其 Coding Plan，所获 API key 与常规 key 用法一致，但可访问新模型。

Hacker News · foohis · 11月23日 10:06 · [社区讨论](https://news.ycombinator.com/item?id=50609685)

**「已证实与未证实」** 已证实：智谱在自家发布说明中称 GLM-5.4 为 7500 亿参数、28 层循环执行两次的架构；The Decoder 报道了该架构细节及“对标 2–3 万亿参数模型”的公司说法；开发者 Simon Willison 实测确认该模型只能通过 Coding Plan 获取，且该套餐的 API key 与常规 key 用法相同。
尚未证实：7500 亿参数模型本体没有任何公开基准分数，仅有 300B 测试模型的数据；“以一半层数达到 2–3 万亿参数模型水平”目前只是公司自述，缺少独立评测；价格、完整开放日期以及是否会进入常规 API 或 OpenRouter 均未说明。

**「背景」** 在主流 Transformer 推理中，每生成一个 token 都要把每一层的权重从显存（HBM）搬到芯片上算一次，权重搬运的内存带宽因此长期是推理速度的头号瓶颈。所谓 Loop Transformer，是让同一批权重在一次前向中被重复计算多遍——用一个“循环”代替堆叠更多独立层，从而在不增加权重读取量的前提下增加有效计算深度。作为参照，阿里在 11 月 16 日的发布中把旗舰 Qwen4-Max 做到 2.4 万亿总参数、每 token 激活 710 亿，而 Z.ai 称 GLM-5.4 仅以 7500 亿参数、28 层跑两遍即可对标 2 万亿至 3 万亿参数级别的模型。

**「为什么重要」** 循环架构针对的是推理中最硬的瓶颈：生成每个 token 都要把整层权重从 HBM 内存搬到芯片上算一次，内存带宽因此长期是推理速度的第一限制；让同一批权重留在片上算两遍，可以减少搬运开销。对开发者的直接后果在接入方式而非算法：想调用 GLM-5.4 必须订阅 Coding Plan，走原有常规 API 套餐或 OpenRouter 的调用会拿不到该模型，迁移前需先确认计费与配额。

**「后续看点」** 值得关注智谱何时公布 7500 亿参数正式模型自身的基准成绩，以及第三方对循环架构在同等显存带宽下实际吞吐的独立测试结果。

**「社区讨论」** Hacker News 讨论中，有评论者认为智谱给出的技术细节相当透明，并称循环 Transformer 是显而易见的方向、只是仍有工程问题待解；另一位评论者从 HBM 带宽角度解释了循环层为何能省下权重搬运开销。开发者 Simon Willison 则记录了实测经历：为拿到 GLM-5.4 不得不切换到 Coding Plan，并对比称 GLM-5.2 生成同一“鹈鹕”测试题时默认使用渐变与动画，风格明显不同。也有用户抱怨部分中国模型“马拉松式思考”，在最简单的任务上反复自我怀疑、完成时间远高于前沿模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://qwen.ai/blog?id=qwen4-max">2026-11-16 — Alibaba launches Qwen4-Max flagship with 2.4T parameters</a></li>

</ul>
</details>

**标签**: `#model release`, `#loop transformers`, `#Zhipu GLM`, `#LLM architecture`, `#inference efficiency`

---

<a id="item-ai-news-2"></a>
### [亚马逊据报以 75 亿美元收购 Decart 优化技术及研究团队](https://techcrunch.com/2026/11/23/amazon-snaps-up-decarts-ai-optimization-tech-for-7-5b-as-it-prepares-to-sell-trainium-chips/) ⭐️ 8.0/10

彭博社 11 月 23 日援引一名知情人士报道，亚马逊已同意以约 75 亿美元收购 Decart 的大部分业务，包括 Decart Optimization Stack、创始团队和 AI 研究人员。TechCrunch 将这笔交易与亚马逊筹备销售自研 AI 训练芯片 Trainium 联系起来，称其意在增强 AWS 的 AI 基础设施能力。交易尚未得到亚马逊或 Decart 公开确认，官方也未披露具体金额、资产范围和交割时间。

TechCrunch AI · 11月23日 17:14

**「已证实与未证实」** 已证实：彭博社记者 Matt Day 报道，亚马逊已同意收购 Decart 的大部分资产，包括 Decart Optimization Stack 优化软件栈及其创始团队和 AI 研究人员（tool-2-1、tool-2-2）；据 explainX 引述的亚马逊官方新闻稿，亚马逊确认签署了收购该优化软件栈并聘用其联合创始人和 AI 团队的协议（tool-2-3）。

尚未证实：约 75 亿美元的对价仅来自彭博社援引的匿名消息源，亚马逊的公告并未给出金额；交易是否已完成交割、以现金还是股票支付，均无官方说明；彭博社称亚马逊不收购 Decart 的 Lucy、Oasis 等 AI 模型，这一点同样不见于亚马逊公告；报道也没有说明这笔收购与亚马逊对外销售 Trainium 芯片之间的具体联系。

**「背景」** Decart 成立于 2023 年，创始人为 Dean Leitersdorf 和 Moshe Shalev，起步时是一家 AI 研究实验室，此后产品线覆盖 Lucy、Oasis 等“世界模型”，以及此次交易的核心资产 Decart Optimization Stack（DOS）——一套让模型在特定硬件上运行得更省、更快的软件优化栈。据融资追踪数据库 Venture Capital Tracker 记录，该公司在 2026 年 5 月完成 3 亿美元 C 轮融资，投资方包括领投的 Radical Ventures、英伟达、Adobe Ventures、丰田创投，以及老股东 Sequoia 和 Benchmark。对亚马逊而言，这类优化软件与自研 Trainium 芯片的销售直接相关：客户采购芯片时，同样需要能充分发挥芯片性能的软件栈。

**「为什么重要」** 如果这笔交易完成，Amazon 将获得一套能同时优化 Nvidia GPU、Google TPU 和自家 Trainium 的推理与训练软件层；目前依赖 Decart Optimization Stack 在多家芯片间调度负载的客户，需要确认 Amazon 是否会允许该软件继续中立支持非 AWS 硬件。Amazon 的收益也很直接：它可以把这套优化能力纳入 Trainium 的软件栈，借此向外部客户卖芯片，而不只是卖算力。

**「后续看点」** 后续应关注亚马逊与 Decart 是否正式确认交易，以及交易是否进入监管审查；目前双方未公布时间表。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://startupintros.com/orgs/decart">Decart: Funding, Team &amp; Investors | Startup Intros</a></li>
<li><a href="https://venturecapitaltracker.com/startup/decart">Decart Funding, Valuation &amp; Investors</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-11-23/amazon-is-said-to-pay-7-5-billion-for-ai-startup-decart-s-tech">Amazon to Acquire Decart AI Tech for $7.5 Billion to Boost ...</a></li>
<li><a href="https://finance.yahoo.com/technology/ai/articles/amazon-agrees-buy-decart-ai-150027613.html?fr=sycsrp_catchall">Amazon agrees to buy Decart AI technology and team in ...</a></li>
<li><a href="https://explainx.ai/blog/amazon-decart-acquisition-7-5-billion-claimed-vs-verified-november-2026">Amazon Buying Decart? $7.5B Deal Status (Nov 2026 ...</a></li>
<li><a href="https://eu.36kr.com/en/p/3934444301335681">From AI Video Generation to Building a Full AI World: Why Decart AI ...</a></li>
<li><a href="https://www.nuaxia.com/post/decart-raises-300m-to-scale-real-time-ai-infrastructure-and-world-models">Decart Raises $300m to Scale Real-Time AI Infrastructure and World...</a></li>
<li><a href="https://thenextweb.com/news/decart-300-million-radical-ventures-world-models">Decart raises $300M to put a real-time world model in front of...</a></li>

</ul>
</details>

**标签**: `#Amazon`, `#Decart`, `#AI chips`, `#acquisition`, `#Trainium`

---

<a id="item-ai-news-3"></a>
### [GPT-6.2 Astra 给出 Smoktunowicz 间隙定理的可机器验证 Lean 证明](https://the-decoder.com/gpt-6-2-astra-solved-a-math-theorem-no-other-ai-could-crack-then-invented-its-own-proof-strategy/) ⭐️ 8.0/10

The Decoder 报道，OpenAI 的 GPT-6.2 Astra 独立给出了 Smoktunowicz 间隙定理（gap theorem）的 Lean 形式化证明，且该证明可由机器逐步核验；Lean 是交互式定理证明器，证明写成代码后能由机器检查，不依赖审稿人的信任，据 Vals AI 称这是同类任务中的首次。报道称，由于 Lean 的数学库 Mathlib 缺少关键基础，模型没有沿用现成路径，而是自行选择了证明策略。在形式化数学基准 Autoform-Hard 上，Astra 以 56 题解出 49 题位居榜首。这些说法目前来自 The Decoder 的二手报道与 Vals AI 的表述，材料中没有 OpenAI 的原始公告、证明文件或独立数学家的复核结果。

The Decoder · 11月23日 12:17

**「已证实与未证实」** 已证实：Vals AI 发布了评测说明与带注释的证明，称 GPT-6.2 Astra 用 94 分钟、约 1800 行 Lean 4 代码给出了代数家 Agata Smoktunowicz 间隙定理（graded domains 情形）的可机器验证形式化证明，且所走路线与已发表的证明不同；另外两家媒体转述了相同的时间和代码行数。The Decoder 报道称 Astra 以 56 项中解出 49 项领跑 Autoform-Hard 榜单。

尚未证实：“首个此类证明”目前只是 Vals AI 的说法（另一家媒体写作“被认为是首个”），没有独立第三方复核该证明或 Autoform-Hard 成绩；该定理此前已有正式发表的数学证明，Astra 完成的是形式化，而非提出新定理，标题中“解出无其他 AI 能解的定理”应在此意义下理解；它自创的“capacity”量及绕开 Mathlib 缺失引理的具体做法，细节也未获独立评估。提供的材料中未见 OpenAI 的官方声明。

**「背景」** GPT-6.2 Astra 是 OpenAI 于 11 月 18 日发布的模型；AI Daily Radar 11 月 19 日的日报曾报道，其 API 定价为每百万输入 token 8 美元、输出 40 美元，上下文窗口为 105 万 token。此次排行榜所在的 Autoform-Hard 由评测机构 Vals AI 推出，含 56 道取自研究生与科研级教材的 Lean 4 形式化任务，题目源自 Meta FAIR 的 AutoformBench。

**「为什么重要」** 对形式化数学和模型评测的使用者来说，这条消息的分量取决于那份 Lean 证明本身能否被第三方编译核验，以及 Mathlib 是否真的缺少所需基础；在看到证明文件并独立跑通之前，「首个」和「自创证明策略」应视为 Vals AI 一侧的说法。关注 Autoform-Hard 的人也应看逐题结果而非仅看 49/56 的总数，因为这个分数只说明该模型在这一套 56 道题上的表现。

**「后续看点」** 接下来可查的是该 Lean 证明是否公开发布并能被他人在本地编译通过，以及 Astra 能否解出 Autoform-Hard 剩余未完成的 7 道题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.vals.ai/blogs/smoktunowicz-gap-theorem">GPT-6.2 Astra Formalizes Smoktunowicz&#x27;s Gap Theorem - vals.ai</a></li>
<li><a href="https://alphasignal.ai/news/openai-s-gpt-6-2-astra-proves-a-math-theorem-no-computer-ever-could">OpenAI&#x27;s GPT-6.2 Astra Proves a Math Theorem No Computer Ever ...</a></li>
<li><a href="https://hermes-ai.net/news/openai-s-gpt-6-2-astra-proves-a-math-theorem-no-computer-ever-could/">OpenAI&#x27;s GPT-6.2 Astra Proves a Math Theorem No Computer Ever ...</a></li>
<li><a href="http://www.geekpark.net/news/374175">2026-11-19 — OpenAI ships GPT-6.2 Astra and Sol with a 20% price cut, and developers push back</a></li>
<li><a href="https://www.vals.ai/">AI Benchmarks for Real-World Tasks | Vals AI</a></li>

</ul>
</details>

**标签**: `#AI math`, `#theorem proving`, `#Lean`, `#model evaluation`, `#OpenAI`

---

<a id="item-ai-news-4"></a>
### [两州起诉马斯克旗下公司，指 Grok 防护不足](https://www.wired.com/story/states-sue-spacex-over-grok-deepfakes/) ⭐️ 8.0/10

俄勒冈州和弗吉尼亚州的总检察长已对埃隆·马斯克旗下多家公司提起诉讼，指控这些公司为 Grok（xAI 的聊天机器人）设置的安全防护不足，使真实人物——包括儿童——的性化图像得以生成。《连线》（Wired）的标题点名 SpaceX，但正文只称被告为“马斯克旗下多家公司”，未列出完整名单。报道没有披露受理法院、具体法律主张和索赔内容，也没有马斯克旗下公司的回应。

Wired · 11月23日 11:00

**「已证实与未证实」** 已证实：据《连线》报道，俄勒冈州和弗吉尼亚州总检察长已起诉马斯克旗下多家公司，指控 Grok 的安全防护不足以阻止真实人物（含儿童）的性化图像生成。
尚未证实：具体被告名单（标题称 SpaceX，正文称“多家公司”）、受理法院与提交日期、援引的法条及索赔金额均未披露；关于 Grok 防护不足这一核心指控，目前只有原告方主张，尚无独立调查或法院认定。

**「背景」** Grok 是马斯克旗下 xAI 的聊天机器人，能按文字提示生成图像；据 CNBC 报道，弗吉尼亚州和俄勒冈州是首批就 Grok 图像生成器起诉马斯克旗下公司（包括 SpaceX）的州。诉状中所说的“nudification”（俗称“脱衣”）指用生成模型把真人照片改写成裸露或性化画面；雅虎新闻报道称，两州总检察长 Jay Jones 和 Dan Rayfield 指控相关公司为在竞争中形成差异而削弱了业界通行的防护措施。据 The Next Web 报道，这是州政府首次针对 Grok 图像生成器提起此类诉讼。

**「为什么重要」** 对在美国提供图像生成功能的产品团队来说，这起案件把合规风险落到了州一级：如何拦截针对真实人物（尤其是未成年人）的性化生成请求、是否设置年龄限制，可能直接成为州总检察长起诉的理由，而不只是联邦机构问询的问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/11/23/oregon-virginia-spacex-grok-deepfake-lawsuits.html">SpaceX sued by Oregon and Virginia over AI deepfake porn ...</a></li>
<li><a href="https://www.yahoo.com/news/politics/articles/virginia-oregon-sue-musk-ai-120000454.html?fr=sycsrp_catchall">Virginia, Oregon sue Musk’s AI company over sexual deepfakes</a></li>
<li><a href="https://thenextweb.com/news/virginia-oregon-spacex-grok-lawsuit">Virginia and Oregon sue Musk’s SpaceX over Grok’s sexual ...</a></li>

</ul>
</details>

**标签**: `#Grok`, `#AI deepfakes`, `#AI regulation`, `#child safety`, `#lawsuits`

---

<a id="item-ai-news-5"></a>
### [1700 万行 Lean 证明引发可信度争论](https://micjm.com/blog/yes-17m-lines-of-lean-is-a-lot/) ⭐️ 7.0/10

一篇博客文章分析了一个约 1700 万行的 Lean 证明工件，Hacker News 的讨论随即集中在 LLM 辅助生成的形式化证明是否可信。评论者的核心担忧是规模：证明越大，潜在错误点越多，而一个反例就足以推翻结论；也有人担心 LLM 写出的说明和代码难以让未参与生成的人理解。讨论中有人称该证明的行数已从 1700 万降到 1300 万，并可能继续下降，但给出的材料没有独立确认这一数字或证明本身是否正确。

Hacker News · seizethecheese · 11月23日 05:00 · [社区讨论](https://news.ycombinator.com/item?id=50607668)

**「已证实与未证实」** 已证实：该条目指向的博客文章讨论了一个约 1700 万行的 Lean 证明工件，相关 Hacker News 讨论集中在 LLM 辅助证明的正确性风险。尚未证实：该证明是否由 LLM 生成、是否包含逻辑错误，以及评论中“已降到 1300 万行”的说法，均未在给出的材料中得到独立确认；博客文章的具体论证也未提供。

**「背景」** 黎曼猜想是数学界最著名的未解难题之一。据滑铁卢大学数学家 Michael Rubinstein 的整理页面，Anthropic 的数学家 Levent Alpöge 于 2026 年 11 月 20 日发布一份四页短文，称自己与 Claude 合作，认为已找到黎曼猜想以及 Dirichlet L 函数广义黎曼猜想的证明，但没有配套论文；该证明以 Lean 形式发布，共 175,187 个文件、约 1700 万行。Lean 是一种证明助手（proof assistant），它把每一步推理写成代码，由内核机械校验，因此理论上形式化证明可被机器逐条检查；但当规模达到上千万行时，人工逐行审阅实际上已不可行，Rubinstein 的页面便汇总了他本人及其他人对这份 Lean 证明所做的检查。

**「为什么重要」** 对 Lean 用户和审阅者来说，最直接的问题是审查成本：上千万行的工件无法靠逐行阅读来建立信任，社区因此把焦点放在缩小证明规模、确认形式化陈述是否忠实于原问题，以及寻找独立复核手段上。

**「后续看点」** 评论者称该证明已降到 1300 万行，并预测可能降至 1100 万行；关注这一行数变化是否发生，以及博客作者是否更新分析。

**「社区讨论」** 多位评论者把规模视为风险来源：jandrese 认为证明越大，出错点越多，一个反例就能让整个结果崩塌；lukaslalinsky 则说没人会审阅上千万行 LLM 生成的代码，担心其中藏有次要信息。Arch485 提出另一种可能：问题未必是 Lean 的 bug，而是某个被转换的子证明本身有误；adgjlsfhk1 称行数已降至 1300 万。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=aDl7-MWFLVc">17 Million Lines Claim to Prove Riemann . We Ran Them. - YouTube</a></li>
<li><a href="https://math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/">Alpöge/Claude proof of the Generalized Riemann Hypothesis</a></li>
<li><a href="https://micjm.com/blog/yes-17m-lines-of-lean-is-a-lot/">Yes, 17 m lines of Lean is a lot | micjm</a></li>

</ul>
</details>

**标签**: `#Lean`, `#formal verification`, `#LLM-generated proofs`, `#mathematics`, `#AI code quality`

---

<a id="item-ai-news-6"></a>
### [Sierra 完成 17.5 亿美元 F 轮融资，估值据报六个月内翻倍至 300 亿美元](https://techcrunch.com/2026/11/23/sierra-doubles-valuation-to-30b-within-six-months-as-demand-for-ai-in-cx-takes-off/) ⭐️ 7.0/10

由前 Salesforce 联席 CEO Bret Taylor 联合创办的企业客服 AI 公司 Sierra 周一宣布，已完成 17.5 亿美元 F 轮融资。据 TechCrunch 报道，本轮融资使其估值在六个月内翻倍至 300 亿美元；而 Sierra 的公告本身只确认了融资规模，未提及估值数字。报道把这轮融资归因于企业在客户体验（CX）场景中的 AI 需求上升，但没有披露客户数量、收入规模或投资方名单。

TechCrunch AI · 11月23日 14:43

**「已证实与未证实」** 已证实：Sierra 于 11 月 23 日宣布完成 17.5 亿美元 F 轮融资，估值 300 亿美元；本轮由 Greenoaks 和 Lightspeed Venture Partners 领投，Benchmark、Sequoia、GV、Tiger Global 等原有领投方全部继续参与（Sierra 官方博客与 CMSWire 报道一致）。
尚未证实：“六个月内估值翻倍”一说来自 TechCrunch 的报道标题，Sierra 官方博客只给出本轮 300 亿美元估值，未列出上一轮的具体数字；融资的具体条款、营收与客户规模、资金用途，以及独立第三方对估值的核实，均未披露。

**「背景」** Sierra 由 Salesforce 前联席 CEO Bret Taylor 创办，向企业提供用于客户体验（CX，即客服、售后等与客户直接打交道的环节）的 AI 智能体，而非仅提供传统的客服软件席位。报道称，其估值在约六个月内翻倍至 300 亿美元，这意味着本轮融资距上一次融资间隔很短，定价随企业采用这类 AI 智能体的需求上升而快速抬升。

**「为什么重要」** 对正在挑选客服 AI 供应商的企业来说，Sierra 手上多了 17.5 亿美元可用于大型联络中心项目的交付与扩张，在与既有厂商竞标时资金更充裕。同时，据报六个月内翻倍的估值抬高了增长预期，采购方在签长期合同前，值得把部署范围、效果如何计量以及续约条件写清楚。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/11/23/sierra-doubles-valuation-to-30b-within-six-months-as-demand-for-ai-in-cx-takes-off/">Sierra doubles valuation to $30B within six months as demand ...</a></li>
<li><a href="https://www.cmswire.com/contact-center/sierra-hits-30b-valuation-on-175b-series-f/">Sierra Hits $30 Billion Valuation on $1.75 Billion Series F</a></li>
<li><a href="https://sierra.ai/blog/series-f-30b">Series F (Building the digital front door) | Sierra</a></li>

</ul>
</details>

**标签**: `#AI funding`, `#enterprise AI`, `#customer experience AI`, `#Sierra`, `#Series F`

---

<a id="item-ai-news-7"></a>
### [沃尔玛开放 Agent Gateway，Meta Muse 可代用户抢购黑五商品](https://www.theverge.com/ai-artificial-intelligence/1039874/walmart-agent-gateway-meta-muse-black-friday) ⭐️ 7.0/10

沃尔玛正在推出一项已投入实际运行的 Agent Gateway 服务，允许 Meta 的 AI 代理 Muse 通过沃尔玛的 Sparky 助手替用户寻找并购买黑色星期五商品。沃尔玛表示，Agent Gateway 能让 AI 代理找到相关商品，又不必共享用户的购买历史。Muse 的购买行为通过“Agent Profiles”完成，该功能在用户的沃尔玛账户内为代理活动提供独立空间，用户可设置消费上限、逐笔批准购买，并查看 Muse 买下的所有商品记录。沃尔玛称这是其上月宣布的 Agent Gateway 的首次实际部署，目前正在逐步铺开，报道未说明复盖多少用户或何时全面开放。

The Verge AI · 11月23日 11:00

**「已证实与未证实」** 已证实：沃尔玛表示，Meta 的 Muse 可以通过 Sparky 助手和 Agent Gateway 查找并购买黑五商品，购买经“Agent Profiles”执行，用户可设消费上限、批准交易并查看购买记录（沃尔玛向 The Verge 说明）。
尚未证实：该功能具体向哪些用户、哪些地区开放，覆盖规模与全面上线时间；代理实际下单的成功率与准确性；以及是否有独立测试或用户实测数据。报道也未提及该服务是否收费或有无额外条件。

**「背景」** Meta 此前推出的 Muse 是一款能代替用户执行任务的个人 AI 代理，购物和比价是其对外展示的能力之一。沃尔玛在本次黑色星期五前一个月宣布了 Agent Gateway，称它可让外部 AI 代理找到相关商品，而不必共享用户的购买历史；这次 Muse 通过 Sparky 助手接入，是该网关的一次实际购物部署。具体购买发生在沃尔玛账户内的 Agent Profiles 中，用户可在那里设置消费上限、批准购买并查看代理的购买记录。

**「为什么重要」** 对开发代理购物功能的团队来说，这提供了一个可参照的落地形态：代理不再直接读取用户的购买历史，而是通过平台提供的网关与账户内的独立“代理档案”获得有限权限，并由用户设置消费上限和逐笔确认。使用该功能的消费者应先检查默认消费上限与批准设置，再让 Muse 下单，并在事后核对代理档案中的购买记录。

**「后续看点」** 黑色星期五过后，沃尔玛是否公布该网关的使用数据，以及是否把 Agent Gateway 从 Meta Muse 扩展到其他 AI 代理提供商。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/">Introducing Muse : The World’s First Personal AI Agent Built for...</a></li>
<li><a href="https://www.engadget.com/2253133/meta-reveals-its-ai-agent-that-can-shop-send-emails-and-plan-trips-on-your-behalf/">Meta Reveals Its AI Agent That Can Shop , Send Emails And Plan...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#agentic commerce`, `#Meta Muse`, `#Walmart`, `#Black Friday`

---

<a id="item-ai-news-8"></a>
### [马斯克称 SpaceX 在 AI 上落后，出租算力比自用更赚钱，《纽约时报》报道](https://www.techmeme.com/261123/p31#a261123p31) ⭐️ 7.0/10

《纽约时报》11 月 23 日报道，知情人士称，埃隆·马斯克已告诉 SpaceX 员工，公司在 AI 方面正在落后；同时，把公司数据中心的算力出租给包括 Anthropic 在内的竞争对手，比用于改进 SpaceX 自身产品更赚钱。报道称，这种做法正在让 SpaceX 自己的 AI 工作更难推进。上述说法来自知情人士，而非 SpaceX 的公开声明。

Techmeme · 11月23日 17:35

**「已证实与尚未证实」** 已证实：据《纽约时报》11 月 23 日报道（Techmeme 转引），马斯克已告知 SpaceX 员工公司在前沿 AI 上落后，并认为把数据中心的算力出租给竞争对手（包括 Anthropic）比用于改进自家产品更赚钱；Quartz 同日报道亦如此表述。

尚未证实：SpaceX 与马斯克本人均未公开确认上述内部讲话，相关说法全部来自《纽约时报》的匿名消息源；报道未披露租赁合同的规模、金额、期限，也未说明出租算力具体挤占了多少内部 AI 研发资源。客户名单亦不一致：Techmeme 与《纽约时报》摘要仅点名 Anthropic，而 Quartz 标题及《纽约时报》文章链接同时提到 Google，Google 是否为租户尚无独立证实。

**「背景」** AI 实验室正以空前规模外租算力：11 月 17 日的日报曾报道，Anthropic 据称计划通过名为“Anthropic Direct”的项目在 2045 年前承诺投入逾 9000 亿美元，其中包括以每年 72 亿美元租用 87.5 万块 TPU（谷歌设计的 AI 芯片）。与此同时，SpaceX 也在向 AI 扩张——《卫报》4 月报道称，SpaceX 获得了以 600 亿美元收购代码生成初创公司 Cursor 的选择权，或改为支付 100 亿美元建立合作。这样一来，“把自建数据中心的算力租出去，还是留给自家产品用”就成了一项需要权衡的实际取舍。

**「为什么重要」** 如果 SpaceX 继续优先对外出租算力，其内部 AI 团队将与付费客户争夺同一批数据中心容量，自身 AI 项目的推进可能受到制约；Anthropic 等租用方则获得了一个新的算力来源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techmeme.com/261117/p11#a261117p11">2026-11-17 — Report: Anthropic&#x27;s &quot;Anthropic Direct&quot; plan commits $900B+ to 2045, leasing 875K TPUs</a></li>
<li><a href="https://www.nytimes.com/2026/11/23/business/elon-musk-ai-anthropic-google.html">Elon Musk Faces an A.I. Dilemma at SpaceX - The New York Times</a></li>
<li><a href="https://qz.com/spacex-leases-computing-power-anthropic-google-ai-112326">SpaceX leases computing power to Anthropic, Google amid AI push</a></li>
<li><a href="https://www.theguardian.com/technology/2026/apr/21/spacex-cursor-ai-startup">SpaceX secures option to buy AI startup Cursor for... | The Guardian</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#AI compute`, `#data centers`, `#Elon Musk`, `#AI infrastructure`

---

<a id="item-ai-news-9"></a>
### [METR 更新 AI 时间跨度图：判断类任务进展落后于编程](https://www.technologyreview.com/2026/11/23/1149548/the-download-ai-judgment-problem-carbon-removal-crop-threat/) ⭐️ 7.0/10

AI 评估非营利机构 METR 发布新版报告，更新其被广泛引用的“时间跨度”图（用模型能完成多长的任务来衡量能力）。新版加入设计 AI 评估、给哲学论证打分等更开放的任务，结论是部分能力仍在指数级提升，但模型在需要判断力的任务上不如编程类任务。MIT Technology Review 的《The Download》简报转述了这一结果，并指出这类能力对自动化研究与开发可能很关键。

MIT Technology Review · 11月23日 13:10

**「已证实与未证实」** 已证实：MIT Technology Review 的简报称，METR 的新报告更新了其时间跨度图，新增开放式任务，并发现部分能力呈指数级改善、模型在判断类任务上表现较弱。
尚未证实：简报未给出具体分数、任务数量或改进幅度，也未直接链接完整报告；因此这些结论仍需看 METR 的原始方法和独立复现。

**「背景」** METR 是一家独立运营的 AI 评估非营利机构，其评测由自己设计并发布结果，其中“任务完成时间跨度”（time horizon，以人类完成同一任务所需时间衡量模型能处理多长的任务）被广泛用于 AI 能力预测与政策讨论。该机构 2025 年 3 月的论文与 2026 年 1 月 29 日发布的 Time Horizon 1.1 曾把前沿趋势描述为大约每 196 天（约 7 个月）翻倍。MIT Technology Review 今年 2 月的一篇文章把这张图称为“AI 界最被误读的图表”，此次新报告正是在该版本基础上扩充了开放式任务。

**「为什么重要」** 如果团队用时间跨度图外推模型自动化研发的进度，应把判断类、开放式的任务单独纳入评测；否则只凭编程等强项会高估模型在真实研发流程中的可靠性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://capitalandcompute.net/ai-benchmarks/metr-time-horizon/">METR Time Horizon : AI Ability Measured in Human Time</a></li>
<li><a href="https://www.baristalabs.io/blog/metr-ai-task-horizons-7-month-doubling-2026">METR &#x27;s Latest Time - Horizon Data Makes AI Capability Planning Much...</a></li>

</ul>
</details>

**标签**: `#METR`, `#AI evaluation`, `#AI capabilities`, `#time horizon`, `#judgment`

---

<a id="item-ai-news-10"></a>
### [OpenAI 首席科学家提议设 AI 开发行业统一门槛](http://www.geekpark.net/news/374304) ⭐️ 7.0/10

11 月 22 日，OpenAI 首席科学家雅库布·帕霍茨基发文，提议各家 AI 企业建立行业统一标准，对先进模型的开发设置共同限制：在研究人员能更可靠地理解和监控模型行为之前，不突破约定的发展门槛。他提出用困惑度（衡量模型预测下一个文本 token 的能力，数值越低表示预测越强）追踪预训练进展，并披露 OpenAI 内部数据：GPT-3.5 对数困惑度约 0.99、GPT-4 约 0.91；低于 0.8 时模型在网络安全和数学上出现新能力，约 0.76 时在部分开放数学问题上取得突破，预计 0.68—0.7 区间可能出现更多变革性能力，但具体是什么尚不确定。帕霍茨基警告，AI 最早可能在 2027 年推动预训练技术快速进展，而对齐和行为监控可能跟不上；他建议企业共同制定评测、透明度和安全红队标准，并在模型首次投入使用前完成评估，奥尔特曼公开支持这一提议，称希望行业就共同限制达成一致。

GeekPark \(极客公园\) · 11月23日 01:22

**「已证实与未证实」** 已证实：据极客公园援引 CnBeta 的报道，OpenAI 首席科学家雅库布·帕霍茨基（Jakub Pachocki）于 11 月 22 日发表文章，提议各家 AI 企业为先进模型开发建立可测量的行业共同限制，并以困惑度（perplexity，衡量模型预测下一个文本 Token 的能力）等可跨企业追踪的指标设定首个开发门槛；TechCrunch 同日也报道了这篇文章，并指出其核心正是困惑度这一度量。OpenAI CEO 萨姆·奥尔特曼公开称这是 OpenAI 一段时间以来最重要的文章之一，并支持行业就共同限制达成一致。文章还披露了 OpenAI 内部的对数困惑度数据：GPT-3.5 约 0.99、GPT-4 约 0.91。

尚未证实：对数困惑度降至 0.8 时出现网络安全与数学新能力、约 0.76 时在部分开放数学问题上取得突破，以及进入 0.68–0.7 区间可能出现“变革性能力”，这些门槛与对应现象都只是 OpenAI 一方的内部观察；关于最早 2027 年预训练出现快速进展、而对齐与行为监控可能跟不上的判断同样属于该公司预测，未经独立验证。目前没有任何其他前沿实验室公开承诺加入或公布可比的困惑度数据，也尚无成形的标准、评测协议或实施时间表；中文报道属于二手汇总，未附原文链接和完整评测方法。

**「背景」** 困惑度（perplexity）衡量模型预测下一个文本 Token 的能力，数值越低说明预测越准；帕霍茨基把它当作预训练进展的替代标尺，理由是传统能力评测基准会随技术进步迅速过时。围绕模型行为监控，OpenAI 此前已有动作：AI Daily Radar 11 月 16 日的日报曾报道，OpenAI 启动首阶段「内嵌评估」，邀请 Apollo Research、METR、Transluce 和 Goodfire 四家外部机构进入内部独立评估模型的对齐、防护与监控系统，但未公布覆盖哪些模型、时间表与任何结论。此次提议的不同之处在于把评估从单家公司内部推到跨企业层面，用可共同追踪的指标设定统一的开发门槛。

**「为什么重要」** 对前沿实验室来说，这一提议若被采纳，会把预训练阶段的困惑度阈值变成与红队测试、透明度标准并列的开发闸门，而不是等模型发布后再用容易过时的任务基准评估；但目前仍只是提议，文章没有说明阈值如何执行或由谁核验，也尚无企业宣布加入。

**「后续看点」** 关注其他前沿 AI 实验室是否公开响应这一行业统一限制提议，以及 OpenAI 是否公布支撑 0.68—0.7 阈值判断的评测方法和数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/our-first-phase-of-embedded-assessments">2026-11-16 — OpenAI 启动首批内嵌评估：Apollo、METR 等四家机构参与</a></li>
<li><a href="https://aiweekly.co/alerts/openais-pachocki-urges-frontier-pause-at-068-07-perplexity">OpenAI &#x27;s Pachocki urges frontier pause at... | AI Weekly</a></li>
<li><a href="https://forklog.com/en/openai-chief-scientist-proposes-measurable-limits-on-advanced-ai-development/">OpenAI chief scientist proposes measurable limits on advanced AI ...</a></li>
<li><a href="https://techcrunch.com/2026/11/22/openais-chief-scientist-has-thoughts-on-how-to-limit-ai-development/">OpenAI ’s chief scientist has thoughts on how to limit AI development</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#AI安全`, `#模型评测`, `#预训练`, `#AI治理`

---

## 芯片与算力

<a id="item-chips-compute-1"></a>
### [Penguin 展出光子外置内存：最高 576GB HBM3E，2027 下半年送样](https://www.tomshardware.com/pc-components/dram/penguin-shows-off-photonic-memory-box-at-sc26-that-can-expand-ai-accelerator-capacity-over-optical-links-device-sports-up-to-576gb-of-hbm3e-customer-samples-expected-in-2027) ⭐️ 7.0/10

Penguin Solutions 在 SC26 超算展上展出了 MemoryAI Photonic Appliance——一台通过光纤链路挂在主机之外的 AI 内存扩展设备：最高 576GB HBM3E 加 16TB DDR5，整机聚合带宽目标 7.2 TB/s（双向各约 3.6 TB/s），走 CXL.mem 3.1 协议、最远 30 米。它基于 Marvell 的 Photonic Fabric 架构，用 8 个 Photonic Fabric 内存模块（PFMM），每模块含 72GB HBM3E 缓存和一个 16 发 16 收、每通道 224 Gbps 的光互连中介层；主机侧可选 PCIe 6.0/CXL 3.1 的光子网卡（PF-NIC，单口最高 2 Tbps、延迟低于 350ns，不含 PCIe/CXL 开销），或把光子 chiplet 直接集成进 XPU（最高 14.4 Tbps、延迟低于 200ns）。Penguin 称应用无需修改即可透明访问外部内存，但客户样品要到 2027 年下半年，且目前没有任何实测性能数据。一个关键限制是：Nvidia 与 AMD 的数据中心 GPU 普遍不支持通用 CXL.mem 主机接口，因此这套方案现阶段只能服务支持 CXL.mem 的 CPU、定制 XPU 或集成 Marvell 光子 chiplet 的加速器。

Tom&\#x27;s Hardware · 11月23日 18:00

**「已证实与未证实」** 已证实：Penguin Solutions 在 SC26 展出了该设备，Tom&\#x27;s Hardware 报道其 576GB HBM3E／16TB DDR5 容量、7.2 TB/s 聚合带宽目标、三种内存访问模式（HBM 直连、HBM 作 DDR5 写穿缓存、DDR5 直连）以及基于 Marvell PFMM 与 PF-NIC 的架构细节。尚未证实：透明访问无需改应用、低于 350ns／200ns 的延迟（前者尚未计入 PCIe/CXL 开销）、2027 年下半年送样能否如期，以及多加速器共享后每张卡实际分到多少带宽——这些均无独立测试或第三方验证。

**「背景」** HBM（高带宽内存）是直接封装在 AI 加速器旁的堆叠内存，容量有限，往往成为运行大模型时的硬瓶颈；过去开发者只能通过增加或更换加速器来扩充内存。CXL 是基于 PCIe 的互连标准，其 CXL.mem 子协议允许处理器用普通的 load/store 指令访问外部内存，把远端内存当作本地内存的一个层级使用，CPU 已普遍支持这一扩展方式。Penguin 的方案在此之上叠加了 Marvell 的光子互连，把外部内存池的访问距离延伸到最长 30 米。

**「为什么重要」** 对采购者而言，真正决定能否用的是主机兼容性而非容量：由于主流 Nvidia、AMD GPU 不支持通用 CXL.mem，现有集群无法直接受益；若绕道支持 CXL.mem 的 CPU 访问，延迟将远超宣传的 350ns，可能吃掉扩容带来的收益。有兴趣的团队应优先确认目标主机是否在硬件与内存管理软件两层支持外部内存映射，并等待实测数据。

**「后续看点」** 2027 年下半年客户样品是否如期交付，以及届时 Penguin 与 Marvell 是否公布实测延迟、八卡分摊后的单卡带宽和支持主机清单。另一个悬而未决的问题是：2028 年行业转向 HBM4／HBM4E 后，Penguin 计划从哪里获得 HBM3E 的批量供应。

**标签**: `#photonic memory`, `#HBM3E`, `#CXL`, `#AI accelerators`, `#optical interconnects`

---

<a id="item-chips-compute-2"></a>
### [AI 服务器签约后涨价最高 45%，内存短缺推高节点成本](https://www.tomshardware.com/tech-industry/big-tech/ai-server-makers-hike-prices-up-to-45-percent-months-after-contracts-are-signed-as-ram-shortage-triples-memory-heavy-cpu-node-costs-financial-firms-still-pay-up-as-the-compute-is-valuable) ⭐️ 7.0/10

据《金融时报》报道，交易和金融服务公司在数据中心服务器合同签署数月后，被要求支付最高 45% 的追加费用；Tom&\#x27;s Hardware 转述称，一名匿名知情人士提到的涨幅为 25%、30% 或 45%。报道称图形处理器（GPU）服务器涨价 20%–30%，而内存密集型 CPU 节点的价格翻倍甚至涨至三倍，原因指向 DRAM（动态随机存取存储器）供应紧张。部分金融公司仍表示会买单，称算力对其有价值；报道未点名具体服务器厂商、型号或合同金额。

Tom&\#x27;s Hardware · 11月23日 12:30

**「已证实与未证实」** 已证实：《金融时报》报道称，服务器供应商在合同签署数月后向客户提出涨价，涨幅分别有 25%、30%、45% 等档位；GPU 服务器涨价 20%–30%，内存密集型 CPU 节点价格翻倍或涨至三倍（Tom&\#x27;s Hardware 与 TrendForce 均转述该报道）。另据《爱尔兰时报》报道，XTX Finland Oy 已于 2026 年 6 月就戴尔爱尔兰子公司在一笔 5.49 亿美元、1680 台服务器订单上追加 6200 万至 7000 万美元的要求提起诉讼，案件仍在审理中。

尚未证实：上述涨幅均出自《金融时报》援引的未具名消息人士，没有具名供应商出面确认具体涨幅、涉及客户或机型；报道也未说明这些合同是否包含价格波动条款——《金融时报》询问过的公司均未证实也未否认。DRAM 短缺是涨价主因的说法同样只有消息人士口径，缺少独立的成本拆解或第三方核价。

**「背景」** DRAM 是服务器的主内存，AI 服务器通常要配置大量内存条；当 DRAM 供应紧张时，整机厂商会把内存成本上涨转嫁到报价里，内存配置越重的 CPU 节点受冲击越明显。此类采购通常提前数月锁定价格，但今年 6 月 XTX Finland 已因戴尔在 5.49 亿美元服务器订单上追加 6200 万至 7000 万美元而起诉戴尔爱尔兰子公司，案件仍在审理，说明合同价并非总能挡住内存涨价。

**「为什么重要」** 对这些采购方而言，合同价已不再是最终价：报道中的金融公司即使面对 25%–45% 的追加账单仍继续采购，说明在算力紧缺时压价空间有限。XTX Finland Oy 已就 Dell 爱尔兰子公司要求在原定 5.49 亿美元之外再加 6200 万–7000 万美元一事起诉，报道称 XTX 还额外支付 500 万美元加入条款以防止价格变动；该案表明价格保护条款也可能需要通过诉讼兑现。

**「后续看点」** 后续可关注 XTX Finland Oy 诉 Dell 爱尔兰子公司案的进展；报道称该案仍在进行，若法院对签约后加价作出裁定，将为类似合同争议提供参照。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ft.com/content/dd2a6594-6146-4ff1-ac8e-54749c1fc99f?syn-25a6b1a6=1">Tech suppliers raise AI server prices up to 45% months after ...</a></li>
<li><a href="https://www.trendforce.com/news/2026/11/23/news-ai-server-prices-reportedly-rise-up-to-45-as-dell-hpe-and-others-raise-prices-after-deals/">[News] AI Server Prices Reportedly Rise Up to 45% as Dell ...</a></li>
<li><a href="https://www.gate.com/news/detail/DELL/ai-server-makers-raise-prices-up-to-45-post-contract-as-ram-shortage-hits-25811641">AI Server Makers Raise Prices Up to 45% Post-Contract as RAM ...</a></li>

</ul>
</details>

**标签**: `#AI servers`, `#memory shortage`, `#data center costs`, `#supply chain pricing`

---

## 电动车与新能源

<a id="item-ev-energy-1"></a>
### [大众计划到 2030 年每年从中国出口约 30 万辆汽车](https://electrek.co/2026/11/23/if-you-cant-beat-em-vw-to-export-300000-chinese-built-cars-per-year-by-2030/) ⭐️ 7.0/10

大众汽车计划到 2030 年每年从中国出口约 30 万辆在中国生产的汽车，把中国制造当作面向海外市场的成本基础，而不是仅服务本土销量。Electrek 11 月 23 日报道称，这一计划出台的背景是大众销量下滑、年产能削减规模接近 100 万辆，以及一批价格更低的中国品牌竞争对手正在进入西方市场。报道没有说明将出口哪些车型、销往哪些具体市场，也没有引用大众的一手声明，因此这目前是一个公开的出口目标，而非已经实现的出口量。

Electrek · 11月23日 12:39

**「已证实与未证实」** 已证实：Electrek 报道称，大众汽车计划到 2030 年每年从中国出口约 30 万辆中国制造的汽车；同一篇报道还提到，大众销量正在下滑，年产能削减规模接近 100 万辆，并提到一批价格更低的中国竞争对手正在进入西方市场。

尚未证实：这篇 Electrek 报道正文被截断，没有引用大众的官方声明或新闻稿，也没有说明涉及哪些车型、出口到哪些市场、这 30 万辆指整车出口还是包含其他形式，以及产能削减的具体规模和时间表。目前只有 Electrek 一家报道，大众方面并未公开确认上述细节。

**「背景」** 大众在中国已经铺开低成本纯电产品线：AI Daily Radar 11 月 17 日的日报提到，一汽-大众基于 CMP 平台的中型纯电轿车 ID. Aura L5 已在中国开启预售，CLTC 续航 580 公里（CLTC 是中国测试循环，数值通常高于欧洲 WLTP 与美国 EPA）。据 carnewschina 报道，同系列的中型纯电 SUV ID. Aura T6 也已在中国开始交付，CLTC 续航最高 660 公里，起售价 129,900 元（约 19,375 美元），对标比亚迪 Sealion 06 等车型——这些先在中国销售、定价紧贴本土竞争的车型，正是“中国制造大众出口”计划的现实基础。

**「为什么重要」** 如果目标兑现，大众在华工厂的角色将从主要供应本土市场转为向海外供货的出口基地，欧洲等市场的消费者可能买到与中国品牌直接比价的大众车型；与此同时，大众在本土削减产能与加深对中国生产的依赖会同时发生，其成本结构与中国产线绑得更紧。

**「后续看点」** 值得关注大众在下一份财报或年度规划中是否给出明确的出口车型清单与目标市场，以及首批中国产出口车辆何时装船发运。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.electrive.com/2026/11/17/volkswagen-opens-pre-orders-for-id-aura-l5-in-china/">2026-11-17 — Volkswagen opens China pre-orders for ID. Aura L5 electric sedan</a></li>
<li><a href="https://carnewschina.com/2026/10/02/volkswagen-id-aura-t6-began-deliveries-in-china-with-660-km-of-range/">Volkswagen ID . Aura T6 began deliveries in China with 660 km range</a></li>

</ul>
</details>

**标签**: `#Volkswagen`, `#China`, `#EV manufacturing`, `#exports`, `#automaker strategy`

---

<a id="item-ev-energy-2"></a>
### [荷兰法院临时裁定：比亚迪 Ti7 因外观近似捷豹路虎卫士被禁在欧盟销售](https://www.electrive.com/2026/11/23/court-deems-byd-ti7-too-similar-to-jlr-defender/) ⭐️ 7.0/10

荷兰一家法院在临时（简易）诉讼程序中裁定，十家比亚迪子公司不得在欧盟范围内生产或销售 Ti7 车型，理由是法官认为该车外观与捷豹路虎（JLR）的卫士（Defender）过于相似。据 electrive 报道，这一裁定属临时措施，主审诉讼仍在进行，报道未提及禁令的生效时间、是否可上诉或是否需要缴纳保证金，也未提供法院裁决书原文。裁定涉及的是单一车型和十家被点名的子公司，而非比亚迪在欧盟的全部业务。

Electrive · 11月23日 17:30

**「已证实与未证实」** 已证实：electrive 报道，荷兰法院在临时程序中命令十家比亚迪子公司停止在欧盟生产与销售 Ti7，认定该车外观与捷豹路虎 Defender 过于相似；主审仍未结束，这项临时命令并非终局判决。卫报亦报道，该禁令将在裁决一周后生效。
尚未证实：临时命令的具体法律依据究竟是外观设计权还是版权，以及禁令覆盖的具体车型版本和地域范围，目前仍不清楚；Automotive News 以“版权案”描述此案，与“外观相似”的表述并不完全一致。卫报称，裁决提到比亚迪“目前没有在欧盟市场推出 Ti7 的具体计划”；这一细节仅来自单家报道，若属实，禁令对实际销量的影响仍待观察。

**「背景」** 涉事车型在中国以方程豹钛 7（Fang Cheng Bao Tai 7）之名销售，是一款七座插电混动 SUV；捷豹路虎（JLR）指其外观抄袭路虎卫士（Defender），并在荷兰提起设计侵权诉讼。据 carnewschina.com 报道，JLR 此前通过扣押程序取得了该车型的相关资料，而荷兰法院随后反过来要求 JLR 销毁被扣押的文件，否则将面临 553,850 美元罚款——这是同一纠纷中的程序性交锋。此次公布的禁售令属于临时裁定，主审程序仍在进行。

**「为什么重要」** 对比亚迪而言，这是一项覆盖整个欧盟、直接针对具体车型的即时限制：Ti7 的在售与生产安排可能被迫中断，已签订单和经销商库存如何处理成为现实问题；同时，这也提示其他计划进入欧洲市场的中国车企，外观设计近似风险可能先以临时禁令的形式落地，而不是等到主审判决。

**「后续看点」** 主审诉讼的实体判决结果，以及比亚迪是否就这项临时裁定提出上诉或申请调整禁令范围。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://carnewschina.com/2026/11/12/dutch-court-orders-jaguar-land-rover-to-destroy-seized-byd-ti-7-files-or-face-553850-usd-penalty/">Dutch court orders Jaguar Land Rover to destroy seized BYD Ti...</a></li>
<li><a href="https://www.theguardian.com/business/2026/nov/22/court-bans-china-byd-selling-defender-clone-suv-in-eu">Court bans China’s BYD from selling ‘ Defender clone... | The Guardian</a></li>
<li><a href="https://www.theguardian.com/business/2026/nov/22/court-bans-china-byd-selling-defender-clone-suv-in-eu">Court bans China’s BYD from selling ‘ Defender clone’ SUV in EU</a></li>
<li><a href="https://www.autonews.com/jaguar-land-rover/ane-byd-loses-copyright-case-over-jlr-defender-lookalike-1120/">BYD loses copyright case over Defender lookalike - Automotive News</a></li>

</ul>
</details>

**标签**: `#BYD`, `#JLR Defender`, `#design dispute`, `#EU injunction`, `#EV sales`

---

<a id="item-ev-energy-3"></a>
### [欧盟理事会倾向把企业车队电动车配额降为自愿目标](https://www.electrive.com/2026/11/23/eu-council-signals-shift-away-from-binding-ev-quotas-for-corporate-fleets/) ⭐️ 7.0/10

欧盟理事会在讨论欧盟委员会的“汽车一揽子计划”（Auto Package）时，似乎正效仿欧洲议会的做法，把针对企业车队的强制性电动车配额降级为自愿目标。按照委员会最初的草案，成员国须为 2030 年起电动公司用车的推广设定具体的强制要求；欧洲议会已先行将约束性配额改为自愿目标，理事会现在释放出跟进信号。这目前仍是政策信号而非最终决定，报道未披露理事会立场的具体细节或官方文件。

Electrive · 11月23日 14:30

**「已证实与未证实」** 已证实：据欧洲议会新闻公报（2026 年 11 月 4 日），议会相关委员会以 89 票赞成、29 票反对、4 票弃权通过草案立场，将成员国在 2030 年和 2035 年新注册企业车辆中零排放与低排放车辆占比目标设为“努力目标”（aspirational targets），区间为 67% 至 95%；草案覆盖欧盟境内雇员超过 250 人、营业额超过 5000 万欧元的大型企业注册的企业用车和厢式车。electrive 10 月 27 日亦报道，欧洲人民党（EVP）已在议会内取得多数，反对具约束力的企业车队电动车配额。

尚未证实：报道称欧盟理事会“似乎”正跟随议会将约束性配额降为自愿目标，但未引用理事会官方文件、表决结果或具体立场文本，理事会正式立场及最终三方谈判结果均未确定；报道也未给出后续表决或生效时间表。

**「背景」** 欧盟委员会的“汽车一揽子方案”（Auto Package）属于立法提案，需要由欧洲议会和代表成员国政府的欧盟理事会共同修改、并在两机构达成一致后才能生效。委员会原稿曾要求成员国自 2030 年起为电动公务车设定具体配额，但欧洲议会已先行将约束性配额改为自愿目标；理事会如今释放出跟进的信号，这意味着该条款在进入议会与理事会之间的最终谈判前可能被进一步弱化。

**「为什么重要」** 如果约束性配额最终退化为自愿目标，成员国就不再被要求为 2030 年起电动公司用车的推广设定可核查的具体指标，这一推广渠道的执行力度会明显减弱；车队运营商与车企在 2030 年前的合规规划，也将更多取决于各国自行作出的自愿承诺，而非统一的欧盟义务。

**「后续看点」** 理事会将发布怎样的正式立场文件，以及理事会、欧洲议会与欧盟委员会在随后三方谈判（trilogue）中如何处置“汽车一揽子计划”的最终文本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.europarl.europa.eu/news/en/press-room/20261103IPR48612/corporate-fleets-accelerating-the-uptake-of-zero-and-low-emission-vehicles">Corporate fleets: accelerating the uptake of zero- and low ...</a></li>
<li><a href="https://www.europarl.europa.eu/pdfs/news/expert/2026/11/press_release/20261103IPR48612/20261103IPR48612_en.pdf">Corporate fleets: accelerating the uptake of zero- and low ...</a></li>
<li><a href="https://www.electrive.com/2026/10/27/evp-secures-majority-against-binding-ev-quotas-for-large-corporate-fleets/">EVP secures majority against binding EV quotas for large ...</a></li>

</ul>
</details>

**标签**: `#EU policy`, `#EV quotas`, `#corporate fleets`, `#electric vehicles`, `#regulation`

---

<a id="item-ev-energy-4"></a>
### [宝马 iX4 在德布勒森工厂投产，与 iX3 共线](https://www.electrive.com/2026/11/23/bmw-ix4-rolls-off-production-line-alongside-ix3-in-debrecen/) ⭐️ 7.0/10

宝马已在匈牙利德布勒森（Debrecen）工厂启动 iX4 的批量生产，使其成为继 iX3 之后在该工厂生产的第二款 Neue Klasse（宝马新一代电动车平台）车型。iX4 是一款采用轿跑式车顶线条的 SUV，将于 2027 年 3 月起交付经销商，初期提供两种动力版本。报道没有给出续航、电池容量、售价或产能数字，也没有说明两种动力版本的具体形式。

Electrive · 11月23日 11:32

**「已证实与未证实」** 已证实：据 electrive 报道，宝马 iX4 已在德布勒森工厂开始批量生产，该工厂此前已生产 iX3，iX4 是这里的第二款 Neue Klasse 车型。
尚未证实：报道未提供 iX4 的售价、续航、电池与动力参数、产能规划，也未说明“2027 年 3 月起交付经销商”是否为确定日期；两款动力版本的具体差异同样没有披露。

**「背景」** 新世代（Neue Klasse）是宝马为其下一代纯电车型启用的整套新技术系列，涵盖新的纯电平台与电子电气架构，匈牙利德布勒森工厂则是专门为这批车型新建的整车厂，首款在此下线的车型是 iX3。宝马新闻稿确认，iX4 是继 iX3 之后在德布勒森投产的第二款新世代车型，且该工厂在投产这款全新车型前不到两个月才刚刚启用 24 小时连续生产。

**「为什么重要」** 对欧洲等市场的买家来说，iX4 提供的是与 iX3 不同的轿跑式车身，但即便现在已下线，也要等到 2027 年 3 月才能通过经销商提车，因此有意购买的人需要把交付时间纳入比较。对宝马而言，德布勒森工厂从此同时生产两款 Neue Klasse 车型，产能爬坡和双车型共线的质量一致性将直接影响交付节奏。

**「后续看点」** 关注宝马在 2027 年 3 月交付启动前公布的 iX4 定价与完整参数，以及德布勒森工厂双车型共线后的实际产量数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsroom.bmwgroup.com/global/series-production-of-the-bmw-ix4-gets-underway/">BMW iX4 Series Production Begins</a></li>

</ul>
</details>

**标签**: `#BMW`, `#Neue Klasse`, `#EV production`, `#electric SUV`, `#Hungary`

---

<a id="item-ev-energy-5"></a>
### [美参议院通过许可改革法案，允许太阳能开发商起诉联邦机构](https://www.pv-magazine.com/2026/11/23/us-senate-passes-permitting-bill-letting-solar-developers-sue-agencies/) ⭐️ 7.0/10

美国参议院以 62 比 33 通过《两党美国可负担性与就业法案》（BAAJA），将其作为众议院已通过的税收法案 H.R. 2347 的修正案；参议院在 11 月 18 日先以 69 比 27 同意用 BAAJA 全文替换原法案文本。据智库两党政策中心（BPC）逐条摘要，法案第 1402 条允许太阳能、陆上风电、储能、输电等 46 类项目的开发商，在许可被“恶意”拒绝或超过法定期限 60 天仍未获批、且构成差别对待模式时起诉联邦机构，须以过去 10 年的统计数据作证，赔偿为项目合理预期建设成本的 50%至 100%；第 1401 条则禁止机构撤销或实质修改 2026 年 11 月 6 日及之后生效的许可（含法院命令、欺诈、紧急危害等六项例外）。法案还将《国家环境政策法》（NEPA）的起诉期限从六年缩短至 150 天，并要求联邦能源管理委员会（FERC）在州政府一年未决后为 230 千伏及以上等合格输电线路发放许可。这还不是法律：众议院须在明年 1 月初本届国会结束前处理参议院修正案，否则法案需重新提出。

pv magazine · 11月23日 08:15

**「已证实与未证实」** 已证实：参议院以 62 比 33 通过作为 H.R. 2347 修正案的 BAAJA，此前 11 月 18 日以 69 比 27 同意替换文本，11 月 9 日以 73 比 25 通过程序性投票；法案由 Capito、Lee、Whitehouse、Heinrich 四位参议员于 9 月 30 日提出。上述条款内容来自 BPC 对参议院通过文本的逐条摘要。
尚未证实：众议院是否放行、法案能否在 1 月初前成为法律；太阳能产业协会（SEIA）所称“2028 至 2035 年新增 167 吉瓦太阳能、2035 年占比超 18%”是该行业协会自己的测算，未获独立验证；赔偿比例和 60 天、150 天等具体门槛均依据 BPC 摘要，报道未提供独立核对。

**「背景」** NEPA 要求联邦行动前进行环境审查，长期以来是太阳能与输电项目遭遇诉讼拖延的主要环节；FERC 则负责跨州输电的联邦许可。2025 年 7 月，内政部出台规定，对联邦土地上的风光项目加设由内政部长 Doug Burgum 把关的额外审查，SEIA 反对该规定并警告许可拖延推高消费者成本；2026 年 4 月 21 日，马萨诸塞州联邦地区法官 Denise J. Casper 发布初步禁令，认定挑战者很可能证明该政策武断专断。

**「为什么重要」** 对项目开发商而言，第 1402 条提供了一条前所未有的起诉通道，但门槛不低：原告必须拿出过去 10 年的统计证据证明“差别对待模式”，这意味着需要长期、可比的审批记录，单个项目的延误未必够用。反过来，NEPA 起诉期限从六年压缩到 150 天、法院认定违规后只能发回机构而不得撤销许可，会明显压缩环保团体阻止项目的常用路径——Sierra Club 已明确反对，称法案“消除了法院对违法行为采取行动的权力”。

**「后续看点」** 众议院是否在明年 1 月初本届国会闭幕、新当选的民主党多数就位前通过参议院修正案；若未通过，法案须在新一届国会重新提出。

**标签**: `#permitting reform`, `#US energy policy`, `#solar`, `#transmission`, `#Congress`

---

<a id="item-ev-energy-6"></a>
### [纽约州公布先进核能总体规划，目标新增 5 吉瓦](https://www.world-nuclear-news.org/articles/new-york-unveils-advanced-nuclear-master-plan) ⭐️ 7.0/10

纽约州州长凯西·霍楚尔宣布，《负责任先进核能开发总体规划》已经完成，为全州实现新增 5 吉瓦核电装机容量的目标列出了路线图。先进核能（advanced nuclear）一般指区别于传统大型轻水堆的新一代反应堆设计。按照世界核能新闻的报道，这份文件目前只是一份规划框架，还不是已获批准的具体建设项目。报道没有披露计划采用的反应堆类型、选址、建设时间表或资金安排，因此 5 吉瓦仍是政策目标，并不等于可以执行的建设承诺。

World Nuclear News · 11月23日 15:55

**「已证实与未证实」** 已证实：据世界核能新闻报道，州长凯西·霍楚尔宣布《负责任先进核能开发总体规划》已完成，该规划为实现新增 5 吉瓦核电装机容量的目标制定了路线图。
尚未证实：规划包含哪些具体项目、采用何种反应堆技术、项目选址在哪里、资金从何而来、需要经过哪些审批和开工时间安排，以及 5 吉瓦目标能否落实；报道未给出任何日期，也未说明州议会或监管机构后续将如何审议。

**「背景」** 先进核能通常指小型模块化反应堆（SMR）和非轻水冷却等新设计：单机功率小于传统大型核电站，多采用工厂预制，其中不少设计需要丰度高于常规燃料（约 5%）的高纯度低浓缩铀（HALEU）。AI Daily Radar 11 月 18 日的日报曾报道，Urenco 与 Blykalla 签署了首个面向商用铅冷反应堆的 HALEU 浓缩合同，说明这类燃料的供应链仍在搭建之中。纽约的 5 GW 目标是本轮规划的出发点，此次公布的是一份路线图，而非已获批的建设项目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.world-nuclear-news.org/articles/urenco-blykalla-sign-haleu-deal">2026-11-18 — Urenco and Blykalla sign first HALEU enrichment deal for a lead-cooled reactor</a></li>

</ul>
</details>

**标签**: `#nuclear energy`, `#New York policy`, `#advanced nuclear`, `#clean energy`

---

## 航天

<a id="item-space-1"></a>
### [星舰飞船完成轨道级回收验证](http://www.geekpark.net/news/374355) ⭐️ 9.0/10

极客公园的一篇分析文章称，美国中部时间 11 月 14 日，SpaceX 的星舰飞船在约 22.5 小时的轨道飞行后返回，被发射塔机械臂捕获；文章称这是人类首次完成轨道级大载重飞船的回收工程验证，使二级回收首次有了成功案例，但没有提供 SpaceX 的官方确认或独立测量数据。文章区分了两级回收的技术难度：一级分离速度约为 2 公里/秒，返回耗时 6 至 7 分钟；二级需要从约 7.8 公里/秒的轨道速度再入，返回耗时 30 分钟至 1 小时，关键难点包括热防护、通信黑障和精准着陆。文章还称，中国商业航天公司穿越者规划了 CYZ1 亚轨道可复用飞船、CYZ2.1 轨道货船（近地轨道 20 吨上行、10 吨下行）和 CYZ2.2 载人版，并已启动未来 30 次商业载人发射的运载服务招标。

GeekPark \(极客公园\) · 11月23日 07:49

**「已证实与未证实」** 已证实：据 Ars Technica 与 phys.org 报道，SpaceX 于 2026 年 11 月 13 日执行星舰第 15 次试飞，飞船在 11 月 14 日返回时于得州星基地被发射塔机械臂捕获；本次试飞同时回收了超重型助推器与飞船上面级，是星舰首次实现两级同时回收。
尚未证实：极客公园所称“约 22.5 小时轨道飞行”“人类航天史上第一次完成轨道级大载重飞船回收工程验证”属该媒体的表述与业内解读，文中未直接引述 SpaceX 的说法；关于穿越者的“全球第三家完成此类全尺寸着陆缓冲试验”“触地冲击过载控制在 5g 以内”、三阶段研制规划，以及面向国内火箭企业采购“未来 30 次商业载人发射”运力等信息，均出自该公司自述，无独立来源验证；文章也未交代捕获后飞船的实际状态与复用计划。

**「背景：从一级回收到二级再入」** 此前所有成功的火箭回收案例都集中在一级：SpaceX 于 2015 年首次完成火箭一子级回收，按极客公园的梳理，国内国家队与民营公司直到 2026 年才分别实现一子级回收，中间相隔约 11 年。AI Daily Radar 11 月 15 日的日报曾报道，星舰第 15 次试飞中飞船在轨约 22.5 小时、绕地球 14 圈后被发射塔机械臂接住；但同一任务的超重助推器在返场途中因制导、导航与控制问题中止捕获，最终触发飞行终止系统落水，SpaceX 当时也没有给出这艘飞船的复用时间表。

**「为什么重要」** 对国内商业航天企业而言，这次回收把「火箭一子级回收」和「飞船二级再入回收」明确分成两条产业赛道：公开进展显示，蓝箭航天朱雀三号采用垂直回收方式，长征十号乙一子级回收也已见报道，但两者都属于一子级回收；而在载人飞船返回一侧，国内目前公开的还只是地面试验，例如穿越者称其全尺寸试验舱着陆缓冲综合试验中，触地冲击过载控制在 5g 以内。这意味着在排产、招标与标准对接上要按两条谱系分别布局：一子级可继续沿着复飞来降本，二级则需先完成热防护、黑障通信和着陆缓冲的工程闭环，并依靠真实载荷返回订单来验证，而不是再增加一次回收演示。文章提到穿越者已面向国内火箭企业启动常态化招标，并规划了未来 30 次商业载人发射的运载服务采购；这类跨公司的船箭接口协同能否落地，将直接决定二级回收在国内是停留在概念阶段，还是进入型号研制。

**「后续看点」** 后续可关注穿越者 CYZ1 亚轨道飞船的试验节点，以及其 30 次商业载人发射运载服务招标的中标结果；报道未给出时间表。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/space/2026/11/with-starship-catch-spacex-still-shows-it-can-dazzle-the-world/">With Starship catch , SpaceX still shows it can dazzle... - Ars Technica</a></li>
<li><a href="https://phys.org/news/2026-11-spacex-starship-spaceship.html">SpaceX Starship test to attempt first-ever spaceship &#x27; catch &#x27;</a></li>
<li><a href="https://www.youtube.com/watch?v=6egy0KSsK2s">SpaceX Starship Flight 15 | Launch &amp; Ship Catch - YouTube</a></li>
<li><a href="https://www.teslarati.com/spacex-catches-starship-first/">2026-11-15 — SpaceX 首次用发射塔接住从轨道返回的星舰</a></li>
<li><a href="https://news.qq.com/rain/a/20260819A034UC00">朱雀三号实现 一 子 级 着陆支腿方式 回 收 _腾讯新闻</a></li>
<li><a href="https://tele.ofweek.com/2026-07/ART-8320510-8420-30694176.html">长征十号乙 一 级 回 收 成功，对 中 国 商业 航 天 意味着什么？ - OFweek...</a></li>

</ul>
</details>

**标签**: `#Starship`, `#二级回收`, `#可重复使用火箭`, `#太空经济`, `#中国商业航天`

---

<a id="item-space-2"></a>
### [中国公布载人登月详细路线图：三次无人任务先行](https://www.nasaspaceflight.com/2026/11/china-roundup-2026-11/) ⭐️ 8.0/10

在 10 月 31 日开幕的第七届载人航天学术大会（北京）上，中国载人航天工程副总设计师、新合并的探月工程总设计师王翔给出了迄今最详细的载人登月任务排序：在首次载人登月尝试之前，先执行三次无人任务。第一步是 2027 年初用单芯级长征十号甲（CZ-10A）发射无人“梦舟”飞船前往天宫空间站，验证交会对接与再入返回（该任务已从 2026 年推迟）；第二步预计 2028 年用长征十号发射无人“揽月”着陆器，在月面演示着陆与上升；第三步预计 2029 年用两枚长征十号分别发射梦舟与揽月，进行全流程无人演练。此后，中国将不经载人先导飞行，直接实施首次登月：两名航天员在月面停留约三天、可能每天出舱活动，第三名留守梦舟，这与阿波罗 8 号、10 号或阿耳忒弥斯 2 号那样的载人预演不同。首次载人登月“2030 年前”的目标由中国载人航天工程办公室时任发言人林西强于 2023 年 5 月 29 日在酒泉宣布。

NASASpaceflight · 11月22日 22:31

**「已证实与未证实」** 已证实：据中国载人航天工程在第七届载人航天学术大会上的介绍，载人登月与嫦娥机器人探月已合并为单一“探月工程”，由王翔担任总设计师；他在会上给出了三次无人任务（2027 年初梦舟-1、约 2028 年无人揽月着陆、约 2029 年双箭全流程演练）的先后顺序，相关细节由《NASA 太空飞行》报道。
尚未证实：2027 年初、2028 年、2029 年均为报道所述“预计”时间，并非公布的确切发射日期；载人登月是否落在 2029 年、从而与中华人民共和国成立 80 周年重合，报道仅称“可能”；三次无人试验的实际硬件状态、长征十号与长征十号甲的首飞时间，均无官方时间表或独立验证。

**「背景」** 中国载人航天工程办公室于 2023 年 5 月 29 日在酒泉神舟十六号发射前发布会上首次公开载人登月计划，由时任新闻发言人林西强提出“2030 年前”实现首次中国人登月，方案为两名航天员在月面停留约六小时、第三名留在环月轨道。该方案依托嫦娥工程已积累的技术基础：2020 年嫦娥五号与 2024 年嫦娥六号已先后验证月面自主起飞和环月轨道交会对接。2026 年 5 月，中国载人航天工程办公室宣布将载人登月工程与机器人嫦娥工程合并为统一的“探月工程”，由载人航天工程副总设计师、新任探月工程总设计师王翔在 10 月 31 日开幕的第七届载人航天学术大会上介绍了此次细化的任务序列。

**「为什么重要」** 由于中国放弃载人先导飞行，这三次无人任务成为登月前必须全部通过的门槛，任何一次推迟都会直接压缩“2030 年前”的窗口；其中最直接的观察指标是 2027 年初的梦舟-1，它已从原定的 2026 年滑出，其长征十号甲火箭采用可重复使用一级、近地轨道运力 14 至 18 吨，首飞结果将同时检验火箭与飞船两条线。

**「后续看点」** 关注梦舟-1 在 2027 年初搭乘长征十号甲的首飞，以及约 2028 年无人揽月着陆器的月面着陆与上升试验能否按期进行。

**标签**: `#China crewed lunar program`, `#Mengzhou spacecraft`, `#Lanyue lander`, `#Tiangong space station`, `#lunar exploration`

---

## 科技产业与政策

<a id="item-tech-industry-1"></a>
### [美司法部寻求没收朝鲜关联黑客从币安窃取的逾 10 亿美元加密资产](https://www.techmeme.com/261123/p30#a261123p30) ⭐️ 8.0/10

美国司法部周一向法院提交没收申请，要求没收逾 10 亿美元加密货币，这批资产据称由与朝鲜有关联的黑客从币安（Binance Holdings Ltd.）窃取。彭博社查阅的法庭文件显示了这一消息，报道未说明被盗事件的具体时间、涉及哪一次入侵，也未说明相关资金是否已被控制。这是一起没收之诉的启动，而非法院裁定，文件本身不代表资产已被追回或所有权已判归美国政府。报道中未包含币安或司法部的公开回应。

Techmeme · 11月23日 17:25

**「已证实与未证实」** 已证实：据彭博社报道，美国司法部于周一提交法庭文件，寻求没收逾 1 亿美元——即超过 10 亿美元——据称由与朝鲜有关联的黑客从币安窃取的加密货币，依据是这份法院文件。
尚未证实：这批资金目前是否已被冻结或由美方实际控制、对应的是哪一次入侵及发生时间、“与朝鲜关联”的具体依据，均只见于彭博社对法庭文件的转述，报道未引用司法部公开声明，也无独立验证；资金数额的具体构成同样未作说明。

**「背景」** Forfeiture（资产没收）是美国司法部通过法院提起的民事程序，请求法官把追踪到的犯罪所得资产所有权收归政府；它是资产追缴，不是刑事定罪。此前 AI Daily Radar 11 月 15 日的日报曾报道，FBI 与司法部宣布打掉一个被命名为 FaceStealer 的朝鲜关联社交工程行动：该行动用 AI 深度伪造和虚假视频会议诱导受害者安装恶意软件，再窃取浏览器会话与 CI/CD（持续集成/交付）凭证，FBI 当时把约 4 亿美元被盗加密货币归因于该行动。这次申请针对的是从 Binance 窃取的逾 10 亿美元资产，属于美方围绕朝鲜关联黑客窃取交易所资金展开的执法链条的又一步；不过目前公开信息只表明司法部已提交申请，尚无法官裁定。

**「为什么重要」** 对交易所、场外交易商和合规团队而言，美国政府一旦对特定链上资金提起没收，任何经手这些资金的平台都可能面临资产被冻结或被卷入诉讼的风险，因此需要按文件所列资金流向做筛查；报道未说明这份文件是否公开了具体钱包地址，也就无法判断筛查范围有多大。

**「后续看点」** 接下来要看法院是否推进这项没收之诉并作出裁定，以及司法部是否自行发布声明或公布被追资金的链上地址。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/cyber-security/fbi-disrupts-north-korean-facestealer-campaign-behind-usd5-billion-binance-hack-doj-seizes-facestealer-cloud-infrastructure-containing-900-videos-of-tech-workers-hackers-used-ai-deepfakes-to-steal-usd400-million-and-compromise-open-source-software">2026-11-15 — FBI, DOJ seize FaceStealer cloud infrastructure tied to North Korean crypto theft</a></li>

</ul>
</details>

**标签**: `#North Korea`, `#cryptocurrency`, `#Binance`, `#DOJ`, `#cybercrime`

---

<a id="item-tech-industry-2"></a>
### [IBM 停止部分美国签证与绿卡担保，转而提供海外调动](https://restofworld.org/2026/ibm-consulting-ends-us-visa-green-card-sponsorship/?utm_source=rss&amp;utm_medium=rss&amp;utm_campaign=feeds) ⭐️ 7.0/10

据 Rest of World 报道，IBM 将停止为部分在美外籍员工办理工作签证和绿卡担保，同时向这些员工提供调往海外岗位的选项。报道称，若选择留下工作，员工可能需要移居他国并接受大幅降薪。IBM 于本月早些时候向员工说明了这一安排。报道未说明受影响员工人数、涉及的具体签证类别、可调往的国家以及降薪幅度。

Rest of World · 11月23日 11:00

**「已证实与未证实」** 已证实：IBM 表示将在其最大部门 IBM Consulting（逾 15 万名员工）的“多数”岗位停止美国签证与绿卡担保，受影响的外籍员工需在年底前转往海外岗位或离职；这一表述出自 IBM 的公开声明，并得到《印度时报》《HR Briefing》等报道的一致转述。

尚未证实：报道中的“大幅降薪”主要来自员工方面的说法，IBM 未公布薪资调整幅度；同样未披露的还包括受影响员工的具体人数、哪些岗位或技能属于例外、迁往哪些国家，以及海外用工的薪酬标准。

**「背景」** H-1B 是美国面向专业技术岗位的临时工作签证，绿卡则需由雇主代为申请；两者都要雇主出钱并走完整流程，所以“是否提供担保”长期是科技公司招聘外籍员工的关键条件。据 Indian Opinion 与 Nationwire 报道，IBM 此次停止担保的范围集中在其规模最大的部门 IBM Consulting——该部门全球员工超过 15 万人，报道并称这与特朗普政府收紧技术移民审查的背景有关。

**「为什么重要」** 对依靠雇主担保维持在美合法身份的员工而言，公司停止担保意味着一旦离职，就必须在有限时间内找到愿意接手担保的新雇主，否则需离开美国；而接受海外调动则可能面临收入下降。受影响者需要在身份与薪酬之间做出取舍。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bhaskarenglish.in/international/news/ibm-stops-us-h1b-visa-green-card-sponsorship-foreign-workers-139651501.html">IBM Stops H-1B Visa &amp; Green Card Sponsorship ; Foreign Workers...</a></li>
<li><a href="https://nationwire.us/ibm-ends-visa-green-card-sponsorship-consulting-roles/">IBM Ends Visa , Green Card Sponsorship for Consulting</a></li>
<li><a href="https://indianopinion.org/ibm-ends-h-1b-sponsorship-for-most-consulting-roles/">IBM ends H-1B, green card sponsorship for most... - Indian Opinion</a></li>
<li><a href="https://nationwire.us/ibm-ends-visa-green-card-sponsorship-consulting-roles/">IBM Ends Visa , Green Card Sponsorship for Consulting</a></li>
<li><a href="https://hrbriefing.com/articles/ibm-ends-visa-sponsorship-for-majority-of-roles-in-its-largest-unit">IBM Ends Visa Sponsorship for Most Consulting Roles — HR Briefing</a></li>
<li><a href="https://timesofindia.indiatimes.com/technology/tech-news/ibm-tells-visa-holders-in-its-150000-people-consulting-unit-to-move-abroad-or-leave-by-year-end-company-says-we-have-opted-to-discontinue-/articleshow/135726102.cms">IBM tells visa and Green card holders in its 150... - The Times of India</a></li>

</ul>
</details>

**标签**: `#IBM`, `#immigration policy`, `#visa sponsorship`, `#tech labor`, `#offshoring`

---

