---
title: Agent rubrics — self-evaluation and correction loops (K97)
type: concept
tags: [concept, eval, rubrics, harness, k97]
keywords: [sydneyrunkle, rubrics, self-correction, agent-eval, deepeval]
related:
  - concepts/agent-completion-verification-gates.md
  - concepts/skill-vetting.md
  - entities/patterns/full-prompt-goal-template.md
  - concepts/self-healing-agent-sessions.md
  - concepts/worldmemarena-multimodal-agent-memory-eval.md
  - entities/tools/claude-code.md
  - entities/skills/cursor-audit.md
  - entities/skills/super-audit.md
  - sources/trading-posts-compilation-17-2026-06-03.md
  - concepts/retrospective-harness-optimization-rho.md
  - sources/arxiv-retrospective-harness-optimization-2606.05922.md
  - concepts/dynamic-workflow-orchestrator-off-model.md
  - entities/tools/aarri-bench.md
  - sources/arxiv-aarri-research-intern-bench-2606-07462-2026-06-09.md
  - concepts/ship-subagent-writer-reviewer-tester.md
  - concepts/bayesian-posterior-guided-skill-evolution.md
  - concepts/orchestration-reward-modeling-orch-rm.md
  - concepts/adversarial-curriculum-structured-reward-doc-fidelity.md
  - sources/arxiv-orch-rm-multi-agent-orchestration-2606.13598.md
  - concepts/gatekeeper-layered-agent-evaluation.md
  - sources/arxiv-gatekeepers-layered-eval-quantum-vqe-2606.18422.md
  - concepts/claim-drift-automated-research.md
  - sources/arxiv-xcientist-research-harness-claim-drift-2606.18874.md
  - entities/skills/grill-with-docs.md
  - concepts/cross-model-verified-agent-translation.md
  - "@osint-wiki/concepts/polyworkbench-multilingual-harness-eval.md"
  - sources/arxiv-residencyrl-simulated-clinical-rl-2608.07418.md
  - concepts/evaluation-first-rubric-induction.md
maturity: draft
created: 2026-06-03
updated: 2026-09-01
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-17-2026-06-03.md"
---

## Relations

- `@concepts/adversarial-curriculum-structured-reward-doc-fidelity.md`
- `@concepts/agent-completion-verification-gates.md` — explicit done criteria before merge
- `@concepts/skill-vetting.md` — rubric rows for skill/MCP Phase-0
- `@entities/patterns/full-prompt-goal-template.md` — success criteria in `/goal` envelopes
- `@concepts/self-healing-agent-sessions.md` — bounded retry vs infinite rubric loops
- `@concepts/worldmemarena-multimodal-agent-memory-eval.md` — eval rubric steal-from (memory MCP)
- `@entities/tools/claude-code.md` — Stop hook + subagent reviewer pattern
- `@entities/skills/cursor-audit.md` — three-model readonly audit synthesis before ship
- `@entities/skills/super-audit.md` — five-model synthesis for prod GO/NO-GO
- `@sources/trading-posts-compilation-17-2026-06-03.md` — K97 Post 6 (@sydneyrunkle)
- `@osint-wiki/concepts/polyworkbench-multilingual-harness-eval.md` — K155 hybrid structural + executable + LLM semantic eval (multilingual compounding)
- `@concepts/evaluation-first-rubric-induction.md`

## Raw Concept

K97 Post 6 (@sydneyrunkle): **Rubrics** — structured criteria agents use to **self-evaluate and self-correct** before declaring work complete. CCC maps to existing verification gates, not a new eval SaaS install.

## Narrative

### Rubric shape for harness work

| Dimension | Example criterion |
|-----------|-------------------|
| Correctness | Tests pass; linter clean; wiki_lint 0 bidirectional gaps |
| Scope | Diff matches `/goal` acceptance bullets only |
| Provenance | Claims tagged `[CONFIRMED]` / `[TENTATIVE]` / `[NEEDS VERIFICATION]` |
| Safety | No secrets committed; no `--force` git without explicit ask |

**Peer (2606.05922):** RHO's `rank_val` / `rank_con` are structured self-rubrics over trajectory groups — steal the **accept-only-if-positive** gate (Sj > 0) for harness promotion, not infinite rubric loops.
| Cost | Subagent used for wide reads; cache-friendly static prompts |

### Integration points [TENTATIVE]

1. **`/goal` template** — section 1 is the rubric (what "done" looks like).
2. **Stop hook** — re-check rubric before session end (`@concepts/hooks-for-automation.md`).
3. **Reviewer subagent** — `code-reviewer`, `@entities/skills/cursor-audit.md` (cross-model), `@entities/skills/super-audit.md` (pre-ship), or other `@entities/skills/` audit pass on large diffs.
4. **Phase-0 audits** — rubric rows in `@concepts/skill-vetting.md` for MCP/skill adopt.

**PolyWorkBench steal (K155):** Long-horizon workplace trajectories degrade when multilingual inputs compound across turns. Federation harness rubrics should layer **structural** checks (schema/files), **executable** checks (scripts/fixtures), and **LLM semantic** grading — not a single judge pass. Reference: `@osint-wiki/concepts/polyworkbench-multilingual-harness-eval.md`.

**Verdict:** **REFERENCE** — steal eval harness ideas; compare to `@entities/tools/deepeval` brief (K55, deferred) before adding eval framework deps.

## Snippets

> Rubrics — agents self-evaluate and self-correct. [TENTATIVE — @sydneyrunkle, Posts.docx K97 Post 6]
