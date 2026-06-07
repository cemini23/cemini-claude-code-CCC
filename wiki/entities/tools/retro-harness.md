---
title: retro-harness — RHO reference implementation (arXiv 2606.05922)
type: entity
tags: [tool, harness, rho, microsoft, phase-0]
keywords: [retro-harness, wbopan, 2606.05922, self-preference, mit]
related:
  - sources/arxiv-retrospective-harness-optimization-2606.05922.md
  - concepts/retrospective-harness-optimization-rho.md
  - concepts/failed-trajectory-harness-repair.md
  - entities/tools/openevolve.md
  - entities/tools/revfactory-harness.md
  - concepts/code-as-agent-harness.md
maturity: draft
created: 2026-06-07
updated: 2026-06-07
---

## Relations

- `@sources/arxiv-retrospective-harness-optimization-2606.05922.md` — arXiv provenance
- `@concepts/retrospective-harness-optimization-rho.md` — methodology synthesis
- `@entities/tools/openevolve.md` — validation-metric optimizer peer
- `@entities/tools/revfactory-harness.md` — harness generator peer (validation-driven)

## Raw Concept

`wbopan/retro-harness` — MIT reference code for **Retrospective Harness Optimization** (MSRA + CityU, arXiv 2606.05922). DPP coreset → group rollout → best-of-N self-preference harness update.

## Narrative

| Check | Verdict |
|-------|---------|
| License | **MIT** [CONFIRMED 2026-06-07] |
| Stars | 0 (release-day repo) |
| Stack | Python (`pyproject.toml`, `uv.lock`), configs, webui |
| Target agent | Codex workspace-folder harness in paper |
| CCC mapping | Trial only — map stages to claude-mem + wiki flaw records manually first |

**Verdict:** **CONDITIONAL-GO** — clone to `/tmp/retro-harness-trial/`; run tests; **NO-GO** prod `~/.claude/` until Claude Code harness adapter exists.

## Phase-0 Audit (2026-06-07)

**Method:** `gh api` license + repo tree listing. No install/run this session.

| Gate | Result |
|------|--------|
| G1 License | PASS — MIT |
| G2 Maturity | WARN — 0★, pushed 2026-06-07 |
| G3 Harness class | Codex-specific; Claude Code port unverified |
| G4 Blast radius | HIGH if pointed at live `.claude/` — isolate |

## Snippets

> "RHO: Retrospective Harness Optimization — improving LLM agents from unlabeled past trajectories."
> — [Source: github.com/wbopan/retro-harness README, retrieved 2026-06-07]
