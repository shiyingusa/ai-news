---
layout: story
lang: en
date: 2026-11-18 12:26:23 -0500
issue: "2026-11-18"
story_id: "quera-and-berkeley-lab-report-180-atom-quantum-dynamics-study-in-nature-5ee6"
permalink: "/2026/11/18/quera-and-berkeley-lab-report-180-atom-quantum-dynamics-study-in-nature-5ee6/"
title: "QuEra and Berkeley Lab report 180-atom quantum dynamics study in Nature"
dek: "QuEra Computing and Lawrence Berkeley National Laboratory's NERSC published a Nature study in which QuEra's Aquila analog neutral-atom quantum computer…"
description: "QuEra Computing and Lawrence Berkeley National Laboratory's NERSC published a Nature study in which QuEra's Aquila analog neutral-atom quantum computer…"
section: "chips-compute"
rank: 112
edition: 1
section_rank: 6
score: 7.0
status: "Demonstrated"
source_name: "The Quantum Insider"
source_url: "https://thequantuminsider.com/2026/11/18/quera-berkeley-lab-study-quantum-dynamics-aquila/"
via: null
discussion_url: null
published_at: "2026-11-18T17:03:12+00:00"
tags: ["quantum computing", "neutral atoms", "QuEra", "Nature study", "quantum simulation"]
topics: ["quantum-computing", "neutral-atoms", "quera", "nature-study", "quantum-simulation"]
order: "20261118-1-987"
image: "/assets/stories/2026-11-18/quera-and-berkeley-lab-report-180-atom-quantum-dynamics-study-in-nature-5ee6-share.jpg"
art: "/assets/stories/2026-11-18/quera-and-berkeley-lab-report-180-atom-quantum-dynamics-study-in-nature-5ee6.jpg"
thumb: "/assets/stories/2026-11-18/quera-and-berkeley-lab-report-180-atom-quantum-dynamics-study-in-nature-5ee6-640.jpg"
photo_credit: {"url": "https://pixabay.com/get/g0b5b24776bfa417809bacabc0293b6db7b22afabcfd64df1beae9568d312b65cae2c9c123602534b8c10c4768fbc9b27636f4ac24076de872adc6e4b1fb58b92_1280.jpg", "author": "TheDigitalArtist", "licence": "Pixabay Content License", "licence_url": "https://pixabay.com/service/license-summary/", "source_url": "https://pixabay.com/photos/quantum-computer-processor-computer-3679893/", "provider": "Pixabay", "width": 3500, "height": 1969}
---

{% raw %}
<div class="story-lead" markdown="1">

QuEra Computing and Lawrence Berkeley National Laboratory's NERSC published a Nature study in which QuEra's Aquila analog neutral-atom quantum computer — a machine that evolves atoms under a programmable laser field rather than running discrete gate operations — was used to observe how quantum systems settle after a sudden change, with arrays of up to 180 atoms (chains of up to 52 atoms and two-dimensional grids of up to 180). The experiments, accessed through Amazon Braket, showed long-lived prethermal states, the breakdown of those patterns at sharp, predictable "resonant melting" points, and in two dimensions a first-order dynamical phase transition the authors say has no direct equilibrium counterpart.

Exact classical calculations on NERSC's Perlmutter supercomputer, written with QuEra's open-source Bloqade software, validated Aquila's output on small systems before the team relied on it at larger sizes. The paper reports peer-reviewed physics from an analog simulator that has been commercially available on Braket since 2022; it claims no speedup over classical methods, and co-author Milan Kornjača describes fault-tolerant machines as the route to exploring beyond analog constraints.

</div>

<div class="fact-check" markdown="1">

## Verified and unconfirmed

- **Verified:** A peer-reviewed paper in Nature, listed there as "Observation of prethermal dynamical phase transitions and…" (article page dated Nov 4, 2026), reports quench-dynamics experiments on a programmable neutral-atom simulator with up to 180 qubits, observing prethermal dynamical phase transitions and resonant melting; QuEra and NERSC/Berkeley Lab announced the result in a press release dated Nov 18, 2026 (also carried by HPCwire), stating that NERSC used its Perlmutter supercomputer and QuEra's open-source Bloqade software for exact small-system checks and ran Aquila through Amazon Braket.
- **Not yet confirmed:** That the two-dimensional transition genuinely has "no equilibrium counterpart," that the observed behavior outruns classical simulation at the 180-atom scale, and the framing of this as a step toward fault-tolerant machines are the authors' interpretations and forward-looking claims, not independently replicated results — classical validation covered only small probing systems, and the press materials give no independent benchmark against state-of-the-art classical methods at large array sizes. The sources also do not explain the gap between the Nature listing date (Nov 4, 2026) and the announcement date (Nov 18, 2026).

</div>

## Background

Aquila is QuEra's analog neutral-atom machine: rather than running gate sequences, it arranges individual atoms in a laser-defined array and lets their quantum state evolve under a controllable field, then measures the result. It has been offered through Amazon Braket since 2022 as that service's first neutral-atom quantum computer, which is why outside groups such as NERSC can rent time on it for their own experiments. The phenomenon at the center of the study, a quench, is a sudden change in a system's parameters after which it settles into a new state; prethermalization describes the long-lived intermediate patterns that appear before that settling completes.

## Why it matters

The practical consequence is a reusable validation template for research groups: design analog schedules with QuEra's open-source Bloqade, check small systems against exact classical calculations on NERSC's Perlmutter, then scale to arrays of up to 180 atoms on Aquila via Amazon Braket. That template applies to today's analog machine; QuEra's roadmap targets its first fault-tolerant system, Libra, for 2028 on Amazon Braket, so teams should not read this result as evidence of an error-corrected advantage.

## Further reading

- [Observation of prethermal dynamical phase transitions and ...](https://www.nature.com/articles/s41586-026-11225-9)
- [QuEra Computing and Lawrence Berkeley National Laboratory ...](https://www.prnewswire.com/news-releases/quera-computing-and-lawrence-berkeley-national-laboratory-publish-nature-study-of-quantum-dynamics-on-up-to-180-qubits-302943182.html)
- [QuEra and Berkeley Lab Publish Nature Study of Quantum ...](https://www.hpcwire.com/off-the-wire/quera-and-berkeley-lab-publish-nature-study-of-quantum-dynamics-on-up-to-180-qubits/)
- [Fault-Tolerant Quantum Computing Roadmap: Libra 2028 | QuEra](https://www.quera.com/our-quantum-roadmap)
- [QuEra Updates Neutral-Atom Quantum Roadmap with 2028 Fault ...](https://quantumcomputingreport.com/quera-updates-neutral-atom-quantum-roadmap-with-2028-fault-tolerant-launch-on-amazon-braket/)

{% endraw %}
