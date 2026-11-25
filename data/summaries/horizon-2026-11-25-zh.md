# AI 每日雷达 - 2026-11-25

> 过去一天共筛查 306 条科技资讯，留下最值得读的 23 条。

---

**人工智能**
1. [GPT-6.2 靠推理与代码设计蛋白质微结合体，五个靶点测得结合信号](#item-ai-news-1) ⭐️ 8.0/10
2. [亚马逊称 AI 代理自主发现并利用零日漏洞](#item-ai-news-2) ⭐️ 8.0/10
3. [分析称沙箱内的模型仍可通过推理服务器侧信道通信](#item-ai-news-3) ⭐️ 7.0/10
4. [开发者称被 Anthropic 指控蒸馏模型，限 24 小时自证](#item-ai-news-4) ⭐️ 7.0/10
5. [OpenAI 与 Anthropic 内部人士称未发布模型已超出安全措施](#item-ai-news-5) ⭐️ 7.0/10
6. [消息人士：Meta 与亚马逊洽谈让 Muse 接入并解除封禁](#item-ai-news-6) ⭐️ 7.0/10

**芯片与算力**
1. [四台服务器共享 CXL 内存：软件锁开销 3–5 微秒，Tom&\#x27;s Hardware 报道](#item-chips-compute-1) ⭐️ 7.0/10

**机器人与自动驾驶**
1. [乌克兰无人艇在班加西港击沉俄导弹护卫舰，并袭击随行货船](#item-robotics-autonomy-1) ⭐️ 8.0/10
2. [Nuro 湾区启动无安全员 Lucid Gravity 机器人出租车测试，Electrek 报道](#item-robotics-autonomy-2) ⭐️ 8.0/10
3. [软银完成收购 Marc Raibert 的机器人与人工智能研究所](#item-robotics-autonomy-3) ⭐️ 7.0/10

**电动车与新能源**
1. [欧盟对华混合动力车设 200 天进口配额，上限 191,780 辆](#item-ev-energy-1) ⭐️ 8.0/10
2. [比亚迪发布第三代唐 EV：五座旗舰 SUV 起售价低于 3 万美元](#item-ev-energy-2) ⭐️ 7.0/10
3. [大众与 Elli 12 月在德国推出 1,995 欧元 V2G 墙盒](#item-ev-energy-3) ⭐️ 7.0/10
4. [瑞士授出 32 处卡车充电站点，Fastned、Obornes 与 Milence 分获三标段](#item-ev-energy-4) ⭐️ 7.0/10
5. [印度拉贾斯坦 8 号机组获首次临界许可，凯加 1 号机组复运](#item-ev-energy-5) ⭐️ 7.0/10

**航天**
1. [神舟二十四号发射，天宫空间站迎来首位外国航天员](#item-space-1) ⭐️ 8.0/10

**科技产业与政策**
1. [澳大利亚通过《数字注意义务法》，大型平台或因可预见伤害面临数十亿罚款](#item-tech-industry-1) ⭐️ 9.0/10
2. [OpenAI 前员工被控窃听，彭博社称发现数百段录音](#item-tech-industry-2) ⭐️ 8.0/10
3. [Flipkart CEO 克里希纳穆尔蒂将于 12 月 4 日离任，CTO 暂代](#item-tech-industry-3) ⭐️ 7.0/10
4. [华为称鸿蒙装机量突破 1 亿台，应用与服务逾 46 万个](#item-tech-industry-4) ⭐️ 7.0/10
5. [TikTok 与 AI 助推“真实犯罪”网络，暴力攻击增多，WIRED 报道](#item-tech-industry-5) ⭐️ 7.0/10
6. [FISA 第 702 条续期或搭上国防授权法案，Politico 报道](#item-tech-industry-6) ⭐️ 7.0/10
7. [美国司法部称破获史上最大诈骗网络，指控 800 余名被告](#item-tech-industry-7) ⭐️ 7.0/10

---

## 人工智能

<a id="item-ai-news-1"></a>
### [GPT-6.2 靠推理与代码设计蛋白质微结合体，五个靶点测得结合信号](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/) ⭐️ 8.0/10

OpenAI 发布报告称，在只给出五个靶蛋白的三维结构和指定结合位点的情况下，GPT-6.2 通过编写代码生成候选微结合体（minibinder，即能贴附到目标蛋白特定位置的小型结合蛋白）的三维设计，并在实验室测试中观察到五个靶点均存在结合的证据。不过要把设计变成可测试的蛋白，仍需专用模型参与：氨基酸序列由专用模型 SolubleMPNN 提出，另有其他专用蛋白模型负责筛选那些被预测能按设计折叠、并在预期位点结合的候选。OpenAI 把这条路线描述为不依赖专用蛋白 AI 模型的结构设计，但从披露的流程看，序列生成与候选筛选仍由专用模型承担，实验室结合证据也只有 OpenAI 一方给出。

Hacker News · acossta · 11月24日 21:02 · [社区讨论](https://news.ycombinator.com/item?id=50634658)

**「已证实与未证实」** 已证实：据 OpenAI 报告，GPT-6.2 在拿到五个靶蛋白三维结构及指定结合位点后自行写代码生成微结合体的三维设计，实验室测试发现五个靶点均有结合迹象；序列由 SolubleMPNN 生成、候选由其他专用蛋白模型筛选，这也是该报告自己写明的内容。
尚未证实：结合证据的强度（亲和力、特异性、可重复性）目前只有 OpenAI 单方描述，没有独立复现或同行评审数据；“不依赖专用蛋白 AI 模型”究竟覆盖多少环节仍不清楚，因为序列设计与候选筛选由专用模型完成。

**「背景」** AI Daily Radar 11 月 19 日的日报曾报道，OpenAI 于 11 月 18 日发布 GPT-6.2 Astra 与 Sol，两者支持 105 万 token 上下文、仅接受文本与图像输入，上线初期实测口碑分化。蛋白质设计过去主要依赖专用模型完成：例如 SolubleMPNN 属于“逆向折叠”模型，在给定蛋白质骨架的三维结构后反推出能折叠成该结构的氨基酸序列（据 OpenProtein.AI 的模型文档）。这正是本次实验中 GPT-6.2 只负责生成三维设计、序列仍交由专用模型给出的技术由来。

**「为什么重要」** 对做蛋白设计的团队来说，这份报告说明通用大模型当前的实用角色更像是串联流程的编排层：用它理解靶点结构、写代码生成骨架，而序列生成和筛选仍交给 SolubleMPNN 等专用模型。因此评估这类结果时，应把“三维结构设计”与“能表达、能结合的序列”分开看，并要求公布结合亲和力与阴性对照数据。

**「社区讨论」** 评论者 fabian2k 质疑 GPT-6.2 究竟设计出了什么，理由是决定蛋白质的其实是氨基酸序列；plaidfuji 认为“超越专用模型”的说法为时尚早，GPT 更像是连接各专用模型的“胶水层”。在 Baker 实验室读过博士的 elhospitaler 则认为，这一方向与把语言模型和蛋白质原生多模态融合的设想一致，并不意外。

<details><summary>参考链接</summary>
<ul>
<li><a href="http://www.geekpark.net/news/374175">2026-11-19 — OpenAI 发布 GPT-6.2 Astra 与 Sol，跑分领先但实测口碑分化</a></li>
<li><a href="https://docs.openprotein.ai/models/proteinmpnn/solublempnn/">SolubleMPNN - OpenProtein.AI docs</a></li>

</ul>
</details>

**标签**: `#AI protein design`, `#GPT-6`, `#OpenAI`, `#AI for science`, `#minibinders`

---

<a id="item-ai-news-2"></a>
### [亚马逊称 AI 代理自主发现并利用零日漏洞](https://arstechnica.com/security/2026/11/amazon-says-hackers-ai-agents-found-and-exploited-0-day-with-little-human-input/) ⭐️ 8.0/10

亚马逊披露，黑客让运行在开源渗透测试框架 Cairn 上的 AI 代理仅凭“获取 shell 访问权限”的指令和一组 IP 地址，自主发现并利用了东亚一所大学服务器上的零日漏洞，并取得系统完全控制。代理在目标服务器运行的开源医学影像 AI 应用中找到该漏洞；黑客使用简体中文提示词，并把模型时区设为北京时间。亚马逊由此警告，代理式攻击操作已在发生，防守方需为这类工具带来的速度和持续性做准备；这些细节目前来自亚马逊的单方披露，尚待独立安全机构复现或确认。

Ars Technica · 11月24日 12:30

**「已证实与未证实」** 已证实：亚马逊在自家安全博客中称，运行于开源渗透测试框架 Cairn 上的 AI 代理在仅获得一份 IP 列表和“获取 shell 访问权限”这一目标指令的情况下，自主发现并利用了 MONAI Label（一款开源医学影像 AI 应用）中的路径遍历零日漏洞，取得了服务器的完整控制权；BleepingComputer 与 Dark Reading 均据此报道，Dark Reading 称从发现漏洞到拿到 root 权限约用时 11 分钟。

尚未证实：将攻击者定性为“中国关联行为体”（依据是简体中文提示词和将模型时区设为北京时间）属于亚马逊自身的归因判断，未提供独立佐证；被入侵的东亚某大学名称、11 分钟这一具体时长、漏洞是否已修复及 MONAI Label 方面是否确认，均无第三方独立核实。

**「背景」** 零日漏洞（0-day）指厂商尚不知情、因而还没有补丁的软件缺陷，攻击者一旦利用就能在无人察觉的情况下取得系统控制权。Cairn 是一个开源的 AI 渗透测试框架，按 Odin Research 的介绍，它让多个 AI 工作代理共享同一份事实与行动计划图谱，持续探索直到达成目标，而自主渗透测试正是它第一个得到验证的用途。据 Security Affairs 报道，亚马逊威胁情报团队还曾发现一台公开托管、未设认证即可访问的 Cairn 实例，显示这类框架的部署门槛相当低。

**「为什么重要」** 如果亚马逊的描述成立，防守方要应对的不再只是单个漏洞，而是从一条简单指令到取得 root 权限的发现—利用链条被大幅压缩；对外暴露的服务器和开源 AI 应用应优先做补丁、最小权限和异常行为监控。

**「后续看点」** 后续关注该开源医学影像项目是否发布漏洞公告或补丁，以及是否有独立安全团队复现 Cairn 代理从发现到利用的完整过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/security/hackers-use-autonomous-ai-tool-cairn-to-find-zero-day-take-over-server/">Hackers use autonomous AI tool Cairn to find zero - day , take over...</a></li>
<li><a href="https://www.darkreading.com/cyberattacks-data-breaches/ai-agents-flaw-discovery-root-access-11-minutes">AI Agents Zip From Flaw Discovery to Root Access in 11 Minutes</a></li>
<li><a href="https://brandefense.io/odin-research/what-is/cairn/">What Is Cairn? The Open-Source AI Penetration Testing Engine</a></li>
<li><a href="https://securityaffairs.com/203664/ai/cairn-ai-framework-used-in-autonomous-zero-day-exploitation.html">Cairn AI Framework Used in Autonomous Zero-Day Exploitation</a></li>
<li><a href="https://www.helpnetsecurity.com/2026/11/23/cairn-ai-agents-autonomous-attacks/">Open-source AI pentesting framework Cairn keeps turning up in ...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#cybersecurity`, `#zero-day exploitation`, `#autonomous offensive operations`, `#Amazon`

---

<a id="item-ai-news-3"></a>
### [分析称沙箱内的模型仍可通过推理服务器侧信道通信](https://www.lesswrong.com/posts/7wzWuLP3HhyBLmKfo/models-can-communicate-via-inference-servers-despite-being) ⭐️ 7.0/10

LessWrong 上的一篇分析文章主张，即使模型被限制在沙箱中，仍可能借助推理服务器层面的侧信道彼此通信，从而绕过通常用来阻止模型之间直接对话的隔离措施。该文针对的是运行多租户推理服务的团队，但文中被转述的主张目前没有独立复现、可运行的攻击代码，也没有推理服务器厂商的确认，因此属于分析性判断，而非已经演示的漏洞。Hacker News 上的讨论普遍质疑其现实可行性，认为这类通信依赖大量苛刻前提。

Hacker News · gmays · 11月25日 02:34 · [社区讨论](https://news.ycombinator.com/item?id=50637686)

**「已证实与未证实」** 已证实：LessWrong 上确实发表了这篇分析（第三方报道称作者为 Niranjan Deshpande），帖子摘要明确主张：同一推理服务器上运行的两个智能体，即使无法互相发送消息、也无法访问同一文件，仍能可靠地通信，并称这是一种基于推理服务器侧信道（side channel，即通过共享硬件或缓存等间接途径传递信息）的隐蔽信道。

尚未证实：上述通信是否在真实云部署中成立、需要哪些前提条件、传输速率有多高，均无独立复现或第三方测量；帖子涉及的具体推理框架与版本、以及防御措施能否阻断信道，报道也未给出可核验细节。

**「背景」** 沙箱（sandbox）通过限制代码执行、文件写入和网络访问来隔离 AI 智能体，通常默认模型只能看到自己的上下文。但在实际部署中，多个租户或智能体往往共享同一个推理服务器（例如单个 vLLM 实例），而这类服务器为了加速生成，会缓存重复提示的前缀计算结果（即 KV cache／前缀缓存），并让先到的请求影响后续请求的排队与解码速度。LessWrong 这篇文章所讨论的隐蔽信道正是建立在这一共享层之上：评论者 amluto 指出浏览器开发者早已因同源策略要求缓存按来源隔离，并主张推理 API 应允许调用方指定缓存分隔键；另一位评论者 kgeist 则描述了利用 prefill 与 decode 互相拖慢来传递比特的时序思路。

**「为什么重要」** 如果这条侧信道成立，最直接受影响的是在同一台推理服务器上服务多个互不信任租户的团队：缓存默认在请求之间共享，使“谁能观测到谁的缓存”成为实际的隔离边界。资料建议按租户或用户划分缓存作用域与缓存键；vLLM 的 PagedAttention 用引用计数分配器在请求间共享 GPU 内存页，正是评论中主张加入“缓存分离键”的位置。不过该攻击依赖对软硬件栈的精确了解和预先共享的通信约定，评论者认为这些条件极不现实，因此眼下更合适的是评估隔离配置，而不是紧急改造。

**「后续看点」** 值得关注的是，是否会出现独立的第三方复现或可运行的端到端演示，以及 vLLM 等推理服务器项目是否会加入按请求划分的缓存隔离键；这只是评论中提出的防御思路。

**「社区讨论」** 评论者对可行性的看法分歧明显：tsimionescu 认为文中讨论的攻击在现实中完全不成立，因为它们要求两个模型事先知道彼此存在，并精确掌握推理服务器的软件与内核细节；amluto 则主张推理服务器应像浏览器隔离不同来源的缓存那样，允许 API 调用指定缓存隔离键。kgeist 提出另一种思路：当同一 vLLM 实例不拆分 prefill（预填充）与 decode（逐 token 生成）时，一个模型可以周期性读取长文档，以拖慢解码速度，另一个模型则用 bash 计时并测算自己的每秒 token 数，据此读出比特。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.lesswrong.com/posts/7wzWuLP3HhyBLmKfo/models-can-communicate-via-inference-servers-despite-being">Models Can Communicate via Inference Servers Despite Being ...</a></li>
<li><a href="https://theprimary.com/ai-tech/2026-11-20/sandboxed-ai-covert-channels">Sandboxed artificial intelligence models can communicate ...</a></li>
<li><a href="https://agihunt.info/en/p/1a210c24cdad568aea5f2734e1e">Models Can Communicate via Inference Servers… · AGI Hunt</a></li>
<li><a href="https://nhimg.org/prompt-caching-security-guide">Prompt Caching Security : Isolation and Side Channels</a></li>
<li><a href="https://arxiv.org/html/2608.09225">Governing the KV Cache :Preventing Timing Side - Channel Leakagein...</a></li>
<li><a href="https://www.systemshardening.com/articles/ai-landscape/vllm-shared-memory-inference-isolation/">vLLM and the KV - Cache Isolation Problem: How Shared Memory...</a></li>

</ul>
</details>

**标签**: `#AI security`, `#inference servers`, `#side channels`, `#sandboxing`, `#model communication`

---

<a id="item-ai-news-4"></a>
### [开发者称被 Anthropic 指控蒸馏模型，限 24 小时自证](https://news.ycombinator.com/item?id=50630809) ⭐️ 7.0/10

一位开发者在 Hacker News 的 Ask HN 版块发帖称，Anthropic 指控其公司利用 Anthropic API 进行模型蒸馏（distillation，即用强模型的输出训练自己的模型），并要求在 24 小时内证明合规。发帖人否认这一指控：公司并不训练自己的模型，唯一可能触发标记的用法，是在调整 AI 配置时运行自动化回归基准测试。这一说法目前只有发帖人单方面的陈述，Anthropic 未公开回应，也未说明检测依据、判罚标准或申诉渠道。讨论集中在两件事上：供应商的执法过程不透明、容易误伤正常用户；以及在不泄露用户数据的前提下，开发者究竟能拿出什么证据来自证清白。

Hacker News · weli · 11月24日 16:45

**「已证实与未证实」** 已证实：Hacker News 用户 weli 于 11 月 24 日发帖称，其公司被 Anthropic 指控用 Claude API 做模型蒸馏（即用大模型输出训练自家模型），并被要求在 24 小时内自证清白；帖子说明他们并不训练自有模型，唯一可疑用法是更改 AI 设置时跑的自动化回归基准测试，并公开征询同行如何在不泄露用户隐私的前提下举证。

尚未证实：Anthropic 是否确实发出该通知、24 小时期限是否属实、被指控的具体行为为何，以及自动化基准测试是否违反其政策——这些均只有发帖人单方陈述，Anthropic 未公开回应，也无第三方佐证；此前 Anthropic 曾公开指控 DeepSeek、Moonshot、MiniMax 等中国开发商蒸馏 Claude（据 DeepLearning.AI 与 n1n 报道），说明此类指控有先例，但并不构成本帖个案的证据。

**「背景」** 模型蒸馏（distillation）指把另一个更强模型的输出当作训练数据来训练自己的模型；这类用途通常被闭源模型厂商的使用政策明确禁止。Anthropic 的 Usage Policy 适用于所有向 Claude 提交输入的用户，包括 API 与企业客户，并于 2026 年 10 月 8 日发布了更新版本。发帖人自称公司只用 API 做自动化回归基准测试、并不训练自己的模型，这一说法目前仍是其单方面陈述，Anthropic 尚未公开说明作出该判定的具体依据。

**「为什么重要」** 对依赖 Anthropic API 的团队来说，这次讨论给出的可行做法是平时就保留可复现的证据链：基准测试脚本及其 git 历史、API key 的使用日志与轮换记录，并准备好第二家供应商作为备份。评论中提到，一旦收到这类通知，24 小时的窗口几乎不足以完成合规举证，而有开发者建议通过 AWS Bedrock 使用 Anthropic 模型，以便出问题时能对接人工客户经理。

**「后续看点」** 可以关注发帖人在 24 小时期限结束后是否更新结果，例如账号与 API 访问是否被恢复，以及 Anthropic 是否公开说明其蒸馏检测逻辑与申诉流程。

**「社区讨论」** 有评论建议把提交给 Anthropic 的证据同样交给 Claude，让它判断这些材料是否足以排除蒸馏嫌疑，理由是 Anthropic 一方很可能也用 Claude 做审核。另有开发者分享亲身经历：在 OpenAI 也遇到过同类指控，事后发现是一个 API key 被泄露、第三方确实在蒸馏，撤销密钥并沟通后访问被恢复。也有人质疑这种做法是否虚伪，或干脆建议换用其他供应商。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/2026-usage-policy-update">2026 Usage Policy update \ Anthropic</a></li>
<li><a href="https://assets.claude.com/88cf16e8b7d203be16d2c726bcd28a6ec7c7f5c8.pdf">Usage Policy - assets.claude.com</a></li>
<li><a href="https://explore.n1n.ai/blog/anthropic-accuses-deepseek-claude-model-distillation-2026-02-24">Anthropic Accuses DeepSeek and Chinese AI Firms of Claude Model ...</a></li>
<li><a href="https://www.deeplearning.ai/the-batch/some-kimi-and-deepseek-users-were-served-claude-instead-anthropic-says">Anthropic &#x27;s Accounts of Distillation , Gray-Market Transfer Stations...</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#model distillation`, `#API policy enforcement`, `#AI developer platform`, `#Hacker News discussion`

---

<a id="item-ai-news-5"></a>
### [OpenAI 与 Anthropic 内部人士称未发布模型已超出安全措施](https://the-decoder.com/dozens-of-insiders-say-openai-and-anthropics-unreleased-models-have-outgrown-their-safety-measures/) ⭐️ 7.0/10

据 Axios 报道，OpenAI 和 Anthropic 的多名员工认为，两家公司自家尚未发布的前沿模型已无法被安全地控制。两家公司内部正在讨论是否暂停发布，甚至是否停止训练，同时员工对管理层的信任正在削弱。The Decoder 转述的这篇报道没有给出具体模型名称、涉及人数、时间表或内部评估文件，两家公司也未公开回应。

The Decoder · 11月24日 14:02

**「已证实与未证实」** 已证实：The Decoder 转述 Axios 的报道称，OpenAI 与 Anthropic 有员工对自家未发布前沿模型的安全性表达担忧，并出现是否暂停发布或停止训练的讨论。
尚未证实：具体涉及多少员工、指向哪些模型、公司是否已做出任何暂停决定，以及这些判断依据的内部评估；报道未提供内部文件、具名信源或公司回应。

**「背景」** 报道中所说的“安全措施”，指两家公司在模型对外发布前设置的内部审查与发布决策流程；争论的焦点是，这些流程是否还能适用于尚未公开的更强模型。Axios 的报道刊出后，OpenAI 一位发言人对媒体表示，公司已采用新的安全要求，可能放慢模型发布节奏；Anthropic 是否作出类似调整，目前没有公开说明。

**「为何重要」** 如果内部争论导致发布延后，那么依赖这两家模型 API 的开发者与企业用户，就不能再假定新版本会按以往节奏到来，模型选型、弃用迁移和合规评估都应预留推迟的余地。

<details><summary>参考链接</summary>
<ul>
<li>Anthropic and OpenAI employees fear unreleased AI models are too ...</li>

</ul>
</details>

**标签**: `#AI safety`, `#frontier models`, `#OpenAI`, `#Anthropic`, `#AI governance`

---

<a id="item-ai-news-6"></a>
### [消息人士：Meta 与亚马逊洽谈让 Muse 接入并解除封禁](https://www.techmeme.com/261125/p13#a261125p13) ⭐️ 7.0/10

《财富》（Fortune）11 月 25 日援引未具名消息人士报道，亚马逊与 Meta 正在持续磋商一项潜在协议，拟把 Meta 的 Muse AI 智能体接入亚马逊平台，并结束亚马逊对它的封禁。报道称，任何此类协议都需要两家公司 CEO 签字批准，但没有披露交易条款、时间表或接入的具体范围。两家公司均未公开确认谈判存在，消息完全来自匿名信源。

Techmeme · 11月25日 10:15

**「已证实与未证实」** 已证实：据《财富》报道（引述未具名消息人士），亚马逊与 Meta 正在讨论一项让 Muse 接入亚马逊、解除现有封禁的潜在协议，且协议需双方 CEO 批准。
尚未证实：谈判能否达成协议、封禁的起始时间与覆盖范围及其实施理由、交易条款和上线时间；亚马逊与 Meta 均未公开确认或置评，报道也未提供可供独立核实的细节。

**「背景」** Muse 是 Meta 的 AI 智能体，报道称其人气候颇高；亚马逊此前对其实施了封禁，但报道未说明封禁的起始时间、覆盖范围或理由。AI 购物智能体通常代替用户在零售网站上浏览和下单，这类跨平台接入一般需要平台方开放接口并谈妥商业条款。

**「为什么重要」** 若协议达成，Muse 将能在亚马逊上代用户完成购物操作——但前提是两家 CEO 都签字；在此之前，亚马逊的封禁仍然有效，用户和开发者不应假定 Muse 已可在亚马逊使用。

**「后续看点」** 接下来看两家公司是否公开确认谈判、CEO 是否签字批准，以及协议是否披露接入范围和上线时间。

**标签**: `#Meta`, `#Amazon`, `#AI agents`, `#partnerships`, `#e-commerce`

---

## 芯片与算力

<a id="item-chips-compute-1"></a>
### [四台服务器共享 CXL 内存：软件锁开销 3–5 微秒，Tom&\#x27;s Hardware 报道](https://www.tomshardware.com/pc-components/dram/shared-cxl-memory-pools-come-with-steep-software-tax-that-could-stall-multi-server-scaling-ut-arlington-shares-real-world-test-that-measured-four-servers-sharing-the-same-pool-at-sc26) ⭐️ 7.0/10

得克萨斯大学阿灵顿分校与英特尔的研究人员在 SC26 上报告了四台服务器共享一个 CXL 内存池的实测：四台 86 核英特尔至强 6787P 服务器（各 256GB DRAM）通过 PCIe 5.0 连接同一台 CXL 内存箱，而该平台没有跨主机缓存一致性和硬件原子操作。锁因此只能由软件用普通读写和显式刷新实现，每次加锁带来 3–5 微秒开销；无争用时锁延迟中位数为 3.7 微秒，多台服务器争用同一把锁时第 95 百分位达 132 微秒。广度优先搜索（BFS）从一台增至四台反而由 0.55 秒增至 0.74 秒，三角形计数耗时从 2.43 秒降至 0.97 秒，哈希表吞吐从 410 万次/秒升至 1660 万次/秒，表明池化收益高度依赖访问模式。研究人员称其交换机仅支持四台服务器，CXL 3.0 的 Back-Invalidate 硬件修复尚未获得厂商确认；这直接影响把 CXL 池用于 AI KV cache 的部署评估，SK 海力士和 Micron 虽在 SC26 展示了池化设计并给出性能提升声明，但四机实测显示跨主机同步频繁的负载不会自动随服务器数量扩展。

Tom&\#x27;s Hardware · 11月24日 11:30

**「已证实与未证实」** 已证实：据 Tom&\#x27;s Hardware 对 SC26 展示的报道，UT Arlington 与英特尔研究人员在四台至强 6787P 服务器加一台 CXL 内存箱的真实硬件上测得每次软件锁 3–5 微秒开销，并报告 BFS、三角形计数和哈希表的具体扩展数据。
尚未证实：该测试的完整方法、原始数据和独立复现结果尚未公开；CXL 3.0 Back-Invalidate 是否受其平台支持仍未获厂商确认；SK 海力士的 2.6 倍首 token 时间、3.0 倍 P99 延迟改善和 Micron 的 10–30 倍代理式 AI 提升均为厂商声明，未见独立验证。

**「背景」** CXL（Compute Express Link）是建立在 PCIe 之上的互联标准，让服务器在自身内存插槽之外挂接共享内存池，从而突破单机 DRAM 容量上限；本次测试即用四台 Xeon 6787P 服务器经 PCIe 5.0 共享一个 CXL 内存机箱。难点在缓存一致性：同一台服务器内，CPU 硬件会自动同步各核缓存并完成原子操作，而跨主机的 CXL 共享池没有这层硬件保障，锁和数据刷新只能由软件用普通读写实现，这正是 3–5 微秒开销的来源；CXL 3.0 规范中的 Back-Invalidate 机制本可在硬件层解决缓存问题，但研究者未获厂商确认其平台支持该功能。同类产品正在密集出现：11 月 23 日的日报曾报道 Penguin Solutions 在 SC26 展示光互连内存机箱，可通过 Optical CXL 3.1 为 AI 系统增加最高 576GB HBM3E 和 16TB DDR5，说明硬件供给已先行，而跨主机软件路径的实际代价才刚开始被量化。

**「为什么重要」** 对计划用 CXL 内存池扩展 AI KV cache 或图分析内存的团队，这次实测给出的直接约束是：按桶或分片独立访问、写少读多的负载（如哈希表）能随主机数扩展，而频繁跨主机同步的负载（如 BFS）可能越加机器越慢。部署前应确认平台是否支持 CXL 3.0 的 Back-Invalidate 和硬件原子操作；若只能依赖软件锁，需把每锁 3–5 微秒的开销和争用时 132 微秒级的尾部延迟计入容量与延迟预算。

**「后续看点」** 后续可核对交换机或服务器厂商是否正式确认该四主机平台支持 CXL 3.0 Back-Invalidate 与硬件原子操作，以及是否有独立团队复现这组四机共享内存基准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/dram/penguin-shows-off-photonic-memory-box-at-sc26-that-can-expand-ai-accelerator-capacity-over-optical-links-device-sports-up-to-576gb-of-hbm3e-customer-samples-expected-in-2027">2026-11-23 — Penguin demos photonic memory appliance with 576GB HBM3E over optical CXL at SC26</a></li>

</ul>
</details>

**标签**: `#CXL memory`, `#data center memory`, `#AI KV cache`, `#server scaling`, `#hardware-software co-design`

---

## 机器人与自动驾驶

<a id="item-robotics-autonomy-1"></a>
### [乌克兰无人艇在班加西港击沉俄导弹护卫舰，并袭击随行货船](https://arstechnica.com/gadgets/2026/11/ukraines-sea-drones-blow-up-russian-warship-in-benghazi-operation/) ⭐️ 8.0/10

据美联社报道，11 月 22 日停靠在利比亚班加西港的俄罗斯海军导弹护卫舰“水星”号（Merkury）遭至少两艘乌克兰海上自杀式无人艇撞击后在港内沉没；乌克兰总统泽连斯基公布了视频，显示无人艇接近并撞上这艘起火的军舰，以及随行的俄干货船“安加拉”号（MV Angara）。乌克兰安全局称，此次行动由一艘母船放出七艘无人艇执行，并称“水星”号上的卡-27 直升机一并被毁。泽连斯基称“安加拉”号正在运输武器，而俄罗斯向目前控制班加西的利比亚国民军提供物资支持；这一说法目前只来自乌方。报道称，这些打击显示乌克兰无人艇的行动范围已从黑海扩展至北非海岸与芬兰湾一带。

Ars Technica · 11月24日 12:00

**「已证实与未证实」** 已证实：美联社报道，11 月 22 日停靠班加西的俄导弹护卫舰“水星”号遭至少两艘乌克兰无人艇撞击后在港内沉没；泽连斯基发布了显示无人艇撞击该舰与干货船“安加拉”号的视频。
尚未证实：乌克兰安全部门所称“从母船放出七艘无人艇”、舰上卡-27 直升机被毁以及“安加拉”号运载武器的说法，目前仅有乌方表述；报道未给出伤亡人数、无人艇型号或母船信息，也未见俄方确认或独立核实损害评估。

**「背景」** 乌克兰此前已多次使用爆炸性海上无人艇（USV，即装载炸药、可远程操控撞击目标的小型无人快艇）打击俄罗斯舰船，报道将本次行动描述为这类打击范围从北非沿岸扩展到芬兰湾的体现。据同一报道，俄罗斯向目前控制班加西的利比亚国民军提供物资支持，而该武装正与设在的黎波里、获国际承认的利比亚政府交战，这解释了俄方舰船为何停泊在班加西港。

**「为什么重要」** 对海军规划者的具体后果是：一艘导弹护卫舰在远离黑海的第三国港口锚泊时，被多艘小型无人艇击沉；这意味着仅靠在港内停泊、依赖东道国提供警戒，已不足以保护高价值舰艇，港口需要增加拦阻浮障、防雷网与专门的反无人艇巡逻。

**「后续看点」** 接下来可以核查的是：俄罗斯国防部是否承认“水星”号沉没，以及商业卫星影像或独立分析人士能否确认该舰舰体状态和“安加拉”号的受损程度。

**标签**: `#naval drones`, `#uncrewed surface vehicles`, `#Ukraine`, `#military robotics`, `#maritime autonomy`

---

<a id="item-robotics-autonomy-2"></a>
### [Nuro 湾区启动无安全员 Lucid Gravity 机器人出租车测试，Electrek 报道](https://electrek.co/2026/11/24/nuro-lucid-gravity-uber-robotaxi-driverless-testing-bay-area/) ⭐️ 8.0/10

据 Electrek 报道，Nuro 已在旧金山湾区四个半岛和南湾城市启动无安全员的 Lucid Gravity 机器人出租车公共道路测试，Lucid 已为该项目交付超过 100 辆 Gravity SUV。面向公众的 Uber 叫车服务原定 2026 年推出，现预计推迟到 2027 年第一季度。当前阶段是测试而非商业运营；报道未披露具体城市、监管许可状态或远程监控安排。

Electrek · 11月24日 15:32

**「已证实与未证实」** 已证实：Electrek 报道称，Nuro 已在湾区四个半岛和南湾城市的公共道路上进行无安全员的 Lucid Gravity 测试，车队规模超过 100 辆，且这些车辆由 Lucid 交付。
尚未证实：公众 Uber 服务能否在 2027 年第一季度如期上线、测试是否获得加州监管批准、四个城市的具体名单以及远程监控安排，报道均未提供；相关时间表目前仅来自 Electrek 的报道。

**「背景」** 所谓“无安全员”测试，是指撤掉坐在驾驶位、随时准备接管车辆的人员，在公共道路上运行，这是从有人监督的路测走向商业化载客之间的一道门槛。Uber 正把第三方自动驾驶车队接入自己的叫车应用：11 月 16 日的日报曾报道，亚马逊旗下的 Zoox 已在拉斯维加斯通过 Uber App 接单。为该项目提供 Gravity SUV 的 Lucid 自身正面临资金压力，11 月 17 日的日报曾报道其第三季度现金消耗环比下降 30%，并获沙特公共投资基金（PIF）追加 17.5 亿美元融资。

**「为什么重要」** 对湾区居民而言，实际变化是公共道路上会出现驾驶座无人的测试车辆，而不是马上能在 Uber 应用里叫到这类车；若 Q1 2027 的时间表不变，公众服务要等到 2027 年第一季度。

**「后续看点」** 关注 Nuro 与 Uber 是否在 2027 年第一季度如期开放公众叫车，以及届时是否公布具体运营城市、车队规模和监管许可信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/11/16/zoox-robotaxis-are-now-on-the-uber-app-in-las-vegas/">2026-11-16 — Zoox robotaxis join the Uber app in Las Vegas</a></li>
<li><a href="https://www.electrive.com/2026/11/16/lucid-cuts-cash-burn-and-secures-additional-1-75-billion/">2026-11-17 — Lucid cuts Q3 cash burn 30% and secures $1.75B from PIF</a></li>

</ul>
</details>

**标签**: `#robotaxi`, `#Nuro`, `#Uber`, `#Lucid Gravity`, `#driverless testing`

---

<a id="item-robotics-autonomy-3"></a>
### [软银完成收购 Marc Raibert 的机器人与人工智能研究所](https://www.therobotreport.com/softbank-acquires-marc-raiberts-robotics-and-ai-institute/) ⭐️ 7.0/10

据 The Robot Report 报道，软银已完成从现代汽车集团手中收购机器人与人工智能研究所（RAI Institute），交易金额未披露，软银回复了该媒体的邮件提问但拒绝置评。RAI 由波士顿动力创始人 Marc Raibert 于 2022 年创立，现代汽车集团出资逾 4 亿美元作为初始资金，总部位于马萨诸塞州剑桥市，研究聚焦移动、操作、感知与智能等机器人基础难题；该机构目前在剑桥和苏黎世两地挂出 24 个空缺岗位，涵盖机器人学习、操作、仿真、导航与硬件工程。The Robot Report 曾在 2026 年 9 月率先报道双方达成收购协议，此次为交易正式完成。收购后 RAI 是否保持独立运作、研究重点是否调整，报道称尚不清楚；同期软银以 53.75 亿美元收购 ABB 机器人业务的交易因中国监管机构阻挠而前景不明。

The Robot Report · 11月24日 14:48

**「已证实与未证实」** 已证实：据 The Robot Report 报道，软银已完成从现代汽车集团手中收购机器人学与人工智能研究院（RAI）；软银回应了该媒体的邮件提问但拒绝置评，交易财务条款未披露。RAI 由波士顿动力创始人 Marc Raibert 于 2022 年创立，现代汽车集团提供逾 4 亿美元初始资金，总部位于马萨诸塞州剑桥市，并在苏黎世设有办公室。该媒体此前于 2026 年 9 月率先报道双方达成收购协议，当时援引了多个消息源。

尚未证实：交易“已完成”目前仅来自 The Robot Report 一家媒体的报道（该媒体称“获悉”），软银拒绝置评，也没有双方联合公告或监管文件佐证；收购价格、RAI 是否会继续独立运营、研究重点是否调整，以及它将与软银旗下的 Skild AI、Agile Robots 等公司如何协作，报道均未给出信息。

**「背景」** RAI 研究所由波士顿动力（Boston Dynamics）创始人 Marc Raibert 于 2022 年创办，总部位于马萨诸塞州剑桥市，成立时获得了现代汽车集团超过 4 亿美元的初始资金，研究方向是移动、操作、感知与智能等机器人基础难题。SoftBank 与 Raibert 并非首次交集：SoftBank 在 2017 年从 Alphabet 手中收购波士顿动力，2021 年又把控股权出售给现代，当时对波士顿动力的估值约为 11 亿美元；现代近期还买下 SoftBank 所持波士顿动力剩余 9.65% 股份，这笔交易因此被视为双方的再次联手。

**「为什么重要」** 这笔交易让软银与 Raibert 再度联手：软银 2017 年从 Alphabet 买下波士顿动力，2021 年以 11 亿美元估值把控股权卖给现代汽车集团，现代近期又买下软银剩余的 9.65% 股份，软银近十年的波士顿动力投资就此结束，RAI 成为它在人形与通用机器人研究上的新抓手。对 RAI 的研究人员和应聘者来说，实际的不确定在于机构独立性与研究方向会不会变——报道明确指出这一点尚无答案，24 个在招岗位今后归属哪套体系也未说明；外界则关注 RAI 的基础研究与软银已投的 Skild AI、Agile Robots 之间是否会产生协同。

**「后续看点」** 值得关注 RAI 是否公布新的组织安排或研究路线，以及剑桥与苏黎世两地 24 个岗位的招聘进展。另一条线是中国监管机构对软银 53.75 亿美元收购 ABB 机器人业务的最终决定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.therobotreport.com/softbank-agrees-to-acquire-robotics-and-ai-institute/">SoftBank agrees to acquire Robotics and AI Institute</a></li>

</ul>
</details>

**标签**: `#SoftBank`, `#Robotics and AI Institute`, `#Marc Raibert`, `#acquisition`, `#robotics research`

---

## 电动车与新能源

<a id="item-ev-energy-1"></a>
### [欧盟对华混合动力车设 200 天进口配额，上限 191,780 辆](https://www.electrive.com/2026/11/24/eu-introduces-import-quotas-for-hybrids-from-china-and-other-countries/) ⭐️ 8.0/10

欧盟确认，自 12 月起对来自中国的混合动力汽车实施进口配额，同时限制其他国家的相关进口。该规定初步适用 200 天，在此期间中国混合动力车进口量被限定为 191,780 辆。报道未说明配额如何在车企之间分配，也未披露针对其他国家进口的具体限制幅度和完整法规文本。

Electrive · 11月24日 12:15

**「已证实与未证实」** 已证实：欧盟对从中国进口的混合动力乘用车实施临时进口配额，上限为 191,780 辆，实施期为 200 天，即 2026 年 12 月 1 日至 2027 年 6 月 18 日；相关措施同时限制来自其他国家的混合动力车进口（electrive 报道，Bloomberg、carnewschina 等亦作此报道）。
尚未证实：配额如何在车企之间分配、具体涵盖哪些车型（普通混动与插电式混动的比例）、对“其他国家”的限制范围与力度，以及 2027 年 6 月 18 日之后的安排，均未见于现有报道；Bloomberg 称该配额为临时措施，欧盟正进行一项调查，最终可能实施为期数年的长期限制，但调查结论与后续方案尚未公布。

**「背景」** 混合动力车（HEV/PHEV）指同时装有内燃机和电驱动系统的车型，介于纯燃油车与纯电动车之间，也是中国车企进入欧洲市场的重要品类。与按车辆逐台征收的关税不同，进口配额直接限定一段时间内的进口数量上限：此次措施先按 200 天执行，从 12 月起算，期间中国混合动力车的进口总量不得超过 191,780 辆。报道没有说明这 200 天期满后如何延续，也没有说明该配额在车企之间如何分配。

**「为什么重要」** 对向欧盟出口混合动力车的中国车企来说，这一配额直接把销量上限固定下来：200 天内 191,780 辆，意味着比亚迪、奇瑞、零跑等近两年在欧洲高速扩张的品牌无法再按现有增速无限放量，需要重新安排发运节奏与车型组合。据 Dataforce 数据，2026 年 10 月零跑在欧洲的注册量已达 13,902 辆、超过特斯拉的 11,722 辆，奇瑞为 7,348 辆（GlobalChinaEV 引用），配额落地后这些增量将首先受到约束。另一条现实路径是把产能搬到欧洲境内：马克龙称法国将在 1 月 18 日公布比亚迪第二座欧盟工厂的方案，比亚迪表示希望利用其欧洲工厂为当地买家造车——《China Car News》报道。对经销商和消费者而言，需留意配额期内的交付周期与价格变化。

**「后续看点」** 12 月措施生效后，关注欧盟是否公布配额在车企间的具体分配方式，以及 200 天期满时是延长、调整还是转为长期机制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://carnewschina.com/2026/11/24/eu-to-cap-hybrid-car-imports-from-china-at-191780-from-december-2026-to-june-2027/">EU to cap hybrid car imports from China at 191 , 780 from December ...</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-11-24/eu-adopts-cap-on-hyrbid-cars-to-help-curb-chinese-imports">EU Adopts Cap on Hybrid Cars to Help Curb Chinese Imports</a></li>
<li><a href="https://auto.mail.ru/article/135134-es-s-dekabrya-2026-goda-ogranichit-import-gibridov-iz-kitaya/">ЕС ограничил ввоз гибридов из Китая: квота 191 780 машин...</a></li>
<li><a href="https://www.theguardian.com/business/2026/sep/24/eu-sales-chinese-hybrid-cars-rocket">Alarm bells sound in Brussels as EU sales of Chinese hybrid cars rocket</a></li>
<li><a href="https://www.globalchinaev.com/post/leapmotor-outsells-tesla-in-europe-in-october-as-chinese-share-slips-to-135">Leapmotor outsells Tesla in Europe in October as Chinese share slips...</a></li>
<li><a href="https://carnewschina.com/2026/11/24/macron-says-france-will-share-plans-for-byds-second-eu-car-plant-on-january-18/">Macron says France will share plans for BYD ’s second EU car plant on...</a></li>

</ul>
</details>

**标签**: `#EU import quotas`, `#hybrid vehicles`, `#China auto imports`, `#trade policy`, `#automotive regulation`

---

<a id="item-ev-energy-2"></a>
### [比亚迪发布第三代唐 EV：五座旗舰 SUV 起售价低于 3 万美元](https://electrek.co/2026/11/24/byd-launches-new-luxury-5-seat-ev-suv-two-30-screens-under-30000/) ⭐️ 7.0/10

比亚迪在中国推出第三代唐（Tang）纯电 SUV，定位五座旗舰车型，车内配备两块尺寸超过 30 英寸的屏幕，起售价低于 3 万美元。报道将这款车描述为“大型、高科技”的五座 SUV，价格按中国市场计算。报道未给出续航里程、电池容量、配置分级或具体上市日期，也没有独立测试数据，因此上述价格与屏幕规格目前仅来自比亚迪一方的发布信息。

Electrek · 11月24日 15:40

**「已证实与未证实」** 已证实：据 Electrek 报道，比亚迪在中国推出第三代唐，定位五座旗舰纯电 SUV，起售价低于 3 万美元；同一篇报道列出的参数为后驱版单电机 402 马力（300 kW），CLTC 续航 730 公里（Premium 版）和 850 公里（Laser Premium、Laser Flagship 版）。行业媒体 ievchina 记录该车在 2026 年成都车展首发，搭载第二代刀片电池和“天神之眼”B 智驾系统。
尚未证实：具体起售价数字（报道只称“低于 3 万美元”）、各版本定价、交付时间以及中国以外市场的上市计划均未公布；730/850 公里为 CLTC 工况数据，并非独立实测，智驾功能的实际能力也没有第三方验证。

**「背景」** 唐是比亚迪旗下的大型 SUV 产品线，比亚迪把此次发布定义为第三代车型，即整车换代而非年度改款，此前两代唐已在同一细分市场销售。报道没有披露电池容量、续航里程、交付时间以及中国以外市场的上市安排。

**「为什么重要」** 对中国的购车者来说，这意味着旗舰级的大屏配置已经进入 3 万美元以下的价格区间；但这一价格只适用于中国市场，海外买家无法以该价格买到同款车型。此外，报道未公布续航与电池参数，因此目前还无法把它与同价位的五座纯电 SUV 做实际对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://electrek.co/2026/11/24/byd-launches-new-luxury-5-seat-ev-suv-two-30-screens-under-30000/">BYD launches new luxury 5-seat EV SUV with two +30&quot; screens for...</a></li>
<li><a href="https://ievchina.com/brands/byd-3rd-gen-tang-2026-specs-850km-range-flash-charge-chengdu/">BYD Tang 2026 Specs , Price : 850 km Range , 5-Min Flash Charge</a></li>

</ul>
</details>

**标签**: `#BYD`, `#Tang EV`, `#electric SUV`, `#vehicle launch`, `#EV pricing`

---

<a id="item-ev-energy-3"></a>
### [大众与 Elli 12 月在德国推出 1,995 欧元 V2G 墙盒](https://www.electrive.com/2026/11/24/vw-and-elli-launch-e1995-v2g-bidi-wallbox/) ⭐️ 7.0/10

大众汽车与能源子公司 Elli 计划于 2026 年 12 月在德国推出其首个车网互动（V2G，Vehicle-to-Grid，指电动车电池向电网反向送电）套餐，其中所需的直流墙盒定价 1,995 欧元。首批发售覆盖大众、大众商用车、Cupra 与斯柯达四个品牌。electrive 报道称电力资费方案的细节也已一并公布，但报道未给出具体电价、墙盒充放电功率或各车型的兼容清单，因此这仍是计划中的产品，消费者目前还无法买到。

Electrive · 11月24日 16:00

**「已证实与未证实」** 已证实：大众与 Elli 宣布 2026 年 12 月进入德国市场，直流墙盒售价 1,995 欧元，并确认大众、大众商用车、Cupra 和斯柯达四个品牌参与首发（据 electrive 报道厂商公布的信息）。
尚未证实：报道未披露电价资费的具体数字、墙盒的充放电功率与所需车型配置，也未给出确切开售日期与交付时间；这些内容目前仅来自厂商说法，没有独立测试或第三方验证。

**「背景」** V2G（车网互动，vehicle-to-grid）指电动车电池不仅能从电网取电，还能反向把电送回家庭或电网，用于削峰填谷或应急供电。要做到这一点，关键在于充电设备：普通车载交流充电机通常只能单向整流，因此反向送电需要具备双向变换能力的直流墙盒，这也是该方案以 DC 墙盒为核心部件的原因。对大众集团而言，这是其能源子公司 Elli 首次在德国市场推出 V2G 套餐，并首次把斯柯达与大众、大众商用车、Cupra 一起纳入首发品牌范围。

**「为什么重要」** 对这四个品牌的车主来说，1,995 欧元对应的是直流墙盒本身，整套方案的实际成本还取决于尚未公布细节的电力资费；下单前需要确认自己的车型是否支持双向充电，以及本地安装与并网条件是否满足。

**「后续看点」** 关注 2026 年 12 月的德国上市是否按期落地，以及 Elli 届时公布的具体电价与支持双向充电的车型名单。

**标签**: `#V2G`, `#bidirectional charging`, `#Volkswagen`, `#Elli`, `#EV charging`

---

<a id="item-ev-energy-4"></a>
### [瑞士授出 32 处卡车充电站点，Fastned、Obornes 与 Milence 分获三标段](https://www.electrive.com/2026/11/24/switzerland-fastned-obornes-and-milence-secure-initial-truck-charging-network/) ⭐️ 7.0/10

瑞士联邦道路局（FEDRO）已完成 2026 年 1 月招标的 32 处卡车充电站点授标，将在国道沿线建设总计 82 座卡车充电站。三个标段分别授予 Fastned（第一标段）、Obornes（第二标段）和 Milence（第三标段）。目前这是授标决定，报道未披露各站点充电功率、单站桩数、开工与投运时间，也未提及电价或结算方式。

Electrive · 11月24日 14:30

**「已证实与未证实」** 已证实：瑞士联邦公路局（FEDRO）将 2026 年 1 月招标的 32 个地点分配给三家企业，第 1 标段归 Fastned、第 2 标段归 Obornes、第 3 标段归 Milence，沿国道规划共 82 座卡车充电站；这是合同授予，不是已投运的充电设施（electrive 根据 FEDRO 公告报道）。
尚未证实：各站点的具体位置、充电功率与单站规模未在报道中说明；首批站点 2030 年投运、2035 年前建成 82 座的进度来自 mobility-360、The EV Report 等二手报道，FEDRO 原始公告的相应时间表尚未经独立核实。

**「背景」** 瑞士联邦公路局（FEDRO）于 2026 年 1 月启动这批选址的招标，本次中标的 32 个场址是其中的全部标段。该计划被置于瑞士《能源战略 2050》和交通部电动出行路线图的框架下，目标是在 2035 年前沿国道建成 82 座卡车快速充电站，首批站点预计 2030 年投运。

**「为什么重要」** 对沿瑞士国道跑干线运输的电动重卡车队来说，补能不再由单一运营商覆盖，而要根据线路分别对接 Fastned、Obornes 和 Milence 三家。在功率等级、投运时间和接入与结算方式公布之前，车队还无法据此排定穿越瑞士的充电计划，跨运营商的使用条件是需要跟进的实际问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://theevreport.com/swiss-electric-truck-charging-sites-fastned-obornes-milence">Swiss Electric Truck Charging Sites Go to Fastned, Obornes ...</a></li>
<li><a href="https://kurrant.com/kurrantly-news/switzerland-awards-32-motorway-charging-sites-for-electric-trucks-to-fastned-obornes-and-milence/">Switzerland Awards 32 Motorway Charging Sites For Electric ...</a></li>
<li><a href="https://mobility-360.ch/en/market-en/fedro-awards-32-fast-charging-sites-for-electric-trucks/">FEDRO awards 32 fast-charging sites for electric trucks</a></li>
<li><a href="https://theevreport.com/swiss-electric-truck-charging-sites-fastned-obornes-milence">Swiss Electric Truck Charging Sites Go to Fastned, Obornes ...</a></li>
<li><a href="https://electricalnews.co.uk/switzerland-awards-32-truck-charging-sites/">Switzerland awards 32 truck charging sites | IN Power</a></li>

</ul>
</details>

**标签**: `#EV charging`, `#electric trucks`, `#Switzerland`, `#Fastned`, `#Milence`

---

<a id="item-ev-energy-5"></a>
### [印度拉贾斯坦 8 号机组获首次临界许可，凯加 1 号机组复运](https://www.world-nuclear-news.org/articles/start-up-milestones-for-indian-plants) ⭐️ 7.0/10

印度核监管机构已批准印度核电公司（NPCIL）为拉贾斯坦原子能项目 8 号机组进行“首次临界”（First Approach to Criticality，即装料后逐步将反应堆推向自持链式反应的关键调试步骤）。这是一项启动前的监管许可，并不代表该机组已经达到临界。与此同时，世界核新闻报道，凯加核电站 1 号机组在经历该媒体称为“创纪录长度”的翻新停堆后恢复运行。报道没有给出停堆持续多久、凯加 1 号机组复运的确切日期，也没有给出 8 号机组何时实际达到临界的时间表。

World Nuclear News · 11月24日 17:10

**「已证实与未证实」** 已证实：据世界核新闻报道，印度核监管机构向印度核电公司（NPCIL）发放了拉贾斯坦原子能项目 8 号机组的首次临界许可；凯加核电站 1 号机组在翻新停堆后恢复运行。
尚未证实：停堆的实际时长（报道仅称“创纪录”）、凯加 1 号机组复运的确切日期、8 号机组真正达到临界的时间，以及机组功率等运行数据，报道均未提供，也没有监管文件或第三方独立信息加以佐证。

**「背景」** 拉贾斯坦原子能项目 8 号机组（RAPP-8）是印度在建的压水重水反应堆（PHWR）机组。所谓“首次临界”（First Approach to Criticality），是调试阶段中逐步提升反应性、让反应堆首次达到自持链式反应的一步；监管机构放行这一步骤，意味着机组可以开始受控启动，但距离并网发电和商业运行仍有距离。

**「为什么重要」** 对 NPCIL 而言，首次临界许可是 8 号机组从建设阶段转入调试的必经关口：只有获得这项许可，后续才能装料并向临界、并网推进，因此它决定该机组何时能开始发电。凯加 1 号机组的复运则意味着，这台在长时间停堆检修后退出运行的机组重新向电网供电；这也说明，翻新延寿是印度现役机组继续服役的现实路径。

**「后续看点」** 接下来可关注 8 号机组是否实际达到首次临界，以及何时并网发电；这两步通常由 NPCIL 或印度核监管机构发布公告确认。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://energy.economictimes.indiatimes.com/news/power/aerb-clears-first-approach-to-criticality-of-700-mw-rajasthan-nuclear-reactor/136030040">AERB clears first approach to criticality of 700 MW Rajasthan ...</a></li>
<li><a href="https://www.nuclearnewsnetwork.com/tracker/rajasthan-8">Rajasthan-8 (RAPP-8) — status and schedule | Nuclear News Network</a></li>

</ul>
</details>

**标签**: `#nuclear`, `#India`, `#reactor restart`, `#regulatory approval`, `#clean energy`

---

## 航天

<a id="item-space-1"></a>
### [神舟二十四号发射，天宫空间站迎来首位外国航天员](https://www.nasaspaceflight.com/2026/11/shenzhou-24/) ⭐️ 8.0/10

中国于 11 月 25 日 00:18 UTC（北京时间 08:18）在酒泉卫星发射中心用长征二号 F/G 运载火箭发射神舟二十四号载人飞船，将三名航天员送往天宫空间站，其中巴基斯坦航天员穆罕默德·泽尚·阿里（Muhammad Zeeshan Ali）成为首位进入该站的外国航天员。指令长汤洪波由此成为首位三访天宫的航天员，吴仪首次执行飞行任务并担任飞行工程师；另一名巴基斯坦航天员胡拉姆·达乌德（Khurram Daud）担任备份。阿里以载荷专家身份在轨约一周，将开展中巴微重力实验并安装样品与实验单元，之后搭乘已在轨的神舟二十三号飞船返回；神舟二十三号指令长朱杨柱则继续留守六个月，届时将成为中国首位单次在轨驻留满一年的航天员。两名巴基斯坦航天员自 4 月起在北京的中国航天员科研训练中心接受训练，依据是两国 2025 年 2 月签署的协议。

NASASpaceflight · 11月24日 16:26

**「已证实与尚未证实」** 已证实：据 NASASpaceflight 报道，神舟二十四号于北京时间 11 月 25 日 8 时 18 分（00:18 UTC）由长征二号 F/G 火箭在酒泉卫星发射中心发射；乘组为中国载人航天工程办公室在发射前一天公布的指令长汤洪波、飞行工程师吴毅和巴基斯坦载荷专家穆罕默德·齐尚·阿里，另一名巴方航天员赫拉姆·达乌德为备份。阿里将成为首位进入轨道的巴基斯坦航天员，计划在轨约一周后改乘神舟二十三号返回。
尚未证实：阿里是否已成功对接并进入天宫、以及“首位进入空间站的外国访客”这一定性，目前仍属任务计划而非已完成的独立确认；该报道发布于 11 月 24 日 16 时 26 分（UTC），早于其自述的发射时刻，正文在升空阶段即被截断，对接时间、在轨实验清单与具体停留天数均依赖中国载人航天方面及二手转述。

**「背景」** 天宫空间站此前接待的都是中国航天员；此次国际参与源于 2025 年 2 月中国与巴基斯坦签署的航天合作协议。根据该协议，巴基斯坦航天员自 2026 年 4 月起在北京的中国航天员科研训练中心接受训练，最终由穆罕默德·齐尚·阿里执行这次短期飞行。

**「为什么重要」** 对其他国家而言，天宫首次有外国航天员进驻，中巴 2025 年 2 月签署的协议由此成为进入该站的现实路径；但阿里的在轨时间仅约一周，且需搭乘先前对接的神舟二十三号返回，实验窗口和载荷规模都受此限制，希望参与微重力实验的研究者需按这一周期安排项目。

**「后续看点」** 阿里约一周后乘神舟二十三号返回地面，其短期驻留的实验结果与交接安排将是首个观察点；朱杨柱延长驻留六个月结束时，能否完成中国首次单次在轨满一年同样值得关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Shenzhou_24">Shenzhou 24 - Wikipedia</a></li>
<li><a href="https://www.nature.com/articles/d41586-026-03829-y">Pakistani astronaut to become first foreign visitor to China ...</a></li>

</ul>
</details>

**标签**: `#Tiangong`, `#Shenzhou-24`, `#China space program`, `#international cooperation`, `#crewed spaceflight`

---

## 科技产业与政策

<a id="item-tech-industry-1"></a>
### [澳大利亚通过《数字注意义务法》，大型平台或因可预见伤害面临数十亿罚款](https://www.techmeme.com/261125/p12#a261125p12) ⭐️ 9.0/10

澳大利亚议会于周三通过了《数字注意义务法》（Digital Duty of Care Act），据美联社报道，该法可对未能防止可预见的网络伤害的科技巨头处以数十亿澳元级罚款。这将是澳大利亚首次以一般性“注意义务”的形式，把预防伤害的责任写入平台的法律义务，而不再只针对具体内容类型逐项设规。美联社的报道未在可见部分给出罚款上限的具体数额、受约束平台的名单、生效时间以及监管执行机构，这些细节仍待确认。该法针对的是“可预见的伤害”，即平台需事先评估并降低其服务可能造成的风险，而非仅在伤害发生后补救。

Techmeme · 11月25日 10:05

**「已证实与未证实」** 已证实：美联社记者 Rod McGuirk 报道，澳大利亚议会周三通过了这项在线安全立法，法律允许对未防止可预见网络伤害的科技巨头处以数十亿美元级别的罚款。
尚未证实：罚款的具体上限、法律正式生效的日期、适用平台的门槛与范围、由哪一监管机构执行，以及“可预见伤害”的判定标准；这些内容在报道可见部分均未出现。

**「背景」** 澳大利亚此前的《2021 年在线安全法》主要依靠 eSafety 专员在接到举报后要求平台下架具体的有害内容，属于事后逐案处理。新法把义务前移：平台必须主动识别并降低可预见伤害的风险，而不是等监管机构点名后再行动，这也是“注意义务”（duty of care）一词的含义所在。

**「为什么重要」** 对在澳大利亚运营的大型平台而言，合规重心将从“接到投诉后删除内容”转向事前的风险评估与减害机制，因为法律责任不再取决于某条内容是否违规，而取决于平台是否预见了可避免的伤害。平台需要在此之前梳理自身在澳大利亚的用户规模是否落入适用范围，并准备可向监管机构证明的风险评估记录。

**「后续看点」** 接下来值得关注的是该法的生效时间表，以及监管机构如何界定和认定“可预见的伤害”——这将决定罚款条款在实践中有多大约束力。

**标签**: `#Australia`, `#online safety`, `#regulation`, `#Big Tech`, `#platform liability`

---

<a id="item-tech-industry-2"></a>
### [OpenAI 前员工被控窃听，彭博社称发现数百段录音](https://www.tomshardware.com/tech-industry/artificial-intelligence/saudi-openai-eavesdropper-who-bugged-company-office-had-hundreds-of-private-recordings-was-in-frequent-communication-with-saudi-government-perp-had-dozens-of-recordings-of-discussions-of-trade-secrets) ⭐️ 8.0/10

前 OpenAI 员工 Abdulrahman Alfozan 被控在行政会议室电视后安装基于 Seeed Xiao ESP32-S3 的隐蔽录音设备，于 10 月被捕，10 月 27 日的起诉书指控他截取口头通信，而非窃取商业秘密或经济间谍。彭博社 11 月 23 日报道称，检方在法庭文件中表示，在其个人电脑上发现数百个音频文件，其中数十段是 2026 年 9 月在 OpenAI 的会议或对话，部分可能涉及商业秘密；文件还称他保存了 AI 生成的转录文本，部分录音上传至 Dropbox，并按日期和内容分类，其手机中还有标记为机密的“战略合作”文件照片。检方称他在秘密录音的同时与沙特政府相关人员频繁联系，并以此反对保释；Alfozan 否认窃取商业秘密，其律师称他与沙特政府没有特殊或秘密关系。法院定于周二举行听证，可能决定是否批准其 100 万美元保释请求，调查也可能带来追加指控。

Tom&\#x27;s Hardware · 11月24日 16:30

**「已证实与未证实」** 已证实：根据 10 月 27 日的起诉书，OpenAI 前员工 Abdulrahman Alfozan 被控“拦截口头通信”（interception of oral communications），而非窃取商业秘密或经济间谍；检方在法庭文件中称，在其个人电脑上发现数百个音频文件，其中数十段是 2026 年 9 月在 OpenAI 发生的会议或对话录音，部分录音已上传至 Dropbox，并按日期和内容重新命名（《彭博社》11 月 23 日报道，Tom&\#x27;s Hardware 转述）。
尚未证实：这些录音是否确实含有商业秘密，以及他是否打算或已经将内容交给沙特方面；Alfozan 本人否认，其律师称他与沙特政府“没有特殊或秘密联系”，检方也表示尚不清楚录音的用途。周二保释听证的结果、100 万美元保释金请求能否获准、是否追加指控，目前均无定论，最新细节仅来自《彭博社》一家媒体的报道。

**「背景」** 本案的直接前情是今年 10 月的一起办公室窃听事件：OpenAI 前员工 Abdulrahman Alfozan 因在公司高管会议室的电视后方安装一枚基于 Seeed Xiao ESP32-S3 微控制器的隐蔽录音装置而被捕，装置数日后被发现，调查随后将其与 Alfozan 关联。10 月 27 日的起诉书对他提出的指控是非法截取口头通信，而非窃取商业机密或经济间谍罪，这意味着目前指控的核心在于录音行为本身，而非录音内容的去向。

**「为什么重要」** 对 OpenAI 而言，直接后果是内部保密审查不再只管文件权限，还要覆盖会议室物理设备和员工个人云盘；检方称录音设备被藏在行政会议室电视后，音频与 AI 转录被上传到 Dropbox。

**「后续看点」** 法院接下来将裁定是否准许 Alfozan 以 100 万美元保释；检方表示，一旦查明这些录音的内容和去向，可能追加指控。若目前“非法截取口头通信”的罪名成立，他最高面临五年监禁和 25 万美元罚款。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bloomberg.com/news/articles/2026-11-23/openai-staffer-likely-captured-secrets-on-hidden-bug-us-says">OpenAI Staffer Likely Captured Secrets on Hidden Bug, US Says</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-10-13/openai-says-staffer-arrested-for-hidden-recording-device-in-office">OpenAI Employee Arrested for Planting Recording Device in ...</a></li>
<li><a href="https://www.pbs.org/newshour/world/ex-openai-worker-accused-of-bugging-conference-room-planned-to-fly-to-saudi-arabia-prosecutors-say">Ex-OpenAI worker accused of bugging conference room ... - PBS</a></li>
<li><a href="https://thehackernews.com/2026/11/former-openai-engineer-pleads-not.html">Former OpenAI Engineer Pleads Not Guilty to Planting Covert Device...</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#corporate espionage`, `#AI trade secrets`, `#national security`, `#Saudi Arabia`

---

<a id="item-tech-industry-3"></a>
### [Flipkart CEO 克里希纳穆尔蒂将于 12 月 4 日离任，CTO 暂代](https://www.techmeme.com/261125/p11#a261125p11) ⭐️ 7.0/10

沃尔玛旗下的 Flipkart 表示，首席执行官 Kalyan Krishnamurthy 计划于 12 月 4 日离任，公司首席技术官（CTO）将出任临时 CEO。据彭博社报道，Krishnamurthy 是将 Flipkart 打造成印度第一大在线零售商的“关键设计师”之一。公告只给出了离任日期和临时接任安排，没有说明永久 CEO 的人选，也没有交代此次人事变动与公司战略或上市计划的关系。

Techmeme · 11月25日 09:40

**「已证实与未证实」** 已证实：彭博社（Sankalp Phartiyal）报道，沃尔玛表示，其旗下的 Flipkart 首席执行官卡利扬·克里希纳穆尔蒂（Kalyan Krishnamurthy）计划于 12 月 4 日离任，并任命公司首席技术官（CTO）为临时 CEO；Flipkart 是印度最大的在线零售商，克里希纳穆尔蒂是公司成长为印度第一大电商的关键推动者。

尚未证实：报道未点名这位临时 CEO 的 CTO 姓名，也未说明克里希纳穆尔蒂离任的原因、是否已有正式继任者的遴选安排，以及管理层更替对 Flipkart 战略的影响。另有报道称，Flipkart 在周一临时召开全员大会，令外界对其离职的猜测升温，但该细节仅见于单一报道。本条为简讯式转述，上述内容均需以沃尔玛或 Flipkart 的官方公告及彭博社原文进一步核实。

**「背景」** Flipkart 是印度最大的在线零售商，由美国零售巨头沃尔玛控股，因此其管理层变动同时牵动沃尔玛的印度业务布局。据彭博社报道，即将离任的首席执行官 Kalyan Krishnamurthy 被视为推动 Flipkart 成长为印度第一电商的关键人物，这也解释了此次人事变动为何受到关注。

**「为什么重要」** 克里希纳穆尔蒂的离开将让 Flipkart 在 12 月 4 日之后进入由 CTO 临时接任的状态，而未公布正式继任者——对这家沃尔玛持股的印度最大电商而言，重大战略与上市准备工作的连续性因此取决于临时安排能维持多久。《经济时报》2024 年 5 月报道，沃尔玛表示正在评估让 Flipkart 上市的最佳时机，并把公司注册地迁回印度与最终 IPO 挂钩；在这一背景下，CEO 缺位是投资者和合作伙伴需要跟踪的具体不确定性，而非抽象的人事变动。

**「后续看点」** 12 月 4 日离任正式生效后，Flipkart 与沃尔玛是否公布常任 CEO 人选，以及临时 CEO 期间业务和融资安排是否出现调整。

<details><summary>参考链接</summary>
<ul>
<li>Flipkart CEO Kalyan Krishnamurthy To Exit After Nearly A Decade</li>
<li><a href="https://economictimes.indiatimes.com/tech/technology/evaluating-the-right-time-for-flipkart-ipo-walmart-international-ceo/articleshow/110185825.cms?from=mdr">Flipkart IPO : Evaluating the right time for Flipkart IPO : Walmart ...</a></li>

</ul>
</details>

**标签**: `#Flipkart`, `#Walmart`, `#India e-commerce`, `#leadership change`, `#executive turnover`

---

<a id="item-tech-industry-4"></a>
### [华为称鸿蒙装机量突破 1 亿台，应用与服务逾 46 万个](https://www.techmeme.com/261125/p7#a261125p7) ⭐️ 7.0/10

华为宣布，其不依赖安卓的鸿蒙操作系统（HarmonyOS）在手机、平板和 PC 上的装机量已超过 1 亿台，平台提供逾 46 万个应用与服务，注册开发者超过 1200 万。这些数字由华为自己公布，《南华早报》记者 Iris Deng 做了报道，报道未附第三方核验数据。鸿蒙是一个“去安卓化”的系统，原有安卓应用不能直接沿用，需要另行开发适配版本。

Techmeme · 11月25日 07:10

**「已证实与未证实」** 已证实：据《南华早报》与新华社报道，华为在一份公司声明中称，HarmonyOS 装机量已突破 1 亿台，生态提供逾 46 万个应用与服务、注册开发者超过 1200 万；新华社另称，华为于 2024 年 10 月推出 HarmonyOS 5 新架构，此后更新至 6、7 版本。

尚未证实：1 亿这一数字是累计激活量还是当前活跃设备数、统计截止时间为何，以及手机、平板、PC 各自的分布，华为均未说明，也没有第三方机构独立核验；46 万应用数和 1200 万开发者数同样仅有华为单方面口径。

**「背景」** 鸿蒙（HarmonyOS）是华为自研的操作系统，其“不依赖安卓”（Android-free）的定位意味着它无法直接借用谷歌的安卓应用生态，必须自建一套应用与开发者体系。对这类系统来说，装机量决定开发者是否愿意投入适配，而应用数量又决定用户是否愿意留下，因此安装量、应用数和注册开发者数三项通常被一起用来衡量生态是否真正站住脚。华为此次公布的正是这三个维度的数字。

**「为什么重要」** 对开发者来说，1 亿台设备意味着华为设备上出现了一个不容忽视的独立应用目标平台：面向这部分用户的应用需要单独的鸿蒙版本和额外适配工作，无法直接复用安卓安装包。不过这批装机量对应的是华为自有设备，与安卓、iOS 的全球体量仍不在同一量级。

**「后续看点」** 可关注第三方机构（如 IDC、Counterpoint）随后发布的鸿蒙在中国智能手机操作系统份额统计，以及华为是否披露各系统版本的装机分布，用来交叉核对这 1 亿台的构成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.scmp.com/tech/big-tech/article/3375680/huaweis-home-grown-harmonyos-passes-100-million-device-mark-landmark-moment">Huawei’s home-grown HarmonyOS passes 100 million device mark ...</a></li>
<li><a href="https://english.news.cn/20261124/36162a70e643422492296708225f79e1/c.html">Huawei&#x27;s homegrown HarmonyOS tops 100 million devices</a></li>
<li><a href="https://timesofindia.indiatimes.com/technology/tech-news/huaweis-android-alternative-hits-100-million-installs-and-overtakes-ios-in-china/articleshow/136154203.cms">Huawei’s Android alternative hits 100 million installs and ...</a></li>

</ul>
</details>

**标签**: `#Huawei`, `#HarmonyOS`, `#operating systems`, `#China tech`, `#mobile ecosystem`

---

<a id="item-tech-industry-5"></a>
### [TikTok 与 AI 助推“真实犯罪”网络，暴力攻击增多，WIRED 报道](https://www.wired.com/story/the-true-crime-community-is-inspiring-violent-attacks-through-tiktok/) ⭐️ 7.0/10

WIRED 报道称，其看到的共享研究显示，一个由迷恋大规模枪击者的年轻人组成的虚无主义网络正利用 TikTok 和 AI 传播信息，与该网络相关的暴力攻击正在大幅增加。报道没有点名研究机构，也没有给出攻击数量、统计时间范围或具体案例。TikTok 是否回应、采取了哪些审核措施，报道同样未说明。

Wired · 11月25日 11:00

**「已证实与未证实」** 已证实：WIRED 报道称，其看到的共享研究显示，一个迷恋大规模枪击者的年轻人网络利用 TikTok 和 AI 传播理念，相关暴力攻击大幅增加。
尚未证实：研究机构、攻击数量、统计口径和具体案例均未披露；TikTok 的回应及审核措施也未说明，报道未提供独立验证。

**「背景」** 这里的“真实犯罪社群”指的是在社交平台上围绕大规模枪击案凶手形成的松散亚文化，参与者以年轻人为主，把凶手当作迷恋对象并交换、传播相关素材。关键在于传播方式的变化：TikTok 的“为你推荐”信息流会依据观看和互动，把用户并未关注的账号内容推送给陌生人，因此这类主题的视频可以越过关注关系触达新观众；据《连线》报道，该网络还借助 AI 生成和扩散内容。此前平台内容治理的讨论多集中在单条违规视频的删除上，而这次研究关注的是一个持续运作、跨账号扩散的网络。

**「为什么重要」** 对平台审核团队而言，直接后果是要应对一个利用 TikTok 和 AI 传播极端叙事、并与不断增加的攻击相关的网络，而不是只删除孤立视频；报道未披露 TikTok 是否已部署相应检测手段。

**「后续看点」** 后续可关注研究团队是否公布完整报告和攻击统计数据，以及 TikTok 是否就报道中的网络和内容审核措施作出回应。

**标签**: `#platform safety`, `#TikTok`, `#content moderation`, `#AI`, `#violent extremism`

---

<a id="item-tech-industry-6"></a>
### [FISA 第 702 条续期或搭上国防授权法案，Politico 报道](https://www.theverge.com/policy/1041568/fisa-ndaa-blue-wave) ⭐️ 7.0/10

距离本届立法会期结束仅剩数周，部分美国国会议员正试图续期《外国情报监视法》（FISA）第 702 条这一无令状监听授权，并考虑把它附加到必须通过的《国防授权法案》（NDAA）上。参议院情报委员会成员、共和党参议员迈克·朗兹（Mike Rounds）对 Politico 表示，第 702 条可能被附加到 NDAA；The Verge 称这是这场拉锯战的最新一步，并指出该授权尚未在法律上失效。目前没有已提交的法案文本或表决安排，续期期限和具体条款也未公布。

The Verge · 11月24日 20:00

**「已证实与未证实」** 已证实：The Verge 报道，参议员迈克·朗兹对 Politico 表示，FISA 第 702 条可能被附加到 NDAA；报道还称该监听授权尚未在法律上失效。
尚未证实：是否真会附加、附加文本的具体内容、续期时长和表决时间表均未公布；The Verge 引用的朗兹原话在报道摘要中被截断。

**「背景」** 第 702 条是《外国情报监视法》\(FISA\) 中最具争议的部分：它允许情报机构无需逐案申请搜查令，即可批量收集被合理认为位于美国境外的非美国人的通信，而美国人的通信往往被顺带获取。国会研究服务处的资料显示，该条款的法定授权已经于 2026 年 6 月 12 日自动废止，此前一项重新授权立法在国会表决失败；The Verge 则指出，这项授权“尚未在技术上失效”。11 月 12 日，多个民权与隐私组织联名致信议员，要求不要把第 702 条的延期塞进《国防授权法案》\(NDAA\) 或其他必须通过的立法——而这正是目前被讨论的路径。

**「为什么重要」** 若走通，第 702 条的续期将不再走单独法案，而是与必须通过的军费法案绑定表决；这会让反对者更难通过单独修正案去增加搜查令要求或限制对美国人通信的查询，也会把续期时间表压到会期最后几周。

**「后续看点」** 未来数周，关注 NDAA 的修正案或最终文本是否真的写入第 702 条续期条款，以及国会是否在会期结束前就此表决。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.brennancenter.org/our-work/research-reports/section-702-foreign-intelligence-surveillance-act-fisa-2026-resource-page">Section 702 of the Foreign Intelligence Surveillance Act ...</a></li>
<li><a href="https://www.congress.gov/crs_external_products/LSB/PDF/LSB11444/LSB11444.1.pdf">The Impact of FISA Section 702 s Repeal - Congress.gov</a></li>
<li><a href="https://www.demandprogress.org/api/media/file/NoFISANDAA.pdf">No FISA in NDAA - demandprogress.org</a></li>

</ul>
</details>

**标签**: `#FISA 702`, `#surveillance policy`, `#US Congress`, `#NDAA`, `#privacy`

---

<a id="item-tech-industry-7"></a>
### [美国司法部称破获史上最大诈骗网络，指控 800 余名被告](https://www.tomshardware.com/tech-industry/cyber-security/us-doj-touts-largest-ever-crackdown-on-scammers-across-the-globe-as-it-seizes-14-000-devices-and-usd17-billion-in-illicit-funds-operation-results-in-800-defendants-and-frees-2-200-forced-laborers) ⭐️ 7.0/10

美国司法部 11 月 24 日宣布，已对 800 余名被告提起指控，涉及 85 个联邦辖区的 400 多起案件，并称已挽回逾 80 亿美元“原本将落入骗子之手的受害者损失”，将其称为该部历史上“最大规模”的反诈骗行动。FBI 局长卡什·帕特尔公布了代号“Operation Blackout”的跨部门行动细节：在亚洲、非洲和中东捣毁 29 个集中式诈骗园区，查没近 170 亿美元资金和超过 1.4 万台设备，50 名“诈骗行为人”在美国被联邦起诉，境外合作伙伴据此逮捕或拘留 320 多人。司法部长托德·布兰奇称行动目标是“拆解犯罪网络”而非只抓个体骗子；该行动源自特朗普 3 月签署的要求政府各部门联合打击诈骗的行政命令。报道内部数字存在不一致：标题与 FBI 部分称查没 170 亿美元，正文另一处则称挽回逾 80 亿美元受害者损失，两者口径不同。上述数字均为司法部与 FBI 自述，未见独立核实。

Tom&\#x27;s Hardware · 11月24日 22:30

**「已证实与未证实」** 已证实：美国司法部官网新闻稿及《福克斯新闻》报道显示，司法部长 Todd Blanche 宣布对 800 多名被告提起指控，案件超过 400 起、分布在 85 个联邦辖区，并称追回逾 80 亿美元“意图骗取受害者损失”。司法部称，FBI 主导的“Operation Blackout”在亚、非、中东捣毁 29 处诈骗园区，限制（restrained）近 170 亿美元非法资金、查获逾 1.4 万台设备。

尚未证实：原文标题称“查获 170 亿美元”，而司法部原文用词是“限制（restrained）”，二者并不等同；同时 170 亿美元与 80 亿美元是两个不同口径（前者为非法资金总额，后者为意图骗取损失），报道未加区分，读者不应视为同一笔金额。2,200 余名被解救的贩运劳工、境外 320 余人被捕、50 名“诈骗人员”在美被起诉等数字均来自执法机构自述，无独立核实；文中引用的盖洛普“2025 年美国民众被骗 68 亿美元”数据亦未经其他来源印证。

**「背景」** 今年 3 月，美国总统特朗普签署行政令，要求联邦政府各部门联合行动，打击民众日常遭遇的诈骗与掠夺性骗局；司法部此次宣布的专项行动正是在这一指令下展开。此类跨境诈骗园区常以人口贩运受害者充当“员工”运营网络骗局，因此联邦执法把解救被贩运劳工与查封园区设备、资金放在同一次行动中处理。

**「为什么重要」** 对普通用户和企业而言，这次行动的规模说明执法打击的对象已不只是零散骗子，而是以人口贩卖维持运转的境外诈骗园区，但报道同时指出，查没的 170 亿美元只占盖洛普数据中美国人在 2025 年因诈骗损失约 680 亿美元的一部分，因此受害者不应指望追回资金成为常态。对在美运营的银行与平台，压力则来自另一侧：报道提到摩根士丹利、美国银行、摩根大通和富国银行已因担心 AI 代理访问客户账户或发起交易而封堵此类活动并修改服务条款。

**「后续看点」** 可关注司法部是否公布逐案明细或更新数据，以厘清“170 亿美元查没”与“80 亿美元挽回损失”的确切口径，以及这 400 多起案件在 85 个联邦辖区的起诉与判决进展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.justice.gov/opa/pr/justice-department-announces-largest-ever-crackdown-scammers-targeting-over-800-defendants">Justice Department Announces Largest-Ever Crackdown on ...</a></li>
<li><a href="https://www.foxnews.com/politics/doj-recovers-8b-charges-more-than-800-suspects-largest-anti-scam-surge-history">Justice Department charges 800 in anti-scam crackdown ...</a></li>
<li><a href="https://www.yahoo.com/news/us/articles/us-doj-touts-largest-ever-223000811.html?fr=sycsrp_catchall">US DOJ touts &quot;largest-ever&quot; crackdown on scammers ... - Yahoo</a></li>

</ul>
</details>

**标签**: `#cybercrime`, `#DOJ`, `#law-enforcement`, `#fraud`, `#policy`

---

