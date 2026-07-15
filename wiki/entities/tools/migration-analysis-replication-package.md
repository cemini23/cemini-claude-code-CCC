---
title: migration-analysis — replication package for "Better Harnesses, Smaller Models"
type: entity
tags: [entity, tool, phase-0, no-go, replication-package, k169]
keywords: [malusamayo, figshare, software-agent-sdk, openhands, no-license]
related:
  - sources/arxiv-better-harnesses-smaller-models-2607.08938.md
  - concepts/failure-mode-harness-adaptation-mapping.md
  - sources/brief-k168-slm-harness-adaptation-2026-07-15.md
maturity: draft
created: 2026-07-15
updated: 2026-07-15
---

## Relations

- `@sources/arxiv-better-harnesses-smaller-models-2607.08938.md` — the paper this repo replicates
- `@concepts/failure-mode-harness-adaptation-mapping.md` — ADOPT taxonomy extracted without installing this package
- `@sources/brief-k168-slm-harness-adaptation-2026-07-15.md` — prod brief stub

## Raw Concept

Public code link cited in `@sources/arxiv-better-harnesses-smaller-models-2607.08938.md` — Phase-0 audited 2026-07-15 to decide if it's worth cloning locally.

## Narrative

### What it is

`github.com/malusamayo/migration-analysis` — **not a reusable harness-adaptation tool.** It is the paper's **result-table/figure replication package**: scripts to re-render `results_table.tex/.md` and four figures from either (a) a compact "core" archive of curated intermediates hosted on figshare, or (b) full run/eval archives to recompute `summary.json` from raw `run.json`/`eval_results.yaml`. The repo embeds `software-agent-sdk` (OpenHands) as a submodule — that's the actual general-purpose agent framework the paper's optimizer was implemented against, and it is a separate, independently-maintained upstream project, not something new produced by this paper.

### Phase-0 audit (2026-07-15)

| Check | Result |
|-------|--------|
| License | **None** — GitHub API `license.spdx_id: null`; no LICENSE file in repo root [CONFIRMED via `gh api`] |
| Size | GitHub metadata 4.7 MB; shallow clone ~43 MB (submodules/data pathing; still under 500MB) — **NO-GO on license**, not size |
| Maturity | 1★, last push 2026-06-30 (pre-print), single-purpose |
| Contents | `.dockerignore`, `AGENTS.md`, `CLAUDE.md`, `LOCA-bench` (submodule), `data/`, `docker-compose.yml`, `docs/`, `replication_package/` (the actual reusable scripts), `software-agent-sdk` (submodule), `src/`, `tasks/` |
| Failure mode class | Academic replication packages: large data-download dependency on figshare (not vendored), tied to specific benchmark task directories the paper curated, not designed for reuse outside reproducing the paper's own numbers |

### Verdict

**NO-GO for local adoption** — not a general tool; it's paper-specific reproduction scaffolding with no license. **REFERENCE only** — worth returning to if we ever want to independently re-verify the paper's Table II numbers, but that requires the figshare archives and paid Vertex AI/AWS Bedrock API access the paper used, which is out of scope for a laptop-only wiki workflow. The one component with standalone value is the `software-agent-sdk` (OpenHands) submodule dependency — track separately if Cemini ever evaluates OpenHands as an agent framework; not currently covered elsewhere in this wiki.

## Snippets

> "This repository contains the replication package for the paper result table and figures." — repo README
