---
title: Verification-gated persist/pivot runtime (K253)
type: concept
tags: [concept, agentic-runtime, persist-pivot, verification-gated, four-role, k253]
keywords: [2608.05144, Argus, Manager, Planner, Engineer, Reviewer, self-evolution]
related:
  - sources/arxiv-automoose-agentic-phase-field-2608.20571.md
  - concepts/diagnostic-prescriptive-asymmetry-mcp-rca.md
  - sources/arxiv-argus-long-horizon-agentic-runtime-2608.05144.md
  - entities/tools/argus-agentic-runtime.md
  - concepts/self-healing-agent-sessions.md
  - concepts/failed-trajectory-harness-repair.md
  - concepts/agent-completion-verification-gates.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - sources/brief-k249-k253-scale-cda-canary-rac-artanno-argus-2026-08-06.md
  - briefs/2026-08-06_ccc-handoff-k249-k253-ingest.md
  - concepts/trajectory-error-lifecycle-attribution.md
maturity: draft
created: 2026-08-06
updated: 2026-08-25
---

## Relations

- `@sources/arxiv-argus-long-horizon-agentic-runtime-2608.05144.md` — K253 provenance
- `@concepts/agent-completion-verification-gates.md` — task-native verification peer
- `@concepts/self-healing-agent-sessions.md` — in-session retry vs persist/pivot
- `@concepts/failed-trajectory-harness-repair.md` — cross-session harness repair peer
- `@sources/arxiv-automoose-agentic-phase-field-2608.20571.md`
- `@concepts/diagnostic-prescriptive-asymmetry-mcp-rca.md`

## Raw Concept

How should long-horizon agents evolve durable state without mutating model weights?

## Narrative

K253 Argus (arXiv **2608.05144**): persistent self-evolving runtime over durable project state. Fixed model weights; evolution via **verified state + control policy**.

### Four roles

| Role | Function |
|------|----------|
| Manager | Project state ownership |
| Planner | Task decomposition |
| Engineer | Implementation |
| Reviewer | Admission gate |

### Persist / pivot discipline

- Admit memories/skills/procedures only after **role-owned review + task-native verification**
- **Persist** when evidence supports continuation
- **Pivot** on measured failure — not blind retry

**Results:** SWE-Bench Pro ~78% vs Direct Copilot 59% (1.41× tokens); mature waves −21% solve-input tokens after verification-gated self-evolution.

Repo `lbx154/Argus`: README badge + `pyproject.toml` claim MIT; GitHub license API **null**; **no LICENSE file** — **NO-GO clone** per Phase-0.

### Cemini steal (ADOPT)

- Four-role separation maps to Task/subagent role graphs
- Verification-gated admission pairs `@concepts/agent-completion-verification-gates.md` and `@concepts/bounded-self-refinement-vs-rsi-taxonomy.md`
- Persist/pivot beats unbounded self-healing retry (`@concepts/self-healing-agent-sessions.md`)

| Verdict | **ADOPT** harness pattern. **NO-GO** clone (no SPDX). Entity `wont_wire`. |
