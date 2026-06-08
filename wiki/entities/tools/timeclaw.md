---
title: TimeClaw — contextualized time-series agent harness (2606.05404)
type: entity
tags: [tool, harness, time-series, phase-0]
keywords: [timeclaw, idea-isail, 2606.05404, apache-2.0]
related:
  - sources/arxiv-timeclaw-contextualized-time-series-2606.05404.md
  - concepts/time-series-native-agent-harness.md
  - concepts/code-as-agent-harness.md
  - "@osint-wiki/concepts/contextualized-time-series-agent-harness.md"
maturity: draft
created: 2026-06-08
updated: 2026-06-08
phase_0_verdict: "CONDITIONAL-GO 2026-06-08 — Apache-2.0; 0★ release-day; harness-pattern REFERENCE for CCC; finance evals → OSINT"
---

## Relations

- `@sources/arxiv-timeclaw-contextualized-time-series-2606.05404.md` — paper provenance
- `@concepts/time-series-native-agent-harness.md` — methodology synthesis
- `@osint-wiki/concepts/contextualized-time-series-agent-harness.md` — finance benchmark routing

## Raw Concept

- **URL:** https://github.com/iDEA-iSAIL-Lab-UIUC/TimeClaw
- **Paper:** arXiv 2606.05404 (not 2605.10038)
- **License:** Apache-2.0 [CONFIRMED 2026-06-08 via `gh api`]
- **Stars / push:** 0★ / 2026-06-07

## Narrative

Reference implementation for **time-series-native agent harness** — MCP workspace, runtime temporal tools, capability evolution, episodic multimodal memory.

| Check | Result |
|-------|--------|
| License | Apache-2.0 ✓ |
| Maturity | 0★, release-day — immature |
| CCC fit | **Steal harness patterns**; do not adopt as Claude Code replacement |
| OSINT fit | TSAIA / CiK finance slices — cross-wiki stub |

**Verdict:** **CONDITIONAL-GO** — clone to `/tmp/timeclaw-trial/` for architecture read; **NO-GO** prod until API keys + finance data paths scoped. No install to `~/.claude/`.

## Phase-0 Audit (2026-06-08)

**Method:** `gh api` license + clone to `/tmp/timeclaw-phase0-ccc/` + venv import smoke (`scripts/adopt_timeclaw_phase0.sh`).

| Gate | Result |
|------|--------|
| SPDX | Apache-2.0 [CONFIRMED — LICENSE file] |
| README | arXiv 2606.05404; Python 3.11; LangChain + fastmcp stack |
| Import | `from timeclaw.agents import TimeClaw` **PASS** in isolated venv |
| Run deps | `OPENAI_API_KEY` required (embeddings + default models); `.env.example` shipped |
| Benchmarks | `main.py --benchmark {cik,tsrbench,tsaia}` — not run (no key in Phase-0) |
| Failure mode | Name collision with arXiv 2605.10038 TimeClaw |
| Blast radius | Low if `/tmp/` only; **NO-GO** `~/.claude/` |

## Snippets

> "TIMECLAW achieves the best average RCRPS and sMAPE" on CiK with ~half tokens vs multi-agent reflection. [Source: arxiv 2606.05404 Table 1 — [TENTATIVE] single-paper eval]
