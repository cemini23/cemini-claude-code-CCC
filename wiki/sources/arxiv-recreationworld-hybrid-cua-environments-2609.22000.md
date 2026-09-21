---
title: "RecreationWorld: Scalable and Verifiable Environments for Hybrid Computer-Use Agents (CCC K375)"
type: source
tags: [source, arxiv, k375]
keywords: [2609.22000, k375]
related:
  - concepts/hybrid-cua-recreation-environments.md
  - briefs/2026-09-21_ccc-k373-k375-sip-ready.md
  - concepts/hybrid-gui-cli-agent-environment.md
maturity: draft
read_status: read
created: 2026-09-21
updated: 2026-09-21
---

## Relations

- `@concepts/hybrid-cua-recreation-environments.md`
- `@briefs/2026-09-21_ccc-k373-k375-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | RecreationWorld: Scalable and Verifiable Environments for Hybrid Computer-Use Agents |
| **arXiv** | 2609.22000 (2026-09) |
| **Retrieved** | 2026-09-21 |

## Narrative

**Verdict: ADOPT eval-first.**

**Hybrid CUAs** interleave GUI exploration, code implementation, and visual verification — neither GUI-only nor terminal-only agents suffice. **Recreation** task: given a running reference app, discover behavior and build a faithful implementation (reference = oracle for hidden behavioral tests). **RECREATIONWORLD**: five-platform reproducible envs (Ubuntu, macOS, Windows, Android, Web) + unified harness with native GUI control and coding tools. **RECREATIONBENCH**: 250 tasks (50/platform) with programmatic + visual assertions validated on reference then frozen; GPT-6 Astra leads at 58.1% overall but full programmatic pass on only 2.8% of tasks. Training trajectories transfer +17.9 pp on OOD benchmarks. Pairs K348 CUA-Universe hybrid GUI+CLI / K321 ASIL structured actions over screenshots. GitHub/HuggingFace cited — **WATCH** until SPDX verified; no clone at Phase-0. GUI runtime **`wont_wire`** — keep cursor-ide-browser.

## Snippets

> "RecreationWorld: Scalable and Verifiable Environments for Hybrid Computer-Use Agents — CCC K375 synthesis." [Source: arXiv 2609.22000 — paraphrase]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2609.22000-recreationworld-scalable-and-verifiable-environm.pdf` |
