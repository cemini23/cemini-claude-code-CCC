---
title: "Harness–policy co-evolution for safety — bounded self-improvement (CCC K340)"
type: concept
tags: [concept, safety, harness-evolution, co-evolution, policy, k340]
keywords: [2609.02786, SafeEvolve, harness-policy co-evolution, safety alignment, skill bank, HITL]
related:
  - sources/arxiv-safeevolve-harness-policy-co-evolution-2609.02786.md
  - entities/tools/safeevolve.md
  - concepts/skill-misevolution.md
  - concepts/trajectory-driven-safety-harness-evolution.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-09-03_ccc-k337-k341-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-09-03
updated: 2026-09-03
---

## Relations

- `@sources/arxiv-safeevolve-harness-policy-co-evolution-2609.02786.md`
- `@entities/tools/safeevolve.md`
- `@concepts/skill-misevolution.md`
- `@concepts/trajectory-driven-safety-harness-evolution.md`
- `@concepts/bounded-self-refinement-vs-rsi-taxonomy.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-09-03_ccc-k337-k341-sip-ready.md`

## Raw Concept

K340 (SafeEvolve): safety alignment needs **both** harness artifact updates and policy learning from the same trajectory evidence — either alone fails.

## Narrative

**Harness-only** safety artifacts may exceed what a frozen weak policy can follow; **policy-only** alignment under a fixed harness misses emerging failure modes. SafeEvolve compiles trajectory evidence into **bounded, versioned, reversible** harness updates (safety prompt + hierarchical skill bank) while co-training policy via harness-use SFT + harness-augmented RL.

**CCC HITL gates:** co-evolution is **not** unattended `.cursor/skills` auto-write (pairs K237 misevolution, K268 SHE, K162 external eval contract). REFERENCE clone for packaging study; trainer **`wont_wire`**. Distinct from K237 SAFEEVOLVE delete-only repair — broader co-evolution paper; cross-link both.

## Snippets

> "Never auto-evolve federation skills from SafeEvolve trajectories — HITL + external eval before any harness self-write." [Source: CCC K340 policy]
