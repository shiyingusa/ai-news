---
layout: issue
permalink: /briefing/2026-11-24/
title: "AI News Briefing: November 24, 2026"
date: 2026-11-24
lang: en
---

> We screened 296 stories from the past day and kept the 12 worth your time.

---

**AI**
1. [NariQ ships 3-bit Qwen3.8-27B quantizations claiming near-BF16 quality](#item-ai-news-1) ⭐️ 7.0/10
2. [Google AI Mode draws on Drive and Wallet for personalized answers](#item-ai-news-2) ⭐️ 7.0/10
3. [Meta rolls out Muse agent to UK adults, a Big Tech first, Politico reports](#item-ai-news-3) ⭐️ 7.0/10
4. [AWS launches five open Strands Decider v2 models, The New Stack reports](#item-ai-news-4) ⭐️ 7.0/10

**Chips &amp; Computing**
1. [US adds Alibaba&\#x27;s Singapore unit Apex to Entity List with Megaspeed, Bloomberg reports](#item-chips-compute-1) ⭐️ 7.0/10

**EVs &amp; Energy**
1. [VW ID. Polo Wait Times Near Two Years Despite 1,000 Cars a Day](#item-ev-energy-1) ⭐️ 7.0/10
2. [Battery-electric cars near 30% of EU new-car market in October, ACEA data shows](#item-ev-energy-2) ⭐️ 7.0/10
3. [Residential solar tied to lower heat deaths in Japan, study finds](#item-ev-energy-3) ⭐️ 7.0/10

**Tech Industry &amp; Policy**
1. [SpaceX and Tesla in talks for $3.5T all-stock merger, FT reports](#item-tech-industry-1) ⭐️ 8.0/10
2. [Google reportedly retracted West Bank Maps changes after Israeli pressure, Wired reports](#item-tech-industry-2) ⭐️ 7.0/10
3. [Two unsecured databases reportedly exposed 3.5 billion credentials](#item-tech-industry-3) ⭐️ 7.0/10
4. [Ladybird&\#x27;s from-scratch browser engine opens alpha testing on macOS and Linux](#item-tech-industry-4) ⭐️ 7.0/10

---

## AI

<a id="item-ai-news-1"></a>
### [NariQ ships 3-bit Qwen3.8-27B quantizations claiming near-BF16 quality](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF) ⭐️ 7.0/10

NariQ has published 3-bit, 2.5-bit and 2-bit GGUF quantizations of Qwen3.8-27B, with the 3-bit file roughly 10 GB and the authors claiming near-BF16 quality across agentic, math, multilingual and image tasks. In the release&\#x27;s own benchmark table, 3-bit and 2.5-bit match or slightly beat BF16 on DeepSWE \(41.0 and 41.9 vs 39.8\) and Terminal-Bench 2.1 \(63.8 and 60.2 vs 62.6\), while the 2-bit version falls to 28.6 on DeepSWE and 86.0 on AIME 25+26 versus 97.7 for BF16. The authors say this is the first 3-bit-or-lower quantization to retain BF16-level performance on long-horizon agentic tasks, but running it currently requires NariQ&\#x27;s own llama.cpp fork. Decode speed is described as comparable to other quantizations on an RTX PRO 6000; the results are author-reported and have not been independently verified.

Hacker News · toebee · Nov 23, 13:42 · [Discussion](https://news.ycombinator.com/item?id=50611402)

**Verified and unconfirmed:** Verified: NariQ&\#x27;s model card publishes BF16, 3-bit, 2.5-bit and 2-bit scores for DeepSWE, Terminal-Bench 2.1, AIME 25+26, MSGM and RealWorldQA, and a commit in the same repository describes the DeepSWE figures as three-round averages with per-cell task counts and Docker-based runs \(tool-3-1\). The card also states that running these files currently requires NariQ&\#x27;s own llama.cpp fork.
Not yet confirmed: All scores are author-reported with no independent replication, and the release does not say what the 4K–64K context-length numbers \(88.9 up to 111.7\) actually measure, so the claim that decode speed is comparable to other quants rests on the vendor&\#x27;s word; several 3-bit and 2.5-bit results also come out above the BF16 baseline without explanation, and the Terminal-Bench version cited, 2.1, is not the 4.1 release listed on the benchmark&\#x27;s own site \(tool-3-3\).

**Background:** Quantization stores a model&\#x27;s weights at fewer bits each — here 3, 2.5 and 2 bits per weight instead of 16-bit BF16 — so a 27B-parameter model fits in a roughly 10 GB GGUF file instead of tens of gigabytes, at the risk of losing accuracy. NariQ&\#x27;s files are built for a custom fork of llama.cpp, the open-source inference runtime that loads GGUF models, so standard llama.cpp builds may not run them. The model card dates the v1 release to Nov 20, 2026 and says the 3-bit and 2.5-bit files match BF16 on long-horizon agent tasks, math and image understanding, while the 2-bit file scores lower.

**Why it matters:** For people running models locally, the practical change is that a 27B agentic model can fit in about 10 GB of storage, roughly a fifth of the ~54 GB needed at BF16, bringing it within reach of 16 GB machines and single consumer GPUs, though context length and runtime overhead reduce that headroom. The catch is compatibility: users must build and run nari-llama.cpp rather than mainline llama.cpp, and the release&\#x27;s own numbers show the 2-bit variant losing substantial long-horizon agentic and math accuracy, so the 3-bit file is the one to test first.

**What to watch:** The next checkable step is independent benchmarking on consumer hardware and whether the required nari-llama.cpp changes land in upstream llama.cpp; until then, the fork requirement is the main barrier to ordinary use.

**Community discussion:** Commenters disagree on whether the near-BF16 results reflect the quantization or the evaluation harness: rao-v said the release does the basic checks they want, including multiple long-horizon task types and held-out evaluations, while WithinReason argued from the plots that most gains come from a harness difference rather than the model. A user also reported about 3.8 tok/s decode on an 18 GB M3 Pro with the 3.0-bit file, and others asked what information is lost and how it compares with Bonsai 2 27B.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF">nari-labs/Qwen3.8-27B-NariQ-GGUF · Hugging Face</a></li>
<li><a href="https://aitecharchive.com/articles/nariq-quantization-qwen3-8-27b-agent-performance-10gb">NariQ Quantization: Qwen3.8-27B Agents in a 10 GB File</a></li>
<li><a href="https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF/commit/9065513f08d8ed7dbe50b9c329cac1f40c70fde9">Report three-round DeepSWE averages...</a></li>
<li><a href="https://www.tbench.ai/">TERMINAL - BENCH</a></li>

</ul>
</details>

**Tags**: `#quantization`, `#Qwen3.8-27B`, `#local LLMs`, `#llama.cpp`, `#model compression`

---

<a id="item-ai-news-2"></a>
### [Google AI Mode draws on Drive and Wallet for personalized answers](https://techcrunch.com/2026/11/23/google-searchs-ai-mode-can-now-tap-into-drive-and-wallet-for-more-personalized-responses/) ⭐️ 7.0/10

Google is extending &quot;Personal Intelligence&quot; in Search&\#x27;s AI Mode — the personalization layer that lets the assistant draw on a user&\#x27;s own context — to Google Drive, Google Wallet and the Gemini app, TechCrunch reported. The point, per the report, is to exploit the data users already keep inside Google&\#x27;s ecosystem, so AI Mode answers can reflect documents and payment or pass information rather than only public web content. The report does not say how the data is accessed, which countries or account types get the capability first, or what privacy controls let users disconnect a source. It therefore establishes the direction of the rollout but not the scope of availability.

TechCrunch AI · Nov 23, 19:14

**Verified and unconfirmed:** Verified: Google announced on Monday that Personal Intelligence in Search&\#x27;s AI Mode now extends to Google Drive, Google Wallet and the Gemini app, per TechCrunch and Google&\#x27;s own blog post, which says users must opt in to connect those services.

Not yet confirmed: The rollout sequence and reach — Android Authority reports Wallet support arrives first, following Gemini connectivity earlier this month, with Drive and the Gemini app connections trailing — but Google&\#x27;s post and the coverage do not specify a full availability date, countries, or which account tiers qualify; they also leave out what data each integration can read, how long it is retained, and whether any independent privacy or security review has been done.

**Background:** Personal Intelligence is Google&\#x27;s opt-in layer that lets AI Mode, the conversational search mode, answer using a signed-in user&\#x27;s own Google data rather than only the public web. According to Google&\#x27;s announcement and Digital Trends, the Wallet connection is read-only and arrives first, with Drive and the Gemini app following in the weeks ahead, and each connected app can be switched off at any time.

**Why it matters:** For people who store documents in Drive and cards, passes or tickets in Wallet, the useful question shifts from &quot;what can the assistant find&quot; to &quot;what of mine is it allowed to read&quot; — so the account-level permissions attached to those Google products become the practical control surface, and users should check which sources they are willing to connect before relying on personalized answers.

**What to watch:** Watch Google&\#x27;s own support documentation for the account types and countries where Personal Intelligence in AI Mode covers Drive, Wallet and the Gemini app, and for whether users can selectively disconnect each source.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/products-and-platforms/products/search/google-search-personal-intelligence-apps/">Tailored Google Search with Personal Intelligence apps</a></li>
<li><a href="https://www.digitaltrends.com/computing/google-is-connecting-wallet-to-ai-mode-in-search-and-drive-and-the-gemini-app-come-next/">Google is connecting Wallet to AI Mode in Search, and Drive ...</a></li>
<li><a href="https://blog.google/products-and-platforms/products/search/google-search-personal-intelligence-apps/">Tailored Google Search with Personal Intelligence apps</a></li>
<li><a href="https://techcrunch.com/2026/11/23/google-searchs-ai-mode-can-now-tap-into-drive-and-wallet-for-more-personalized-responses/">Google Search&#x27;s AI Mode can now tap into Drive and Wallet for ...</a></li>
<li><a href="https://www.androidauthority.com/personal-intelligence-ai-mode-3738563/">Google expands Personal Intelligence in AI Mode for Search</a></li>

</ul>
</details>

**Tags**: `#Google AI Mode`, `#personalization`, `#Google Drive`, `#Google Wallet`, `#privacy`

---

<a id="item-ai-news-3"></a>
### [Meta rolls out Muse agent to UK adults, a Big Tech first, Politico reports](https://www.techmeme.com/261124/p4#a261124p4) ⭐️ 7.0/10

Meta has rolled out its personal AI agent Muse to adults in the UK, with Politico describing it as the first AI agent from a Big Tech company to launch in the country. The agent is pitched at helping with everyday tasks, but the report does not say which tasks it handles, what it costs, or which platforms it runs on. UK watchdogs have warned about AI agents, and Politico reports that regulators will be watching the Muse rollout closely.

Techmeme · Nov 24, 07:50

**Verified and unconfirmed:** Verified: Meta rolled out its personal AI agent Muse to UK adults, as reported by Politico, which characterizes it as the first Big Tech AI agent launch in the UK. Not yet confirmed: which everyday tasks Muse performs, its price and platform availability, the specific content of UK watchdogs&\#x27; warnings about agents, and whether Meta has launched Muse in other markets; the &quot;first Big Tech&quot; description rests on Politico&\#x27;s reporting rather than an independent count.

**Background:** Muse is Meta&\#x27;s personal AI agent: users chat with it in the Meta AI app or directly in WhatsApp, and it carries out tasks on their behalf — chasing a refund, renewing car insurance, turning saved travel Reels into an itinerary — rather than only answering questions. AI Daily Radar&\#x27;s 23 November digest reported that Walmart had made Muse the first shopping agent on its new Agent Gateway, able to search for and buy Black Friday deals through Walmart&\#x27;s Sparky assistant, with spending limits and purchase approvals set in a dedicated &quot;Agent Profiles&quot; space inside the customer&\#x27;s account.

**Why it matters:** UK adults can now delegate everyday tasks to an agent built by Meta, at a point when UK watchdogs have already flagged concerns about agents generally. The terms Meta sets for what Muse can access and do will be the first worked example of how those warnings are applied to a Big Tech agent, and will shape the ground rules competitors face when they bring similar products to the UK.

**What to watch:** Watch for the first public statement or action from UK regulators specifically about Muse, and for whether Meta names additional countries for the agent&\#x27;s rollout.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theverge.com/ai-artificial-intelligence/1039874/walmart-agent-gateway-meta-muse-black-friday">2026-11-23 — Walmart lets Meta&#x27;s Muse agent buy Black Friday deals via Agent Gateway</a></li>
<li><a href="https://about.fb.com/news/2026/11/introducing-muse-in-the-uk-a-personal-ai-agent-you-control/">Introducing Muse in the UK: A Personal AI Agent You Control</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#Meta`, `#UK regulation`, `#consumer AI`, `#Big Tech`

---

<a id="item-ai-news-4"></a>
### [AWS launches five open Strands Decider v2 models, The New Stack reports](https://www.techmeme.com/261123/p55#a261123p55) ⭐️ 7.0/10

AWS on Monday launched Strands Decider v2, a family of five open “decision models” that The New Stack reports are built on Google’s Gemma 4 and released under the Apache 2.0 license. The models span 2 billion to 31 billion parameters, giving AI builders a single permissively licensed family across small and large sizes. The report does not include benchmark results or explain what the models do beyond the decision-model label, so the capability claims remain unverified.

Techmeme · Nov 24, 04:25

**Verified and unconfirmed:** Verified: Strands Labs&\#x27; own announcement says Strands Decider v2 is a family of five decision models built on Gemma 4, spanning 2B to 31B parameters under Apache 2.0, with weights published on Hugging Face and v2 support in the open-source Strands Decider repository; the models do not generate text but pick from a supplied list of options, returning a probability for each in a single forward pass, and VentureBeat independently describes the release the same way. The New Stack dates the launch to &quot;Monday,&quot; consistent with third-party coverage placing it on Nov 23, 2026.

Not yet confirmed: the accuracy and calibration of the returned probabilities at each model size rest so far on the vendor&\#x27;s description, with no independent benchmark supplied; throughput, latency and how the five sizes compare in real agent-routing workloads are also unverified, and the item offers no detail on what changed from the earlier Strands Labs release seven weeks prior.

**Background:** Strands Decider is a family of &quot;system one&quot; models — the term for fast, intuitive decisions rather than the slower step-by-step deliberation of reasoning models — which AWS&\#x27;s Strands Labs positions for tasks like agent routing, where a model picks which tool or path an agent should take. The official release notes say v2 ships five such models built on Google&\#x27;s Gemma 4, spanning E2B to 31B parameters, with weights published on Hugging Face and v2 support added to the open-source Strands Decider repository. The New Stack notes the launch came only about seven weeks after the previous Strands Labs release.

**Why it matters:** For AI builders, the practical change is a permissively licensed family that covers both small and large models, so teams can test a lightweight variant for constrained deployments and a 31B variant for heavier workloads without separate license terms. The report provides no independent performance data, so teams should validate quality before standardizing on it.

**What to watch:** Watch for independent benchmark results across the five sizes, especially the 31B variant, which would test whether the larger models deliver enough gain to justify their size.

<details><summary>References</summary>
<ul>
<li><a href="https://strandsagents.com/blog/introducing-strands-decider-v2/">Introducing Strands Decider v2: open, calibrated system one ...</a></li>
<li><a href="https://explainx.ai/blog/aws-strands-decider-v2-gemma4-november-2026">Strands Decider v2: 5 Open Models (Apache 2.0) | explainx.ai Blog</a></li>
<li><a href="https://strandsagents.com/blog/introducing-strands-decider-v2/">Introducing Strands Decider v2: open, calibrated system one ...</a></li>
<li><a href="https://venturebeat.com/data/awss-strands-decider-v2-targets-the-agent-decisions-that-hinge-on-a-single-detail">AWS&#x27;s Strands Decider v2 targets the agent decisions that ...</a></li>
<li><a href="https://explainx.ai/blog/aws-strands-decider-v2-gemma4-november-2026">Strands Decider v2: 5 Open Models (Apache 2.0) | explainx.ai Blog</a></li>

</ul>
</details>

**Tags**: `#AWS`, `#open models`, `#Gemma 4`, `#Apache 2.0`, `#model release`

---

## Chips &amp; Computing

<a id="item-chips-compute-1"></a>
### [US adds Alibaba&\#x27;s Singapore unit Apex to Entity List with Megaspeed, Bloomberg reports](https://www.techmeme.com/261124/p10#a261124p10) ⭐️ 7.0/10

The US Commerce Department added Apex Enterprise Solutions, a Singapore-based subsidiary of Alibaba Group, to its Entity List, alongside Singapore-linked distributor Megaspeed and five affiliates, Bloomberg reported, citing a filing. The listing puts the entities on a roster that requires US suppliers to obtain a license before exporting controlled goods to them, including advanced AI chips — a constraint on Alibaba&\#x27;s AI compute plans routed through Singapore. The report did not give an effective date, the full list of items covered, or any comment from Commerce or Alibaba. The action came the same day Singapore Prime Minister Lawrence Wong said Singapore should not be used as a route to circumvent US chip export controls, as authorities probe Megaspeed&\#x27;s purchases of Nvidia chips.

Techmeme · Nov 24, 11:10

**Verified and unconfirmed:** Verified: Bloomberg reports that a US Commerce Department filing adds Alibaba&\#x27;s Singaporean subsidiary Apex Enterprise Solutions, Megaspeed and five affiliates to the Entity List.
Not yet confirmed: The specific conduct or rationale behind Apex&\#x27;s listing, the identities of all five affiliates, and the listing&\#x27;s effective date; Alibaba says Apex never diverted chips covered by US export restrictions and will take legal steps to protect its rights.

**Background:** The Entity List is the US Commerce Department’s roster of foreign parties that need a license before receiving items subject to US export controls, including many advanced chips. The addition of Apex Enterprise Solutions \(Singapore\) Private Limited requires a US license for exports, reexports and transfers to the company of items covered by US rules, and Alibaba said on Nov. 24 that the designation was erroneous.

**Why it matters:** For Alibaba, a Singapore-based procurement channel is now covered by US export licensing, so any American supplier shipping controlled chips or equipment to Apex needs a license first; distributors and cloud partners dealing with Apex, Megaspeed or the five affiliates should verify the listing before fulfilling orders, since Entity List obligations attach to the US exporter rather than the buyer.

**What to watch:** Watch for Commerce&\#x27;s formal Federal Register notice naming the entities and stating the license requirements and effective date, and for the outcome of Singapore&\#x27;s probe into Megaspeed&\#x27;s Nvidia chip purchases.

<details><summary>References</summary>
<ul>
<li><a href="https://aistockwire.com/blog/alibaba-baba-apex-enterprise-solutions-singapore-entity-list-megaspeed-november-2026">Alibaba&#x27;s Singapore unit Apex added to the US entity list</a></li>
<li><a href="https://www.straitstimes.com/business/alibaba-disputes-us-blacklisting-of-singapore-subsidiary-over-chip-rerouting-risks">Alibaba disputes US blacklisting of Singapore subsidiary over ...</a></li>
<li><a href="https://www.straitstimes.com/world/united-states/us-blacklists-megaspeed-chip-firm-linked-to-nvidia-scandal">US blacklists Megaspeed , Alibaba unit amid Nvidia... | The Straits Times</a></li>
<li><a href="https://uz.kursiv.media/en/2026-11-24/us-blacklist-megaspeed-alice-huang/">US blacklists Megaspeed , once led by China spy suspect Alice Huang</a></li>

</ul>
</details>

**Tags**: `#export controls`, `#Entity List`, `#Alibaba`, `#AI compute`, `#US-China tech`

---

## EVs &amp; Energy

<a id="item-ev-energy-1"></a>
### [VW ID. Polo Wait Times Near Two Years Despite 1,000 Cars a Day](https://insideevs.com/news/816560/vw-id-polo-cupra-raval-skoda-epiq-demand-high-wait-times/) ⭐️ 7.0/10

Volkswagen Group underestimated demand for its new family of small electric cars, and buyers are now waiting well over a year for delivery. The ID. Polo, Cupra Raval and Škoda Epiq are assembled at the group&\#x27;s Martorell plant in Spain, which is already building about 1,000 cars per day. InsideEVs&\#x27; headline cites waits of nearly two years, while the electrive report behind it says ID. Polo customers sometimes wait more than a year and that the other three models in the family also require patience; the two accounts are not reconciled and no order-book figures are published. Volkswagen now plans to scale up Spanish production faster, but a shortage of battery cells is also slowing output.

InsideEVs · Nov 24, 08:43

**Verified and unconfirmed:** Verified: InsideEVs reports that the Martorell plant in Spain, which builds the Volkswagen ID. Polo and Cupra Raval, is already producing 1,000 cars per day, and that production there is now to be ramped up faster.

Not yet confirmed: The wait-time figures rest on the outlet&\#x27;s reporting rather than a cited Volkswagen statement, and the numbers do not fully agree — the headline says buyers face waits of nearly two years, while the article text says ID. Polo customers sometimes wait more than a year and that the other three models in the family also require patience. The attribution of the delays to a battery-cell shortage, the claim that Volkswagen underestimated demand, and any per-model wait times or delivery dates are not confirmed by the company in the report.

**Background:** The ID. Polo and Cupra Raval belong to Volkswagen Group’s new family of affordable small electric cars, which the group is assembling at a Spanish plant. The plant has already reached 1,000 cars per day, but a shortage of battery cells is constraining how quickly output can be increased.

**Why it matters:** For buyers, the practical consequence is that ordering one of these models now may mean waiting more than a year for delivery, and the bottleneck is not only the Martorell assembly line&\#x27;s throughput but also battery cell supply. Volkswagen Group&\#x27;s battery unit PowerCo has identified three cell production sites — Salzgitter \(Germany\), Valencia \(Spain\) and St. Thomas \(Canada\) — so the pace at which Spanish cell capacity comes online is the lever that determines whether those wait times shorten.

**What to watch:** Watch for Volkswagen to publish revised delivery estimates or announce additional battery-cell capacity for Martorell. The quoted wait times only shorten if cell supply improves, not just assembly-line speed.

<details><summary>References</summary>
<ul>
<li><a href="https://www.volkswagen-group.com/en/volkswagen-group-sites-17481">Volkswagen Group sites | Volkswagen Group</a></li>

</ul>
</details>

**Tags**: `#Volkswagen ID. Polo`, `#Cupra Raval`, `#EV demand`, `#production capacity`, `#wait times`

---

<a id="item-ev-energy-2"></a>
### [Battery-electric cars near 30% of EU new-car market in October, ACEA data shows](https://www.electrive.com/2026/11/24/acea-battery-electric-cars-capture-30-per-cent-of-eu-passenger-car-market/) ⭐️ 7.0/10

Battery-electric cars accounted for nearly 30% of EU passenger car registrations in October, with 280,000 units registered — 61% more than in the same month a year earlier, according to figures from ACEA, the European automobile manufacturers&\#x27; association. The October total is above the 250,000-plus monthly pace the report says pure electric cars have recently been sustaining across the bloc. The report does not give a country-by-country or model breakdown, and does not state the absolute October 2025 comparison figure behind the 61% growth rate.

Electrive · Nov 24, 10:30

**Verified and unconfirmed:** Verified: electrive reported, citing ACEA \(the European Automobile Manufacturers&\#x27; Association, which the search result confirms represents 17 major European car, truck, van and bus makers\), that 280,000 battery-electric cars were registered in the EU in October, 61 per cent more than a year earlier, and that BEVs took nearly 30 per cent of the overall passenger car market.

Not yet confirmed: no ACEA release or dataset was available to check the figures independently, and the report gives no country or brand breakdown, no total market volume, and no clarity on whether the scope is the EU alone or the wider EU+EFTA+UK grouping ACEA often uses; the headline rounds the share to 30 per cent while the article text says &quot;nearly 30 per cent.&quot;

**Background:** ACEA, the European Automobile Manufacturers&\#x27; Association, publishes monthly registration figures for new passenger cars across the EU, and those counts are widely used as a proxy for sales because a car is registered when it is delivered. Battery-electric cars spent years as a single-digit sliver of that market before moving into the mainstream, so the monthly share has become the standard gauge of how quickly the EU fleet is turning over to electric drive. The October figure is a single month&\#x27;s snapshot rather than a year-to-date total, and the report does not give the overall size of the EU market that the roughly 30 per cent share is measured against.

**Why it matters:** At roughly 280,000 registrations in a single month, the EU is adding BEVs at an annualised pace above 3.3 million, which is the volume figure charging-network operators and grid planners use to size new installations — so October&\#x27;s number matters less as a record than as evidence that monthly demand is running above the 250,000-plus level the market has recently held.

**What to watch:** The next ACEA monthly registration release, covering November, to see whether the near-30% share holds or whether October was lifted by a one-off surge before year-end fleet compliance buying.

<details><summary>References</summary>
<ul>
<li><a href="https://www.acea.auto/">ACEA - European Automobile Manufacturers&#x27; Association</a></li>

</ul>
</details>

**Tags**: `#EV adoption`, `#EU passenger car market`, `#ACEA data`, `#battery-electric vehicles`, `#market share`

---

<a id="item-ev-energy-3"></a>
### [Residential solar tied to lower heat deaths in Japan, study finds](https://www.pv-magazine.com/2026/11/24/residential-solar-linked-to-reduced-health-risks-from-extreme-temperatures/) ⭐️ 7.0/10

Peer-reviewed research in Social Science &amp; Medicine by Yi-Chun Ko and Shinsuke Uchida estimates that residential solar adoption in Japan reduced excess deaths on extremely hot days by about 8.2% a year for the general population and 8.5% for people aged 65 and older. The study uses the 2011 Great East Japan Earthquake as a natural experiment: nuclear shutdowns pushed electricity prices up by as much as 38% while a national subsidy expanded household solar, and the authors combine 2009-2014 monthly mortality data from 44 prefectures with weather and installation records. The estimated benefit is strongest in warmer prefectures, places with larger price increases and areas with stricter conservation targets, and the paper finds no comparable effect during cold temperatures. The authors call it the first causal evidence that household solar can serve as a public-health intervention, while cautioning that adoption skews toward higher-income households and the benefits may be uneven without targeted policy.

pv magazine · Nov 24, 09:18

**Verified and unconfirmed:** Verified: The study is a peer-reviewed article in Social Science &amp; Medicine \(vol. 410, 2026\) by Yi-Chun Ko of the Asian Growth Research Institute and Shinsuke Uchida of Doshisha University, and journal indexes confirm its stated scope — whether residential solar PV can mitigate health risks by reducing households&\#x27; reliance on grid electricity during extreme heat \(tool-2-1, tool-2-3\); its publication listing dates to October 2026 \(tool-2-2\).

Not yet confirmed: The headline figures — an ~8.2% annual reduction in heat-related excess deaths overall and ~8.5% for people 65 and older — are the authors&\#x27; own model-based estimates from their instrumental-variable design, not independently replicated measurements, and the &quot;first causal evidence&quot; description is the co-author&\#x27;s characterization of his own work; the 38% electricity price increase and the prefecture-level mortality and installation data are stated in the paper without independent verification here, and the authors themselves note that solar adoption skews toward higher-income households, so the size and distribution of any real-world benefit remain uncertain.

**Background:** Japan&\#x27;s 2011 Great East Japan Earthquake forced nuclear plants offline, pushing electricity prices up by as much as 38% while a national subsidy was expanding rooftop solar. That combination gave researchers a natural experiment: prefectures faced the same broad price shock but differed in how much residential solar was installed. They combined monthly mortality, weather and official installation data for 44 prefectures from 2009 to 2014, using an instrumental-variable method—a statistical technique for separating solar adoption from other local factors—to estimate its effect on heat-related deaths.

**Why it matters:** For policymakers and health officials, the finding adds a public-health rationale to residential-solar support, but it also flags an equity constraint: because adoption is concentrated among higher-income households, the heat-mortality benefit may bypass renters and low-income older people unless programs are targeted at them.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0277953626010105">Climate resilience through residential solar energy: Reducing ...</a></li>
<li><a href="https://ifp.nyu.edu/2026/journal-article-abstracts/s0277953626010105/">Climate resilience through residential solar energy: Reducing ...</a></li>
<li><a href="https://ideas.repec.org/a/eee/socmed/v410y2026ics0277953626010105.html">Climate resilience through residential solar energy: Reducing ...</a></li>

</ul>
</details>

**Tags**: `#residential solar`, `#public health`, `#extreme heat`, `#energy affordability`, `#climate resilience`

---

## Tech Industry &amp; Policy

<a id="item-tech-industry-1"></a>
### [SpaceX and Tesla in talks for $3.5T all-stock merger, FT reports](https://www.techmeme.com/261124/p8#a261124p8) ⭐️ 8.0/10

The Financial Times reported, citing unnamed sources, that SpaceX and Tesla are negotiating an all-stock merger valued at $3.5 trillion, a combination that would be the largest merger on record if completed. The talks are being overseen by two special committees—board groups meant to handle conflicts—of five directors described as &quot;disinterested,&quot; all of whom have ties to Elon Musk, according to the report. The all-stock structure would pay shareholders in shares rather than cash. The report gives no timeline or regulatory-review details, and the account rests on unnamed sources rather than company confirmation.

Techmeme · Nov 24, 10:50

**Verified and unconfirmed:** Verified: The Financial Times reported that SpaceX and Tesla have entrusted five directors with negotiating the terms of a potential $3.5tn combination and are racing to complete a deal before the end of the year. Elon Musk said in October that the two companies were exploring a merger, the New York Times reported.

Not yet confirmed: The $3.5tn valuation, the all-stock structure, the assertion that all five directors have ties to Musk and the year-end deadline all rest on unnamed sources; neither company has confirmed a signed agreement, a board vote or a regulatory filing. The FT account describes a single group of five directors working out terms, while the headline refers to two special committees of five — leaving unresolved whether five directors are involved in total or five on each committee.

**Background:** A special committee is a board group set up to evaluate a transaction when executives or large shareholders have a conflict of interest, and its credibility depends on the members&\#x27; independence from the conflicted parties. The Financial Times reports that the SpaceX and Tesla talks are being handled by two such committees involving five directors described as &quot;disinterested,&quot; but that all five have ties to Elon Musk — the detail that makes the governance structure central to how the proposed deal would be assessed.

**Why it matters:** For Tesla&\#x27;s public shareholders, the decision would rest with five directors the FT describes as having ties to Elon Musk, so the credibility of their independence — not just the $3.5T valuation — becomes the central issue in any approval, and minority investors and listing-rule reviewers are likely to press on how conflicts were handled. The New York Times reported in October that the two companies were already exploring a merger; the change now is that specific all-stock terms and a named negotiating structure are on the table. If a deal proceeds on these terms, Tesla holders would end up owning stock in a combined company whose center of gravity is Musk&\#x27;s private rocket and satellite business rather than the carmaker.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ft.com/content/2585e45e-9133-4215-a2d8-e1275e1033b9?syn-25a6b1a6=1">SpaceX - Tesla : the directors negotiating the biggest merger ever</a></li>
<li><a href="https://www.nytimes.com/2026/10/21/business/elon-musk-spacex-tesla-merger.html">Elon Musk Says SpaceX and Tesla Are Exploring a Merger - The New...</a></li>
<li><a href="https://www.nytimes.com/2026/10/21/business/elon-musk-spacex-tesla-merger.html">Elon Musk Says SpaceX and Tesla Are Exploring a Merger - The New...</a></li>

</ul>
</details>

**Tags**: `#SpaceX`, `#Tesla`, `#Elon Musk`, `#mergers and acquisitions`, `#corporate governance`

---

<a id="item-tech-industry-2"></a>
### [Google reportedly retracted West Bank Maps changes after Israeli pressure, Wired reports](https://www.techmeme.com/261123/p53#a261123p53) ⭐️ 7.0/10

Wired reported, citing anonymous sources, that a Google product manager spent years updating Google Maps to serve Palestinians in the West Bank more accurately—including mapping Israeli checkpoints—and that Google later retracted key parts of that work after Israeli pressure. The report does not specify which Maps features or data were removed, when the rollback happened, or who ordered it. It relies on unnamed sources rather than documents or an on-the-record Google response.

Techmeme · Nov 24, 04:00

**Verified and unconfirmed:** Verified: Wired published an investigation reporting that a Google product manager spent years trying to map Israeli checkpoints in the West Bank more accurately in Google Maps, and that the company later reversed key parts of that work, according to Wired&\#x27;s headline and summary.

Not yet confirmed: That Israeli government pressure was the reason for the rollback — this rests on Wired&\#x27;s unnamed sources, and the item carries no on-record Google statement, no identification of which map changes shipped versus were removed, and no independent verification; Wired itself reported in December 2024 that Palestinians had long complained about missing and outdated West Bank data in Maps.

**Background:** Navigation apps such as Google Maps build routes from a road graph assembled out of licensed data, satellite imagery and user-contributed edits; in the West Bank, Palestinian movement is constrained by Israeli checkpoints and other barriers, so whether those points appear in the graph, and how they are labelled, changes the routes the app suggests. Mapping that infrastructure is therefore a political act as much as a technical one, and the Wired account describes one product manager treating accurate checkpoint mapping as a personal mission inside Google.

**Why it matters:** For Google Maps users in the West Bank, the reported rollback means checkpoint information may be less complete than the product team had built, so navigation there may require local or official confirmation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.wired.com/story/inside-googles-failure-to-make-google-maps-work-for-palestinians/">Inside Google’s Failure to Make Google Maps Work for ...</a></li>
<li><a href="https://www.wired.me/story/inside-googles-failure-to-make-google-maps-work-for-palestinians">Inside Google’s Failure to Make Google Maps Work for Palestinians</a></li>
<li><a href="https://www.wired.com/story/google-maps-west-bank/">How Google Maps Makes It Harder for Palestinians to ... - WIRED</a></li>

</ul>
</details>

**Tags**: `#google-maps`, `#platform-policy`, `#censorship`, `#west-bank`, `#investigative-reporting`

---

<a id="item-tech-industry-3"></a>
### [Two unsecured databases reportedly exposed 3.5 billion credentials](https://www.wired.com/story/3-billion-usernames-passwords-and-documents-leaked-online/) ⭐️ 7.0/10

WIRED reports that a pair of unsecured databases exposed 3.5 billion usernames, passwords and documents belonging to hundreds of millions of people — data the outlet says could let attackers &quot;own&quot; a victim&\#x27;s digital life. &quot;Unsecured&quot; means the databases were left reachable without authentication, rather than being broken into. The report does not name the companies operating the databases, describe how the data was found or by whom, or say whether the exposed records have since been secured or taken offline. The figure of 3.5 billion comes from the reporting itself; no independent verification or sample of the records has been published.

Wired · Nov 24, 11:00

**Verified and unconfirmed:** Verified: WIRED reports that two unsecured databases were found holding sensitive information — usernames, passwords and documents — on hundreds of millions of people, including data that could let an attacker take over a victim&\#x27;s accounts.

Not yet confirmed: The 3.5 billion figure appears in the report&\#x27;s headline without an itemized breakdown; the available text does not name the affected companies or services, say who discovered the databases, establish that the records are genuine and current rather than compiled from older leaks, or confirm whether the databases have since been secured.

**Background:** Both stores were left unauthenticated — reachable from the open internet with no login or password — a configuration failure rather than an intrusion: anyone who located the storage endpoint could read and download records directly, without exploiting a software flaw. The two exposures are unrelated to each other, according to the findings shared with WIRED, so this is a pair of separate misconfigurations rather than one breached provider.

**Why it matters:** Exposed username-and-password pairs are the raw material for credential stuffing, in which attackers replay leaked logins against other services on the assumption that people reuse them — so the practical exposure extends well beyond whatever service held the data. The immediate problem for users is that the report names no affected company, leaving them unable to check whether their accounts were in the set; until the operators are identified, the only defensive step available is the generic one of changing reused passwords and enabling two-factor authentication.

**What to watch:** Watch for the databases to be secured or taken offline, and for the identity of their operators or any confirmation from affected companies — the detail that would let users determine whether they are in the exposed set.

<details><summary>References</summary>
<ul>
<li><a href="https://www.wired.com/story/3-billion-usernames-passwords-and-documents-leaked-online/">Database Leaks Expose 3.5 Billion Usernames, Passwords, and ...</a></li>
<li><a href="https://imtr.net/article/database-leaks-expose-35-billion-usernames-passwords-and-documents-5900">Database Leaks Expose 3.5 Billion Usernames, Passwords, and ...</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#data breach`, `#privacy`, `#credentials`, `#unsecured databases`

---

<a id="item-tech-industry-4"></a>
### [Ladybird&\#x27;s from-scratch browser engine opens alpha testing on macOS and Linux](https://www.theverge.com/tech/1040872/ladybird-indie-browser-engine-alpha-testing) ⭐️ 7.0/10

Ladybird, an independent browser built on an engine written from scratch, is now available in alpha for macOS and Linux, developer Andreas Kling announced. The release comes after more than four years of development and makes Ladybird the first browser in years to ship an entirely new engine, rather than relying on the three that dominate today: Gecko \(Mozilla Firefox\), Blink \(Google Chrome and its derivatives\) and WebKit \(Safari\). The build is an early alpha aimed at testing rather than daily use, and there is no Windows version yet — The Verge reports Kling says one is planned for the &quot;later stages&quot; of the project.

The Verge · Nov 23, 22:38

**Verified and unconfirmed:** Verified: Ladybird&\#x27;s developer announced an alpha release of the browser on macOS and Linux, following more than four years of work; the browser uses an engine developed independently of Gecko, Blink and WebKit.
Not yet confirmed: How well the alpha renders real-world websites, its stability and performance, and any download or hardware requirements — none of these have been independently tested. The timing of a Windows build is also unstated, with The Verge reporting only that it is planned for &quot;later stages&quot; of the project.

**Background:** Nearly all mainstream browsers today run on just three engines — Gecko \(Firefox\), Blink \(Chrome\) and WebKit \(Safari\) — so a genuinely new engine has to implement web standards from scratch rather than inherit an existing codebase. Ladybird&\#x27;s own release plans list Linux and macOS as the targets for the 2026 alpha and a beta planned for 2027, with a native Windows port treated as a lower priority to be considered later.

**Why it matters:** Web compatibility has effectively been set by three engines for more than a decade, so a fourth implementation matters to anyone who depends on one vendor&\#x27;s rendering decisions — site developers and standards participants now get an independent check on whether features behave the same way outside Blink, Gecko and WebKit. The practical caveat for testers is that this is alpha software on two desktop platforms only; treat it as a compatibility test bed, not a browser to migrate to.

**What to watch:** Kling&\#x27;s next milestone posts: whether the alpha moves toward a beta, and when the Windows build promised for the project&\#x27;s &quot;later stages&quot; appears.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ladybird_%28web_browser%29">Ladybird (web browser) - Wikipedia</a></li>
<li><a href="https://ladybird.org/posts/alpha/">Ladybird is now in alpha - Ladybird</a></li>

</ul>
</details>

**Tags**: `#browser engines`, `#Ladybird`, `#open source`, `#software release`, `#web platform`

---