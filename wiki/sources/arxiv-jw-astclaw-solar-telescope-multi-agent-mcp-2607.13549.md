---
title: "JW-ASTClaw: Multi-Agent Framework for Autonomous Solar Telescope"
type: source
tags: [source, arxiv, multi-agent, mcp, graceful-degradation, astronomy, k173]
keywords: [2607.13549, JW-ASTClaw, SFMM, perception-decision-execution, MCP]
related:
  - concepts/mcp-multi-agent-graceful-degradation-stack.md
  - concepts/mcp-contract-grounded-synthesis-and-validation-gate.md
  - concepts/subagent-orchestration.md
  - concepts/client-as-first-order-harness-factor.md
  - sources/brief-k173-mcp-graceful-degradation-2026-07-16.md
maturity: draft
created: 2026-07-16
updated: 2026-07-16
---

## Relations

- `@concepts/mcp-multi-agent-graceful-degradation-stack.md` — synthesized steal
- `@concepts/subagent-orchestration.md` — multi-agent orchestration peer
- `@sources/brief-k173-mcp-graceful-degradation-2026-07-16.md` — prod brief stub

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | JW-ASTClaw: A Generalizable Multi-Agent Framework for Autonomous Solar Telescope… |
| **Author** | Tong, Lin, Deng, et al. (NAOC / Chinese Meridian Project) |
| **Type** | Research in Astronomy and Astrophysics preprint |
| **arXiv** | 2607.13549 |
| **Retrieved** | 2026-07-16 |
| **Pages** | 17 |
| **Code** | none public at Phase-0 |

## Narrative

First LLM-driven multi-agent control on an operational solar telescope (SFMM). **Three-layer** perception–decision–execution wired by **MCP**. Perception agents (data-quality, cloud-analyzer, flare-detector) encode observer expertise as LLM-callable rules; central reasoner fuses/conflicts. **Graceful degradation**: cloud LLM → local inference → rule-based fallback for remote stations with bad connectivity. Portability claim: reuse perception/decision; swap telescope-specific execution interfaces only.

Astronomy primary domain — CCC steals architecture patterns only. No public repo → **REFERENCE**.

## Snippets

> "supports graceful degradation from cloud LLM to local inference and finally to rule-based fallback" — Abstract

> — [Source: arxiv-2607.13549, retrieved 2026-07-16]
