---
lang: en
title: "Editorial Standards"
description: "How AI Daily Radar selects, checks, labels, credits and corrects its stories, and how AI is used to write them."
permalink: /standards/
---

# Editorial Standards

These are the rules every AI Daily Radar story is held to. They are built into the software that writes the site, so they apply to every story, every day.

## How AI is used {#ai-disclosure}

AI Daily Radar is produced with AI assistance. A large language model sorts incoming stories into sections, scores them, merges duplicate reports and writes the summary, background and analysis on each story page, in English and in Chinese. Stories are not reviewed by a human editor before they are published. We do not invent bylines: stories are credited to AI Daily Radar.

What the AI is not allowed to do: invent facts, quotes, dates or figures that are not in the sources; present a company's claims as independently verified; or describe a plan or demo as a shipped product.

## Original sources first {#sources}

Every story names the publisher that originally reported it and links to that report. When we found the story through an aggregator or community (Techmeme, Hacker News, Reddit), the story page says so with a "Found via" line, but the credit and the link go to the original publisher. We prefer primary sources: the company's own announcement, the research paper, the regulator's filing.

We do not republish articles. Our pages carry our own summary and analysis, short enough that the original report stays worth reading.

## Status labels {#status-labels}

Each story carries one label for how far the main development has actually got. The label never goes higher than the source proves.

| Label | Meaning |
|---|---|
| **Rumored** | Reported from unnamed sources or leaks; not confirmed by the company. |
| **Planned** | A stated intention or roadmap item; nothing launched yet. |
| **Announced** | Officially unveiled, but not yet usable or purchasable. |
| **Demonstrated** | Shown working in a demo, test or paper, but not released. |
| **Released** | Shipped to some users, developers or a limited market. |
| **Available** | Generally obtainable by the public. |

## Verified and unconfirmed {#verification}

Most story pages include a "Verified and unconfirmed" box. The first line states what the primary source itself establishes and who says so. The second line lists what rests only on a company's word, unnamed sources, a single report or a demo, and what important detail is missing, such as a price, date or independent test. When sources disagree on a figure, version or date, the box says so instead of picking one silently.

We weigh sources roughly in this order: official primary documents (filings, papers, regulator records, company announcements); established news organizations with their own reporting; specialist trade publications; analysts and newsletters; and community posts, which we use for discussion, not as proof.

## The Radar score {#radar-score}

The number beside each headline (0 to 10) is the model's rating of how important the story is for our readers, scored against a written rubric for its section: is it really about this field, is it new, who is affected, and how credible the source is. Rumors and stock chatter are scored down. Only stories scoring 6.5 or higher (7.0 for Tech Industry & Policy) are published, and each section and source type has a cap so no single topic fills the issue. The score is a ranking aid, not a measure of truth.

## One story per event {#events}

When several outlets report the same event, or different stages of one developing story on the same day, we publish one story and list the other reports under "Coverage of this story".

## Quality checks before publishing {#quality}

Before an issue goes live, each story must have a real headline and a complete summary, and must not contain signs of a failed AI response. Stories that fail are dropped. If too many stories fail on the same day, the whole issue is held back and the previous day's site stays up unchanged.

## Images {#images}

We do not use news organizations' photos. Story images are either licensed photos (Wikimedia Commons under free licenses, or Pixabay and Pexels under their own licenses), credited under the image, or our own generated artwork. We do not edit news photos with AI.

## Corrections {#corrections}

If you find an error, email [{{ site.contact_email }}](mailto:{{ site.contact_email }}) with the story link. When an error is confirmed we correct the story, add a note saying what changed and when, list it in our [corrections log]({{ '/corrections/' | relative_url }}), and change the rule or source that caused it where we can.

## Independence {#independence}

The site may display advertising. Advertisers have no say in which stories are selected, how they are scored or how they are described. We do not accept payment for coverage.
