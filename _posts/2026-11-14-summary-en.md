---
layout: issue
permalink: /briefing/2026-11-14/
redirect_from:
  - /2026/11/14/summary-en/
title: "AI News Briefing: November 14, 2026"
date: 2026-11-14
lang: en
---

> We screened 454 AI stories from the past day and kept the 22 worth your time.

---

**AI**
1. [GGML, the tensor library under llama.cpp, reaches v1.0.0](#item-ai-news-1) ⭐️ 8.0/10
2. [Lovable-generated apps exposed passport data and 200K private messages via default keys](#item-ai-news-2) ⭐️ 7.0/10
3. [Anthropic makes Claude Opus 5.5 default, tells users to drop &quot;think hard&quot;](#item-ai-news-3) ⭐️ 7.0/10
4. [Runway open-sources Praxis-1, a robot controller built on video-trained models](#item-ai-news-4) ⭐️ 7.0/10

**Chips &amp; Computing**
1. [U.S. Treasury Secretary questions whether Nvidia knowingly sold GPUs to shell companies](#item-chips-compute-1) ⭐️ 7.0/10
2. [Malaysia plans data-center law to track GPU imports via power use](#item-chips-compute-2) ⭐️ 7.0/10
3. [NPR: Commerce Department pressed over delayed Nvidia chip export controls](#item-chips-compute-3) ⭐️ 7.0/10

**EVs &amp; Energy**
1. [Dongfeng Nissan opens NX7 PHEV orders: ~198 miles electric range, ~$20,000](#item-ev-energy-1) ⭐️ 7.0/10
2. [Tesla Model Y RWD range rises 8.5% to 348 miles at $39,990](#item-ev-energy-2) ⭐️ 7.0/10
3. [Tesla Opens $29,990 Cybercab Orders to Select Customers, With $299/Month Self-Driving](#item-ev-energy-3) ⭐️ 7.0/10
4. [Canada announces $634M for EV charging and $50B grid strategy](#item-ev-energy-4) ⭐️ 7.0/10
5. [UNSW prototypes three-minute lithium-ion battery health test](#item-ev-energy-5) ⭐️ 7.0/10
6. [Masdar completes 365 MW solar-plus-storage Lockhart complex in California](#item-ev-energy-6) ⭐️ 7.0/10
7. [Yanhe Technology puts three perovskite solar module types in orbit](#item-ev-energy-7) ⭐️ 7.0/10

**Space**
1. [SpaceX catches Starship upper stage at launch tower for first time](#item-space-1) ⭐️ 9.0/10
2. [Starship Flight 15 reaches low-Earth orbit; booster catch possible Saturday](#item-space-2) ⭐️ 7.0/10
3. [SpaceX investigating why Starship Flight 15 booster aborted chopsticks catch](#item-space-3) ⭐️ 7.0/10
4. [SpaceX launches 22-hour Starship Flight 15, aborts booster catch](#item-space-4) ⭐️ 7.0/10

**Tech Industry &amp; Policy**
1. [Italy&\#x27;s privacy regulator fines Meta €805M over alleged Android photo and video access](#item-tech-industry-1) ⭐️ 8.0/10
2. [Altimeter and Atreides investors urge Nvidia board to weigh Huang&\#x27;s &quot;potential return&quot;](#item-tech-industry-2) ⭐️ 7.0/10
3. [Sean Duffy Blames FAA Groundstop on Wiring Work and Possible Faulty Router](#item-tech-industry-3) ⭐️ 7.0/10
4. [Microsoft says Microsoft 365 fully restored after global outage](#item-tech-industry-4) ⭐️ 7.0/10

---

## AI

<a id="item-ai-news-1"></a>
### [GGML, the tensor library under llama.cpp, reaches v1.0.0](https://github.com/ggml-org/ggml/releases/tag/v1.0.0) ⭐️ 8.0/10

GGML, the open-source C tensor library that sits underneath llama.cpp and many other local-inference tools, has tagged version 1.0.0 — its first 1.x release. The supplied material contains no release notes, so the specific changes in this version \(API stability guarantees, performance work, or breaking changes\) are not confirmed here. What users describe is cumulative rather than a single leap: one long-time user says monthly upgrades typically bring 5–10% speed gains, and another notes that mixture-of-experts \(MoE\) models slightly larger than the GPU memory budget can keep less-used experts in host memory instead of failing to load.

Hacker News · cobychapple · Nov 14, 02:28 · [Discussion](https://news.ycombinator.com/item?id=50493062)

**Background:** GGML is the C tensor library that supplies the low-level math kernels and hardware backends that llama.cpp and other local-inference tools call to run models. Release coverage reports that the v1.0.0 tag arrives about three and a half years after the project&\#x27;s inception and marks its move to formal semantic versioning, while the release notes listed on a SourceForge mirror describe pruning the deprecated public API and legacy DIAG\_MASK operators alongside new FP8 support and configurable YaRN truncation.

**What changes for local inference:** For builders whose mixture-of-experts model slightly exceeds VRAM, ggml v1.0.0&\#x27;s ability to keep less-used experts in host memory means the model loads and runs instead of failing — but the payoff is conditional: it depends on expert weights sitting in pinned host memory \(Windows pinning limits can stop the cache from activating\), on PCIe bandwidth, and on having enough cache slots to avoid thrashing, and an independent test on a PCIe 3.0 system found it roughly tied with the merged cache. Because ggml reaches hardware through dedicated backends, users on non-CUDA cards, such as Vulkan-only AMD GPUs, remain covered by the same release.

**Community discussion:** Commenters frame the project as the quiet infrastructure of local AI: one user reports that a 50K-token prompt benchmark improved from 4:22 to 3:59 after upgrading, attributing much of the gain to faster prefill with the remainder in token generation, while another praises that GGML-based software remains usable on an older AMD card limited to Vulkan. A third user highlights the practical memory behavior for MoE models that slightly exceed GPU capacity, describing expert offloading to host memory as a load-saving fallback rather than a guarantee of speed.

<details><summary>References</summary>
<ul>
<li><a href="https://sourceforge.net/projects/ggml.mirror/files/v1.0.0/">ggml - Browse /v1.0.0 at SourceForge.net</a></li>
<li><a href="https://af.net/realtime/ggml-org-releases-llama-cpp-v1-0-0-and-ggml-v1-0-0-with-strict-semantic-versioning/">ggml-org Releases llama.cpp v1.0.0 and ggml v1.0.0 with ...</a></li>
<li><a href="https://www.youtube.com/watch?v=ohp15NcKDhA">llama . cpp Just Made Huge MoE Models 4× Faster - YouTube</a></li>
<li><a href="https://huggingface.co/blog/ggml-org/llama-cpp-v1">llama . cpp v 1 . 0 . 0 : A stronger foundation for the local AI ecosystem</a></li>

</ul>
</details>

**Tags**: `#open-source AI`, `#local inference`, `#llama.cpp`, `#GGML`, `#model runtime`

---

<a id="item-ai-news-2"></a>
### [Lovable-generated apps exposed passport data and 200K private messages via default keys](https://www.crissyfield.de/research/lovable-en/) ⭐️ 7.0/10

Security research on Lovable, an AI app builder, found that many apps it generated exposed sensitive user data—including passport details and more than 200,000 private messages—through publicly shipped read-only API keys and permissive Supabase defaults. The issue affects people using those generated apps, not a failure of the underlying model, and centers on Supabase, the hosted database and authentication service many such apps rely on. The write-up&\#x27;s author confirmed the post on Hacker News, but the available account does not specify how many apps were affected or whether the exposed data has been secured.

Hacker News · armcat · Nov 14, 17:43 · [Discussion](https://news.ycombinator.com/item?id=50499017)

**Context:** Lovable is an AI app builder that generates full web applications and can connect them to Supabase, a hosted Postgres backend with authentication and auto-generated APIs. Such apps ship a read-only Supabase API key in the browser, so that key is public by design; what it can read is supposed to be limited by row-level security, the per-table rules that filter database rows. A commenter on the item argued that Supabase chose permissive defaults years ago to ease onboarding and that existing projects may still retain them.

**Check your Supabase defaults:** Builders who shipped Lovable apps on stock Supabase settings should assume the public anon key bundled in their client code can read more than intended: a Supabase maintainer discussion notes that under default settings it is &quot;quite easy&quot; for anonymous users to probe an API, with the caveat that requests still need a valid JWT. The practical remediation is to enable row-level security and restrict the anon role&\#x27;s access rather than relying on the key being labeled read-only.

**Community discussion:** Commenters debated whether the exposure should be called a breach: one argued that reading data made public by a shipped read-only API key is not hacking and that the publication itself is the leak, while another blamed Supabase&\#x27;s permissive defaults and said an October 30 fix may not cover existing projects. Others described AI-generated apps as easy, numerous targets whose users often do not understand the risk, and called for deny-by-default databases, least-privilege APIs, and automated authentication tests.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.lovable.dev/integrations/supabase">Connect to Supabase - Lovable Documentation</a></li>
<li><a href="https://github.com/orgs/supabase/discussions/4547">Option to disable anon key access to database · supabase ...</a></li>

</ul>
</details>

**Tags**: `#AI app builders`, `#security vulnerability`, `#Lovable`, `#Supabase`, `#data exposure`

---

<a id="item-ai-news-3"></a>
### [Anthropic makes Claude Opus 5.5 default, tells users to drop &quot;think hard&quot;](https://the-decoder.com/anthropic-says-outdated-prompting-habits-are-slowing-down-claude-opus-5-5/) ⭐️ 7.0/10

Anthropic has made Claude Opus 5.5 the default model on all paid plans and published a prompting guide that advises retiring older habits. The headline recommendation is to stop using instructions like &quot;think hard&quot; and instead start at Medium effort. The Decoder&\#x27;s report relays Anthropic&\#x27;s own announcement and does not include benchmarks or measurements showing how much the older prompting style actually costs users. The guidance is therefore a vendor recommendation rather than an independently verified result.

The Decoder · Nov 14, 16:42

**Why old prompting habits carried over:** Earlier Claude models required explicit instructions such as &quot;think hard&quot; to trigger deeper reasoning, so users built prompts around coaxing more deliberation out of the model. Anthropic&\#x27;s guidance for Opus 5.5 describes a different setup: thinking is always on, reasoning depth is set through effort levels from low to max, and the model defaults to medium effort. One analysis of those levels reports that Opus 5.5 at medium effort beats Opus 5 at high effort, which is why guidance now points users to start at medium rather than pushing for maximum reasoning.

**Impact:** Paid-plan users will now reach Opus 5.5 without selecting it, so existing prompts and saved templates that lean on &quot;think hard&quot; phrasing should be re-checked against the new Medium-effort starting point rather than carried over unchanged.

<details><summary>References</summary>
<ul>
<li><a href="https://betterstack.com/community/guides/ai/claude-opus-55-prompting-guide/">How to Prompt Claude Opus 5.5: What Changed and What to ...</a></li>
<li><a href="https://www.techgeum.com/blog/ai/claude-opus-5-5-effort-levels">Claude Opus 5.5 Effort Levels: Low to Max Explained</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#Claude Opus 5.5`, `#prompting`, `#model defaults`, `#developer guidance`

---

<a id="item-ai-news-4"></a>
### [Runway open-sources Praxis-1, a robot controller built on video-trained models](https://the-decoder.com/runways-open-source-praxis-1-turns-video-ai-into-a-robot-controller/) ⭐️ 7.0/10

Runway released Praxis-1, a robotics model published with open weights and source code under the Apache 2.0 license, which the company says adapts knowledge learned from video training into robot control. According to the report, Praxis-1 leads the World Action Model category on Nvidia&\#x27;s RoboLab-120 benchmark. The stated limitation is that the model cannot yet plan complex action sequences on its own, so it acts as a controller rather than an autonomous task planner. The Decoder&\#x27;s coverage is brief and the benchmark placement is attributed to the release rather than described as an independent evaluation.

The Decoder · Nov 14, 09:45

**What a world action model is:** Praxis-1 belongs to a category Runway calls &quot;world action models&quot; \(WAMs\), which learn control from video rather than only from paired robot-action recordings; Runway says it is the top-performing WAM on Nvidia&\#x27;s RoboLab-120 leaderboard and beats every open-weight vision-language-action \(VLA\) model, the competing family that maps camera images plus text instructions directly to motor commands. RoboLab-120, the benchmark behind that claim, is an Nvidia set of 120 tasks spanning pick-and-place, stacking, rearrangement and tool use, each with language instructions and automated success/failure detection. A secondary report puts the released model at 27 billion parameters with a 46.2% success rate on that benchmark.

**Impact:** Because Praxis-1 ships under Apache 2.0 with both weights and source code, developers can inspect, modify, and deploy it without copyleft obligations or a vendor API, which matters for teams that need on-premise or custom robot stacks. The acknowledged lack of independent multi-step planning means users would still need to supply a higher-level planner or scripted task decomposition to drive it through longer sequences.

<details><summary>References</summary>
<ul>
<li><a href="https://runway.com/news/company-news/praxis-1-is-now-available">Runway Praxis - 1 Is Now Available: Open-Weight Robotics Model</a></li>
<li><a href="https://devtrends.ru/news/runway-otkryla-vesa-robototexniceskoi-modeli-praxis-1-pod-apache-20">Runway открыла веса робототехнической модели Praxis - 1 под...</a></li>
<li><a href="https://github.com/meadowshn/RoboLab_">GitHub - meadowshn/ RoboLab _ · GitHub</a></li>

</ul>
</details>

**Tags**: `#Runway`, `#Praxis-1`, `#open-source AI`, `#robotics`, `#video models`

---

## Chips &amp; Computing

<a id="item-chips-compute-1"></a>
### [U.S. Treasury Secretary questions whether Nvidia knowingly sold GPUs to shell companies](https://www.tomshardware.com/tech-industry/artificial-intelligence/u-s-treasury-secretary-questions-whether-nvidia-knowingly-sold-ai-gpus-to-shell-companies-says-company-itself-is-responsible-i-think-it-is-important-that-anyone-at-the-company-there-be-held-accountable-for-that) ⭐️ 7.0/10

In a CNBC interview, U.S. Treasury Secretary Scott Bessent said export controls cannot stop all restricted hardware from reaching China, but argued the focus should shift from Jensen Huang&\#x27;s &quot;personal foibles&quot; to whether Nvidia knew its customers were &quot;obviously pass-through shell companies&quot; and whether it made a &quot;robust effort&quot; to prevent leakage — adding that &quot;anyone at the company there be held accountable.&quot; Bessent said it is not known whether Huang himself knew, declined to speculate on consequences for Nvidia, and said he expects the company&\#x27;s board to investigate; he also criticized Nvidia general counsel Timothy Teter for contacting the Commerce Department over the detention of Megaspeed&\#x27;s Alice Wong in Singapore, saying Teter &quot;probably should have done more oversight rather than the haranguing.&quot; Bessent said he does not favor new restrictions or added agency powers, arguing existing rules should be enforced instead, and said Treasury, War, and State departments and the USTR had backed adding Megaspeed to the Entity List for months, while the Commerce Department&\#x27;s Bureau of Industry and Security — which holds that authority — reportedly stalled the move. The remarks are criticism and questioning rather than a new enforcement action or documented finding against Nvidia; the article&\#x27;s premise that China obtained millions of restricted GPUs is an allegation it attributes to prior reporting.

Tom&\#x27;s Hardware · Nov 14, 15:35

**Export-control context:** U.S. export controls prohibit Nvidia and other chipmakers from selling advanced AI GPUs to China without authorization, and the Commerce Department’s Bureau of Industry and Security \(BIS\) maintains the Entity List of parties subject to additional restrictions. Enforcement depends on identifying the true end customer, which makes pass-through or shell-company buyers a central concern in diversion cases.

**Enforcement gap persists:** For Nvidia and its distributors, the operative question is whether Megaspeed — the Singapore company at the center of the diversion allegations — is actually blacklisted: Reuters reported that Treasury and three other agencies backed adding it to the Entity List, but the authority sits with Commerce&\#x27;s Bureau of Industry and Security, and no listing has been imposed. Until that changes, U.S. suppliers remain legally permitted to ship to such intermediaries, so the burden falls on Nvidia&\#x27;s own customer vetting rather than on a government prohibition.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reuters.com/business/retail-consumer/bessent-says-treasury-favored-limits-megaspeed-2026-11-13/">Bessent blames Commerce Dept over lack of export controls for ...</a></li>
<li><a href="https://www.siliconreport.com/bessent-says-agencies-favored-putting-megaspeed-on-entity-list">Bessent says agencies favored putting Megaspeed on entity list</a></li>
<li><a href="https://explainx.ai/blog/bessent-blames-commerce-megaspeed-entity-list-lutnick-ouster-talks-nvidia-huang-2026">Bessent Blames Lutnick Over Megaspeed Entity List (Nov 13 ...</a></li>

</ul>
</details>

**Tags**: `#export controls`, `#Nvidia`, `#AI GPUs`, `#supply chain`, `#U.S. policy`

---

<a id="item-chips-compute-2"></a>
### [Malaysia plans data-center law to track GPU imports via power use](https://www.tomshardware.com/tech-industry/artificial-intelligence/malaysia-plans-new-law-using-data-center-power-consumption-to-catch-ai-gpu-smugglers-but-real-world-tdp-variance-and-lack-of-physical-audits-could-undermine-it-new-law-also-forces-operators-to-pay-for-unused-electricity-capacity) ⭐️ 7.0/10

Malaysia plans to require data-center operators to disclose AI accelerator imports, power consumption, facility locations, and the identities of operators and hyperscale customers under a new law aimed at detecting GPUs diverted to export-restricted countries such as China. The Digital Ministry is reviewing existing legislation to determine whether authorities can act against re-exporters, and the proposal would also make operators pay for all electricity capacity they reserve, whether or not it is used; Malaysia has approved 117 data-center projects, 55 of them operational, according to the trade minister. The minister said authorities would cooperate with U.S. counterparts and provide information about facilities housing particular GPUs, but it is unspecified whether operators must report GPU models and serial numbers or whether Malaysia will conduct on-site inspections. The article notes that power data alone cannot reliably count accelerators because rated wattage varies—Nvidia&\#x27;s H100 and H200 SXM GPUs are rated at 700W, while B200 SXM is rated at 1,000W—and actual draw depends on workloads, server configuration, and facility power usage effectiveness.

Tom&\#x27;s Hardware · Nov 14, 15:10

**Background:** Malaysia introduced export controls on advanced US-origin AI chips in 2025 following diplomatic pressure from Washington, and in June 2026 Malaysian authorities foiled an attempt to smuggle nearly $13 million in AI servers through Kuala Lumpur. The proposed disclosure law extends that enforcement approach from border seizures to the data-center level, where restricted accelerators can be imported legally and then diverted.

**Impact:** For data-center operators in Malaysia, the plan would turn reserved electricity capacity into a paid commitment and add disclosure of facility locations and customer identities; until the law is finalized, it remains unclear whether they would also have to report GPU models and serial numbers or submit to physical inventory audits.

<details><summary>References</summary>
<ul>
<li><a href="https://factlen.com/news/malaysian-customs-seize-12-1-million-in-smuggled-ai-chips-at-kuala-lumpur-airpor-38681-96d95b54">Malaysian Customs Seize $12.1 Million in Smuggled AI Chips at</a></li>

</ul>
</details>

**Tags**: `#export controls`, `#AI GPUs`, `#data centers`, `#Malaysia`, `#power consumption`

---

<a id="item-chips-compute-3"></a>
### [NPR: Commerce Department pressed over delayed Nvidia chip export controls](https://news.google.com/rss/articles/CBMiwgFBVV95cUxPcjdnek9mQmRSSGo0bmFxaVRBcmVzbEdEbkwxV3FWNFdGa1A1T1QyN2ZZZ2d1aE9jVm0xTjA4NlowU2xsSVFzUHZFMmZ2WGNRWXdzVHh2dmh1T3Z3a0FKamNMYXRnaDRJUzFlUU5YZFhJbEJmREViR3ZEdDlVTk9TUmdmWGJqQ2xicE9tekdpajIyLVgtb3B6TGFTdE9fQVZxWGdSY3pDQWFzZW1hRy16ME85b0cxT3pCVHdZcFNxUFB6dw?oc=5) ⭐️ 7.0/10

NPR reports that the US Commerce Department is facing pressure for delaying export controls on Nvidia chips, according to a headline carried in a chip-industry news feed. The supplied material contains only that headline: it names no officials applying the pressure, no date for the delay, no indication of which specific controls are affected, and no response from Commerce or Nvidia. It should therefore be treated as a reported, developing policy story rather than a confirmed change to export rules. No details on scope, timing, or the legal mechanism involved could be verified from the available content.

Google News: chips · Nov 14, 22:21

**Background:** US curbs on advanced AI chip exports are run through the Commerce Department, whose Bureau of Industry and Security keeps the Entity List: once a firm is on it, US suppliers need a license before selling to it. The pressure on Commerce follows reporting that the department held back adding the cloud-computing firm Megaspeed to that list, with Treasury Secretary Scott Bessent publicly blaming Commerce for Nvidia chip sales to China. CNBC also reported that Jensen Huang, who resigned as Nvidia CEO amid the Megaspeed scandal, had pushed to ease restrictions on exporting advanced AI chips to China.

**Enforcement exposure:** For companies that ship or buy high-end AI chips, the immediate effect is that the existing licensing regime stays in place while the new controls are held up — and the delay has become a cabinet-level dispute, with Treasury Secretary Scott Bessent publicly blaming Howard Lutnick&\#x27;s Commerce Department for failing to properly oversee exports of high-spec AI chips. The department&\#x27;s enforcement record is also under separate scrutiny, with the New York Times reporting that a Commerce Department inquiry into Megaspeed was halted after Nvidia intervened, a precedent that raises questions about how firmly any new rule would be applied once issued.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/cqvg2d1eg7zro">Bessent blames Lutnick&#x27;s department for Nvidia chip sales to...</a></li>
<li><a href="https://www.theguardian.com/technology/2026/nov/13/nvidia-scandal-sparks-us-national-security-concerns-china">Nvidia scandal: US treasury chief blames Lutnick’s commerce ...</a></li>
<li><a href="https://www.cnbc.com/2026/11/13/us-inflation-outlook-federal-reserve-rate-hike.html">Bessent blames Lutnick’s Commerce , slams Nvidia chip China leakage</a></li>
<li><a href="https://www.bbc.com/news/articles/cqvg2d1eg7zro">Bessent blames Lutnick&#x27;s department for Nvidia chip sales to...</a></li>
<li><a href="https://www.nytimes.com/2026/11/09/business/economy/nvidia-megaspeed-investigation-huang.html">U.S. Commerce Dept . Inquiry Into Megaspeed Was Halted After...</a></li>

</ul>
</details>

**Tags**: `#export controls`, `#Nvidia`, `#AI chips`, `#US-China tech policy`, `#semiconductor supply chain`

---

## EVs &amp; Energy

<a id="item-ev-energy-1"></a>
### [Dongfeng Nissan opens NX7 PHEV orders: ~198 miles electric range, ~$20,000](https://electrek.co/2026/11/14/20k-nissan-nx7-phev-goes-on-sale-with-nearly-200-miles-of-electric-range/) ⭐️ 7.0/10

Dongfeng Nissan opened early orders for the NX7 plug-in hybrid \(PHEV\), claiming up to 320 km \(about 198 miles\) of all-electric driving from a 40 kWh lithium iron phosphate \(LFP\) battery at a price of roughly $20,000. Both the range and the price are the company&\#x27;s own announced figures at the start of pre-orders, not independently tested results or confirmed final trim pricing, and the report gives no delivery timeline or market availability beyond the Chinese order book.

Electrek · Nov 14, 21:26

**Context: big-battery PHEVs and the NX7&\#x27;s earlier specs:** A plug-in hybrid \(PHEV\) pairs a gasoline engine with a grid-chargeable battery, so a larger pack lets more of a driver&\#x27;s miles happen on electricity alone; the NX7&\#x27;s 40 kWh lithium iron phosphate \(LFP\) pack is unusually large for the segment, and LFP chemistry trades some energy density for lower cost and longer cycle life. Earlier coverage of the Dongfeng Nissan NX7 described a 40.95 kWh battery with 225 km of CLTC electric range, and CarNewsChina reported that pre-sales opened on November 13 across three trims priced from 129,900 to 149,900 yuan \(about $19,400–$22,400\), with a formal launch scheduled for the Guangzhou Auto Show on November 27. The roughly 320 km figure in the current report is higher than that earlier number, and the item does not explain the difference.

<details><summary>References</summary>
<ul>
<li><a href="https://carnewschina.com/2026/11/13/nissan-opens-pre-sales-for-nx7-phev-in-china-with-320-km-ev-range-1666-km-combined/">Nissan opens pre-sales for NX 7 PHEV in China with 320 km EV range...</a></li>
<li><a href="https://theelectricviking.com/dongfeng-nissan-nx7-phev-revealed-225-km-electric-range-new-hybrid/">Dongfeng Nissan NX 7 PHEV Revealed With 225 km Electric Range...</a></li>

</ul>
</details>

**Tags**: `#Nissan NX7`, `#PHEV`, `#LFP battery`, `#EV pricing`, `#China EV market`

---

<a id="item-ev-energy-2"></a>
### [Tesla Model Y RWD range rises 8.5% to 348 miles at $39,990](https://www.notateslaapp.com/news/5017/tesla-model-y-rwd-gets-increased-range-at-same-price) ⭐️ 7.0/10

Tesla has raised the EPA-estimated range of the Model Y rear-wheel-drive version by 8.5%, from roughly 321 miles to 348 miles, while keeping the U.S. starting price at $39,990, according to Not a Tesla App. The report does not say whether the gain comes from a hardware change, a software update, or revised testing or rating procedures, and it cites no primary Tesla confirmation of the figure. The increase applies to the EPA estimate for the entry Model Y, Tesla&\#x27;s highest-volume vehicle, at an unchanged sticker price.

Not a Tesla App · Nov 14, 22:06

**Prior rating and lineup context:** Tesla&\#x27;s current-generation Model Y, the &quot;Juniper&quot; refresh, had been listed with a 321-mile EPA range for the rear-wheel-drive version starting at $39,990, according to Edmunds&\#x27; 2026 model overview, so the 348-mile figure is an increase over an existing rating rather than a new trim or battery option. The change also follows Tesla&\#x27;s removal of the $41,990 all-wheel-drive Model Y configuration from its configurator a day earlier, which left the rear-wheel-drive version as the lineup&\#x27;s entry point, Electrek reported.

**Impact:** Buyers of the base Model Y now get about 27 more EPA-estimated miles for the same $39,990, which narrows the range gap to pricier trims without changing the entry price. Because the report does not identify the source of the gain, owners of existing Model Y RWD cars have no indication from this account whether an over-the-air update would deliver the same range or whether it depends on new hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://electrek.co/2026/11/13/tesla-kills-41990-model-y-awd-configurator/">Tesla kills $41, 990 Model Y AWD: all- wheel drive now costs... | Electrek</a></li>
<li><a href="https://www.edmunds.com/tesla/model-y/">2026 Tesla Model Y Prices, Reviews, and Pictures | Edmunds</a></li>

</ul>
</details>

**Tags**: `#Tesla`, `#Model Y`, `#EV range`, `#pricing`, `#EPA ratings`

---

<a id="item-ev-energy-3"></a>
### [Tesla Opens $29,990 Cybercab Orders to Select Customers, With $299/Month Self-Driving](https://insideevs.com/news/815473/tesla-cybercab-pricing-sales-announced/) ⭐️ 7.0/10

Tesla has reportedly opened orders for its Cybercab to &quot;select customers&quot; at $29,990, which would make it the company&\#x27;s cheapest vehicle, according to InsideEVs. Autonomous driving is not included in that price: the report pegs it at $299 per month. The source is a brief report and does not specify how customers qualify for an order, when deliveries begin, or whether the $29,990 figure is before taxes and incentives; the pricing and order access have not been independently confirmed in the supplied material.

InsideEVs · Nov 14, 00:06

**Background:** The Cybercab is Tesla&\#x27;s lowest-priced vehicle in this pricing scheme, at $29,990. Tesla is treating autonomous driving as a separate subscription rather than bundling it into the sticker price, so the $299 monthly fee is a recurring cost on top of the purchase price.

**What buyers are actually committing to:** For a personal-use buyer, the $29,990 price is not the full cost: the $299 monthly autonomous-driving subscription is described as mandatory, and the car reportedly operates only inside Tesla&\#x27;s Robotaxi geofences, so personal use is limited to mapped service areas rather than anywhere the owner drives. Prospective buyers should confirm the geofence boundaries and subscription terms for their own address before placing a pre-order.

<details><summary>References</summary>
<ul>
<li><a href="https://electrek.co/2026/11/13/tesla-cybercab-personal-use-orders-299-subscription-geofence/">Tesla Cybercab orders open at $29,990 + $299/mo, only in ...</a></li>
<li><a href="https://techcrunch.com/2026/11/14/tesla-opens-cybercab-pre-orders-for-personal-use-with-geo-restrictions-and-a-299-monthly-fee/">Tesla opens Cybercab pre-orders ‘for personal use,’ with geo ...</a></li>

</ul>
</details>

**Tags**: `#Tesla`, `#Cybercab`, `#autonomous driving`, `#EV pricing`, `#vehicle orders`

---

<a id="item-ev-energy-4"></a>
### [Canada announces $634M for EV charging and $50B grid strategy](https://www.electrive.com/2026/11/14/canada-invests-billions-in-charging-infrastructure-and-grid-upgrades/) ⭐️ 7.0/10

Canada has announced just over $634 million to expand electric-vehicle charging infrastructure and grid capacity, with the charging funding intended to roughly double the more than 50,000 chargers supported through existing federal programs. The government is pairing that with a national electricity strategy that targets more than $50 billion to double Canada&\#x27;s grid capacity by 2050. The item describes announced investment and targets, not completed construction or measured charger counts; it does not give a timeline for the charging expansion or specify how the money will be split.

Electrive · Nov 14, 13:00

**Background:** Public charging in Canada has so far been built largely through government support programmes; the source notes that existing programmes have backed more than 50,000 chargers, a number the new funding is meant to roughly double. &quot;Grid capacity&quot; refers to how much electricity a network can deliver at times of peak demand, so adding chargers and electrifying transport raises the upstream requirement on transmission and distribution infrastructure as well as on charging sites themselves.

**Impact:** For Canadian EV drivers and charging operators, the intended consequence is that the federally supported public charger base would grow from more than 50,000 to roughly 100,000, though the source does not say when the new chargers will be operational or where they will be located.

**Tags**: `#EV charging infrastructure`, `#Canada`, `#grid upgrades`, `#government policy`, `#clean energy investment`

---

<a id="item-ev-energy-5"></a>
### [UNSW prototypes three-minute lithium-ion battery health test](https://www.pv-magazine.com/2026/11/14/unsw-develops-three-minute-lithium-ion-battery-health-test/) ⭐️ 7.0/10

University of New South Wales researchers have prototyped a three-minute lithium-ion battery health test that they say is 95.5% faster and more than 80% cheaper than the roughly 10-hour full charge-discharge testing used today, which costs about AUD 120 per EV battery pack. The system sends short electrical pulses through individual cells and uses statistical models to estimate health in under three minutes per cell, with more than 90% accuracy in lab tests; it is designed for LFP, NCA, and NMC chemistries and to work with battery-management systems already used by recyclers and storage operators. The researchers are targeting a cost under AUD 25, but the results remain prototype and lab claims rather than independently validated or commercially deployed performance. UNSW and DY New Energy have partnered on an AUD 1.3 million project to test the approach on more than 500 batteries in real-world conditions, alongside a machine-learning reuse-or-recycle decision engine and an iBMS module for real-time monitoring.

pv magazine · Nov 14, 10:47

**Why battery health checks are slow:** A used EV battery’s state of health determines whether it is suitable for second-life use in stationary storage or should go to recycling. The conventional check requires a full charge–discharge cycle, which takes about 10 hours and places aged cells under sustained stress.

**Impact:** For recyclers and second-life storage operators, the near-term test is operational: the platform is meant to handle mixed, unsorted LFP/NCA/NMC batches and connect to existing battery-management systems, so the planned 500-plus-battery field trial must show that the lab&\#x27;s more-than-90% accuracy holds on the packs operators actually receive.

**Tags**: `#battery health testing`, `#lithium-ion batteries`, `#second-life EV batteries`, `#battery recycling`, `#UNSW`

---

<a id="item-ev-energy-6"></a>
### [Masdar completes 365 MW solar-plus-storage Lockhart complex in California](https://www.pv-magazine.com/2026/11/14/masdar-completes-950-million-solar-and-battery-storage-project-in-california/) ⭐️ 7.0/10

Masdar announced completion of the $950 million Lockhart Solar and Storage complex in California, pairing 365 MW of solar photovoltaic generation with 173.7 MW of battery storage. The project was developed by Terra-Gen, which Masdar jointly owns with Igneo Infrastructure Partners, and is designed to generate enough electricity for roughly 350,000 homes and businesses. Its output is contracted through a mix of long-term power purchase agreements with California load-serving entities and corporate offtake agreements, and construction spanned about four years, peaking above 1,000 on-site jobs. Masdar says it has invested roughly $3 billion in the U.S. so far and plans another $20 billion over the next decade, targeting up to 25 GW of U.S. renewable capacity by 2030 — targets, not yet built capacity.

pv magazine · Nov 14, 09:30

**Context:** Solar-plus-storage plants pair PV panels with batteries that charge on surplus midday generation and discharge later, typically into evening peaks; here the battery capacity \(173.7 MW\) is roughly half the solar capacity \(365 MW\). The developer, Terra-Gen, is jointly owned by Masdar and Igneo Infrastructure Partners, so the completed Lockhart complex sits inside a portfolio Masdar already co-owns rather than marking a new market entry. Masdar says it has invested about $3 billion in the U.S. to date.

**Impact:** Because the output is already sold under long-term utility and corporate agreements, the new capacity enters the contracted supply of California load-serving entities and corporate buyers rather than the merchant market. The article does not disclose the battery&\#x27;s storage duration, so how much solar energy the 173.7 MW can shift into evening peaks — the main grid-stability value of pairing storage with PV — remains unquantified. Masdar also projects the facility will deliver upwards of $40 million in local property tax revenue over its operating life.

**Tags**: `#solar-plus-storage`, `#utility-scale batteries`, `#California`, `#Masdar`, `#Terra-Gen`

---

<a id="item-ev-energy-7"></a>
### [Yanhe Technology puts three perovskite solar module types in orbit](https://www.pv-magazine.com/2026/11/14/yanhe-technology-launches-three-perovskite-solar-module-technologies-into-orbit/) ⭐️ 7.0/10

Yanhe Technology launched three independently developed space photovoltaic modules on Nov. 7 into a 535 km sun-synchronous orbit aboard Galactic Energy&\#x27;s Ceres-2 Y3 rocket from the Jiuquan Satellite Launch Center. Two tandem modules — perovskite-crystalline silicon and perovskite-CIGS — are mounted on the North University of China-1 satellite, which flies a dawn-dusk orbit with near-continuous sunlight, while a flexible single-junction perovskite module rides on Yunyao-1 28 for imaging during thermal cycling and monitoring of degradation from particle radiation and atomic oxygen. The company called it China&\#x27;s first simultaneous in-orbit validation of three perovskite-based PV technologies, but did not disclose conversion efficiencies, rated power, active areas, or weights, and has not specified how long the monitoring campaign will run or how much telemetry is expected. The mission follows a September deployment of a flexible perovskite module on the Tianyi-52 satellite, which Yanhe described as China&\#x27;s first component-level in-orbit test of flexible perovskite PV.

pv magazine · Nov 14, 07:30

**Why perovskites in orbit:** Perovskite solar cells are thin-film photovoltaic devices that can be made lightweight and potentially cheap, while a tandem module stacks a perovskite layer on another absorber—crystalline silicon or CIGS \(copper indium gallium selenide\)—to capture more of the solar spectrum. Spacecraft conventionally use III-V gallium arsenide cells, and the open question for perovskites is whether they can retain performance under radiation and repeated thermal cycling. Yanhe&\#x27;s September campaign put a flexible perovskite module on the Tianyi-52 satellite; the new flight adds two tandem designs and a second flexible single-junction device.

**Impact:** The three-way comparison is meant to show satellite power designers whether perovskite tandems can compete with the III-V gallium arsenide cells commonly used in satellite power systems, and Yanhe is assessing the fully thin-film perovskite-CIGS design for flexibility and radiation resistance relative to silicon-based tandems. Until efficiencies and degradation data are published, however, the architectures remain unproven under prolonged radiation exposure and repeated thermal cycling, the conditions the mission is designed to test.

**Tags**: `#perovskite solar`, `#space photovoltaics`, `#solar modules`, `#in-orbit validation`, `#China solar`

---

## Space

<a id="item-space-1"></a>
### [SpaceX catches Starship upper stage at launch tower for first time](https://x.com/i/broadcasts/2brajgZlOKRMka) ⭐️ 9.0/10

SpaceX caught the Starship upper stage, Ship 42, with the chopstick arms of its Starbase launch tower on Nov. 14, 2026, about 22.5 hours after liftoff—the first time an orbital rocket&\#x27;s upper stage has returned to its launch site and been caught. Ship 42 reached orbit, deployed all 26 Starlink V3 satellites, and used three camera-carrying satellites to inspect its heat shield; SpaceX said the images looked good enough to pass on a backup splashdown, and the ship fired its engines after about 14 orbits to reenter and be caught. The booster did not make it back: Super Heavy aborted its catch attempt over a guidance issue and ran short on propellant, splashing down in the Gulf of Mexico, and Elon Musk said the fix is better engine consistency with Raptor V3.2 plus a software change to cut the engines about one second earlier. Super Heavy has been caught three times, most recently in March 2025, but every previous Ship ended in the ocean or was lost; Flight 14 in September reached orbit but splashed down in the Pacific after about three hours when some engines shut down.

Hacker News · ls612 · Nov 14, 21:22 · [Discussion](https://news.ycombinator.com/item?id=50500963)

**Background:** SpaceX&\#x27;s tower catch uses the launch tower&\#x27;s “chopstick” arms to grab a descending rocket stage instead of landing it on legs, a key step toward rapid reuse. Before Flight 15, SpaceX had caught the Super Heavy booster three times, most recently in March 2025, but had never attempted the maneuver with the upper stage, which returns from orbital velocity and is a harder target. The previous Starship mission, in September, reached orbit but splashed down in the Pacific after about three hours when some engines shut down.

**Impact:** NASA&\#x27;s Artemis lunar lander depends on refilling Starship in orbit with repeated tanker flights, so a Ship that can return to the tower is a prerequisite for that architecture. The catch does not yet prove the economics: SpaceX has caught a Ship once and Super Heavy three times, but it has not demonstrated re-flying the same vehicle or the rapid turnaround that a tanker cadence would require; Musk has said he expects weekly Starship launches in the first half of 2027.

**Community discussion:** Commenters treated the catch as a turning point but focused on the unproven next steps: small\_model argued the cost gains depend on the heat shield holding up and on re-flying the same ships, while hinkley said he was disappointed SpaceX is not pursuing landing gear and doubted that approach could scale to heavier rockets. Others were celebratory, with codeulike noting &quot;dont panic&quot; written on the fuselage.

**Tags**: `#SpaceX`, `#Starship`, `#tower catch`, `#reusability`, `#Flight 15`

---

<a id="item-space-2"></a>
### [Starship Flight 15 reaches low-Earth orbit; booster catch possible Saturday](https://arstechnica.com/space/2026/11/starship-flight-15-powers-to-orbit-setting-up-a-possible-catch-on-saturday/) ⭐️ 7.0/10

SpaceX&\#x27;s 15th Starship test flight lifted off from Starbase, Texas, on Friday and reached a nominal low-Earth orbit after a flawless first-stage ascent. The booster released the upper stage above the Gulf of Mexico, and the upper stage then ignited its Raptor engines; Ars Technica reports this was the second time Starship has flown to low-Earth orbit. A booster catch attempt is described as possible on Saturday, not as having already happened.

Ars Technica · Nov 14, 00:49

**Why an orbital flight matters:** Starship is SpaceX&\#x27;s two-stage, fully reusable launch system: a Super Heavy first stage and a Starship upper stage, both designed to return and fly again rather than be expended. Reaching low-Earth orbit is the prerequisite for the missions SpaceX has sold the vehicle for, including deploying satellites and refueling a tanker in orbit for lunar missions. Flight 15 was the 15th test flight in a little over three years, an iterative campaign in which each launch is meant to retire specific risks before the next attempt.

**Tags**: `#Starship`, `#SpaceX`, `#orbital test flight`, `#reusable launch`, `#Starbase`

---

<a id="item-space-3"></a>
### [SpaceX investigating why Starship Flight 15 booster aborted chopsticks catch](https://www.space.com/space-exploration/launches-spacecraft/spacex-says-starship-flight-15-booster-aborted-chopsticks-landing-catch-after-launch-due-to-guidance-issue-video) ⭐️ 7.0/10

SpaceX is investigating why the Super Heavy booster on Starship Flight 15, Booster 22, aborted its planned tower &quot;chopsticks&quot; catch and was destroyed over the Gulf of Mexico about 6.5 minutes after lifting off from Starbase, Texas, on Nov. 13. The flight had aimed to recover both the booster and the Ship upper stage for what the company billed as the first full recovery of an orbital launch system. SpaceX&\#x27;s Dan Huot first attributed the abort to a guidance issue, then said a day later that the booster&\#x27;s guidance and navigation control \(GNC\) system worked as intended: it detected the booster was not where it needed to be for a catch, triggered an automatic abort and sent it to an offshore contingency splashdown. On Nov. 14, SpaceX&\#x27;s Kate Tice said early indications are that the booster ended its boostback burn early because of a low fuel mass alarm, with the root cause still under investigation; one of 33 engines dropped out after stage separation, leaving 32 for the boostback burn, after all 33 fired on ascent.

Space.com · Nov 14, 14:53

**Background:** Super Heavy is Starship&\#x27;s first stage, and after stage separation it flips and fires a &quot;boostback&quot; burn to reverse course and fly back toward the launch tower, whose metal &quot;chopstick&quot; arms catch it in mid-air instead of letting it land on legs. Flight 15 was aiming to combine that with a return of the Ship upper stage for what SpaceX billed as the first complete recovery of an orbital launch system, a step beyond the booster catches demonstrated on earlier flights. Rocket guidance systems are designed to abort such a catch automatically and divert the booster offshore when the vehicle is not where it needs to be, which is what happened here.

**Impact:** Because the booster was destroyed offshore rather than recovered, SpaceX cannot inspect Booster 22&\#x27;s hardware and will have to pin down the low fuel mass alarm from flight data before the next catch attempt. The episode also shows how the catch is gated: the abort was automatic, triggered when the vehicle&\#x27;s position drifted outside the limits required to return to the tower.

**Tags**: `#Starship Flight 15`, `#Super Heavy booster`, `#chopsticks catch`, `#SpaceX anomaly investigation`, `#spaceflight test`

---

<a id="item-space-4"></a>
### [SpaceX launches 22-hour Starship Flight 15, aborts booster catch](https://www.space.com/space-exploration/launches-spacecraft/spacex-starship-flight-15-chopsticks-double-catch-super-heavy-ship) ⭐️ 7.0/10

SpaceX launched Starship Flight 15 from Starbase, Texas, on Nov. 13 at 5:47 p.m. ET, beginning a planned 22-hour test that reached low Earth orbit and deployed 26 Starlink V3 satellites. The Super Heavy booster hot-staged successfully, but SpaceX called off the launch tower&\#x27;s &quot;chopsticks&quot; catch and brought it down for a controlled splashdown in the Gulf of Mexico about 6.5 minutes after launch, for reasons not immediately disclosed. The Ship was left in a roughly 275-kilometer orbit and is being prepared for what would be its first return to the launch site, contingent on engineers confirming that reentry, landing-burn, and tower-approach systems are healthy.

Space.com · Nov 13, 23:20

**Context:** SpaceX recovers Super Heavy boosters by flying them back to the launch tower and catching them with the tower&\#x27;s mechanical arms, an approach aimed at rapid reuse rather than splashdowns or landing legs. The rocket has already gone through several design generations: SpaceX caught three Version 1 Super Heavy boosters and re-flew two of them, while no Version 3 booster had been recovered before Flight 15. Flight 14, launched Sept. 28, was the first Starship flight to reach orbit, making Flight 15&\#x27;s insertion only the second.

**Impact:** The aborted catch means SpaceX has still not recovered a Version 3 Super Heavy booster, leaving that reusability milestone for a later flight. The Ship&\#x27;s own return remains pending a health assessment that SpaceX says will include imagery from three camera-equipped Starlink V3 satellites to inspect its heat shield and other hardware.

**Tags**: `#Starship`, `#SpaceX`, `#Super Heavy`, `#test flight`, `#booster recovery`

---

## Tech Industry &amp; Policy

<a id="item-tech-industry-1"></a>
### [Italy&\#x27;s privacy regulator fines Meta €805M over alleged Android photo and video access](https://www.techmeme.com/261114/p11#a261114p11) ⭐️ 8.0/10

Italy&\#x27;s data protection agency said on Saturday it had fined Meta Platforms €805 million \(about $887 million\) after finding the company accessed Android users&\#x27; photos and videos without obtaining their consent or informing them. The decision, reported by Reuters, is a national enforcement action and the report gives no detail on the technical mechanism, the number of users affected, or whether Meta intends to appeal. The agency&\#x27;s stated objection is framed around consent and notification rather than around any specific Android permission bypass, so the scope of the finding remains unclear from the available account.

Techmeme · Nov 14, 15:10

**Background:** Italy&\#x27;s data protection agency announced the penalty on Nov. 14 after finding that Meta had accessed Italian Android users&\#x27; photos and videos without specific consent, Reuters reported. The agency is also demanding changes to Facebook&\#x27;s gallery feature, according to reports of the decision, tying the case to a particular Android feature rather than a broad new privacy rule.

**Impact:** The exposure is currently confined to one country&\#x27;s regulator: the Reuters excerpt does not say whether the finding applies to all Android users in Italy or a narrower group, nor whether Meta will contest it, and those two unknowns determine whether the €805 million figure holds or becomes a template for other EU authorities. For developers, the case turns on disclosure practice — the agency&\#x27;s objection as reported is that users were not told about the access or asked for consent — rather than on whether Android&\#x27;s own permission prompts appeared.

**Community Discussion:** Hacker News commenters focused on the gaps in the reporting: one asked how photos could be accessed without a consent prompt and said the article lacked detail, while another argued that users must grant permission on their device and can revoke it in settings, and questioned what exactly Italy was protecting. Others doubted that large tech fines are ever actually paid, and one pointed readers to enforcementtracker.com as a running tally of EU enforcement decisions.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reuters.com/world/italy-fines-meta-887-million-over-android-users-data-access-2026-11-14/">Italy fines Meta $887 million over Android users&#x27; data access</a></li>
<li><a href="https://www.yahoo.com/news/world/articles/italy-fines-meta-nearly-1-140421554.html?fr=sycsrp_catchall">Italy Fines Meta Nearly $1 Billion Over Company Accessing ...</a></li>
<li><a href="https://www.straitstimes.com/world/europe/italy-fines-meta-1-14-billion-over-android-users-data-access">Italy fines Meta €805 million over Android data access | The ...</a></li>

</ul>
</details>

**Tags**: `#Meta`, `#privacy regulation`, `#Italy`, `#Android`, `#data protection`

---

<a id="item-tech-industry-2"></a>
### [Altimeter and Atreides investors urge Nvidia board to weigh Huang&\#x27;s &quot;potential return&quot;](https://www.techmeme.com/261114/p18#a261114p18) ⭐️ 7.0/10

Brad Gerstner of Altimeter and Gavin Baker of Atreides, two investors holding a combined $2.13 billion in Nvidia stock, reportedly sent a letter asking Nvidia&\#x27;s board of directors to weigh all options for the company&\#x27;s future leadership, including what they describe as &quot;the potential return of Jensen Huang.&quot; CNBC&\#x27;s Katie Tarasov reported the letter; the account, relayed by Techmeme, does not quote the letter in full or describe the reasoning behind the succession proposal. The report describes a shareholder request, not a board decision — no board response, formal proposal, or timeline has been disclosed, and no primary filing or copy of the letter was cited.

Techmeme · Nov 14, 19:55

**Background:** Altimeter Capital is a technology-focused investment firm, and its CEO Brad Gerstner signed the letter along with Atreides Management&\#x27;s Gavin Baker; the two report owning $2.13 billion in Nvidia stock. According to CNBC, Gerstner posted the letter on X rather than filing it, asking Nvidia&\#x27;s board to pursue a &quot;slow, measured, and deliberate process&quot; regarding the company&\#x27;s future leadership. Because the board rather than shareholders directly controls CEO succession, the letter is a request for a process, and its phrase &quot;potential return&quot; implies a leadership change has occurred or is contemplated, though the supplied report does not describe the circumstances.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Altimeter_Capital">Altimeter Capital - Wikipedia</a></li>
<li><a href="https://www.cnbc.com/2026/11/14/nvidia-investors-jensen-huang-return-board-letter.html">Nvidia board urged to consider &#x27;potential return of Jensen Huang &#x27;</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#corporate governance`, `#shareholder activism`, `#semiconductors`, `#leadership succession`

---

<a id="item-tech-industry-3"></a>
### [Sean Duffy Blames FAA Groundstop on Wiring Work and Possible Faulty Router](https://www.techmeme.com/261114/p14#a261114p14) ⭐️ 7.0/10

The FAA lifted its third-ever nationwide ground stop Friday evening, clearing domestic flights to take off at 8:35 pm EST after several hours of system instability. Transportation Secretary Sean Duffy attributed the outage to copper-to-fiber wiring work at a single remote facility and said contractor L3Harris may have installed a &quot;faulty router,&quot; a cause he framed as likely rather than confirmed. More than a million travelers were affected, airlines canceled flights into the evening—Air Canada scrapped all U.S.-bound flights for the rest of Friday—and Duffy warned that without major system updates there will be &quot;more of these&quot; outages because air traffic control still runs on decades-old analog equipment.

Techmeme · Nov 14, 17:15

**Background:** A nationwide FAA ground stop is rare: Friday&\#x27;s was only the third in the agency&\#x27;s history, with domestic flights cleared to resume takeoff at 8:35 pm EST. The disruption centered on wiring work at a single remote facility, while Transportation Secretary Sean Duffy said the air traffic control system still relies on decades-old analog equipment.

**Funding and travel fallout:** The outage lands directly on the FAA&\#x27;s modernization budget: Congress has already given the agency $12.5 billion to upgrade its aging air traffic control and telecom systems, and Duffy has asked for another $50 billion for air traffic control and airports, so the router incident becomes concrete evidence in that funding fight. For travelers, the practical effect outlasts the groundstop itself — more than a million people were affected, and carriers including Air Canada cancelled all U.S.-bound and U.S.-departing flights for the rest of Friday evening while they reset schedules.

<details><summary>References</summary>
<ul>
<li><a href="https://www.usatoday.com/story/business/2026/11/14/faa-ground-stop-blame-installed-router/92782974007/">FAA ground stop blamed on router installed by contractor</a></li>
<li><a href="https://www.reuters.com/business/aerospace-defense/us-aviation-shutdown-blamed-l3-harris-installed-router-2026-11-14/">US aviation shutdown blamed on L3 Harris installed router</a></li>

</ul>
</details>

**Tags**: `#FAA outage`, `#critical infrastructure`, `#network reliability`, `#L3Harris`, `#aviation`

---

<a id="item-tech-industry-4"></a>
### [Microsoft says Microsoft 365 fully restored after global outage](https://www.techmeme.com/261114/p8#a261114p8) ⭐️ 7.0/10

Microsoft said access to all Microsoft 365 products has been fully restored, ending a global outage that disrupted government offices, traders, hospitals, and businesses. Bloomberg described it as one of Microsoft&\#x27;s longest outages, but the supplied report does not give the cause, exact duration, or number of affected customers. The restoration is Microsoft&\#x27;s own account; independent verification and a technical postmortem were not included.

Techmeme · Nov 14, 08:03

**How the outage unfolded:** The disruption began on 12 November 2026, when users in more than 70 countries reported problems with Microsoft 365 as well as Outlook, Teams and Copilot, making the restoration a multi-day incident rather than a brief spike. Microsoft confirmed completion on its Microsoft 365 status page, saying it had &quot;restored service to the remaining impacted customers and regions&quot; and pointing customers to incident MO1550821 in the Microsoft 365 admin center for further updates.

**Continuity gap:** Organizations that depend on Exchange Online for Outlook mail, Teams calendars, and Copilot faced a disruption Microsoft&\#x27;s final record put at roughly 30 hours, from 5:05 AM ET on November 12 to 11:10 AM ET on November 13, across multiple regions. That makes a fallback for mail and calendar, not just individual apps, the practical continuity requirement when a single cloud dependency fails.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2026_Microsoft_outage">2026 Microsoft outage - Wikipedia</a></li>
<li><a href="https://www.theguardian.com/technology/2026/nov/14/microsoft-says-services-fully-restored-after-global-outage">Microsoft says services fully restored after global outage hits...</a></li>
<li><a href="https://www.on-sitetechnology.com/microsoft-365-outage-november-2026/">Microsoft 365 and Outlook Outage, Nov 12, 2026: Timeline</a></li>

</ul>
</details>

**Tags**: `#microsoft`, `#microsoft 365`, `#cloud outage`, `#service reliability`, `#critical infrastructure`

---