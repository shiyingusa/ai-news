# AI 每日雷达 - 2026-11-27

> 过去一天共筛查 217 条科技资讯，留下最值得读的 12 条。

---

**人工智能**
1. [AMD 专用 llama.cpp 分支登上 Hacker News](#item-ai-news-1) ⭐️ 7.0/10

**芯片与算力**
1. [台积电 A14 的 0.9 版 PDK 可供设计导入](#item-chips-compute-1) ⭐️ 8.0/10
2. [得州解冻 1,800 多个数据中心项目，《金融时报》报道](#item-chips-compute-2) ⭐️ 7.0/10
3. [磷化铟供应链吃紧，AI 光互连面临材料瓶颈](#item-chips-compute-3) ⭐️ 7.0/10

**电动车与新能源**
1. [田湾 8 号机组完成热试并接收首炉核燃料](#item-ev-energy-1) ⭐️ 8.0/10
2. [IONNA 加州启用 22 枪充电站，并向特斯拉开放自动充电认证](#item-ev-energy-2) ⭐️ 7.0/10
3. [西班牙电动车补贴预算耗尽，Auto+ 短期内不再追加](#item-ev-energy-3) ⭐️ 7.0/10
4. [三菱日联银行为日本两座 90MW 储能项目放款，融资条款挂钩通胀调整](#item-ev-energy-4) ⭐️ 7.0/10
5. [中国光伏累计装机达 1.33 太瓦，江苏公布 2027 年竞价框架](#item-ev-energy-5) ⭐️ 7.0/10
6. [通威签署罗马尼亚 Dama Solar 846 MW 组件供应协议](#item-ev-energy-6) ⭐️ 7.0/10
7. [港科大用跨界面工程做出 27.04%效率钙钛矿电池](#item-ev-energy-7) ⭐️ 7.0/10

**科技产业与政策**
1. [英国 FCA 拟要求 DeFi 平台取得授权，立场严于美欧，《金融时报》报道](#item-tech-industry-1) ⭐️ 7.0/10

---

## 人工智能

<a id="item-ai-news-1"></a>
### [AMD 专用 llama.cpp 分支登上 Hacker News](https://devnull.land/amd-specific-llama-cpp) ⭐️ 7.0/10

一个针对 AMD GPU 优化的 llama.cpp 分支在 Hacker News 上被分享，意在改善在 AMD 硬件上本地跑大模型的推理效率，帖子里聚集了不少自己动手改内核的开发者。该帖正文无法获取，因此分支的具体改动、维护者、许可证和实测加速比都无法从现有报道中核实。评论区给出的背景是：约 2018 年的 gfx906 数据中心卡算力平平，却配有 32GB HBM2 和约 1TB/s 带宽，二手价约 200 美元，同时没有 tensor core、也不支持原生 bf16，于是社区多年来各自维护针对这类卡的 llama.cpp 分支。

Hacker News · julianlam · 11月26日 17:11 · [社区讨论](https://news.ycombinator.com/item?id=50657265)

**「已证实与未证实」** 已证实：Hacker News 于 2026 年 11 月 26 日出现一篇题为「AMD-specific fork of llama.cpp」的帖子（发布者 julianlam），链接指向 devnull.land 上的介绍页；评论区多位开发者分别表示，自己为 AMD 显卡（gfx906 系列、MI100、R9700 等）维护或使用 llama.cpp 的优化分支。

尚未证实：该 fork 究竟改动了什么、支持哪些显卡与 ROCm 版本、有无可复现的性能数据、以何种许可证发布，现有材料均无法核实——介绍页正文未提供。评论中「32GB、约 1 TB/s 带宽的 gfx906 显卡仅约 200 美元」「R9700 单卡 prefill 2400 tok/s、decode 150 tok/s」等数字，是个人用户对各自项目的说法，并非对该 fork 的独立测试。

**「背景」** llama.cpp 是用 C/C++ 编写的开源本地大模型推理引擎，长期以 Nvidia 的 CUDA 为主要优化路径；在 AMD 显卡上它需要经由 ROCm/HIP 后端运行，针对新架构的适配和调优通常落后于 CUDA 版本。正因如此，社区常会针对特定 AMD 架构自行打补丁、分叉维护，这次被讨论的 llama-cpp-rdna-boosts 就是其中之一，面向 AMD 的 RDNA 系列显卡，帖子作者称其比原版 llama.cpp 表现更好。

**「为什么重要」** 对还在用 gfx906 这类老卡的开发者来说，专用分支目前是让 llama.cpp 跑得动、跑得快的主要途径，但这类优化是针对具体架构手写移植的：换成 Radeon AI PRO R9700 或 Strix Halo 等新硬件，就得另找对应的分支或工具集合，采用前应先确认其内核是否覆盖自己的 GPU 型号和量化格式。

**「后续看点」** 值得留意这个分支的改动是否会被合并回 llama.cpp 上游，以及作者是否会公布可复现的基准数据，让不同 AMD 卡上的加速比可以横向比较。

**「社区讨论」** 评论者 rao-v 认为，这正是围绕廉价 gfx906 老卡形成的一个小而活跃的优化生态，并贴出了自己的个人仓库作为例子；fiddlerwoaroof 也称自己把部分 Nvidia 内核移植到 ROCm 后性能明显提升，并表示已做过验证。另一位评论者 malicz 自述在单张 R9700 上达到 2400 tok/s 的 prefill 和 150 tok/s 的 decode，但这些数字均为个人自述，没有提供可复现的基准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://devnull.land/amd-specific-llama-cpp">AMD-specific fork of llama.cpp | devnull.land</a></li>
<li><a href="https://news.ycombinator.com/item?id=50657265">AMD - specific fork of llama . cpp | Hacker News</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#AMD`, `#LLM inference`, `#open-source`, `#GPU optimization`

---

## 芯片与算力

<a id="item-chips-compute-1"></a>
### [台积电 A14 的 0.9 版 PDK 可供设计导入](https://www.tomshardware.com/tech-industry/semiconductors/tsmcs-a14-1-4nm-class-node-is-ready-for-chip-design-boost-cells-promise-14-percent-performance-uplift-or-23-percent-power-cut-over-n2p) ⭐️ 8.0/10

台积电在 2026 欧洲 OIP 生态研讨会上宣布，A14（1.4 纳米级）制程的 0.9 版 PDK 与设计生态已可供客户设计导入；Cadence 和 Synopsys 也已在 Arm Cortex-A725 核上完成全流程 EDA 认证。台积电称，借助 NanoFlex Pro 标准单元架构和用于关键路径的 Boost Cells，A14 在相同功耗下比 N2P 提升 14% 性能，或在相同速度下降低 23% 总功耗；相对基线 N2P，台积电还宣称能效提升 50%、逻辑密度提升 23%。这些仍是厂商对比数据，尚无独立测量或量产芯片验证；A14 计划 2027 年下半年风险生产、2028 年下半年量产，A13 则计划 2029 年下半年进入高量产。西门子 EDA 未完成全部认证，其晶体管级 EM/IR 认证目标在 2026 年第四季度。

Tom&\#x27;s Hardware · 11月26日 13:00

**「已证实与未证实」** 已证实：Tom&\#x27;s Hardware 报道，TSMC 在 2026 欧洲 OIP 生态研讨会上宣布 A14 的 0.9 版 PDK 与设计生态可供设计导入，Cadence 与 Synopsys 已在 Arm Cortex-A725 上完成全流程认证，并给出 2027 年下半年风险生产、2028 年下半年量产的日程。
尚未证实：14% 性能提升、23% 功耗下降、50% 能效提升等数字均为 TSMC 对 N2P 的对比承诺，尚无独立测量或量产芯片数据；Siemens EDA 的晶体管级 EM/IR 认证仍在进行，目标 2026 年第四季度，其认证覆盖也少于另外两家。

**「背景」** 在芯片行业里，“1.4nm 级”只是代际命名，并非晶体管的实际物理尺寸，指的是比 2nm 级（N2P）更先进的一代工艺。PDK（process design kit，工艺设计套件）是代工厂交给客户的器件模型、设计规则与参数集合，版本推进到 0.9 通常被业界视为可用于正式设计的成熟度门槛；EDA（电子设计自动化）工具认证则是确认 Cadence、Synopsys 等厂商的布局布线、时序、功耗与签核工具能在这套规则下跑通全流程。台积电已在 N2/N2P 上引入纳米片晶体管，A14 改用第二代纳米片与 NanoFlex Pro 标准单元架构，这也是本次 Boost Cell 与低功耗单元能起作用的基础。

**「为什么重要」** 对计划采用 A14 的芯片设计团队来说，Cadence 与 Synopsys 的全流程认证意味着可以用两条已验证的工具链启动设计；依赖 Siemens EDA 晶体管级 EM/IR 的团队则要等到 2026 年第四季度。A14 要到 2028 年下半年才量产，从设计导入到可出货仍有约两年，早期项目需要把工具与 IP 风险前置处理。

**「后续看点」** 首要节点是 Siemens EDA 的 A14 晶体管级 EM/IR 认证是否在 2026 年第四季度按期完成；随后看 A14 能否按计划在 2027 年下半年进入风险生产。

**标签**: `#TSMC`, `#A14`, `#1.4nm-class`, `#semiconductor manufacturing`, `#EDA`

---

<a id="item-chips-compute-2"></a>
### [得州解冻 1,800 多个数据中心项目，《金融时报》报道](https://www.tomshardware.com/tech-industry/data-centers/texas-lifts-freeze-on-1-800-data-center-projects-in-greg-abbott-u-turn-companies-rush-for-permits-before-gina-hinojosas-january-arrival) ⭐️ 7.0/10

得州在 8 月暂停 1,800 多个数据中心项目审批后，已根据州长格雷格·阿博特办公室的新指令恢复审批；《金融时报》报道称，当时受冻结影响的是总计 474 吉瓦的新增电力申请。阿博特办公室表示，恢复审批是因为得州电力可靠性委员会（ERCOT）已完成对数据中心如何影响当地社区的信息收集。由于当选州长吉娜·希诺霍萨将于 1 月就职并已承诺限制新建数据中心，开发商正赶在她上任前争取许可；但报道指出，新增电力申请的处理预计不会很快。

Tom&\#x27;s Hardware · 11月27日 11:00

**「已证实与未证实」** 已证实：Tom&\#x27;s Hardware 援引《金融时报》报道，得州已恢复审批此前在 8 月被冻结的 1800 多个数据中心项目，受影响的新增用电申请为 474 吉瓦；州长格雷格·阿博特办公室发出新指令，并确认得州电力可靠性委员会（ERCOT）已完成其所需的、关于数据中心如何影响当地社区的信息收集。ZeroHedge 援引得州环境质量委员会（TCEQ）在 11 月恢复正常许可审查后称，解冻后首个获批的许可似乎发给了 SpaceX 位于 Starbase、价值 240 亿美元的项目（原始报道为 Politico）。

尚未证实：恢复审批的具体条款、时间表和适用范围，以及“开发商抢在 1 月新州长 Gina Hinojosa 上任前获批”的说法，均来自《金融时报》的转述，且没有原始监管文件佐证；Hinojosa 承诺限制新数据中心建设也只是其公开表态，具体政策尚不清楚。SpaceX 获得首个许可一事目前仅有 Politico 一家报道。此外，关于是哪家机构在推进解冻，现有来源说法不一致：Tom&\#x27;s Hardware 将恢复审批归因于 ERCOT 完成调查，ZeroHedge 则称 TCEQ 已恢复正常审查；474 吉瓦这一数字来自州政府审计的统计，尚未经过独立核实。

**「背景」** 这轮冻结始于 2026 年 8 月：雅培办公室以电网承受能力和居民生活为由暂停数据中心项目审批，涉及 1,800 多个项目、合计 474 吉瓦的用电申请；10 月州里又暂停 17 个施工许可，并关闭了一个仍在自动放行许可的在线门户。随后，负责州电网的得州电力可靠性委员会（ERCOT）被要求评估数据中心对当地社区的影响，雅培办公室现在称其已完成信息收集。另一个背景是，当选州长 Gina Hinojosa 在 11 月胜选，竞选时主张在州议会通过社区保护措施前继续暂停新建数据中心，并将于明年 1 月上任。

**「为什么重要」** 对数据中心开发商而言，实际动作是在希诺霍萨 1 月就职前拿到许可，否则可能面临更严的审批环境；而 ERCOT 并网处理缓慢，已促使部分项目转向自建发电，利用得州丰富的天然气资源。自建电源能绕开电网排队，但会把排放和当地社区反对带到项目现场。

**「后续看点」** 希诺霍萨 1 月就职后是否收紧数据中心审批，以及 ERCOT 恢复受理后实际处理并网申请的速度；10 月被关闭的自动审批门户是否重新开放也值得关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.zerohedge.com/energy/texas-first-data-center-permit-after-freeze-went-spacexs-24b-starbase-project">Texas &#x27; First Data - Center Permit After The Freeze Went... | ZeroHedge</a></li>
<li><a href="https://www.ibtimes.co.uk/texas-halts-data-centre-grid-connections-ai-energy-surge-1813892">Texas &#x27;AI Epicentre&#x27; Pauses Data Center Connections as ERCOT ...</a></li>
<li><a href="https://www.texastribune.org/2026/11/04/data-center-texas-pause-gina-hinojosa-governor-policies/">Under Hinojosa, Texas data center approvals could stay paused</a></li>
<li><a href="https://www.usatoday.com/story/news/2026/11/06/hinojosa-texas-data-centers-pause-what-to-know/92641237007/">Texas Governor-elect Hinojosa calls for data center pause</a></li>

</ul>
</details>

**标签**: `#data centers`, `#Texas`, `#power grid`, `#permitting`, `#capacity`

---

<a id="item-chips-compute-3"></a>
### [磷化铟供应链吃紧，AI 光互连面临材料瓶颈](https://www.tomshardware.com/tech-industry/photonics/inside-the-indium-phosphide-squeeze-and-the-optical-boom-inp-remains-tightly-constrained-as-the-demand-from-ai-puts-the-entire-supply-chain-under-pressure) ⭐️ 7.0/10

随着 AI 数据中心从铜缆转向光互连，磷化铟（InP）这种用于制造激光器、调制器和光探测器的关键材料正成为供应链瓶颈。据 Tom&\#x27;s Hardware 梳理，住友电工和 AXT 合计占全球 InP 衬底产能近 80%，JX Advanced Metals 约占 10%；AXT 多数衬底在中国生产，出口需许可证，而中国约占全球精炼铟产量的 70%。Lumentum 首席执行官迈克尔·赫尔斯顿在 7 月表示，该公司 InP 晶圆厂出货比客户需求低 30% 以上，Coherent 也把 InP 产能称为其收发器业务的“首要约束”。英伟达已分别向 Lumentum 和 Coherent 投资 20 亿美元，并附带数十亿美元采购承诺和未来产能权利，但扩建 InP 衬底和激光器产能仍需数年。

Tom&\#x27;s Hardware · 11月26日 16:00

**「已证实与未证实」** 已证实：Tom&\#x27;s Hardware 的报道确认了 InP 衬底产能集中度（住友电工与 AXT 合计近 80%、JX 约 10%）、AXT 中国产线需出口许可，以及英伟达对 Lumentum 和 Coherent 各 20 亿美元的投资。
尚未证实：短缺的量化规模与持续时间、英伟达投资所附采购承诺和产能权利的具体条款均未披露；Lumentum 的 30% 出货缺口和 Coherent 的“首要约束”说法来自公司高管，未经独立核实。

**「背景」** 硅光子本身不发光：硅是间接带隙材料，可以导光、分光和调制，但光源通常要依赖 III-V 族材料；InP 因约 1.34 eV 的直接带隙，长期被用作激光器、调制器和光探测器等有源光器件的平台。此前 InP 供应链规模小但相对稳定，主要服务电信和国防；随着 AI 数据中心把铜互连推到极限，光模块、近封装光学和共封装光学放大了对这条小供应链的需求。

**「为什么重要」** 对 AI 数据中心运营商和光模块厂商来说，InP 衬底和激光器产能已成为扩产计划中的硬性约束；英伟达通过投资为 Lumentum 和 Coherent 锁定未来产能，没有类似采购承诺的买家可能面临更长交期和更紧张的供应分配。

**「后续看点」** 接下来关注 Lumentum 和 Coherent 的下一份财报及产能扩张披露，以及 AXT 在中国出口许可方面的进展；这些信息将检验供应缺口是在收窄还是扩大。

**标签**: `#indium phosphide`, `#optical interconnect`, `#AI data centers`, `#semiconductor supply chain`, `#photonics`

---

## 电动车与新能源

<a id="item-ev-energy-1"></a>
### [田湾 8 号机组完成热试并接收首炉核燃料](https://www.world-nuclear-news.org/articles/Tianwan-moving-step-closer-becoming-worlds-biggest-nuclear-power-plant) ⭐️ 8.0/10

世界核新闻（World Nuclear News）报道，中国田湾核电站 8 号机组已完成热试（对反应堆系统和设备在接近运行工况下的整体测试），并接收了首炉核燃料。该报道称，待厂址内全部八台机组投运后，田湾将成为全球装机规模最大的核电站。报道没有给出 8 号机组首次临界、并网或商运的时间表，也没有提供全厂总装机容量数字，因此“全球最大”目前仍是基于全部机组投运这一前提的描述，而不是已实现的状态。

World Nuclear News · 11月26日 14:33

**「已证实与未证实」** 已证实：世界核新闻（World Nuclear News）报道，田湾 8 号机组已完成热试，首炉核燃料已运抵现场。
尚未证实：8 号机组何时首次临界、并网发电和投入商业运行；全厂八台机组的总装机容量；“全部投运后成为全球最大核电站”这一定性判断，报道未给出与其他核电站的容量对比数据。

**「背景」** 田湾核电站位于江苏连云港黄海沿岸，规划建设 8 台机组；其中 7、8 号机组采用俄罗斯设计的 VVER-1200 第三代压水堆，中俄在 2018 年 6 月签署了这两台机组的建设协议。热试是在首次装料前用加热的一回路冷却剂检验系统密封、泵阀和控制设备，热试通过后才进入装料阶段。此前 7 号机组已开始首次装料，8 号机组此次完成热试并收到首批燃料，意味着该扩建工程朝整体投运又推进了一步。

**「后续看点」** 下一步可关注田湾 8 号机组首次临界与并网发电的官方通报，以及全部八台机组投运后公布的全厂装机容量数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.world-nuclear-news.org/articles/Tianwan-moving-step-closer-becoming-worlds-biggest-nuclear-power-plant">Tianwan moves step closer to becoming... - World Nuclear News</a></li>
<li><a href="https://interestingengineering.com/energy/china-loads-first-fuel-into-new-1-2gw-reactor-at-worlds-largest-nuclear-plant">China loads first fuel into new 1.2GW reactor at Tianwan nuclear plant</a></li>

</ul>
</details>

**标签**: `#nuclear power`, `#Tianwan`, `#China energy`, `#reactor commissioning`, `#clean energy`

---

<a id="item-ev-energy-2"></a>
### [IONNA 加州启用 22 枪充电站，并向特斯拉开放自动充电认证](https://www.electrive.com/2026/11/26/ionna-opens-22-bay-charging-hub-in-california-and-adds-tesla-autocharge/) ⭐️ 7.0/10

IONNA 在美国加利福尼亚州威斯敏斯特（Westminster）启用新的旗舰充电站，设有 22 个充电车位，单枪峰值功率最高可达 400 kW。据 electrive 报道，该站开业的同时，IONNA 将自动充电认证（即插即充，车辆自行完成身份识别与计费，无需刷卡或打开 App）扩展到特斯拉车型。支持 Stellantis 旗下品牌车型的同类功能计划于 12 月跟进。报道未给出该站的充电价格、可用率或独立实测的功率数据。

Electrive · 11月26日 18:30

**「已证实与未证实」** 已证实：据 electrive 报道，IONNA 在加州威斯敏斯特开设了含 22 个车位、峰值功率最高 400 kW 的充电站，并将自动充电认证扩展至特斯拉车辆。
尚未证实：具体支持哪些特斯拉车型、需要何种软件版本，以及 Stellantis 品牌 12 月上线的确切日期，目前仅有 IONNA 一方的说法；充电价格、站点实际可用率与独立测试的持续功率均未披露。

**「背景」** IONNA 是一家美国电动汽车快充网络运营商。Autocharge（自动充电认证）指车辆插枪后由车辆与充电桩自动完成身份识别和计费授权，车主无需再打开 App 或刷卡；某一车型能否使用该功能，取决于充电网络与车企之间的兼容支持。

**「为什么重要」** 对特斯拉车主而言，这意味着在 IONNA 站点可以跳过扫码或刷卡步骤，插枪即自动识别并计费，减少首次使用时的认证失败；Stellantis 品牌车主则要等到 12 月才能获得同样体验。实际操作前值得先确认自己的车型与车机软件是否在支持列表内，因为报道没有说明兼容范围。

**「后续看点」** 关注 12 月 IONNA 是否如期为 Stellantis 旗下品牌车型开放自动充电认证，以及届时公布的具体品牌与车型清单。

**标签**: `#IONNA`, `#EV charging infrastructure`, `#Tesla Autocharge`, `#California`, `#400 kW charging`

---

<a id="item-ev-energy-3"></a>
### [西班牙电动车补贴预算耗尽，Auto+ 短期内不再追加](https://www.electrive.com/2026/11/26/budget-exhausted-spain-cuts-purchase-subsidies-for-electric-cars/) ⭐️ 7.0/10

西班牙面向私人消费者的 Auto+ 电动车购置补贴预算已经用尽：政府为纯电动车和插电式混合动力车划拨的 3.5 亿欧元在很短时间内分配完毕。据 electrive 报道，由于西班牙议会选举临近，这笔资金在可预见的未来不会补充。这意味着尚未购车的私人买家眼下不能再指望这项补贴，具体何时恢复取决于选举后的政策安排。

Electrive · 11月26日 11:30

**「已证实与未证实」** 已证实：electrive 报道，西班牙 Auto+ 面向私人的补贴额度已耗尽，政府为该计划投入的 3.5 亿欧元在短期内分配完毕，且短期内不会补充。
尚未证实：报道未援引政府原始文件，未说明剩余申请如何处理、单车补贴金额，以及选举后是否推出替代计划。

**「背景」** Auto+ 是西班牙政府面向私人购车者的直接补贴计划，对纯电动车和插电式混合动力车发放购车款补贴，以缩小它们与燃油车之间的前期购置价差。该计划按固定预算额度运作：资金池用尽即停止受理，而不是一项可无限续期的长期权益。因此当本轮额度在短时间内被申请完毕，补贴便自然中断。

**「为什么重要」** 对西班牙的私人买家而言，购车成本将立即上升——Auto+ 的资金已分配完毕，短期内也没有新的补贴可以申请。经销商和车企需要按没有补贴的价格来规划年底及明年的订单；打算购车的人应把补贴从预算中剔除，并留意选举后是否出现新的补贴计划。

**「后续看点」** 西班牙议会选举后，新一届政府是否会为电动车购置补贴重新拨款，以及 Auto+ 是否公布资金执行明细或收尾安排。

**标签**: `#Spain`, `#EV purchase subsidies`, `#policy change`, `#EV market`, `#Auto+ program`

---

<a id="item-ev-energy-4"></a>
### [三菱日联银行为日本两座 90MW 储能项目放款，融资条款挂钩通胀调整](https://www.pv-magazine.com/2026/11/27/japan-battery-financing-adapts-to-inflation-linked-capacity-contracts/) ⭐️ 7.0/10

HEXA Energy Services 表示，三菱日联银行（MUFG Bank）已就日本北部和南部两座电网级电池储能项目完成项目融资协议下的首次贷款放款，两项目并网容量合计 90 MW，分别位于北海道美呗市和熊本县熊本市，均在日本 2023 财年长期脱碳电力拍卖中获得容量合同。HEXA 称这批融资解决了“日本国内没有先例的融资要求”，条款反映与通胀和利率变化挂钩的合同价格调整；三菱日联银行也确认参与了这一新引入的价格调整机制相关安排。HEXA 首席执行官水田洋一郎称，首次放款在约两个月内完成。公司未披露贷款金额、期限，以及两个项目的兆瓦时储能容量。

pv magazine · 11月27日 11:15

**「已证实与未证实」** 已证实：HEXA Energy Services 宣布三菱日联银行已为北海道美呗和熊本两座合计 90 MW 并网容量的储能项目完成首次放款，三菱日联银行确认参与并处理了长期脱碳电力拍卖新引入的合同价格调整机制相关融资安排；两项目在 2023 财年拍卖中中标。
尚未证实：贷款金额、期限和两个项目的兆瓦时容量均由公司以未披露带过；通胀与利率调整对实际融资成本的影响幅度没有独立数据；放款不等于项目已建成并网，投运时间表未见说明。

**「背景」** 日本的长期脱碳电源拍卖（LTDA）于 2023 财年启动，向中标项目提供为期 20 年的容量支付，以缓解电池储能等低碳电源项目的前期投资压力；2023 财年那一轮拍卖分配了约 1.09 GW 储能容量，本次获得融资的两个项目正是该轮中标者。该机制过去以固定的长期容量支付为基础，而 MUFG 此次处理的是拍卖新引入的合同价格调整条款——合同价格随通胀和利率变化，这也是银行所称需要为这两个项目单独设计融资结构的原因。

**「为什么重要」** 对日本储能开发商而言，把容量合同价格随通胀和利率调整的条款纳入项目融资，是让贷款方接受长期固定收费合同贬值风险的关键一步，HEXA 称这在日本没有先例，意味着后续拍卖中标项目可能沿用类似结构。但并网仍是硬约束：据文中数据，2025 年底约有 172 GW 电网级电池容量停留在接入研究阶段，实际并网仅约 0.64 GW，融资落地并不保证项目按期投运。

**「后续看点」** HEXA 计划在 2026 财年为富山县小矢部市的电池项目安排项目融资，该公司还在 2025 财年拍卖轮次中拿下两个电池项目，这些项目能否复制同样的通胀挂钩融资结构值得关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://shulman-advisory.com/japan-doubles-ltda-price-cap-ahead-of-3rd-auction-to-counter-inflation-pressures/">Japan Doubles LTDA Price Cap Ahead of 3rd Auction to Counter ...</a></li>
<li><a href="https://www.nishimura.com/sites/default/files/newsletters/file/natural_resources_energy_241224_en.pdf">Long-Term Decarbonization Power Source Auctions in Japan ...</a></li>

</ul>
</details>

**标签**: `#Japan`, `#grid-scale battery storage`, `#project finance`, `#capacity contracts`, `#MUFG`

---

<a id="item-ev-energy-5"></a>
### [中国光伏累计装机达 1.33 太瓦，江苏公布 2027 年竞价框架](https://www.pv-magazine.com/2026/11/27/chinese-pv-industry-brief-china-hits-1-33-tw-of-cumulative-solar-capacity/) ⭐️ 7.0/10

中国国家能源局称，截至 2026 年 10 月底，中国光伏累计装机约 1.33 太瓦，同比增长 16.3%；10 月新增 12.86 吉瓦，环比下降 5.7%，前 10 个月新增约 123.69 吉瓦。江苏省发改委公布 2027 年新能源机制电价竞价框架，初始电量 13 太瓦时，其中 12.5 太瓦时分配给光伏和陆上风电，报价区间为 0.200—0.391 元/千瓦时，结算期 10 年。对于新获批或登记备案的公用事业规模项目，可享受机制电价结算的电量将根据实际并网利用小时数相对当地同类项目平均水平的比例进行调整。

pv magazine · 11月27日 11:06

**「已证实与未证实」** 已证实：国家能源局数据显示，截至 2026 年 10 月底，中国光伏累计装机约 1.33 太瓦，同比增长 16.3%，10 月新增 12.86 吉瓦；江苏省发改委已公布 2027 年机制电价竞价框架，初始电量为 13 太瓦时，报价区间为 0.200—0.391 元/千瓦时，结算期 10 年。
尚未证实：竞价最终出清价格、可结算电量分配和项目中标结果，以及拍卖的具体时间表；该框架只规定了规则，尚未给出这些结果。

**「背景」** “机制电价”竞拍是各省为新建可再生能源项目划定一笔可享受机制电价结算的电量、一个报价区间和结算年限的安排：江苏此次拿出 13 太瓦时电量（其中 12.5 太瓦时给光伏与陆上风电），报价区间为 0.200—0.391 元/千瓦时，结算期 10 年。江苏不是首个启动 2027 年竞拍的省份——据 Sxcoal 报道，广西已于 2026 年 9 月公布 2027 年竞价方案，报价上限 0.36 元/千瓦时、下限 0.15 元/千瓦时；辽宁则在 11 月公布 2027 年竞价结果，光伏机制电价定为 0.20 元/千瓦时，恰在江苏此次报价区间的下限。

**「为什么重要」** 对江苏新建光伏和陆上风电开发商而言，机制电价可结算电量与实际并网利用小时数挂钩，因此同一报价下的收入会随项目出力表现分化；0.200—0.391 元/千瓦时的报价区间和 10 年结算期是可直接用于收益测算的硬性约束。

**「后续看点」** 下一期国家能源局月度装机数据将检验 10 月新增环比下降 5.7%是否延续；江苏 2027 年竞价的实际申报、出清价格和项目分配结果也值得跟踪。位于浙江的永杰铝业（Yongjie Aluminum）配套 72 兆瓦光伏与 30 兆瓦/75 兆瓦时储能项目计划 12 月 28 日投运，可作为绿电直供模式的运行观察点。

<details><summary>参考链接</summary>
<ul>
<li>Guangxi launches 2027 renewable energy mechanism power price auction - Sxcoal</li>
<li>Liaoning Announces 2027 Renewable Energy Bidding Results</li>

</ul>
</details>

**标签**: `#China solar`, `#solar capacity`, `#renewable energy policy`, `#Jiangsu auction`, `#clean energy`

---

<a id="item-ev-energy-6"></a>
### [通威签署罗马尼亚 Dama Solar 846 MW 组件供应协议](https://www.pv-magazine.com/2026/11/27/tongwei-signs-846-mw-module-deal-for-romanias-dama-solar-project/) ⭐️ 7.0/10

通威与 Rezolv Energy 签署协议，将为罗马尼亚 Arad 县的 Dama Solar 项目供应 846 MW 的 TNC 3.0 组件。项目规划装机容量 1.36 GWp，投运后预计年发电约 1,800 GWh，被称为欧洲最大的单体太阳能电站之一。报道显示，首批组件已从通威南通工厂发运，交付开始；但项目本身尚未投运，报道未披露组件价格或投运日期。

pv magazine · 11月27日 10:00

**「已证实与未证实」** 已证实：据 pv magazine 报道，通威与 Rezolv Energy 签署 846 MW TNC 3.0 组件供应协议，用于罗马尼亚 Arad 县规划中的 1.36 GWp Dama Solar 项目；首批组件已从南通发运。
尚未证实：项目投运时间、最终年发电量（报道为约 1,800 GWh 的预期值）、组件价格，以及 846 MW 组件能否全部按期交付，均无独立信息或合同细节支持。

**「背景」** Dama Solar 由 Actis 于 2022 年创立并控股的独立可再生能源开发商 Rezolv Energy 开发，厂址位于罗马尼亚西部阿拉德县（Arad County），土地和并网条件已落实，目前处于建设前的最后开发阶段。欧洲投资银行（EIB）在 2026 年 9 月 30 日的新闻稿中宣布为这个约 1.3 GWp 级项目提供 1 亿欧元融资，项目将接入罗马尼亚高压电网。

**「为什么重要」** 对 Rezolv Energy 而言，协议锁定了 Dama Solar 的组件供应，首批已经发运；但在项目完成建设、并网和投运前，每年约 1,800 GWh 的发电量仍只是预期，不能视为已实现的清洁电力供应。

**「后续看点」** 关注 Dama Solar 的并网或投运时间表，以及通威 846 MW 组件交付完成的进度；报道未给出具体日期。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rezolv.energy/project/dama-solar/">Dama Solar - Rezolv Energy</a></li>
<li><a href="https://www.eib.org/en/press/all/2026-324-eib-powers-europe-s-solar-future-with-eur100-million-for-romania-s-1-3-gwp-dama-solar">EIB powers Europe’s solar future with €100 million for ...</a></li>

</ul>
</details>

**标签**: `#solar`, `#Romania`, `#Tongwei`, `#Rezolv Energy`, `#utility-scale PV`

---

<a id="item-ev-energy-7"></a>
### [港科大用跨界面工程做出 27.04%效率钙钛矿电池](https://www.pv-magazine.com/2026/11/27/hong-kong-researchers-build-27-04-efficient-perovskite-solar-cell-via-trans-interface-engineering/) ⭐️ 7.0/10

香港科技大学（HKUST）研究团队在《Nature Photonics》发表论文，报告了一种称为“跨界面工程”（trans-interface engineering，TIE）的方法，并制出光电转换效率达 27.04%的钙钛矿太阳能电池，认证效率为 26.67%，但论文未披露认证机构名称。与常见的做法——在钙钛矿吸收层与电荷传输层之间铺一层平面中间层——不同，TIE 在两层内分别掺入三官能和单官能有机连接分子，再用由偶氮二异丁腈（AIBN）产生的氰基异丙基自由基引发聚合，使连接分子在两层之间形成垂直、共价结合的“纳米连接链”，穿透两个界面。研究称这种做法在保持电荷传输的同时抑制了界面机械失效。在最大功率点跟踪与一个太阳光照条件下，92%的受测器件 T80 寿命（效率降至初始值 80%所需时间）达到至少 1,400 小时；团队认为这一比例同时说明器件间的可复现性有所提高。上述结果均为实验室规模的单个电池数据，未涉及组件放大或户外实证。

pv magazine · 11月27日 09:57

**「已证实与未证实」** 已证实：香港科技大学团队在《Nature Photonics》发表论文（2026 年 11 月第 20 卷第 11 期封面文章），其转界面工程（TIE）制备的钙钛矿电池获得 26.67%的认证效率，最佳器件效率为 27.04%；在最大功率点跟踪与一个太阳光照条件下，92%的受测器件 T80 寿命不低于 1,400 小时（T80 指效率降至初始值 80%所需时间）。以上数据来自论文本身及 HKUST 的新闻稿。

尚未证实：认证效率由哪家机构出具，报道未披露；27.04%为实验室最佳器件数据，并非独立认证值；T80 结果全部来自实验室加速测试，尚无户外实证或组件级放大数据；论文所称“可扩展至其他多层光电器件”目前仅为作者判断。

**「背景」** 钙钛矿太阳能电池用溶液法涂布的钙钛矿吸光层替代硅片，实验室小面积效率已逼近晶硅，但吸光层与电荷传输层之间的界面在温度循环和机械应力下容易分层、开裂，是其走向量产的主要障碍之一。此前的界面工程多靠在两层之间加一层平面钝化膜，难以同时兼顾电荷传输与机械强度。效率数据方面，27.04% 属实验室小面积器件水平，论文另给出 26.67% 的认证值，与商用组件效率不属同一量级；T80 指效率衰减到初始值 80% 所经历的时间。

**「为什么重要」** 对钙钛矿研发团队来说，这组数据中更值得关注的是可复现性，而不是 27.04%的冠军效率：92%的器件都能达到 1,400 小时的 T80 寿命，意味着该界面方案可能成为筛选取代平面中间层的候选工艺。但要提醒的是，认证机构未公开，26.67%的认证值与 27.04%的实验室值也不宜与其他团队的结果直接横向比较，评估时应先确认测试条件与认证来源。

**「后续看点」** 接下来可留意研究团队是否公开认证机构名称，以及在更大面积器件或组件上能否复现同样的 T80 寿命数据；这两项是判断该界面工艺能否走出实验室的可核查指标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41566-026-02007-w">Trans-interface engineering for reliable perovskite ... - Nature</a></li>
<li><a href="https://hkust.edu.hk/news/hkust-pioneers-trans-interface-engineering-boost-perovskite-solar-cell-efficiency-and">HKUST Pioneers Trans-Interface Engineering to Boost ...</a></li>

</ul>
</details>

**标签**: `#perovskite solar cells`, `#solar PV`, `#interface engineering`, `#HKUST`, `#clean energy`

---

## 科技产业与政策

<a id="item-tech-industry-1"></a>
### [英国 FCA 拟要求 DeFi 平台取得授权，立场严于美欧，《金融时报》报道](https://www.techmeme.com/261126/p17#a261126p17) ⭐️ 7.0/10

《金融时报》报道，英国金融行为监管局（FCA）计划要求去中心化金融（DeFi）平台取得授权后才能运营，并把“缺乏消费者保护”和币安（Binance）涉及 63 亿美元的被盗事件列为收紧监管的理由。报道称，这一立场比美国与欧盟现行做法更严格。目前这只是一项已表态的监管意图，报道未给出拟议规则的适用范围、时间表或条文细节，也未说明非托管的纯链上协议是否会被纳入。

Techmeme · 11月26日 13:10

**「已证实与未证实」** 已证实：据《金融时报》报道（经 Techmeme 转述），FCA 表示计划要求 DeFi 平台取得授权，并以消费者保护不足和币安被盗事件作为理由。
尚未证实：报道所引的 63 亿美元被盗金额、FCA 与美国和欧盟做法的具体比较，以及规则的适用范围、生效时间和是否已有正式咨询文件，目前都只有这一家媒体的转述，尚无 FCA 官方文件或公开征求意见稿佐证。

**「背景」** DeFi（去中心化金融）指在公共区块链上由智能合约自动执行、不依赖银行或券商等中心化中介的借贷、交易和做市服务，其特点是往往没有一个持牌实体可以为消费者损失负责，这也是监管机构争论的焦点。据 Forklog 和《金融时报》报道，FCA 提到的依据是 10 月 Binance 遭遇的 63 亿美元窃案：与朝鲜有关的黑客将赃款通过包括 THORChain 在内的去中心化协议转移洗白。AI Daily Radar 11 月 23 日的日报曾报道，美国司法部正寻求没收从 Binance 窃取、与朝鲜关联的逾 10 亿美元加密货币，那是同一案件的后续司法动作，而本次是英国监管方首次以此案为由提出对 DeFi 平台发牌。

**「为什么重要」** 若该计划落地，面向英国零售用户提供借贷、交易等服务的 DeFi 项目将需要向 FCA 申请授权才能合法运营，这与报道描述的美欧更宽松路径不同，跨境项目可能要为英国单独设计合规方案。关键的不确定点是“DeFi 平台”如何界定，尤其是无托管、无运营主体的协议是否被涵盖，这决定了哪些团队实际需要行动。

**「后续看点」** 关注 FCA 是否发布正式的咨询文件或政策声明，以及其中对“DeFi 平台”的定义是否包含非托管协议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techmeme.com/261123/p30#a261123p30">2026-11-23 — DOJ seeks forfeiture of $1B+ stolen from Binance, Bloomberg reports</a></li>
<li><a href="https://forklog.com/en/uk-to-tighten-regulations-for-defi-platforms-following-binance-hack/">UK to Tighten Regulations for DeFi Platforms Following Binance Hack</a></li>

</ul>
</details>

**标签**: `#UK FCA`, `#DeFi regulation`, `#crypto policy`, `#Binance hack`, `#financial regulation`

---

