---
title: Reconstructive agent memory vs verbatim replay
type: concept
tags: [concept, memory, harness, negative-transfer, k230]
keywords: [MemHarness, reconstruct, GRPO, OOD]
related:
  - sources/arxiv-agent-memory-poisoning-utility-2608.21230.md
  - sources/arxiv-memharness-reconstructed-memory-2607.28272.md
  - entities/tools/memharness.md
  - concepts/selective-experience-memory-harness.md
  - concepts/procedural-memory-transfer-after.md
  - concepts/modular-instruction-memory-learnable-selection.md
  - concepts/agentic-online-rl-self-evolving-systems.md
  - concepts/memory-poisoning-write-execute-forget-lifecycle.md
  - sources/brief-k230-k233-memharness-tycho-agentradio-askchem-2026-07-31.md
  - concepts/phase1-adopt-wire.md
  - concepts/decision-coupled-hierarchical-agentic-memory.md
  - sources/arxiv-ham-vln-hierarchical-agentic-memory-2607.29600.md
  - concepts/memory-poisoning-content-screening-bound.md
maturity: draft
created: 2026-07-31
updated: 2026-08-25
---

## Relations

- `@sources/arxiv-memharness-reconstructed-memory-2607.28272.md`
- `@entities/tools/memharness.md`
- `@concepts/selective-experience-memory-harness.md`
- `@concepts/procedural-memory-transfer-after.md`
- `@concepts/decision-coupled-hierarchical-agentic-memory.md` — K236 decision-coupled write
- `@sources/arxiv-agent-memory-poisoning-utility-2608.21230.md`

## Raw Concept

Should retrieved experiential memory be injected verbatim, or reconstructed for the current decision state?

## Narrative

**Problem:** Semantic relevance ≠ action-level applicability. Verbatim replay causes negative transfer under state mismatch.

**Pattern (MemHarness):** At each step, a policy critiques and **reconstructs** retrieved experience conditioned on present state, then acts. Reconstruction trained end-to-end (GRPO). Improves ALFWorld/WebShop and OOD robustness vs static memory banks.

**Cemini steal:** Before stuffing `hot.md` / claude-mem / prior trajectory snippets into context: rewrite as **state-conditioned guidance**, or drop. Aligns with τ-gated experience memory (selective harness) and AFTER negative-transfer warnings.

**Verdict:** **ADOPT** reconstruct-before-inject. **GO** Apache REFERENCE `.local/adopts/MemHarness`.

### K236 complement (2026-08-03)

HAM-VLN couples memory **write to the decision turn** (world-graph semantics on same MLLM call as action). Complements reconstruct-before-inject: recent waypoints verbatim in bounded window; older entries retrieved — see `@concepts/decision-coupled-hierarchical-agentic-memory.md`.
