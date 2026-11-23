---
layout: issue
permalink: /briefing/2026-11-23/
title: "AI News Briefing: November 23, 2026"
date: 2026-11-23
lang: en
---

> We screened 232 stories from the past day and kept the 22 worth your time.

---

**AI**
1. [Zhipu&\#x27;s GLM-5.4 runs 28 layers twice in a 750B &\#x27;Loop Transformer&\#x27;](#item-ai-news-1) ⭐️ 8.0/10
2. [Amazon to buy much of Decart for $7.5B, Bloomberg reports](#item-ai-news-2) ⭐️ 8.0/10
3. [GPT-6.2 Astra produces machine-verifiable Lean proof of Smoktunowicz&\#x27;s gap theorem](#item-ai-news-3) ⭐️ 8.0/10
4. [Oregon and Virginia Sue Musk Companies Over Grok Deepfakes](#item-ai-news-4) ⭐️ 8.0/10
5. [Blog post on 17-million-line Lean artifact sparks LLM proof debate](#item-ai-news-5) ⭐️ 7.0/10
6. [Sierra raises $1.75B Series F at reported $30B valuation](#item-ai-news-6) ⭐️ 7.0/10
7. [Walmart lets Meta&\#x27;s Muse agent buy Black Friday deals via Agent Gateway](#item-ai-news-7) ⭐️ 7.0/10
8. [Musk told SpaceX staff it lags in AI as renting compute pays more, NYT reports](#item-ai-news-8) ⭐️ 7.0/10
9. [METR&\#x27;s updated AI time-horizon plot shows weaker judgment skills](#item-ai-news-9) ⭐️ 7.0/10
10. [OpenAI scientist proposes shared AI development limits, warns of 2027 acceleration](#item-ai-news-10) ⭐️ 7.0/10

**Chips &amp; Computing**
1. [Penguin demos photonic memory appliance with 576GB HBM3E over optical CXL at SC26](#item-chips-compute-1) ⭐️ 7.0/10
2. [AI server makers raise prices up to 45% after contracts are signed, FT reports](#item-chips-compute-2) ⭐️ 7.0/10

**EVs &amp; Energy**
1. [VW plans 300,000 China-built car exports a year by 2030](#item-ev-energy-1) ⭐️ 7.0/10
2. [Dutch court orders BYD to halt EU sales of Ti7 over Defender likeness](#item-ev-energy-2) ⭐️ 7.0/10
3. [EU Council signals shift away from binding EV quotas for corporate fleets](#item-ev-energy-3) ⭐️ 7.0/10
4. [BMW starts iX4 series production in Debrecen, dealers from March 2027](#item-ev-energy-4) ⭐️ 7.0/10
5. [Senate passes permitting overhaul with route for solar developers to sue agencies](#item-ev-energy-5) ⭐️ 7.0/10
6. [New York completes master plan for 5 GW of advanced nuclear](#item-ev-energy-6) ⭐️ 7.0/10

**Space**
1. [Starship&\#x27;s first second-stage catch reframes launch costs, GeekPark reports](#item-space-1) ⭐️ 9.0/10
2. [China details three uncrewed precursor missions before 2030 crewed Moon landing](#item-space-2) ⭐️ 8.0/10

**Tech Industry &amp; Policy**
1. [DOJ seeks forfeiture of $1B+ stolen from Binance, Bloomberg reports](#item-tech-industry-1) ⭐️ 8.0/10
2. [IBM ends U.S. visa sponsorship for some workers, offering overseas relocation, report says](#item-tech-industry-2) ⭐️ 7.0/10

---

## AI

<a id="item-ai-news-1"></a>
### [Zhipu&\#x27;s GLM-5.4 runs 28 layers twice in a 750B &\#x27;Loop Transformer&\#x27;](https://z.ai/blog/glm-5.4) ⭐️ 8.0/10

Z.ai has published the release note for GLM-5.4, a 750-billion-parameter flagship model built on what the company calls its first &quot;Loop Transformer&quot;: 28 of its layers are computed twice per token instead of once. Z.ai says this lets the model match systems with 2 to 3 trillion parameters, but the only benchmark scores released so far come from a smaller 30B test model, not the full flagship. The company is framing GLM-5.4 as the start of &quot;Generalized Coding,&quot; in which code generation also produces videos, games, and CAD models. Access is currently gated: commenters report the model is not on OpenRouter or the standard Z.ai API plan, and requires Z.ai&\#x27;s Coding Plan, whose API keys otherwise behave like regular ones.

Hacker News · foohis · Nov 23, 10:06 · [Discussion](https://news.ycombinator.com/item?id=50609685)

**Verified and unconfirmed:** Verified: Z.ai&\#x27;s release note states that GLM-5.4 is a 750B-parameter model in which 28 layers run twice, that the company positions it as its first Loop Transformer, and that published benchmark scores so far cover only a 30B test model. Not yet confirmed: the claim that the model matches 2–3-trillion-parameter systems rests on Z.ai&\#x27;s own word with no published full-scale benchmarks or independent evaluation, and the Coding Plan–only availability comes from a user report rather than a documented Z.ai statement.

**Background:** Loop transformers address inference&\#x27;s main physical bottleneck: to generate each token, a conventional model must stream every layer&\#x27;s weights from high-bandwidth memory \(HBM\) into the compute chip, run that layer once, then swap in the next — so memory bandwidth, not arithmetic, sets the pace. Reusing the same weights for a second pass through a block of layers amortizes that weight movement and trades spare compute for reduced memory traffic. Z.ai is not first to the idea — The Decoder notes the company is following OpenAI into loop transformer territory — but GLM-5.4 is where it becomes the architecture of Zhipu&\#x27;s 750-billion-parameter flagship rather than an experiment.

**Why it matters:** Developers who want to try GLM-5.4 today have to subscribe to Z.ai&\#x27;s Coding Plan rather than use a standard API key or OpenRouter, which changes how teams would integrate or price it. The architecture itself targets the memory-bandwidth cost of inference: reusing each layer twice means fewer weight transfers per token, a lever that matters most for large models where moving weights on and off the chip dominates cost.

**What to watch:** Watch for benchmark results for the full 750B model rather than the 30B test model, along with independent evaluations, and for GLM-5.4 to appear on the standard Z.ai API or OpenRouter.

**Community discussion:** Hacker News commenters welcomed the technical detail Zhipu published, with one calling it a refreshing contrast to the disclosure typical of Western labs, and another explaining loop transformers as a fix for the memory-bandwidth bottleneck of moving each layer on and off the chip. Simon Willison reported that access required switching to the Coding Plan and that GLM-5.4&\#x27;s generated &quot;pelican&quot; images look very different from GLM-5.2&\#x27;s gradient-and-animation-heavy defaults, while another commenter argued that Chinese models&\#x27; long &quot;marathon thinking&quot; sessions make them slow on simple tasks.

**Tags**: `#model release`, `#loop transformers`, `#Zhipu GLM`, `#LLM architecture`, `#inference efficiency`

---

<a id="item-ai-news-2"></a>
### [Amazon to buy much of Decart for $7.5B, Bloomberg reports](https://techcrunch.com/2026/11/23/amazon-snaps-up-decarts-ai-optimization-tech-for-7-5b-as-it-prepares-to-sell-trainium-chips/) ⭐️ 8.0/10

Amazon has agreed to acquire much of AI startup Decart, including its Decart Optimization Stack software along with its founding team and AI researchers, for roughly $7.5 billion, Bloomberg reported on November 23, citing one unnamed source. The deal has not been publicly confirmed by either company in the reporting, so the price, the precise assets that transfer, and the timing all remain unverified. TechCrunch framed the purchase as part of Amazon&\#x27;s push to strengthen the AI infrastructure underpinning its in-house Trainium chips as it prepares to sell that silicon to outside customers.

TechCrunch AI · Nov 23, 17:14

**Verified and unconfirmed:** Verified: Amazon has agreed to acquire much of the AI startup Decart, including its Decart Optimization Stack along with its founding team and AI researchers, Bloomberg&\#x27;s Matt Day reported, citing a person familiar with the matter; Amazon&\#x27;s own announcement confirmed the agreement but gave no price, according to explainx.ai&\#x27;s account of that post. The deal is described as signed, not closed.

Not yet confirmed: The ~$7.5 billion figure comes only from Bloomberg&\#x27;s unnamed source — Amazon has not disclosed a price, and the same reporting says Amazon is not acquiring Decart&\#x27;s AI models \(Lucy, Oasis and similar\). What exactly is excluded, the deal&\#x27;s closing conditions and timing, and any link to Trainium sales plans are not established by the primary sources.

**背景:** Decart 于 2023 年由 Dean Leitersdorf 和 Moshe Shalev 创立，于 2024 年 10 月公开启动，并完成由 Oren Zeev 领投的 2100 万美元种子轮融资；到 2026 年 5 月，它表示已从包括 NVIDIA、Adobe Ventures、Toyota Ventures、Sequoia 和 Benchmark 在内的投资方处筹集了 3 亿美元 C 轮融资。其公开产品包括世界模型 Lucy、Oasis 以及被收购的 Decart Optimization Stack（DOS）。

**Why it matters:** Decart&\#x27;s Optimization Stack sits between models and chips, and the company says it runs across Nvidia GPUs, Google TPUs and Amazon Trainium — claiming 1,600 tokens per second for agentic inference against an industry average it puts near 200. Buying it would give AWS ownership of the software layer it needs to pitch Trainium on cost per token rather than raw hardware, so teams weighing Trainium against rival accelerators should watch one open compatibility question: whether the stack stays available on Nvidia and Google silicon or becomes AWS-exclusive, which Bloomberg&\#x27;s report does not address.

**What to watch:** Watch for public confirmation from Amazon or Decart, or disclosure in a regulatory filing, which would establish the $7.5 billion figure and the scope of the transferred technology and staff. Any detail on how the Optimization Stack feeds Amazon&\#x27;s Trainium roadmap would show whether the chip-selling rationale holds.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Decart">Decart - Wikipedia</a></li>
<li><a href="https://venturecapitaltracker.com/startup/decart">Decart Funding, Valuation &amp; Investors</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-11-23/amazon-is-said-to-pay-7-5-billion-for-ai-startup-decart-s-tech">Amazon to Acquire Decart AI Tech for $7.5 Billion to Boost ...</a></li>
<li><a href="https://finance.yahoo.com/technology/ai/articles/amazon-agrees-buy-decart-ai-150027613.html?fr=sycsrp_catchall">Amazon agrees to buy Decart AI technology and team in ...</a></li>
<li><a href="https://explainx.ai/blog/amazon-decart-acquisition-7-5-billion-claimed-vs-verified-november-2026">Amazon Buying Decart? $7.5B Deal Status (Nov 2026 ...</a></li>
<li><a href="https://eu.36kr.com/en/p/3934444301335681">From AI Video Generation to Building a Full AI World: Why Decart AI ...</a></li>
<li><a href="https://www.nuaxia.com/post/decart-raises-300m-to-scale-real-time-ai-infrastructure-and-world-models">Decart Raises $300m to Scale Real-Time AI Infrastructure and World...</a></li>
<li><a href="https://thenextweb.com/news/decart-300-million-radical-ventures-world-models">Decart raises $300M to put a real-time world model in front of...</a></li>

</ul>
</details>

**Tags**: `#Amazon`, `#Decart`, `#AI chips`, `#acquisition`, `#Trainium`

---

<a id="item-ai-news-3"></a>
### [GPT-6.2 Astra produces machine-verifiable Lean proof of Smoktunowicz&\#x27;s gap theorem](https://the-decoder.com/gpt-6-2-astra-solved-a-math-theorem-no-other-ai-could-crack-then-invented-its-own-proof-strategy/) ⭐️ 8.0/10

OpenAI&\#x27;s GPT-6.2 Astra independently produced a Lean proof of Smoktunowicz&\#x27;s gap theorem that, according to The Decoder citing the evaluation firm Vals AI, is the first machine-verifiable proof of the result by any AI. Because key foundations were missing from Mathlib — Lean&\#x27;s standard library of formalized mathematics — the model chose its own proof strategy instead of assembling existing lemmas. On Autoform-Hard, a theorem-proving benchmark, Astra now leads the leaderboard with 49 of 56 tasks solved. The report is secondary coverage: it does not say how the model was prompted, whether anyone outside OpenAI and Vals AI has checked the proof, or whether Astra is generally available.

The Decoder · Nov 23, 12:17

**Verified and unconfirmed:** Verified: Vals AI&\#x27;s own write-up states that GPT-6.2 Astra wrote a Lean 4 proof of Smoktunowicz&\#x27;s gap theorem for graded domains in 94 minutes, about 1,800 lines, taking a route that differs from the published proof — building on a new quantity it called &quot;capacity&quot; and working around three deep results absent from Mathlib; The Decoder also reports Astra leading Autoform-Hard with 49 of 56 tasks solved.

Not yet confirmed: the claim that this is the first computer-checkable proof of the theorem and that no other AI could solve it rests on Vals AI&\#x27;s assessment rather than an independent review, and neither OpenAI nor a third party has publicly confirmed the &quot;self-invented strategy&quot; framing, the leaderboard figures, or how much scaffolding and human guidance the 94-minute run involved.

**Background:** Lean is a proof assistant: it checks a proof step by step, so a proof it accepts is machine-verified rather than judged by human readers, and most such proofs lean on Mathlib, Lean&\#x27;s community library of formalized mathematics. Autoform-Hard, as Vals AI describes it, is a 56-task set of Lean 4 formalization problems drawn from graduate- and research-level textbooks, taken from Meta FAIR&\#x27;s AutoformBench. AI Daily Radar&\#x27;s November 19 digest reported that OpenAI released GPT-6.2 Astra on November 18 with a 1.05 million-token context window and a 20% API price cut; the theorem result is this same model&\#x27;s reported showing on that benchmark.

**Why it matters:** Because a Lean proof is machine-checkable, mathematicians can test the claim by running it through Lean rather than trusting the 49-of-56 benchmark score; the definitions and lemmas Astra built to replace the missing Mathlib foundations are the parts most likely to conceal an error or a nonstandard assumption, so they deserve checking first.

**What to watch:** Whether independent reviewers or the Autoform-Hard maintainers reproduce the Lean proof and the 49-of-56 result, and whether the missing Mathlib foundations are contributed upstream.

<details><summary>References</summary>
<ul>
<li><a href="https://www.vals.ai/blogs/smoktunowicz-gap-theorem">GPT-6.2 Astra Formalizes Smoktunowicz&#x27;s Gap Theorem - vals.ai</a></li>
<li><a href="https://alphasignal.ai/news/openai-s-gpt-6-2-astra-proves-a-math-theorem-no-computer-ever-could">OpenAI&#x27;s GPT-6.2 Astra Proves a Math Theorem No Computer Ever ...</a></li>
<li><a href="https://hermes-ai.net/news/openai-s-gpt-6-2-astra-proves-a-math-theorem-no-computer-ever-could/">OpenAI&#x27;s GPT-6.2 Astra Proves a Math Theorem No Computer Ever ...</a></li>
<li><a href="http://www.geekpark.net/news/374175">2026-11-19 — OpenAI ships GPT-6.2 Astra and Sol with a 20% price cut, and developers push back</a></li>
<li><a href="https://www.vals.ai/">AI Benchmarks for Real-World Tasks | Vals AI</a></li>

</ul>
</details>

**Tags**: `#AI math`, `#theorem proving`, `#Lean`, `#model evaluation`, `#OpenAI`

---

<a id="item-ai-news-4"></a>
### [Oregon and Virginia Sue Musk Companies Over Grok Deepfakes](https://www.wired.com/story/states-sue-spacex-over-grok-deepfakes/) ⭐️ 8.0/10

The attorneys general of Oregon and Virginia have sued several of Elon Musk&\#x27;s companies, alleging that the Grok chatbot was shipped with safeguards too weak to stop it from producing sexualized imagery of real people, including children. Wired reported the filings, which target Musk&\#x27;s companies rather than a single product team. The report does not specify which entities are named as defendants, in which courts the suits were filed, or what relief the states are seeking. The allegations have not been tested in court.

Wired · Nov 23, 11:00

**Verified and unconfirmed:** Verified: Wired reports that the Oregon and Virginia attorneys general filed lawsuits against several of Musk&\#x27;s companies alleging inadequate Grok safeguards against sexualized deepfake imagery of real people, including children. Not yet confirmed: the specific corporate defendants, the courts and case numbers, the exact legal claims and remedies sought, whether any identified minors are involved, and any response from Musk&\#x27;s companies—the report as summarized does not supply these details.

**Background:** Grok is the chatbot and image generator from Elon Musk&\#x27;s xAI, and &quot;nudification&quot; refers to using such tools to produce sexualized images of real people without their consent. CNBC reported that Oregon and Virginia are the first states to sue over the Grok image generator, and according to Yahoo News the complaints allege SpaceX weakened industry-standard safeguards against nudification in order to set Grok apart from competing products. The suits name several of Musk&\#x27;s companies rather than only the AI developer.

**Why it matters:** For companies running image or chatbot products in the United States, the suits signal that state attorneys general will pursue consumer-protection and child-safety theories directly against AI developers over outputs, not just over marketing claims—so operators should expect state-by-state standards for blocking sexualized depictions of real people, and should preserve logs and moderation records that show what safeguards were actually deployed.

**What to watch:** Watch the public court dockets in Oregon and Virginia for the named defendants and claims, and for any motion seeking an injunction against Grok&\#x27;s image features or a substantive response from Musk&\#x27;s companies.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/11/23/oregon-virginia-spacex-grok-deepfake-lawsuits.html">SpaceX sued by Oregon and Virginia over AI deepfake porn ...</a></li>
<li><a href="https://www.yahoo.com/news/politics/articles/virginia-oregon-sue-musk-ai-120000454.html?fr=sycsrp_catchall">Virginia, Oregon sue Musk’s AI company over sexual deepfakes</a></li>
<li><a href="https://thenextweb.com/news/virginia-oregon-spacex-grok-lawsuit">Virginia and Oregon sue Musk’s SpaceX over Grok’s sexual ...</a></li>

</ul>
</details>

**Tags**: `#Grok`, `#AI deepfakes`, `#AI regulation`, `#child safety`, `#lawsuits`

---

<a id="item-ai-news-5"></a>
### [Blog post on 17-million-line Lean artifact sparks LLM proof debate](https://micjm.com/blog/yes-17m-lines-of-lean-is-a-lot/) ⭐️ 7.0/10

A blog post at micjm.com argues that a 17-million-line Lean proof is unusually large and examines the implications for review and correctness. The post sparked a Hacker News discussion in which commenters debated whether LLM-assisted proofs of that size can be trusted, with some warning that errors could hide in converted sub-proofs or in the sheer volume of code. Commenters also said the artifact had been shrunk to 13 million lines, a claim that was not independently verified in the available material.

Hacker News · seizethecheese · Nov 23, 05:00 · [Discussion](https://news.ycombinator.com/item?id=50607668)

**Verified and unconfirmed:** Verified: A blog post at micjm.com argues that a 17-million-line Lean proof is large enough to raise review concerns, and Hacker News commenters discussed the implications for LLM-assisted proof generation.
Not yet confirmed: That the proof is LLM-generated, that it concerns the Generalized Riemann Hypothesis, and that it has been reduced to 13 million lines all rest on community comments and were not established by the available source material.

**Background:** Lean is a proof assistant in which proofs are written as code and checked by a small trusted kernel, so a formalization can in principle be verified mechanically instead of read line by line — which is why the size of a Lean development matters as a practical review problem. This artifact traces to a November 20, 2026 note by mathematician Levent Alpöge, who said that working with Claude he believed he had found a proof of the Riemann Hypothesis and of the Generalized Riemann Hypothesis for Dirichlet L-functions, and released it as a Lean development of 175,187 files and roughly 17 million lines, with no accompanying paper, according to a University of Waterloo page that collects checks of the proof.

**Community discussion:** Commenters questioned whether LLM-generated proofs of millions of lines can be trusted, with one arguing that a large proof has a larger attack surface and another suggesting an incorrect converted sub-proof could be the failure point rather than a Lean bug. A further commenter noted the artifact had reportedly shrunk from 17 million to 13 million lines, while others worried that no human will ever review code of that size.

<details><summary>References</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=aDl7-MWFLVc">17 Million Lines Claim to Prove Riemann . We Ran Them. - YouTube</a></li>
<li><a href="https://math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/">Alpöge/Claude proof of the Generalized Riemann Hypothesis</a></li>

</ul>
</details>

**Tags**: `#Lean`, `#formal verification`, `#LLM-generated proofs`, `#mathematics`, `#AI code quality`

---

<a id="item-ai-news-6"></a>
### [Sierra raises $1.75B Series F at reported $30B valuation](https://techcrunch.com/2026/11/23/sierra-doubles-valuation-to-30b-within-six-months-as-demand-for-ai-in-cx-takes-off/) ⭐️ 7.0/10

Sierra, the enterprise customer-experience company co-founded by former Salesforce co-CEO Bret Taylor, said on Monday that it raised $1.75 billion in a Series F round. TechCrunch reported that the round doubled Sierra&\#x27;s valuation to $30 billion within roughly six months, a figure attributed to the report rather than confirmed in the company&\#x27;s own statement. The report frames the raise as riding demand for AI in customer experience, but it does not name the participating investors, disclose revenue or customer counts, or specify how the new capital will be allocated. No product or capability launch accompanied the funding announcement.

TechCrunch AI · Nov 23, 14:43

**Verified and unconfirmed:** Verified: Sierra said on Nov. 23 that it raised a $1.75 billion Series F at a $30 billion valuation, led by Greenoaks and Lightspeed Venture Partners, with Benchmark, Sequoia, Greenoaks, GV and Tiger Global all returning, according to the company&\#x27;s own announcement and CMSWire.

Not yet confirmed: That the valuation doubled within six months \(implying a prior round near $15 billion\) rests on TechCrunch&\#x27;s reporting rather than a figure in Sierra&\#x27;s announcement; the sources also give no revenue, customer-count or booking details to support the demand claim.

**Background:** CX, short for customer experience, covers the support, service and sales conversations a company has with its customers — the area where Sierra sells AI software, according to the report. Sierra is co-founded by Bret Taylor, a former co-CEO of Salesforce, the large enterprise software vendor whose products include customer service tools. The $30 billion figure is double the valuation the company carried roughly six months earlier, which is why the round is being described as a rapid re-rating rather than a first-time mark.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/11/23/sierra-doubles-valuation-to-30b-within-six-months-as-demand-for-ai-in-cx-takes-off/">Sierra doubles valuation to $30B within six months as demand ...</a></li>
<li><a href="https://www.cmswire.com/contact-center/sierra-hits-30b-valuation-on-175b-series-f/">Sierra Hits $30 Billion Valuation on $1.75 Billion Series F</a></li>
<li><a href="https://sierra.ai/blog/series-f-30b">Series F (Building the digital front door) | Sierra</a></li>

</ul>
</details>

**Tags**: `#AI funding`, `#enterprise AI`, `#customer experience AI`, `#Sierra`, `#Series F`

---

<a id="item-ai-news-7"></a>
### [Walmart lets Meta&\#x27;s Muse agent buy Black Friday deals via Agent Gateway](https://www.theverge.com/ai-artificial-intelligence/1039874/walmart-agent-gateway-meta-muse-black-friday) ⭐️ 7.0/10

Walmart is rolling out a live implementation of the Agent Gateway it announced last month, and Meta&\#x27;s Muse AI agent is the first shopping agent using it: Muse can search for and purchase Black Friday deals through Walmart&\#x27;s Sparky assistant. Purchases run through Walmart &quot;Agent Profiles,&quot; a dedicated space for agent activity inside a customer&\#x27;s Walmart account where shoppers can set spending limits, approve purchases, and review a history of everything the agent bought. Walmart says the gateway lets agents find relevant products without being given the customer&\#x27;s purchase history. The Verge describes the integration as live and rolling out, without specifying how many customers have access or whether it extends past the Black Friday period.

The Verge AI · Nov 23, 11:00

**Verified and unconfirmed:** Verified: Walmart says it is rolling out a live implementation of its Agent Gateway, that Meta&\#x27;s Muse can find and purchase Black Friday deals via the Sparky assistant, and that Agent Profiles let customers set spending limits, approve purchases and view agent purchase history.
Not yet confirmed: Independent testing of a Muse-initiated purchase, how many customers or which markets have access, whether the integration continues after Black Friday, and whether other AI agents besides Muse are supported on the gateway.

**Background:** Meta introduced Muse in September 2026 as a personal AI agent that acts across apps rather than just answering questions — it was pitched with shopping and browsing capabilities, including comparing prices and placing orders on a user&\#x27;s behalf. Walmart had announced its Agent Gateway the month before this rollout, described as a way for outside AI agents to find relevant products without being handed a shopper&\#x27;s purchase history; Muse is now a live implementation of that gateway, operating through per-agent &quot;Agent Profiles&quot; inside a customer&\#x27;s Walmart account where spending limits and purchase approvals are set.

**Why it matters:** For shoppers, the practical control surface is the Agent Profile: spending limits and per-purchase approval are what stand between an agent and a real charge, so those settings should be configured before Muse is given access. For developers building shopping agents, Agent Gateway is the interface to watch, since Walmart says it supplies product discovery without handing over a customer&\#x27;s purchase history — a privacy constraint other retailers may copy.

**What to watch:** Whether Walmart extends Agent Gateway beyond the Black Friday window and names additional AI agent partners, or reports how many purchases agents actually completed during the sale.

<details><summary>References</summary>
<ul>
<li><a href="https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/">Introducing Muse : The World’s First Personal AI Agent Built for...</a></li>
<li><a href="https://www.engadget.com/2253133/meta-reveals-its-ai-agent-that-can-shop-send-emails-and-plan-trips-on-your-behalf/">Meta Reveals Its AI Agent That Can Shop , Send Emails And Plan...</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#agentic commerce`, `#Meta Muse`, `#Walmart`, `#Black Friday`

---

<a id="item-ai-news-8"></a>
### [Musk told SpaceX staff it lags in AI as renting compute pays more, NYT reports](https://www.techmeme.com/261123/p31#a261123p31) ⭐️ 7.0/10

Elon Musk told SpaceX employees that the company is falling behind in AI and that renting out computing capacity from its data centers to outside customers — including Anthropic — is more lucrative than using that capacity to improve SpaceX&\#x27;s own products, the New York Times reported on November 23, citing unnamed sources. According to the report, the rentals are making it harder for SpaceX&\#x27;s own AI effort, which must compete for the same compute it sells. Neither SpaceX nor Anthropic has publicly confirmed the remarks or the customer relationship, and the report provides no figures for rental revenue, contracted capacity, or which other buyers are involved.

Techmeme · Nov 23, 17:35

**Verified and unconfirmed:** Verified: The New York Times reported on November 23, citing unnamed sources, that Elon Musk told SpaceX employees the company is falling behind in AI and that renting data-center computing to competitors, including Anthropic, is more lucrative than using it to improve SpaceX&\#x27;s own products; Quartz and Fortune have likewise reported that SpaceX leases compute capacity to AI companies.

Not yet confirmed: SpaceX has not publicly confirmed the internal meeting, Musk&\#x27;s remarks, or which companies are customers — the Times account rests entirely on people it does not name, and no contract terms, capacity figures, or revenue numbers have been disclosed. Quartz&\#x27;s headline names Google as a customer alongside Anthropic, while the Times summary names only Anthropic, so the full customer list remains unconfirmed.

**Background:** Renting out data-center capacity is lucrative because outside AI developers are committing to enormous compute deals: AI Daily Radar&\#x27;s November 17 digest reported that Anthropic — named in the Times report as one of the customers renting SpaceX capacity — was planning a program called Anthropic Direct that would lease 875,000 Google TPUs for $7.2 billion a year through 2045, based on Financial Times reporting on internal documents. SpaceX has meanwhile been expanding its own AI footprint, disclosing in April an option to acquire the code-generation startup Cursor for $60 billion or pay $10 billion for a partnership, The Guardian reported.

**Why it matters:** SpaceX&\#x27;s internal AI teams would be bidding for capacity against paying outside customers, so internal projects can be deprioritized whenever an external contract pays more — a dynamic the report says is already slowing the company&\#x27;s own AI work. For AI labs, it means an additional supplier of data-center capacity outside the major cloud providers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techmeme.com/261117/p11#a261117p11">2026-11-17 — Report: Anthropic&#x27;s &quot;Anthropic Direct&quot; plan commits $900B+ to 2045, leasing 875K TPUs</a></li>
<li><a href="https://www.nytimes.com/2026/11/23/business/elon-musk-ai-anthropic-google.html">Elon Musk Faces an A.I. Dilemma at SpaceX - The New York Times</a></li>
<li><a href="https://qz.com/spacex-leases-computing-power-anthropic-google-ai-112326">SpaceX leases computing power to Anthropic, Google amid AI push</a></li>
<li><a href="https://fortune.com/2026/07/19/spacex-ai-compute-renting-business-google-anthropic-pentagon-deals-revenue-valuation-elon-musk-colossus-data-centers/">SpaceX is quietly building an AI compute business that may ...</a></li>
<li><a href="https://www.theguardian.com/technology/2026/apr/21/spacex-cursor-ai-startup">SpaceX secures option to buy AI startup Cursor for... | The Guardian</a></li>

</ul>
</details>

**Tags**: `#SpaceX`, `#AI compute`, `#data centers`, `#Elon Musk`, `#AI infrastructure`

---

<a id="item-ai-news-9"></a>
### [METR&\#x27;s updated AI time-horizon plot shows weaker judgment skills](https://www.technologyreview.com/2026/11/23/1149548/the-download-ai-judgment-problem-carbon-removal-crop-threat/) ⭐️ 7.0/10

METR, the AI evaluation nonprofit, has published a new version of its widely shared &quot;time horizon&quot; plot, which measures how long a task a model can complete, and reports that some capabilities are still improving exponentially while models perform worse on tasks requiring judgment than on coding. The update adds more open-ended tasks, including designing AI evaluations and scoring philosophical arguments, and the models struggled with them. MIT Technology Review&\#x27;s The Download newsletter, which summarizes the report, frames that gap as potentially crucial to automating research and development. The newsletter does not link directly to METR&\#x27;s report, so the specific task counts, scores and doubling times behind the update are not given in the account available here.

MIT Technology Review · Nov 23, 13:10

**Verified and unconfirmed:** Verified: MIT Technology Review&\#x27;s newsletter reports that METR&\#x27;s new report updates its time-horizon plot with additional open-ended tasks, such as designing AI evaluations and scoring philosophical arguments, and that models performed poorly on them relative to coding. Not yet confirmed: the newsletter does not link to or quote the primary report, so the size of the measured gains, the exact scores on the new judgment-heavy tasks, the task suite&\#x27;s composition and any independent replication of the results are not established here.

**Background:** METR is a nonprofit that runs its own AI evaluations and publishes the results, and its time-horizon metric measures how long a task — in terms of the time a human expert would need — a model can complete reliably. The earlier version of the plot, described in METR&\#x27;s March 19, 2025 paper and its January 29, 2026 &quot;Time Horizon 1.1&quot; release, characterized the frontier trend as task length doubling roughly every seven months, or about 196 days. MIT Technology Review&\#x27;s February 2026 article had already called it the most misunderstood graph in AI; the new edition keeps that framing but broadens the task suite beyond well-specified work to open-ended judgment tasks.

**Why it matters:** Teams that treat time-horizon doubling as a proxy for when models can automate R&amp;D should test on open-ended judgment tasks rather than code-style benchmarks, since METR&\#x27;s update indicates those two capabilities are not advancing at the same rate.

**What to watch:** Look for METR&\#x27;s full report and task-level results, and whether the judgment-task gap narrows in its next time-horizon update.

<details><summary>References</summary>
<ul>
<li><a href="https://metr.org/">METR</a></li>
<li><a href="https://www.baristalabs.io/blog/metr-ai-task-horizons-7-month-doubling-2026">METR &#x27;s Latest Time - Horizon Data Makes AI Capability Planning Much...</a></li>

</ul>
</details>

**Tags**: `#METR`, `#AI evaluation`, `#AI capabilities`, `#time horizon`, `#judgment`

---

<a id="item-ai-news-10"></a>
### [OpenAI scientist proposes shared AI development limits, warns of 2027 acceleration](http://www.geekpark.net/news/374304) ⭐️ 7.0/10

OpenAI chief scientist Jakub Pachocki posted a proposal on November 22 for AI companies to adopt common limits on advanced model development, using a cross-company metric such as perplexity — a next-token prediction score where lower is better — as an initial threshold, and to commit not to cross it until stronger monitoring exists. He disclosed internal figures showing GPT-3.5 at about 0.99 log perplexity and GPT-4 at about 0.91, with new cybersecurity and math capabilities appearing below 0.8 and breakthroughs on some open math problems around 0.76; he expects 0.68–0.7 could bring more transformative but unspecified abilities. Pachocki warned that pretraining could advance rapidly as early as 2027 while alignment and behavior monitoring lag, and proposed shared evaluation, transparency and red-team standards before deployment. OpenAI CEO Sam Altman endorsed the article, but no lab has announced adoption and the proposal sets no binding rules.

GeekPark \(极客公园\) · Nov 23, 01:22

**Verified and unconfirmed:** Verified: OpenAI chief scientist Jakub Pachocki published a post proposing that leading AI labs agree on measurable limits for advanced model development, built around perplexity as a cross-company tracking metric — TechCrunch and ForkLog both reported the post on Nov 22.

Not yet confirmed: The specific internal figures \(log-perplexity of about 0.99 for GPT-3.5 and 0.91 for GPT-4, capability jumps below 0.8, breakthroughs near 0.76, transformative capability at 0.68–0.7\), Sam Altman&\#x27;s endorsement, and the 2027 acceleration warning come only from the post as relayed by GeekPark/CnBeta; no other lab has adopted the proposal or published comparable numbers, which AI Weekly notes leaves the &quot;common limits&quot; idea without a second signatory, and no independent test confirms the thresholds.

**Background:** AI Daily Radar&\#x27;s November 16 digest reported that OpenAI had started a first phase of &quot;embedded assessments,&quot; bringing Apollo Research, METR, Transluce and Goodfire inside to independently evaluate its models&\#x27; alignment, safeguards and monitoring systems; that digest noted OpenAI disclosed no models, timetable or conclusions, and that limits on access raised questions about how independent the reviews could be. Pachocki&\#x27;s proposal would push that kind of pre-deployment evaluation from a single company&\#x27;s internal program toward shared cross-company standards, anchored to a pretraining metric \(perplexity, a measure of how well a model predicts the next text token\) that outside firms could track against one another.

**Why it matters:** For frontier labs, the proposal would turn perplexity-style pretraining metrics into a pre-deployment gate, requiring agreed red-team and monitoring milestones before a model crosses a set threshold. Because it is voluntary and no company has signed on, it does not yet change any release schedule or safety requirement.

**What to watch:** Watch for any AI company formally committing to the proposed common limits or publishing a concrete threshold and evaluation protocol; no adoption or timetable has been announced.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/our-first-phase-of-embedded-assessments">2026-11-16 — OpenAI 启动首批内嵌评估：Apollo、METR 等四家机构参与</a></li>
<li><a href="https://aiweekly.co/alerts/openais-pachocki-urges-frontier-pause-at-068-07-perplexity">OpenAI &#x27;s Pachocki urges frontier pause at... | AI Weekly</a></li>
<li><a href="https://forklog.com/en/openai-chief-scientist-proposes-measurable-limits-on-advanced-ai-development/">OpenAI chief scientist proposes measurable limits on advanced AI ...</a></li>
<li><a href="https://techcrunch.com/2026/11/22/openais-chief-scientist-has-thoughts-on-how-to-limit-ai-development/">OpenAI ’s chief scientist has thoughts on how to limit AI development</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#AI安全`, `#模型评测`, `#预训练`, `#AI治理`

---

## Chips &amp; Computing

<a id="item-chips-compute-1"></a>
### [Penguin demos photonic memory appliance with 576GB HBM3E over optical CXL at SC26](https://www.tomshardware.com/pc-components/dram/penguin-shows-off-photonic-memory-box-at-sc26-that-can-expand-ai-accelerator-capacity-over-optical-links-device-sports-up-to-576gb-of-hbm3e-customer-samples-expected-in-2027) ⭐️ 7.0/10

Penguin Solutions demonstrated a MemoryAI Photonic Appliance at SC26 that adds up to 576 GB of HBM3E and 16 TB of DDR5 to AI systems over optical CXL.mem 3.1 links, targeting the memory-capacity limit of AI accelerators. The box is built from eight of Marvell&\#x27;s Photonic Fabric Memory Modules — each with 72 GB of HBM3E cache and a photonic interposer with 16 transmit and 16 receive channels — for an aggregate bidirectional bandwidth target of 7.2 TB/s, or about 3.6 TB/s in each direction. It supports HBM Direct, HBM-plus-DDR5 cached, and DDR5 Direct modes, and can connect hosts up to 30 meters away. Customer samples are not expected until the second half of 2027, and the appliance delivers full benefit only to hosts that support CXL.mem or integrate Marvell&\#x27;s photonic chiplet, since Nvidia and AMD data-center GPUs generally lack a general-purpose CXL.mem host interface.

Tom&\#x27;s Hardware · Nov 23, 18:00

**Verified and unconfirmed:** Verified: Penguin Solutions showed the MemoryAI Photonic Appliance at SC26 with up to 576 GB of HBM3E plus 16 TB of DDR5, a 7.2 TB/s aggregate bandwidth target, CXL.mem 3.1 over optical links, and customer samples slated for the second half of 2027, according to Tom&\#x27;s Hardware&\#x27;s report from the show.
Not yet confirmed: Actual application performance, the claim of transparent access without application changes, the sub-350ns PF-NIC and sub-200ns chiplet latency figures \(which exclude PCIe/CXL overhead\), pricing, and where Penguin will source HBM3E in volume around 2028 as the industry moves to HBM4.

**Background:** CXL \(Compute Express Link\) is an open interconnect standard that lets a processor address memory residing outside its own package as a coherent extension of its own address space; the CXL.mem protocol is the part of the spec that carries those memory reads and writes. HBM3E is the current generation of high-bandwidth memory — DRAM stacked in layers beside an AI accelerator — and its fixed per-chip capacity is one reason developers add or replace accelerators when a model outgrows it. Penguin&\#x27;s appliance is built on Marvell&\#x27;s Photonic Fabric, in which memory modules carry a photonic interposer and connect to hosts over optical links rather than copper.

**Why it matters:** System designers evaluating the appliance should first confirm host support: Nvidia and AMD data-center GPUs do not generally expose a CXL.mem host interface, so the full-capacity benefit is limited to CXL-capable CPUs, custom XPUs with Marvell&\#x27;s chiplet, or future accelerators. Even on supported hosts, the 7.2 TB/s is shared across as many as eight accelerators, and Penguin&\#x27;s transparent-access claim depends on memory-management software that treats the external pool as another memory tier.

**What to watch:** Customer samples are scheduled for the second half of 2027; watch whether Penguin names host platforms or accelerator partners that support CXL.mem, and whether benchmarks show a gain over simply adding accelerators.

**Tags**: `#photonic memory`, `#HBM3E`, `#CXL`, `#AI accelerators`, `#optical interconnects`

---

<a id="item-chips-compute-2"></a>
### [AI server makers raise prices up to 45% after contracts are signed, FT reports](https://www.tomshardware.com/tech-industry/big-tech/ai-server-makers-hike-prices-up-to-45-percent-months-after-contracts-are-signed-as-ram-shortage-triples-memory-heavy-cpu-node-costs-financial-firms-still-pay-up-as-the-compute-is-valuable) ⭐️ 7.0/10

Trading and financial-services firms buying data-center servers are reportedly being billed up to 45% more than the prices agreed months earlier, with memory-heavy CPU nodes doubling or tripling in cost while GPU servers rose 20–30%, according to the Financial Times. The FT attributes the increases to the DRAM shortage and cites unnamed people describing the gap between the initial quote and the final invoice, one calling a 25, 30 or 45 percent increase &quot;disconcerting.&quot; Those buyers are reportedly absorbing the cost rather than walking away — &quot;we&\#x27;ve never said no,&quot; one person said, because &quot;the compute is valuable to us&quot; — and none of the companies the FT asked would confirm or deny whether their contracts contain clauses against price volatility. The report points to an existing test case: in June, XTX Finland Oy sued a Dell Irish subsidiary after Dell sought $62–70 million on top of an agreed $549 million for 1,680 servers, a dispute that is still ongoing.

Tom&\#x27;s Hardware · Nov 23, 12:30

**Verified and unconfirmed:** Verified: The Financial Times reported that data center server suppliers are seeking price increases of 25%, 30% or as much as 45% on contracts signed months earlier, with GPU servers up 20–30% and memory-heavy CPU nodes doubling or tripling in price; TrendForce and other outlets repeated the figures, crediting the FT. The one documented dispute is on the record: XTX Finland Oy is suing a Dell Irish subsidiary over an added $62–70 million on a previously agreed $549 million order for 1,680 servers, a case The Irish Times reported in June and that is still ongoing.
Not yet confirmed: Every percentage figure rests on unnamed people described by the FT, with no customer, contract, invoice or specific server model and configuration published, and no supplier named in the FT account beyond the Dell litigation; whether buyers hold clauses capping price volatility is unresolved — the FT asked the companies it contacted and none confirmed or denied it.

**Background:** AI servers combine CPUs, GPUs and large amounts of DRAM, the main memory used in servers, and memory-heavy CPU nodes are especially exposed when memory supply tightens; orders are often placed months before delivery, so vendors can face higher component costs before they ship. A June example of the same tension: XTX Finland sued a Dell Irish subsidiary after Dell sought $62 million–$70 million more on a $549 million order for 1,680 servers, and XTX reportedly paid $5 million extra for a clause meant to prevent such increases, the Irish Times reported.

**Why it matters:** The consequence is contractual: XTX reportedly paid $5 million extra for a clause specifically meant to prevent price changes and is still in court, so buyers placing orders months ahead should treat escalation terms and delivery-timing conditions as a cost line, not boilerplate.

**What to watch:** The Irish proceedings brought by XTX Finland Oy against Dell&\#x27;s Irish subsidiary, which the report says remain ongoing; a ruling would indicate whether an agreed server price is enforceable once memory costs spike.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ft.com/content/dd2a6594-6146-4ff1-ac8e-54749c1fc99f?syn-25a6b1a6=1">Tech suppliers raise AI server prices up to 45% months after ...</a></li>
<li><a href="https://www.trendforce.com/news/2026/11/23/news-ai-server-prices-reportedly-rise-up-to-45-as-dell-hpe-and-others-raise-prices-after-deals/">[News] AI Server Prices Reportedly Rise Up to 45% as Dell ...</a></li>
<li><a href="https://www.gate.com/news/detail/DELL/ai-server-makers-raise-prices-up-to-45-post-contract-as-ram-shortage-hits-25811641">AI Server Makers Raise Prices Up to 45% Post-Contract as RAM ...</a></li>

</ul>
</details>

**Tags**: `#AI servers`, `#memory shortage`, `#data center costs`, `#supply chain pricing`

---

## EVs &amp; Energy

<a id="item-ev-energy-1"></a>
### [VW plans 300,000 China-built car exports a year by 2030](https://electrek.co/2026/11/23/if-you-cant-beat-em-vw-to-export-300000-chinese-built-cars-per-year-by-2030/) ⭐️ 7.0/10

Volkswagen intends to export roughly 300,000 vehicles built in China each year by 2030, Electrek reported, framing the move as leaning into Chinese manufacturing rather than fighting the cost advantage of Chinese rivals. The plan sits alongside declining VW sales and annual capacity cuts approaching one million units, as affordable Chinese-brand cars push into Western markets. It is a forward-looking export target, not shipped volume: the report does not name which models, plants or destination markets would account for the 300,000 units, and cites no primary Volkswagen announcement or filing.

Electrek · Nov 23, 12:39

**Verified and unconfirmed:** Verified: Electrek reports that Volkswagen plans to export roughly 300,000 China-built VW vehicles per year by 2030, a strategy the outlet frames against the company&\#x27;s declining sales and annual capacity cuts approaching one million units.

Not yet confirmed: The report does not name the models slated for export, the destination markets, or a start date, and it cites no Volkswagen statement, filing or press release for the 300,000 figure or the capacity-cut number — so both rest on Electrek&\#x27;s account alone. The article as published is a truncated teaser that breaks off before the underlying details, and no independent confirmation or pricing information is available.

**Background:** Volkswagen already builds and sells these cars in China. AI Daily Radar&\#x27;s November 17 digest reported that FAW-Volkswagen, the group&\#x27;s main Chinese joint venture, had opened pre-orders there for the ID. Aura L5, a mid-size electric sedan on its CMP platform quoted at 580 km of CLTC range — a Chinese test cycle that typically returns higher figures than Europe&\#x27;s WLTP or the US EPA standard. A closely related model, the ID. Aura T6 SUV, drew attention when CarNewsChina reported deliveries starting at 129,900 yuan \(about $19,375\), positioning it against the BYD Sealion 06 and Geely EX5. The export target extends that existing low-cost Chinese production base — and the models it already yields — to overseas markets.

**Why it matters:** If the target holds, a meaningful slice of VW&\#x27;s global volume would come from Chinese plants rather than its German and other European factories — the same facilities where the company is cutting capacity by close to a million units a year. Buyers in the receiving markets would get VW-badged cars priced closer to Chinese-brand competitors, while VW&\#x27;s European workforce and suppliers absorb the production shift.

**What to watch:** Watch for Volkswagen to specify which models, Chinese plants and destination markets make up the 300,000-unit target, and for confirmation of the scale of the European capacity cuts in its next production announcements.

<details><summary>References</summary>
<ul>
<li><a href="https://www.electrive.com/2026/11/17/volkswagen-opens-pre-orders-for-id-aura-l5-in-china/">2026-11-17 — Volkswagen opens China pre-orders for ID. Aura L5 electric sedan</a></li>
<li><a href="https://carnewschina.com/2026/10/02/volkswagen-id-aura-t6-began-deliveries-in-china-with-660-km-of-range/">Volkswagen ID . Aura T6 began deliveries in China with 660 km range</a></li>

</ul>
</details>

**Tags**: `#Volkswagen`, `#China`, `#EV manufacturing`, `#exports`, `#automaker strategy`

---

<a id="item-ev-energy-2"></a>
### [Dutch court orders BYD to halt EU sales of Ti7 over Defender likeness](https://www.electrive.com/2026/11/23/court-deems-byd-ti7-too-similar-to-jlr-defender/) ⭐️ 7.0/10

A Dutch court has ordered ten BYD subsidiaries, in interim proceedings, to stop building and selling the Ti7 in the EU, ruling that the model looks too similar to the JLR Defender. The order covers the company&\#x27;s EU operations rather than a single market, meaning the model cannot be produced or sold there while the case continues. The main trial on the design claim is still pending, so the injunction is provisional rather than a final finding of infringement. No court document or filing was published with the report, and the ruling&\#x27;s duration and any appeal by BYD were not stated.

Electrive · Nov 23, 17:30

**Verified and unconfirmed:** Verified: A Dutch court, ruling in interim proceedings, ordered ten BYD subsidiaries to stop building and selling the Ti7 in the EU after finding the model looks too similar to JLR&\#x27;s Defender, electrive reported; the Guardian reported the ban takes effect one week after the ruling and that the court noted BYD &quot;currently has no concrete plans to place the Ti 7 on the market in the EU.&quot; Automotive News likewise reported that the court found the Ti7 infringes the Defender&\#x27;s design.

Not yet confirmed: No court document or judgment was published alongside the reports, so the injunction&\#x27;s precise terms — how long it lasts, whether it covers imports as well as sales, and whether BYD will appeal — are not established, and the main trial on the infringement claim is still pending, meaning the underlying design dispute has not been finally decided.

**Background:** The order came in Dutch interim proceedings \(kort geding\), a fast-track route for urgent relief in which the court rules on a provisional basis while a separate case on the merits continues. The underlying claim is that the Ti7 — sold in China as the Fang Cheng Bao Tai 7 — copies the exterior design of the JLR Defender. The same dispute had already produced a Dutch ruling: as reported on 12 November, a court ordered Jaguar Land Rover to destroy design files it had seized from BYD or face a penalty of $553,850.

**Why it matters:** The immediate consequence is commercial: BYD&\#x27;s EU arm cannot build or deliver the Ti7 until the provisional order is lifted, so customers and dealers with orders for the model face uncertainty about delivery, and BYD&\#x27;s options are to appeal the interim decision, redesign the disputed styling, or wait for the main trial. The case also signals that European courts are willing to use fast interim relief to remove a competitor&\#x27;s vehicle from the market before a full infringement ruling exists.

**What to watch:** Watch whether BYD appeals the interim order and how the Dutch court rules in the main trial, which will decide whether the design claim holds beyond the provisional stage.

<details><summary>References</summary>
<ul>
<li><a href="https://carnewschina.com/2026/11/12/dutch-court-orders-jaguar-land-rover-to-destroy-seized-byd-ti-7-files-or-face-553850-usd-penalty/">Dutch court orders Jaguar Land Rover to destroy seized BYD Ti...</a></li>
<li><a href="https://www.theguardian.com/business/2026/nov/22/court-bans-china-byd-selling-defender-clone-suv-in-eu">Court bans China’s BYD from selling ‘ Defender clone... | The Guardian</a></li>
<li><a href="https://www.theguardian.com/business/2026/nov/22/court-bans-china-byd-selling-defender-clone-suv-in-eu">Court bans China’s BYD from selling ‘ Defender clone’ SUV in EU</a></li>
<li><a href="https://www.autonews.com/jaguar-land-rover/ane-byd-loses-copyright-case-over-jlr-defender-lookalike-1120/">BYD loses copyright case over Defender lookalike - Automotive News</a></li>

</ul>
</details>

**Tags**: `#BYD`, `#JLR Defender`, `#design dispute`, `#EU injunction`, `#EV sales`

---

<a id="item-ev-energy-3"></a>
### [EU Council signals shift away from binding EV quotas for corporate fleets](https://www.electrive.com/2026/11/23/eu-council-signals-shift-away-from-binding-ev-quotas-for-corporate-fleets/) ⭐️ 7.0/10

The EU Council appears to be siding with the European Parliament in favour of turning proposed binding electric-vehicle quotas for corporate fleets into voluntary targets, according to electrive. The European Commission had included a draft passage in its &\#x27;Auto Package&\#x27; that would have required member states to set concrete mandates for ramping up electric company cars from 2030; the Parliament has already downgraded those quotas to voluntary targets, and the Council now seems to be following that approach. Nothing has been adopted: the report describes a Council signal rather than a formal negotiating position, and the final shape of the rules will only emerge from the legislative process.

Electrive · Nov 23, 14:30

**Verified and unconfirmed:** Verified: The European Parliament&\#x27;s press service reports that MEPs backed draft rules covering corporate cars and vans of large businesses \(more than 250 employees and turnover above €50 million\), adopted 89 votes to 29 with four abstentions, that would replace binding quotas with aspirational national targets ranging from 67% to 95% for 2030 and 2035; electrive reported on 27 October that the EVP group had secured a majority against binding quotas.

Not yet confirmed: That the Council has formally endorsed a voluntary approach — the report says only that the Council &quot;seems to be following suit&quot; and cites no Council document or vote, and the final scope, target levels and legal force will not be settled until member states and Parliament conclude negotiations.

**Background:** Company cars were one of the levers the European Commission built into its &quot;Auto Package&quot;: a draft clause would have obliged member states to set concrete mandates for ramping up electric company cars from 2030. The European Parliament has already moved to turn those binding quotas into voluntary targets, making the Council&\#x27;s position the second of the two legislative steps that would precede any final text.

**Why it matters:** Corporate fleets are a major channel for EV uptake, so whether the 2030 obligation on member states is binding or voluntary determines whether fleet operators face a legal requirement or a discretionary national target. Automakers and fleet managers planning 2030 compliance should track the Council&\#x27;s formal position, since a voluntary framework would leave the level of ambition to each member state.

**What to watch:** Watch for the Council to formalise its position on the Auto Package and for the resulting negotiations with the Parliament, which will show whether the voluntary-target approach survives into the final text.

<details><summary>References</summary>
<ul>
<li><a href="https://www.europarl.europa.eu/news/en/press-room/20261103IPR48612/corporate-fleets-accelerating-the-uptake-of-zero-and-low-emission-vehicles">Corporate fleets: accelerating the uptake of zero- and low ...</a></li>
<li><a href="https://www.europarl.europa.eu/pdfs/news/expert/2026/11/press_release/20261103IPR48612/20261103IPR48612_en.pdf">Corporate fleets: accelerating the uptake of zero- and low ...</a></li>
<li><a href="https://www.electrive.com/2026/10/27/evp-secures-majority-against-binding-ev-quotas-for-large-corporate-fleets/">EVP secures majority against binding EV quotas for large ...</a></li>

</ul>
</details>

**Tags**: `#EU policy`, `#EV quotas`, `#corporate fleets`, `#electric vehicles`, `#regulation`

---

<a id="item-ev-energy-4"></a>
### [BMW starts iX4 series production in Debrecen, dealers from March 2027](https://www.electrive.com/2026/11/23/bmw-ix4-rolls-off-production-line-alongside-ix3-in-debrecen/) ⭐️ 7.0/10

BMW has begun series production of the iX4 at its Debrecen plant in Hungary, where the iX3 is already built, making the coupé-styled electric SUV the second Neue Klasse model assembled there. According to electrive, the car will reach dealers from March 2027, initially in two drivetrain variants. The report gives no specifications, battery or range figures, prices, production volumes, or which two variants will be offered first.

Electrive · Nov 23, 11:32

**Verified and unconfirmed:** Verified: BMW has started series production of the iX4 in Debrecen alongside the iX3, and the model is the second Neue Klasse vehicle built at that plant, electrive reported.
Not yet confirmed: technical specifications, range, pricing, production volumes and which two drivetrain variants will launch; the March 2027 dealer date is BMW&\#x27;s stated plan, and no independent confirmation of output or timing exists yet.

**Background:** BMW&\#x27;s Neue Klasse is its new-generation electric vehicle family, and the Debrecen plant already builds the iX3, the first Neue Klasse model assembled there. BMW&\#x27;s newsroom says the plant began iX4 series production less than two months after introducing 24-hour production, making the iX4 the second Neue Klasse model at the site rather than the opening of a new factory.

**Why it matters:** Debrecen now builds two Neue Klasse models on the same line, so buyers who want the iX4&\#x27;s coupé body instead of the iX3&\#x27;s will have to wait for the March 2027 dealer launch and, at least initially, choose from only two drivetrain options.

**What to watch:** Watch for BMW to publish iX4 specifications, prices and the names of the two launch variants ahead of the March 2027 dealer rollout.

<details><summary>References</summary>
<ul>
<li><a href="https://newsroom.bmwgroup.com/global/series-production-of-the-bmw-ix4-gets-underway/">BMW iX4 Series Production Begins</a></li>

</ul>
</details>

**Tags**: `#BMW`, `#Neue Klasse`, `#EV production`, `#electric SUV`, `#Hungary`

---

<a id="item-ev-energy-5"></a>
### [Senate passes permitting overhaul with route for solar developers to sue agencies](https://www.pv-magazine.com/2026/11/23/us-senate-passes-permitting-bill-letting-solar-developers-sue-agencies/) ⭐️ 7.0/10

The US Senate voted 62-33 last week to pass the Bipartisan American Affordability and Jobs Act of 2026 \(BAAJA\), attached as an amendment to H.R. 2347, a House-passed tax bill whose text senators agreed 69-27 on Nov. 18 to replace. The bill would set new deadlines on federal energy permitting and, under Section 1402, let sponsors of 46 listed project types — including solar, onshore wind, storage, nuclear, fossil fuel and transmission — sue agencies over a permit denied in bad faith or delayed more than 60 days past a deadline as part of a pattern of disparate treatment, with damages of 50% to 100% of reasonably expected construction costs. Section 1401 would bar agencies from revoking or materially amending permits in effect on or after Nov. 6, 2026, subject to six exceptions, and cap NEPA challenges at 150 days instead of six years. None of this is law yet: the House must act on the Senate amendment before the current Congress ends in early January.

pv magazine · Nov 23, 08:15

**Verified and unconfirmed:** Verified: The Senate passed BAAJA 62-33 as an amendment to H.R. 2347, after a 69-27 vote on Nov. 18 to substitute the bill&\#x27;s text and a 73-25 procedural vote on Nov. 9, pv magazine reported; the bill was introduced Sept. 30 by Senators Shelley Moore Capito, Mike Lee, Sheldon Whitehouse and Martin Heinrich.

Not yet confirmed: The specific mechanics — the 60-day delay threshold, 50%-100% damages range, the Nov. 6, 2026 permit cut-off date, the 150-day NEPA window, FERC&\#x27;s one-year state backstop and the 18-month behind-the-meter aggregation rule — come from a section-by-section summary by the Bipartisan Policy Center, not from bill text quoted in the report, and could change in the House; SEIA&\#x27;s estimate that the bill unlocks 167 GW of solar by 2035 is the trade group&\#x27;s own modeling, and the report gives no House vote date.

**Background:** US energy projects must clear reviews under the National Environmental Policy Act \(NEPA\), and litigation over those reviews has been a recurring source of multi-year delays for solar and transmission. Developers are already working under Interior Department rules introduced in July 2025 that add elevated review for wind and solar on federal land; in April 2026 a federal judge in Massachusetts preliminarily enjoined that policy as likely arbitrary and capricious. BAAJA is the Senate&\#x27;s answer to that bottleneck.

**Why it matters:** For developers, the bill&\#x27;s practical change is a cause of action rather than a faster queue: a sponsor alleging disparate treatment would need statistical evidence comparing its treatment with the previous 10 years, and could recover 25% to 50% of development and construction costs from the federal Judgment Fund where bad-faith interference is proven. The trade-off is on the other side of the ledger — cutting the window to sue over a NEPA decision from six years to 150 days and limiting courts to remanding rather than voiding permits makes it harder for project opponents to halt construction.

**What to watch:** House action on the Senate amendment before the current Congress ends in early January, when a newly elected Democratic majority takes office; if the bill is not cleared by then, it would have to be reintroduced.

**Tags**: `#permitting reform`, `#US energy policy`, `#solar`, `#transmission`, `#Congress`

---

<a id="item-ev-energy-6"></a>
### [New York completes master plan for 5 GW of advanced nuclear](https://www.world-nuclear-news.org/articles/new-york-unveils-advanced-nuclear-master-plan) ⭐️ 7.0/10

New York Governor Kathy Hochul announced that the state has completed its Master Plan for Responsible Advanced Nuclear Development, a roadmap intended to reach a target of 5 GW of new nuclear generating capacity. The announcement covers the planning document and the capacity goal; it does not describe individual projects. No sites, reactor designs, construction schedules, cost estimates or funding mechanisms were included in the report of the announcement, so the 5 GW figure remains a state target rather than a committed build programme.

World Nuclear News · Nov 23, 15:55

**Verified and unconfirmed:** Verified: World Nuclear News reports that Hochul announced completion of the Master Plan for Responsible Advanced Nuclear Development and that it sets a 5 GW new nuclear capacity target. Not yet confirmed: which reactor technologies or project sites the plan favours, the timeline for construction, the cost, and any siting, permitting or procurement measures — the report gives none of these details.

**Background:** &quot;Advanced nuclear&quot; covers reactor designs beyond today&\#x27;s large light-water plants, including small modular reactors and designs cooled by liquid metal, gas or molten salt. The 5 GW figure is New York&\#x27;s stated capacity target, and the master plan is meant to set out how state agencies and outside stakeholders would reach it; the American Nuclear Society&\#x27;s Newswire dates the plan&\#x27;s introduction by Governor Hochul to November 18. The state has also been funding supporting infrastructure: World Nuclear News reported that the New York Power Authority awarded USD10 million to develop a nuclear workforce across the state.

**Why it matters:** For reactor vendors and utilities eyeing New York, the plan establishes an explicit state capacity goal they can position against, but because no sites, offtake arrangements or incentive mechanisms have been named, it functions as a policy signal rather than a procurement path developers can act on yet.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ans.org/news/">Nuclear Newswire -- ANS</a></li>
<li><a href="https://www.world-nuclear-news.org/articles/moves-to-bolster-us-nuclear-workforce-development">Moves to bolster US nuclear workforce development</a></li>

</ul>
</details>

**Tags**: `#nuclear energy`, `#New York policy`, `#advanced nuclear`, `#clean energy`

---

## Space

<a id="item-space-1"></a>
### [Starship&\#x27;s first second-stage catch reframes launch costs, GeekPark reports](http://www.geekpark.net/news/374355) ⭐️ 9.0/10

SpaceX&\#x27;s Starship returned from an orbital flight and was caught by the launch tower&\#x27;s mechanical arms on November 14 \(US Central time\), which GeekPark describes as the first engineering validation of recovering an orbital-class heavy spacecraft — the first successful case of second-stage recovery. The article argues the significance lies in cost: full reusability at large scale would lower the price of moving mass to and from orbit, and it draws a sharp line between booster recovery \(separation at roughly 2 km/s, a 6–7 minute return\) and ship recovery \(re-entry from about 7.8 km/s, a 30-minute to one-hour return through thermal protection, communications blackout, aerodynamic braking and precision landing\). Alongside that, it profiles Chinese startup Chuanyuezhe \(穿越者\), which says it has completed a full-scale landing-buffer test keeping touchdown shock load under 5g — claiming to be the third commercial company worldwide to do so — and plans a suborbital reusable crewed ship \(CYZ1\), an orbital cargo vehicle \(CYZ2.1, 20 tonnes up and 10 tonnes down to low Earth orbit\) and an orbital crewed version \(CYZ2.2, at least 10 people\), with the stated goal of cutting the China-US gap to within five years. The piece is secondary analysis with vague attributions: it names no SpaceX or independent source for the catch, and its specifics — including the roughly 22.5-hour flight duration and the 2026 Chinese booster recoveries it cites for comparison — are not corroborated within the article.

GeekPark \(极客公园\) · Nov 23, 07:49

**Verified and unconfirmed:** Verified: SpaceX caught Starship&\#x27;s upper stage with the launch tower&\#x27;s arms at Starbase, Texas, on November 14, 2026, after Flight 15 lifted off on November 13 carrying 26 Starlink satellites; the Super Heavy booster was caught as well, the first time both stages of the 124-meter vehicle were recovered \(Ars Technica, Phys.org, and SpaceX&\#x27;s own launch webcast\).

Not yet confirmed: the roughly 22.5-hour orbital duration of the ship&\#x27;s flight and the framing of the catch as the first engineering validation of orbital-class heavy spacecraft recovery rest on GeekPark&\#x27;s account alone. Every figure about the Chinese startup 穿越者 \(Space Transportation Pioneer\) — its January 2023 founding, the under-5g touchdown impact in its full-size landing-buffer test, the claim to be the world&\#x27;s third commercial company to complete such a test, the CYZ1 / CYZ2.1 / CYZ2.2 three-stage plan, and its plan to tender 30 commercial crewed launches — comes from the company itself, with no dates attached to the milestones. The argument that second-stage recovery will bend the space-economy cost curve is the outlet&\#x27;s and its interviewees&\#x27; projection, not an independently measured result.

**Background:** Every previous Starship upper stage either splashed down in the ocean or was lost; AI Daily Radar&\#x27;s November 15 digest reported that the 15th test flight instead brought Ship 42 back to the launch site after about 22.5 hours and 14 orbits, while the Super Heavy booster&\#x27;s own catch was aborted and the booster was destroyed over the Gulf of Mexico. The distinction the GeekPark article draws is between that first-stage return, which is powered and lasts roughly 6-7 minutes from about 2 km/s, and second-stage recovery, which means surviving re-entry from orbital velocity near 7.8 km/s and therefore draws on crewed-spacecraft technology. GeekPark also frames the milestone against the roughly 11-year gap between SpaceX&\#x27;s first booster landing in 2015 and Chinese first-stage recoveries in 2026.

**Why it matters:** For China&\#x27;s commercial space sector, the concrete consequence is that first-stage milestones do not carry over to second-stage recovery: Long March 10B and Zhuque-3 have demonstrated first-stage recovery, but the article reports that 穿越者 is pursuing the separate crewed-spacecraft reentry and landing path and has opened recurrent tenders covering 30 future commercial crewed launches. The near-term action item is therefore to settle ship–rocket interface standards and secure real payload and crew orders, as Chinese reuse work shifts from single recovery tests toward reflight validation and cost-per-delivery metrics.

**What to watch:** Whether SpaceX&\#x27;s next Starship flight repeats the tower catch and publishes recovery data, which would turn a single success into a reusable cadence. On the Chinese side, watch for Chuanyuezhe&\#x27;s CYZ1 suborbital vehicle to reach flight test and for the outcome of its tender for 30 commercial crewed launch contracts; neither has a published date.

<details><summary>References</summary>
<ul>
<li><a href="https://arstechnica.com/space/2026/11/with-starship-catch-spacex-still-shows-it-can-dazzle-the-world/">With Starship catch , SpaceX still shows it can dazzle... - Ars Technica</a></li>
<li><a href="https://phys.org/news/2026-11-spacex-starship-spaceship.html">SpaceX Starship test to attempt first-ever spaceship &#x27; catch &#x27;</a></li>
<li><a href="https://www.youtube.com/watch?v=6egy0KSsK2s">SpaceX Starship Flight 15 | Launch &amp; Ship Catch - YouTube</a></li>
<li><a href="https://www.teslarati.com/spacex-catches-starship-first/">2026-11-15 — SpaceX 首次用发射塔接住从轨道返回的星舰</a></li>
<li><a href="https://news.qq.com/rain/a/20260819A034UC00">朱雀三号实现 一 子 级 着陆支腿方式 回 收 _腾讯新闻</a></li>
<li><a href="https://finance.eastmoney.com/a/202611193934879054.html">朱雀三号有新 进 展 ！ 商业 航 天 复 用 降本将迎关键验证(附股) _ 东方财富网</a></li>
<li><a href="https://tele.ofweek.com/2026-07/ART-8320510-8420-30694176.html">长征十号乙 一 级 回 收 成功，对 中 国 商业 航 天 意味着什么？ - OFweek...</a></li>

</ul>
</details>

**Tags**: `#Starship`, `#二级回收`, `#可重复使用火箭`, `#太空经济`, `#中国商业航天`

---

<a id="item-space-2"></a>
### [China details three uncrewed precursor missions before 2030 crewed Moon landing](https://www.nasaspaceflight.com/2026/11/china-roundup-2026-11/) ⭐️ 8.0/10

China&\#x27;s human spaceflight agency has laid out its most detailed sequence yet for putting astronauts on the Moon before 2030, presented by Wang Xiang, deputy chief designer of the human spaceflight program and chief designer of the newly merged Lunar Exploration Project, at the 7th Manned Space Symposium in Beijing that opened Oct. 31. Three uncrewed missions come first: Mengzhou-1, a single-core Chang Zheng 10A flight sending an unmanned Mengzhou capsule to the Tiangong space station to validate docking and re-entry, now expected in early 2027 after slipping from 2026; then a single triple-core Chang Zheng 10 launching an uncrewed Lanyue lander to demonstrate lunar landing and ascent, likely in 2028; and finally a pair of CZ-10 launches around 2029 rehearsing the full mission robotically, including trans-lunar injection, lunar orbit docking, surface operations and return. Only after those succeed would a crew repeat the profile, with two astronauts descending while a third stays aboard Mengzhou in lunar orbit, and the lander remaining on the surface for three days with potentially daily moonwalks. Unlike Apollo or Artemis, China plans no crewed test flight beyond low Earth orbit and no lunar-orbit-only precursor before its first landing attempt, relying instead on autonomous ascent and lunar orbit docking already flown by the robotic Chang&\#x27;e 5 and Chang&\#x27;e 6 missions.

NASASpaceflight · Nov 22, 22:31

**Verified and unconfirmed:** Verified: CMSA announced the &quot;by 2030&quot; crewed landing goal on May 29, 2023, and this year merged the crewed landing program with the robotic Chang&\#x27;e program into a single Lunar Exploration Project; Wang Xiang presented the three-uncrewed-mission sequence at the symposium that began Oct. 31, and Chang&\#x27;e 5 \(2020\) and Chang&\#x27;e 6 \(2024\) did demonstrate autonomous lunar ascent and lunar orbit docking. Not yet confirmed: the 2028 and 2029 dates for the uncrewed lander test and the full dress rehearsal are expectations rather than firm schedules, and no hardware milestone, launch date or independent assessment of the CZ-10, Mengzhou or Lanyue vehicles is reported; the report also does not state whether the three-day surface stay and daily moonwalks change the roughly six hours on the surface described when the goal was announced in 2023.

**Background:** China first publicly set a crewed lunar landing goal of &quot;by 2030&quot; at the Shenzhou-16 pre-launch press conference in Jiuquan on May 29, 2023, when CMSA spokesperson Lin Xiqiang described two crewmembers spending roughly six hours on the surface while a third waited in orbit. Details of the architecture — the Mengzhou crew spacecraft, the Lanyue lander, a rover and an Apollo-style lunar-orbit rendezvous — followed about six weeks later at a commercial aerospace forum in Wuhan. In May 2026 the China Manned Space Agency merged the crewed landing effort with the robotic Chang&\#x27;e program into a single Lunar Exploration Project, whose chief designer, Wang Xiang, presented the sequencing plan on Oct. 31.

**Why it matters:** Because China is skipping an Apollo 8- or Artemis II-style crewed test flight, the uncrewed dress rehearsal around 2029 carries the entire burden of proving rendezvous, docking and ascent with crew aboard — so any failure or delay in the Mengzhou-1 station flight, already pushed from 2026 to early 2027, compresses the schedule in front of a landing attempt that Chinese officials have linked to 2029.

**What to watch:** The first concrete checkpoint is the Mengzhou-1 launch on the CZ-10A to Tiangong in early 2027, which must validate docking and re-entry before the lunar sequence proceeds.

**Tags**: `#China crewed lunar program`, `#Mengzhou spacecraft`, `#Lanyue lander`, `#Tiangong space station`, `#lunar exploration`

---

## Tech Industry &amp; Policy

<a id="item-tech-industry-1"></a>
### [DOJ seeks forfeiture of $1B+ stolen from Binance, Bloomberg reports](https://www.techmeme.com/261123/p30#a261123p30) ⭐️ 8.0/10

The US Department of Justice is seeking forfeiture of more than $1 billion in cryptocurrency that hackers linked to North Korea stole from Binance Holdings, according to a court filing reported by Bloomberg on Monday. The filing is a legal request, not a final ruling or a confirmed recovery of the funds. The report does not say whether the cryptocurrency has been seized, where it is held, or when a court will act.

Techmeme · Nov 23, 17:25

**Verified and unconfirmed:** Verified: Bloomberg reported Monday that a court filing shows the DOJ seeking forfeiture of more than $1 billion in cryptocurrency stolen from Binance by hackers linked to North Korea.
Not yet confirmed: The filing&\#x27;s exact legal basis, the precise amount, whether the funds have been located or seized, and the court&\#x27;s response are not established in the report; no independent confirmation or ruling was cited.

**Background:** Forfeiture is a legal process in which the government asks a court to transfer ownership of assets it says are proceeds of crime; it is a filing, not a criminal conviction, and the sums named in such complaints are what prosecutors claim rather than money already recovered. The action follows an earlier enforcement push against the same threat: AI Daily Radar&\#x27;s November 15 digest reported that the FBI and Justice Department had disrupted a North Korean social-engineering campaign they named FaceStealer, seizing cloud infrastructure holding 900 victim videos, with the FBI attributing roughly $400 million in stolen cryptocurrency to that operation. Monday&\#x27;s filing targets a larger sum, more than $1 billion, tied specifically to a hack of Binance.

**Why it matters:** For Binance and its users, the filing creates an active US legal claim over more than $1 billion of stolen crypto, but it does not establish that the exchange or its customers will recover any assets. The report also does not say whether DOJ has located or seized the funds.

**What to watch:** Watch the court docket for a ruling on the forfeiture request and for any DOJ statement confirming whether the cryptocurrency has been seized or recovered.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/cyber-security/fbi-disrupts-north-korean-facestealer-campaign-behind-usd5-billion-binance-hack-doj-seizes-facestealer-cloud-infrastructure-containing-900-videos-of-tech-workers-hackers-used-ai-deepfakes-to-steal-usd400-million-and-compromise-open-source-software">2026-11-15 — FBI, DOJ seize FaceStealer cloud infrastructure tied to North Korean crypto theft</a></li>

</ul>
</details>

**Tags**: `#North Korea`, `#cryptocurrency`, `#Binance`, `#DOJ`, `#cybercrime`

---

<a id="item-tech-industry-2"></a>
### [IBM ends U.S. visa sponsorship for some workers, offering overseas relocation, report says](https://restofworld.org/2026/ibm-consulting-ends-us-visa-green-card-sponsorship/?utm_source=rss&amp;utm_medium=rss&amp;utm_campaign=feeds) ⭐️ 7.0/10

IBM has told some of its U.S.-based immigrant employees that it is ending visa and green-card sponsorship, and is offering relocation to another country as an alternative to losing their jobs — an option that can come with a steep pay cut, Rest of World reported. The report, published Nov. 23, says IBM made the decision earlier in the month but does not specify how many employees are affected, which IBM business units or U.S. offices are covered, or how large the pay reductions are. No public statement from IBM on the scope of the change was cited, so the numbers behind it remain unverified.

Rest of World · Nov 23, 11:00

**Verified and unconfirmed:** Verified: IBM is discontinuing U.S. visa and green-card sponsorship for most roles in IBM Consulting, its largest division with more than 150,000 employees, and visa holders in that unit have been told to relocate abroad or leave by year-end, according to multiple outlets \(NationWire, HR Briefing, The Times of India\) citing IBM&\#x27;s own statement.

Not yet confirmed: IBM has not published how many employees are affected, which roles or countries remain eligible for sponsorship, the size of the pay cuts tied to relocation, or whether relocation is guaranteed; the precise effective date and the exact wording of the year-end deadline rest on outlet reporting rather than a public IBM document.

**Background:** H-1B is a temporary U.S. work visa that requires an employer sponsor, and green-card sponsorship is the employer-backed route to permanent residency — so when a company withdraws sponsorship, affected workers must find another sponsor, change status or leave the country. IBM&\#x27;s change covers most roles in IBM Consulting, its largest division, which employs more than 150,000 people globally, according to Indian Opinion. Nationwire reported that the move comes amid a wider Trump administration crackdown on skilled foreign hiring that is reshaping large technology employers.

**Why it matters:** For affected employees, the choice is material: U.S. work authorization is tied to the sponsoring employer, so a worker who loses sponsorship generally has limited time to find a new sponsor or leave the country, and relocated staff are typically paid according to the local market rather than U.S. rates. Employees weighing the offer should establish in writing what their new salary, location and immigration status would be before accepting.

<details><summary>References</summary>
<ul>
<li><a href="https://nationwire.us/ibm-ends-visa-green-card-sponsorship-consulting-roles/">IBM Ends Visa , Green Card Sponsorship for Consulting</a></li>
<li><a href="https://indianopinion.org/ibm-ends-h-1b-sponsorship-for-most-consulting-roles/">IBM ends H-1B, green card sponsorship for most... - Indian Opinion</a></li>
<li><a href="https://nationwire.us/ibm-ends-visa-green-card-sponsorship-consulting-roles/">IBM Ends Visa , Green Card Sponsorship for Consulting</a></li>
<li><a href="https://hrbriefing.com/articles/ibm-ends-visa-sponsorship-for-majority-of-roles-in-its-largest-unit">IBM Ends Visa Sponsorship for Most Consulting Roles — HR Briefing</a></li>
<li><a href="https://timesofindia.indiatimes.com/technology/tech-news/ibm-tells-visa-holders-in-its-150000-people-consulting-unit-to-move-abroad-or-leave-by-year-end-company-says-we-have-opted-to-discontinue-/articleshow/135726102.cms">IBM tells visa and Green card holders in its 150... - The Times of India</a></li>

</ul>
</details>

**Tags**: `#IBM`, `#immigration policy`, `#visa sponsorship`, `#tech labor`, `#offshoring`

---