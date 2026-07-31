---
title: Fara — Microsoft computer-use agent models
type: entity
tags: [entity, tool, cua, microsoft, browser, k124]
keywords: [2606.20785, faragen, fara1.5, qwen]
related:
  - sources/arxiv-fara-scalable-cua-environments-2606.20785.md
  - concepts/scalable-cua-training-pipeline.md
  - concepts/cli-anything-agent-native-computer-use.md
  - entities/tools/webwright.md
  - entities/tools/cua.md
maturity: draft
created: 2026-06-24
updated: 2026-07-31
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-ccc-harness.mdc"
---

## Relations

- `@sources/arxiv-fara-scalable-cua-environments-2606.20785.md` — FaraGen1.5 paper
- `@entities/tools/webwright.md` — CCC browser harness (Webwright vs native CUA)

## Raw Concept

Microsoft open-source computer-use agent models + FaraGen data pipeline (arXiv 2606.20785).

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | https://github.com/microsoft/fara |
| **License** | MIT [CONFIRMED — gh api 2026-06-24] |
| **Stars** | ~5900 |
| **Models** | Fara1.5-4B/9B/27B on Azure AI catalog |

**Stack:** FaraGen1.5 env/solver/verifier pipeline → SFT on generated trajectories → native CUA models.

**Phase-0 (K124):** MIT license verified — **PASS**.

**Adoption verdict:** **REFERENCE** — Cemini uses cursor-ide-browser + Webwright for harness verification, not native CUA inference. Steal verifier triple + synthetic environment pattern only.

## Snippets

> "Fara1.5-9B reaches 63.4% on Online-Mind2Web and 86.6% on WebVoyager."
> — [Source: arxiv-2606.20785, retrieved 2026-06-24]
