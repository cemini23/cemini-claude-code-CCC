---
title: AOHP — OS-level agent harness on Android (arXiv 2606.23449)
type: source
tags: [source, arxiv, aohp, os-level, android, k123]
keywords: [2606.23449, aosp, agent-native-os, openclaw]
related:
  - concepts/os-level-agent-harness-android.md
  - entities/tools/aohp.md
  - concepts/runtime-harness-interface-adaptation.md
  - concepts/code-as-agent-harness.md
  - concepts/system-scaling-harness-agentic-ai.md
  - sources/brief-k123-dia-agentic-web-aohp-2026-06-23.md
maturity: draft
read_status: read
created: 2026-06-23
updated: 2026-06-25
---

## Relations

- `@concepts/os-level-agent-harness-android.md` — architecture synthesis
- `@entities/tools/aohp.md` — OpenDFM/AOHP repo (Apache-2.0)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | AOHP: An Open-Source OS-Level Agent Harness for Personalized, Efficient and Secure Interaction |
| **Authors** | Zhao et al. (Tsinghua, PKU, HKU) |
| **arXiv** | 2606.23449v1 [cs.AI] |
| **Code** | https://github.com/aohp-os/aohp (Apache-2.0) |
| **Location** | `raw-sources/arxiv-2606.23449-2606-23449v1-aohp-an-open-source-os-level-agent.pdf` |
| **Retrieved** | 2026-06-23 |
| **Read status** | read (three mechanisms, OpenClaw eval) |

## Narrative

**AOHP** (Android Open Harness Project) — AOSP-based **agent-native OS** treating agents as first-class actors.

**Three mechanisms:**
1. **Personalized service composition** — task-level entrances (e.g. unified shopping) vs per-app switching
2. **Efficient agent interfaces** — parallel background execution, structured UI, event streams
3. **Secure information flow** — sandbox sensitive values via information-flow tracking

**Results vs stock Android (OpenClaw agents):** +21.12% completion rate, -51.55% token cost, improved security-policy compliance.

**CCC relevance:** architectural reference for OS-level harness primitives; **CONDITIONAL-GO** laptop (AOSP build heavy); **NO-GO** Cemini prod.

## Snippets

> "AOHP preserves the mature Android software and hardware ecosystem while introducing three agent-oriented system mechanisms."
> — [Source: arxiv-2606.23449-2606-23449v1-aohp-an-open-source-os-level-agent.pdf, retrieved 2026-06-23]
