---
layout: story
lang: en
date: 2026-11-19 06:28:09 -0500
issue: "2026-11-19"
story_id: "java4shell-critical-openjdk-flaw-allows-rce-on-avx-512-servers-3797"
permalink: "/2026/11/19/java4shell-critical-openjdk-flaw-allows-rce-on-avx-512-servers-3797/"
title: "Java4Shell: critical OpenJDK flaw allows RCE on AVX-512 servers"
dek: "Calif Research says it has found a critical OpenJDK remote-code-execution flaw, tracked as CVE-2026-114938 and nicknamed Java4Shell, which it rates 9.2 on CVSS 4.0; the report cites vendor scores ranging from 8 to 9.8."
description: "Calif Research says it has found a critical OpenJDK remote-code-execution flaw, tracked as CVE-2026-114938 and nicknamed Java4Shell, which it rates 9.2 on CVSS 4.0; the report cites vendor scores ranging from 8 to 9.8."
section: "tech-industry"
rank: 15
edition: 0
section_rank: 5
score: 7.0
status: "Released"
source_name: "Tom's Hardware"
source_url: "https://www.tomshardware.com/tech-industry/cyber-security/critical-java-vulnerability-puts-millions-of-sites-services-and-devices-at-risk-of-remote-code-execution-triggers-with-64-as-and-an-sign-openjdk-optimization-bug-lets-an-attacker-trigger-it-just-by-inputting-repeated-text"
via: null
discussion_url: null
published_at: "2026-11-19T10:30:00+00:00"
tags: ["Java", "remote code execution", "security vulnerability", "Oracle", "CVE-2026-114938"]
topics: ["java", "remote-code-execution", "security-vulnerability", "oracle", "cve-2026-114938"]
order: "20261119-0-984"
image: "/assets/stories/2026-11-19/java4shell-critical-openjdk-flaw-allows-rce-on-avx-512-servers-3797-share.jpg"
art: "/assets/stories/2026-11-19/java4shell-critical-openjdk-flaw-allows-rce-on-avx-512-servers-3797.jpg"
thumb: "/assets/stories/2026-11-19/java4shell-critical-openjdk-flaw-allows-rce-on-avx-512-servers-3797-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g035d58e886eeb7ec49ac0b875dfb25855e6f29d1616992ce128fc111ce676a34350144196d5f42cbae2fbd1f404fc4ed3f6ca6b571ee34b2291b28d9ed7eb708_1280.jpg", "author": "Akela999", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/electrical-data-center-2476783/", "provider": "Pixabay", "width": 4096, "height": 2160}
---

{% raw %}
<div class="story-lead" markdown="1">

Calif Research says it has found a critical OpenJDK remote-code-execution flaw, tracked as CVE-2026-114938 and nicknamed Java4Shell, which it rates 9.2 on CVSS 4.0; the report cites vendor scores ranging from 8 to 9.8. The bug is a missing bounds check in a hand-written Base64-decoding optimization: an attacker who sends 64 'A' characters followed by an '=' padding character can overwrite adjacent memory on x86-64 chips with AVX-512 VBMI support, which the report identifies as Intel Ice Lake and AMD Zen 4 server parts.

The report says Oracle has fixed the flaw and issued updated Java versions, but bundled Java in Keycloak, Jira, Confluence, Jenkins and PingFederate allowed unauthenticated RCE, while Kafka Broker, Solr, Elasticsearch, Gerrit and Spinnaker were exploitable after authentication. Older CPUs without VBMI are not affected, and the report does not list the specific vulnerable or patched Java versions.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** CVE-2026-114938 — nicknamed Java4Shell by Calif Research, the lab that reported it — is a memory-corruption flaw in OpenJDK's optimized Base64 decoder, publicly disclosed on November 17, 2026, and it only affects x86-64 processors with AVX-512 VBMI support, per Sophos's and Censys's advisories. Oracle has already fixed it and shipped updated Java builds; the reported severity is CVSS 4.0 9.2 (Critical) from the researchers versus CVSS 3.1 8.1 (High) from Oracle, a gap that reflects different scoring scales as well as different assessments.
- **Not yet confirmed:** that any of this is being exploited in the wild, the number of vulnerable systems behind the "millions" framing, the specific list of affected applications (Keycloak, Jira, Confluence, Jenkins and PingFederate unauthenticated; Kafka Broker, Solr, Elasticsearch, Gerrit and Spinnaker post-authentication) and vulnerable container images — all of which rest on Calif's own post — and Calif's claim that an AI bot found the bug for about $200 in tokens. The source material also gives no exact list of affected OpenJDK versions, no timeline for downstream vendor patches, and no independent reproduction beyond the researchers' own demonstration.

</div>

## Background

Base64 is a text encoding used to carry binary data through email, HTML and configuration files, and the flaw sits in a hand-written assembly optimization of OpenJDK's decoder. OpenJDK is the shared codebase that most Java distributions, including Oracle's, derive from, so applications and container images that bundle a Java runtime inherit the issue; the vulnerable path is limited to x86-64 chips exposing AVX-512 VBMI, and Calif says ARM64 systems are not affected.

## Why it matters

Teams running Keycloak, Jira, Confluence, Jenkins or PingFederate on Intel Ice Lake or AMD Zen 4 servers should treat this as an emergency patch: Calif demonstrated unauthenticated remote code execution against default installations of those products, and code execution after login in Kafka Broker, Solr, Elasticsearch, Gerrit and Spinnaker. Because the flaw sits in OpenJDK's Base64 decoding and many containers bundle their own Java runtime, upgrading the host JVM or OS package alone can leave the embedded copy exposed — inventory container images and application-bundled JDKs, while noting that hosts without AVX-512 VBMI are not affected.

## What to watch

Watch for Oracle's and Red Hat's advisories to name the affected and fixed Java builds, and for independent confirmation that the flaw is exploitable in default configurations.

## Further reading

- [Advisory: OpenJDK Base64 Vulnerability - Java4Shell (CVE-2026 ...](https://www.sophos.com/en-us/security-advisories/sophos-sa-20261118-java4shell)
- [Nov 18 Advisory: OpenJDK Remote Code Execution (Java4Shell ...](https://censys.com/advisory/cve-2026-114938/)
- [Java4Shell CVE-2026-114938: Patch Vulnerable OpenJDK ...](https://computingforgeeks.com/java4shell-cve-2026-114938/)
- [Java 4 Shell (CVE-2026-114938): OpenJDK RCE Vulnerability FAQ](https://www.tenable.com/blog/java4shell-cve-2026-114938-frequently-asked-questions-about-openjdk-rce-vulnerability)
- [How to Find, Mitigate, and Patch the Critical Java4Shell Flaw ...](https://blog.qualys.com/vulnerabilities-threat-research/2026/11/17/how-to-find-mitigate-and-patch-the-critical-java4shell-flaw-cve-2026-114938-now)
- [Java4Shell CVE-2026-114938: What You Need to Know](https://blog.checkpoint.com/security/java4shell-cve-2026-114938-check-your-java-services-now/)
- [Java4Shell Flaw (CVE-2026-114938) Enables Pre-Auth RCE in ...](https://thehackernews.com/2026/11/java4shell-cve-2026-114938-enables-pre.html)

{% endraw %}
