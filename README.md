# AI Daily Radar

Source code for **[aidailyradar.com](https://aidailyradar.com)**, a daily, bilingual (English first, Chinese second) briefing of the most important AI news.

Every day a GitHub Actions job:

1. Collects AI news from AI labs, tech media, newsletters, Hacker News, Reddit, GitHub, Google News and Chinese AI media.
2. Scores every item with an LLM against the `ai-news` rubric (`profiles/ai-news/`) and drops anything that is not primarily about AI.
3. Deduplicates stories, writes a summary, background and impact for each selected item in English and Chinese.
4. Publishes the result to the Jekyll site in `docs/` via the `gh-pages` branch.

## Where things live

| What | Path |
|---|---|
| Sources, model, languages, limits | `data/config.github.json` |
| AI news scoring and writing rules | `profiles/ai-news/` |
| Website (homepage, about, privacy, styles) | `docs/` |
| Site settings, including the AdSense ID | `docs/_config.yml` |
| Daily schedule | `.github/workflows/daily-summary.yml` |
| Site-only redeploy on push | `.github/workflows/deploy-site.yml` |
| Upstream engine documentation | `horizon-docs/` |

## Required GitHub secret

| Secret | Purpose |
|---|---|
| `DEEPSEEK_API_KEY` | LLM used for scoring and writing (change `ai` in `data/config.github.json` to use another provider) |

## Credits

Built on [Horizon](https://github.com/Thysrael/Horizon) by Thysrael, used under the MIT License (see `LICENSE`).
