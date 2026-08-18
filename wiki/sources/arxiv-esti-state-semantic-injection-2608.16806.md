---
title: "ESTI — when state becomes an attack surface (state-semantic injection in LLM-driven embodied agents)"
type: source
tags: [source, arxiv, embodied-agent, security, state-semantic-injection, planner-integrity, k288]
keywords: [2608.16806, ESTI, state-semantic injection, planner-state integrity, embodied agents, ESTI-Bench, schema-preserving false evidence]
related:
  - concepts/planner-state-semantic-integrity-attack-surface.md
  - entities/patterns/state-semantic-injection-esti.md
  - concepts/traceable-scholarship-citation-first-generation.md
  - sources/brief-k285-k289-harness-wave-2026-08-18.md
  - briefs/2026-08-18_ccc-handoff-k285-k289-ingest.md
  - "@cybersecurity-wiki/concepts/esti-state-semantic-injection-stub.md"
maturity: draft
created: 2026-08-18
updated: 2026-08-18
---

## Relations

- `@concepts/planner-state-semantic-integrity-attack-surface.md`
- `@entities/patterns/state-semantic-injection-esti.md`
- `@concepts/traceable-scholarship-citation-first-generation.md` — K259 traceable scholarship (conditional-delivery framing)
- `@cybersecurity-wiki/concepts/esti-state-semantic-injection-stub.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | When State Becomes an Attack Surface: State-Semantic Injection in LLM-Driven Embodied Agents |
| **arXiv** | 2608.16806 |
| **Authors** | Jiawei Liu, Jiacheng Guo, Tian Zhang, Yiwei Xu, Juan Wang, Jinlin Fan, Bowen Xiao, Chi Guo (Wuhan University); Hongxin Hu, Keyan Guo (University at Buffalo) |
| **Code** | none public |
| **Retrieved** | 2026-08-18 |

## Narrative

Studies the **downstream, conditional** question after adversarial state delivery to an LLM-driven embodied agent: if exactly one planner-facing state producer is compromised, can a **schema-preserving false record** be adopted by the planner and realized as a targeted final-state consequence?

**ESTI (Environment State-Text Injection)** encodes a preselected adversarial goal as false state evidence over existing and interactable objects, relations, affordances, task-stage constraints, or execution feedback — while leaving the user instruction, planner, and executor unchanged. It does **not** insert explicit competing commands (the prompt-injection trope); it rewrites native semantic values in the planner-visible state records. The adversary is **component-scoped, predicate-local, non-adaptive**.

**ESTI-Bench** evaluates state-to-execution propagation against Vanilla IPI, EIRAD, and BADROBOT across ProgPrompt/VirtualHome, VoxPoser/RLBench, and AI2-THOR/iTHOR. ESTI improves planning-level and execution-level attack success over the strongest baseline by up to **+89.32 and +43.69 pp**, respectively. All ablation settings share **dataset-level groundability** (schema-compatible false evidence only on goals feasible to instantiate with available entities/interactions); under this matched condition, **carrier compatibility and representation-level consistency** strongly affect planning adoption, whereas removing **runtime re-grounding** changes P-ASR/E-ASR by only 1.92/3.85 points.

**Key scope discipline:** the paper characterizes downstream consequences *conditional on successful state delivery*; it neither estimates the probability of obtaining write access nor treats planning deviation as equivalent to physical attack success.

| Verdict | **ADOPT** planner-state integrity threat model: treat planner-visible state producers as an integrity boundary; audit schema-preserving false evidence; distinguish planning adoption vs execution realization. **Cybersec-primary**; CCC policy awareness. No public code → **policy only**. Pairs K259 traceable scholarship, K274 CDH trajectory audit. |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.16806-when-state-becomes-an-attack-surface-state-seman.pdf` |
