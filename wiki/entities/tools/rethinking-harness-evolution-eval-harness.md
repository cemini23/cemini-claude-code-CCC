---
title: rethinking-harness-evolution/code — matched-budget harness-eval methodology reference
type: entity
tags: [entity, tool, phase-0, reference, evaluation-methodology, k169]
keywords: [terminal-bench, e2b, parallel sampling, sequential refinement, agent debugger, no-license]
related:
  - sources/arxiv-rethinking-harness-evolution-evaluation-2607.12227.md
  - concepts/harness-evolution-vs-test-time-scaling-baseline.md
  - sources/brief-k169-harness-evolution-eval-discipline-2026-07-15.md
maturity: draft
created: 2026-07-15
updated: 2026-07-15
---

## Relations

- `@sources/arxiv-rethinking-harness-evolution-evaluation-2607.12227.md` — the paper this repo implements
- `@concepts/harness-evolution-vs-test-time-scaling-baseline.md` — the checklist this repo operationalizes
- `@sources/brief-k169-harness-evolution-eval-discipline-2026-07-15.md` — prod brief stub

## Raw Concept

Public code link cited in the abstract of `@sources/arxiv-rethinking-harness-evolution-evaluation-2607.12227.md` — Phase-0 audited 2026-07-15.

## Narrative

### What it is

`github.com/rethinking-harness-evolution/code` — a real, focused implementation of the paper's **four-method matched-budget comparison**: Parallel Sampling, Sequential Refinement, Harness Evolution (AHE with explore-agent disabled), and Harness Scaling, run against Terminal-Bench 2.1 via E2B sandboxes. Files: `evolve.py` / `evolve_ahe.py` / `evolve_seq.py` (the four method drivers), `run_code_agent_baseline.py`, `audit_blind_rollout_selection.py`, `trace_converter.py`, `agents/`, `configs/`. Requires `CLAUDE_API_KEY`, `E2B_API_KEY`, `GITHUB_TOKEN`, plus `GPT54_LLM_*` / `ANTHROPIC_*` / `ADB_LLM_*` / `SERPER_API_KEY` for the Harness Evolution path — real paid-API and sandbox infrastructure, not a walk-in local tool.

### Phase-0 audit (2026-07-15)

| Check | Result |
|-------|--------|
| License | **No LICENSE file** — GitHub API `license.spdx_id: null`; `pyproject.toml` claims `MIT` text-only (no LICENSE file — classic no-LICENSE pattern, treat as unlicensed for fork/redistribute) [CONFIRMED via `gh api` + shallow clone] |
| Size | GitHub metadata 387 KB; shallow clone ~2.4 MB |
| Maturity | 1★, account created 2026-07-04, single push 2026-07-06 (anonymized pre-print-review account pattern) |
| Failure mode class | Requires 4 external paid APIs (Claude, GPT, E2B compute sandboxes, Serper search) + `tmux` for long runs; not portable to a laptop-only, no-paid-infra workflow without meaningful spend |

### Verdict

**NO-GO for local adoption as-is** — no license (can't legally fork/modify/redistribute), and the infra cost (E2B sandbox-per-rollout, multiple frontier-model API calls per experiment) is disproportionate to CCC's laptop-only, low-spend posture. **REFERENCE** — the *design* of the four-way comparison (same seed harness, matched K, explicit pass@1 vs pass@k reporting, disjoint train/val/test split) is the reusable artifact. If Cemini ever needs to audit a specific harness-evolution claim rigorously (e.g. before a prod harness change with real deployment cost), reimplement this comparison shape cheaply rather than adopting the repo wholesale — see `@concepts/harness-evolution-vs-test-time-scaling-baseline.md` for the condensed checklist version.

## Snippets

> "This repo supports four methodologies: Parallel Sampling, Sequential Refinement, Harness Evolution, Harness Scaling." — repo README
