---
layout: story
lang: en
date: 2026-11-19 06:28:00 -0500
issue: "2026-11-19"
story_id: "ruby2hell-reported-pre-auth-rce-in-stock-rails-7fa0"
permalink: "/2026/11/19/ruby2hell-reported-pre-auth-rce-in-stock-rails-7fa0/"
title: "Ruby2ßhell: reported pre-auth RCE in stock Rails"
dek: "A public write-up dubbed Ruby2ßhell claims a pre-authentication remote code execution vulnerability in stock Ruby on Rails, tied to a single-byte overflow in ß case conversion."
description: "A public write-up dubbed Ruby2ßhell claims a pre-authentication remote code execution vulnerability in stock Ruby on Rails, tied to a single-byte overflow in ß case conversion."
section: "tech-industry"
rank: 11
edition: 0
section_rank: 1
score: 7.0
status: "Announced"
source_name: "verialabs.com"
source_url: "https://verialabs.com/ruby2shell/"
via: "Hacker News"
discussion_url: "https://news.ycombinator.com/item?id=50556287"
published_at: "2026-11-19T05:09:11+00:00"
tags: ["Ruby on Rails", "pre-auth RCE", "vulnerability disclosure", "case conversion", "memory safety"]
topics: ["ruby-on-rails", "pre-auth-rce", "vulnerability-disclosure", "case-conversion", "memory-safety"]
order: "20261119-0-988"
image: "/assets/stories/2026-11-19/ruby2hell-reported-pre-auth-rce-in-stock-rails-7fa0-share.jpg"
art: "/assets/stories/2026-11-19/ruby2hell-reported-pre-auth-rce-in-stock-rails-7fa0.jpg"
thumb: "/assets/stories/2026-11-19/ruby2hell-reported-pre-auth-rce-in-stock-rails-7fa0-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g5fbfb36ee17d6bb86e2877b1f88ee4149eeb53494f2ce44d785333a85abe1f2ffa58e79c1776647d6057bb2bbf3aa3eb460da8a6b6cf98b1e8988017104724a0_1280.jpg", "author": "cookieone", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/technology-network-storage-industry-8118380/", "provider": "Pixabay", "width": 6016, "height": 4016}
---

{% raw %}
<div class="story-lead" markdown="1">

A public write-up dubbed Ruby2ßhell claims a pre-authentication remote code execution vulnerability in stock Ruby on Rails, tied to a single-byte overflow in ß case conversion. Commenters discussing the post describe a Windows-1252 path: ß has no uppercase form in that encoding, so upcasing expands it to "SS" and adds a byte, potentially overrunning a buffer whose headroom check assumes case conversion preserves length. The claim is a blog-level disclosure, not an official Rails advisory, and commenters note that an existing Ruby advisory already covers six other vulnerabilities.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** The Ruby core team rates a heap-based buffer overflow in Ruby's string case conversion as critical, tracked as CVE-2026-132825 and dubbed "ruby2ßhell"; it says changing the case of a crafted string may allow remote code execution, that proof-of-concept exploits can trigger code execution in some scenarios, and that patched versions have been released, per Cybersecurity News and Orca Security.
- **Not yet confirmed:** That the flaw gives pre-authentication RCE on stock, unmodified Rails applications — that framing comes from the Veria Labs blog post rather than the CVE description — along with the specific fixed version numbers and any independent reproduction; commenters also note the write-up overlaps substantially with a separate Ruby advisory covering six other vulnerabilities.

</div>

## Background

Ruby's built-in string methods such as `upcase` can change a string's length in some encodings — the German ß becomes "SS" — so code that reserves buffer space before converting can end up one byte short. On 2026-11-18 the Ruby project published an advisory covering seven vulnerabilities in its regular expression engine and in string case conversion, stating that proof-of-concept code exists for some of them. Commenters on this disclosure note that the flaw described here falls within that advisory's scope rather than being a separate issue.

## Why it matters

Rails teams should inventory endpoints that upcase or downcase user-supplied strings in Windows-1252 and monitor for an official advisory; the public discussion does not identify affected versions or a patch.

## What to watch

Watch for an official Ruby on Rails security advisory or CVE assignment that confirms affected versions, reproduces the pre-authentication path, and names a patched release.

## Community discussion

Commenters are divided on novelty and exploitability: one argues that AI-assisted research is turning single-byte overflows into full RCE reports, while another says the issue is already covered by an existing Ruby advisory that lists six other vulnerabilities. Another commenter calls a one-byte overflow to RCE "definitely achievable" but "tough," and a further reply notes that codepoints such as ffi can expand to three codepoints.

## Coverage of this story

- 2026-11-18 · ruby-lang.org: [Multiple vulnerabilities in Regexp and String case conversion](https://www.ruby-lang.org/en/news/2026/11/18/multiple-vulnerabilities-in-regexp-and-string/)
- 2026-11-19 · verialabs.com: [Ruby2ßhell: Pre-authentication RCE on stock Rails](https://verialabs.com/ruby2shell/)

## Further reading

- [Security advisories: multiple vulnerabilities in Regexp and ...](https://www.ruby-lang.org/en/news/2026/11/18/multiple-vulnerabilities-in-regexp-and-string/)
- [ruby2ßhell: Critical One-Byte Heap Overflow in Ruby Could ...](https://cybersecuritynews.com/ruby2shell-rce/)
- [Ruby2ßhell: Pre-authentication RCE on stock Rails | Hacker News](https://news.ycombinator.com/item?id=50556287)
- [ruby2ßhell: CVE-2026-132825 Ruby Heap Overflow RCE](https://orca.security/resources/blog/ruby2shell-ruby-heap-overflow-rce/)

{% endraw %}
