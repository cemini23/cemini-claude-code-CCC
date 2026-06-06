---
title: SkillAdaptor — self-adapting skills from trajectories (arXiv 2606.01311)
type: source
tags: [source, arxiv, agent-skills, skill-adaptation, openclaw]
keywords: [2606.01311, skilladaptor, step-level-attribution, training-free, openclaw]
related:
  - concepts/skilladaptor-step-level-skill-adaptation.md
  - concepts/muse-autoskill-skill-lifecycle.md
  - concepts/failed-trajectory-harness-repair.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/agent-skills-progressive-disclosure.md
  - concepts/skill-vetting.md
  - concepts/thin-harness-fat-skills-garrytan.md
  - concepts/self-healing-agent-sessions.md
  - entities/mcp-servers/anthropic-skills.md
maturity: draft
read_status: read
created: 2026-06-06
updated: 2026-06-06
---

## Relations

- `@concepts/skilladaptor-step-level-skill-adaptation.md` — CCC synthesis
- `@concepts/muse-autoskill-skill-lifecycle.md` — MUSE lifecycle peer (evaluation + refinement)
- `@concepts/failed-trajectory-harness-repair.md` — harness repair vs skill-card repair (different artifact layer)
- `@concepts/continual-harness-online-self-improvement.md` — training-free trajectory improvement peer
- `@concepts/agent-skills-progressive-disclosure.md` — skill record structure (title, principle, applicability)
- `@concepts/skill-vetting.md` — Qualifier gate parallels Phase-0 promotion

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | SkillAdaptor: Self-Adapting Skills for LLM Agents from Trajectories |
| **Authors** | Zhuoyun Yu, Xin Xie, Wuguannan Yao, Chenxi Wang, Lei Liang, Xiang Qi, Shumin Deng |
| **Affiliation** | Zhejiang University; Ant Digital Technologies / Ant Group |
| **arXiv** | 2606.01311v1 [cs.CL] |
| **Code** | https://github.com/zjunlp/SkillAdaptor (announced; release pending) |
| **Location** | `raw-sources/arxiv-2606.01311-skilladaptor-self-adapting-skills-for-llm-agents.pdf` |
| **Retrieved** | 2026-06-06 |
| **Read status** | read (abstract, method, benchmarks, ablations, case study) |

## Narrative

**SKILLADAPTOR** is a **training-free** modular skill adaptor that shifts skill maintenance from trajectory-level reflection to **step-level failure attribution**. Given a failed execution trace, a frozen backbone LLM agent with a dynamic skill collection **K**:

1. **Attribution** — `Localizer` finds earliest accountable fault step `(t*, π)`; `Linker` weights suspect skills and routes to `REVISE` or `GENERATE`.
2. **Modification** — `Reviser` / `Generator` produce targeted skill-card edits (principle, when-to-apply, procedure).
3. **Qualification** — `Qualifier` acceptance gate blocks unstable skills from entering retrieval.

Skills are retrieved via embedding similarity (Qwen3-Embedding-8B) + backbone rerank. Initialization distills skills from **successful** trajectories only; failed trajectories drive subsequent adaptation (up to 10 rounds or 3 consecutive no-change rounds).

Evaluated on **WebShop**, **PinchBench**, **Claw-Eval** with Kimi-K2.5, GLM-5, GPT-5.2. Largest single-metric gains vs baselines: +1.7 WebShop Succ% (Kimi), +1.5 PinchBench Avg Score% (GLM), +1.8 Claw-Eval Avg Score (Kimi). Ablations show Localizer+Linker and Qualifier are both load-bearing — initial success-only distillation alone nearly vanishes gains.

**CCC relevance:** plug-in for OpenClaw-class harnesses; complements Cemini's static Phase-0 `skill-vetting.md` with a **post-execution refinement loop** grounded in localized procedure edits, not whole-trajectory rewrites.

## Snippets

> "We propose SKILLADAPTOR, a training-free step-level skill adaptation framework with explicit failure attribution, and it can plug into OpenClaw-class agent harnesses."

> "Without Localizer and Linker, WebShop success drops to 28.6% … so step-level attribution is needed to target effective revisions."

> "Without Qualifier … WebShop success falls to 26.3% … removing qualification allows unstable skills to enter retrieval."

> — [Source: arxiv-2606.01311-skilladaptor-self-adapting-skills-for-llm-agents.pdf p.1–5, retrieved 2026-06-06]
