---
title: "Planner-state semantic integrity attack surface (K288)"
type: concept
tags: [concept, embodied-agent, security, planner-integrity, state-semantic-injection, k288]
keywords: [2608.16806, ESTI, state-semantic injection, planner-state integrity, schema-preserving false evidence, embodied agents]
related:
  - sources/arxiv-esti-state-semantic-injection-2608.16806.md
  - entities/patterns/state-semantic-injection-esti.md
  - concepts/traceable-scholarship-citation-first-generation.md
  - entities/patterns/convergent-detour-hijacking.md
  - sources/brief-k285-k289-harness-wave-2026-08-18.md
  - briefs/2026-08-18_ccc-handoff-k285-k289-ingest.md
  - concepts/phase1-adopt-wire.md
  - "@cybersecurity-wiki/concepts/esti-state-semantic-injection-stub.md"
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-18
updated: 2026-08-18
---

## Relations

- `@sources/arxiv-esti-state-semantic-injection-2608.16806.md`
- `@entities/patterns/state-semantic-injection-esti.md`
- `@concepts/traceable-scholarship-citation-first-generation.md` — K259 conditional-delivery framing
- `@entities/patterns/convergent-detour-hijacking.md` — K274 CDH trajectory audit
- `@cybersecurity-wiki/concepts/esti-state-semantic-injection-stub.md`

## Raw Concept

An LLM-driven embodied agent reads environment state (objects, relations, affordances, task-stage rules, feedback) as trusted planning evidence. What if one compromised state producer injects schema-preserving false records — no explicit commands — and the planner adopts them as facts?

## Narrative

ESTI (arXiv 2608.16806) treats the **planner-facing state interface as an integrity boundary** between perception, planning, and execution. The attack is **state-semantic injection**: encode a preselected adversarial goal as false state evidence over *existing and interactable* objects/relations/affordances/constraints/feedback — leaving user instruction, planner, and executor untouched. No explicit competing commands (the prompt-injection trope); only native semantic values are rewritten.

### Steal (ADOPT — threat-model pattern)

1. **Planner-visible state producers are an integrity boundary.** Every component that emits state the planner reads (scene description, object attributes, spatial relations, affordances, task-phase rules, execution feedback) is a trust boundary — compromise of exactly one can steer planning.
2. **Schema-preserving false evidence beats explicit commands.** False records must conform to the semantic role + representation format of the compromised field to be adopted; an explicit competing command is easier to reject. Defense must audit *consistency across records*, not just look for injected instructions.
3. **Distinguish planning adoption from execution realization.** P-ASR (planner adopts the adversarial predicate) ≠ E-ASR (predicate becomes true after execution). Treat them as separate metrics; planning deviation is not the same as physical attack success.
4. **Carrier compatibility + representation-level consistency drive adoption.** Under matched dataset-level groundability, those two properties strongly affect whether false evidence is adopted — whereas removing runtime re-grounding barely moves P-ASR/E-ASR (+1.92/+3.85 pts). Defenders should focus on carrier/representation consistency checks, not re-grounding alone.
5. **State delivery is conditional — don't overclaim.** ESTI-Bench characterizes consequences *conditional on successful state delivery*; it does not estimate the probability of write access. Scope the threat model precisely (pairs K259 traceable scholarship).

### Why this pairs K259 (traceable scholarship) and K274 (CDH)

K259's citation-first / conditional-delivery discipline is exactly the framing ESTI applies to its own results (conditional on delivery, no write-access estimate). K274's convergent-detour-hijacking is the digital-agent counterpart: both exploit the planner's trust in an intermediate artifact (skill registry vs planner-visible state) — ESTI extends the integrity-boundary lesson to embodied execution.

### Local adopt

- **No clone** — no public code. **Policy only.** Cybersec-primary stub; CCC keeps policy awareness.

| Verdict | **ADOPT** treat planner-visible state producers as integrity boundaries; audit schema-preserving false evidence; distinguish planning adoption vs execution realization. `policy_wired`; Cybersec-primary. |
