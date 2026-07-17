---
title: ACP + MCP three-layer human / agent / execution split
type: concept
tags: [concept, acp, mcp, architecture, human-in-the-loop, k182]
keywords: [2607.14919, Agent-Client Protocol, authorization, interrupt]
related:
  - sources/arxiv-agent-client-protocol-hri-genai-2607.14919.md
  - entities/tools/sancho-acp-clients.md
  - concepts/client-as-first-order-harness-factor.md
  - concepts/mcp-contract-grounded-synthesis-and-validation-gate.md
  - concepts/cage-1-enterprise-agent-governance-eval.md
  - sources/brief-k182-acp-mcp-three-layer-2026-07-17.md
maturity: draft
created: 2026-07-17
updated: 2026-07-17
---

## Relations

- `@sources/arxiv-agent-client-protocol-hri-genai-2607.14919.md` — K182 provenance
- `@concepts/client-as-first-order-harness-factor.md` — UI/client matters (K140)
- `@concepts/cage-1-enterprise-agent-governance-eval.md` — human authorization / Prebind

## Raw Concept

Where should human UI, agent orchestration, and tool execution meet?

## Narrative

### Steal

| Layer | Protocol | Responsibility |
|-------|----------|----------------|
| Human ↔ Agent | **ACP** (or equivalent UI contract) | Observability, explicit auth, interrupt |
| Agent ↔ Execution | **MCP** | Tools/skills/runtime |
| Execution | robot / shell / APIs | Side effects |

Do not collapse UI auth into free-form chat. Keep interrupt and authorization native.

### Verdict

**ADOPT** three-layer checklist for Cemini agent UIs. **CONDITIONAL** local `sancho-acp-clients` (Apache) as ACP examples; core robot repo missing.

## Snippets

> "native support for … real-time observability, explicit human authorization, and immediate task interruption" — Abstract
