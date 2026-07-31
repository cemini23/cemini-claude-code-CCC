---
title: Reconstructive agent memory vs verbatim replay
type: concept
tags: [concept, memory, harness, negative-transfer, k230]
keywords: [MemHarness, reconstruct, GRPO, OOD]
related:
  - sources/arxiv-memharness-reconstructed-memory-2607.28272.md
  - entities/tools/memharness.md
  - concepts/selective-experience-memory-harness.md
  - concepts/procedural-memory-transfer-after.md
  - concepts/modular-instruction-memory-learnable-selection.md
  - concepts/agentic-online-rl-self-evolving-systems.md
  - concepts/memory-poisoning-write-execute-forget-lifecycle.md
  - sources/brief-k230-k233-memharness-tycho-agentradio-askchem-2026-07-31.md
maturity: draft
created: 2026-07-31
updated: 2026-07-31
---

## Relations

- `@sources/arxiv-memharness-reconstructed-memory-2607.28272.md`
- `@entities/tools/memharness.md`
- `@concepts/selective-experience-memory-harness.md`
- `@concepts/procedural-memory-transfer-after.md`

## Raw Concept

Should retrieved experiential memory be injected verbatim, or reconstructed for the current decision state?

## Narrative

**Problem:** Semantic relevance ≠ action-level applicability. Verbatim replay causes negative transfer under state mismatch.

**Pattern (MemHarness):** At each step, a policy critiques and **reconstructs** retrieved experience conditioned on present state, then acts. Reconstruction trained end-to-end (GRPO). Improves ALFWorld/WebShop and OOD robustness vs static memory banks.

**Cemini steal:** Before stuffing `hot.md` / claude-mem / prior trajectory snippets into context: rewrite as **state-conditioned guidance**, or drop. Aligns with τ-gated experience memory (selective harness) and AFTER negative-transfer warnings.

**Verdict:** **ADOPT** reconstruct-before-inject. **GO** Apache REFERENCE `.local/adopts/MemHarness`.
