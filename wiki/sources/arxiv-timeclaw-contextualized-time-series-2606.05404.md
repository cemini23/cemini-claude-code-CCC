---
title: Harnessing Generalist Agents for Contextualized Time Series — TimeClaw (arXiv 2606.05404)
type: source
tags: [source, arxiv, harness, time-series, timeclaw]
keywords: [2606.05404, timeclaw, contextualized-time-series, mcp-workspace, capability-evolution]
related:
  - concepts/time-series-native-agent-harness.md
  - entities/tools/timeclaw.md
  - concepts/code-as-agent-harness.md
  - concepts/mcp-context-optimization.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/etclovg-harness-layers.md
  - concepts/muse-autoskill-skill-lifecycle.md
  - concepts/runtime-context-mcp-file-refs.md
  - entities/tools/claude-mem.md
  - entities/mcp-servers/stash.md
  - "@osint-wiki/concepts/contextualized-time-series-agent-harness.md"
maturity: draft
read_status: read
created: 2026-06-08
updated: 2026-06-08
---

## Relations

- `@concepts/time-series-native-agent-harness.md` — CCC synthesis
- `@entities/tools/timeclaw.md` — reference implementation
- `@concepts/code-as-agent-harness.md` — modality-native harness peer
- `@concepts/mcp-context-optimization.md` — MCP workspace pattern
- `@osint-wiki/concepts/contextualized-time-series-agent-harness.md` — finance/TSAIA routing stub

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Harnessing Generalist Agents for Contextualized Time Series |
| **Authors** | Zihao Li et al. (UIUC iSAIL) |
| **arXiv** | 2606.05404v1 [cs.AI] |
| **Code** | https://github.com/iDEA-iSAIL-Lab-UIUC/TimeClaw |
| **Location** | `raw-sources/arxiv-2606.05404-harnessing-generalist-agents-for-contextualized.pdf` |
| **Retrieved** | 2026-06-08 |
| **Read status** | read (abstract + §3 harness architecture + benchmarks) |

**Not to confuse** with arXiv **2605.10038** — a different paper also branded "TimeClaw" (exploratory execution learning).

## Narrative

**TimeClaw** is a **time-series-native agent harness** for contextualized temporal reasoning: numerical series plus text/metadata context. Targets two misalignments when LLMs serialize time series as tokens: (1) **datatype misalignment** — trends/periodicity distorted in token space; (2) **agentic-process misalignment** — text-centric agent loops cannot slice/aggregate/decompose at numerical precision.

Three harness components:

1. **Runtime-native temporal tools** — series loaded in task-local workspace `W`; tools execute on-server at full precision via MCP-style protocols; compact structured observations return to agent; auditable trajectories required for numerical claims.
2. **Experience-driven capability evolution** — evolution operator `E` admits verified recurring sub-procedures into toolset `T` (e.g. finance evolved `portfolio_var`, `portfolio_sharpe`, `capm_regression` on TSAIA).
3. **Episodic multimodal memory** — context key + time-series fingerprint `Ψ(X)` retrieve past reasoning traces.

**Benchmarks:** CiK (contextual forecasting), TSRBench (perception/reasoning/prediction/decision), TSAIA (finance MCQ). Vs multi-agent reflection: best avg RCRPS on CiK with ~half tokens; TSRBench 49.8% overall with GPT-5-nano; TSAIA +38.9% relative vs finance agents.

## Snippets

> "TIMECLAW operates on time-series-native runtime instead of serialized text." [Source: arxiv-2606.05404 p.2, retrieved 2026-06-08]

> "Every numerical claim [must be] grounded in a returned tool observation rather than inferred from free-form language reasoning." [Source: arxiv-2606.05404 §3.2, retrieved 2026-06-08]

> "Code is available at https://github.com/iDEA-iSAIL-Lab-UIUC/TimeClaw" [Source: arxiv abstract; `gh api` Apache-2.0 confirmed 2026-06-08]
