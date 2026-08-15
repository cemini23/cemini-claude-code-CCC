---
title: Trajectory-driven safety harness evolution (SHE / K265)
type: concept
tags: [concept, safety, harness, evolution, k265]
keywords: [2608.09885, SHE, Rule-Bank, Safety-Memory, Tool-Policy, attribution]
related:
  - sources/arxiv-she-safety-harness-evolution-2608.09885.md
  - entities/tools/she-safety-harness.md
  - concepts/failed-trajectory-harness-repair.md
  - concepts/etclovg-harness-layers.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - sources/brief-k261-k265-harness-wave-2026-08-11.md
  - briefs/2026-08-11_ccc-handoff-k261-k265-ingest.md
  - concepts/phase1-adopt-wire.md
  - concepts/skill-misevolution.md
  - sources/arxiv-skill-misevolution-2608.12851.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-11
updated: 2026-08-15
---

## Relations

- `@sources/arxiv-she-safety-harness-evolution-2608.09885.md`
- `@entities/tools/she-safety-harness.md`
- `@concepts/failed-trajectory-harness-repair.md`
- `@concepts/etclovg-harness-layers.md`

## Raw Concept

How do we evolve safety harness artifacts from failure trajectories without coupling all responsibilities into one blob?

## Narrative

SHE four artifacts: **System Prompt · Rule Bank · Safety Memory · Tool Policy**. Attribution routes failures to the smallest responsible artifact; retain only safety–utility validated edits.

### Steal (ADOPT)

1. Name which harness artifact owns a failure before editing (pairs ETCLOVG / HarnessFix).
2. Bounded artifact-local edits + validation — not free-form prompt soup.
3. **HITL gate** before mutating prod Cursor/Claude harnesses — no unattended closed loop rewriting pass criteria (K162).

| Verdict | **ADOPT** + Apache REFERENCE clone. Runtime auto-evolve **wont_wire**. |
