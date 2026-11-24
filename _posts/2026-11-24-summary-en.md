---
layout: issue
permalink: /briefing/2026-11-24/
title: "AI News Briefing: November 24, 2026"
date: 2026-11-24
lang: en
---

> We screened 276 stories from the past day and kept the 7 worth your time.

---

**AI**
1. [Anthropic formal-math repo posts Lean claim VP ≠ VNP over every field](#item-ai-news-1) ⭐️ 7.0/10
2. [Google&\#x27;s AI Mode expands Personal Intelligence to Drive, Wallet and Gemini](#item-ai-news-2) ⭐️ 7.0/10
3. [ByteDance&\#x27;s Doubao phone push hits app-ecosystem limits, GeekPark argues](#item-ai-news-3) ⭐️ 7.0/10

**EVs &amp; Energy**
1. [Jordan to seek private investors for 200 MW solar and 400 MWh battery storage](#item-ev-energy-1) ⭐️ 7.0/10
2. [Saudi Arabia raises self-consumption cap to 50 MW and allows battery storage](#item-ev-energy-2) ⭐️ 7.0/10

**Space**
1. [Myriota raises about $40M in first close of Series C](#item-space-1) ⭐️ 7.0/10

**Tech Industry &amp; Policy**
1. [Ladybird releases first alpha of its from-scratch browser engine](#item-tech-industry-1) ⭐️ 7.0/10

---

## AI

<a id="item-ai-news-1"></a>
### [Anthropic formal-math repo posts Lean claim VP ≠ VNP over every field](https://github.com/anthropics/formal-math/tree/main/vp-vnp) ⭐️ 7.0/10

Anthropic&\#x27;s public formal-math repository now hosts a Lean formalization claiming that VP ≠ VNP over every field, separating two algebraic complexity classes that are analogues of P and NP. Lean is a proof assistant in which such arguments can be machine-checked, but the posting is not a peer-reviewed validation, and the material does not explain any AI method behind the proof. The claim is narrower than P vs NP and is presented for complexity theorists and formal-verification researchers to inspect.

Hacker News · mikeryan52 · Nov 23, 22:09 · [Discussion](https://news.ycombinator.com/item?id=50620102)

**Verified and unconfirmed:** Verified: Anthropic&\#x27;s formal-math GitHub repository hosts a paper titled “VP ≠ VNP over every field,” credited to Claude/Anthropic, alongside a Lean 4 formalization reported at roughly 73,000 lines; the repository describes the work as a research artifact Anthropic does not maintain and states that no human mathematician has checked the proof.
Not yet confirmed: The mathematical claim that VP ≠ VNP over every field has not been independently verified or peer-reviewed, and the paper itself says it has not analyzed how the argument relates to relativization or algebrization; it also remains unclear how much of the work was AI-generated beyond the “Claude” attribution.

**Background:** VP and VNP are the algebraic analogues of P and NP: VP covers problems solvable by polynomial-size arithmetic circuits, VNP those whose polynomials are sums of monomials that can be computed efficiently, so VP ≠ VNP is the algebraic counterpart of the P vs NP question and has been open since Valiant formulated it in the 1970s. The work is hosted in Anthropic&\#x27;s formal-math repository as a Lean development — Lean being an interactive proof assistant that machine-checks every step of a proof against a small trusted kernel — which is why the thread read it as a sign of AI-assisted mathematics rather than a conventional paper announcement. The authors themselves note in the paper that &quot;we have not analysed how it relates to relativization and algebrization&quot;, the standard barrier results any such separation must come to terms with.

**Why it matters:** For complexity theorists and Lean users, the practical consequence is an auditing job rather than a settled theorem: the development can be built and inspected \(one commenter pointed to a browser tool for reading the Lean source without a local setup\), but standard references still describe a lower bound on the permanent&\#x27;s circuit size — what VP ≠ VNP requires — as an outstanding open problem, so the formalization&\#x27;s axiom list, definitions and any unfinished proofs should be checked before the result is cited or extended. The paper itself concedes it has not analysed how the argument relates to relativization and algebrization, the usual barriers for separating complexity classes, and states that it does not settle P versus NP.

**What to watch:** The next check is independent machine-checking of the Lean development and any peer-reviewed write-up that addresses the paper&\#x27;s stated lack of analysis of relativization and algebrization.

**Community discussion:** Commenters read the post as Anthropic pushing toward P vs NP and debated whether AI will soon solve problems that would otherwise occupy graduate students for years; one commenter highlighted the paper&\#x27;s own admission that it has not analyzed relativization or algebrization, barriers relevant to such complexity-theory separations.

<details><summary>References</summary>
<ul>
<li><a href="https://agihunt.info/en/e/1a20a795a118dbdb4f5bd2bb40d">Claude-authored paper claims VP≠VNP over every… · AGI Hunt</a></li>
<li><a href="https://news.lavx.hu/article/anthropic-publishes-claimed-proof-that-vp-vnp-over-every-field">Anthropic Publishes Claimed Proof That VP ≠ VNP Over Every Field</a></li>
<li><a href="https://fourweekmba.com/ai-claude-written-paper-claims-vp-vnp-with-a-lean-proof/">Claude-Written Paper Claims VP ≠ VNP, With a Lean Proof</a></li>
<li><a href="https://en.wikipedia.org/wiki/Arithmetic_circuit_complexity">Arithmetic circuit complexity - Wikipedia</a></li>
<li><a href="https://hexagonmath.org/2611.00954v1">VP ||#92;neq$ VNP over every field · Hexagon</a></li>

</ul>
</details>

**Tags**: `#formal verification`, `#Lean`, `#complexity theory`, `#AI for mathematics`, `#Anthropic`

---

<a id="item-ai-news-2"></a>
### [Google&\#x27;s AI Mode expands Personal Intelligence to Drive, Wallet and Gemini](https://techcrunch.com/2026/11/23/google-searchs-ai-mode-can-now-tap-into-drive-and-wallet-for-more-personalized-responses/) ⭐️ 7.0/10

Google&\#x27;s AI Mode in Search can now draw on data from Google Drive and Google Wallet to personalize its answers, and the same Personal Intelligence capability is being extended to the standalone Gemini app, TechCrunch reported on November 23. The practical shift is that AI Mode responses can be grounded in a user&\#x27;s own files and saved items rather than only the public web, with the personalization running inside Google&\#x27;s existing ecosystem instead of through a third-party connector. The report did not say which countries or account types get the feature, whether users must opt in, or which Drive file types and Wallet contents can be read.

TechCrunch AI · Nov 23, 19:14

**Verified and unconfirmed:** Verified: TechCrunch reported that Personal Intelligence in AI Mode now reaches Drive and Wallet and is coming to the Gemini app, describing it as Google drawing on user data already inside its ecosystem.
Not yet confirmed: Google&\#x27;s own announcement, the rollout scope \(countries, account types, free versus paid tiers\), whether the data linkage is opt-in or on by default, which file types in Drive are searchable, and any independent test of answer quality or privacy behavior — the report supplies none of these.

**Background:** Personal Intelligence is Google&\#x27;s label for connecting data from apps people already use — Gmail, Photos, YouTube and Search — so Gemini and AI Mode can answer using personal context rather than general knowledge. Google said on November 13 that all Gemini app users in the U.S. could connect Google Wallet for responses informed by their spending habits; the new step carries that Wallet connection, plus Drive, into AI Mode in Search rather than leaving it inside the Gemini app.

**Why it matters:** For people who keep documents in Drive and passes or cards in Wallet, an AI Mode answer can now reflect private material rather than only public web pages, so it is worth checking which Google apps are linked to AI Mode and whether that connection is opt-in before treating a response as purely web-sourced. The report does not state the default setting, so account-level review is the practical step.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/products/gemini-app/google-wallet-gemini-app/">Gemini finance insights with Google Wallet integration</a></li>
<li><a href="https://www.androidauthority.com/personal-intelligence-ai-mode-3738563/">Google expands Personal Intelligence in AI Mode for Search</a></li>

</ul>
</details>

**Tags**: `#Google AI Mode`, `#Gemini app`, `#personalization`, `#Google Drive`, `#Google Wallet`

---

<a id="item-ai-news-3"></a>
### [ByteDance&\#x27;s Doubao phone push hits app-ecosystem limits, GeekPark argues](http://www.geekpark.net/news/374374) ⭐️ 7.0/10

GeekPark argues that ByteDance&\#x27;s Doubao phone strategy has hit an ecosystem wall: Doubao can book a Caocao ride, but it cannot tap send on a WeChat message because WeChat, Taobao and Meituan are among more than 150 apps on Doubao&\#x27;s October 14 list that bar the assistant from operating their pages. The only Doubao phones on sale come from ZTE&\#x27;s Nubia—the M153 engineering sample last December at 3,499 yuan and the NaviX Ultra in September at 5,999 yuan—and GeekPark says about 200,000 units are planned for 2026, against 57.9 million smartphones shipped in China in the third quarter, according to IDC. ByteDance has approached Xiaomi, OPPO, vivo, Honor, Lenovo and Transsion about replacing their own assistants with Doubao, but those manufacturers have kept the system-assistant slot; a deal with another major phone maker is rumored to land in November, while ZTE on November 3 denied a reported plan to put its phone business into a joint venture. The piece uses an unconfirmed supply-chain report that Foxconn&\#x27;s FIH has an OpenAI phone assembly order for late 2027 or 2028 to argue that AI companies increasingly want control of both operating system and hardware, but ByteDance has not announced a phone of its own, and GeekPark notes its earlier hardware retreats from Smartisan&\#x27;s phone team and Pico.

GeekPark \(极客公园\) · Nov 23, 15:47

**Verified and unconfirmed:** Verified: GeekPark reports that Doubao&\#x27;s phone assistant published a list on October 14 of more than 150 apps — WeChat, Taobao and Meituan among them — that do not allow it to act on their pages, and that both Doubao phones so far come from ZTE&\#x27;s Nubia: the M153 engineering sample \(December, ¥3,499\) and the NaviX Ultra \(September, from ¥5,999\). Separately, the November 19 Cailian Press \(财联社\) supply-chain report that Foxconn unit FIH Mobile won an OpenAI phone assembly order, with launch around late 2027 or 2028, was picked up by Android Authority and Gizmochina.

Not yet confirmed: OpenAI has not confirmed it is building a phone, and its reported specs — a MediaTek Dimensity 9600 with dual AI processors, per TF International analyst Ming-Chi Kuo — rest on analyst and supply-chain claims. No party has confirmed any ByteDance acquisition of, or stake in, ZTE&\#x27;s phone business; ZTE publicly denied a joint-venture version of that plan on November 3, the reported deal with another major phone maker said to close in November is unattributed, and the ~200,000-unit 2026 stocking figure plus ZTE&\#x27;s evaluation of rival models come from unnamed sources.

**Background:** ByteDance&\#x27;s phone effort began in December 2025 with the Nubia M153, a 3,499-yuan engineering sample sold in small quantities, and reached ordinary buyers in September 2026 with the Nubia NaviX Ultra from 5,999 yuan — both built by ZTE&\#x27;s Nubia. On the first model, the Doubao phone assistant gained a system-level Android permission called INJECT\_EVENTS, which lets it tap and swipe on screen like a finger; such an assistant cannot be downloaded from an app store and must be tightly bound to the handset, occupying the slot phone makers normally reserve for their own assistants such as Xiaomi&\#x27;s Xiao Ai or Honor&\#x27;s YOYO.

**Why it matters:** For users, Doubao&\#x27;s automation stops at the boundary of apps that have integrated with it: Caocao is reachable, but sending a WeChat message after the ride still requires the user. For ByteDance, GeekPark argues that device volume, not model quality, is the gating factor—at roughly 200,000 units planned for 2026, it lacks the leverage to bring WeChat or Taobao to the table.

**What to watch:** Watch for the rumored tie-up between ByteDance and a second major phone maker, which the report says is due to be formally announced within November — and whether it covers only a single co-branded model or the system assistant itself. ZTE has already denied \(November 3\) a plan to bundle its handset business into a joint venture with an unnamed internet company and local state capital, so any confirmation or denial from ZTE or ByteDance would settle the separate speculation about a Nubia acquisition, while reports of more Doubao-branded Nubia models remain unconfirmed.

<details><summary>References</summary>
<ul>
<li><a href="https://www.gate.com/news/detail/FIH-MOBILE/fih-mobile-receives-openai-phone-assembly-order-for-2027-2028-launch-25725255">FIH Mobile Receives OpenAI Phone Assembly Order for 2027-2028 ...</a></li>
<li><a href="https://www.androidauthority.com/openai-phone-foxconn-assembly-3737193/">OpenAI reportedly picks Foxconn to assemble its first phone</a></li>
<li><a href="https://www.gizmochina.com/2026/11/19/openai-phone-fih-mobile-foxconn-assembly-order/">OpenAI phone assembly order goes to Foxconn’s FIH Mobile ...</a></li>
<li><a href="https://app.myzaker.com/news/article.php?pk=6a58b9f58e9f096cb42f8d75">还是太心急了! 字 节 跳动将和 中 兴 通讯推出AI...</a></li>

</ul>
</details>

**Tags**: `#AI assistants`, `#AI phones`, `#ByteDance`, `#Doubao`, `#mobile ecosystem`

---

## EVs &amp; Energy

<a id="item-ev-energy-1"></a>
### [Jordan to seek private investors for 200 MW solar and 400 MWh battery storage](https://www.pv-magazine.com/2026/11/23/jordan-plans-200-mw-solar-100-mw-400-mwh-storage-projects/) ⭐️ 7.0/10

Jordan&\#x27;s Ministry of Energy and Mineral Resources said at the inaugural Jordan-EU Investment Conference last week that it will invite private investors early next year to build a 200 MW solar plant and a 100 MW/400 MWh battery energy storage system \(BESS\). Both would run on a build-own-operate model, with state-owned National Electric Power Company buying the solar output and acting as beneficiary of the storage project. The ministry puts the solar plant at roughly $100 million to $130 million of investment, with an initial prequalification request expected in February 2027, and the BESS at $70 million to $90 million, with prequalification expected in March 2027. Project locations have not been announced, and the two projects sit inside a wider package that also includes a 100 MW wind project, a 450 MW pumped-storage hydropower plant, shared infrastructure for green hydrogen and green ammonia, and natural gas projects.

pv magazine · Nov 23, 10:36

**Verified and unconfirmed:** Verified: pv magazine, citing the ministry&\#x27;s conference announcement, reports the 200 MW solar and 100 MW/400 MWh BESS plans, the build-own-operate structure with NEPCO as offtaker and storage beneficiary, the $100–130 million and $70–90 million investment ranges, and the February and March 2027 prequalification dates.
Not yet confirmed: The cost ranges are planning estimates rather than bid or contract prices; locations, tariffs, financing terms and the storage technology supplier are all undisclosed, and no project has been financed or built.

**Background:** The projects use a build-own-operate model in which the state-owned National Electric Power Company buys the solar plant&\#x27;s output and acts as beneficiary of the battery system, following a pattern Jordan has used to bring in private power producers. Growth in the country&\#x27;s solar fleet has stalled: IRENA put Jordan&\#x27;s cumulative solar capacity at 2,195 MW at the end of 2025, the same figure it reported a year earlier. In September, the energy regulator approved the first 200 renewable energy systems under a revised grid-connection framework that varies the arrangements available by customer category and consumption profile.

**Why it matters:** For developers and financiers, the concrete near-term step is prequalification: interested investors need to be ready to respond to a solar request in February 2027 and a storage request a month later, in a procurement where the offtaker is state-owned NEPCO rather than a private buyer. For scale, IRENA figures cited by pv magazine put Jordan&\#x27;s cumulative solar capacity at 2,195 MW at the end of 2025 — the same as a year earlier — so the proposed 200 MW plant would be a meaningful addition to a fleet that did not grow last year, while the 400 MWh battery would be one of the country&\#x27;s larger storage assets.

**What to watch:** Watch for the ministry&\#x27;s prequalification requests for the solar project in February 2027 and the BESS in March 2027, and for the project locations and final investment terms, which have not been disclosed.

**Tags**: `#Jordan`, `#solar`, `#battery storage`, `#BESS`, `#renewable energy`

---

<a id="item-ev-energy-2"></a>
### [Saudi Arabia raises self-consumption cap to 50 MW and allows battery storage](https://www.pv-magazine.com/2026/11/23/saudi-arabia-expands-self-consumption-rules-to-50-mw/) ⭐️ 7.0/10

Saudi Arabia&\#x27;s Electricity Regulatory Authority \(SERA\) has replaced the 2 MW ceiling on renewable self-consumption systems with a 50 MW cap, and the updated framework explicitly permits integrated battery storage, pv magazine reports, citing a statement carried by the Saudi Press Agency. The rules cover solar, wind, waste-to-energy and biofuel installations that generate and consume power at the same facility, and split grid-connected systems into four bands: 1–11 kW, above 11 kW to 50 kW, above 50 kW to 2 MW, and above 2 MW to 50 MW. Systems up to 11 kW need no prior approval and pay no connection fee but must be installed by an accredited contractor, while systems above 2 MW require a study permit and a generation license from SERA, with application or connection fees of SAR 16,500 for 2–4 MW and SAR 35,000 above 4 MW. The framework also sets out mandatory net billing: surplus exports earn credits that carry into the next billing cycle, can be applied across multiple accounts belonging to the same consumer, and expire 12 months after accrual.

pv magazine · Nov 23, 09:14

**Verified and unconfirmed:** Verified: SERA&\#x27;s updated self-consumption regulation lifts the maximum covered system capacity from 2 MW to 50 MW, permits integrated battery storage, defines the four capacity bands with their approval requirements and fees, and establishes mandatory net billing, according to the regulation as described by the Saudi Press Agency and reported by pv magazine.
Not yet confirmed: The effective date of the new rules and whether they apply to applications already in process are not stated; the monetary value or rate at which exported kilowatt-hours are credited under net billing is not given; and the capacity thresholds, fees and credit terms rest on the regulator&\#x27;s own announcement with no independent assessment of how they will work in practice.

**Background:** Self-consumption rules cover on-site generation — rooftop and building-scale solar, wind, waste-to-energy or biofuel systems — that is consumed at the same facility where it is produced rather than sold wholesale. Saudi Arabia&\#x27;s Electricity Regulatory Authority first issued such regulations three years ago and maintained a separate framework for small solar systems; the update reported now merges the two into a single set of categories. The framework also sets out mandatory net billing, meaning surplus electricity exported to the grid is credited financially and carried forward against future bills for up to 12 months, rather than being compensated through a fixed feed-in tariff.

**Why it matters:** Commercial and industrial consumers can now plan onsite solar-plus-storage sized to their own load well beyond the old 2 MW limit, but any project above 2 MW must budget for a study permit, a SERA generation license and a fee of SAR 16,500 or SAR 35,000 depending on size, and route the application through an accredited consultant or contractor. Service providers are also required to publish qualified contractors, approved equipment and available network capacity, which developers should check before committing to a site.

**What to watch:** Watch for SERA&\#x27;s electronic connection platform and the service providers&\#x27; promised lists of qualified contractors, approved equipment and available network capacity, which will show how quickly the 50 MW band becomes usable in practice.

**Tags**: `#Saudi Arabia`, `#solar policy`, `#self-consumption`, `#battery storage`, `#distributed energy`

---

## Space

<a id="item-space-1"></a>
### [Myriota raises about $40M in first close of Series C](https://www.techmeme.com/261123/p45#a261123p45) ⭐️ 7.0/10

Australia-based Myriota, which sells low-cost, low-power satellite connectivity for industrial IoT devices, raised roughly $40 million in a first close of its Series C round, the Wall Street Journal&\#x27;s Rhiannon Hoyle reported. The company said the money will go toward hiring staff and scaling its satellite constellation and operations. The report gives no investor names, no valuation, and no total target for the round, so the $40 million is a partial close rather than a completed raise; sensors in the field connect directly to Myriota&\#x27;s satellites rather than to terrestrial networks.

Techmeme · Nov 23, 23:25

**Verified and unconfirmed:** Verified: Myriota announced on 24 November 2026 that it closed the first tranche of its Series C, raising AU$60 million \(about US$40 million\), led by Main Sequence Ventures, Hostplus and the National Reconstruction Fund Corporation, with Funds SA joining as a new investor, according to the company&\#x27;s own announcement; Myriota says the money will scale its satellite constellation and fund hiring and expansion, and Dealroom puts its cumulative funding above AU$160 million \(US$107.5 million\).

Not yet confirmed: The final size of the round — the company says the first close came ahead of schedule and the round has yet to close, so the total remains unknown; SmartCompany reports a &quot;$50 million raise&quot; with AU$25 million from the NRFC, a figure that conflicts with the AU$60 million first close and that no source reconciles; the WSJ framing of Myriota as helping &quot;bridge the gap between AI and the real world&quot; is the outlet&\#x27;s characterization, and the figure of 100 new jobs rests on a single report.

**Background:** Satellite IoT connects sensors in places with no cellular coverage — mines, farms, remote pipelines — by passing small amounts of data through overhead satellites instead of ground towers. Myriota, founded in Adelaide in 2014 by Alex Grant and David Haley, runs a constellation of pico-satellites \(very small satellites\) and sells satellite-only or hybrid satellite-cellular links for industrial devices, per its own site; Tracxn&\#x27;s company profile puts its funding before this round at about $80.3M across six rounds. The new money is a &quot;first close&quot; — an initial tranche of a round that later investors can top up before it is declared final.

<details><summary>References</summary>
<ul>
<li><a href="https://myriota.com/">Secure Satellite IoT Connectivity Solutions | Myriota</a></li>
<li><a href="https://tracxn.com/d/companies/myriota/__qSrFQT4_j7MdsJ4V-lZ_gfNP4Lwe_fWraBEQfxbVxfs">Myriota - 2026 Company Profile, Team, Funding &amp; Competitors - Tracxn</a></li>
<li><a href="https://sky-brokers.com/supplier/myriota/">Myriota</a></li>
<li><a href="https://myriota.com/news/myriota-series-c-announcement/">Myriota raises AU$60M Series C for satellite IoT</a></li>
<li><a href="https://southaustralia.dealroom.co/news/feed/myriota-raises-first-39m-of-series-c-in-100-days-to-scale-satellite-iot">Myriota raises first $39M of Series C in 100 days to scale ...</a></li>
<li><a href="https://www.smartcompany.com.au/startupsmart/national-reconstruction-fund-myriota-capital-raise-50-million/">NRF helps rocket Myriota capital raise to $50 million</a></li>

</ul>
</details>

**Tags**: `#satellite IoT`, `#space technology`, `#funding`, `#Series C`, `#Australia`

---

## Tech Industry &amp; Policy

<a id="item-tech-industry-1"></a>
### [Ladybird releases first alpha of its from-scratch browser engine](https://ladybird.org/posts/alpha/) ⭐️ 7.0/10

The Ladybird project released its first alpha on 23 November 2026, so macOS and Linux users can now install the browser without compiling it themselves. The engine implements its own HTML parsing, CSS, layout, JavaScript and WebAssembly, borrowing external components only for text shaping \(HarfBuzz\), 2D graphics \(Skia\), video \(ffmpeg\) and SQLite, and it runs separate tabs in separate processes. The project warns that some sites will not work and that it makes &quot;no promises about security today&quot;, inviting security researchers to attack it and users to file crash and broken-site reports from inside the browser. One early tester reported that most sites he tried rendered correctly, including ffmpeg compiled to WebAssembly and a Pyodide Python REPL, though Datasette Lite failed on a missing \`navigator.serviceWorker.startMessages\` function.

Hacker News · janvdberg · Nov 23, 16:13 · [Discussion](https://news.ycombinator.com/item?id=50614249)

**Verified and unconfirmed:** Verified: The Ladybird project published its first alpha on 23 November 2026, installable on macOS and Linux without compiling it yourself; the project&\#x27;s own October newsletter reported that it passed Safari Technology Preview on the Web Platform Tests suite on 26 October, after gaining roughly 75,650 passes in five days \(Ladybird\).

Not yet confirmed: That the alpha is usable as a daily browser — the project itself warns that some sites will not work and that it will crash sometimes, and explicitly makes &quot;no promises about security today.&quot; The 7x JetStream 3 WebAssembly speedup and the scale of coding-agent contributions are the project&\#x27;s own figures rather than independent measurements, and the smooth-rendering reports come from a handful of individual commenters and one blogger&\#x27;s testing, not a broad compatibility study.

**Background:** Ladybird began inside SerenityOS, Andreas Kling&\#x27;s from-scratch operating system, where developers wrote their own browser instead of embedding Chromium, Gecko or WebKit; it later became a standalone project with its own HTML parser, CSS engine, layout and JavaScript implementation. Independent engines are scarce — in practice Chromium, WebKit and Gecko — which is why a new engine that renders real websites draws attention. In February 2026 Kling described porting parts of the LibJS JavaScript engine from C++ to 25,000 lines of Rust in two weeks with AI coding agents, and the project has kept using such agents to fill gaps in the web-platform-tests suite; until this alpha, anyone who wanted to try the browser had to compile it themselves.

**Why it matters:** For anyone who wants to test a browser engine that is not Chromium, Gecko or WebKit, this is the first build that requires no toolchain, and the tester&\#x27;s process listing shows tab-level process isolation already in place. The same release notes argue against using it for real accounts: the project says it will crash sometimes and has not been hardened, so testing should stay on throwaway logins and use the built-in broken-site reporter rather than a primary Gmail or GitHub session.

**What to watch:** Watch whether the filed Datasette Lite failure, caused by the missing service-worker \`startMessages\` API, is fixed, and what the project&\#x27;s next monthly &quot;This Month in Ladybird&quot; update reports on web-platform-tests passes and crash volume now that outside users are running the alpha.

**From the comments:** Testers were enthusiastic: one said every site he tried rendered correctly and complained only of slightly jerky scrolling, while another reported that ProxMox&\#x27;s NoVNC remote console felt snappier than in Firefox. Others pushed for more than rendering parity — one commenter wants a non-compliant JavaScript mode that spoofs or randomizes fingerprinting values, plus finer-grained permissions — and another noted that swapping in production-grade libraries such as SQLite and Skia drove much of the improvement.

<details><summary>References</summary>
<ul>
<li><a href="https://ladybird.org/newsletter/2026-10-31/">This Month in Ladybird - October 2026 - Ladybird</a></li>

</ul>
</details>

**Tags**: `#browsers`, `#open source`, `#web standards`, `#software releases`, `#privacy`

---