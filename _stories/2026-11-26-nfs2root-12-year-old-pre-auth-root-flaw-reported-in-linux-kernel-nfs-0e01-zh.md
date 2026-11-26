---
layout: story
lang: zh
date: 2026-11-26 06:28:37 -0500
issue: "2026-11-26"
story_id: "nfs2root-12-year-old-pre-auth-root-flaw-reported-in-linux-kernel-nfs-0e01"
permalink: "/zh/2026/11/26/nfs2root-12-year-old-pre-auth-root-flaw-reported-in-linux-kernel-nfs-0e01/"
title: "Linux 内核 NFS 服务器被指存在潜伏 12 年的预认证远程 root 漏洞"
dek: "一份公开报告称，Linux 内核的 NFS 服务器中存在编号为 CVE-2026-99362 的预认证远程 root 漏洞，即攻击者无需先通过身份认证即可触达该缺陷，且该缺陷据称已在代码中潜伏约 12 年。"
description: "一份公开报告称，Linux 内核的 NFS 服务器中存在编号为 CVE-2026-99362 的预认证远程 root 漏洞，即攻击者无需先通过身份认证即可触达该缺陷，且该缺陷据称已在代码中潜伏约 12 年。"
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

一份公开报告称，Linux 内核的 NFS 服务器中存在编号为 CVE-2026-99362 的预认证远程 root 漏洞，即攻击者无需先通过身份认证即可触达该缺陷，且该缺陷据称已在代码中潜伏约 12 年。报告未随附可运行的利用代码，讨论中也有评论者指出目前没有公开的概念验证（PoC），因此该漏洞的实际可利用性尚未得到独立验证。报道没有给出受影响的完整内核版本区间和修复提交清单；评论者根据报告内容称，问题只涉及 NFS 4.1 及 4.2 以上协议版本，并据此提出临时缓解办法。

</div>

<div class="fact-check" markdown="1">

## 已证实与未证实

- **已证实：** 据 OpenSec 博客（CVE-2026-99362），Linux 内核内置的 NFS 服务器 nfsd 存在一个据称潜伏约 12 年的预认证远程 root 漏洞；该文给出的受影响条件是 nfsd 已加载（lsmod | grep -w nfsd）、启用了 NFSv4.1 或 4.2（cat /proc/fs/nfsd/versions 显示 +4.1/+4.2），且 2049 端口可从非回环地址访问。Hacker News 讨论中，有运维者据此做临时缓解，例如 superkuh 将 "-4.1 -4.2" 写入 /proc/fs/nfsd/versions 关闭这两个次版本（重启后失效）。
- **尚未证实：** 目前没有公开的 PoC 或利用代码（评论者 gsich 指出“no poc posted”），也无独立复现或实测结果；现有报道未包含上游内核补丁提交、发行版安全公告或 CVE 官方记录，因此确切受影响的内核版本范围、修复版本，以及“预认证即可取得 root”的实际可利用性，目前仍只有该博客一方说法。另有一条搜索结果讲的是另一个 NFSv4 漏洞 CVE-2026-31402（NFSv4.0 LOCK 重放缓存堆溢出），与本案无关，不能作为佐证。

</div>

## 背景

NFS(Network File System)是 Linux 内核内置的网络文件系统，其服务端 nfsd 直接运行在内核态而非用户空间守护进程，因此 nfsd 中的内存破坏漏洞一旦可被远程触发，影响面覆盖所有启用该服务的机器，且不受普通应用层沙箱约束。据 watchtowr 的漏洞 FAQ 归类，编号 CVE-2026-99362 的问题属于 NFS 中的越界写（out-of-bounds write）；OpenCVE 的记录显示，凡是包含存在缺陷的 nfsd 组件、尚未加入更新后序列缓冲区边界检查的内核版本都可能受影响，较新的内核版本已包含修复。Red Hat 客户门户于 2026 年 11 月 19 日登记该 CVE，并把相关产品标为“Affected”，即其分析团队已确认受此漏洞影响、修复可能在不久后发布。

## 为什么重要

对把 NFS 服务暴露在不可信网络上的运维者来说，问题不在于漏洞是否已被利用，而在于修复路径：在补丁回溯到所用内核（尤其是已停止支持的发行版）之前，只能靠降低攻击面来过渡。评论者给出的一个具体做法是先停掉 nfs-server，再执行 `echo "-4.1 -4.2" | sudo tee /proc/fs/nfsd/versions` 关闭这两个协议版本；该设置重启后即失效，属于临时措施，而且需要先确认客户端确实没有使用 4.1/4.2。另有评论者称自己在 NFSv4 前加了 spiped 隧道从而认为不受影响，这属于个人判断，报告并未确认隧道能阻断该路径。

## 后续看点

值得跟踪的是主流发行版内核是否发布对应修复提交与稳定版回溯，以及是否出现公开的 PoC 或独立复现报告——这两者会决定该漏洞从“已披露”变成“可被实际利用”的时间窗。

## 社区讨论

讨论集中在缓解手段而非漏洞本身：superkuh 认为关闭 NFS 4.1/4.2 是当下可行的临时方案，aidenn0 则推测用 spiped 隧道包裹 NFSv4 就安全，r3tr0 声称可用基于 XDP 的 L7 防火墙规则拦截并给出了仓库链接——这些均为评论者自述，未经独立验证。gsich 则直指关键限制：没有公开 PoC。另有评论者借此事讨论 AI 辅助代码审计对开源项目漏洞发现速度的影响。

## 延伸阅读

- [CVE-2026-99362 - Red Hat Customer Portal](https://access.redhat.com/security/cve/cve-2026-99362)
- [NFS2ROOT (CVE-2026-99362) FAQ: Linux NFS Exposure and Fix](https://watchtowr.com/intelligence/nfs2root-linux-nfs-cve-2026-99362-faq/)
- [CVE-2026-99362 - Vulnerability Details - OpenCVE](https://app.opencve.io/cve/CVE-2026-99362)
- [NFS2ROOT ( CVE - 2026 - 99362 ): pre-auth root in Linux nfsd | OpenSec](https://opensec.in/blog/nfs2root-cve-2026-99362)
- [#linux # cve # nfsv 4 #kernelsecurity #freebsd #sysadmin #infosec...](https://www.linkedin.com/posts/azbest_linux-cve-nfsv4-activity-7450057323148009473-aq_e)
- [Nfs2root: A 12-year-old pre-auth remote root in the... | Hacker News](https://news.ycombinator.com/item?id=50647161)

{% endraw %}
