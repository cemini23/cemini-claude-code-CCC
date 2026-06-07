---
title: Failed-trajectory harness diagnosis and repair (HarnessFix)
type: concept
tags: [concept, harness, reliability, k100, harnessfix]
keywords: [2606.06324, harnessfix, htir, etclovg, trajectory-repair]
related:
  - sources/arxiv-failed-trajectory-harness-repair-2606.06324-2026-06-05.md
  - concepts/etclovg-harness-layers.md
  - concepts/code-as-agent-harness.md
  - concepts/self-healing-agent-sessions.md
  - concepts/skill-vetting.md
  - concepts/subagent-orchestration.md
  - concepts/seclaw-agent-security-evaluation.md
  - concepts/claude-premortem-skill.md
  - entities/tools/openspec.md
  - entities/tools/openevolve.md
  - "@osint-wiki/concepts/exploration-graph-dead-ends.md"
  - entities/tools/lazy-tool.md
  - sources/arxiv-maven-agentic-tool-calling-2605.30738.md
  - concepts/skilladaptor-step-level-skill-adaptation.md
  - sources/arxiv-skilladaptor-2606.01311.md
  - concepts/agentic-memory-cross-scenario-generality.md
  - concepts/retrospective-harness-optimization-rho.md
  - sources/arxiv-retrospective-harness-optimization-2606.05922.md
  - entities/tools/retro-harness.md
maturity: validated
created: 2026-06-05
updated: 2026-06-07
---

## Relations

- `@sources/arxiv-failed-trajectory-harness-repair-2606.06324-2026-06-05.md` — arXiv provenance (deep-read)
- `@concepts/etclovg-harness-layers.md` — layer vocabulary for diagnosis
- `@concepts/self-healing-agent-sessions.md` — runtime retry vs harness *repair* (different loop)
- `@concepts/seclaw-agent-security-evaluation.md` — trajectory eval (security); HarnessFix (reliability)
- `@osint-wiki/concepts/exploration-graph-dead-ends.md` — wiki `## Dead Ends` preserves abandoned paths; HarnessFix automates flaw consolidation from traces
- `@concepts/skilladaptor-step-level-skill-adaptation.md` — SkillAdaptor repairs **skill cards** at step granularity; HarnessFix repairs **harness artifacts** (prompts, hooks, validators)
- `@concepts/agentic-memory-cross-scenario-generality.md` — memory eval (2606.04315) vs harness repair; both reject outcome-only optimization

## Raw Concept

arXiv **2606.06324** — **HarnessFix**: trace-guided framework that (1) compiles failed runs into **HTIR** (Harness-aware Trace IR), (2) attributes failures to **TraceSteps** and **ETCLOVG** layers, (3) consolidates recurring diagnoses into **flaw records**, (4) applies **scoped repair operators** with regression-bounded acceptance. Reported +15.2%–50.0% held-out gains on SWE-Bench Verified, Terminal-Bench 2.0, GAIA, AppWorld vs initial harnesses and self-evolution baselines [TENTATIVE — paper claims, not replicated in Cemini workflow].

## Narrative

### Problem statement

Outcome-driven prompt/workflow optimization and runtime supervision often **skip diagnosis**: they patch from final scores without locating evidence in the trajectory or the responsible harness layer. HarnessFix argues failures emerge in interleaved reasoning, tool calls, and state — and must be mapped to **editable harness artifacts** (prompts, tool specs, orchestration code, hooks, validators) — not model weights.

### HarnessFix pipeline (four agents)

```text
failed trace + harness code
  → HTIR (TraceSteps + temporal / provenance / control-flow links)
  → diagnosis records (symptom → responsible step(s) → ETCLOVG layer(s))
  → flaw records (merged recurring patterns)
  → repair spec (scoped operators + edit constraints + validation thresholds)
  → candidate patch → pre-validation → held-out flaw/regression check → harness repair memory
```

| Stage | Output | CCC analogue |
|-------|--------|--------------|
| HTIR | Step-level TraceSteps with role, status, artifact effect | Manual read of session transcript + git diff |
| Diagnosis | Layer-tagged root cause | Tag `## Dead Ends` / log.md with ETCLOVG layer |
| Scoped repair | Operator-bound patch spec | OpenSpec change + skill-vetting before `.claude/` edits |
| Validation | ΔD_target ≥ δ_min AND R_new ≤ r_max | Lint + targeted pytest / smoke before merge |

### Repair operators (steal-from Table II)

Each `@concepts/etclovg-harness-layers.md` row maps to **typical flaws** and **candidate operators** — e.g. Tool Interface → schema narrowing, argument validation, tool-menu ranking; Verification → readiness checks, effect-evidence completion guarding (AppWorld example: reject `complete_task()` when state delta empty).

**Critical constraint:** repair is **not** free-form self-edit of core orchestration — operators bound editable artifacts and forbid benchmark/oracle leakage into patches.

### Cemini steal-from (no HarnessFix install)

| Paper mechanism | CCC implementation |
|-----------------|-------------------|
| Trajectory-grounded diagnosis | File failed sessions in `wiki/log.md` with ETCLOVG layer tag — `prompts/harness-flaw-record-template.md`; `@osint-wiki/concepts/exploration-graph-dead-ends.md` on entity pages |
| Scoped repair specs | `@entities/tools/openspec.md` acceptance criteria + `@concepts/claude-premortem-skill.md` before harness edits |
| Regression-bound acceptance | `wiki_lint.py` + `preingest_check.py` after ingest; prod `vet_skill.py` before skill promotion |
| Observability gaps | Stop-hook logging; claude-mem; defenseclaw `skill-scanner` (step 3b on `@concepts/skill-vetting.md`) |
| Verification gaps | SeClaw-style trajectory rubric when benchmark ships; Glasswing reviewer subagent |

### vs related patterns

| Pattern | HarnessFix difference |
|---------|----------------------|
| `@concepts/self-healing-agent-sessions.md` | Self-healing retries *in session*; HarnessFix *mutates harness code* from failed traces |
| `@entities/tools/openevolve.md` | Evolves configs/prompts search-style; HarnessFix is diagnosis-first with operators |
| SeClaw | Security trajectory eval; HarnessFix targets reliability harness flaws |
| Outcome-only prompt tuning | No step-level attribution |
| `@concepts/skilladaptor-step-level-skill-adaptation.md` (2606.01311) | Same step-level attribution idea; edits **skill cards** in K, not harness code/prompts |
| `@concepts/retrospective-harness-optimization-rho.md` (2606.05922) | Label-free self-preference over rollouts; full harness Skills+Tools; accept iff Sj > 0 |

### Adoption posture

| Check | Verdict |
|-------|---------|
| Full HarnessFix stack on laptop | **NO-GO** — research framework; four-agent loop + benchmark harnesses |
| ETCLOVG + operator vocabulary | **ADOPTED** — `@concepts/etclovg-harness-layers.md` |
| Manual flaw-record discipline | **ADOPTED** — `.cursor/rules/ccc-wiki-workflow.mdc` + `prompts/harness-flaw-record-template.md` |
| Prod deploy | **STEAL-FROM** — trajectory logs + dual Stage-1 scan; see prod adoption brief |

## Snippets

> "Existing efforts… are primarily outcome-driven rather than diagnosis-driven… without first identifying where the responsible evidence lies in the trajectory and which harness layer failed."
> — [Source: arxiv-2606.06324 §I, retrieved 2026-06-05]

> "A patch is accepted only when it satisfies both the target improvement and the regression limit."
> — [Source: arxiv-2606.06324 §III-D2, retrieved 2026-06-05]
