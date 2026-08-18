---
title: "State-semantic injection (ESTI) pattern (K288)"
type: entity
tags: [entity, pattern, security, embodied-agent, planner-integrity, state-semantic-injection, k288]
keywords: [k288, ESTI, state-semantic injection, planner-state integrity, schema-preserving false evidence]
related:
  - sources/arxiv-esti-state-semantic-injection-2608.16806.md
  - concepts/planner-state-semantic-integrity-attack-surface.md
  - sources/brief-k285-k289-harness-wave-2026-08-18.md
  - briefs/2026-08-18_ccc-handoff-k285-k289-ingest.md
  - concepts/phase1-adopt-wire.md
  - "@cybersecurity-wiki/concepts/esti-state-semantic-injection-stub.md"
maturity: draft
wire_status: policy_wired
created: 2026-08-18
updated: 2026-08-18
---

## Relations

- `@sources/arxiv-esti-state-semantic-injection-2608.16806.md`
- `@concepts/planner-state-semantic-integrity-attack-surface.md`
- `@cybersecurity-wiki/concepts/esti-state-semantic-injection-stub.md`

## Raw Concept

Reusable threat-model pattern extracted from K288 ESTI — planner-state semantic integrity.

## Narrative

The transferable pattern: treat **planner-visible state producers** as an integrity boundary; audit for **schema-preserving false evidence** (no explicit commands — only native semantic values rewritten); distinguish **planning adoption (P-ASR)** from **execution realization (E-ASR)**; focus defenses on **carrier compatibility + representation-level consistency** rather than re-grounding alone; scope claims **conditional on successful state delivery**. **`policy_wired`** — Cybersec-primary; CCC policy awareness only.

**Phase-0:** `scripts/adopt_k288_phase0.sh`
