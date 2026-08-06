---
title: "Argus — persistent self-evolving long-horizon agentic runtime"
type: source
tags: [source, arxiv, agentic-runtime, persist-pivot, verification-gated, k253]
keywords: [2608.05144, Argus, Manager, Planner, Engineer, Reviewer, SWE-Bench Pro]
related:
  - concepts/verification-gated-persist-pivot-runtime.md
  - entities/tools/argus-agentic-runtime.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - concepts/self-healing-agent-sessions.md
  - concepts/failed-trajectory-harness-repair.md
  - concepts/agent-completion-verification-gates.md
  - sources/brief-k249-k253-scale-cda-canary-rac-artanno-argus-2026-08-06.md
  - briefs/2026-08-06_ccc-handoff-k249-k253-ingest.md
maturity: draft
created: 2026-08-06
updated: 2026-08-06
---

## Relations

- `@concepts/verification-gated-persist-pivot-runtime.md`
- `@entities/tools/argus-agentic-runtime.md`
- `@concepts/agent-completion-verification-gates.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Argus |
| **arXiv** | 2608.05144 |
| **Repo** | `lbx154/Argus` (~10MB GH) — README badge + `pyproject.toml` claim MIT; GitHub license API **null**; **no LICENSE file** in root |
| **Domain** | Long-horizon SWE agent runtime |
| **Retrieved** | 2026-08-06 |

## Narrative

Persistent self-evolving runtime: Manager / Planner / Engineer / Reviewer over durable project state. Fixed model weights; evolution via verified state + control policy. Admit memories/skills/procedures only after role-owned review + task-native verification. Persist when evidence supports; pivot on measured failure.

SWE-Bench Pro ~78% vs Direct Copilot 59% (1.41× tokens); mature waves −21% solve-input tokens after verification-gated self-evolution.

| Verdict | **ADOPT** four-role + verification-gated admission + persist/pivot harness. **NO-GO** clone (no SPDX file). Entity `wont_wire`. |
