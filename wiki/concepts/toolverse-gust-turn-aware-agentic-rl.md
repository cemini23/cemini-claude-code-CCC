---
title: ToolVerse / GUST — tool-dependency graphs and turn-aware credit
type: concept
tags: [concept, agentic-rl, mcp, long-horizon, credit-assignment, k191]
keywords: [2607.15660, GUST, Dynamic Unlocking Sampling, Turn-Aware Relative Advantage]
related:
  - sources/arxiv-toolverse-long-horizon-mcp-rl-2607.15660.md
  - concepts/hierarchical-skill-stack-lazy-orchestration.md
  - concepts/agentic-online-rl-self-evolving-systems.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - concepts/multilingual-long-horizon-agent-eval.md
  - sources/brief-k190-k194-mcp-gateway-toolverse-tars-2026-07-20.md
maturity: draft
created: 2026-07-20
updated: 2026-07-20
---

## Relations

- `@sources/arxiv-toolverse-long-horizon-mcp-rl-2607.15660.md` — provenance
- `@concepts/hierarchical-skill-stack-lazy-orchestration.md` — multi-tool structure peer
- `@concepts/agentic-online-rl-self-evolving-systems.md` — RL systems peer
- `@concepts/bounded-self-refinement-vs-rsi-taxonomy.md` — do not close RL loops without execution+ human gate
- `@concepts/multilingual-long-horizon-agent-eval.md` — long-horizon eval peer (K152)

## Raw Concept

K191 ToolVerse (Meituan): scale agentic RL to hundreds of real MCP envs; synthesize long-horizon tasks from a **tool dependency graph**; assign credit with **Turn-Aware Relative Advantage**.

## Narrative

### Steal

1. **Dependency-graph tasks** — unlock tools only after prerequisites succeed (mirrors real multi-MCP workflows).
2. **Turn-level advantage** — sparse end reward alone is hostile to long TipDrop/poker/agent trajectories; prefer per-step signals when training or diagnosing policies.
3. **No install** — no official SPDX artifact; ignore name-collision repos.

### Cemini map

| Project | Use |
|---------|-----|
| Poker arena | Multi-hand / multi-tool decide chains → per-hand or per-street scores, not only session PnL |
| TipDrop | Scanner→signal→post pipelines as unlock graph for eval harnesses |
| Prod | Log turn-level success for long LangGraph runs |

| Verdict | **ADOPT** graph + turn-aware scoring checklist; **NO-GO** ToolVerse clone |

## Snippets

> "task design strategy based on a tool dependency graph, utilizing Dynamic Unlocking Sampling Algorithm … GUST"
> — [Source: arxiv-2607.15660]
