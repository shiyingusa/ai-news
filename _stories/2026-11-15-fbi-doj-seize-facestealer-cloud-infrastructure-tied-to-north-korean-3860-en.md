---
layout: story
lang: en
date: 2026-11-15 06:00:00 -0500
issue: "2026-11-15"
story_id: "fbi-doj-seize-facestealer-cloud-infrastructure-tied-to-north-korean-3860"
permalink: "/2026/11/15/fbi-doj-seize-facestealer-cloud-infrastructure-tied-to-north-korean-3860/"
title: "FBI, DOJ seize FaceStealer cloud infrastructure tied to North Korean crypto theft"
dek: "The FBI and the Justice Department said they disrupted a North Korean social-engineering campaign they named FaceStealer, seizing cloud infrastructure that contained 900 videos of targeted victims."
section: "tech-industry"
rank: 12
section_rank: 1
score: 8.0
status: "Announced"
source_name: "Tom's Hardware"
source_url: "https://www.tomshardware.com/tech-industry/cyber-security/fbi-disrupts-north-korean-facestealer-campaign-behind-usd5-billion-binance-hack-doj-seizes-facestealer-cloud-infrastructure-containing-900-videos-of-tech-workers-hackers-used-ai-deepfakes-to-steal-usd400-million-and-compromise-open-source-software"
via: null
discussion_url: null
published_at: "2026-11-15T16:30:00+00:00"
tags: ["North Korea cybercrime", "cryptocurrency theft", "FBI/DOJ", "deepfake social engineering", "supply chain security"]
topics: ["north-korea-cybercrime", "cryptocurrency-theft", "fbi-doj", "deepfake-social-engineering", "supply-chain-security"]
order: "20261115-987"
image: "/assets/stories/2026-11-15/fbi-doj-seize-facestealer-cloud-infrastructure-tied-to-north-korean-3860-share.jpg"
art: "/assets/stories/2026-11-15/fbi-doj-seize-facestealer-cloud-infrastructure-tied-to-north-korean-3860.jpg"
thumb: "/assets/stories/2026-11-15/fbi-doj-seize-facestealer-cloud-infrastructure-tied-to-north-korean-3860-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/gcdeb7cd2474e11d2f214a2e66e84d95f71172c041c3c94d031bce2fe0d0062b764d79d5d525047457124bd5119b1c1f3230e685a446f8bcd2f6233f55d6a79b0_1280.jpg", "author": "bsdrouin", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/network-server-system-2402637/", "provider": "Pixabay", "width": 1920, "height": 1080}
---

{% raw %}
<div class="story-lead" markdown="1">

The FBI and the Justice Department said they disrupted a North Korean social-engineering campaign they named FaceStealer, seizing cloud infrastructure that contained 900 videos of targeted victims. According to the FBI, the operation used AI deepfakes, stolen contact lists and personal data, and fake Zoom or Teams meetings to get victims to install malware, then harvested browser sessions and build-system (CI/CD) credentials. The FBI attributes about $400 million in stolen cryptocurrency to the campaign; Tom's Hardware ties it to the Binance heist and describes that hack as taking over $5 billion, most of it frozen or recovered, without reconciling that figure with the FBI's campaign total. The FBI also says the group repeatedly tried to compromise open-source software, mainly JavaScript/npm modules and Rust crates.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** The FBI and DOJ publicly attributed the FaceStealer campaign to North Korea and announced the seizure of cloud infrastructure holding 900 videos of targeted victims, per the DOJ press release and the FBI's IC3 advisory (dated 12 November 2026) that the article cites; the FBI states roughly $400 million in stolen cryptocurrency is tied to the campaign, and describes attackers luring victims to typo-squatted meeting domains and prompting malware-laden "updates."
- **Not yet confirmed:** The headline's $5 billion Binance figure conflicts with the body, which says "over $5 billion" was taken with "most" frozen or recovered, and with the FBI's $400 million total for the campaign — the sources do not reconcile the two numbers or specify how much was actually recovered; the article attributes the 18-month campaign duration only to reporting, and its link between FaceStealer and the March 2026 Axios/NPM compromise is its own inference ("almost certainly"), since the FBI does not name that package.

</div>

## Background

FaceStealer describes a social-engineering method rather than a piece of malware: attackers first take over a person's messaging and video accounts, harvest their contacts, chat history and recorded video, then reuse that material to impersonate colleagues and recruiters convincingly enough to get a real target onto a fake Zoom or Teams call. Two earlier incidents fit that pattern. Tom's Hardware had reported that the Binance intrusion began with fake job interviews and a malicious Homebrew download, and in March 2026 the widely used Axios npm package briefly shipped a remote-access tool after its developer was approached by someone posing as a hiring company — a case the article says matches the FBI's description, though the FBI report does not name Axios.

## Why it matters

The concrete risk lands on developers and crypto teams: the article says the Axios npm compromise began with a developer being approached through a fake job offer, and the FBI says FaceStealer uses such meetings to steal browser sessions and CI/CD credentials. Unsolicited interview invitations that end in a meeting-client "update" should be treated as a supply-chain risk, especially for maintainers of widely used packages.

{% endraw %}
