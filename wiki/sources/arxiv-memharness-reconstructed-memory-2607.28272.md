---
title: "MemHarness — memory is reconstructed, not replayed"
type: source
tags: [source, arxiv, memory, harness, grpo, k230]
keywords: [2607.28272, MemHarness, reconstructive memory, negative transfer, ALFWorld]
related:
  - concepts/reconstructive-agent-memory-vs-verbatim-replay.md
  - concepts/selective-experience-memory-harness.md
  - concepts/procedural-memory-transfer-after.md
  - concepts/modular-instruction-memory-learnable-selection.md
  - entities/tools/memharness.md
  - sources/brief-k230-k233-memharness-tycho-agentradio-askchem-2026-07-31.md
maturity: draft
created: 2026-07-31
updated: 2026-07-31
---

## Relations

- `@concepts/reconstructive-agent-memory-vs-verbatim-replay.md`
- `@entities/tools/memharness.md`
- `@concepts/selective-experience-memory-harness.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | MemHarness: Memory Is Reconstructed, Not Replayed |
| **Author** | Wu, Fu, Wen, et al. (ZJU / Shanghai AI Lab) |
| **arXiv** | 2607.28272 |
| **Pages** | 20 |
| **Retrieved** | 2026-07-31 |
| **Code** | `KnowledgeXLab/MemHarness` Apache-2.0 (~39MB) — **GO** REFERENCE |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.28272-memharness-memory-is-reconstructed-not-replayed.pdf` |

## Narrative

Verbatim replay of retrieved trajectories causes **negative transfer** when past states diverge from present. MemHarness: retrieve → critique/reconstruct for current state → act; reconstructive skill via GRPO. Beats pure RL + static memory on ALFWorld/WebShop; strong OOD robustness. **ADOPT** reconstruct-before-inject; **GO** Apache clone.
