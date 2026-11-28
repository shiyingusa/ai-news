---
layout: issue
permalink: /briefing/2026-11-28/
title: "AI News Briefing: November 28, 2026"
date: 2026-11-28
lang: en
---

> We screened 233 stories from the past day and kept the 18 worth your time.

---

**AI**
1. [Google&\#x27;s DeepCrossAttention claims up to 3x speedup at comparable quality](#item-ai-news-1) ⭐️ 7.0/10
2. [DeepMind&\#x27;s &quot;Humanity&\#x27;s First Exam&quot; finds top models fail repeated everyday tasks](#item-ai-news-2) ⭐️ 7.0/10
3. [Embo raises $110M seed led by a16z for world-model robot AI](#item-ai-news-3) ⭐️ 7.0/10
4. [Dwarkesh Q&amp;A: Erdil and Kokotajlo on an intelligence explosion before 2029](#item-ai-news-4) ⭐️ 7.0/10

**Chips &amp; Computing**
1. [Lawsuit notes show Commerce pressed Intel to accept 10% stake, Wired reports](#item-chips-compute-1) ⭐️ 8.0/10
2. [MATCH Act&\#x27;s ASML China service ban could backfire, LithoWar analysis argues](#item-chips-compute-2) ⭐️ 7.0/10
3. [SemiAnalysis benchmarks AWS Trainium3, claims best inference cost-per-token after Nvidia Vera Rubin](#item-chips-compute-3) ⭐️ 7.0/10
4. [Kioxia&\#x27;s Gen 3 XL-Flash targets 3 µs reads, samples in March 2027](#item-chips-compute-4) ⭐️ 7.0/10

**EVs &amp; Energy**
1. [EU EV Sales Beat Gas and Diesel Combined in October, InsideEVs Reports](#item-ev-energy-1) ⭐️ 8.0/10
2. [Germany&\#x27;s solar output passes 100 TWh in a year for the first time](#item-ev-energy-2) ⭐️ 8.0/10
3. [BRF Froan: electric bulk carrier with a 23.5 MWh battery](#item-ev-energy-3) ⭐️ 7.0/10
4. [Toyota confirms Highlander 9X as its first EREV, on sale early 2027](#item-ev-energy-4) ⭐️ 7.0/10
5. [Congress passes e-bike battery safety law making voluntary standards mandatory](#item-ev-energy-5) ⭐️ 7.0/10
6. [Arriva wins €2bn North Holland contract with 200+ electric buses](#item-ev-energy-6) ⭐️ 7.0/10
7. [CATL unveils 100 kWh &\#x27;30\#&\#x27; swappable battery for passenger cars](#item-ev-energy-7) ⭐️ 7.0/10

**Space**
1. [Stoke Space&\#x27;s Nova Pathfinder booster arrives at SLC-14 ahead of 2027 debut](#item-space-1) ⭐️ 7.0/10

**Tech Industry &amp; Policy**
1. [SAP confirms GitHub incident; report says stolen tokens allowed source-code changes, SecurityWeek reports](#item-tech-industry-1) ⭐️ 7.0/10
2. [AMD and Winbond firmware flaws speed up BitLocker PIN brute-force attacks](#item-tech-industry-2) ⭐️ 7.0/10

---

## AI

<a id="item-ai-news-1"></a>
### [Google&\#x27;s DeepCrossAttention claims up to 3x speedup at comparable quality](https://research.google/blog/supercharging-transformer-residual-connections/) ⭐️ 7.0/10

Google Research&\#x27;s blog describes DeepCrossAttention \(DCA\), which changes transformer residual connections so each token can attend to embeddings from prior layers—attention across depth rather than only across tokens—and reports comparable model quality with up to 3x faster performance in its experiments. The result targets people building and training transformers, where scaling depth and attention is a central cost. The speedup and quality parity are Google&\#x27;s own lab claims; the supplied material contains no independent benchmark or peer-reviewed paper.

Hacker News · ComputedCamp995 · Nov 27, 23:06 · [Discussion](https://news.ycombinator.com/item?id=50672565)

**Verified and unconfirmed:** Verified: Google Research&\#x27;s blog post and the underlying ICML 2025 paper \(arXiv 2502.06785\) both state that DeepCrossAttention — depth-wise cross-attention over the residual stream — reaches the same model quality up to 3x faster while adding a negligible number of parameters, and improves perplexity for a given training time; the blog also reports that retrofitting DCA onto a pre-trained transformer and briefly continuing training cut LM1B perplexity by 0.19 versus 0.02 for continued standard training.

Not yet confirmed: the &quot;up to 3x&quot; figure is a best-case result from Google&\#x27;s own language-modeling experiments \(LM1B-scale, per the paper\) and has not been independently reproduced or shown to hold at frontier scale; the reported parameter overhead, perplexity gains and speedups are the authors&\#x27; measurements rather than third-party benchmarks, and no released model, code availability or production deployment is confirmed.

**Background:** Transformer layers each pass their output forward through a residual \(skip\) connection, which adds that layer&\#x27;s result to the running representation so very deep networks remain trainable. In a standard transformer those additions carry fixed, equal weight, and the Google Research post notes that simply summing previous layers this way can dilute useful information. DeepCrossAttention keeps the depth-wise routing but makes it learned: each token queries a weighted mix of all earlier layer embeddings rather than receiving a uniform sum, which is the mechanism the reported speedup and quality parity rest on.

**Why it matters:** For teams with existing checkpoints, the more actionable claim is the reported retrofit: a commenter quoting the blog says adding DCA to a pre-trained transformer and briefly continuing training reduced LM1B perplexity by 0.19, versus 0.02 for standard continued training. If that replicates, it suggests a cheaper adaptation path than retraining from scratch, but the evidence is still a single lab experiment.

**What to watch:** Watch for independent replications and any code or implementation release from Google Research that would let teams test DCA on their own models.

**Community discussion:** Commenters focused on the retrofit result—one quoted the LM1B perplexity improvement \(0.19 vs. 0.02\) and said modifying model dimensions mid-training &quot;has a lot of promise&quot;—while another criticized the post&\#x27;s line charts as better suited to bar charts because the methods have no temporal ordering.

<details><summary>References</summary>
<ul>
<li><a href="https://research.google/blog/supercharging-transformer-residual-connections/">Supercharging transformer residual connections</a></li>
<li><a href="https://arxiv.org/html/2502.06785">DeepCrossAttention : Supercharging Transformer Residual ...</a></li>
<li><a href="https://research.google/blog/supercharging-transformer-residual-connections/">Supercharging transformer residual connections - Google Research</a></li>
<li><a href="https://arxiv.org/abs/2502.06785">[2502.06785] DeepCrossAttention: Supercharging Transformer ...</a></li>
<li><a href="https://explainx.ai/blog/google-deepcrossattention-transformer-residual-connections-2026">DeepCrossAttention (DCA): Google Fix for Deep Transformers ...</a></li>

</ul>
</details>

**Tags**: `#transformer architecture`, `#model efficiency`, `#attention mechanisms`, `#Google Research`, `#AI research`

---

<a id="item-ai-news-2"></a>
### [DeepMind&\#x27;s &quot;Humanity&\#x27;s First Exam&quot; finds top models fail repeated everyday tasks](https://the-decoder.com/google-deepminds-humanitys-first-exam-shows-top-ai-models-still-fail-simple-everyday-tasks-under-repeated-runs/) ⭐️ 7.0/10

Google DeepMind tested 18 AI models with a benchmark it calls &quot;Humanity&\#x27;s First Exam,&quot; and the top performers solved nearly every task family at least once — but stumbled when asked for 16 correct answers in a row. Even the strongest entrant, OpenAI&\#x27;s GPT-6.2 Astra, failed to stay consistent across those repeated runs, according to The Decoder&\#x27;s coverage. Visual perception accounted for 73 percent of the errors, and giving models more compute time at inference did not close the gap. The results come from DeepMind&\#x27;s own evaluation rather than an independent third-party test, and the report does not detail the task set or per-model scores.

The Decoder · Nov 28, 11:12

**Verified and unconfirmed:** Verified: Google DeepMind launched Humanity&\#x27;s First Exam, a reliability benchmark that Google&\#x27;s blog says uses 544 prompts; The Decoder reports that it tested 18 models and that even leading systems such as OpenAI&\#x27;s GPT-6.2 Astra stumbled when asked for 16 consecutive correct answers, with visual perception accounting for 73% of errors.

Not yet confirmed: The full per-model scores, the exact 73% error breakdown across all 18 models, and the finding that more compute time does not fix the failures have not been independently replicated; those details rest on The Decoder&\#x27;s account and Google&\#x27;s benchmark description, and the excerpt does not provide the underlying paper or a complete results table.

**Background:** The benchmark&\#x27;s name inverts Humanity&\#x27;s Last Exam, a deliberately brutal test of frontier models; Humanity&\#x27;s First Exam goes the other way, asking straightforward everyday questions that people get right almost every time. Google launched it on Kaggle as a public leaderboard built from 544 short text and image prompts, scoring how consistently a model answers rather than how often it answers correctly on a single try.

**Why it matters:** For teams deploying models on repetitive everyday work, single-run benchmark scores overstate reliability: a model that can do a task once may still fail a string of 16 attempts, which is closer to how production pipelines consume model output. The finding that 73 percent of errors trace to visual perception points builders toward verifying image- and document-reading steps and adding retries or human checks there, rather than assuming extra inference-time compute will fix the failures.

**What to watch:** Watch for DeepMind to publish the full benchmark, its task definitions and per-model pass rates, and for independent groups to rerun it on models outside the original 18.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/google-deepmind/humanitys-first-exam/">Humanity ’ s First Exam : Testing LLM reliability</a></li>
<li><a href="https://www.theneuron.ai/newsletter/deepmind-s-new-ai-exam/">DeepMind &#x27; s new AI exam | The Neuron</a></li>
<li><a href="https://www.kaggle.com/benchmarks/deepmind/hfe">Humanity &#x27; s First Exam (HFE) Leaderboard | Kaggle</a></li>
<li><a href="https://www.theneuron.ai/newsletter/deepmind-s-new-ai-exam/">DeepMind &#x27; s new AI exam | The Neuron</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/google-deepmind/humanitys-first-exam/">Humanity ’ s First Exam : Testing LLM reliability</a></li>

</ul>
</details>

**Tags**: `#AI reliability`, `#benchmark evaluation`, `#Google DeepMind`, `#visual perception`, `#foundation models`

---

<a id="item-ai-news-3"></a>
### [Embo raises $110M seed led by a16z for world-model robot AI](https://the-decoder.com/robotics-startup-embo-raises-110-million-in-seed-funding-to-build-world-model-ai-for-robots/) ⭐️ 7.0/10

Robotics startup Embo emerged from stealth with a $110 million seed round led by Andreessen Horowitz \(a16z\) to build what it describes as a universal robot brain based on world models — AI systems that learn how physical reality behaves rather than only how text is sequenced. According to the company&\#x27;s announcement, its models are trained on large amounts of internet video and practice motor skills in simulation. The team includes researchers from Google DeepMind, Meta and MIT. Embo has not released a product, published benchmark results, named customers, or given a timeline for availability.

The Decoder · Nov 28, 10:48

**Verified and unconfirmed:** Verified: Embo announced its public launch and a $110 million seed round led by a16z, according to the company&\#x27;s own announcement.

Not yet confirmed: The technical claims — that video-trained world models can generalize across robot bodies and acquire fine-grained motor skills in simulation — rest only on Embo&\#x27;s description; no model release, benchmark, demo video, customer deployment, valuation, full investor list or launch date has been disclosed.

**Background:** A world model is an AI system that learns to predict how a physical scene will change over time from observation, rather than mapping sensor inputs directly to actions; Embo says it trains on large amounts of internet video and then practices motor skills in simulation. The company emerged from stealth alongside the announcement, with Andreessen Horowitz leading the $110 million seed round and Khosla Ventures, DST Global and Nvidia&\#x27;s venture arm NVentures participating. Aiparabellum reported that the team is led by former DeepMind researcher Danijar Hafner.

<details><summary>References</summary>
<ul>
<li><a href="https://dealroom.co/news/175093-embo-raises-110m-seed-to-build-robot-brains-with-world-models/">Embo raises $110M seed to build robot brains with world models</a></li>
<li><a href="https://aiparabellum.com/embo-raises-110m-seed-robot-brain-world-models/">Embo Raises $110M Seed to Build a Robot Brain on World Models</a></li>
<li><a href="https://embo.com/introducing-embo">Introducing Embo | Embo</a></li>

</ul>
</details>

**Tags**: `#robotics`, `#world models`, `#embodied AI`, `#funding`, `#startups`

---

<a id="item-ai-news-4"></a>
### [Dwarkesh Q&amp;A: Erdil and Kokotajlo on an intelligence explosion before 2029](https://www.techmeme.com/261127/p13#a261127p13) ⭐️ 7.0/10

Dwarkesh Patel published a podcast Q&amp;A with AI researchers Ege Erdil and Daniel Kokotajlo covering the odds of an intelligence explosion before 2029, the case for pausing AI development, and the risks of the US antagonizing China. The episode is promoted with the line &quot;If we pause now, people still won&\#x27;t understand what&\#x27;s at stake,&quot; which the description does not attribute to either speaker. It is a recorded discussion of forecasts and arguments rather than new research, a model release, or a policy change, and the published description does not include the participants&\#x27; specific probability estimates or predictions. The full episode is out on the Dwarkesh Podcast feed.

Techmeme · Nov 27, 20:15

**Verified and unconfirmed:** Verified: Dwarkesh Patel published a podcast episode featuring AI researchers Ege Erdil and Daniel Kokotajlo, according to the episode page and Techmeme&\#x27;s listing; the page carries the quote &quot;If we pause now, people still won&\#x27;t understand what&\#x27;s at stake,&quot; and Patel writes that the two agreed on more than he expected, with the discussion covering intelligence-explosion timing \(including 2027 versus 2028\), pausing AI, and US tensions with China.

Not yet confirmed: the specific forecasts, odds figures or policy conclusions each guest gave, and whether they converged or disagreed on them — no transcript or independent account of the episode&\#x27;s content is available, and the &quot;before 2029&quot; framing comes from the episode&\#x27;s own description; Erdil has separately been described as holding 2045+ timelines, so how his position is presented in this episode cannot be checked from the listing alone.

**Background:** Daniel Kokotajlo is an author at the AI Futures Project, which published the AI 2027 and AI 2040 scenario reports; an India Today report in November said the project&\#x27;s researchers forecast a superhuman AI researcher emerging between May and November 2027. Ege Erdil, a researcher at Google DeepMind, has argued for much longer timelines — 2045 or later — and has said an intelligence explosion, a rapid self-reinforcing jump in AI capability, is not plausible, which sets up the interview&\#x27;s central disagreement. The pause discussion comes after AI Daily Radar&\#x27;s November 25 digest reported that dozens of insiders at OpenAI and Anthropic believed unreleased frontier models had outgrown safety controls and that both companies were debating whether to pause releases or stop training.

<details><summary>References</summary>
<ul>
<li><a href="https://www.dwarkesh.com/p/daniel-kokotajlo-ege-erdil">AI researchers debate what we should do next – Daniel Kokotajlo ...</a></li>
<li><a href="https://www.youtube.com/watch?v=WLBsUarvWTw">AGI is still 30 years away — Ege Erdil &amp; Tamay Besiroglu - YouTube</a></li>
<li><a href="https://www.indiatoday.in/technology/news/story/intelligence-explosion-now-expected-in-2027-as-anthropic-ai-progress-doubles-3036529-2026-11-11">Intelligence explosion now expected in 2027 as Anthropic AI ...</a></li>
<li><a href="https://www.dwarkesh.com/p/daniel-kokotajlo-ege-erdil">AI researchers debate what we should do next – Daniel Kokotajlo and...</a></li>
<li><a href="https://www.youtube.com/watch?v=WLBsUarvWTw">AGI is still 30 years away — Ege Erdil &amp; Tamay Besiroglu - YouTube</a></li>
<li><a href="https://the-decoder.com/dozens-of-insiders-say-openai-and-anthropics-unreleased-models-have-outgrown-their-safety-measures/">2026-11-25 — Insiders say OpenAI and Anthropic frontier models have outgrown safety controls, Axios reports</a></li>

</ul>
</details>

**Tags**: `#AI timelines`, `#AI safety`, `#AGI`, `#AI geopolitics`, `#AI policy`

---

## Chips &amp; Computing

<a id="item-chips-compute-1"></a>
### [Lawsuit notes show Commerce pressed Intel to accept 10% stake, Wired reports](https://arstechnica.com/tech-policy/2026/11/intel-faced-a-choice-give-trump-10-or-face-the-consequences/) ⭐️ 8.0/10

Internal notes from an August 2025 call, described in a federal lawsuit, record Commerce Department lawyer David Shapiro telling Intel&\#x27;s chief financial officer that the offer of a roughly 10 percent US government equity stake was not up for bargaining: &quot;Do not make the mistake of thinking that this is a negotiation,&quot; he said, adding that the President expected to announce a deal on those terms that Friday. According to a summary of his remarks prepared for Intel&\#x27;s directors, Shapiro acknowledged the board could decline, but noted that rejection &quot;will have consequences that \[he\] cannot predict.&quot; The reporting does not say what those consequences were described to be, what the government paid or what conditions came with the stake, and it offers no measure of the holding&\#x27;s effect on Intel&\#x27;s chipmaking capacity or output.

Ars Technica · Nov 27, 12:05

**Verified and unconfirmed:** Verified: According to Ars Technica&\#x27;s account of WIRED&\#x27;s reporting, internal notes from an August 2025 call — contained in a federal lawsuit — record Commerce Department lawyer David Shapiro telling Intel&\#x27;s CFO not to make the &quot;mistake of thinking that this is a negotiation,&quot; that &quot;the President is expecting to announce a deal on these terms on Friday,&quot; and that rejection &quot;will have consequences that \[Shapiro\] cannot predict&quot;; Intel agreed to give the US government a roughly 10 percent stake \(WIRED, The Daily Beast, Yahoo\).

Not yet confirmed: The underlying lawsuit&\#x27;s allegations have not been adjudicated, the accuracy and completeness of the quoted call notes have not been independently tested, and the source text available here is truncated — it does not name the plaintiff, court or claims, nor state the stake&\#x27;s price, valuation, share class or voting rights, or the government&\#x27;s stated legal authority for the demand.

**Background:** The stake at issue is not new: the US government&\#x27;s roughly 10 percent equity position in Intel was announced in August 2025, the same month Commerce Department lawyer David Shapiro pressed the company&\#x27;s CFO on the terms. What this report adds is the internal record of how the board was moved to accept — notes from a company call that now appear in a federal lawsuit. Intel is the largest US-headquartered maker of advanced logic chips, which is why the terms of government ownership bear directly on who controls domestic chipmaking capacity.

**Why it matters:** The notes as described leave Intel&\#x27;s board with two recorded options: accept the government&\#x27;s terms on the administration&\#x27;s timetable, or accept consequences the official said he could not predict. For other chipmakers that depend on federal money or approvals, the practical concern is that the cost of the stake can be priced while the cost of refusing cannot, so boards should expect equity demands to arrive with a deadline attached rather than as something to negotiate.

<details><summary>References</summary>
<ul>
<li>Not Just Nvidia: Inside Team Trump&#x27;s Takeover of Intel | WIRED</li>
<li>Trump Team&#x27;s Secret Ultimatum Exposed in Court - Yahoo</li>
<li>Trump Team&#x27;s Secret Ultimatum Exposed in Court - The Daily Beast</li>

</ul>
</details>

**Tags**: `#Intel`, `#US industrial policy`, `#semiconductor supply chain`, `#government equity stake`, `#chip policy`

---

<a id="item-chips-compute-2"></a>
### [MATCH Act&\#x27;s ASML China service ban could backfire, LithoWar analysis argues](https://www.techmeme.com/261127/p16#a261127p16) ⭐️ 7.0/10

A LithoWar analysis argues that the pending US export-control measure known as the MATCH Act could backfire if it bars ASML from servicing the roughly 350 immersion DUV \(deep-ultraviolet\) scanners already installed in China. Rather than idling those machines, the analysis contends, a service cutoff would open room for rival firms to maintain the tools, for reverse engineering of equipment ASML can no longer support, and for competitors to recruit ASML-trained staff. The bill targets servicing rather than new sales, and it is a proposed measure, not enacted law; the backfire outcome is the author&\#x27;s argument, not a measured result.

Techmeme · Nov 28, 02:00

**Verified and unconfirmed:** Verified: The MATCH Act is a pending US export-control measure that, as LithoWar describes it, would bar sales of immersion DUV lithography scanners to China and cut off parts, service and software support for machines already installed there; explainx and bits-chips.com describe the bill the same way, with explainx reporting it is currently folded into the Senate&\#x27;s defense bill and could be attached to the FY2027 defense legislation in mid-December 2026. LithoWar attributes the figure of roughly 350 immersion scanners in China to ASML&\#x27;s installed base there, and bits-chips.com likewise reports the bill would cut support for &quot;much of the installed fleet.&quot;

Not yet confirmed: The ~350 figure is an estimate that none of the available reports traces to an ASML disclosure or a regulatory document, and LithoWar&\#x27;s central claim — that a servicing ban would let rivals take over maintenance, reverse-engineer the tools and hire ASML&\#x27;s Chinese staff — is the author&\#x27;s argument about unintended consequences, not a measured outcome. Whether the measure passes, and in what final form, remains open; the reports also note Dutch government opposition and ASML CEO Christophe Fouquet&\#x27;s warning that a total cutoff could backfire, but the source material available here is a headline and teaser, so the underlying sourcing for those positions could not be checked.

**Background:** Immersion DUV scanners — ASML&\#x27;s Twinscan NXT line — are the workhorse machines that pattern most chips made on mature and mid-range nodes, and US export controls have so far focused on blocking sales of new tools rather than on the installed base already sitting inside China. Tom&\#x27;s Hardware reported that Chinese fabs have been squeezing more life out of those older immersion DUV tools as controls tightened, while ZeroHedge reported that China had accumulated roughly 340 ASML scanners and that chip hawks in Congress were moving to attach several export-control bills to the must-pass FY2027 defense bill. Because these machines depend on ASML-supplied parts, calibration and field engineers, service access is the remaining lever the MATCH Act would pull — the premise of LithoWar&\#x27;s argument.

**Why it matters:** The lever at stake is control over an installed base rather than new sales: if ASML is cut off from servicing those ~350 tools, the analysis says maintenance know-how and spare-part supply could migrate to third-party service providers and Chinese firms, eroding the long-term grip the control is meant to preserve. Fabs running those scanners would then need alternative service and parts arrangements, and ASML would lose the service relationship that keeps its tools tied to its own ecosystem.

**What to watch:** Whether the MATCH Act advances from a proposed measure into enacted law, and how the final text defines &quot;servicing&quot; — the treatment of spare parts, on-site engineers and software updates determines whether the backfire scenario is plausible.

<details><summary>References</summary>
<ul>
<li><a href="https://explainx.ai/blog/match-act-asml-immersion-scanners-servicing-backfire-november-2026">MATCH Act ASML: 350 Immersion Scanners at Risk (2026 ...</a></li>
<li><a href="https://bits-chips.com/article/the-match-act-could-hand-china-the-keys-to-advanced-lithography/">The Match Act could hand China the keys to advanced ...</a></li>
<li><a href="https://byte.eco/post/how-the-match-act-could-backfire-by-barring-asml-from-its-350-immersion-scanners-in-china">How the MATCH Act could backfire by barring ASML from its…</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/semiconductors/china-is-squeezing-more-life-out-of-asmls-older-duv-tools-as-chip-controls-tighten">Chinese fabs are reportedly upgrading older ASML ... | Tom&#x27;s Hardware</a></li>
<li><a href="https://www.zerohedge.com/technology/chip-war-goes-nuclear-beijing-hoarded-340-asml-scanners-congress-targets-service-calls">Chip War Goes Nuclear: Beijing Hoarded 340 ASML Scanners ...</a></li>

</ul>
</details>

**Tags**: `#export controls`, `#ASML`, `#lithography`, `#China semiconductors`, `#supply chain`

---

<a id="item-chips-compute-3"></a>
### [SemiAnalysis benchmarks AWS Trainium3, claims best inference cost-per-token after Nvidia Vera Rubin](https://newsletter.semianalysis.com/p/trainium3-inferencex) ⭐️ 7.0/10

SemiAnalysis published a microarchitecture deep dive on AWS&\#x27;s Trainium3 accelerator, placing it on its InferenceX leaderboard alongside Google TPUv7, OpenAI&\#x27;s Jalapeño, AMD parts and Nvidia&\#x27;s GB300 and Rubin NVL72. The firm says Trainium3 running vLLM with PDS sits on a better throughput-per-TCO \(total cost of ownership\) frontier than every listed accelerator except Nvidia&\#x27;s Vera Rubin across the curve of cost versus p90 interactivity, and that it trades blows with or beats GB300 on cost to generate tokens. SemiAnalysis attributes part of the gain to design choices rather than Amazon&\#x27;s supply chain alone: its Trainium Descriptor Generation Engines \(DGE\), the counterpart of Nvidia&\#x27;s TMA tile-movement unit, let the chip hit peak HBM bandwidth utilization at small message sizes, which the firm says is not possible on Nvidia GPUs. The results come from SemiAnalysis&\#x27;s own UBenchX microbenchmarks and an AgentX test that replays real coding-agent sessions against a Trainium3 server, with AWS Annapurna Labs engineers helping validate the experiments; the excerpt published no absolute throughput, price or instance-availability figures.

SemiAnalysis · Nov 27, 15:54

**Verified and unconfirmed:** Verified: SemiAnalysis measured Trainium3 on its InferenceX and UBenchX suites, ran an end-to-end agentic coding workload against a Trainium3 server, and says AWS Annapurna Labs co-founder Nafea Bshara and Trainium chief architect Ron Diamant helped validate the experiments. Not yet confirmed: the specific claims that Trainium3 beats or matches Nvidia GB300 on cost per token and reaches peak HBM bandwidth utilization at small message sizes rest on SemiAnalysis&\#x27;s own benchmarks and charts, and the excerpt gives no absolute performance numbers, instance pricing, general-availability date or independent replication.

**Background:** Trainium is AWS&\#x27;s in-house AI accelerator family, designed by Annapurna Labs; AWS says Trainium3 has eight large cores, each with Tensor, Vector, Scalar and GPSIMD engines, and up to twice the MXFP8 compute throughput of Trainium2. Nvidia&\#x27;s data-center GPUs began as graphics processors and have added AI-specific hardware generation by generation—Tensor Cores in Volta, TMA for tile data movement in Hopper—whereas Trainium was designed from the ground up for machine learning with tiles as a first-class primitive, a contrast that shapes how inference workloads map onto the chip.

**Why it matters:** For teams choosing inference hardware, the practical claim is that Trainium3&\#x27;s cost advantage depends on a specific software path — vLLM with PDS on Neuron — so a real migration means validating that stack against the framework and kernels a team already runs, not just comparing chip specifications; the headline numbers also come from the benchmark vendor whose suite is being cited, and the underlying data lives in charts the excerpt does not reproduce.

**What to watch:** Watch for AWS to publish Trainium3 instance pricing and general-availability terms, and for third parties to reproduce the cost-per-token results on InferenceX rather than relying on the benchmark author&\#x27;s own run.

<details><summary>References</summary>
<ul>
<li><a href="https://aws.amazon.com/ai/machine-learning/trainium/">AI Accelerator - AWS Trainium - AWS</a></li>

</ul>
</details>

**Tags**: `#AWS Trainium`, `#AI accelerators`, `#inference`, `#microarchitecture`, `#semiconductor supply chain`

---

<a id="item-chips-compute-4"></a>
### [Kioxia&\#x27;s Gen 3 XL-Flash targets 3 µs reads, samples in March 2027](https://www.tomshardware.com/pc-components/ssds/kioxias-3rd-gen-xl-flash-hits-optane-class-3-microsecond-read-latency-with-70-percent-higher-density-samples-march-2027-ahead-of-18-million-iops-gp2-ssds) ⭐️ 7.0/10

Kioxia has showcased a third-generation XL-Flash prototype that it says reaches 3 µs average read latency — less than 10% of the 40 µs of its BiCS8 TLC flash — while delivering 70% higher bit density and about 135% better efficiency than Gen 2 through CBA wafer bonding. The low-latency NAND is aimed at a memory tier between DRAM and conventional flash in AI servers and data centers, a role Intel&\#x27;s Optane once targeted. Kioxia named its GP2 enterprise SSD as the first product to use the flash, with claimed ratings above 18 million 512-byte random-read IOPS, up to 28 GB/s sequential reads over PCIe 6.0 x4 and up to 50 drive writes per day. XL-Flash samples are due to select customers by the end of Q1 2027, while GP2 evaluation samples are promised only by the end of 2027; the figures are vendor claims for a prototype and the drive&\#x27;s exact specifications may change.

Tom&\#x27;s Hardware · Nov 27, 12:00

**Verified and unconfirmed:** Verified: Kioxia showcased the Gen 3 XL-Flash prototype at its KIOXIA Forum in Tokyo and states that it uses CBA bonding, delivers 3 µs average read latency, 70% higher bit density and roughly 135% better efficiency than Gen 2; it named GP2 as the first product to use it. Not yet confirmed: independent measurements of latency, IOPS or endurance; the SLC cell type, 128Gb die size, 150,000–250,000 P/E cycles and 4.8 Gb/s interface are reported details, and Kioxia has not disclosed layer count; GP2&\#x27;s 18 million+ IOPS, 28 GB/s sequential read and 50 DWPD figures are targets, with exact specifications subject to change.

**Background:** XL-Flash is Kioxia&\#x27;s storage-class memory: NAND tuned for low read latency and high write endurance rather than cheap capacity, so it can sit between DRAM and ordinary flash. The first generation arrived in 2019 with single-level cells \(SLC, one bit per cell\) and sub-5 µs reads, and the 2022 second generation added a two-bit MLC option that traded some like-for-like performance for lower cost per bit. The memory tier it targets was left open when Intel wound down Optane, its 3D XPoint-based rival, in 2022.

**Why it matters:** Teams designing AI-server memory hierarchies should not plan procurement around GP2 yet: XL-Flash samples arrive in Q1 2027 and GP2 evaluation samples only at the end of 2027, so the drive cannot address current HBM or DRAM capacity pressure. If the 512-byte-read performance holds, storage and model-serving software will need to issue and schedule small I/Os, rather than the usual 4KB accesses, to capture the benefit.

**What to watch:** Watch whether Kioxia ships XL-Flash Gen 3 samples to select customers by the end of Q1 2027 and GP2 evaluation samples by the end of 2027, and whether independent tests reproduce the 3 µs latency and above-18-million-IOPS claims.

**Tags**: `#Kioxia`, `#XL-Flash`, `#NAND flash`, `#low-latency memory`, `#AI data centers`

---

## EVs &amp; Energy

<a id="item-ev-energy-1"></a>
### [EU EV Sales Beat Gas and Diesel Combined in October, InsideEVs Reports](https://insideevs.com/news/817061/eu-ev-sales-october-jump/) ⭐️ 8.0/10

Electric vehicles outsold petrol and diesel cars combined in the European Union in October, InsideEVs reported, turning a 127,000-car deficit in the same month a year earlier into a lead of nearly 70,000 cars. The report presents the result as a single-month crossover and does not give total registrations, market-share percentages, or the underlying registration data the comparison rests on. It also leaves the powertrain categories undefined — whether &quot;EV&quot; covers only battery-electric cars or includes plug-in hybrids is not stated — so the exact scope of the flip is not established by the account.

InsideEVs · Nov 27, 15:15

**Verified and unconfirmed:** Verified: ACEA&\#x27;s October registration release reports battery-electric cars at 23.4% of EU new-car registrations in January–October 2026, up from 16.4% a year earlier, with petrol and diesel combined at 27.7%, down from 36.5%; it also reports 279,799 battery-electric registrations in October alone, up 61.4% year on year.
Not yet confirmed: That EVs outsold petrol and diesel cars combined in October by nearly 70,000 units, and that the prior-year gap was 127,000, rests on InsideEVs&\#x27; report; the supplied ACEA figures give year-to-date shares and October BEV volume but no October petrol-plus-diesel total, and the year-to-date shares \(BEV 23.4% vs petrol and diesel 27.7%\) do not by themselves establish the October overtake. The term “EVs” is also undefined—battery-electric only or including plug-in hybrids.

**Background:** AI Daily Radar&\#x27;s November 24 digest, citing figures from ACEA, the European automakers&\#x27; association, reported that battery-electric cars took nearly 30% of EU passenger-car registrations in October — roughly 280,000 units, 61% more than in the same month a year earlier and above the 250,000-plus monthly pace pure electric cars had recently been sustaining. That established the volume behind the shift; the new comparison adds the other side of the ledger, where combined petrol and diesel sales held a 127,000-car lead a year earlier but trailed by nearly 70,000 cars in October. The earlier ACEA-based report gave no country-by-country or model breakdown, and the same level of detail is missing from the combined tally.

**Why it matters:** For automakers and dealers selling in the EU, a month in which EVs are the largest group in the new-car market changes the volume base used for product planning and charging investment — but only if it persists. The report does not separate how much of the 197,000-car swing came from EV growth versus falling petrol and diesel sales, which is the first thing to check before treating October as a new baseline rather than an outlier month.

**What to watch:** Watch the next monthly EU new-car registration figures to see whether EVs keep the lead, and whether the shift is driven by rising EV volumes or by a decline in petrol and diesel sales.

<details><summary>References</summary>
<ul>
<li><a href="https://www.electrive.com/2026/11/24/acea-battery-electric-cars-capture-30-per-cent-of-eu-passenger-car-market/">2026-11-24 — Battery-electric cars near 30% of EU new-car market in October, ACEA data shows</a></li>
<li><a href="https://www.acea.auto/pc-registrations/new-car-registrations-5-4-in-october-2026-year-to-date-battery-electric-23-4-market-share/">New car registrations: +5.4% in October 2026 year-to-date ...</a></li>
<li><a href="https://www.acea.auto/files/Press_release_car_registrations_October_2026.pdf">EMBARGOED PRESS RELEASE 6.00 CET (5.00 GMT), 24 November 2026</a></li>
<li><a href="https://theevreport.com/eu-car-registrations-october-2026-battery-electric-share">EU Car Registrations: Battery-Electric Share 23.4% Through ...</a></li>

</ul>
</details>

**Tags**: `#EV sales`, `#European Union`, `#market share`, `#gasoline and diesel`, `#EV adoption`

---

<a id="item-ev-energy-2"></a>
### [Germany&\#x27;s solar output passes 100 TWh in a year for the first time](https://www.pv-magazine.com/2026/11/28/germanys-solar-generation-tops-100-twh-in-2026/) ⭐️ 8.0/10

Germany&\#x27;s photovoltaic systems generated more than 100 TWh of electricity in a calendar year for the first time, according to the Fraunhofer Institute for Solar Energy Systems&\#x27; Energy-Charts platform. The data showed 100.2 TWh by the morning of Nov. 27, up about 10 TWh from the 90 TWh recorded for 2025. Of the total, 80.6 TWh was fed into the grid by plants paid under Germany&\#x27;s Renewable Energy Sources Act \(EEG\), 2.6 TWh came from other PV systems, and 16.9 TWh was consumed on site by the producers. Solar was the country&\#x27;s second-largest source of net generation so far this year, behind wind at 124.4 TWh and ahead of gas at 82.1 TWh; lignite \(63 TWh\) and hard coal \(27.2 TWh\) together produced less than solar. The figures are running totals for the year to date, not a final full-year accounting.

pv magazine · Nov 28, 08:00

**Verified and unconfirmed:** Verified: Fraunhofer ISE&\#x27;s Energy-Charts data, as reported by pv magazine, shows 100.2 TWh of German solar generation by the morning of Nov. 27, split into 80.6 TWh of EEG-supported grid feed-in, 2.6 TWh from other PV systems and 16.9 TWh of self-consumption, against 90 TWh for the whole of 2025.
Not yet confirmed: the final full-year 2026 total, since the 100.2 TWh figure is a year-to-date reading taken in late November; the report also relies on a single data platform and does not give an independently audited breakdown, and the mid-November projection of the milestone by the solar and battery trade group BSB rested on the same Fraunhofer ISE numbers.

**Background:** Germany&\#x27;s Renewable Energy Sources Act \(EEG\) is the support scheme behind most of the country&\#x27;s solar build-out: it pays guaranteed or auction-set rates for photovoltaic power delivered to the grid, which is why Fraunhofer ISE reports EEG-supported feed-in, other grid feed-in and self-consumption as separate lines rather than one number. The institute&\#x27;s public Energy-Charts platform compiles the metered generation data that this year&\#x27;s total and earlier annual totals are drawn from, so the milestone is measured on the same basis as previous years.

**Why it matters:** Because lignite and hard coal together produced 90.2 TWh so far this year, solar has moved ahead of coal in Germany&\#x27;s generation mix, but the output is concentrated in sunny midday hours — the 16.9 TWh of self-consumption shows how much now sits behind the meter. Grid operators and battery developers face a growing midday surplus to absorb or curtail, and the year-on-year gain of about 10 TWh indicates the trend is continuing rather than a one-off weather effect.

**What to watch:** Fraunhofer ISE&\#x27;s final 2026 generation figures on Energy-Charts after the year closes, which will confirm the full-year total and whether solar holds its place ahead of coal in the annual mix.

**Tags**: `#Germany solar`, `#solar generation`, `#Fraunhofer ISE`, `#renewable energy milestone`, `#Energy-Charts`

---

<a id="item-ev-energy-3"></a>
### [BRF Froan: electric bulk carrier with a 23.5 MWh battery](https://electrek.co/2026/11/27/worlds-largest-electric-bulk-cargo-shop-packs-massive-23-5-mwh-battery/) ⭐️ 7.0/10

Electrek reports that a newly built bulk carrier, the BRF Froan, carries a 23,500 kWh \(23.5 MWh\) battery — presented as the largest pack yet fitted to an electric bulk cargo ship. The vessel is described as carrying coal, sugar and other bulk cargoes, the heavy, high-volume trade that has been hardest to electrify. The report gives no battery supplier, route, range, charging arrangement or delivery date, and the &quot;world&\#x27;s largest&quot; description is the outlet&\#x27;s characterization rather than an independently verified record. No figures on how the ship is charged or how far it can sail on a single charge are included.

Electrek · Nov 27, 19:22

**Verified and unconfirmed:** Verified: Electrek reports that the BRF Froan is a new electric bulk carrier fitted with a 23,500 kWh \(23.5 MWh\) battery, and describes it as the largest such ship in the bulk cargo segment.
Not yet confirmed: The battery manufacturer, the ship&\#x27;s operator, its routes and service area, charging method and power, range, and any independent confirmation of the &quot;world&\#x27;s largest&quot; claim — the report does not state a delivery or commissioning date either.

**Background:** BRF Froan is a 129.9-meter bulk carrier — a ship built for unpackaged cargo such as coal, grain or sugar — that is heading to Norway to have its battery installed, according to Interesting Engineering. Operator Berge Rederi says shore-power facilities will be installed at both ports the vessel serves, letting it recharge there; the company estimates annual shore charging at 5,133,000 kWh.

**Why it matters:** For operators and ports, a pack this size moves the binding constraint ashore: a 23.5 MWh battery has to be replenished at the berths the ship serves, so the port&\#x27;s charging capacity and the ship&\#x27;s schedule become as decisive as the battery itself. Charterers evaluating electric bulk tonnage will need to confirm charging arrangements at both ends of a route before treating the vessel as a drop-in substitute for conventional fuel.

<details><summary>References</summary>
<ul>
<li><a href="https://interestingengineering.com/transportation/worlds-largest-electric-bulker-carrier">World’s largest electric cargo ship with 23.5 MWh battery set ...</a></li>
<li><a href="https://www.bergerederi.no/froan">BRF Froan - Berge Rederi AS</a></li>

</ul>
</details>

**Tags**: `#electric shipping`, `#batteries`, `#cargo ship`, `#maritime decarbonization`, `#23.5 MWh`

---

<a id="item-ev-energy-4"></a>
### [Toyota confirms Highlander 9X as its first EREV, on sale early 2027](https://electrek.co/2026/11/27/toyota-confirms-highlander-9x-first-erev-top-tier-tech/) ⭐️ 7.0/10

Toyota has confirmed that the Highlander 9X will go on sale in early 2027 as the brand&\#x27;s first extended-range electric vehicle \(EREV\) — a plug-in vehicle whose combustion engine acts mainly as a generator to recharge the battery rather than drive the wheels. The model will use technology from Huawei and CATL, according to Electrek. Toyota has not disclosed the vehicle&\#x27;s electric range, battery size, powertrain output, price, or which markets it will be sold in, so the early-2027 date is the only firm detail beyond the two Chinese suppliers named.

Electrek · Nov 27, 17:18

**Verified and unconfirmed:** Verified: Toyota confirmed the Highlander 9X as its first EREV with an early-2027 on-sale date and named Huawei and CATL as technology suppliers, Electrek reported. Not yet confirmed: range, battery capacity, power output, price, target markets, and exactly which components Huawei and CATL will supply; no independent testing or production-model specifications exist yet.

**Background:** An extended-range electric vehicle \(EREV\) drives its wheels with an electric motor and carries a small gasoline engine that works only as a generator to recharge the battery, so it runs on electricity most of the time but refuels instead of relying on a charger. The Highlander 9X has been signposted since GAC Toyota&\#x27;s June 2025 technology day, where the joint venture said Chinese engineers would lead development of the next-generation Highlander and Sienna for the Chinese market and that both would get range-extended powertrains, according to CarNewsChina.

**Why it matters:** For a company that built its electrified lineup around its own hybrid systems, Toyota&\#x27;s first EREV will depend on Huawei and CATL for core electrified technology — so the model&\#x27;s specifications and timing rest on those supplier relationships. Buyers cross-shopping it against Toyota&\#x27;s existing hybrids and plug-in hybrids have no range or price figures to compare until Toyota publishes them.

**What to watch:** Watch for Toyota to release the Highlander 9X&\#x27;s powertrain and battery specifications and to confirm which markets it will be sold in, ahead of the stated early-2027 on-sale date.

<details><summary>References</summary>
<ul>
<li><a href="https://carnewschina.com/2026/11/25/toyota-highlander-erev-expected-to-debut-in-china-on-november-27/">Toyota Highlander EREV expected to debut in China on November 27</a></li>

</ul>
</details>

**Tags**: `#Toyota`, `#EREV`, `#Highlander 9X`, `#CATL`, `#Huawei`

---

<a id="item-ev-energy-5"></a>
### [Congress passes e-bike battery safety law making voluntary standards mandatory](https://electrek.co/2026/11/27/congress-just-passed-a-major-e-bike-safety-law-heres-what-it-actually-means/) ⭐️ 7.0/10

Congress has passed legislation that would turn what have largely been voluntary US e-bike battery safety standards into mandatory federal requirements, Electrek reports. The change would apply to the e-bike batteries and bikes sold in the US, shifting the burden of safety compliance from voluntary industry practice to federal law. The report does not name the specific standards involved, the effective date, the penalties for non-compliance, or whether the bill has yet been signed into law; it describes the requirements only as &quot;on the verge&quot; of becoming mandatory.

Electrek · Nov 27, 11:24

**Verified and unconfirmed:** Verified: Electrek reports that Congress passed legislation converting largely voluntary US e-bike battery safety standards into mandatory federal requirements.
Not yet confirmed: Which specific standards the law codifies, when the requirements take effect, what enforcement or penalties apply, whether the bill has been signed, and how manufacturers and importers would be required to demonstrate compliance — none of these details appear in the report.

**Background:** US e-bike battery safety has rested largely on voluntary standards — chiefly Underwriters Laboratories&\#x27; testing criteria — which manufacturers could adopt or skip. The Consumer Product Safety Commission published a proposed rule \(16 CFR Part 1265\) on June 24, 2026 that would make lithium-ion battery safety standards mandatory for e-bikes and other micromobility devices, and the Senate separately passed a bill directing the agency to issue a final rule adopting UL standards within 180 days of enactment. The legislation Congress has now passed follows that second, legislative track.

**Why it matters:** If the requirements take effect as described, US e-bike sellers and importers could no longer rely on voluntary compliance, and would instead need to show their batteries meet a federal standard before selling them — a certification and testing burden that falls hardest on smaller brands and direct-to-consumer importers.

<details><summary>References</summary>
<ul>
<li><a href="https://biketips.com/cpsc-ebike-battery-safety-rule-2026/">New Federal E-Bike Battery Rule: What Riders Should Know</a></li>
<li><a href="https://www.peopleforbikes.org/news/senate-passes-battery-safety-bill">Senate Passes Bill to Strengthen Federal Safety Standards for ...</a></li>

</ul>
</details>

**Tags**: `#e-bike safety`, `#battery regulation`, `#federal policy`, `#micromobility`

---

<a id="item-ev-energy-6"></a>
### [Arriva wins €2bn North Holland contract with 200+ electric buses](https://www.electrive.com/2026/11/28/arriva-secures-two-billion-euro-contract-for-electric-buses-in-north-holland/) ⭐️ 7.0/10

Arriva has won a long-term contract to run bus services in the northwest of the Dutch province of North Holland, a deal valued at roughly €2 billion. The agreement covers the deployment of more than 200 electric buses alongside adjustments to the route network. According to electrive, the award extends Arriva&\#x27;s recent run of major contract wins in the Netherlands. The report does not specify when the buses enter service, which manufacturer will supply them, or how much of the €2 billion is vehicle investment versus operating subsidy.

Electrive · Nov 28, 09:00

**Verified and unconfirmed:** Verified: Arriva&\#x27;s own announcement states the North-West North Holland bus contract is worth about €2 billion and runs 13 years from July 2028, with a two-year option; the fleet will be 100% electric and number more than 200 buses, which Arriva calls its largest-ever bus contract \(Arriva; also reported by Sustainable Bus and Bus News\).

Not yet confirmed: the split between new and existing vehicles, which manufacturers will supply the buses, and how much of the €2 billion covers vehicles versus operations are not specified; the initial electrive report gave no start date or operator-level detail, so those figures rest on Arriva&\#x27;s release and the trade press rather than an independent test or regulatory filing.

**Background:** The deal is a concession: a long-term award by a regional transport authority to a single operator to run an area&\#x27;s bus network, which is why the electric fleet and the route changes are bundled into the same contract rather than procured separately. Arriva already runs bus services in the Netherlands, and the report describes this award as extending a run of major contract wins there.

**Why it matters:** More than 200 electric buses have to be charged, serviced and parked, so the award obliges Arriva to build depot charging and maintenance capacity at a scale well beyond a pilot — in practice the main constraint on when the vehicles enter service. The vehicle order is also still open: the contract names no manufacturer, and Arriva has sourced e-buses from BYD before, ordering 82 of them for its Budapest zero-emission tender, so the bus and charging-equipment contracts are the concrete openings for suppliers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sustainable-bus.com/news/arriva-north-holland-new-contract-netherlands/">Arriva wins €2 billion bus contract in the Netherlands, with ...</a></li>
<li><a href="https://news.arriva.co.uk/news/arriva-strengthens-position-in-the-netherlands-with-major-2bn-bus-contract">Arriva strengthens position in the Netherlands with record € ...</a></li>
<li><a href="https://bus-news.com/arriva-awarded-record-e2-billion-contract-for-holland-based-services/">Arriva Awarded Record €2 Billion Contract for Holland-Based ...</a></li>
<li><a href="https://www.sustainable-bus.com/author/dhk67gfkd3w/page/288/">Editorial Staff, Author at Sustainable Bus - Page 288 of 362</a></li>

</ul>
</details>

**Tags**: `#electric buses`, `#fleet electrification`, `#public transport`, `#Netherlands`, `#contracts`

---

<a id="item-ev-energy-7"></a>
### [CATL unveils 100 kWh &\#x27;30\#&\#x27; swappable battery for passenger cars](https://www.electrive.com/2026/11/27/catl-introduces-100kwh-30-swappable-battery-for-passenger-cars/) ⭐️ 7.0/10

CATL has introduced a new battery pack for its battery-swapping ecosystem in China, dubbed the &quot;30\#&quot; battery block, with a capacity of 100 kWh. According to the company&\#x27;s announcement, the pack can be swapped in under a minute, and it can alternatively be fast-charged at a conventional charging station rather than being confined to swap stations. CATL did not disclose the pack&\#x27;s chemistry, which vehicle models will accept it, when it will enter service or what it will cost, so the sub-minute swap time and 100 kWh figure remain company claims rather than independently measured results.

Electrive · Nov 27, 14:30

**Verified and unconfirmed:** Verified: CATL unveiled a 100 kWh passenger-car battery pack called “30\#” for its swapping network in China, which the company says can be exchanged in about a minute and can also be fast-charged at ordinary charging stations, electrive reported on 27 November; Chinese and specialist outlets covering the same launch \(CarNewsChina, Interesting Engineering\) attribute the 99-second swap figure, a 700 km CLTC range and a lifetime warranty for packs in the network to CATL.

Not yet confirmed: everything beyond capacity and the two use modes rests on CATL&\#x27;s own presentation — the 700 km CLTC range, 99-second swap, 600 kW peak discharge, a 3-second 0–100 km/h sprint and a 27-year locking-mechanism lifespan have not been independently tested, and the reports leave out battery chemistry, which vehicle models are compatible, pack price, and when or where the pack will be deployed; the sources also conflict on swap time, with electrive saying “under a minute” while the other outlets report 99 seconds, which is just over one minute.

**Background:** Battery swapping exchanges a depleted pack for a charged one at a dedicated station rather than waiting at a charger, which requires packs built to a shared size and connector and cars designed around that standard. CATL already operates a battery-swapping ecosystem in China, and the &quot;30\#&quot; is a new pack added to that line-up rather than a standalone product — the company positions it as dual-use, since the same pack can also fast-charge at ordinary stations. Because the format only works if carmakers build vehicles to accept it, the pack&\#x27;s reach depends on which automakers adopt CATL&\#x27;s swap standard.

**Why it matters:** A swappable pack that also accepts standard fast charging removes the main practical objection to swap-based EVs — that drivers are tied to a proprietary station network — which matters most for fleet operators weighing CATL&\#x27;s swapping system against conventional charging; whether that flexibility reaches buyers depends on which models CATL certifies for the pack, details it has not yet published.

<details><summary>References</summary>
<ul>
<li><a href="https://interestingengineering.com/energy/catl-100kwh-chocolate-battery-435-mile-range">CATL &#x27;s 100 kWh swappable battery offers 435-mile range for EVs</a></li>
<li><a href="https://carnewschina.com/2026/11/27/catl-unveils-30-chocolate-battery-with-a-100-kwh-capacity/">CATL unveils 30# Chocolate swappable battery with a 100 kWh ...</a></li>
<li><a href="https://beyondeastmedia.com/articles/catl-chocolate-battery-30-100kwh-3s-acceleration">CATL Unveils 30# Chocolate Battery with 100 kWh Pack and...</a></li>

</ul>
</details>

**Tags**: `#CATL`, `#battery swapping`, `#EV batteries`, `#China`, `#fast charging`

---

## Space

<a id="item-space-1"></a>
### [Stoke Space&\#x27;s Nova Pathfinder booster arrives at SLC-14 ahead of 2027 debut](https://www.nasaspaceflight.com/2026/11/stoke-nova-booster-slc-14-2027-debut/) ⭐️ 7.0/10

Stoke Space&\#x27;s Nova Pathfinder first stage arrived at Space Launch Complex 14 at Cape Canaveral Space Force Station on Nov. 22 after a 17-day road trip from Washington, then entered the pad&\#x27;s Horizontal Integration Facility; it is the first rocket at the historic pad since the 1960s. Stoke plans a pad-in-the-loop wet dress rehearsal campaign, after which the stage will roll back to the HIF to have its remaining Zenith engines integrated, return for a static fire, and later mate with the second stage. The company is targeting an early 2027 inaugural launch, with a Stage 2 static fire scheduled for December at Moses Lake once the upper stage is mated with its Andromeda engine. Four of seven Zenith flight engines have completed acceptance testing, and Stage 2 has completed cryogenic proof testing and a full wet dress rehearsal.

NASASpaceflight · Nov 27, 14:52

**Verified and unconfirmed:** Verified: NASASpaceflight reported that the first stage arrived at SLC-14 on Nov. 22 and entered the HIF, and that Stage 2 completed cryogenic proof testing and a full wet dress rehearsal; Stoke Space&\#x27;s own X post said a rocket was at SLC-14 for the first time in 60 years. Not yet confirmed: The early 2027 launch date and the December Stage 2 static fire are Stoke&\#x27;s plans, not completed events; the report gives no payload capacity, price, or independent confirmation that the integrated vehicle will fly on that schedule.

**Background:** Nova is Stoke Space&\#x27;s two-stage, fully reusable rocket, and its upper stage is the unusual part: instead of ablative material or ceramic tiles, it uses an actively cooled metallic heat shield with cryogenic propellant circulated through it during reentry, which the company says is meant to permit repeated flights with minimal inspection between them. SLC-14 itself is a historic Cape Canaveral pad that has not hosted a rocket since the 1960s, so Pathfinder&\#x27;s arrival also reactivates the rebuilt complex. Beyond this first flight, Stoke unveiled a heavier Nova Block 2 variant in September, and that version is expected to begin flying in 2029, according to Payload.

**Why it matters:** Stoke&\#x27;s ability to hit the early 2027 target now depends on installing the remaining three Zenith engines, completing Stage 1 static fire and mating the two stages, the steps that gate the first integrated Nova vehicle.

**What to watch:** Watch the Stage 2 static fire at Moses Lake in December, then the Stage 1 wet dress rehearsals and static fire at SLC-14 before the early 2027 launch target.

<details><summary>References</summary>
<ul>
<li><a href="https://payloadspace.com/seops-signs-rideshare-deal-with-stoke/">SEOPS Signs Rideshare Deal With Stoke</a></li>

</ul>
</details>

**Tags**: `#Stoke Space`, `#Nova Pathfinder`, `#SLC-14`, `#launch vehicle development`, `#wet dress rehearsal`

---

## Tech Industry &amp; Policy

<a id="item-tech-industry-1"></a>
### [SAP confirms GitHub incident; report says stolen tokens allowed source-code changes, SecurityWeek reports](https://www.techmeme.com/261127/p9#a261127p9) ⭐️ 7.0/10

SAP has confirmed a cybersecurity incident after detecting suspicious activity on GitHub, the code-hosting platform where it keeps source code. According to SecurityWeek, attackers obtained authentication tokens belonging to SAP employees and used them to copy and alter source code stored there. SAP has not publicly said which repositories or products were affected, how many accounts were involved, or whether altered code reached any software it ships. The company&\#x27;s confirmation covers the suspicious GitHub activity itself; the token theft and code alteration rest on the outlet&\#x27;s reporting.

Techmeme · Nov 27, 16:35

**Verified and unconfirmed:** Verified: SAP confirmed an IT security incident and said it detected suspicious activity on GitHub, according to SecurityWeek and BleepingComputer.
Not yet confirmed: That attackers stole SAP employees&\#x27; authentication tokens and used them to copy and alter source code rests on DER SPIEGEL reporting and insider sources cited by BleepingComputer; SAP has not confirmed which repositories were affected, whether altered code reached products, how many tokens were involved, or when the activity occurred.

**Background:** GitHub access tokens — including personal access tokens and OAuth tokens issued to developer tools — are long-lived credentials that let a user or script act on repositories without re-entering a password. Because they authenticate directly to the API, they can bypass password checks and often multi-factor prompts, which is why stolen tokens are a common route into code hosting accounts. For a vendor like SAP, whose enterprise products are built and shipped from its repositories, unauthorized changes to source code raise questions about build integrity and not just data exposure.

**Why it matters:** For SAP customers and developers, the concern is code integrity rather than uptime: if employee tokens were enough to modify repositories, then pulled code should be checked against expected commits and signed releases rather than trusted because it sits in SAP&\#x27;s GitHub organisation. Until SAP names the affected repositories, teams cannot tell whether anything they build on was touched.

**What to watch:** Watch for SAP&\#x27;s own incident statement or a SecurityWeek follow-up specifying which repositories and how many accounts were involved, and whether any altered code reached a released product.

<details><summary>References</summary>
<ul>
<li><a href="https://www.securityweek.com/sap-confirms-cyberattack-source-code-reportedly-compromised/">SAP Confirms Cyberattack, Source Code Reportedly... - SecurityWeek</a></li>
<li><a href="https://cybersecuritynews.com/sap-security-incident/">SAP Confirms Security Incident as Hackers Reportedly Steal ...</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/sap-confirms-security-incident-after-suspicious-github-activity/">SAP confirms security incident after suspicious GitHub activity</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#SAP`, `#source code`, `#GitHub`, `#security incident`

---

<a id="item-tech-industry-2"></a>
### [AMD and Winbond firmware flaws speed up BitLocker PIN brute-force attacks](https://www.tomshardware.com/tech-industry/cyber-security/amd-and-winbond-vulnerabilities-let-attackers-brute-force-bitlocker-pins-on-millions-of-pcs-cracking-a-six-digit-pin-drops-from-19-years-to-20-days) ⭐️ 7.0/10

Researchers at Technische Universität Berlin found firmware vulnerabilities in AMD&\#x27;s fTPM \(firmware trusted platform module\) storage handling and in Winbond SPI flash chips with RPMC \(replay-protected monotonic counter\) rollback protection that let an attacker with physical access defeat BitLocker&\#x27;s failed-attempt lockout and brute-force a short PIN much faster. For Winbond, a voltage glitch makes the chip reveal its HMAC key, and a low-cost interposer then impersonates the chip so the failed-attempt counter never rises; the team tested two Winbond models and believes the flaw is in the RPMC engine design. On AMD systems, the firmware does not verify that the counter increment actually happened, so an attacker can intercept the command without any HMAC key; the researchers verified at least one attack on machines from Zen 2 through an AI 5 330 laptop and suspect all contemporary AMD fTPM consumer hardware is affected. The report says a six-digit numeric PIN that would take 19 years under normal lockout can be broken in about 20 days, potentially affecting millions of PCs, and no vendor has committed to fixing the root causes; Microsoft has only announced a recommendation to use six-digit PINs instead of four during setup.

Tom&\#x27;s Hardware · Nov 27, 12:30

**Verified and unconfirmed:** Verified: Researchers at Technische Universität Berlin published an arXiv paper \(2611.18126, &quot;Hello Again: Exploiting Replay Protected…&quot;\) in which they demonstrate end-to-end, on locked and encrypted hardware, that a low-cost interposer board can suppress or roll back the TPM&\#x27;s failed-attempt counter; their setup recovered a 4-digit Windows Hello PIN in 40 hours instead of 69 days, and the authors state that none of the vendors they contacted had committed to fixing the root-cause vulnerabilities. The attacks require physical access to the machine.

Not yet confirmed: The &quot;millions of PCs&quot; scale rests on the paper&\#x27;s estimate of Winbond&\#x27;s roughly 25% SPI flash market share and on the researchers&\#x27; theory that the flaw extends across Winbond&\#x27;s lineup and to all contemporary AMD consumer platforms — they verified at least one AMD attack only on machines from Zen 2 through an AI 5 330 laptop. The 20-day six-digit-PIN figure is the researchers&\#x27; projected brute-force time, not an independently reproduced result, and neither AMD, Winbond, Microsoft nor OEMs have published fix timelines; the reported Microsoft guidance recommending six-digit PINs is described by the article without a linked Microsoft statement. Secondary coverage assigns CVE-2026-43613 to the AMD issue.

**Background:** BitLocker, Microsoft&\#x27;s built-in Windows disk encryption, can lean on the firmware TPM \(fTPM\) — a trusted-platform-module function implemented in CPU microcode and used by nearly all modern consumer x86 machines — rather than a separate chip. The fTPM keeps its anti-guessing protection in an SPI flash chip on the motherboard: an encrypted counter of failed unlock attempts that triggers a 10-minute wait after 32 successive tries, which is what stretches a short PIN to years of guessing. The new research targets that counter and the channel between the CPU and the flash chip.

**Why it matters:** Owners of affected machines cannot rely on BitLocker&\#x27;s 10-minute lockout to stop a thief who has physical access and cheap hardware from guessing a short PIN. The remediation path is uneven: AMD&\#x27;s missing counter check could be fixed in firmware via AGESA, but that requires OEM BIOS updates for devices that may be out of support, while the Winbond flaw can only be fixed by replacing the SPI chip. Microsoft&\#x27;s announced six-digit PIN recommendation does not address the counter bypass.

**What to watch:** Watch whether AMD releases an AGESA firmware update that makes its SPI controller actually verify failed-attempt counter writes, and whether OEMs then publish BIOS updates for affected laptops — the same distribution bottleneck that slowed Spectre/Meltdown fixes, since the researchers say no vendor has yet committed to fixing the root cause. Also watch whether Microsoft goes beyond its setup-time recommendation of a six-digit PIN and changes the BitLocker default itself.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2611.18126v1">[2611.18126v1] Hello Again: Exploiting Replay Protected ...</a></li>
<li><a href="https://secnews.co.uk/2026/11/tpm-lockout-reset-rpmc-attack-bitlocker-windows-hello-pins-cve-2026-43613/">Flash chip attack resets TPM lockout to crack BitLocker and ...</a></li>
<li><a href="https://pro-gamer.gg/amd-winbond-cve-2026-43613-bitlocker-pin-20-days-ryzen-pcs/">AMD Ryzen &amp; Winbond Flaws Cut BitLocker Cracking to 20 Days</a></li>
<li><a href="https://www.itechguides.com/amd-cpu-ftpm-enable-or-disable/">AMD CPU fTPM : How to Enable or Disable It</a></li>

</ul>
</details>

**Tags**: `#BitLocker`, `#hardware security`, `#AMD`, `#Winbond`, `#vulnerability research`

---