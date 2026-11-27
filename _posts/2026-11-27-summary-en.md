---
layout: issue
permalink: /briefing/2026-11-27/
title: "AI News Briefing: November 27, 2026"
date: 2026-11-27
lang: en
---

> We screened 217 stories from the past day and kept the 12 worth your time.

---

**AI**
1. [AMD-specific fork of llama.cpp draws builder interest on Hacker News](#item-ai-news-1) ⭐️ 7.0/10

**Chips &amp; Computing**
1. [TSMC&\#x27;s A14 1.4nm-class node ready for design with PDK 0.9](#item-chips-compute-1) ⭐️ 8.0/10
2. [Texas lifts data-center permit freeze on 1,800+ projects, FT reports](#item-chips-compute-2) ⭐️ 7.0/10
3. [Indium phosphide supply stays tight as AI optical demand climbs](#item-chips-compute-3) ⭐️ 7.0/10

**EVs &amp; Energy**
1. [Tianwan unit 8 completes hot tests and takes first fuel load](#item-ev-energy-1) ⭐️ 8.0/10
2. [IONNA opens 22-bay, 400 kW California hub with Tesla Autocharge](#item-ev-energy-2) ⭐️ 7.0/10
3. [Spain&\#x27;s Auto+ EV subsidy budget runs dry ahead of elections](#item-ev-energy-3) ⭐️ 7.0/10
4. [MUFG funds two Japan battery projects with inflation-linked capacity contracts](#item-ev-energy-4) ⭐️ 7.0/10
5. [China&\#x27;s Solar Capacity Reaches 1.33 TW as Jiangsu Sets 2027 Auction Terms](#item-ev-energy-5) ⭐️ 7.0/10
6. [Tongwei signs 846 MW module deal for Romania&\#x27;s Dama Solar](#item-ev-energy-6) ⭐️ 7.0/10
7. [HKUST perovskite solar cell reaches 27.04% via trans-interface engineering](#item-ev-energy-7) ⭐️ 7.0/10

**Tech Industry &amp; Policy**
1. [UK FCA plans to require DeFi platforms to get authorization, FT reports](#item-tech-industry-1) ⭐️ 7.0/10

---

## AI

<a id="item-ai-news-1"></a>
### [AMD-specific fork of llama.cpp draws builder interest on Hacker News](https://devnull.land/amd-specific-llama-cpp) ⭐️ 7.0/10

An AMD-targeted fork of llama.cpp has been published and shared on Hacker News, pitched at improving local LLM inference on AMD GPUs. The material available does not include the fork&\#x27;s own benchmarks, the specific AMD GPU generations or ROCm versions it supports, or whether its changes have been proposed upstream to mainline llama.cpp. The discussion around it is substantive rather than incidental: commenters describe a longer-running, informal effort to tune llama.cpp for AMD hardware, including used gfx906 datacenter cards from around 2018 that pair 32GB of HBM2 memory with roughly 1 TB/s of bandwidth for a few hundred dollars.

Hacker News · julianlam · Nov 26, 17:11 · [Discussion](https://news.ycombinator.com/item?id=50657265)

**Verified and unconfirmed:** Verified: The item is a Hacker News submission dated 26 November 2026 titled &quot;AMD-specific fork of llama.cpp&quot;, linking to devnull.land/amd-specific-llama-cpp, and it is presented as an AMD-targeted fork of llama.cpp; the submission itself carries no README, benchmark, version or license text in what was supplied. The comments describe other people&\#x27;s separate AMD-focused forks and tuning work \(gfx906 cards, an MI100 ROCm kernel port, an R9700 setup\), not the contents of this fork.

Not yet confirmed: What this fork changes relative to upstream llama.cpp, which AMD architectures it targets, any measured speedup, its license, and whether it is installable today. The performance figures in the comments — 2400 tok/s prefill and 150 tok/s decode on an R9700, &quot;1 TB/s&quot; HBM2 datacenter cards for $200, tripled Qwen 3.8 speeds on an M1 port — are commenters&\#x27; own claims about their own setups and were not independently checked.

**Background:** llama.cpp is an open-source inference engine for running quantized large language models locally on consumer hardware; its default build paths and kernel tuning have historically centered on Nvidia&\#x27;s CUDA, so AMD users depend on the ROCm/HIP backend and on community forks that add hand-tuned kernels for specific card families. The fork discussed here, llama-cpp-rdna-boosts, is one of those projects: its author reports raising token generation from 35 to 55 tokens per second and prefill from 700 to 1,300 tokens per second on his own AMD setup, with results varying by hardware. Commenters in the Hacker News thread said AMD-optimized forks generally outperform vanilla llama.cpp and asked for a branch switchable by environment variable rather than a separate fork pinned to a commit.

**Why it matters:** For developers running models locally on AMD GPUs, this is another implementation to weigh against mainline llama.cpp and other ROCm-oriented forks. Because it is a fork rather than an upstream change, anyone adopting it should first confirm which GPU generations and ROCm builds it targets and how closely it tracks upstream commits, since diverging from mainline means carrying patch maintenance themselves.

**Community discussion:** Commenter rao-v traces the interest to early 2025, when builders noticed that AMD&\#x27;s circa-2018 gfx906 datacenter cards offered large HBM2 memory and very high bandwidth cheaply, and points to their own repository optimizing llama.cpp for those cards, which lack tensor cores and native bf16 support. fiddlerwoaroof reports using Claude to port Nvidia kernels to ROCm on an MI100 and claims a two-to-three-fold speedup on a Qwen model, saying it has been stable and that the ported kernels were validated; these are individual reports, not independent benchmarks of the fork itself.

<details><summary>References</summary>
<ul>
<li><a href="https://devnull.land/amd-specific-llama-cpp">AMD-specific fork of llama.cpp | devnull.land</a></li>
<li><a href="https://news.ycombinator.com/item?id=50657265">AMD - specific fork of llama . cpp | Hacker News</a></li>

</ul>
</details>

**Tags**: `#llama.cpp`, `#AMD`, `#LLM inference`, `#open-source`, `#GPU optimization`

---

## Chips &amp; Computing

<a id="item-chips-compute-1"></a>
### [TSMC&\#x27;s A14 1.4nm-class node ready for design with PDK 0.9](https://www.tomshardware.com/tech-industry/semiconductors/tsmcs-a14-1-4nm-class-node-is-ready-for-chip-design-boost-cells-promise-14-percent-performance-uplift-or-23-percent-power-cut-over-n2p) ⭐️ 8.0/10

TSMC says its A14 \(1.4nm-class\) process is ready for customer design work, with version 0.9 of its process design kit ready for design-in and Cadence and Synopsys having completed full design-flow certification on an Arm Cortex-A725 CPU core using TSMC foundation IP. The node adds Boost Cells, which TSMC says deliver 14% higher performance at the same power or 23% lower total power at the same speed than N2P with NanoFlex; TSMC also claims 50% better energy efficiency, 22% higher drawn transistor density and 23% higher logic density than baseline N2P. TSMC plans risk production in the second half of 2027 and mass production in the second half of 2028. It also outlined an A14-to-A13 migration path that it says can cut die area by about 6% without changing the A14 design flow, with A13 high-volume manufacturing set for the second half of 2029.

Tom&\#x27;s Hardware · Nov 26, 13:00

**Verified and unconfirmed:** Verified: TSMC said at its 2026 Europe OIP Ecosystem Workshop that A14 PDK 0.9 is ready for design-in and that Cadence and Synopsys completed full design-flow certification on an Arm Cortex-A725 core; the claimed 14% speed, 23% power, 50% energy-efficiency, 22% transistor-density and 23% logic-density gains are TSMC&\#x27;s own comparisons against N2P. Not yet confirmed: independent measurements of those gains, actual customer tapeout results or yields, A14 pricing, and whether the H2 2027 risk-production and H2 2028 mass-production schedules hold.

**Background:** A process design kit \(PDK\) is the bundle of transistor models, design rules and standard-cell libraries a foundry gives customers so commercial EDA tools can simulate, place and route a chip; version 0.9 is the revision the industry conventionally treats as usable for real design work, which is why TSMC frames it as &quot;ready for design-in&quot; well before any silicon ships. A14 is the successor to N2P, TSMC&\#x27;s 2nm-class node with its NanoFlex cell architecture, and the performance, power and density figures in the announcement are all stated against that N2P baseline.

**Why it matters:** Chip designers planning A14 products can now start implementation with Cadence or Synopsys flows that TSMC has certified end-to-end on an Arm Cortex-A725 core, reducing the risk that tool gaps delay a project. Teams using Siemens EDA have only partial certification—5 of 13 categories as of October 1—and must wait for transistor-level EM/IR certification targeted for the fourth quarter of 2026 before that flow covers the full sign-off chain.

**What to watch:** Siemens EDA&\#x27;s transistor-level EM/IR certification is targeted for the fourth quarter of 2026; the next hard checkpoints after that are A14 risk production in the second half of 2027 and mass production in the second half of 2028.

**Tags**: `#TSMC`, `#A14`, `#1.4nm-class`, `#semiconductor manufacturing`, `#EDA`

---

<a id="item-chips-compute-2"></a>
### [Texas lifts data-center permit freeze on 1,800+ projects, FT reports](https://www.tomshardware.com/tech-industry/data-centers/texas-lifts-freeze-on-1-800-data-center-projects-in-greg-abbott-u-turn-companies-rush-for-permits-before-gina-hinojosas-january-arrival) ⭐️ 7.0/10

Texas has resumed approving data-center projects after an August freeze, acting on a directive from outgoing Governor Greg Abbott&\#x27;s office that affects more than 1,800 projects and 474 gigawatts of power requests, Tom&\#x27;s Hardware reported, citing the Financial Times. The state grid operator, ERCOT, has finished gathering information on how data centers affect local communities, the report said. Developers are rushing to get approvals before Governor-elect Gina Hinojosa, who has pledged to rein in data-center construction, takes office in January. The report did not say how many permits have been issued since the resumption or how quickly ERCOT will process the 474 GW of requests.

Tom&\#x27;s Hardware · Nov 27, 11:00

**Verified and unconfirmed:** Verified: Tom&\#x27;s Hardware, citing the Financial Times, reported that Governor Greg Abbott&\#x27;s office confirmed the Electric Reliability Council of Texas \(ERCOT\) had finished gathering information on how data centers affect local communities and that the state has resumed approving data center projects; the August halt covered more than 1,800 projects and 474 GW of power requests, figures IBTimes also reported when the freeze was ordered. ZeroHedge, citing Politico, said the Texas Commission on Environmental Quality had returned to normal permit review in November and that the first permit issued after the freeze appears to have gone to SpaceX&\#x27;s $24 billion Starbase project.

Not yet confirmed: No ERCOT or governor&\#x27;s office document is quoted, and the report gives no count of permits approved since the resumption, no timeline for clearing the backlog, and no statement from Governor-elect Gina Hinojosa&\#x27;s office beyond her earlier pledge to rein in construction; the characterization that developers are &quot;rushing&quot; to beat her January inauguration rests on FT&\#x27;s reporting, and the SpaceX-first-permit detail rests on a single Politico account relayed by ZeroHedge.

**Background:** ERCOT, the nonprofit that operates most of Texas&\#x27;s power grid, must review the large new electricity loads data centers request before they can connect, which is why the state&\#x27;s permit pause could halt projects even where land and financing were in place. The freeze began in August, when Governor Greg Abbott&\#x27;s office stopped approvals and left 474 gigawatts of power requests subject to the moratorium, and in October the state suspended 17 more construction permits and shut an automated portal that had kept approving them. The reversal comes as Governor-elect Gina Hinojosa, who won in November, has called for a pause on new data centers until the state adopts protections for host communities; the Texas Tribune reported that approvals could stay paused until legislators pass new laws next year if she keeps those campaign promises.

**Why it matters:** Developers can now seek approvals again, but the relief may be short-lived: Hinojosa takes office in January and has pledged to curb construction. The report also cautions that new power requests will not be processed quickly, pushing some developers to build their own generation, with gas turbines among the options.

**What to watch:** Hinojosa&\#x27;s first moves on data-center permitting after she takes office in January, and ERCOT&\#x27;s processing pace for the 474 GW of requests.

<details><summary>References</summary>
<ul>
<li><a href="https://www.zerohedge.com/energy/texas-first-data-center-permit-after-freeze-went-spacexs-24b-starbase-project">Texas &#x27; First Data - Center Permit After The Freeze Went... | ZeroHedge</a></li>
<li><a href="https://www.ibtimes.co.uk/texas-halts-data-centre-grid-connections-ai-energy-surge-1813892">Texas &#x27;AI Epicentre&#x27; Pauses Data Center Connections as ERCOT ...</a></li>
<li><a href="https://www.texastribune.org/2026/11/04/data-center-texas-pause-gina-hinojosa-governor-policies/">Under Hinojosa, Texas data center approvals could stay paused</a></li>
<li><a href="https://www.usatoday.com/story/news/2026/11/06/hinojosa-texas-data-centers-pause-what-to-know/92641237007/">Texas Governor-elect Hinojosa calls for data center pause</a></li>

</ul>
</details>

**Tags**: `#data centers`, `#Texas`, `#power grid`, `#permitting`, `#capacity`

---

<a id="item-chips-compute-3"></a>
### [Indium phosphide supply stays tight as AI optical demand climbs](https://www.tomshardware.com/tech-industry/photonics/inside-the-indium-phosphide-squeeze-and-the-optical-boom-inp-remains-tightly-constrained-as-the-demand-from-ai-puts-the-entire-supply-chain-under-pressure) ⭐️ 7.0/10

Indium phosphide \(InP\), the compound semiconductor used to make the lasers and photodetectors that turn electrical data into light, is the binding constraint on the optical links that AI data centers are switching to, according to this Tom&\#x27;s Hardware explainer. Sumitomo Electric and AXT together account for almost 80% of global InP substrate manufacturing, with JX Advanced Metals adding roughly another 10%. AXT makes most of its substrates in China, where exports now require government licences, and China produces around 70% of the world&\#x27;s refined indium, so controls bite on both the raw material and the finished wafer. Lumentum CEO Michael Hurlston said in July that its InP fabs were shipping more than 30% below customer demand despite rapid capacity expansion, and Coherent called InP capacity the &quot;primary constraint&quot; on its transceiver business. The report adds that Nvidia has invested $2 billion each in Lumentum and Coherent, attaching multibillion-dollar purchase commitments and future capacity rights, while new substrate and laser capacity can take years to qualify.

Tom&\#x27;s Hardware · Nov 26, 16:00

**Verified and unconfirmed:** Verified: Tom&\#x27;s Hardware reports the substrate market shares for Sumitomo Electric, AXT and JX Advanced Metals, China&\#x27;s roughly 70% share of refined indium, and the Chinese export-licensing requirement on AXT&\#x27;s substrate output; it also quotes Lumentum&\#x27;s CEO on fabs running more than 30% below demand and Coherent describing InP capacity as its primary constraint, both company statements.
Not yet confirmed: no independent measurement of the size of the shortfall is given — the demand gap rests on the two vendors&\#x27; own characterisations — and the report offers no timeline for when new InP capacity or newly qualified suppliers will reach volume, nor the detailed terms behind Nvidia&\#x27;s stated $2 billion investment in each company.

**Background:** Indium phosphide is a III-V compound semiconductor with a direct bandgap of about 1.34 eV, which lets it emit light efficiently; silicon&\#x27;s indirect bandgap mostly produces heat instead. That is why silicon-photonic systems, which can guide and modulate light using mature CMOS-style processes, still rely on InP-based lasers and other active optical components — demand that is growing as AI data centers move from copper links to optics.

**Why it matters:** Because Nvidia has tied its optical-component supply to capacity rights and purchase commitments at Lumentum and Coherent, buyers outside those agreements may find remaining InP laser and transceiver capacity allocated first to Nvidia&\#x27;s accelerator buildouts. Moving to silicon photonics does not remove the dependency: silicon can guide and modulate light but has an indirect bandgap and does not emit it, so these systems still need a III-V laser, usually built on InP.

**What to watch:** Watch Lumentum&\#x27;s and Coherent&\#x27;s upcoming quarterly results for whether InP fab output closes the gap with demand, and whether China&\#x27;s export-licensing regime for indium and InP wafers tightens or eases.

**Tags**: `#indium phosphide`, `#optical interconnect`, `#AI data centers`, `#semiconductor supply chain`, `#photonics`

---

## EVs &amp; Energy

<a id="item-ev-energy-1"></a>
### [Tianwan unit 8 completes hot tests and takes first fuel load](https://www.world-nuclear-news.org/articles/Tianwan-moving-step-closer-becoming-worlds-biggest-nuclear-power-plant) ⭐️ 8.0/10

Tianwan unit 8 in China has completed hot tests — the pre-operational run-through of plant systems before the reactor is started — and received its initial fuel load, World Nuclear News reported. Delivering fuel moves the unit into the last stage of commissioning, ahead of start-up and connection to the grid. The site is expected to become the world&\#x27;s largest nuclear power plant once all eight of its units are in operation, a status that depends on every unit running rather than on unit 8&\#x27;s fuel delivery alone.

World Nuclear News · Nov 26, 14:33

**Verified and unconfirmed:** Verified: World Nuclear News reports that hot tests are complete for Tianwan unit 8 and that its initial fuel load has been delivered.
Not yet confirmed: No start-up date, grid-connection date or commercial operation date is given, and no independent confirmation of the testing results is available; the &quot;world&\#x27;s largest nuclear power plant&quot; description rests on the site&\#x27;s expectation that all eight units will eventually operate.

**Background:** Tianwan sits on the Yellow Sea coast near Lianyungang in Jiangsu province, and its newest pair, units 7 and 8, are Russian-designed VVER-1200 pressurized water reactors built under agreements Russia and China signed in June 2018; units 5 and 6 use Chinese ACPR1000 reactors. Hot tests are the non-nuclear checks of plant systems at operating temperature and pressure, and delivery of the initial fuel load is a later commissioning step before a reactor can start. Unit 7, the first of the VVER-1200 pair, had already begun loading fuel in a reported shift from construction to nuclear commissioning.

**Why it matters:** Fuel loading is the point after which a reactor&\#x27;s schedule is measured in start-up steps rather than construction milestones, so unit 8 is now the unit to track for new baseload capacity at Tianwan. The site cannot claim the &quot;world&\#x27;s largest&quot; title until all eight units are running, which makes the operating status of the other units as important as unit 8&\#x27;s progress.

**What to watch:** Watch for the announcement of first criticality and grid connection for Tianwan unit 8, the next checkable steps before commercial operation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tianwan_Nuclear_Power_Plant">Tianwan Nuclear Power Plant - Wikipedia</a></li>
<li><a href="https://www.world-nuclear-news.org/articles/Tianwan-moving-step-closer-becoming-worlds-biggest-nuclear-power-plant">Tianwan moves step closer to becoming... - World Nuclear News</a></li>
<li><a href="https://interestingengineering.com/energy/china-loads-first-fuel-into-new-1-2gw-reactor-at-worlds-largest-nuclear-plant">China loads first fuel into new 1.2GW reactor at Tianwan nuclear plant</a></li>

</ul>
</details>

**Tags**: `#nuclear power`, `#Tianwan`, `#China energy`, `#reactor commissioning`, `#clean energy`

---

<a id="item-ev-energy-2"></a>
### [IONNA opens 22-bay, 400 kW California hub with Tesla Autocharge](https://www.electrive.com/2026/11/26/ionna-opens-22-bay-charging-hub-in-california-and-adds-tesla-autocharge/) ⭐️ 7.0/10

IONNA has opened a flagship charging site in Westminster, California, with 22 charging bays and peak power of up to 400 kW, according to electrive. The opening coincides with an expansion of automatic charging authentication to Tesla vehicles, so a compatible car identifies itself over the charging cable and a session starts without an app or card. Support for models from Stellantis brands is scheduled to follow in December. The report does not say which Tesla models are covered, how much power an individual bay delivers when the site is busy, or what the hub charges per kWh.

Electrive · Nov 26, 18:30

**Verified and unconfirmed:** Verified: electrive reports that IONNA opened a 22-bay site in Westminster, California, with peak power of up to 400 kW, and that automatic charging authentication has been extended to Tesla vehicles, with Stellantis brands to follow in December.
Not yet confirmed: which Tesla models and software versions actually support the automatic authentication, the exact December date for Stellantis brands, whether all 22 bays can deliver 400 kW simultaneously, and the site&\#x27;s pricing. These details rest on IONNA&\#x27;s announcement and were not independently tested.

**Background:** Automatic charging authentication — often branded Autocharge or Plug &amp; Charge — lets a vehicle identify itself to the charger over the cable, so a session starts and bills without an app, card or RFID tag. IONNA runs a US fast-charging network, and this site&\#x27;s launch is paired with extending that automatic authentication to Tesla cars, with models from Stellantis brands to be added in December.

**Why it matters:** For Tesla drivers, an IONNA bay can now work like a Tesla Supercharger: plug in and the session starts, with no app, card or screen interaction, which removes the main friction that has kept some owners on Tesla&\#x27;s own network. The practical check is whether a given car has the feature enabled — drivers heading to Westminster should confirm their model is supported before relying on plug-and-charge, and Stellantis owners will have to wait for the December rollout.

**What to watch:** Whether IONNA publishes the list of Tesla models and software versions supported by automatic authentication, and whether the promised Stellantis brand support arrives on schedule in December.

**Tags**: `#IONNA`, `#EV charging infrastructure`, `#Tesla Autocharge`, `#California`, `#400 kW charging`

---

<a id="item-ev-energy-3"></a>
### [Spain&\#x27;s Auto+ EV subsidy budget runs dry ahead of elections](https://www.electrive.com/2026/11/26/budget-exhausted-spain-cuts-purchase-subsidies-for-electric-cars/) ⭐️ 7.0/10

Spain&\#x27;s Auto+ purchase-incentive programme for private buyers has used up its budget after the government allocated €350 million for electric cars and plug-in hybrids over a short period. According to electrive, the pot will not be refilled &quot;for the foreseeable future&quot; because parliamentary elections are approaching. The upshot is that private buyers in Spain can no longer count on the national purchase subsidy when pricing an EV or plug-in hybrid. The report does not say whether applications already in the pipeline will still be paid.

Electrive · Nov 26, 11:30

**Verified and unconfirmed:** Verified: electrive reports that the Auto+ budget for private individuals is exhausted and that €350 million was allocated to purchase incentives for electric cars and plug-in hybrids.
Not yet confirmed: the report cites no primary government document, so the exact remaining balance, the treatment of pending applications, and the claim that funding will not be restored for the foreseeable future rest on the outlet&\#x27;s reporting rather than an official statement.

**Background:** Auto+ is Spain&\#x27;s purchase-incentive scheme for private individuals buying battery-electric cars and plug-in hybrids; it pays part of the upfront price, lowering the effective cost of the vehicle. Spain allocated €350 million to the program.

**Why it matters:** Private buyers in Spain lose the national purchase incentive as a factor in their purchasing decision, effectively raising the net price of an electric or plug-in hybrid car relative to the subsidised level, while the report leaves open what happens to buyers who applied before the money ran out — a question worth resolving with a dealer or the administering body before committing to an order.

**What to watch:** Watch Spain&\#x27;s parliamentary elections and the funding decisions of the government that follows them, since the report ties the decision not to replenish Auto+ to that vote.

**Tags**: `#Spain`, `#EV purchase subsidies`, `#policy change`, `#EV market`, `#Auto+ program`

---

<a id="item-ev-energy-4"></a>
### [MUFG funds two Japan battery projects with inflation-linked capacity contracts](https://www.pv-magazine.com/2026/11/27/japan-battery-financing-adapts-to-inflation-linked-capacity-contracts/) ⭐️ 7.0/10

MUFG Bank has made initial loan disbursements under project-finance agreements for two grid-scale battery storage projects in Japan, HEXA Energy Services said: one in Bibai, Hokkaido, and one in Kumamoto, with combined grid-connection capacity of 90 MW. Both projects won capacity contracts in Japan&\#x27;s fiscal 2023 long-term decarbonization power auction, and the loans are the first to price in the auction&\#x27;s newly introduced contract price adjustment mechanism, which indexes payments to changes in inflation and interest rates. HEXA said the initial disbursements were completed in about two months, but it did not disclose the loan amount, tenor, or the projects&\#x27; storage capacity in megawatt-hours.

pv magazine · Nov 27, 11:15

**Verified and unconfirmed:** Verified: HEXA Energy Services and MUFG Bank both said initial loan disbursements have been made for the two projects, and the companies put their combined grid-connection capacity at 90 MW; the projects won contracts in the fiscal 2023 long-term decarbonization auction, and MUFG said the financing addressed the auction&\#x27;s new contract price adjustment mechanism. Not yet confirmed: the loan amount, tenor, per-project megawatt-hour capacity, and the exact formula or caps of the inflation- and interest-linked price adjustment, none of which HEXA disclosed; no independent party has confirmed the financing terms.

**Background:** Japan&\#x27;s Long-Term Decarbonization Power Source Auction, launched in fiscal 2023, awards successful bidders 20-year fixed capacity payments to offset the large upfront cost of assets such as grid-scale batteries; the first auction was held in January 2024. Because those payments were fixed in nominal terms, inflation eroded their value, and the government raised the auction&\#x27;s price cap ahead of its third round to counter inflation pressures. The contract price adjustment mechanism indexing payments to inflation and interest rates that MUFG had to model is the newer layer of that same design.

**Why it matters:** This is HEXA&\#x27;s third round of project debt for auction-backed batteries, giving other fiscal 2023 auction winners a worked example of how banks will treat inflation- and interest-indexed capacity payments — a structure lenders had not previously financed in Japan. Developers weighing bids in later auction rounds should watch how much of the indexation risk lenders absorb versus pass back to the project.

**What to watch:** HEXA plans to arrange project finance in its 2026 fiscal year for a battery project in Oyabe, Toyama prefecture; whether that deal reuses the same indexed-contract terms will show if the structure is becoming standard. Separately, Japan&\#x27;s connection queue — about 172 GW at the study stage versus roughly 0.64 GW actually connected at the end of 2025 — remains the binding constraint on turning financed projects into operating ones.

<details><summary>References</summary>
<ul>
<li><a href="https://shulman-advisory.com/japan-doubles-ltda-price-cap-ahead-of-3rd-auction-to-counter-inflation-pressures/">Japan Doubles LTDA Price Cap Ahead of 3rd Auction to Counter ...</a></li>
<li><a href="https://www.nishimura.com/sites/default/files/newsletters/file/natural_resources_energy_241224_en.pdf">Long-Term Decarbonization Power Source Auctions in Japan ...</a></li>

</ul>
</details>

**Tags**: `#Japan`, `#grid-scale battery storage`, `#project finance`, `#capacity contracts`, `#MUFG`

---

<a id="item-ev-energy-5"></a>
### [China&\#x27;s Solar Capacity Reaches 1.33 TW as Jiangsu Sets 2027 Auction Terms](https://www.pv-magazine.com/2026/11/27/chinese-pv-industry-brief-china-hits-1-33-tw-of-cumulative-solar-capacity/) ⭐️ 7.0/10

China&\#x27;s cumulative installed solar capacity reached about 1.33 TW at the end of October 2026, up 16.3% year on year, according to National Energy Administration \(NEA\) figures reported by pv magazine. October additions of 12.86 GW were down 5.7% from September, bringing installations for the first ten months of 2026 to roughly 123.69 GW. Separately, the Jiangsu Provincial Development and Reform Commission published its 2027 mechanism price auction framework for new renewable projects, covering an initial 13 TWh — 12.5 TWh of it for solar and onshore wind — with bids allowed between CNY 0.200 \($0.029\)/kWh and CNY 0.391/kWh and a 10-year settlement period. For newly approved utility-scale projects, the volume eligible for mechanism price settlement will be scaled to actual grid-export utilization hours relative to local averages for comparable projects.

pv magazine · Nov 27, 11:06

**Verified and unconfirmed:** Verified: The NEA reported ~1.33 TW cumulative solar capacity at end-October 2026, +16.3% year on year, with 12.86 GW added in October and ~123.69 GW in January–October, per pv magazine. Jiangsu&\#x27;s development and reform commission published the 13 TWh, CNY 0.200–0.391/kWh, 10-year-settlement framework. Trina Solar&\#x27;s board-level plan to inject CNY 1.35 billion into Trina Storage would lift its stake from 60.14% to 68.43%. Not yet confirmed: The Trina capital injection is subject to shareholder approval and has not closed. Longi&\#x27;s and Trina&\#x27;s 2027 related-party transaction figures \(CNY 1.186 billion and CNY 152 million\) are estimates, not confirmed orders. The Yongjie Aluminum project is not yet running; the Dec. 28 start date and the projected CNY 9 million carbon-tariff and CNY 3 million electricity savings are the NEA&\#x27;s and project partners&\#x27; expectations. China Huaneng&\#x27;s 400 MW offshore solar project has only begun construction.

**Background:** A terawatt is 1,000 gigawatts, so China’s 1.33 TW of cumulative solar capacity equals about 1,330 GW of installed peak generating potential, not actual output. Jiangsu’s “mechanism price” auction is a provincial competitive tender that fixes the settlement price winning renewable projects receive for a set period; the 2027 framework sets a 10-year settlement term and a bidding band of CNY 0.200–0.391/kWh.

**Why it matters:** Jiangsu&\#x27;s utilization-hours adjustment means developers bidding into the 2027 auction carry the risk of curtailment themselves: if a plant exports less power than comparable local projects, the share of its output paid at the mechanism price shrinks, which puts a premium on siting and grid-connection quality rather than on bid price alone. The CNY 0.200–0.391/kWh band also gives developers a firm reference for project economics a year ahead.

**What to watch:** The NEA said the 72 MW solar plus 30 MW/75 MWh battery project supplying Yongjie Aluminum in Zhejiang is scheduled to begin operations on Dec. 28, a test of whether direct green-power supply can cut an aluminum producer&\#x27;s carbon tariff and electricity costs as projected. Jiangsu&\#x27;s 2027 auction results, including clearing prices within the published band, will show how developers price utilization risk.

**Tags**: `#China solar`, `#solar capacity`, `#renewable energy policy`, `#Jiangsu auction`, `#clean energy`

---

<a id="item-ev-energy-6"></a>
### [Tongwei signs 846 MW module deal for Romania&\#x27;s Dama Solar](https://www.pv-magazine.com/2026/11/27/tongwei-signs-846-mw-module-deal-for-romanias-dama-solar-project/) ⭐️ 7.0/10

Tongwei and Rezolv Energy have signed an agreement for 846 MW of Tongwei TNC 3.0 modules for the Dama Solar project in Arad County, western Romania. The plant is planned at 1.36 GWp of installed capacity and is expected to generate about 1,800 GWh of electricity a year once operational. The modules use a quarter-cut cell design that Tongwei says combines high power output with long-term reliability; Tongwei is handling production scheduling and supply coordination from its vertically integrated manufacturing chain. The first truckload of modules has left Tongwei&\#x27;s Nantong facility, which the company describes as the start of deliveries under the agreement — the plant itself is not yet built or generating.

pv magazine · Nov 27, 10:00

**Verified and unconfirmed:** Verified: pv magazine reported that Tongwei and Rezolv Energy signed an 846 MW supply agreement for TNC 3.0 modules, and Tongwei said the first truckload had departed its Nantong plant; the project&\#x27;s 1.36 GWp capacity and Arad County location come from the same report. Not yet confirmed: the roughly 1,800 GWh annual generation figure is a projection for an unbuilt plant, and module pricing, the delivery schedule, and a construction or commissioning date were not disclosed; the description of Dama Solar as one of Europe&\#x27;s largest single-site solar plants rests on the companies&\#x27; characterization rather than an independent ranking.

**Background:** Dama Solar is being developed by Rezolv Energy, the independent renewable power producer Actis established in 2022, on a flat site in Arad County that Rezolv describes as being in final development with grid access already confirmed near the site. In September 2026 the European Investment Bank agreed €100 million in financing for the 1.3 GWp plant, which will connect to Romania&\#x27;s high-voltage network. The Tongwei order therefore shifts the project from financing into equipment procurement, with the first truckload already dispatched from Tongwei&\#x27;s Nantong factory.

**Why it matters:** The agreement covers modules only, so the 846 MW order secures panel supply but leaves inverters, construction contracts, grid connection and commissioning as separate, undisclosed steps — the practical thing to track for anyone gauging when Dama Solar&\#x27;s 1.36 GWp actually reaches the Romanian grid. It also shows a Chinese manufacturer placing a multi-hundred-megawatt order into an EU utility-scale project, with shipments already moving rather than merely contracted.

**What to watch:** Watch for the completion of the remaining module deliveries from Nantong and for Rezolv&\#x27;s construction and grid-connection milestones in Arad County. No delivery completion date or commissioning date was disclosed in the announcement.

<details><summary>References</summary>
<ul>
<li><a href="https://rezolv.energy/project/dama-solar/">Dama Solar - Rezolv Energy</a></li>
<li><a href="https://www.eib.org/en/press/all/2026-324-eib-powers-europe-s-solar-future-with-eur100-million-for-romania-s-1-3-gwp-dama-solar">EIB powers Europe’s solar future with €100 million for ...</a></li>

</ul>
</details>

**Tags**: `#solar`, `#Romania`, `#Tongwei`, `#Rezolv Energy`, `#utility-scale PV`

---

<a id="item-ev-energy-7"></a>
### [HKUST perovskite solar cell reaches 27.04% via trans-interface engineering](https://www.pv-magazine.com/2026/11/27/hong-kong-researchers-build-27-04-efficient-perovskite-solar-cell-via-trans-interface-engineering/) ⭐️ 7.0/10

Researchers at the Hong Kong University of Science and Technology \(HKUST\) reported a lab-scale perovskite solar cell that reached 27.04% power conversion efficiency, with a certified value of 26.67% from an undisclosed certification body. Their trans-interface engineering approach replaces a planar interlayer with vertically aligned, covalently bonded nanolinks that penetrate both the perovskite absorber and the charge-transport layer, intended to improve charge transfer and resist mechanical failure at that interface. In one-sun maximum-power-point testing, 92% of tested devices retained 80% of initial efficiency for at least 1,400 hours \(T80\), a result the team presents as evidence of both stability and device-to-device reproducibility. The work was published in Nature Photonics and remains a research result, not a commercial module or independently scaled manufacturing process.

pv magazine · Nov 27, 09:57

**Verified and unconfirmed:** Verified: HKUST researchers published the work in Nature Photonics as the November 2026 cover article \(Volume 20, Issue 11\), and both the paper&\#x27;s abstract and the HKUST announcement confirm a certified power conversion efficiency of 26.67%, with the team&\#x27;s best cell reaching 27.04%; the paper also reports that 92% of tested devices held T80 lifetimes of at least 1,400 hours under maximum-power-point tracking and one-sun illumination.

Not yet confirmed: The certification body is not named in either the paper abstract or the pv magazine report, the 27.04% figure is the team&\#x27;s own best-cell measurement rather than the certified value, and nothing in the supplied material shows independent replication, module-scale or commercial manufacturing data, or a cost and production timeline — the paper&\#x27;s claim that TIE extends to other multilayer optoelectronic devices also remains untested outside this study.

**Background:** Perovskite solar cells use a thin crystalline absorber that has risen fast in laboratory efficiency but still degrades under heat, moisture and mechanical stress, which is why stability rather than raw power output has held the technology back from mass production. The boundary between the perovskite absorber and the adjacent charge-transport layer is a known weak spot: the usual fix is to insert a flat passivating interlayer, which can improve defect passivation and adhesion but forces a trade-off between extracting charge efficiently and keeping the interface mechanically stable. HKUST&\#x27;s trans-interface engineering instead grows nanolinks that run vertically through both layers, bonding them into one continuous structure rather than placing a separate film between them.

**Why it matters:** For perovskite developers, the result points to interface mechanics as well as electrical passivation as a reproducibility lever: HKUST bonds the absorber and transport layer together, and reports that 92% of cells reached the 1,400-hour T80 mark. Teams seeking to compare or reproduce the 26.67% certified figure will need the certification body named and the linker and AIBN-derived radical initiation steps replicated.

**What to watch:** Watch for the certification body to be named and for independent groups to reproduce the 26.67% certified result; a module-scale demonstration would be the next test beyond this cell-level paper.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41566-026-02007-w">Trans-interface engineering for reliable perovskite ... - Nature</a></li>
<li><a href="https://hkust.edu.hk/news/hkust-pioneers-trans-interface-engineering-boost-perovskite-solar-cell-efficiency-and">HKUST Pioneers Trans-Interface Engineering to Boost ...</a></li>

</ul>
</details>

**Tags**: `#perovskite solar cells`, `#solar PV`, `#interface engineering`, `#HKUST`, `#clean energy`

---

## Tech Industry &amp; Policy

<a id="item-tech-industry-1"></a>
### [UK FCA plans to require DeFi platforms to get authorization, FT reports](https://www.techmeme.com/261126/p17#a261126p17) ⭐️ 7.0/10

The UK Financial Conduct Authority plans to require decentralized finance \(DeFi\) platforms — services that run lending, trading and similar functions through smart contracts rather than a central operator — to obtain authorization before serving UK users, according to a Financial Times report. The FCA cited &quot;lack of consumer protections&quot; and the Binance heist, which the report puts at $6.3 billion, as its reasons. The FT describes the approach as stricter than those taken in the US and the EU. No draft rules, scope definition or timetable were included in the account, so the plan is a stated intention rather than a published or finalized regime.

Techmeme · Nov 26, 13:10

**Verified and unconfirmed:** Verified: The Financial Times reported that the FCA says it plans to require DeFi platforms to obtain authorization, and that the regulator gave consumer-protection gaps and the Binance hack as its rationale.
Not yet confirmed: The exact scope \(which activities and which entities count as the regulated party\), the timing of any consultation or final rules, whether the requirement is a firm policy decision or a proposal, and the $6.3 billion loss figure — none of these are detailed in the available account, and no FCA publication or statement was cited directly.

**Background:** DeFi, or decentralised finance, refers to lending, trading and similar services run by smart contracts on public blockchains rather than by a licensed firm with a legal entity behind it — the gap the FCA cites when it says the sector lacks consumer protections. The case the FT reports the regulator pointing to is the October hack at the centralised exchange Binance, which it described as a record $6.3bn theft; Forklog reported that hackers linked to North Korea laundered the proceeds through decentralised protocols including THORChain. AI Daily Radar&\#x27;s 23 November digest reported that the US Department of Justice was seeking forfeiture of more than $1 billion in cryptocurrency stolen from Binance, a court request rather than a confirmed recovery, which illustrates how far the aftermath of that heist has already reached into US enforcement.

**Why it matters:** If adopted, the requirement would make the UK one of the few major jurisdictions to force DeFi front-ends and protocol operators to hold authorization, which for teams without a legal entity in the UK most likely means geoblocking British users or restructuring how the service is offered — and because most DeFi protocols are permissionless, enforcement would probably fall on websites, wallets and interfaces rather than on the contracts themselves.

**What to watch:** Watch for the FCA&\#x27;s formal consultation or policy paper, which should define which DeFi activities fall in scope and when the requirement would take effect.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techmeme.com/261123/p30#a261123p30">2026-11-23 — DOJ seeks forfeiture of $1B+ stolen from Binance, Bloomberg reports</a></li>
<li><a href="https://forklog.com/en/uk-to-tighten-regulations-for-defi-platforms-following-binance-hack/">UK to Tighten Regulations for DeFi Platforms Following Binance Hack</a></li>

</ul>
</details>

**Tags**: `#UK FCA`, `#DeFi regulation`, `#crypto policy`, `#Binance hack`, `#financial regulation`

---