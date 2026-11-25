# AI Daily Radar - 2026-11-25

> We screened 306 stories from the past day and kept the 23 worth your time.

---

**AI**
1. [OpenAI says GPT-6.2 can design protein minibinders, with lab binding evidence](#item-ai-news-1) ⭐️ 8.0/10
2. [Amazon: hackers&\#x27; AI agents found and exploited a zero-day with minimal human input](#item-ai-news-2) ⭐️ 8.0/10
3. [Sandboxed models can communicate via inference servers, LessWrong analysis claims](#item-ai-news-3) ⭐️ 7.0/10
4. [Anthropic gave a company 24 hours to disprove distillation, poster says](#item-ai-news-4) ⭐️ 7.0/10
5. [Insiders say OpenAI and Anthropic frontier models have outgrown safety controls, Axios reports](#item-ai-news-5) ⭐️ 7.0/10
6. [Meta and Amazon discuss linking Muse AI agent, ending Amazon block, Fortune reports](#item-ai-news-6) ⭐️ 7.0/10

**Chips &amp; Computing**
1. [Shared CXL memory test finds 3–5µs software lock overhead](#item-chips-compute-1) ⭐️ 7.0/10

**Robots &amp; Self-Driving**
1. [Ukrainian naval drones sink Russian corvette Merkury in Benghazi](#item-robotics-autonomy-1) ⭐️ 8.0/10
2. [Nuro starts driverless robotaxi testing in Bay Area as public launch slips to 2027](#item-robotics-autonomy-2) ⭐️ 8.0/10
3. [SoftBank completes acquisition of Marc Raibert&\#x27;s RAI Institute](#item-robotics-autonomy-3) ⭐️ 7.0/10

**EVs &amp; Energy**
1. [EU sets 200-day quota capping Chinese hybrid car imports at 191,780](#item-ev-energy-1) ⭐️ 8.0/10
2. [BYD launches third-gen Tang EV, a five-seat SUV with dual 30-inch screens under $30,000](#item-ev-energy-2) ⭐️ 7.0/10
3. [VW and Elli price V2G wallbox at €1,995 for December launch](#item-ev-energy-3) ⭐️ 7.0/10
4. [Switzerland awards 32 truck charging sites to Fastned, Obornes and Milence](#item-ev-energy-4) ⭐️ 7.0/10
5. [India clears first-criticality step for Rajasthan 8 as Kaiga 1 restarts](#item-ev-energy-5) ⭐️ 7.0/10

**Space**
1. [Shenzhou-24 carries first Pakistani astronaut to Tiangong](#item-space-1) ⭐️ 8.0/10

**Tech Industry &amp; Policy**
1. [Australia passes Digital Duty of Care Act, exposing tech giants to multibillion-dollar fines](#item-tech-industry-1) ⭐️ 9.0/10
2. [Prosecutors allege hundreds of recordings in OpenAI bugging case](#item-tech-industry-2) ⭐️ 8.0/10
3. [Flipkart CEO Krishnamurthy to exit Dec. 4; CTO interim, Bloomberg reports](#item-tech-industry-3) ⭐️ 7.0/10
4. [Huawei says HarmonyOS passes 100 million installations](#item-tech-industry-4) ⭐️ 7.0/10
5. [Research links a TikTok mass-shooter &\#x27;true crime&\#x27; network to rising attacks, WIRED reports](#item-tech-industry-5) ⭐️ 7.0/10
6. [FISA Section 702 reauthorization may ride on the defense bill](#item-tech-industry-6) ⭐️ 7.0/10
7. [DOJ announces record anti-scam sweep: 800+ charged, 2,200 trafficking victims freed](#item-tech-industry-7) ⭐️ 7.0/10

---

## AI

<a id="item-ai-news-1"></a>
### [OpenAI says GPT-6.2 can design protein minibinders, with lab binding evidence](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/) ⭐️ 8.0/10

OpenAI reports that its GPT-6 models, specifically GPT-6.2, can design protein minibinders — small binding proteins — when given the three-dimensional structures of target proteins and the intended attachment site. According to OpenAI, the model wrote code to generate 3D designs without using specialized protein AI models, and laboratory tests found evidence of binding across five targets. The end-to-end workflow was not fully general-purpose, however: OpenAI says a specialized model called SolubleMPNN was used to suggest amino acid sequences for the designs, and other specialized protein models helped select candidates predicted to fold as intended and bind at the correct site. The report describes a research result, not a product or a service users can access.

Hacker News · acossta · Nov 24, 21:02 · [Discussion](https://news.ycombinator.com/item?id=50634658)

**Verified and unconfirmed:** Verified: OpenAI states that GPT-6.2 generated 3D minibinder designs by writing code, and that its own lab tests found evidence of binding for five targets. Not yet confirmed: how much of the design work was genuinely done by GPT-6.2 rather than the specialized models — SolubleMPNN produced the sequences and other tools filtered candidates — and OpenAI&\#x27;s own account supplies no binding affinities, success rates, comparison with existing design methods, peer review, or independent replication.

**Background:** OpenAI&\#x27;s GPT-6.2 family, the flagship Astra and the lighter Sol, arrived in mid-November 2026 with a 1.05 million-token context window and text-and-image input but text-only output, as AI Daily Radar&\#x27;s November 19 digest reported; that earlier report covered benchmark scores and mixed early user reviews, not scientific applications. Protein design has conventionally split the job in two: a generative model proposes a three-dimensional backbone, then an inverse-folding model such as SolubleMPNN, part of the ProteinMPNN family, reads that fixed backbone and suggests amino acid sequences predicted to fold into it. That division of labor is the backdrop for the new claim, since OpenAI says GPT-6.2 wrote code to produce the 3D designs itself and then handed sequence suggestion and candidate filtering to SolubleMPNN and other specialized protein models.

**Why it matters:** For protein designers, the interesting claim is architectural rather than a new model: a general reasoning model can write the design code and act as an orchestration layer over specialized tools like SolubleMPNN, which still handle sequence generation and filtering. Teams evaluating this should treat the five-target binding result as a vendor-reported demonstration and keep existing physics- and ML-based design pipelines in place until success rates per target are published and independently reproduced.

**Community discussion:** Commenters pushed back on the framing that this goes &quot;beyond specialized models&quot;: one reader asked what GPT-6.2 actually designed, since SolubleMPNN supplied the amino acid sequences and other protein models did the selection, and another described the model more modestly as a glue layer between specialized tools. A commenter who says they did a PhD at the Baker lab called the direction expected — fusing language models with protein design natively, as has been done with images — while treating the current result as early.

<details><summary>References</summary>
<ul>
<li><a href="http://www.geekpark.net/news/374175">2026-11-19 — OpenAI 发布 GPT-6.2 Astra 与 Sol，跑分领先但实测口碑分化</a></li>
<li><a href="https://docs.openprotein.ai/models/proteinmpnn/solublempnn/">SolubleMPNN - OpenProtein.AI docs</a></li>

</ul>
</details>

**Tags**: `#AI protein design`, `#GPT-6`, `#OpenAI`, `#AI for science`, `#minibinders`

---

<a id="item-ai-news-2"></a>
### [Amazon: hackers&\#x27; AI agents found and exploited a zero-day with minimal human input](https://arstechnica.com/security/2026/11/amazon-says-hackers-ai-agents-found-and-exploited-0-day-with-little-human-input/) ⭐️ 8.0/10

Amazon reported that AI agents running on Cairn, an open-source AI penetration-testing framework, discovered and exploited a zero-day vulnerability in an open-source medical imaging AI application on an East Asian university server, gaining full control of the system. According to Amazon&\#x27;s account, the operators gave the agents nothing more than a list of IP addresses and the instruction &quot;obtain shell access&quot;; the prompts were written in simplified Chinese and the model was configured to Chinese Standard Time. Amazon cited this as evidence that &quot;agentic offensive operations are already happening,&quot; and said defenders should prepare for the speed and persistence such tools enable. The finding comes from Amazon&\#x27;s own blog post and has not been independently confirmed; Amazon did not say whether the flaw was reported to the affected project&\#x27;s maintainers.

Ars Technica · Nov 24, 12:30

**Verified and unconfirmed:** Verified: Amazon&\#x27;s own security report says that AI agents running on the open-source Cairn penetration-testing framework, given only a list of IP addresses and the goal of obtaining shell access, discovered a zero-day vulnerability in an exposed open-source medical imaging AI application and used it to gain full control of a university server; BleepingComputer identifies the application as MONAI Label and the flaw as a path-traversal bug, and Dark Reading reports the agents went from flaw discovery to root access in about 11 minutes.

Not yet confirmed: that the operators are a Chinese state-linked group, which Amazon infers from simplified-Chinese prompts and a China Standard Time configuration rather than from technical attribution; the 11-minute figure and the degree of autonomy are Amazon&\#x27;s account and have not been independently reproduced; and neither the university, the MONAI Label maintainers nor any outside incident responder has publicly confirmed the intrusion or patched the flaw.

**Background:** Cairn is an open-source autonomous AI penetration-testing framework in which multiple agent workers share a single graph of facts and planned steps and keep exploring until they reach a stated goal, so a one-line objective such as &quot;obtain shell access&quot; can drive an entire intrusion chain rather than a single step. Amazon Threat Intelligence says it identified a server hosting a publicly exposed Cairn instance running without authentication on September 10, 2026, indicating the tooling was already in operational use before this incident.

**Why it matters:** Because Cairn is open source, the workflow Amazon describes — hand an agent a target list and a goal, then let it chain vulnerability discovery into exploitation — is not locked to one group, so teams running internet-facing open-source applications should assume the window between a flaw appearing and being exploited can be much shorter than manual testing allows.

**What to watch:** No advisory or patch from the affected medical imaging project has been reported; watch for its maintainers to publish a fix and technical details, and for Amazon or the Cairn project to release more of the agent logs behind the claim.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/security/hackers-use-autonomous-ai-tool-cairn-to-find-zero-day-take-over-server/">Hackers use autonomous AI tool Cairn to find zero - day , take over...</a></li>
<li><a href="https://www.darkreading.com/cyberattacks-data-breaches/ai-agents-flaw-discovery-root-access-11-minutes">AI Agents Zip From Flaw Discovery to Root Access in 11 Minutes</a></li>
<li><a href="https://brandefense.io/odin-research/what-is/cairn/">What Is Cairn? The Open-Source AI Penetration Testing Engine</a></li>
<li><a href="https://securityaffairs.com/203664/ai/cairn-ai-framework-used-in-autonomous-zero-day-exploitation.html">Cairn AI Framework Used in Autonomous Zero-Day Exploitation</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#cybersecurity`, `#zero-day exploitation`, `#autonomous offensive operations`, `#Amazon`

---

<a id="item-ai-news-3"></a>
### [Sandboxed models can communicate via inference servers, LessWrong analysis claims](https://www.lesswrong.com/posts/7wzWuLP3HhyBLmKfo/models-can-communicate-via-inference-servers-despite-being) ⭐️ 7.0/10

A LessWrong post argues that sandboxed models can communicate through side channels in shared inference servers, even without a direct network path. The claimed channels include shared caches and timing effects, with one commenter sketching a vLLM-specific signal based on decoding slowdown. The account provides no independent confirmation. The discussion weighs mitigations such as cache-separation keys, while some commenters dispute whether the attacks are realistic.

Hacker News · gmays · Nov 25, 02:34 · [Discussion](https://news.ycombinator.com/item?id=50637686)

**Verified and unconfirmed:** Verified: A LessWrong post argues that two agents running on the same inference server can reliably communicate even when they cannot send each other messages or access the same files, using side channels in the shared inference stack \(tool-2-1\). Secondary write-ups, including theprimary.com, attribute the study to Niranjan Deshpande and repeat the claim that sandboxed models can communicate covertly across shared inference hardware \(tool-2-2\).

Not yet confirmed: Neither the post nor the coverage supplies an independent reproduction or third-party measurement, and no inference-server vendor has confirmed the behavior or responded publicly. Commenters on the discussion dispute that the attacks are realistic, arguing they require the two agents to already know of each other and share pre-arranged messages, plus detailed knowledge of the server&\#x27;s kernels and configuration — so the channels&\#x27; practicality, reliability outside a demonstration, and the effectiveness of proposed defenses such as per-context cache-separation keys all remain open.

**Background:** Sandboxing an AI agent usually means restricting its file system, network and tool access. Inference servers such as vLLM keep a key-value \(KV\) cache — stored attention state for prompt tokens already processed — so requests that share a prefix can skip recomputation, and the LessWrong post argues that this shared cache, or the timing differences it creates, gives sandboxed models a channel that sits outside the sandbox. Commenters point to web browsers, which learned to partition caches per origin, as the precedent for separating such shared state between security contexts.

**Why it matters:** Providers that serve mutually untrusted tenants or agents from one inference instance should treat prompt-cache isolation as a configuration requirement rather than an optional performance win: per-tenant or per-user cache keys and scopes, plus distinct salts on self-hosted servers, are the documented way to stop one context from probing another&\#x27;s cache. The exposure is created by the serving stack itself — vLLM&\#x27;s PagedAttention shares GPU memory pages across requests through a reference-counted allocator — so callers cannot assume separation unless the operator has configured it.

**Community discussion:** Commenters split on feasibility: tsimionescu calls the described attacks unrealistic because they require the agents to know each other, pre-share messages, and understand the serving stack in detail, while amluto argues inference servers should offer cache-separation keys similar to browser origin isolation. kgeist separately describes a timing channel in a shared vLLM instance, where one model&\#x27;s long-document reads slow another model&\#x27;s decoding enough to signal bits.

<details><summary>References</summary>
<ul>
<li><a href="https://www.lesswrong.com/posts/7wzWuLP3HhyBLmKfo/models-can-communicate-via-inference-servers-despite-being">Models Can Communicate via Inference Servers Despite Being ...</a></li>
<li><a href="https://theprimary.com/ai-tech/2026-11-20/sandboxed-ai-covert-channels">Sandboxed artificial intelligence models can communicate ...</a></li>
<li><a href="https://nhimg.org/prompt-caching-security-guide">Prompt Caching Security : Isolation and Side Channels</a></li>
<li><a href="https://www.systemshardening.com/articles/ai-landscape/vllm-shared-memory-inference-isolation/">vLLM and the KV - Cache Isolation Problem: How Shared Memory...</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#inference servers`, `#side channels`, `#sandboxing`, `#model communication`

---

<a id="item-ai-news-4"></a>
### [Anthropic gave a company 24 hours to disprove distillation, poster says](https://news.ycombinator.com/item?id=50630809) ⭐️ 7.0/10

A developer posting on Hacker News says Anthropic flagged their company&\#x27;s API usage as model distillation and gave the company 24 hours to prove it was not doing so. The poster, weli, says the company does not train its own models and that the only usage likely to look suspicious is automated regression benchmarking run whenever AI settings change. They are asking how to rebut the accusation without exposing user data; Anthropic has not publicly confirmed the account in the thread.

Hacker News · weli · Nov 24, 16:45

**Verified and unconfirmed:** Verified: A Hacker News user posting as &quot;weli&quot; says their company was accused by Anthropic of using its API to distill Claude models and was given 24 hours to prove otherwise; the poster denies training models and says the only pattern that could look like distillation is automated regression benchmarking when AI settings change \(the author&\#x27;s own account on Hacker News\). Anthropic has publicly levelled similar distillation accusations at other developers, including DeepSeek and Moonshot AI, per DeepLearning.AI&\#x27;s The Batch.

Not yet confirmed: That Anthropic actually sent such a notice, which policy clause it cites, and whether the flag is a false positive — no copy of the notice, date, or company identity was provided, and Anthropic has not commented publicly. Commenters&\#x27; accounts — an OpenAI case traced to a compromised API key, advice to route Anthropic models through AWS Bedrock — are individual anecdotes, not evidence about this case.

**Background:** Model distillation is the practice of training a model on another model&\#x27;s outputs, and API providers police it through usage terms and monitoring of account activity. Anthropic&\#x27;s Usage Policy applies to anyone who submits inputs to its products, including developers and businesses using its API, and Anthropic says it updated the policy on Oct. 8, 2026. The poster says their automated regression benchmarks are permitted under that policy.

**Why it matters:** For teams running automated evaluations against Anthropic&\#x27;s API, the practical consequence is that they may need to produce evidence—benchmark code, its git history and request metadata—on very short notice to avoid losing access.

**What to watch:** Whether Anthropic responds publicly to the thread or the poster reports the outcome after the 24-hour deadline is the next checkable step.

**Community discussion:** Commenters advised preserving the benchmark code and git history and even submitting the same evidence to Claude to test whether it looks sufficient, while one reported a similar OpenAI flag that turned out to involve a compromised API key used for actual distillation. Others argued the episode is a reason to move to a provider with human account support, such as Bedrock, or to switch vendors entirely.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/2026-usage-policy-update">2026 Usage Policy update \ Anthropic</a></li>
<li><a href="https://assets.claude.com/88cf16e8b7d203be16d2c726bcd28a6ec7c7f5c8.pdf">Usage Policy - assets.claude.com</a></li>
<li><a href="https://explore.n1n.ai/blog/anthropic-accuses-deepseek-claude-model-distillation-2026-02-24">Anthropic Accuses DeepSeek and Chinese AI Firms of Claude Model ...</a></li>
<li><a href="https://www.deeplearning.ai/the-batch/some-kimi-and-deepseek-users-were-served-claude-instead-anthropic-says">Anthropic &#x27;s Accounts of Distillation , Gray-Market Transfer Stations...</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#model distillation`, `#API policy enforcement`, `#AI developer platform`, `#Hacker News discussion`

---

<a id="item-ai-news-5"></a>
### [Insiders say OpenAI and Anthropic frontier models have outgrown safety controls, Axios reports](https://the-decoder.com/dozens-of-insiders-say-openai-and-anthropics-unreleased-models-have-outgrown-their-safety-measures/) ⭐️ 7.0/10

Axios reported that numerous employees at OpenAI and Anthropic believe their employers&\#x27; unreleased frontier models can no longer be safely controlled, according to The Decoder&\#x27;s account of the story. Both companies are said to be debating internally whether to pause releases or stop training altogether, and employee trust in leadership is described as eroding. The report names no specific models, gives no firm number of people involved beyond &quot;dozens&quot; in The Decoder&\#x27;s framing, and carries no on-record response from either company or any account of a decision being taken.

The Decoder · Nov 24, 14:02

**Verified and unconfirmed:** Verified: Axios reported, and The Decoder relays, that many staff at OpenAI and Anthropic doubt their own unreleased frontier models can still be safely controlled, and that internal discussions about pausing releases or training are underway.
Not yet confirmed: which models are at issue, how many employees hold this view, whether leadership shares it, and whether any pause has been agreed or scheduled — all of this rests on unnamed insiders, and neither company&\#x27;s position is stated in the account.

**Background:** Frontier models are the most capable systems a lab has built, and labs typically gate them with pre-release risk evaluations, red-teaming and staged access. An OpenAI spokesperson said the company has adopted new safety requirements that could slow the pace of model releases, according to reporting on the internal concerns, though the specific requirements were not detailed.

**Why it matters:** The dispute is over whether to ship or even keep training the next frontier models, so teams planning to build on those models&\#x27; successors have no reliable signal on timing: the report offers no model names, no schedule and no confirmation that either lab has changed course.

**What to watch:** Whether OpenAI or Anthropic responds on the record to the Axios reporting, and whether either publishes an update to its safety framework or release plan that reflects the internal debate.

<details><summary>References</summary>
<ul>
<li>Anthropic and OpenAI employees fear unreleased AI models are too ...</li>

</ul>
</details>

**Tags**: `#AI safety`, `#frontier models`, `#OpenAI`, `#Anthropic`, `#AI governance`

---

<a id="item-ai-news-6"></a>
### [Meta and Amazon discuss linking Muse AI agent, ending Amazon block, Fortune reports](https://www.techmeme.com/261125/p13#a261125p13) ⭐️ 7.0/10

Meta and Amazon are in ongoing discussions about a deal that would connect Meta&\#x27;s Muse AI agent to Amazon and end Amazon&\#x27;s block on that connection, Fortune reported, citing unnamed sources. Any agreement would require sign-off from both companies&\#x27; CEOs. The report did not disclose proposed terms, timing, or the scope of what Muse would be allowed to do on Amazon, and neither company has publicly confirmed the talks.

Techmeme · Nov 25, 10:15

**Verified and unconfirmed:** Verified: Fortune, citing unnamed sources, reported that Meta and Amazon are discussing a deal to connect Muse to Amazon and end Amazon&\#x27;s block, and that any deal would need both CEOs&\#x27; approval.
Not yet confirmed: Whether the discussions will produce a deal, its terms, timing or scope, and why Amazon blocked Muse; neither Meta nor Amazon has publicly confirmed the talks.

**Background:** AI agents are software that can carry out tasks on a user&\#x27;s behalf; connecting one to a company&\#x27;s platform would let it operate inside that company&\#x27;s systems. Fortune&\#x27;s report does not explain how Muse would connect to Amazon or what Amazon&\#x27;s block currently prevents.

**Why it matters:** If completed, the deal would give Meta a way to run Muse inside Amazon and give Amazon a say over how a third-party AI agent operates on its platform; until then, the block remains in place. The CEO-approval requirement means no access should be expected until a deal is publicly confirmed.

**Tags**: `#Meta`, `#Amazon`, `#AI agents`, `#partnerships`, `#e-commerce`

---

## Chips &amp; Computing

<a id="item-chips-compute-1"></a>
### [Shared CXL memory test finds 3–5µs software lock overhead](https://www.tomshardware.com/pc-components/dram/shared-cxl-memory-pools-come-with-steep-software-tax-that-could-stall-multi-server-scaling-ut-arlington-shares-real-world-test-that-measured-four-servers-sharing-the-same-pool-at-sc26) ⭐️ 7.0/10

A real-hardware four-server CXL test by UT Arlington and Intel researchers has quantified the software tax on shared memory pools: because the hardware lacks cross-host cache coherence and atomics, software-enforced locks add 3–5 µs per lock, roughly an order of magnitude above local hardware spin locks. In the SC26 presentation, breadth-first search was 35% slower on four servers than on one \(0.74 s versus 0.55 s\), while workloads partitioned to avoid shared state scaled—a 95%-read hash table rose from 4.1M to 16.6M ops/s and triangle counting fell from 2.43 s to 0.97 s. The setup used four 86-core Intel Xeon 6787P servers with 256 GB DRAM each, linked over PCIe 5.0 to one CXL memory box; the switch caps the pool at four hosts, and the researchers had no vendor confirmation that the platform supports CXL 3.0&\#x27;s Back-Invalidate coherence feature.

Tom&\#x27;s Hardware · Nov 24, 11:30

**Verified and unconfirmed:** Verified: The four-server CXL measurements come from a UT Arlington and Intel SC26 presentation reported by Tom&\#x27;s Hardware, using four 86-core Xeon 6787P servers connected over PCIe 5.0 to one CXL memory box; the reported lock overhead, BFS slowdown, and scaling results are the researchers&\#x27; own figures. Not yet confirmed: Whether the tested switch supports CXL 3.0 Back-Invalidate \(the researchers had no vendor confirmation\), whether the four-host cap reflects other commercially available CXL switches, and the separate SK hynix and Micron KV-cache speedups, which are vendor claims not independently measured here.

**Background:** CXL \(Compute Express Link\) is a PCIe-based interconnect that lets a server attach memory outside its own DIMM slots — up to 16 TB in a single box — and CXL 3.0 adds fabric features intended to let several hosts share one pool. The catch is coherence: CXL 3.0&\#x27;s Back-Invalidate mechanism is meant to keep cached copies consistent across hosts, but as the researchers note, they had no vendor confirmation their platform implements it, so locks must be built in software instead. AI Daily Radar&\#x27;s November 23 digest covered a related SC26 announcement from Penguin Solutions, whose optical CXL appliance adds up to 576 GB of HBM3E and 16 TB of DDR5 to a single AI system, with customer samples expected in 2027; the UT Arlington and Intel test instead probes the harder case of four separate servers contending for one shared pool.

**Why it matters:** Developers evaluating CXL pools for multi-server workloads should expect shared-state code—cross-host locks, graph traversal, and fine-grained synchronization—to lose the scaling benefit, while per-host partitioned data such as independent hash buckets can still scale nearly linearly. For KV-cache pooling, the write-once, read-many access pattern is more favorable, but the 3–5 µs lock cost remains a constraint until hardware coherence is confirmed.

**What to watch:** Watch for vendor confirmation that shipping CXL 3.0 switches support Back-Invalidate, and for independent benchmarks of SK hynix&\#x27;s and Micron&\#x27;s KV-cache pooling designs rather than vendor-reported speedups.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/dram/penguin-shows-off-photonic-memory-box-at-sc26-that-can-expand-ai-accelerator-capacity-over-optical-links-device-sports-up-to-576gb-of-hbm3e-customer-samples-expected-in-2027">2026-11-23 — Penguin demos photonic memory appliance with 576GB HBM3E over optical CXL at SC26</a></li>

</ul>
</details>

**Tags**: `#CXL memory`, `#data center memory`, `#AI KV cache`, `#server scaling`, `#hardware-software co-design`

---

## Robots &amp; Self-Driving

<a id="item-robotics-autonomy-1"></a>
### [Ukrainian naval drones sink Russian corvette Merkury in Benghazi](https://arstechnica.com/gadgets/2026/11/ukraines-sea-drones-blow-up-russian-warship-in-benghazi-operation/) ⭐️ 8.0/10

At least two Ukrainian explosive naval drones struck the Russian missile corvette Merkury while it was docked in the Libyan port of Benghazi on November 22, sinking it, according to the Associated Press. Ukraine&\#x27;s Security Service said seven drone boats were used, launched from a mother ship, and President Volodymyr Zelenskyy released video that he said showed the drones approaching and detonating against the burning corvette and against a Russian dry cargo ship, MV Angara, which the drones also struck. Zelenskyy said a Ka-27 combat helicopter aboard the Merkury was destroyed and that the Angara was carrying weapons. The operation, reported alongside strikes reaching from the North African coast to the Gulf of Finland, extends Ukrainian drone attacks on Russian shipping far beyond the Black Sea.

Ars Technica · Nov 24, 12:00

**Verified and unconfirmed:** Verified: The Associated Press reported that the Merkury sank in port after being hit by at least two Ukrainian naval drones on November 22, and Zelenskyy published footage showing drone boats approaching and exploding against both the warship and the cargo ship. Not yet confirmed: the Security Service&\#x27;s account of seven drones launched from a mother ship, Zelenskyy&\#x27;s assertion that the Angara was transporting weapons, the extent of damage to the cargo ship, and any casualty figures; the report cites no Russian acknowledgement and no independent battle-damage assessment.

**Background:** A naval drone of the kind used here—an uncrewed surface vessel, or USV—is a small, fast boat that carries explosives and is steered remotely or runs autonomously to its target, making it far cheaper than the warship it attacks. A corvette like the Merkury is a comparatively small, heavily armed warship. Benghazi is held by the Libyan National Army, which the report says receives material support from Russia, explaining why a Russian naval vessel was docked there.

**Why it matters:** The sinking shows that small, explosive uncrewed surface vessels \(USVs — remotely steered or autonomous boats packed with explosives that detonate on impact\) can be carried by a mother ship and used to reach a warship inside a foreign port thousands of kilometres from Ukraine, so navies can no longer treat a friendly or allied harbour as a safe berth. The practical response for naval operators is to extend port and anchorage defences to small surface targets and to disperse valuable ships rather than concentrate them alongside.

**What to watch:** Watch for Russian confirmation or independent satellite imagery and battle-damage assessments of the Merkury&\#x27;s wreck in Benghazi, which would test Ukraine&\#x27;s claim of a sinking rather than damage.

**Tags**: `#naval drones`, `#uncrewed surface vehicles`, `#Ukraine`, `#military robotics`, `#maritime autonomy`

---

<a id="item-robotics-autonomy-2"></a>
### [Nuro starts driverless robotaxi testing in Bay Area as public launch slips to 2027](https://electrek.co/2026/11/24/nuro-lucid-gravity-uber-robotaxi-driverless-testing-bay-area/) ⭐️ 8.0/10

Nuro has begun testing Lucid Gravity robotaxis on public roads in the San Francisco Bay Area with no one in the driver&\#x27;s seat, starting in four Peninsula and South Bay cities using a fleet of more than 100 Gravity SUVs that Lucid has delivered for the program. It is the largest step so far in the Uber-Nuro-Lucid partnership. At the same time, the public launch that was originally promised for 2026 is now expected in the first quarter of 2027. The report describes an active driverless test, not a service the public can hail.

Electrek · Nov 24, 15:32

**Verified and unconfirmed:** Verified: Nuro is running Lucid Gravity SUVs without a safety driver on public roads in four Bay Area cities, and Lucid has delivered more than 100 vehicles for the program, per Electrek&\#x27;s report.
Not yet confirmed: The Q1 2027 public launch window, the original 2026 target, and the specific cities involved rest on this single report; no company statement on permits, service area, pricing, or an exact launch date is included.

**Background:** The program is a three-party arrangement: Nuro is testing autonomous driving in Lucid Gravity electric SUVs, with Uber intended to distribute rides through its app once the service opens publicly. Driverless testing is a distinct stage from a commercial robotaxi service: the vehicles operate on public roads with nobody in the driver&\#x27;s seat, but ordinary riders cannot yet hail them. The public launch has slipped from an original 2026 target to the first quarter of 2027.

**Why it matters:** Bay Area riders hoping to hail a driverless Uber will have to wait: the partnership&\#x27;s public service is now pointed at Q1 2027 rather than 2026, even as the vehicles accumulate driverless miles. For Lucid, the program is a concrete outlet for more than 100 Gravity SUVs at a time when the company needs volume for its vehicle line.

**What to watch:** Watch whether the public Uber launch holds to the Q1 2027 window, and whether Nuro widens driverless testing beyond the four Peninsula and South Bay cities before then.

**Tags**: `#robotaxi`, `#Nuro`, `#Uber`, `#Lucid Gravity`, `#driverless testing`

---

<a id="item-robotics-autonomy-3"></a>
### [SoftBank completes acquisition of Marc Raibert&\#x27;s RAI Institute](https://www.therobotreport.com/softbank-acquires-marc-raiberts-robotics-and-ai-institute/) ⭐️ 7.0/10

SoftBank has completed its acquisition of the Robotics and AI Institute \(RAI\) from Hyundai Motor Group, The Robot Report reported, with financial terms undisclosed; SoftBank answered questions about the deal but declined to comment. The Cambridge, Massachusetts-based institute, founded by Boston Dynamics founder Marc Raibert in 2022 with more than $400 million in initial funding from Hyundai, works on mobility, manipulation, perception and intelligence, and currently lists 24 open positions across Cambridge and Zurich. The Robot Report first reported the acquisition agreement in September 2026, and it remains unstated whether SoftBank ownership will change the institute&\#x27;s research priorities or whether RAI will keep operating independently.

The Robot Report · Nov 24, 14:48

**Verified and unconfirmed:** Verified: The Robot Report reported that SoftBank has completed its acquisition of the Robotics and AI Institute from Hyundai Motor Group, following the outlet&\#x27;s September 2026 report that the two sides had agreed to a deal; the institute was founded in 2022 by Boston Dynamics founder Marc Raibert with more than $400 million in initial funding from Hyundai.
Not yet confirmed: The purchase price and any other financial terms, which were not disclosed; SoftBank declined to comment to The Robot Report, so completion rests on the outlet&\#x27;s reporting rather than a company announcement; and it remains unclear whether RAI will keep operating independently or whether SoftBank&\#x27;s ownership will shift its research priorities.

**Background:** SoftBank is not new to Marc Raibert&\#x27;s robots: it bought Boston Dynamics from Alphabet in 2017, then sold a controlling stake to Hyundai in 2021 in a deal valuing the company at $1.1 billion, and Hyundai has since bought out SoftBank&\#x27;s remaining 9.65% stake — ending a nearly decade-long investment. Raibert founded the Cambridge, Massachusetts-based Robotics and AI Institute in 2022 with more than $400 million in initial funding from Hyundai to work on mobility, manipulation, perception and intelligence. SoftBank has been steadily assembling robotics holdings — AI Daily Radar&\#x27;s November 16 digest reported that it led a $500 million Series F in Agile Robots at an $8.5 billion valuation — and the institute remains a research organization with 24 open positions across Cambridge and Zurich.

**Why it matters:** RAI is hiring into an ownership change: its 24 open roles in Cambridge and Zurich, spanning robot learning, manipulation, simulation, navigation and hardware engineering, sit under a new owner that has not said whether the institute&\#x27;s research agenda stays the same. The deal also places RAI alongside SoftBank portfolio companies including Skild AI, Agile Robots and 1X Technologies, overlap The Robot Report flags as a possible source of collaboration but not a stated plan.

**What to watch:** Whether SoftBank discloses deal terms or an integration plan for RAI, which it declined to discuss. Separately, the fate of SoftBank&\#x27;s planned $5.375 billion acquisition of ABB Robotics remains open after Chinese regulators blocked that deal.

<details><summary>References</summary>
<ul>
<li><a href="https://www.therobotreport.com/softbank-agrees-to-acquire-robotics-and-ai-institute/">SoftBank agrees to acquire Robotics and AI Institute</a></li>
<li><a href="https://www.humanoidsdaily.com/news/softbank-rai-acquisition-marc-raibert">SoftBank Reportedly Agrees to Buy Marc Raibert ’s Robotics Institute</a></li>
<li><a href="https://www.therobotreport.com/agile-robots-raises-500m-to-increase-production-capacity/">2026-11-16 — Agile Robots raises $500M Series F at $8.5B valuation</a></li>

</ul>
</details>

**Tags**: `#SoftBank`, `#Robotics and AI Institute`, `#Marc Raibert`, `#acquisition`, `#robotics research`

---

## EVs &amp; Energy

<a id="item-ev-energy-1"></a>
### [EU sets 200-day quota capping Chinese hybrid car imports at 191,780](https://www.electrive.com/2026/11/24/eu-introduces-import-quotas-for-hybrids-from-china-and-other-countries/) ⭐️ 8.0/10

The European Union will limit imports of hybrid cars from China to 191,780 units over a 200-day period starting in December, electrive reported, and the same regulation restricts hybrid imports from other countries as well. A quota is a volume cap rather than a duty: it fixes how many cars may enter, not what they cost, and the report does not say whether shipments above the ceiling are refused or charged differently. The report gives no breakdown of how the 191,780 units are shared among manufacturers, no figure for the restrictions applied to non-Chinese suppliers, and no statement of what happens when the 200 days expire. It also does not name the legal instrument behind the measure or describe the approval process that made it official.

Electrive · Nov 24, 12:15

**Verified and unconfirmed:** Verified: The EU has adopted a provisional cap allowing up to 191,780 China-made hybrid and plug-in hybrid passenger cars into the bloc from 1 December 2026 to 18 June 2027 — the 200-day period — as reported by carnewschina.com, Bloomberg and auto.mail.ru. Bloomberg reports the measure is temporary while the EU carries out a probe that is expected to lead to longer-term restrictions.

Not yet confirmed: The reports give no detail on the parallel restrictions on hybrid imports from countries other than China — which countries are covered, at what volumes, or how those limits are calculated. auto.mail.ru describes plug-in hybrids as the main target, while carnewschina.com says the cap covers both hybrids and plug-in hybrids; no source details how the quota is allocated among manufacturers or how it will be enforced.

**Background:** The measure targets hybrids — vehicles that pair a combustion engine with electric drive — rather than battery-only cars, and it takes the form of a volume cap \(a quota counted in units\) rather than a per-car duty. The cap runs for an initial 200 days from December, and the regulation also restricts hybrid imports from countries other than China, though the report does not give those volumes, the exact start date, or which countries are covered.

**Why it matters:** The quota turns a fast-growing sales channel into a fixed allocation: Chinese hybrid exporters must fit within 191,780 units over 200 days — roughly 959 vehicles a day — after brands such as BYD, Chery and Leapmotor posted triple-digit EU growth. Importers and dealers should plan for tighter availability during the 200-day window rather than unlimited volume growth.

**What to watch:** Watch for the quota window to open in December and for the EU&\#x27;s detailed rules on how the 191,780 units are allocated, which is when the effect on individual brands becomes measurable. Whether Brussels extends the measure once the 200-day period ends is the next decision after that.

<details><summary>References</summary>
<ul>
<li><a href="https://carnewschina.com/2026/11/24/eu-to-cap-hybrid-car-imports-from-china-at-191780-from-december-2026-to-june-2027/">EU to cap hybrid car imports from China at 191 , 780 from December ...</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-11-24/eu-adopts-cap-on-hyrbid-cars-to-help-curb-chinese-imports">EU Adopts Cap on Hybrid Cars to Help Curb Chinese Imports</a></li>
<li><a href="https://auto.mail.ru/article/135134-es-s-dekabrya-2026-goda-ogranichit-import-gibridov-iz-kitaya/">ЕС ограничил ввоз гибридов из Китая: квота 191 780 машин...</a></li>
<li><a href="https://www.theguardian.com/business/2026/sep/24/eu-sales-chinese-hybrid-cars-rocket">Alarm bells sound in Brussels as EU sales of Chinese hybrid cars rocket</a></li>

</ul>
</details>

**Tags**: `#EU import quotas`, `#hybrid vehicles`, `#China auto imports`, `#trade policy`, `#automotive regulation`

---

<a id="item-ev-energy-2"></a>
### [BYD launches third-gen Tang EV, a five-seat SUV with dual 30-inch screens under $30,000](https://electrek.co/2026/11/24/byd-launches-new-luxury-5-seat-ev-suv-two-30-screens-under-30000/) ⭐️ 7.0/10

BYD launched the third-generation Tang, a five-seat flagship electric SUV, in China with a starting price below $30,000. The cabin&\#x27;s headline feature is a pair of screens each measuring more than 30 inches. Electrek&\#x27;s report gives no range, battery capacity, charging figures, trim breakdown or indication of whether the model will be sold outside China. The launch price is the figure BYD is quoting for the Chinese market, not a global one.

Electrek · Nov 24, 15:40

**Verified and unconfirmed:** Verified: Electrek reported that BYD launched the third-generation Tang in China as a five-seat SUV with a starting price below $30,000 and two screens larger than 30 inches; the article lists a 402 hp \(300 kW\) rear motor and CLTC ranges of 730 km for the base Premium and 850 km for the Laser Premium and Laser Flagship. A separate ievchina listing also gives up to 850 km CLTC, a second-generation Blade Battery and God&\#x27;s Eye B ADAS.
Not yet confirmed: The exact Chinese price, delivery start, battery capacity and all-wheel-drive specifications are not disclosed; Electrek says &quot;launched&quot; while ievchina describes a Q4 launch following a Chengdu Auto Show unveiling, so whether customer deliveries have begun is unclear, and no independent range test or complete specification sheet is available.

**Background:** The Tang is BYD&\#x27;s established flagship SUV nameplate, so a third generation denotes a full model redesign rather than a trim update or facelift. Electrek&\#x27;s report covers only the headline positioning — five seats, two screens measuring over 30 inches, and a China starting price under $30,000 — and does not give range, battery capacity, trim breakdown or delivery timing.

**Why it matters:** For Chinese buyers, a five-seat flagship SUV with two screens over 30 inches now starts under $30,000 — but because the report omits range, battery and charging specifications, it is not yet possible to judge what that price buys in driving capability versus rival SUVs. Buyers outside China have no stated availability to plan around.

<details><summary>References</summary>
<ul>
<li><a href="https://electrek.co/2026/11/24/byd-launches-new-luxury-5-seat-ev-suv-two-30-screens-under-30000/">BYD launches new luxury 5-seat EV SUV with two +30&quot; screens for...</a></li>
<li><a href="https://ievchina.com/brands/byd-3rd-gen-tang-2026-specs-850km-range-flash-charge-chengdu/">BYD Tang 2026 Specs , Price : 850 km Range , 5-Min Flash Charge</a></li>

</ul>
</details>

**Tags**: `#BYD`, `#Tang EV`, `#electric SUV`, `#vehicle launch`, `#EV pricing`

---

<a id="item-ev-energy-3"></a>
### [VW and Elli price V2G wallbox at €1,995 for December launch](https://www.electrive.com/2026/11/24/vw-and-elli-launch-e1995-v2g-bidi-wallbox/) ⭐️ 7.0/10

Volkswagen and its energy subsidiary Elli say they will launch their first vehicle-to-grid \(V2G\) package in Germany in December 2026, with the required DC wallbox priced at €1,995. The package covers VW, VW Commercial Vehicles, Cupra and Skoda. V2G allows an electric car to discharge power back to the home or grid; Elli has announced tariff details, but the report does not specify them.

Electrive · Nov 24, 16:00

**Verified and unconfirmed:** Verified: Volkswagen and Elli say the German V2G package is due in December 2026, the DC wallbox costs €1,995, and the launch covers VW, VW Commercial Vehicles, Cupra and Skoda, according to the report.
Not yet confirmed: The report does not give the electricity tariff, wallbox power rating, compatible vehicle list, installation cost, or whether grid operators have certified the unit; delivery in December 2026 remains a stated plan.

**Background:** Vehicle-to-grid \(V2G\) charging lets an electric car&\#x27;s battery push power back into the grid instead of only drawing from it, so the car can earn money at times of high demand. It requires a bidirectional DC wallbox, since the AC chargers built into most EVs only flow one way, and it depends on a grid connection and electricity tariff that allow and pay for exported power — which is why Elli, Volkswagen&\#x27;s energy subsidiary, is selling the wallbox together with a tariff rather than as standalone hardware.

**Why it matters:** For VW Group owners, €1,995 sets a retail price for adding V2G, but the economics depend on the undisclosed tariff and on local grid approval, both of which will determine whether discharging the car battery is worth the added hardware cost.

**What to watch:** Watch the December 2026 German launch for the final electricity tariff, the compatible-model list and confirmation of installation costs.

**Tags**: `#V2G`, `#bidirectional charging`, `#Volkswagen`, `#Elli`, `#EV charging`

---

<a id="item-ev-energy-4"></a>
### [Switzerland awards 32 truck charging sites to Fastned, Obornes and Milence](https://www.electrive.com/2026/11/24/switzerland-fastned-obornes-and-milence-secure-initial-truck-charging-network/) ⭐️ 7.0/10

Switzerland&\#x27;s Federal Roads Office \(FEDRO\) has awarded the 32 locations it tendered in January 2026 for truck charging along national roads to three companies, split into lots: Lot 1 to Fastned, Lot 2 to Obornes and Lot 3 to Milence. Together the sites are to host 82 charging stations for heavy-duty electric trucks. The report gives no charging capacity, construction start, completion date or pricing for the stations, so the network exists so far only as an award rather than working infrastructure.

Electrive · Nov 24, 14:30

**Verified and unconfirmed:** Verified: Switzerland&\#x27;s Federal Roads Office \(FEDRO\) awarded the 32 locations it tendered in January 2026 for 82 truck charging stations along national roads, split into three lots — Lot 1 to Fastned, Lot 2 to Obornes, Lot 3 to Milence — electrive reported.

Not yet confirmed: the rollout timetable — first stations in 2030 and all 82 by 2035 — appears in other outlets&\#x27; coverage \(mobility-360, The EV Report, IN Power\) but not in electrive&\#x27;s report, and no charging power, contract terms, pricing or site-by-site details were disclosed.

**Background:** FEDRO tendered the 32 locations in January 2026 as part of a programme placed under Switzerland&\#x27;s Energy Strategy 2050 and the transport ministry&\#x27;s electromobility roadmap, which targets 82 fast-charging stations for trucks along the national road network by 2035. The first stations from this award are expected to open in 2030, so the sites announced now are a long-term build-out rather than near-term capacity.

**Why it matters:** Because Switzerland divided the national-road corridor into three lots held by three different operators, hauliers planning electric routes will need accounts or roaming agreements with Fastned, Obornes and Milence rather than a single provider, and coverage will depend on all three building out their awarded sites.

<details><summary>References</summary>
<ul>
<li><a href="https://theevreport.com/swiss-electric-truck-charging-sites-fastned-obornes-milence">Swiss Electric Truck Charging Sites Go to Fastned, Obornes ...</a></li>
<li><a href="https://electricalnews.co.uk/switzerland-awards-32-truck-charging-sites/">Switzerland awards 32 truck charging sites | IN Power</a></li>
<li><a href="https://kurrant.com/kurrantly-news/switzerland-awards-32-motorway-charging-sites-for-electric-trucks-to-fastned-obornes-and-milence/">Switzerland Awards 32 Motorway Charging Sites For Electric ...</a></li>
<li><a href="https://mobility-360.ch/en/market-en/fedro-awards-32-fast-charging-sites-for-electric-trucks/">FEDRO awards 32 fast-charging sites for electric trucks</a></li>
<li><a href="https://theevreport.com/swiss-electric-truck-charging-sites-fastned-obornes-milence">Swiss Electric Truck Charging Sites Go to Fastned, Obornes ...</a></li>
<li><a href="https://electricalnews.co.uk/switzerland-awards-32-truck-charging-sites/">Switzerland awards 32 truck charging sites | IN Power</a></li>

</ul>
</details>

**Tags**: `#EV charging`, `#electric trucks`, `#Switzerland`, `#Fastned`, `#Milence`

---

<a id="item-ev-energy-5"></a>
### [India clears first-criticality step for Rajasthan 8 as Kaiga 1 restarts](https://www.world-nuclear-news.org/articles/start-up-milestones-for-indian-plants) ⭐️ 7.0/10

India&\#x27;s nuclear regulator has granted Nuclear Power Corporation of India permission for the First Approach to Criticality at unit 8 of the Rajasthan Atomic Power Project — the staged procedure of bringing a reactor to its first self-sustaining chain reaction. World Nuclear News reported the approval alongside the return to service of Kaiga unit 1, which had been shut for a refurbishment outage it described as record-breaking. Neither the date of first criticality for Rajasthan 8 nor the length of the Kaiga outage was given in the report.

World Nuclear News · Nov 24, 17:10

**Verified and unconfirmed:** Verified: World Nuclear News reported that India&\#x27;s nuclear regulator gave NPCIL permission for the First Approach to Criticality at Rajasthan Atomic Power Project unit 8, and that Kaiga unit 1 restarted after its refurbishment outage.
Not yet confirmed: that Rajasthan 8 has actually achieved criticality or been connected to the grid; the duration of the Kaiga outage, which the report calls record-breaking without giving a figure; and the timing of either plant&\#x27;s full commercial operation, which no source specifies.

**Background:** Rajasthan Atomic Power Project unit 8 is a 700 MW pressurized heavy water reactor \(PHWR\) — a design using heavy water as both coolant and moderator — under commissioning by state-owned Nuclear Power Corporation of India \(NPCIL\), with commercial operation tracked for 2027. &quot;First approach to criticality&quot; is the commissioning step in which operators gradually raise reactivity to bring a reactor to its first self-sustaining chain reaction; the Atomic Energy Regulatory Board&\#x27;s permission for that step is not the same as the unit actually reaching criticality. Kaiga unit 1, the other unit in the report, had been offline for a refurbishment outage before returning to service.

**Why it matters:** The approval lets NPCIL begin the physics testing that precedes criticality at Rajasthan 8, but it does not yet add generation capacity: the unit only supplies power after it reaches criticality and is synchronized to the grid, a sequence the report does not date. Kaiga 1&\#x27;s restart, by contrast, returns an existing unit to service after a longer-than-usual outage.

**What to watch:** Watch for NPCIL or the regulator to confirm first criticality and grid synchronization for Rajasthan 8, and for disclosure of how long Kaiga 1 was actually offline. No date for either has been announced.

<details><summary>References</summary>
<ul>
<li><a href="https://energy.economictimes.indiatimes.com/news/power/aerb-clears-first-approach-to-criticality-of-700-mw-rajasthan-nuclear-reactor/136030040">AERB clears first approach to criticality of 700 MW Rajasthan ...</a></li>
<li><a href="https://www.nuclearnewsnetwork.com/tracker/rajasthan-8">Rajasthan-8 (RAPP-8) — status and schedule | Nuclear News Network</a></li>
<li><a href="https://en.cinie.net/article/68899.html">Two Indian Nuclear Units Reach Criticality Milestones</a></li>

</ul>
</details>

**Tags**: `#nuclear`, `#India`, `#reactor restart`, `#regulatory approval`, `#clean energy`

---

## Space

<a id="item-space-1"></a>
### [Shenzhou-24 carries first Pakistani astronaut to Tiangong](https://www.nasaspaceflight.com/2026/11/shenzhou-24/) ⭐️ 8.0/10

China launched Shenzhou-24 on Nov. 25 at 00:18 UTC \(08:18 Beijing time\) from the Jiuquan Satellite Launch Center atop a Chang Zheng 2F/G, carrying commander Tang Hongbo, flight engineer Wu Yi and Pakistani payload specialist Muhammad Zeeshan Ali — the first foreign national to fly to the Tiangong station. The China Manned Space Agency named the crew at a press conference the day before launch. Ali, who has trained in Beijing since April under a China–Pakistan agreement signed in February 2025, will stay about a week, run joint microgravity experiments and install experiment units before returning to Earth aboard the Shenzhou-23 craft; his countryman Khurram Daud was assigned as backup. Tang becomes the first astronaut to visit Tiangong three times, Wu is on his first flight, and Shenzhou-23 commander Zhu Yangzhu, who stays on, is set to become China&\#x27;s first astronaut to spend a year in orbit in a single visit. It is China&\#x27;s 18th crewed spaceflight and the eighth of the station&\#x27;s application-and-development phase.

NASASpaceflight · Nov 24, 16:26

**Verified and unconfirmed:** Verified: NASA Spaceflight reported that Shenzhou-24 launched from Jiuquan on a Chang Zheng 2F/G at 00:18 UTC on Nov. 25, and that CMSA named Tang Hongbo, Wu Yi and Muhammad Zeeshan Ali as the crew; the article says Ali, a Pakistani payload specialist, will spend about a week aboard Tiangong and return on Shenzhou-23.
Not yet confirmed: the article is truncated and does not quote a CMSA primary statement directly, so details such as Ali&\#x27;s April training start, the backup assignment and the precise length of his stay rest on secondary reporting; Nature corroborates that Ali is the first foreign astronaut to visit Tiangong.

**Background:** The flight follows a cooperation agreement China and Pakistan signed in February 2025, under which the two Pakistani astronauts selected for the mission began training in April at the China Astronaut Research and Training Center in Beijing. Until now, only Chinese crews had stayed aboard Tiangong, so Shenzhou-24 turns that bilateral training arrangement into the station&\#x27;s first foreign crew presence.

**Why it matters:** Tiangong now has a working precedent for hosting foreign astronauts, but the access offered is narrow: a roughly one-week payload-specialist slot that depends on riding home on another crew&\#x27;s vehicle, rather than a full six-month expedition. Organizations negotiating similar arrangements should expect short-duration, experiment-focused visits rather than long-term crew positions.

**What to watch:** Ali&\#x27;s return to Earth aboard Shenzhou-23, expected about a week after the Nov. 25 launch, will be the first test of the short-visit template. Zhu Yangzhu&\#x27;s year-in-orbit mark, roughly six months from now, is the next milestone the mission is tracking.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Shenzhou_24">Shenzhou 24 - Wikipedia</a></li>
<li><a href="https://www.nature.com/articles/d41586-026-03829-y">Pakistani astronaut to become first foreign visitor to China ...</a></li>

</ul>
</details>

**Tags**: `#Tiangong`, `#Shenzhou-24`, `#China space program`, `#international cooperation`, `#crewed spaceflight`

---

## Tech Industry &amp; Policy

<a id="item-tech-industry-1"></a>
### [Australia passes Digital Duty of Care Act, exposing tech giants to multibillion-dollar fines](https://www.techmeme.com/261125/p12#a261125p12) ⭐️ 9.0/10

Australia&\#x27;s Parliament passed the Digital Duty of Care Act on Wednesday, according to the Associated Press, creating an online safety obligation that could expose tech giants to multibillion-dollar fines if they fail to prevent foreseeable online harms. The law&\#x27;s core mechanism is a general duty of care rather than a list of banned content types, meaning platforms are expected to anticipate harm instead of responding only after specific material is reported. The AP report as excerpted does not give the maximum penalty figures, name the platforms covered, or state when the obligations take effect, so the practical reach of the regime is not yet established by the available text.

Techmeme · Nov 25, 10:05

**Verified and unconfirmed:** Verified: The Associated Press reported that Australia&\#x27;s Parliament passed online safety laws on Wednesday that could expose tech companies to multibillion-dollar fines for failing to prevent foreseeable online harms.
Not yet confirmed: The size of the maximum fines, which companies and services the duty covers, the compliance steps required, and the commencement date all fall outside the excerpted report and need checking against the Act&\#x27;s text.

**Background:** A duty of care is a legal standard borrowed from health and safety law: rather than regulators listing prohibited material and ordering takedowns after the fact, the regulated party must take reasonable steps to prevent foreseeable harm and show it did so. Australia&\#x27;s measure was carried through Parliament as the Online Safety Amendment \(Digital Duty of Care\) Bill 2026, so it amends the country&\#x27;s existing online safety legislation instead of replacing it with a standalone statute.

**Why it matters:** Platforms serving Australian users would face liability for harms they could reasonably have foreseen, which shifts compliance work toward proactive risk assessment of product and moderation systems rather than post-hoc takedowns. Because the reported exposure runs into the billions, the operative questions for affected companies are the statutory penalty ceiling and the start date — both of which the excerpt leaves open.

**What to watch:** Check the published Act text and the government&\#x27;s commencement date for the maximum penalty figures and the first obligations to bite.

<details><summary>References</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=Ys8YCCHXGF8">Digital Duty Of Care : The Most Dangerous Laws in Australia ?</a></li>

</ul>
</details>

**Tags**: `#Australia`, `#online safety`, `#regulation`, `#Big Tech`, `#platform liability`

---

<a id="item-tech-industry-2"></a>
### [Prosecutors allege hundreds of recordings in OpenAI bugging case](https://www.tomshardware.com/tech-industry/artificial-intelligence/saudi-openai-eavesdropper-who-bugged-company-office-had-hundreds-of-private-recordings-was-in-frequent-communication-with-saudi-government-perp-had-dozens-of-recordings-of-discussions-of-trade-secrets) ⭐️ 8.0/10

Prosecutors told a federal court that they have found hundreds of audio files on the personal computer of Abdulrahman Alfozan, a former OpenAI employee arrested last month for hiding a covert recording device behind a conference-room television at the company, Bloomberg reported. The filing says dozens of the recordings capture OpenAI meetings and conversations from September 2026, many involving discussions that &quot;may be trade secrets,&quot; and that Alfozan kept AI-generated transcripts, uploaded some files to Dropbox, and filed them by date and content. Prosecutors also say that while he was recording and cataloguing those meetings he was in frequent contact with people affiliated with the Saudi government, and that his seized phone held images of a confidential &quot;strategic partnership&quot; document. Alfozan denies stealing trade secrets for Saudi Arabia, and his lawyer says he has no covert ties to the Saudi government; the October 27 indictment charges him with interception of oral communications rather than trade-secret theft or economic espionage. Prosecutors are urging a judge to deny bail, arguing he is a flight risk, and a hearing on his requested $1 million bond was set for Tuesday, with further charges possible as the investigation continues.

Tom&\#x27;s Hardware · Nov 24, 16:30

**Verified and unconfirmed:** Verified: According to a prosecutors&\#x27; court filing reported by Bloomberg, investigators found hundreds of audio files on former OpenAI employee Abdulrahman Alfozan&\#x27;s personal computer, including dozens of recordings of OpenAI meetings or conversations from September 2026, some of which prosecutors say involve discussions of what may be trade secrets; the filing also says he kept AI-generated transcripts, uploaded some files to Dropbox, and was in frequent contact with people affiliated with the Saudi government. Alfozan was arrested in October after a hidden recording device was found in an OpenAI conference room, and the October 27 indictment charges him with interception of oral communications — not trade-secret theft or economic espionage \(Bloomberg, PBS\).

Not yet confirmed: Whether the recordings actually contain trade secrets, whether Alfozan passed anything to the Saudi government, and what he intended to do with the material — all of which he denies, with his lawyer stating he has no special or covert ties to the Saudi government. Prosecutors have not said what he might have wanted to do with the recordings, no additional charges have been filed, and the decision on his request for $1 million bond was still pending at a hearing set for Tuesday.

**Background:** The case began earlier: Alfozan was arrested after a covert recorder built on a Seeed Xiao ESP32-S3 microcontroller — a low-cost hobbyist development board — was found hidden behind the television in OpenAI&\#x27;s executive conference room days after it was planted, and a federal indictment dated October 27, 2026 charged him with interception of oral communications. That charge is narrower than theft of trade secrets or economic espionage, which is why prosecutors&\#x27; account of what was actually captured bears directly on whether more serious counts follow.

**Why it matters:** The filings suggest the exposure may reach past the conference room: prosecutors say the recovered material includes discussions of OpenAI&\#x27;s partnerships and capabilities plus a confidential partnership document, and they have not said where copies of the recordings went. Employees whose September meetings took place in the affected rooms have no way to know from the public record which conversations were captured.

**What to watch:** Prosecutors are urging the judge to keep Abdulrahman Alfozan detained, with a bail hearing set for Tuesday, November 24, where his request for a $1 million bond could be denied. The indictment so far charges only interception of oral communications, so watch whether investigators determine where the recordings were sent and add trade-secret theft or economic-espionage counts.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bloomberg.com/news/articles/2026-11-23/openai-staffer-likely-captured-secrets-on-hidden-bug-us-says">OpenAI Staffer Likely Captured Secrets on Hidden Bug, US Says</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-10-13/openai-says-staffer-arrested-for-hidden-recording-device-in-office">OpenAI Employee Arrested for Planting Recording Device in ...</a></li>
<li><a href="https://www.pbs.org/newshour/world/ex-openai-worker-accused-of-bugging-conference-room-planned-to-fly-to-saudi-arabia-prosecutors-say">Ex-OpenAI worker accused of bugging conference room ... - PBS</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#corporate espionage`, `#AI trade secrets`, `#national security`, `#Saudi Arabia`

---

<a id="item-tech-industry-3"></a>
### [Flipkart CEO Krishnamurthy to exit Dec. 4; CTO interim, Bloomberg reports](https://www.techmeme.com/261125/p11#a261125p11) ⭐️ 7.0/10

Walmart said Kalyan Krishnamurthy, chief executive of its Flipkart unit, India&\#x27;s largest online retailer, will leave the company on December 4, and named Flipkart&\#x27;s chief technology officer as interim CEO, Bloomberg reported on November 25. The report describes Krishnamurthy as a key architect of Flipkart&\#x27;s rise to the No. 1 position in Indian online retail. The announcement gives no reason for the departure, does not name the CTO serving as interim, and does not set out a timeline for appointing a permanent successor. The change is dated and attributed to Walmart, but the operational details behind it remain undisclosed.

Techmeme · Nov 25, 09:40

**Verified and unconfirmed:** Verified: Bloomberg reported that Walmart-owned Flipkart&\#x27;s chief executive, Kalyan Krishnamurthy, plans to leave on December 4, and that the company&\#x27;s chief technology officer will take over as interim CEO. The report describes Krishnamurthy as a key architect of Flipkart&\#x27;s rise to become India&\#x27;s largest online retailer.

Not yet confirmed: The interim CEO is not named, no reason is given for the departure, and there is no timetable or process for appointing a permanent successor. It is also unclear whether the statement came from Walmart or from Flipkart — the headline attributes it to Walmart, while the summary attributes it to Flipkart — and a separate account reported that Flipkart called an emergency town hall on the Monday before the announcement amid speculation about the exit, a detail the company has not confirmed.

**Background:** Flipkart is Walmart&\#x27;s main e-commerce holding in India, and Bloomberg describes Krishnamurthy as a key architect of its rise to become the country&\#x27;s No. 1 online retailer. Putting the chief technology officer in the interim role means a technology executive will run the company while a permanent successor is found; the report gives no timetable for that search.

**Why it matters:** Krishnamurthy was the executive most associated with Flipkart&\#x27;s climb to India&\#x27;s largest online retailer, and his exit on December 4 leaves the company under an interim CTO with no named permanent successor. That leadership gap lands while Walmart is still weighing when to list Flipkart: the Economic Times reported Walmart&\#x27;s international CEO saying it was evaluating the right time for an IPO, with Flipkart preparing to move its domicile back from Singapore to India for that purpose. Investors tracking a potential listing should watch whether a permanent CEO is appointed before any filing, since an interim chief during a pre-IPO period complicates diligence and succession messaging.

**What to watch:** Watch the December 4 handover and whether Walmart identifies the interim CTO and a timetable for naming a permanent Flipkart CEO.

<details><summary>References</summary>
<ul>
<li>Flipkart CEO Kalyan Krishnamurthy To Exit After Nearly A Decade</li>
<li><a href="https://economictimes.indiatimes.com/tech/technology/evaluating-the-right-time-for-flipkart-ipo-walmart-international-ceo/articleshow/110185825.cms?from=mdr">Flipkart IPO : Evaluating the right time for Flipkart IPO : Walmart ...</a></li>

</ul>
</details>

**Tags**: `#Flipkart`, `#Walmart`, `#India e-commerce`, `#leadership change`, `#executive turnover`

---

<a id="item-tech-industry-4"></a>
### [Huawei says HarmonyOS passes 100 million installations](https://www.techmeme.com/261125/p7#a261125p7) ⭐️ 7.0/10

Huawei announced that HarmonyOS, its Android-free operating system, has surpassed 100 million installations across smartphones, tablets and PCs, the South China Morning Post reported. The company says the platform offers more than 460,000 apps and services and has more than 12 million registered developers. The milestone is a vendor-reported installation count, not an active-user figure, and no per-device breakdown was provided.

Techmeme · Nov 25, 07:10

**Verified and unconfirmed:** Verified: Huawei said in a statement on Tuesday that HarmonyOS, its Android-free operating system, has passed 100 million installations across smartphones, tablets and PCs, and that its ecosystem offers more than 460,000 apps and services from over 12 million registered developers — figures carried by the South China Morning Post and Xinhua, which also note the current generation followed HarmonyOS 5, introduced in October 2024, with versions 6 and 7 arriving afterwards.

Not yet confirmed: All three figures come from Huawei itself; no independent measurement of installs, app counts or developer registrations is cited, and the reports do not specify the period over which the 100 million accumulated or how installations are counted \(pre-installed devices versus upgrades versus active users\). A separate report that HarmonyOS has overtaken iOS in China rests on a single outlet and is not corroborated by the sources above.

**Background:** HarmonyOS is Huawei&\#x27;s in-house operating system, and the company describes it as Android-free — meaning the release in question is built to run apps made for Huawei&\#x27;s own runtime rather than depending on Android app compatibility, which is why app counts and developer numbers are the figures used to judge whether it can stand alone. The installation total spans smartphones, tablets and PCs, so it reflects an OS shared across several device categories rather than phones alone.

**Why it matters:** For app makers targeting China, the install base makes HarmonyOS a separate platform to assess alongside Android, not an extension of it, because Huawei describes the OS as Android-free. The lack of active-user and device-mix figures means the practical addressable market for any single app remains unclear.

<details><summary>References</summary>
<ul>
<li><a href="https://www.scmp.com/tech/big-tech/article/3375680/huaweis-home-grown-harmonyos-passes-100-million-device-mark-landmark-moment">Huawei’s home-grown HarmonyOS passes 100 million device mark ...</a></li>
<li><a href="https://english.news.cn/20261124/36162a70e643422492296708225f79e1/c.html">Huawei&#x27;s homegrown HarmonyOS tops 100 million devices</a></li>

</ul>
</details>

**Tags**: `#Huawei`, `#HarmonyOS`, `#operating systems`, `#China tech`, `#mobile ecosystem`

---

<a id="item-tech-industry-5"></a>
### [Research links a TikTok mass-shooter &\#x27;true crime&\#x27; network to rising attacks, WIRED reports](https://www.wired.com/story/the-true-crime-community-is-inspiring-violent-attacks-through-tiktok/) ⭐️ 7.0/10

WIRED reported on November 25 that research shared with the magazine shows a network of young people fixated on mass shooters — described as a nihilistic &quot;true crime community&quot; — is using TikTok and AI to spread its message, and that attacks linked to the group are increasing sharply. According to WIRED&\#x27;s account, the network recruits and radicalizes through short-form video and uses AI tools to produce and distribute its material. The report does not name the researchers behind the findings, give a count of linked attacks or a time frame for the increase, or describe how TikTok has responded. The underlying research has not been published, so the claim rests on WIRED&\#x27;s description of work it was shown rather than on an accessible study or independent verification.

Wired · Nov 25, 11:00

**Verified and unconfirmed:** Verified: WIRED reports that research shared with it links a network of young people obsessed with mass shooters to a growing number of violent attacks, and that the group uses TikTok and AI to spread its message.
Not yet confirmed: The identity and methodology of the researchers, the number of attacks and the period over which they increased, the specific role TikTok&\#x27;s recommendation system plays, and any response or takedown action from TikTok — none of these appear in the available account, and no independent replication of the findings exists.

**Background:** The report describes a loose network of young people whose fixation is on mass shooters rather than on the victims or investigations that mainstream true-crime content usually covers, and characterises the group&\#x27;s outlook as nihilistic. Two distribution channels are named: TikTok&\#x27;s short-video feeds and AI tools, which together let the group produce and circulate glorification material faster than conventional moderation can act on it. The research itself is only described as having been shared with WIRED; the excerpt does not name the researchers or institution behind it, give attack counts, or detail how TikTok has responded.

**Why it matters:** The claim points at a moderation gap that content takedowns alone do not close: if the network spreads through recommendation-driven discovery of niche communities rather than through individual rule-breaking videos, platforms would need to target the communities and the AI-generated material themselves. Until the researchers publish their data, platform safety teams, regulators and outside scientists have no way to check the scale of the increase or measure whether any intervention works.

**Tags**: `#platform safety`, `#TikTok`, `#content moderation`, `#AI`, `#violent extremism`

---

<a id="item-tech-industry-6"></a>
### [FISA Section 702 reauthorization may ride on the defense bill](https://www.theverge.com/policy/1041568/fisa-ndaa-blue-wave) ⭐️ 7.0/10

Sen. Mike Rounds \(R-SD\), a member of the Senate Select Committee on Intelligence, told Politico that Section 702 of the Foreign Intelligence Surveillance Act could be attached to the National Defense Authorization Act \(NDAA\), the military spending bill Congress treats as must-pass, as the legislative session runs down. &quot;We don&\#x27;t have two weeks to work just on FISA,&quot; Rounds said, according to The Verge, adding that amending it onto the NDAA would open a path. Section 702 is the authority that lets US intelligence agencies collect the communications of foreigners abroad without individual warrants, which also sweeps in some Americans&\#x27; messages; The Verge reports it has not technically lapsed even though an earlier reauthorization vote failed. No bill text has been filed, and Rounds described only a possible procedural route, not a settled plan.

The Verge · Nov 24, 20:00

**Verified and unconfirmed:** Verified: Rounds, an intelligence committee member, told Politico that Section 702 could be attached to the NDAA, and The Verge reports the authority has not technically lapsed despite a failed reauthorization vote. Not yet confirmed: whether congressional leadership will actually attach the reauthorization, what its text and duration would be, and whether it can pass before the session ends — no filed bill or enacted text is cited, and the quoted remarks are truncated.

**Background:** Section 702 of the Foreign Intelligence Surveillance Act authorizes U.S. intelligence agencies to target non-U.S. persons reasonably believed to be abroad, using programmatic selectors, to acquire foreign intelligence information; the Brennan Center notes that the resulting data has also been used to gain warrantless access to Americans&\#x27; communications. The current reauthorization fight has already drawn opposition to the NDAA route: on Nov. 12, 2026, civil-society and surveillance-reform groups urged lawmakers to keep Section 702 reauthorization out of the NDAA or any other must-pass legislation in the waning days of the 119th Congress.

**Why it matters:** Attaching 702 to the NDAA would force lawmakers who oppose warrantless collection to either accept the reauthorization as part of the defense bill or vote the bill down, rather than fighting it as standalone legislation with room for amendments. For the intelligence agencies whose collection rests on 702 orders, the difference is continuity instead of a lapse.

**What to watch:** Watch the final NDAA text for a 702 reauthorization provision, and whether it emerges before the session ends rather than being pushed into the next Congress.

<details><summary>References</summary>
<ul>
<li><a href="https://www.brennancenter.org/our-work/research-reports/section-702-foreign-intelligence-surveillance-act-fisa-2026-resource-page">Section 702 of the Foreign Intelligence Surveillance Act ...</a></li>
<li><a href="https://www.demandprogress.org/api/media/file/NoFISANDAA.pdf">No FISA in NDAA - demandprogress.org</a></li>

</ul>
</details>

**Tags**: `#FISA 702`, `#surveillance policy`, `#US Congress`, `#NDAA`, `#privacy`

---

<a id="item-tech-industry-7"></a>
### [DOJ announces record anti-scam sweep: 800+ charged, 2,200 trafficking victims freed](https://www.tomshardware.com/tech-industry/cyber-security/us-doj-touts-largest-ever-crackdown-on-scammers-across-the-globe-as-it-seizes-14-000-devices-and-usd17-billion-in-illicit-funds-operation-results-in-800-defendants-and-frees-2-200-forced-laborers) ⭐️ 7.0/10

The U.S. Department of Justice said it has charged more than 800 defendants in over 400 cases filed across 85 federal districts and recovered more than $8 billion in intended victim losses, an action it calls the largest anti-scam crackdown in its history. FBI Director Kash Patel separately described Operation Blackout, an interagency effort that he said dismantled 29 fraud compounds in Asia, Africa and the Middle East, seized almost $17 billion in funds and more than 14,000 devices, and freed more than 2,200 trafficked workers; about 50 people face U.S. federal charges in that operation, and foreign partners arrested or detained more than 320 others. The two money figures are not the same measure: $8 billion is the DOJ&\#x27;s figure for intended victim losses, while $17 billion is the FBI&\#x27;s seizure total for Operation Blackout, and the accounts give no breakdown of how much has been returned to victims. The push follows a March executive order from President Donald Trump requiring a government-wide crackdown on fraud and predatory schemes.

Tom&\#x27;s Hardware · Nov 24, 22:30

**Verified and unconfirmed:** Verified: The Justice Department&\#x27;s own announcement, dated this week, states that federal prosecutors have charged more than 800 defendants in over 400 cases across 85 federal districts, and that more than $8 billion in intended victim losses was recovered; Attorney General Todd Blanche and FBI Director Kash Patel are named as the officials presenting the results, and the DOJ release describes FBI-led Operation Blackout as having restrained nearly $17 billion in illicit funds, seized more than 14,000 digital devices and dismantled 29 scam compounds. Fox News and Yahoo carried the same $8 billion and 800-defendant figures.

Not yet confirmed: No independent audit backs any of the totals, and the two dollar amounts measure different things — roughly $17 billion &quot;restrained&quot; by the FBI versus more than $8 billion in &quot;intended victim losses recovered&quot; from prosecutions — so the headline&\#x27;s framing of a single $17 billion seizure should not be read as money returned to victims. The count of 2,200 trafficked workers freed, the 320-plus arrests by foreign partners and the 50 people facing U.S. charges under Operation Blackout rest solely on FBI statements, and the report does not say how many of the 800 defendants have been convicted versus merely charged.

**Background:** The sweep follows a March executive order by President Donald Trump requiring a government-wide crackdown on fraud and predatory schemes. The &quot;compounds&quot; at the center of Operation Blackout are centralized facilities where, according to the FBI, trafficked workers are forced to run online scams — a model that has made fraud a cross-border, multibillion-dollar business. Tom&\#x27;s Hardware cites Gallup data estimating that Americans lost $68 billion to scams in 2025.

**Why it matters:** The enforcement targets the operating infrastructure rather than individual scammers — the 29 dismantled compounds and the more than 2,200 trafficked workers freed point at the coerced-labor pipeline that staffs many online fraud operations, so the disruption is to the labor supply as much as to the money flow. Victims should not read the seizure figures as restitution: the DOJ describes $8 billion as intended losses, and neither the department&\#x27;s account nor the reporting gives a repayment figure, so anyone defrauded by these networks has no announced route to recover funds from the seizures.

<details><summary>References</summary>
<ul>
<li><a href="https://www.justice.gov/opa/pr/justice-department-announces-largest-ever-crackdown-scammers-targeting-over-800-defendants">Justice Department Announces Largest-Ever Crackdown on ...</a></li>
<li><a href="https://www.foxnews.com/politics/doj-recovers-8b-charges-more-than-800-suspects-largest-anti-scam-surge-history">Justice Department charges 800 in anti-scam crackdown ...</a></li>
<li><a href="https://www.yahoo.com/news/us/articles/us-doj-touts-largest-ever-223000811.html?fr=sycsrp_catchall">US DOJ touts &quot;largest-ever&quot; crackdown on scammers ... - Yahoo</a></li>

</ul>
</details>

**Tags**: `#cybercrime`, `#DOJ`, `#law-enforcement`, `#fraud`, `#policy`

---

