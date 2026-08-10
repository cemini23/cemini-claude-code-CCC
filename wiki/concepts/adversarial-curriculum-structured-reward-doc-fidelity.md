---
title: Adversarial curriculum + structured reward + documentation fidelity (ResidencyRL / K260)
type: concept
tags: [concept, harness, rl, curriculum, rubrics, documentation, safety, k260]
keywords: [2608.07418, ResidencyRL, premature-closure, red-flags, SOAP-hallucination, GRPO, autorater]
related:
  - sources/arxiv-residencyrl-simulated-clinical-rl-2608.07418.md
  - entities/tools/residencyrl.md
  - concepts/harness-native-agent-rl-training.md
  - concepts/agent-rubrics-self-correction.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - concepts/failed-trajectory-harness-repair.md
  - concepts/mcp-claim-validation-and-parameter-grounding.md
  - sources/brief-k260-residencyrl-2026-08-10.md
  - briefs/2026-08-10_ccc-handoff-k260-residencyrl-ingest.md
  - concepts/phase1-adopt-wire.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-10
updated: 2026-08-10
---

## Relations

- `@sources/arxiv-residencyrl-simulated-clinical-rl-2608.07418.md`
- `@entities/tools/residencyrl.md`
- `@concepts/harness-native-agent-rl-training.md`
- `@concepts/agent-rubrics-self-correction.md`
- `@concepts/bounded-self-refinement-vs-rsi-taxonomy.md`

## Raw Concept

How do multi-turn agents avoid premature closure, keep durable notes honest, and train against adversarial users—not only cooperative ones?

## Narrative

K260 ResidencyRL (arXiv **2608.07418**) is clinical OOD, but the harness lessons transfer:

1. **Curriculum packs** — mix routine, information-asymmetric intake, and adversarial scenarios. Friendly-only evals hide premature-closure and safety failures.
2. **Hierarchical structured reward** — primary rubrics (task quality, communication, documentation) **plus** hard safety penalties (hallucinations, contraindications, missed red flags). Soft autoraters alone Goodhart; prefer execution verify when available (pairs K162 hierarchy).
3. **Resist premature termination** — finish required elicitation / safety checks before `terminate`; early stop caused base-model chart hallucination in paper case studies.
4. **Documentation fidelity** — durable artifacts (SOAP-like notes, Discord posts, wiki claims, tool reports) may only contain **elicited or observed** facts. Do not invent fields to satisfy a schema (pairs Traceable Scholarship / K259 claim validation).
5. **Persist on critical protocols despite deflection** — re-ask with rationale when the operator/user dodges a required check (pairs K244 clarify-before-act); do not silently skip.

### Cemini steal (ADOPT)

| # | Rule |
|---|------|
| 1 | Eval / RL / red-team packs include adversarial + information-asymmetric cases, not only happy-path. |
| 2 | Score long-horizon agents with rubrics **and** hard safety/fidelity penalties. |
| 3 | Gate `done`/terminate on required-check coverage — not vibes. |
| 4 | Never fabricate unobserved facts into durable state to fill templates. |
| 5 | Required clarifications: persist once with rationale; then refuse/escalate — do not invent answers. |

| Verdict | **ADOPT** policy. Clinical ResidencyRL code **NO-GO** / `wont_wire`. |
