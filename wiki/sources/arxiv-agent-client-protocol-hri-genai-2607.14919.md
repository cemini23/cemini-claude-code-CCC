---
title: "Human-Robot Interaction in GenAI Architectures via the Agent-Client Protocol"
type: source
tags: [source, arxiv, acp, mcp, hri, coding-agent, k182]
keywords: [2607.14919, ACP, Agent-Client Protocol, Sancho, three-layer]
related:
  - concepts/acp-mcp-three-layer-human-agent-execution.md
  - concepts/client-as-first-order-harness-factor.md
  - concepts/mcp-contract-grounded-synthesis-and-validation-gate.md
  - entities/tools/sancho-acp-clients.md
  - sources/brief-k182-acp-mcp-three-layer-2026-07-17.md
maturity: draft
created: 2026-07-17
updated: 2026-07-17
---

## Relations

- `@concepts/acp-mcp-three-layer-human-agent-execution.md`
- `@entities/tools/sancho-acp-clients.md` — Apache-2.0 clients; core `MAPIRlab/sancho` 404
- `@concepts/client-as-first-order-harness-factor.md`
- `@sources/brief-k182-acp-mcp-three-layer-2026-07-17.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Human-Robot Interaction in GenAI Architectures via the Agent-Client Protocol |
| **Author** | Moncada-Ramirez, Ruiz-Sarmiento, Gonzalez-Jimenez |
| **arXiv** | 2607.14919 |
| **Code** | `MAPIRlab/sancho-acp-clients` (Apache-2.0); `MAPIRlab/sancho` **404** |
| **Retrieved** | 2026-07-17 |

## Narrative

MCP standardizes agent↔execution; HRI/UI layer is still ad hoc. Paper adopts **ACP** (Agent-Client Protocol, from coding-agent world) for UI↔agent, with MCP below for agent↔robot. Fully decoupled **three layers**: human interaction / deliberative orchestration / physical execution. Enables swap of UIs or robot backends; supports observability, **explicit human authorization**, and immediate interruption. Evaluated on physical Sancho mobile robot across three heterogeneous UIs.

CCC steal: same topology for Claude Code/Cursor UI ↔ agent ↔ tools/MCP — keep authorization and interrupt as first-class, not chat-only.

## Snippets

> "combining ACP at the interface-agent link and MCP at the agent-execution link" — Abstract
