---
title: SkillAdaptor — step-level skill adaptation from failed trajectories
type: concept
tags: [concept, agent-skills, skill-adaptation, training-free, arxiv]
keywords: [2606.01311, skilladaptor, localizer, linker, qualifier, credit-assignment]
related:
  - sources/arxiv-skilladaptor-2606.01311.md
  - concepts/muse-autoskill-skill-lifecycle.md
  - concepts/failed-trajectory-harness-repair.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/agent-skills-progressive-disclosure.md
  - concepts/skill-vetting.md
  - concepts/thin-harness-fat-skills-garrytan.md
  - concepts/self-healing-agent-sessions.md
  - entities/mcp-servers/anthropic-skills.md
  - concepts/retrospective-harness-optimization-rho.md
  - sources/arxiv-retrospective-harness-optimization-2606.05922.md
  - concepts/bayesian-posterior-guided-skill-evolution.md
maturity: draft
created: 2026-06-06
updated: 2026-06-10
---

## Relations

- `@sources/arxiv-skilladaptor-2606.01311.md` — arXiv 2606.01311 provenance
- `@concepts/muse-autoskill-skill-lifecycle.md` — MUSE evaluates/refines skills; SkillAdaptor attributes failures to procedure spans
- `@concepts/failed-trajectory-harness-repair.md` — HarnessFix repairs harness code/prompts; SkillAdaptor repairs skill cards
- `@concepts/continual-harness-online-self-improvement.md` — both training-free; SkillAdaptor is skill-bank-only
- `@concepts/agent-skills-progressive-disclosure.md` — skill record fields (principle, when-to-apply, procedure)
- `@concepts/skill-vetting.md` — Qualifier ≈ promotion gate before skill enters retrieval
- `@concepts/thin-harness-fat-skills-garrytan.md` — modular plug-in for OpenClaw-class harnesses

## Raw Concept

arXiv **2606.01311** — **SkillAdaptor**: training-free skill maintenance via **step-level credit assignment** on failed trajectories. Three-stage pipeline: **Attribution** (Localizer + Linker) → **Modification** (Reviser/Generator) → **Qualification** (accept/reject gate). Backbone frozen; only skill collection **K** changes.

## Narrative

### Problem: trajectory-level adaptation diffuses blame

Most training-free skill pipelines (memory distillation, workflow refinement, EvoSkill-style evolution) reflect on **whole trajectories** or session summaries. Long-horizon tasks contain many correct intermediate steps; a single early fault can invalidate downstream actions. Outcome-level updates produce **overly broad or misdirected** skill revisions — the same credit-assignment problem HarnessFix addresses at harness-layer, but here at **skill-card** granularity.

### SkillAdaptor pipeline

```text
failed (q, τ, r=false)
  → Localizer: earliest accountable step t* + failure description π
  → Linker: weighted suspect skills + action ∈ {REVISE, GENERATE}
  → Reviser/Generator: targeted skill-card edit
  → Qualifier: accept → K updated; reject → Rejected History
```

**Initialization:** run tasks without skills; distill **K₀** from successful trajectories only. **Injection:** embed+rerank retrieve top skills per task. **Adaptation:** up to 10 rounds; freeze after 3 consecutive no-change rounds. ~65–75% of accepted writes land in rounds 1–2.

### Ablation load-bearing components

| Removed | Effect (Kimi-K2.5) |
|---------|-------------------|
| Localizer + Linker | WebShop Succ% 33.0% → 28.6%; Claw-Eval Avg 75.8 → 74.5 |
| Qualifier | WebShop Succ% → 26.3%; higher variance on PinchBench/Claw-Eval |
| All adaptors (K₀ only) | WebShop Score 32.5 ≈ base 32.1 — success-only distillation insufficient |

### Task-class effectiveness

| Task class | SkillAdaptor fit | Why |
|------------|------------------|-----|
| Data / Code | **High** | Localizable parsing, tool args, procedure steps |
| Productivity | Moderate | Ordering/schema fixes help; env rules may cap gains |
| Research / Memory / Security | Lower | Persistent state, external knowledge beyond single skill span |

### Cemini mapping

| Paper component | CCC analogue today | Gap |
|-----------------|-------------------|-----|
| Localizer + Linker | Manual post-mortem in `wiki/log.md` + flaw records | No automated step→skill link |
| Qualifier | `@concepts/skill-vetting.md` Phase-0 + smoke test | No auto-reject of bad skill edits |
| Skill injection | Progressive disclosure Level-1/2 | No embedding rerank over skill bank |
| OpenClaw plug-in | `~/.claude/skills/` + hooks | No post-session skill auto-edit |

**Verdict:** **REFERENCE** — steal **step-level attribution before skill edit** and **qualifier gate before promotion** patterns. Pairs with MUSE unit-test gate, HarnessFix flaw-record discipline, and RHO's accept-only-if-positive harness gate (skill-span vs full-harness scope).

**Peer (2606.05922):** `@concepts/retrospective-harness-optimization-rho.md` optimizes the **full harness** from trajectory groups; SkillAdaptor edits **skill cards** only.

## Phase-0 Audit (2026-06-06)

**Method:** `gh api` license check + README decode. No clone/run (vapor repo).

| Check | Result |
|-------|--------|
| Repo | `github.com/zjunlp/SkillAdaptor` |
| License | **MIT** [CONFIRMED via GitHub API] |
| Maturity | **6★**; 1 commit (2026-05-20); tree = `README.md` + `LICENSE` only |
| README | Placeholder `# SkillAdaptor` — no install/run instructions |
| Failure mode | **Vapor code** — paper announces release; repo is stub |
| Transport / creds | N/A — no executable surface yet |

**Decision — NO-GO (install).** **REFERENCE (methodology)** until runnable code + smoke test on laptop. Re-run Phase-0 when repo ships beyond README. Steal patterns only (Localizer/Linker/Qualifier) into manual `wiki/log.md` + `@concepts/skill-vetting.md` promotion gate.

## Snippets

> "SkillAdaptor is most effective when failure signals are localizable, and execution traces expose intermediate structure."

> "Skills distilled solely from successful trajectories do not reliably transfer across tasks … effective adaptation depends on precise failure attribution and qualification rather than skill accumulation alone."

> — [Source: arxiv-2606.01311-skilladaptor-self-adapting-skills-for-llm-agents.pdf p.4–5, retrieved 2026-06-06]
