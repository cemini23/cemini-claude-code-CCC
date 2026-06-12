---
title: SkillHone — continual skill evolution via persistent decision history
type: concept
tags: [concept, skill-evolution, harness, subagent, k111]
keywords: [2606.08671, skillhone, decision-history, redacted-evaluation]
related:
  - sources/arxiv-skillhone-continual-skill-evolution-2606.08671.md
  - concepts/muse-autoskill-skill-lifecycle.md
  - concepts/bayesian-posterior-guided-skill-evolution.md
  - concepts/self-harness-model-specific-improvement-loop.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/skill-vetting.md
  - concepts/ship-subagent-writer-reviewer-tester.md
  - concepts/agent-skills-progressive-disclosure.md
  - entities/mcp-servers/anthropic-skills.md
  - concepts/subagent-orchestration.md
  - entities/tools/hermes-agent.md
maturity: draft
created: 2026-06-12
updated: 2026-06-12
---

## Relations

- `@sources/arxiv-skillhone-continual-skill-evolution-2606.08671.md` — Tencent WeChat paper
- `@concepts/muse-autoskill-skill-lifecycle.md` — lifecycle + unit-test framing
- `@concepts/bayesian-posterior-guided-skill-evolution.md` — posterior beliefs over skills
- `@concepts/self-harness-model-specific-improvement-loop.md` — harness self-improvement
- `@concepts/continual-harness-online-self-improvement.md` — reset-free harness refinement
- `@concepts/skill-vetting.md` — probe/redaction hygiene
- `@concepts/ship-subagent-writer-reviewer-tester.md` — role-separated eval pattern
- `@concepts/agent-skills-progressive-disclosure.md` — skill bundle structure
- `@entities/mcp-servers/anthropic-skills.md` — Skill-Creator reference route

## Raw Concept

How do later sessions improve a skill without losing why prior revisions happened?

## Narrative

**SkillHone** [TENTATIVE — 2606.08671, no public code]: treats skill evolution as **continual** — not a bounded GEPA run that ships only the final SKILL.md. Core artifact is **decision history** linking:

- diagnosis (what failed)
- proposed revision
- evaluation evidence (probes, redacted traces)
- outcome (accept/reject)

Plus evidence-side lineage: which probes exposed which failure modes and how they shaped outcomes.

**Architecture:** role-bounded subagent dispatches — **eval subagents** run candidate skills on practice probes, return **redacted evidence** only; **optimization subagents** draft revisions from evidence + history without hidden probe access. Portable across Claude Code, Codex, Hermes (scoped dispatches + permission separation).

**Contrast matrix:**

| Route | Retains decision history | Continual across sessions |
|-------|-------------------------|---------------------------|
| Skill-Creator | No | No (one-shot synthesis) |
| GEPA / Hermes-SE | Partial (run logs) | Bounded run |
| Bayesian-Agent | Posterior over skills | Yes (registry) |
| Self-Harness | Harness flaw records | Yes (harness surfaces) |
| SkillHone | Structured decision + evidence history | Yes |

**Results** (Qwen3.6-35B-A3B eval backbone, open-web deep research): +15.8 GAIA, +3.2 WebWalkerQA-EN vs commercial retrieval-backed agent; beats prior skill-evolution baselines.

**CCC adoption:** REFERENCE until public repo + license. Steal-from: append decision-history blocks to wiki skill pages and `briefs/` when iterating skills; pair with redacted tester subagent from `@concepts/ship-subagent-writer-reviewer-tester.md`.

## Snippets

> "Later agents inherit not only the current skill and current evaluation assets, but also the decisions that shaped both."

> "Optimization subagents use this evidence and prior decision records to form diagnoses and draft skill revisions, without accessing hidden probe targets or validators."
