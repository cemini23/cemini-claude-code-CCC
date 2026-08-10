---
title: "ResidencyRL — Google clinical multi-turn RL harness (closed)"
type: entity
tags: [entity, tool, rl, clinical, google, k260]
keywords: [2608.07418, ResidencyRL, Gemini, GRPO, NO-GO, closed-source]
related:
  - sources/arxiv-residencyrl-simulated-clinical-rl-2608.07418.md
  - concepts/adversarial-curriculum-structured-reward-doc-fidelity.md
  - concepts/harness-native-agent-rl-training.md
  - sources/brief-k260-residencyrl-2026-08-10.md
  - briefs/2026-08-10_ccc-handoff-k260-residencyrl-ingest.md
  - concepts/phase1-adopt-wire.md
maturity: draft
wire_status: wont_wire
created: 2026-08-10
updated: 2026-08-10
---

## Relations

- `@sources/arxiv-residencyrl-simulated-clinical-rl-2608.07418.md`
- `@concepts/adversarial-curriculum-structured-reward-doc-fidelity.md`

## Raw Concept

Phase-0 entity for K260 ResidencyRL (Google DeepMind clinical agent RL).

## Narrative

| Artifact | License / access | Size | Verdict |
|----------|------------------|------|---------|
| ResidencyRL codebase | Closed (Google internal; medical-safety rationale) | n/a | **NO-GO** clone |
| Paper methods | arXiv 2608.07418 | PDF ~5.5MB | **ADOPT** patterns only |

No `.local/adopts/` shelf — authors explicitly decline open-sourcing. Datasets cited (DDxPlus, AMIE Mx, AgentClinic, CRAFT-MD) are third-party benches, not a ResidencyRL drop-in.

**Phase-0:** `scripts/adopt_k260_phase0.sh`

## Phase-1

`wont_wire` runtime. Steal patterns → `@concepts/adversarial-curriculum-structured-reward-doc-fidelity.md` (`policy_wired`).

## Dead Ends

- Do not attempt to reconstruct/train a clinical ResidencyRL clone from the paper alone for Cemini prod.
- Do not treat Gemini Cloud API availability as “code GO.”
