---
title: Skill misevolution — practice can make skills worse (board K237)
type: concept
tags: [concept, skills, safety, she, lifecycle, k237]
keywords: [2608.12851, SAFEEVOLVE, authoring, retrieval, execution, HITL, dual-id]
related:
  - sources/arxiv-mediskill-evo-process-constrained-2608.23397.md
  - concepts/process-constrained-self-evolution.md
  - concepts/rlm-continual-harness.md
  - sources/arxiv-skill-misevolution-2608.12851.md
  - concepts/harness-policy-co-evolution-safety.md
  - sources/arxiv-safeevolve-harness-policy-co-evolution-2609.02786.md
  - entities/tools/safeevolve.md
  - entities/tools/she-safety-harness.md
  - entities/skills/route.md
  - entities/skills/skill-set-budget.md
  - sources/brief-k237-meta-harness-vero-misevolution-2026-08-14.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - concepts/phase1-adopt-wire.md
  - concepts/repo-level-verified-code-proof-eval.md
  - concepts/skill-set-selection-under-budget.md
  - sources/arxiv-k244-harness-skill-selection-cluster.md
  - sources/arxiv-prime-agent-rlm-harness-2608.23552.md
  - concepts/vague-goal-self-evolution.md
  - sources/arxiv-aspire-vague-goal-self-evolution-2608.31111.md
  - concepts/trajectory-driven-safety-harness-evolution.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-15
updated: 2026-09-03
---

## Relations

- `@sources/arxiv-skill-misevolution-2608.12851.md`
- `@concepts/trajectory-driven-safety-harness-evolution.md`
- `@entities/tools/she-safety-harness.md`
- `@entities/skills/route.md`
- `@sources/brief-k237-meta-harness-vero-misevolution-2026-08-14.md`
- `@sources/arxiv-mediskill-evo-process-constrained-2608.23397.md`
- `@concepts/process-constrained-self-evolution.md`
- `@concepts/rlm-continual-harness.md`
- `@concepts/vague-goal-self-evolution.md`
- `@sources/arxiv-aspire-vague-goal-self-evolution-2608.31111.md`

## Raw Concept

Does HITL on a skill **write** protect later sessions, or can retrieval still activate an unsafe span after "successful" practice?

## Narrative

Board K237 / arXiv 2608.12851: evolved skill configs can author unsafe artifacts (brief: 21/21) and retain fresh-session harm (15). A terminal success-rate is not a library-safety metric.

### Steal (ADOPT — already policy_wired)

1. **Govern three gates:** authoring (CU/UG/Stealth), retrieval (URR), execution (C-ASR).
2. **HITL on write ≠ retrieval-time safety** — keep retrieval lineage; retire on evidenced harm.
3. **Prefer delete-only repair + reuse-time attribution** (SAFEEVOLVE: retire after 2 harmful reuses, library cap).
4. **No unattended auto-evolve** of `.cursor/skills/*` (pairs SHE HITL / K162). Wired in `/route` skill v2.3.3 rule 10.

**Dual-ID:** ACCEL is also **K237** in `cemini-phase1-policy-wires.mdc`. This page = 2608.12851. AutoDesign/Vero in the same board brief are CCC **K281 / K280**.

| Verdict | **ADOPT** lifecycle gates. Runtime `wont_wire` (no SAFEEVOLVE product). |
