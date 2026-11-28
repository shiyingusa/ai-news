---
layout: story
lang: en
date: 2026-11-28 06:25:54 -0500
issue: "2026-11-28"
story_id: "google-s-deepcrossattention-claims-up-to-3x-speedup-at-comparable-bcf3"
permalink: "/2026/11/28/google-s-deepcrossattention-claims-up-to-3x-speedup-at-comparable-bcf3/"
title: "Google's DeepCrossAttention claims up to 3x speedup at comparable quality"
dek: "Google Research's blog describes DeepCrossAttention (DCA), which changes transformer residual connections so each token can attend to embeddings from prior layers—attention across depth rather than only across tokens…"
description: "Google Research's blog describes DeepCrossAttention (DCA), which changes transformer residual connections so each token can attend to embeddings from prior layers—attention across depth rather than only across tokens…"
section: "ai-news"
rank: 1
edition: 0
section_rank: 1
score: 7.0
status: "Demonstrated"
source_name: "research.google"
source_url: "https://research.google/blog/supercharging-transformer-residual-connections/"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50672565"
published_at: "2026-11-27T23:06:29+00:00"
tags: ["transformer architecture", "model efficiency", "attention mechanisms", "Google Research", "AI research"]
topics: ["transformer-architecture", "model-efficiency", "attention-mechanisms", "google-research", "ai-research"]
order: "20261128-0-998"
image: "/assets/stories/2026-11-28/google-s-deepcrossattention-claims-up-to-3x-speedup-at-comparable-bcf3-share.jpg"
art: "/assets/stories/2026-11-28/google-s-deepcrossattention-claims-up-to-3x-speedup-at-comparable-bcf3.jpg"
thumb: "/assets/stories/2026-11-28/google-s-deepcrossattention-claims-up-to-3x-speedup-at-comparable-bcf3-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/gdb5f523af4ef192a230a16d55d9d6334e48177613211e117660aab4f14aa2aa93c357fec2d7543671c68c7cabbd3e216235b91032dd7ba111780d7a8ede31901_1280.jpg", "author": "ann_zima", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/data-center-industry-2927337/", "provider": "Pixabay", "width": 4196, "height": 2447}
---

{% raw %}
<div class="story-lead" markdown="1">

Google Research's blog describes DeepCrossAttention (DCA), which changes transformer residual connections so each token can attend to embeddings from prior layers—attention across depth rather than only across tokens—and reports comparable model quality with up to 3x faster performance in its experiments. The result targets people building and training transformers, where scaling depth and attention is a central cost.

The speedup and quality parity are Google's own lab claims; the available reporting contains no independent benchmark or peer-reviewed paper.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** Google Research's blog post and the underlying ICML 2025 paper (arXiv 2502.06785) both state that DeepCrossAttention — depth-wise cross-attention over the residual stream — reaches the same model quality up to 3x faster while adding a negligible number of parameters, and improves perplexity for a given training time; the blog also reports that retrofitting DCA onto a pre-trained transformer and briefly continuing training cut LM1B perplexity by 0.19 versus 0.02 for continued standard training.
- **Not yet confirmed:** the "up to 3x" figure is a best-case result from Google's own language-modeling experiments (LM1B-scale, per the paper) and has not been independently reproduced or shown to hold at frontier scale; the reported parameter overhead, perplexity gains and speedups are the authors' measurements rather than third-party benchmarks, and no released model, code availability or production deployment is confirmed.

</div>

## Background

Transformer layers each pass their output forward through a residual (skip) connection, which adds that layer's result to the running representation so very deep networks remain trainable. In a standard transformer those additions carry fixed, equal weight, and the Google Research post notes that simply summing previous layers this way can dilute useful information. DeepCrossAttention keeps the depth-wise routing but makes it learned: each token queries a weighted mix of all earlier layer embeddings rather than receiving a uniform sum, which is the mechanism the reported speedup and quality parity rest on.

## Why it matters

For teams with existing checkpoints, the more actionable claim is the reported retrofit: a commenter quoting the blog says adding DCA to a pre-trained transformer and briefly continuing training reduced LM1B perplexity by 0.19, versus 0.02 for standard continued training. If that replicates, it suggests a cheaper adaptation path than retraining from scratch, but the evidence is still a single lab experiment.

## What to watch

Watch for independent replications and any code or implementation release from Google Research that would let teams test DCA on their own models.

## Further reading

- [Supercharging transformer residual connections](https://research.google/blog/supercharging-transformer-residual-connections/)
- [DeepCrossAttention : Supercharging Transformer Residual ...](https://arxiv.org/html/2502.06785)
- [Supercharging transformer residual connections - Google Research](https://research.google/blog/supercharging-transformer-residual-connections/)
- [[2502.06785] DeepCrossAttention: Supercharging Transformer ...](https://arxiv.org/abs/2502.06785)
- [DeepCrossAttention (DCA): Google Fix for Deep Transformers ...](https://explainx.ai/blog/google-deepcrossattention-transformer-residual-connections-2026)

<div class="community" markdown="1">

## Community discussion: opinion, not evidence

Commenters focused on the retrofit result—one quoted the LM1B perplexity improvement (0.19 vs. 0.02) and said modifying model dimensions mid-training "has a lot of promise"—while another criticized the post's line charts as better suited to bar charts because the methods have no temporal ordering.

</div>

{% endraw %}
