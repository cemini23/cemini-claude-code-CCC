---
title: SkillHone — continual skill evolution via decision history (arXiv 2606.08671)
type: source
tags: [source, arxiv, skillhone, skill-evolution, harness, k111]
keywords: [2606.08671, skillhone, decision-history, gepa, skill-creator]
related:
  - concepts/skillhone-continual-skill-decision-history.md
  - concepts/muse-autoskill-skill-lifecycle.md
  - concepts/bayesian-posterior-guided-skill-evolution.md
  - concepts/self-harness-model-specific-improvement-loop.md
  - concepts/skill-vetting.md
  - entities/tools/hermes-agent.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/ship-subagent-writer-reviewer-tester.md
  - concepts/subagent-orchestration.md
maturity: draft
read_status: read
created: 2026-06-12
updated: 2026-06-12
---

## Relations

- `@concepts/skillhone-continual-skill-decision-history.md` — CCC synthesis
- `@concepts/muse-autoskill-skill-lifecycle.md` — unified skill lifecycle sibling
- `@concepts/bayesian-posterior-guided-skill-evolution.md` — posterior-guided evolution contrast
- `@concepts/self-harness-model-specific-improvement-loop.md` — harness self-improvement sibling
- `@concepts/skill-vetting.md` — evaluation/redaction discipline for skill assets
- `@entities/tools/hermes-agent.md` — portable runtime (Claude Code, Codex, Hermes)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | SkillHone: A Harness for Continual Agent Skill Evolution Through Persistent Decision History |
| **Authors** | Zhiwei Li*, Yong Hu (WeChat / Tencent) |
| **arXiv** | 2606.08671v1 [cs.LG] |
| **Location** | `raw-sources/arxiv-2606.08671-skillhone-a-harness-for-continual-agent-skill-ev.pdf` |
| **Retrieved** | 2026-06-12 |
| **Read status** | read (loop, subagent roles, benchmark deltas) |

## Narrative

**SkillHone** — harness for **continual** skill evolution across many sessions. Unlike Skill-Creator (one-shot synthesis) or GEPA/Hermes-SE (bounded reflective runs that retain only final artifact), SkillHone persists **structured decision history**: diagnosis → proposed revision → evaluation evidence → outcome — plus evidence-side records (which probes exposed which failure modes).

**Role-separated subagents:** evaluation subagents run candidate skills on practice probes with **redacted reporting**; optimization subagents draft revisions from redacted evidence + prior decision records without access to hidden probe targets. Portable across skill-enabled runtimes (Claude Code, Codex, Hermes) — assumes only scoped dispatches with separated permissions.

**Benchmarks** (raw open-web deep research — no integrated commercial search stack; agents organize retrieval via portable skills):

| Backbone | GAIA | WebWalkerQA-EN |
|----------|------|----------------|
| SkillHone skills (Qwen3.6-35B-A3B eval) | +15.8 vs commercial deep-research agent | +3.2 |
| vs prior skill-evolution methods | exceeds | exceeds |

References Skill-Creator (`anthropics/skills`) and Hermes-Agent-Self-Evolution (NousResearch).

**CCC relevance:** decision-history artifact for wiki/skill lineage; redacted eval subagent pattern maps to ship-subagent writer/reviewer/tester. **No public SkillHone repo** found (2026-06-12) — REFERENCE until release + license.

## Snippets

> "Existing methods improve skills in bounded runs and retain only the final artifact, discarding the decision history that later agents need to interpret prior revisions, evaluations, and rejected alternatives."

> "Evaluation subagents can inspect probes and traces and run candidate skills, but return only redacted evidence to the optimization side."
