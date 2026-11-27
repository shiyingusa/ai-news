---
layout: story
lang: en
date: 2026-11-26 06:27:53 -0500
issue: "2026-11-26"
story_id: "nfs2root-12-year-old-pre-auth-root-flaw-reported-in-linux-kernel-nfs-0e01"
permalink: "/2026/11/26/nfs2root-12-year-old-pre-auth-root-flaw-reported-in-linux-kernel-nfs-0e01/"
title: "Nfs2root: 12-year-old pre-auth root flaw reported in Linux kernel NFS server"
dek: "A writeup published on opensec.in under the name \"nfs2root\" (CVE-2026-99362) describes a pre-authentication remote root vulnerability in the Linux kernel's NFS server that the author says went unnoticed for 12 years."
description: "A writeup published on opensec.in under the name \"nfs2root\" (CVE-2026-99362) describes a pre-authentication remote root vulnerability in the Linux kernel's NFS server that the author says went unnoticed for 12 years."
section: "tech-industry"
rank: 18
edition: 0
section_rank: 3
score: 7.0
status: "Released"
source_name: "opensec.in"
source_url: "https://opensec.in/blog/nfs2root-cve-2026-99362"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50647161"
published_at: "2026-11-25T20:35:50+00:00"
tags: ["Linux kernel", "NFS server", "security vulnerability", "remote root", "open-source security"]
topics: ["linux-kernel", "nfs-server", "security-vulnerability", "remote-root", "open-source-security"]
order: "20261126-0-981"
image: "/assets/stories/2026-11-26/nfs2root-12-year-old-pre-auth-root-flaw-reported-in-linux-kernel-nfs-0e01-share.jpg"
art: "/assets/stories/2026-11-26/nfs2root-12-year-old-pre-auth-root-flaw-reported-in-linux-kernel-nfs-0e01.jpg"
thumb: "/assets/stories/2026-11-26/nfs2root-12-year-old-pre-auth-root-flaw-reported-in-linux-kernel-nfs-0e01-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g11c9e2a4bd8e7d61bc05d3f08adb0336f86a89914c1fd26d1aa76b8ec93d144675310560cec09d455b02181d1780d28111afe5c4cf7df2a0929883d681841cf9_1280.jpg", "author": "cookieone", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/technology-network-storage-industry-8118380/", "provider": "Pixabay", "width": 6016, "height": 4016}
---

{% raw %}
<div class="story-lead" markdown="1">

A writeup published on opensec.in under the name "nfs2root" (CVE-2026-99362) describes a pre-authentication remote root vulnerability in the Linux kernel's NFS server that the author says went unnoticed for 12 years. If accurate, an attacker who can reach an exposed NFS service could gain root-level access without first authenticating.

As of the discussion around the report, no proof-of-concept code had been posted and the flaw had not been independently reproduced, so the severity rests on the author's account rather than a public exploit. Commenters reading the report believe it concerns NFS 4.1 and 4.2 rather than all NFS versions, which would narrow the set of affected servers.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** OpenSec's report, which labels the issue CVE-2026-99362, describes a 12-year-old pre-authentication remote root vulnerability in the Linux kernel's NFS server; its detection guidance checks whether nfsd is loaded, whether NFSv4.1 or 4.2 is enabled, and whether port 2049 is reachable on a non-loopback address.
- **Not yet confirmed:** A Hacker News commenter said no proof-of-concept was posted, and another described disabling NFSv4.1/4.2 via /proc/fs/nfsd/versions as a temporary workaround; the report does not provide exploit evidence or a full technical write-up, and independent testing, practical exploitability, and whether that workaround fully closes the issue are unconfirmed.

</div>

## Background

NFS (Network File System) is the long-standing protocol Linux uses to share directories over a network, and the server side of it, `nfsd`, runs inside the kernel itself — so a flaw there sits below authentication and below any userspace service an administrator could restart. The vulnerability, tracked as CVE-2026-99362 and dubbed NFS2ROOT, is an out-of-bounds write involving a sequence buffer bounds check; it is present in kernel releases that do not yet carry the corrected check and resolved in newer ones that do, according to vulnerability trackers. Red Hat's analysis team, in an assessment dated November 19, 2026, listed the flaw against its products and said a fix may be released in the near future, meaning distribution patch coverage is still being worked out.

## Why it matters

Operators running kernel NFS servers that answer NFS 4.1 or 4.2 should treat internet- or tenant-reachable exports as untrusted until their distribution ships a fix, and long-term-support or out-of-support kernels may lag. One commenter described a temporary workaround: stopping the NFS server and restricting the enabled minor versions with `echo "-4.1 -4.2" | sudo tee /proc/fs/nfsd/versions`, noting the change reverts on reboot and should first be checked against clients that actually negotiate those versions.

## What to watch

Watch for kernel updates or distribution advisories referencing CVE-2026-99362, and for a public proof-of-concept or independent reproduction, which would settle the open questions about affected versions and reachability.

## Further reading

- [CVE-2026-99362 - Red Hat Customer Portal](https://access.redhat.com/security/cve/cve-2026-99362)
- [NFS2ROOT (CVE-2026-99362) FAQ: Linux NFS Exposure and Fix](https://watchtowr.com/intelligence/nfs2root-linux-nfs-cve-2026-99362-faq/)
- [CVE-2026-99362 - Vulnerability Details - OpenCVE](https://app.opencve.io/cve/CVE-2026-99362)
- [NFS2ROOT ( CVE - 2026 - 99362 ): pre-auth root in Linux nfsd | OpenSec](https://opensec.in/blog/nfs2root-cve-2026-99362)
- [Nfs2root: A 12-year-old pre-auth remote root in the... | Hacker News](https://news.ycombinator.com/item?id=50647161)

<div class="community" markdown="1">

## Community discussion: opinion, not evidence

Commenters focused on mitigation rather than the flaw's mechanics: one reported running NFSv4 behind spiped, another proposed the version-disable workaround above and checked which clients actually used 4.1 or 4.2 first, and a third pointed out that no proof-of-concept had been published — an assessment of the disclosure, not evidence the bug is harmless. A side thread argued the episode shows AI-assisted code review finding long-lived bugs that human review missed.

</div>

{% endraw %}
