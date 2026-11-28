---
layout: story
lang: en
date: 2026-11-28 06:26:46 -0500
issue: "2026-11-28"
story_id: "amd-and-winbond-firmware-flaws-speed-up-bitlocker-pin-brute-force-2a8b"
permalink: "/2026/11/28/amd-and-winbond-firmware-flaws-speed-up-bitlocker-pin-brute-force-2a8b/"
title: "AMD and Winbond firmware flaws speed up BitLocker PIN brute-force attacks"
dek: "Researchers at Technische Universität Berlin found firmware vulnerabilities in AMD's fTPM (firmware trusted platform module) storage handling and in Winbond SPI flash chips with RPMC (replay-protected monotonic counter) rollback…"
description: "Researchers at Technische Universität Berlin found firmware vulnerabilities in AMD's fTPM (firmware trusted platform module) storage handling and in Winbond SPI flash chips with RPMC (replay-protected monotonic counter) rollback…"
section: "tech-industry"
rank: 18
edition: 0
section_rank: 2
score: 7.0
status: "Demonstrated"
source_name: "Tom's Hardware"
source_url: "https://www.tomshardware.com/tech-industry/cyber-security/amd-and-winbond-vulnerabilities-let-attackers-brute-force-bitlocker-pins-on-millions-of-pcs-cracking-a-six-digit-pin-drops-from-19-years-to-20-days"
via: null
discussion_url: null
published_at: "2026-11-27T12:30:00+00:00"
tags: ["BitLocker", "hardware security", "AMD", "Winbond", "vulnerability research"]
topics: ["bitlocker", "hardware-security", "amd", "winbond", "vulnerability-research"]
order: "20261128-0-981"
image: "/assets/stories/2026-11-28/amd-and-winbond-firmware-flaws-speed-up-bitlocker-pin-brute-force-2a8b-share.jpg"
art: "/assets/stories/2026-11-28/amd-and-winbond-firmware-flaws-speed-up-bitlocker-pin-brute-force-2a8b.jpg"
thumb: "/assets/stories/2026-11-28/amd-and-winbond-firmware-flaws-speed-up-bitlocker-pin-brute-force-2a8b-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g772f03c3434225907eff143179bd0f1a4424ddf48c01f76918f8c8217e03cd177bc97c9b6f1a92b7f43d787b3a5467e254f1a1d206eefe21cac0986ded5d52b7_1280.jpg", "author": "Magnascan", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/mother-board-electronics-computer-581597/", "provider": "Pixabay", "width": 3264, "height": 2448}
---

{% raw %}
<div class="story-lead" markdown="1">

Researchers at Technische Universität Berlin found firmware vulnerabilities in AMD's fTPM (firmware trusted platform module) storage handling and in Winbond SPI flash chips with RPMC (replay-protected monotonic counter) rollback protection that let an attacker with physical access defeat BitLocker's failed-attempt lockout and brute-force a short PIN much faster. For Winbond, a voltage glitch makes the chip reveal its HMAC key, and a low-cost interposer then impersonates the chip so the failed-attempt counter never rises; the team tested two Winbond models and believes the flaw is in the RPMC engine design.

On AMD systems, the firmware does not verify that the counter increment actually happened, so an attacker can intercept the command without any HMAC key; the researchers verified at least one attack on machines from Zen 2 through an AI 5 330 laptop and suspect all contemporary AMD fTPM consumer hardware is affected. The report says a six-digit numeric PIN that would take 19 years under normal lockout can be broken in about 20 days, potentially affecting millions of PCs, and no vendor has committed to fixing the root causes; Microsoft has only announced a recommendation to use six-digit PINs instead of four during setup.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** Researchers at Technische Universität Berlin published an arXiv paper (2611.18126, "Hello Again: Exploiting Replay Protected…") in which they demonstrate end-to-end, on locked and encrypted hardware, that a low-cost interposer board can suppress or roll back the TPM's failed-attempt counter; their setup recovered a 4-digit Windows Hello PIN in 40 hours instead of 69 days, and the authors state that none of the vendors they contacted had committed to fixing the root-cause vulnerabilities. The attacks require physical access to the machine.
- **Not yet confirmed:** The "millions of PCs" scale rests on the paper's estimate of Winbond's roughly 25% SPI flash market share and on the researchers' theory that the flaw extends across Winbond's lineup and to all contemporary AMD consumer platforms — they verified at least one AMD attack only on machines from Zen 2 through an AI 5 330 laptop. The 20-day six-digit-PIN figure is the researchers' projected brute-force time, not an independently reproduced result, and neither AMD, Winbond, Microsoft nor OEMs have published fix timelines; the reported Microsoft guidance recommending six-digit PINs is described by the article without a linked Microsoft statement. Secondary coverage assigns CVE-2026-43613 to the AMD issue.

</div>

## Background

BitLocker, Microsoft's built-in Windows disk encryption, can lean on the firmware TPM (fTPM) — a trusted-platform-module function implemented in CPU microcode and used by nearly all modern consumer x86 machines — rather than a separate chip. The fTPM keeps its anti-guessing protection in an SPI flash chip on the motherboard: an encrypted counter of failed unlock attempts that triggers a 10-minute wait after 32 successive tries, which is what stretches a short PIN to years of guessing. The new research targets that counter and the channel between the CPU and the flash chip.

## Why it matters

Owners of affected machines cannot rely on BitLocker's 10-minute lockout to stop a thief who has physical access and cheap hardware from guessing a short PIN. The remediation path is uneven: AMD's missing counter check could be fixed in firmware via AGESA, but that requires OEM BIOS updates for devices that may be out of support, while the Winbond flaw can only be fixed by replacing the SPI chip. Microsoft's announced six-digit PIN recommendation does not address the counter bypass.

## What to watch

Watch whether AMD releases an AGESA firmware update that makes its SPI controller actually verify failed-attempt counter writes, and whether OEMs then publish BIOS updates for affected laptops — the same distribution bottleneck that slowed Spectre/Meltdown fixes, since the researchers say no vendor has yet committed to fixing the root cause. Also watch whether Microsoft goes beyond its setup-time recommendation of a six-digit PIN and changes the BitLocker default itself.

## Further reading

- [[2611.18126v1] Hello Again: Exploiting Replay Protected ...](https://arxiv.org/abs/2611.18126v1)
- [Flash chip attack resets TPM lockout to crack BitLocker and ...](https://secnews.co.uk/2026/11/tpm-lockout-reset-rpmc-attack-bitlocker-windows-hello-pins-cve-2026-43613/)
- [AMD Ryzen & Winbond Flaws Cut BitLocker Cracking to 20 Days](https://pro-gamer.gg/amd-winbond-cve-2026-43613-bitlocker-pin-20-days-ryzen-pcs/)
- [AMD CPU fTPM : How to Enable or Disable It](https://www.itechguides.com/amd-cpu-ftpm-enable-or-disable/)

{% endraw %}
