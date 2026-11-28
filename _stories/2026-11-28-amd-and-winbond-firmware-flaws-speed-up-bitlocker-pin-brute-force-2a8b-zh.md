---
layout: story
lang: zh
date: 2026-11-28 06:28:04 -0500
issue: "2026-11-28"
story_id: "amd-and-winbond-firmware-flaws-speed-up-bitlocker-pin-brute-force-2a8b"
permalink: "/zh/2026/11/28/amd-and-winbond-firmware-flaws-speed-up-bitlocker-pin-brute-force-2a8b/"
title: "AMD 与 Winbond 固件漏洞让 BitLocker PIN 可被快速暴力破解"
dek: "柏林工业大学（Technische Universität Berlin）的研究者在 arXiv 论文中披露，AMD 负责与非易失存储通信的 fTPM 固件，以及 Winbond 支持 RPMC（回滚保护）的 SPI 闪存芯片…"
description: "柏林工业大学（Technische Universität Berlin）的研究者在 arXiv 论文中披露，AMD 负责与非易失存储通信的 fTPM 固件，以及 Winbond 支持 RPMC（回滚保护）的 SPI 闪存芯片…"
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

柏林工业大学（Technische Universität Berlin）的研究者在 arXiv 论文中披露，AMD 负责与非易失存储通信的 fTPM 固件，以及 Winbond 支持 RPMC（回滚保护）的 SPI 闪存芯片，都存在缺陷：攻击者只要能够物理接触设备，并加装一块低成本转接板，就能让记录解锁失败次数的计数器不增加，从而绕过“连续 32 次尝试后每次需等待 10 分钟”的限制。按正常机制穷举六位数字 PIN 需要约 19 年；Tom's Hardware 称攻击可把这一时间压缩到数天甚至数小时，其标题给出的六位 PIN 数字为 20 天。

研究者在从 Zen 2 到锐龙 AI 5 330 的 AMD 机型上至少验证了其中一种攻击，并推测所有使用 fTPM 的当代 AMD 消费级平台都可能受影响；Winbond 方案则可借电压毛刺读出 HMAC 密钥，该厂商在 SPI 闪存市场约占 25% 份额，因此潜在受影响设备达数百万台。截至报道时，涉事公司均未承诺修复根因漏洞：Winbond 路径只能更换芯片，AMD 路径需通过 AGESA 固件更新、并依赖 OEM 发布 BIOS；微软只是在设置流程中改为建议用户使用六位 PIN 而非四位。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** 柏林工业大学研究团队的论文《Hello Again: Exploiting Replay Protected…》已发布在 arXiv（编号 2611.18126，11 月 13 日），摘要称团队在锁定且加密的真实硬件上完成端到端演示，正常限速下需 69 天才能试出的 4 位 Windows Hello PIN，其装置 40 小时即破解；论文与 Tom's Hardware 的报道都确认，攻击需要接触设备本体。
- **尚未证实：** 受影响设备到底有多少，目前只是按 Winbond 约占 SPI 闪存 25% 市场份额推算出的「数百万台」；「所有现代 AMD 平台均可能受影响」也只是推断，实测只覆盖 Zen 2 到 AI 5 330 机型，Winbond 侧只对两款芯片做了故障注入；「无厂商承诺修复根因、微软仅建议改用六位 PIN」出自论文作者说法与媒体转述，尚不见厂商公开回应或第三方复现；CVE-2026-43613 编号只见于二手报道。两处数字口径也不一致：Tom's Hardware 称六位数字 PIN 的破解时间从 19 年缩短到 20 天，论文摘要给出的则是四位 PIN 从 69 天缩短到 40 小时。

</div>

## 背景

现代 x86 消费级电脑普遍用「固件可信平台模块」（fTPM）代替独立安全芯片：它运行在 CPU 固件里，而记录解锁失败次数的计数器则被加密存放在主板上的 SPI Flash 芯片中（这块芯片同时存放 BIOS 等固件）。按正常设计，BitLocker 允许连续 32 次尝试，之后每次都要等待 10 分钟，因此六位数字 PIN 需约 19 年才能穷举完。TPM 与 SPI 芯片之间的命令靠 HMAC 密钥签名，部分 Winbond 芯片还带有 RPMC 回滚保护，用来防止计数器被篡改或被还原到旧状态——这两道防线正是本次研究攻击的目标。

## 为什么重要

这些攻击针对的正是磁盘加密要防范的场景——设备被偷；对已过保修期的 AMD 或 Winbond 机型，修复要走“AGESA 更新 → OEM 发布 BIOS”这条漫长的链条，而参考 Spectre/Meltdown 时期的经验，旧设备常被厂商跳过，所以这些机器可能长期无法修补。对高风险用户而言，现实可行的缓解手段是把 PIN 改为更长的字母数字口令，但这只能拉长破解时间，并不能消除计数器可被绕过的缺陷；同时论文指出，该问题很可能同样适用于 BitLocker 之外其他基于 fTPM 的磁盘加密方案。

## 后续看点

接下来值得关注的是 AMD 是否会发布包含该缺陷修复的 AGESA 固件，以及各 OEM 厂商是否、何时为受影响的整机（尤其是已过支持期的旧机型）推送相应 BIOS 更新。另一个可查的节点是微软推荐使用六位 PIN 的策略何时真正落实到 Windows 的安装与设置流程中。

## 延伸阅读

- [[2611.18126v1] Hello Again: Exploiting Replay Protected ...](https://arxiv.org/abs/2611.18126v1)
- [Flash chip attack resets TPM lockout to crack BitLocker and ...](https://secnews.co.uk/2026/11/tpm-lockout-reset-rpmc-attack-bitlocker-windows-hello-pins-cve-2026-43613/)
- [AMD Ryzen & Winbond Flaws Cut BitLocker Cracking to 20 Days](https://pro-gamer.gg/amd-winbond-cve-2026-43613-bitlocker-pin-20-days-ryzen-pcs/)

{% endraw %}
