---
title: Solver-grounded agent numerics — trusted tool is source of truth
type: concept
tags: [concept, verification, tools, numerics, k199]
keywords: [2607.18147, solver-grounded, LLM-as-interface, not LLM-as-computer]
related:
  - sources/arxiv-smart-grids-agentic-tutorial-2607.18147.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - concepts/agent-completion-verification-gates.md
  - concepts/model-native-vs-tool-mediated-fulfillment.md
  - sources/brief-k197-k201-harness-solver-pruner-2026-07-21.md
  - concepts/domain-mcp-skills-fresh-subagent-orchestration.md
  - sources/arxiv-agents4geos-mcp-multiphyics-2607.18557.md
  - entities/tools/agents4geos.md
maturity: draft
created: 2026-07-21
updated: 2026-07-22
---

## Relations

- `@sources/arxiv-smart-grids-agentic-tutorial-2607.18147.md` — provenance (energy OOD)
- `@concepts/bounded-self-refinement-vs-rsi-taxonomy.md` — execution > LLM judge
- `@concepts/agent-completion-verification-gates.md` — gates peer
- `@concepts/model-native-vs-tool-mediated-fulfillment.md` — tool-mediated peer

## Raw Concept

K199 smart-grid tutorial principle, generalized: **a numerical result is reported only when it originates from a trusted tool and passes explicit verification.** LLM is interface/orchestrator, not calculator.

## Narrative

### Steal (ADOPT)

1. Poker / TipDrop / prod: never let the LLM invent EV, odds, PnL, or schedule numbers — call solver/DB and cite it.
2. Eval protocol axes from paper (adapt): task utility · solver-grounded correctness · faithfulness/safe failure · cost/latency.
3. When no solver exists, degrade to schema/range checks — do not pretend physical feasibility.
4. Smart-grid case code: **NO-GO** (no SPDX).

| Verdict | **ADOPT** solver-grounded rule; energy content **REFERENCE**/route-out |

## Snippets

> "When the LLM is the interface and a trusted tool is the source of truth, the agent inherits the tool’s correctness. When the LLM is asked to compute, it does not."
> — [Source: arxiv-2607.18147 Conclusion]
