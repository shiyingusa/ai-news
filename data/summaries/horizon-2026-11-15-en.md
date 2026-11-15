# AI Daily Radar - 2026-11-15

> We screened 119 stories from the past day and kept the 13 worth your time.

---

**AI**
1. [Meituan releases LongCat-2.5, a 1.6T agent model trained without Nvidia GPUs](#item-ai-news-1) ⭐️ 8.0/10
2. [Lovable apps exposed passport data and 200K private messages](#item-ai-news-2) ⭐️ 7.0/10
3. [Amodei calls compute Anthropic&\#x27;s &quot;deepest business dilemma&quot; before IPO](#item-ai-news-3) ⭐️ 7.0/10
4. [Meta FAIR/NYU: vision encoder pretraining optional, vision-only parameters required](#item-ai-news-4) ⭐️ 7.0/10

**Chips &amp; Computing**
1. [WSJ: Nvidia chips reached Chinese firms via SE Asian data centers](#item-chips-compute-1) ⭐️ 8.0/10
2. [NYT: Lutnick pushed to narrow chip curbs tied to ex-firm client in Malaysia](#item-chips-compute-2) ⭐️ 7.0/10
3. [TSMC reportedly plans $500M fund for chip startups and suppliers](#item-chips-compute-3) ⭐️ 7.0/10

**Robots &amp; Self-Driving**
1. [Nidus raises $30M for AI software for defense manufacturing robots](#item-robotics-autonomy-1) ⭐️ 7.0/10

**EVs &amp; Energy**
1. [Dongfeng Nissan opens NX7 PHEV early orders at ~$20,000, claiming ~198 miles EV range](#item-ev-energy-1) ⭐️ 7.0/10
2. [Tesla Model Y RWD range rises 8.5% to 348 miles at $39,990](#item-ev-energy-2) ⭐️ 7.0/10

**Space**
1. [SpaceX catches Starship upper stage at launch tower for the first time](#item-space-1) ⭐️ 10.0/10

**Tech Industry &amp; Policy**
1. [FBI, DOJ seize FaceStealer cloud infrastructure tied to North Korean crypto theft](#item-tech-industry-1) ⭐️ 8.0/10
2. [EFF asks appeals court to require warrant for ALPR searches](#item-tech-industry-2) ⭐️ 7.0/10

---

## AI

<a id="item-ai-news-1"></a>
### [Meituan releases LongCat-2.5, a 1.6T agent model trained without Nvidia GPUs](https://the-decoder.com/meituan-releases-a-1-6-trillion-parameter-agent-model-that-never-touched-an-nvidia-gpu/) ⭐️ 8.0/10

Meituan has published the weights of LongCat-2.5, a 1.6-trillion-parameter model built for agent tasks, and says it was trained entirely on Chinese hardware with no Nvidia GPUs involved. Meituan reports a score of 88.4 on Terminal Bench, a benchmark for command-line agent work, placing it just behind Claude Opus 5. The published sample deployment runs on 194 Huawei Ascend chips, according to The Decoder&\#x27;s report, which does not give the exact Opus 5 score, the size or duration of the training run, or the license terms attached to the weights.

The Decoder · Nov 15, 10:06

**Verified and unconfirmed:** Verified: The Decoder reports that Meituan published the weights for LongCat-2.5, a 1.6-trillion-parameter model designed for AI agents, and that Meituan&\#x27;s reported Terminal Bench score is 88.4; the article also states the sample deployment runs on 194 Huawei Ascend chips and that Meituan&\#x27;s materials make no mention of Nvidia GPUs.

Not yet confirmed: The 88.4 Terminal Bench figure and the claim that it lands &quot;just behind Claude Opus 5&quot; come from Meituan&\#x27;s own reporting, with no independent benchmark run or methodology details \(harness version, number of trials, pass criteria\) cited. The assertion that training used only Chinese hardware rests on Meituan&\#x27;s account, which the article does not detail — total chip count, training compute, and whether any non-Chinese accelerators were involved in development are all unstated. The item also omits the model&\#x27;s license terms, context length, and where the weights can be downloaded.

**Background:** Open-weight releases publish a model&\#x27;s weights so developers can download, run, and fine-tune it themselves, unlike closed models available only through an API. Agent models are built for multi-step tasks in which the model calls tools and carries out actions rather than only answering a single prompt. Meituan&\#x27;s release is notable in that context because the source says the model was trained entirely on Chinese hardware and the sample deployment runs on 194 Huawei Ascend chips, with no mention of Nvidia GPUs.

**Why it matters:** For teams building agents, LongCat-2.5 is a frontier-scale open-weight option whose training and reference serving setup depend on Huawei Ascend rather than Nvidia, giving a concrete configuration \(194 chips\) to compare against for anyone evaluating a non-CUDA inference stack. The practical limit is scale: a 1.6-trillion-parameter model still requires a multi-node cluster to serve, so this is a datacenter-scale choice rather than something a small team can run locally, and moving tooling onto Huawei&\#x27;s software ecosystem carries its own porting cost.

**What to watch:** Watch for an independent run of LongCat-2.5 on Terminal Bench or a public leaderboard entry, since the 88.4 figure currently rests on Meituan&\#x27;s own reporting, and for the release of full training-hardware and licensing details.

**Tags**: `#Meituan`, `#LongCat-2.5`, `#agent models`, `#Huawei Ascend`, `#open-weight models`

---

<a id="item-ai-news-2"></a>
### [Lovable apps exposed passport data and 200K private messages](https://www.crissyfield.de/research/lovable-en/) ⭐️ 7.0/10

Security research published at crissyfield.de reports that apps built with Lovable, the AI app builder, exposed passport details and more than 200,000 private messages. In the Hacker News thread, Lovable&\#x27;s head of security attributed the exposures to insufficient Row-Level Security \(RLS\), the Supabase/Postgres rules that decide which rows a signed-in user can read or write when the browser talks directly to the database. Lovable says it scans every app automatically before publishing and offers a free, deeper SAST \(static application security testing\) scan, with a &quot;Fix&quot; option and background auto-fix for findings. The report does not specify how many apps or users were affected, and the post&\#x27;s author said only that the situation is &quot;fairly self-explanatory.&quot;

Hacker News · armcat · Nov 14, 17:43 · [Discussion](https://news.ycombinator.com/item?id=50499017)

**Verified and unconfirmed:** Verified: The researcher who wrote the report \(HN user neathack, publishing with the Crissy Field team\) confirmed authorship in the thread, and the report states that apps built with Lovable exposed passport details and more than 200,000 private messages. Lovable&\#x27;s Head of Security, Igor, responding in the same thread, attributed the exposures to insufficient Row-Level Security in those apps and did not dispute the findings.

Not yet confirmed: The number of affected apps and users, the exposure window and whether all the reported data has been remediated rest on this single research post, whose full text was not supplied. Lovable&\#x27;s claim that its automatic pre-publish scanning and optional auto-fix would catch or resolve such issues is the vendor&\#x27;s own account, and a commenter&\#x27;s assertion that Supabase changed its insecure defaults on October 30 while existing projects keep the old ones is unverified here.

**Background:** Lovable is an AI app builder that generates full-stack web apps, commonly wiring the browser frontend directly to a Supabase \(hosted Postgres\) backend using a public API key. In that architecture there is no application server in the middle to enforce access checks, so Row-Level Security — Postgres policies that restrict which rows each user may read or write — is the only barrier between one visitor&\#x27;s data and everyone else&\#x27;s. Apps assembled by builders unfamiliar with database permissions can therefore go live with missing or overly permissive policies. Commenters also pointed to a long-running Supabase discussion about permissive defaults for existing projects, a claim attributed to community members rather than established here.

**Why it matters:** For teams shipping Lovable apps on Supabase, this is a configuration failure rather than a sophisticated attack: RLS protects nothing until policies are defined for each table, and the affected apps had insufficient policies. Because commenters report that Supabase&\#x27;s newer defaults may not apply to existing projects, the practical action is to audit already-published apps table by table and run the scanner&\#x27;s fixes.

**What to watch:** Watch Supabase&\#x27;s GitHub discussion \#4547 for confirmation that its changed defaults cover existing projects, and Lovable for published results from the pre-publish scanning it says runs on every app.

**From the comments:** Commenters split the blame: yakkomajuri argued that having the frontend talk directly to Supabase with RLS as the only guardrail was always &quot;a minefield,&quot; while SOLAR\_FIELDS pointed to Supabase&\#x27;s years-old decision to ease onboarding at the cost of security and said existing projects may still run the old defaults. Oras noted that AI-generated apps mainly lower the skill needed to find such exposures.

**Tags**: `#AI app builders`, `#vibe coding`, `#security`, `#data exposure`, `#Supabase`

---

<a id="item-ai-news-3"></a>
### [Amodei calls compute Anthropic&\#x27;s &quot;deepest business dilemma&quot; before IPO](https://the-decoder.com/anthropic-ceo-amodei-admits-theres-a-huge-uncertainty-in-whats-going-to-happen-next-year-days-before-a-record-ipo/) ⭐️ 7.0/10

Days before a planned record IPO, Anthropic CEO Dario Amodei described buying compute as the company&\#x27;s &quot;deepest business dilemma,&quot; according to The Decoder. The report says Anthropic&\#x27;s commitments total nearly $901 billion and that the IPO is largely meant to serve as a financial buffer, because it is not clear whether future revenue will justify those costs. It provides no IPO valuation, timetable, revenue forecast, or direct transcript of Amodei&\#x27;s remarks.

The Decoder · Nov 14, 19:05

**Verified and unconfirmed:** Verified: The Decoder reports that Anthropic CEO Dario Amodei called buying compute &quot;the deepest business dilemma&quot; the company faces, days before a planned IPO, and that the offering is intended partly as a financial buffer against uncertainty over whether future revenue will cover those costs. Not yet confirmed: the roughly $901 billion commitments figure in the item conflicts with other coverage of Anthropic&\#x27;s IPO filing, which cites $518 billion in commitments \(tool-1-2, tool-1-3\), while a separate report describes a $100 billion raise at a $1.4 trillion valuation with Goldman projecting over $600 billion in annual revenue by 2030 \(tool-1-1\) — the item itself provides no IPO date, pricing, filing citation or direct transcript, so the commitment total, valuation and revenue projections remain unverified vendor and press claims.

**Background:** Frontier AI companies secure compute through long-term capacity commitments, which become fixed costs well before the revenue from future models is known. Anthropic&\#x27;s planned IPO is intended partly to provide a financial buffer against that mismatch.

**Why it matters:** Prospective IPO investors would have to weigh nearly $901 billion in commitments against revenue the report does not quantify; without IPO terms or a revenue forecast, that gap is the central unresolved risk.

**What to watch:** The next checkable step is Anthropic&\#x27;s public S-1 and the setting of a price range, which would expose the revenue figures investors must weigh against the roughly $901 billion in compute commitments; as of early November reporting, no price range or IPO date had been set. Watch also whether the debut valuation lands near the roughly $2 trillion target floated in market commentary, and whether the final commitment figure is disclosed as $895 billion or $901 billion.

<details><summary>References</summary>
<ul>
<li><a href="https://www.zerohedge.com/markets/anthropic-launches-100-billion-ipo-worth-14-trillion-or-10-trillion-depending-whos-counting">Anthropic Launches $100 Billion IPO Worth $1.4 Trillion... | ZeroHedge</a></li>
<li><a href="https://www.martincid.com/business/anthropic-ipo-dario-amodei-no-hedge-on-earth-compute/">Anthropic IPO Filing Puts CEO Dario Amodei ’s ‘No Hedge on Earth...</a></li>
<li><a href="https://www.thestreet.com/technology/anthropic-ipo-filing-reveals-518-billion-ai-investment-dario-amodei">Anthropic &#x27;s IPO filing reveals a staggering AI bet - TheStreet</a></li>
<li><a href="https://www.axi.com/au/blog/education/stocks/anthropic-ipo">Anthropic IPO : How Australian Investors Can Get Exposure... / Axi AU</a></li>
<li><a href="https://cleus.ai/blog/anthropic-ipo-filing-s1-explained">Anthropic IPO Filing : $17B Revenue, $23B Loss... | Cleus Blog</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#AI business`, `#IPO`, `#compute costs`, `#AI infrastructure`

---

<a id="item-ai-news-4"></a>
### [Meta FAIR/NYU: vision encoder pretraining optional, vision-only parameters required](https://www.reddit.com/r/MachineLearning/comments/1xx1k2o/meta_fair_nyu_unbundling_multimodal_vision/) ⭐️ 7.0/10

A Meta FAIR and NYU team trained more than 200 multimodal LLMs from scratch on identical data to separate three choices that standard vision encoders bundle: separate pretraining, vision-only parameters, and placement before the LLM. In matched-compute comparisons using Qwen3 1.7B and 4B configurations with 0.4B vision parameters, a 0.6B–6.4B scaling ladder, 16 Cambrian VQA benchmarks at 448 px, and 12 language benchmarks, the authors report that separate encoder pretraining is optional: four pretraining objectives \(contrastive, self-supervised, and two captioning variants\) at best tied a from-scratch encoder, and pretraining MetaCLIP 6.5× longer raised ImageNet linear-probe accuracy from 80.4% to 84.4% without improving VQA. Vision-only parameters were required: encoder-free models trailed at every size and needed about 3× the compute to catch up, while giving the LLM the encoder’s parameters improved text but not VQA. Placement before the LLM was also optional: an “in-fusion” design adding zero-initialized vision-only weights to the first eight layers, unused by text tokens, matched the encoder from 1.7B to 6.4B with about 13% lower time to first token; at 1.7B it reached 45.0 VQA versus 44.4 for the encoder, 42.3 when text shared the branches, and 35.1 when vision branches sat in the last eight layers.

Reddit · r/MachineLearning · /u/trungh98 · Nov 15, 17:38

**Verified and unconfirmed:** Verified: The poster, /u/trungh98, discloses that he is one of the study&\#x27;s authors and links a paper \(alphaxiv 2611.17334\), a project blog/FAQ and author X threads; an arXiv cs.CV recent-submissions listing independently shows a paper titled &quot;Unbundling Multimodal Vision Encoding&quot; \(tool-2-1\). The post itself states the experimental design: 200+ MLLMs trained from scratch on identical data with encoder pretraining charged to the same compute budget, main comparisons at Qwen3-1.7B/4B with 0.4B vision parameters, a 0.6B–6.4B scaling ladder, and evaluation on 16 Cambrian VQA benchmarks at 448 px plus 12 language benchmarks. Not yet confirmed: Every quantitative result — pretrained encoders only tying from-scratch ones, encoder-free models needing ~3x compute, 45.0 vs 44.4 VQA for in-fusion vs encoder at 1.7B, ~13% lower time to first token, and the 80.4%→84.4% ImageNet gain from 6.5x longer MetaCLIP pretraining — rests solely on the authors&\#x27; own summary, with no independent replication or peer-review outcome given; the Reddit post is also truncated, so per-benchmark breakdowns and the claimed gaps between Gemma 4 12B, Kimi K3 and Inkling 2 Small cannot be checked from the supplied material.

**Background:** Most multimodal LLMs pair a separately pretrained image encoder—often trained with contrastive image-text objectives—with a language model, so a standard encoder bundles three choices: extra pretraining, parameters reserved for vision tokens, and placement before the LLM. Published models rarely control for data, compute, or encoder pretraining, making architectural differences hard to attribute. Recent models have diverged on this default, with some dropping the encoder and others training it from scratch.

**Why it matters:** For teams designing multimodal LLMs under a fixed compute budget, the practical implication is to allocate parameters to vision-specific capacity rather than to a separately pretrained encoder; the authors’ in-fusion variant matched encoder VQA while cutting time to first token by about 13% in their controlled 1.7B–6.4B tests. The caveat is that these are matched-compute experiments with one data pipeline and benchmark set, not production deployments, so teams should re-check the placement and compute trade-off against their own latency and accuracy targets.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/list/cs.CV/recent">Computer Vision and Pattern Recognition</a></li>

</ul>
</details>

**Tags**: `#multimodal learning`, `#vision encoders`, `#MLLMs`, `#model scaling`, `#AI research`

---

## Chips &amp; Computing

<a id="item-chips-compute-1"></a>
### [WSJ: Nvidia chips reached Chinese firms via SE Asian data centers](https://www.techmeme.com/261115/p1#a261115p1) ⭐️ 8.0/10

The Wall Street Journal reported on November 15 that Nvidia AI chips have been reaching Chinese companies through large Southeast Asian data centers that exploited a gap in U.S. sanctions, with those facilities supplying compute to Chinese firms and providing cover for alleged chip smuggling; the investigation frames the arrangement as a multibillion-dollar business built during Jensen Huang&\#x27;s tenure as CEO. The material available here is a Techmeme headline and one-line summary of the Journal piece: it names no countries, operators, chip models or volumes, and carries no response from Nvidia or the data-center companies. These are allegations by a single news organization, not documented findings or an enforcement action.

Techmeme · Nov 15, 05:55

**Verified and unconfirmed:** Verified: The Wall Street Journal \(reporters Jon Emont, Stu Woo, Patricia Kowsmann and Raffaele Huang\) reports that very large data centers in Southeast Asia exploited a gap in U.S. sanctions, supplying computing power to Chinese companies and providing cover for alleged chip smuggling; separately, the New York Times reports that Washington is investigating Megaspeed, a company that set up Southeast Asian data centers to serve Chinese firms, over allegedly smuggling chips into China, and CNN reports that Jensen Huang resigned on Thursday after admitting to an affair.

Not yet confirmed: Nvidia&\#x27;s own knowledge of or role in the arrangements, any figure behind the &quot;multibillion-dollar business&quot; in the headline, shipment volumes, which specific facilities were involved, and any Nvidia or data-center-operator response — none of that appears in the material supplied, and the smuggling characterization rests on the Journal&\#x27;s &quot;alleged&quot; reporting rather than a proven finding. The U.S. inquiry is also plainly still open: Treasury Secretary Scott Bessent demanded answers within 10 days on whether Nvidia pushed &quot;seemingly illicit&quot; chip sales to China, per Bloomberg.

**Background:** US export controls bar Nvidia&\#x27;s most advanced AI accelerators from going to China without a license, and enforcement turns on where the hardware physically ends up and who ultimately operates it — a question far harder to answer for a data center in a third country than for a shipment with a Chinese consignee. Nvidia has argued that tight restrictions mainly push Chinese buyers toward domestic alternatives, and its CEO had lobbied Washington to loosen the controls, according to CNN&\#x27;s November 14 report. That same report said Jensen Huang resigned on Thursday after admitting to an affair, leaving the company exposed to scrutiny from officials including Treasury Secretary Scott Bessent, who is demanding answers within 10 days on whether Nvidia pushed &quot;seemingly illicit&quot; chip sales to China.

**Why it matters:** Nvidia&\#x27;s exposure now runs through its customers: if the reported route worked by selling hardware to data centers in permitted Southeast Asian jurisdictions and letting Chinese firms use the capacity, the exports may have been lawful at the point of sale and questionable only downstream, which shifts scrutiny onto operators and resellers to document who ultimately runs the workloads. Companies leasing GPU capacity in the region should expect questions about end users that a data center&\#x27;s location alone no longer answers.

**What to watch:** Treasury Secretary Scott Bessent said on November 15 that he wants answers within 10 days — a deadline falling around November 25 — on whether Nvidia pushed &quot;seemingly illicit&quot; chip sales to China. Watch for that response, any Commerce Department action targeting Southeast Asian data-center capacity, and a company statement on the Journal&\#x27;s findings.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tovima.com/wsj/before-his-ouster-jensen-huang-belittled-the-executive-replacing-him/">Before His Ouster, Jensen Huang Belittled the Executive... - tovima.com</a></li>
<li><a href="https://www.nytimes.com/2026/11/15/us/politics/trump-lutnick-ai-chips-cantor-fitzgerald.html">Lutnick Pushed to Weaken Chip Rules That Overlap With His Family...</a></li>
<li><a href="https://edition.cnn.com/2026/11/14/tech/china-megaspeed-nvidia-scandal-hnk-intl">How the Nvidia scandal lifted the curtain on a loophole that’s giving...</a></li>
<li><a href="https://edition.cnn.com/2026/11/14/tech/china-megaspeed-nvidia-scandal-hnk-intl">How the Nvidia scandal lifted the curtain on a loophole that’s giving...</a></li>

</ul>
</details>

**Tags**: `#export controls`, `#Nvidia`, `#AI data centers`, `#chip smuggling`, `#Southeast Asia`

---

<a id="item-chips-compute-2"></a>
### [NYT: Lutnick pushed to narrow chip curbs tied to ex-firm client in Malaysia](https://www.techmeme.com/261115/p9#a261115p9) ⭐️ 7.0/10

A New York Times investigation published Nov. 15 reports that Commerce Secretary Howard Lutnick has pushed to narrow chip export restrictions that would affect data centers in Southeast Asia, some of which are clients of his former firm, Cantor Fitzgerald. According to the article as summarized by Techmeme, one such facility in Malaysia may serve Tencent, the Chinese cloud and social-media company. The account describes Lutnick as personally involved in writing the new rules while the commercial interests at stake overlap with his former firm&\#x27;s business. The available item is a headline and one-line summary of the Times investigation: it does not identify the specific rule provisions being narrowed, the evidence behind the report, whether any change has been adopted, or how Lutnick or Cantor Fitzgerald responded.

Techmeme · Nov 15, 16:10

**Verified and unconfirmed:** Verified: The New York Times published an investigation reporting that Commerce Secretary Howard Lutnick pushed to narrow chip export restrictions that overlap with his family&\#x27;s business interests, and that he has been drafting new rules affecting Southeast Asian data centers, some of which are clients of his former firm, Cantor Fitzgerald. Techmeme summarizes the story as involving a Malaysia data center that may serve Tencent.

Not yet confirmed: The specific rules under consideration, the identity of the client and data center, whether that facility actually serves Tencent, and whether the curbs were ultimately narrowed are drawn from the Times&\#x27; reporting alone and are not independently established here. The supplied item is a headline and one-line summary with no detail on the evidence behind the investigation, the timing or status of any rule change, or any response from Lutnick, the Commerce Department, Cantor Fitzgerald or Tencent.

**Background:** US curbs on advanced chip exports are drafted and administered by the Commerce Department, so the commerce secretary personally shapes which foreign buyers and data-center operators can obtain American AI silicon. Howard Lutnick came to the post from Cantor Fitzgerald, the financial services group whose businesses include investment banking, capital markets and advisory work \(tool-3-3\); according to the Times account, some of the Southeast Asian data-center operators affected by the rules he is writing are clients of that firm. That overlap — a rule-writer whose former employer collects fees from companies the rules would touch — is the conflict the investigation puts at issue.

**Why it matters:** For operators of AI data centers in Malaysia and elsewhere in Southeast Asia, the reported push matters because the export rules under discussion determine whether they can host customers linked to China without losing access to restricted American chips — so siting and tenancy decisions now hinge on rule text that is still being drafted. Companies with capacity in the region should treat their exposure to Chinese-linked tenants as unresolved until the final rule language is published.

**What to watch:** Watch for the Commerce Department to publish the actual text of the revised Southeast Asia data-center rule, and for statements from Lutnick, Cantor Fitzgerald or Tencent responding to the Times report; whether the narrowing survives in the published version is the checkable test of the investigation&\#x27;s claims.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cantor.com/">Home - Cantor</a></li>

</ul>
</details>

**Tags**: `#chip export controls`, `#AI data centers`, `#Malaysia`, `#Tencent`, `#policy influence`

---

<a id="item-chips-compute-3"></a>
### [TSMC reportedly plans $500M fund for chip startups and suppliers](https://www.techmeme.com/261115/p4#a261115p4) ⭐️ 7.0/10

Taiwan Semiconductor Manufacturing Co. plans to create a $500 million venture fund to invest in promising chip startups, suppliers and other upstream partners, Nikkei Asia reported in an interview-based story. The fund is framed by TSMC as a way to back what one quoted executive called &quot;the future&\#x27;s Nvidia&quot; — that is, to hold stakes in the companies that could become the next major chip designer or equipment maker. The report gives no timeline for the fund&\#x27;s launch, no indication of whether it has been formally approved by TSMC&\#x27;s board, and no detail on investment size per company or the fund&\#x27;s structure. The $500 million figure is small next to TSMC&\#x27;s capital spending on fabs, so this reads as an ecosystem and relationship-building vehicle rather than a capacity commitment.

Techmeme · Nov 15, 06:45

**Verified and unconfirmed:** Verified: Nikkei Asia \(Cheng Ting-Fang\) reports, in an interview-based article, that TSMC plans to create a $500 million venture fund to support promising chip startups, suppliers and other upstream partners, and quotes the company saying it &quot;also want\[s\] to support the future&\#x27;s Nvidia.&quot;

Not yet confirmed: TSMC has not been shown to have issued its own announcement of the fund; the $500 million figure, the fund&\#x27;s legal structure, investment targets, timeline and first deals rest on the Nikkei report alone, and the available excerpt is truncated, so the full scope of the quoted remarks is unknown.

**Background:** TSMC is the world&\#x27;s largest contract chipmaker, or foundry: companies such as Nvidia and Apple design chips but outsource fabrication to TSMC&\#x27;s plants. Nvidia&\#x27;s rise as the leading supplier of AI accelerators made it one of TSMC&\#x27;s most important customers, which is the relationship the phrasing about backing &quot;the future&\#x27;s Nvidia&quot; points to — a startup that would design chips and need a foundry to build them.

**Why it matters:** For chip startups and TSMC&\#x27;s upstream suppliers, the fund would add a strategic investor with deep visibility into manufacturing — one that can offer process know-how and priority access to capacity alongside cash, which specialist financial investors cannot. The caveat for anyone hoping to tap it: because the report describes only an intention, with no stated fund size per deal, eligibility criteria or investment mandate beyond &quot;upstream partners,&quot; startups cannot yet plan around it until TSMC confirms the vehicle and its terms.

**What to watch:** Watch for TSMC to formally confirm the fund&\#x27;s existence, size and structure — for example in a board resolution or earnings-call remarks — and for the first named portfolio companies, which would show whether the mandate leans toward design startups or toward equipment and materials suppliers.

**Tags**: `#TSMC`, `#semiconductor supply chain`, `#venture funding`, `#chip startups`, `#foundry`

---

## Robots &amp; Self-Driving

<a id="item-robotics-autonomy-1"></a>
### [Nidus raises $30M for AI software for defense manufacturing robots](https://www.techmeme.com/261115/p5#a261115p5) ⭐️ 7.0/10

Nidus, a startup building AI-powered technology for manufacturing robots used by US defense industrial companies, has raised $30 million across a pre-seed and a seed round, with Kleiner Perkins and Costanoa among its backers. The company says it reached &quot;seven figures&quot; in bookings with defense industrial customers in just four months. The report does not name customers, disclose how much of the $30 million came from each round, or specify whether those bookings are paid orders or softer commitments, and no deployment or performance figures were provided.

Techmeme · Nov 15, 06:50

**Verified and unconfirmed:** Verified: Upstarts Media reports that Nidus raised $30M combined across a pre-seed and a seed round, with Kleiner Perkins and Costanoa among its backers; a Nidus job posting independently describes the company as building AI-and-robotics-based autonomous manufacturing systems.
Not yet confirmed: The &quot;seven figures&quot; in bookings from defense industrial customers within four months is Nidus&\#x27;s own claim, with no customer names, contract values or revenue figures disclosed. The sources also do not say how the $30M splits between the pre-seed and seed, who led either round, or whether the robots are in production deployment rather than pilots.

**Background:** Nidus develops the AI layer for manufacturing robots operated by US defense industrial companies, rather than the robot hardware itself, and its early backers include Kleiner Perkins and Costanoa. The milestone the company cites is bookings — committed customer orders rather than revenue recognized — which it says reached seven figures within four months.

**Why it matters:** Defense industrial manufacturers weighing automation now have a newly funded supplier option, but the only evidence of traction is the company&\#x27;s own bookings figure — with no named customers or shipped-unit numbers — so procurement teams should ask for delivery references rather than accept the funding announcement as proof of deployment.

<details><summary>References</summary>
<ul>
<li><a href="https://robottraining.jobs/jobs/nidus/robot-operator">Robot Operator at Nidus : $30/hr | RobotTraining.jobs</a></li>

</ul>
</details>

**Tags**: `#robotics`, `#manufacturing automation`, `#defense tech`, `#venture funding`, `#AI`

---

## EVs &amp; Energy

<a id="item-ev-energy-1"></a>
### [Dongfeng Nissan opens NX7 PHEV early orders at ~$20,000, claiming ~198 miles EV range](https://electrek.co/2026/11/14/20k-nissan-nx7-phev-goes-on-sale-with-nearly-200-miles-of-electric-range/) ⭐️ 7.0/10

Dongfeng Nissan opened the early order book on its NX7 plug-in hybrid on November 13, promising up to 320 km \(~198 miles\) of all-electric range from a 40 kWh lithium iron phosphate \(LFP\) battery at a price of roughly $20,000. Both figures come from the company as reported by Electrek; the item does not say which trim gets the full 320 km or the $20,000 price, which test cycle the range figure uses, or when deliveries start. A 40 kWh pack is large for a plug-in hybrid — comparable to the batteries in some small battery-electric cars — which is what makes the range claim plausible rather than incremental.

Electrek · Nov 14, 21:26

**Verified and unconfirmed:** Verified: Dongfeng Nissan opened early ordering for the NX7 PHEV, according to Electrek&\#x27;s report of the company&\#x27;s announcement, with a stated 40 kWh LFP battery and a target of up to 320 km of electric range. Not yet confirmed: the ~198-mile range and ~$20,000 price are manufacturer claims with no independent testing, and the sources leave out the test cycle used, the trim breakdown, the price of the long-range version, and the delivery date.

**Background:** A plug-in hybrid \(PHEV\) pairs a battery and electric motor with a gasoline engine, so it can cover daily driving on grid electricity and fall back on fuel for longer trips — which makes battery size the main driver of how much driving is actually electric. LFP \(lithium iron phosphate\) is the cheaper, longer-lasting but less energy-dense battery chemistry, so combining a 40 kWh LFP pack with a roughly $20,000 price is the specific pairing Dongfeng Nissan is claiming. The Electrek report does not specify which test cycle the 320 km figure is measured on, so the &quot;up to&quot; range should be read as a manufacturer claim rather than a measured result.

**Why it matters:** If the claim holds in production form, a 40 kWh battery at this price would let most Chinese buyers cover daily driving on electricity alone while keeping a gas engine for longer trips — a use pattern that depends on reliable home or workplace charging, since the large pack makes the car heavier and slower to charge from a standard outlet than a typical plug-in hybrid.

**What to watch:** Watch for Dongfeng Nissan&\#x27;s full launch pricing and trim sheet, which should clarify whether the ~$20,000 price and 320 km range apply to the same version, followed by the first customer deliveries and independent range tests.

**Tags**: `#Nissan NX7`, `#PHEV`, `#LFP battery`, `#EV range`, `#China auto market`

---

<a id="item-ev-energy-2"></a>
### [Tesla Model Y RWD range rises 8.5% to 348 miles at $39,990](https://www.notateslaapp.com/news/5017/tesla-model-y-rwd-gets-increased-range-at-same-price) ⭐️ 7.0/10

Tesla has raised the EPA-estimated range of the Model Y Rear-Wheel Drive in the U.S. by 8.5%, from roughly 321 miles to 348 miles, while keeping the starting price at $39,990. The change is a specification update to an existing trim rather than a new model or platform. The figures come from Not a Tesla App, a Tesla-focused outlet, which reports the updated rating without citing a Tesla statement or EPA filing directly; the underlying documents would be Tesla&\#x27;s own online configurator and the EPA&\#x27;s published range data.

Not a Tesla App · Nov 14, 22:06

**Verified and unconfirmed:** Verified: Not a Tesla App reports that Tesla raised the Model Y RWD&\#x27;s EPA-estimated range by 8.5% to 348 miles in the U.S. while keeping the $39,990 starting price unchanged.
Not yet confirmed: The figures rest on this single Tesla-focused outlet&\#x27;s report; the item supplies no Tesla configurator listing, EPA filing or Tesla statement, and does not specify the model year affected, whether the gain comes from a hardware, software or testing change, or whether other Model Y trims received similar updates.

**Background:** The Model Y RWD is the entry-level, rear-wheel-drive version of Tesla&\#x27;s mid-size SUV. Its EPA-estimated range is the U.S. window-sticker figure calculated under standardized test procedures, so it is meant for vehicle-to-vehicle comparison rather than as a guarantee of real-world driving distance.

**Why it matters:** For U.S. buyers, the cheapest Model Y now carries about 27 more miles of EPA-estimated range for the same $39,990, which narrows the gap between the entry trim and pricier long-range versions without adding cost. Buyers should treat the 348 miles as a standardized EPA test figure rather than a guaranteed real-world highway result, and should confirm the number on Tesla&\#x27;s configurator at the point of order.

**What to watch:** Watch for Tesla&\#x27;s configurator and the EPA&\#x27;s published fuel-economy data to confirm the 348-mile rating, and for whether other Model Y trims receive similar range updates at unchanged prices.

**Tags**: `#Tesla`, `#Model Y`, `#EV range`, `#pricing`, `#EPA range`

---

## Space

<a id="item-space-1"></a>
### [SpaceX catches Starship upper stage at launch tower for the first time](https://www.teslarati.com/spacex-catches-starship-first/) ⭐️ 10.0/10

SpaceX&\#x27;s launch tower at Starbase, Texas caught the Starship upper stage Ship 42 with its chopstick arms on Saturday, the first time any orbital rocket&\#x27;s upper stage has returned to its launch site and been caught. The ship had spent roughly 22.5 hours in orbit on Flight 15, completing about 14 orbits and deploying all 26 of its Starlink V3 satellites; three of those satellites carried cameras whose imagery of the heat shield SpaceX judged good enough to skip a backup splashdown option. The flight began with a setback: Super Heavy aborted its own catch during the coast phase over a guidance, navigation and control fault, hovered over the Gulf of Mexico and was destroyed in the water. Elon Musk attributed the booster loss to slightly underperforming engines that left too little propellant for the return, and said the fix is greater engine consistency with Raptor V3.2 plus a software change to shut the engines down about one second earlier.

Teslarati · Nov 14, 21:40

**Verified and unconfirmed:** Verified: SpaceX&\#x27;s own broadcast and posts, corroborated by Teslarati, Ars Technica and The Verge, establish that Ship 42 was caught by the tower arms after Flight 15, following roughly 22.5 hours in orbit and deployment of 26 Starlink V3 satellites, and that the Super Heavy booster was lost in the Gulf of Mexico after aborting its catch. Unconfirmed: the heat shield&\#x27;s condition rests on SpaceX&\#x27;s own camera imagery and its decision to forgo the splashdown option, not on independent inspection; Musk&\#x27;s explanation for the booster loss \(engine underperformance and a propellant shortfall\) is his account alone, and the Raptor V3.2 and software fixes have not yet flown; no refurbishment cost or turnaround time for the recovered ship has been disclosed.

**Background:** SpaceX had already caught its Super Heavy booster with the launch tower three times, most recently in March 2025, but every previous Starship upper stage ended in the ocean or was lost. Falcon 9 routinely lands its boosters yet discards its upper stage on every launch, so recovering an orbital upper stage is a separate and harder problem.

**Why it matters:** Recovering the ship is the piece that makes the rest of SpaceX&\#x27;s plans depend on reflight rather than on landings alone: Starlink V3 deployment at scale, the proposed Starmind orbital compute constellation and NASA&\#x27;s Artemis lunar lander all assume ships that can be refurbished and flown again quickly, with Artemis additionally requiring orbital refueling by repeated tanker flights. The next test of that assumption is whether a recovered ship flies again, since a catch that still requires heavy refurbishment would not deliver the cadence economics.

**What to watch:** Whether SpaceX reflies a recovered ship rather than a new one, and whether the next flight attempts to catch both the booster and the ship. Musk has said he expects Starship to reach a weekly launch cadence in the first half of 2027.

**Community discussion:** Hacker News commenters treated the catch as the first reusable orbital upper stage since the Space Shuttle, with Zigurd cautioning that the Shuttle&\#x27;s upper stage was technically successful but required expensive refurbishment and capped launch cadence — the constraint this program now has to beat. Others focused on the near-term test: small\_model argued the next steps are a double catch and re-flying the same ships, while ChuckMcM suggested the booster might have been recovered with a couple more tonnes of propellant and said the eventual mass fraction to orbit remains unclear.

**Tags**: `#SpaceX`, `#Starship`, `#reusable launch`, `#orbital catch`, `#Starbase`

---

## Tech Industry &amp; Policy

<a id="item-tech-industry-1"></a>
### [FBI, DOJ seize FaceStealer cloud infrastructure tied to North Korean crypto theft](https://www.tomshardware.com/tech-industry/cyber-security/fbi-disrupts-north-korean-facestealer-campaign-behind-usd5-billion-binance-hack-doj-seizes-facestealer-cloud-infrastructure-containing-900-videos-of-tech-workers-hackers-used-ai-deepfakes-to-steal-usd400-million-and-compromise-open-source-software) ⭐️ 8.0/10

The FBI and the Justice Department said they disrupted a North Korean social-engineering campaign they named FaceStealer, seizing cloud infrastructure that contained 900 videos of targeted victims. According to the FBI, the operation used AI deepfakes, stolen contact lists and personal data, and fake Zoom or Teams meetings to get victims to install malware, then harvested browser sessions and build-system \(CI/CD\) credentials. The FBI attributes about $400 million in stolen cryptocurrency to the campaign; Tom&\#x27;s Hardware ties it to the Binance heist and describes that hack as taking over $5 billion, most of it frozen or recovered, without reconciling that figure with the FBI&\#x27;s campaign total. The FBI also says the group repeatedly tried to compromise open-source software, mainly JavaScript/npm modules and Rust crates.

Tom&\#x27;s Hardware · Nov 15, 16:30

**Verified and unconfirmed:** Verified: The FBI and DOJ publicly attributed the FaceStealer campaign to North Korea and announced the seizure of cloud infrastructure holding 900 videos of targeted victims, per the DOJ press release and the FBI&\#x27;s IC3 advisory \(dated 12 November 2026\) that the article cites; the FBI states roughly $400 million in stolen cryptocurrency is tied to the campaign, and describes attackers luring victims to typo-squatted meeting domains and prompting malware-laden &quot;updates.&quot; Not yet confirmed: The headline&\#x27;s $5 billion Binance figure conflicts with the body, which says &quot;over $5 billion&quot; was taken with &quot;most&quot; frozen or recovered, and with the FBI&\#x27;s $400 million total for the campaign — the sources do not reconcile the two numbers or specify how much was actually recovered; the article attributes the 18-month campaign duration only to reporting, and its link between FaceStealer and the March 2026 Axios/NPM compromise is its own inference \(&quot;almost certainly&quot;\), since the FBI does not name that package.

**Background:** FaceStealer describes a social-engineering method rather than a piece of malware: attackers first take over a person&\#x27;s messaging and video accounts, harvest their contacts, chat history and recorded video, then reuse that material to impersonate colleagues and recruiters convincingly enough to get a real target onto a fake Zoom or Teams call. Two earlier incidents fit that pattern. Tom&\#x27;s Hardware had reported that the Binance intrusion began with fake job interviews and a malicious Homebrew download, and in March 2026 the widely used Axios npm package briefly shipped a remote-access tool after its developer was approached by someone posing as a hiring company — a case the article says matches the FBI&\#x27;s description, though the FBI report does not name Axios.

**Why it matters:** The concrete risk lands on developers and crypto teams: the article says the Axios npm compromise began with a developer being approached through a fake job offer, and the FBI says FaceStealer uses such meetings to steal browser sessions and CI/CD credentials. Unsolicited interview invitations that end in a meeting-client &quot;update&quot; should be treated as a supply-chain risk, especially for maintainers of widely used packages.

**Tags**: `#North Korea cybercrime`, `#cryptocurrency theft`, `#FBI/DOJ`, `#deepfake social engineering`, `#supply chain security`

---

<a id="item-tech-industry-2"></a>
### [EFF asks appeals court to require warrant for ALPR searches](https://www.eff.org/deeplinks/2026/11/were-asking-appeals-court-require-warrant-alpr-searches) ⭐️ 7.0/10

EFF has filed a brief asking an appeals court to hold that searching a networked license-plate reader \(ALPR\) system is a Fourth Amendment search, which would require a warrant. EFF argues that the “vast, interconnected network” of ALPR cameras continuously tracks drivers around the country. The filing is advocacy, not a court ruling, and no court has yet decided whether such searches require a warrant.

Hacker News · nobody9999 · Nov 15, 02:00 · [Discussion](https://news.ycombinator.com/item?id=50503255)

**Verified and unconfirmed:** Verified: EFF says it filed a brief arguing that networked ALPR tracking is a Fourth Amendment search and should require a warrant. Not yet confirmed: whether the court will accept that argument or impose a warrant requirement; the item provides no case name, court, ruling, or decision date.

**Background:** ALPRs are automated cameras that photograph passing license plates and log where and when each plate was seen, creating searchable databases that can reconstruct a driver’s movements. Whether querying that networked data is itself a Fourth Amendment “search”—normally requiring a warrant or a recognized exception—is the question EFF has pressed in court, including before the California Court of Appeal. The issue is live in multiple jurisdictions: North Carolina’s statute permits warrantless plate searches, while courts continue to weigh constitutional limits.

**Why it matters:** A ruling in EFF’s favor would require law enforcement to obtain a warrant before searching historical ALPR data, affecting how agencies query camera networks that record plate sightings over time.

**What to watch:** Watch for the appeals court’s decision on whether to require a warrant for ALPR database searches. The item gives no case name, argument date, or expected ruling date.

**Community discussion:** Commenters broadly supported EFF’s argument, with several saying ALPR systems should retain only plates tied to active warrants. One commenter cited New Hampshire’s law, which bars bulk collection, limits capture to plates, and requires deletion of non-hit images within three minutes.

<details><summary>References</summary>
<ul>
<li><a href="https://deflockilm.org/alpr-cameras-in-the-courts/">ALPR in the Courts - DeFlockILM</a></li>
<li><a href="https://www.pressreleasepoint.com/hearing-thursday-eff-urges-appeals-court-curb-police-access-alpr-databases">Hearing Thursday: EFF Urges Appeals Court to... | PressReleasePoint</a></li>

</ul>
</details>

**Tags**: `#ALPR`, `#surveillance`, `#privacy`, `#Fourth Amendment`, `#EFF`

---

