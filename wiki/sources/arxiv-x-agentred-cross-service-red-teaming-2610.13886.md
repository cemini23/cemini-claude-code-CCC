---
title: "X-AgentRed: Red-Teaming Personal Agents in Evolving Multi-Service Ecos (CCC K448)"
type: source
tags: [source, arxiv, k448]
keywords: [2610.13886, k448]
related:
  - concepts/cross-service-compositional-harm-graph.md
  - concepts/agent-data-injection-attacks.md
  - concepts/hybrid-mcp-tool-discovery-lazy-catalog.md
  - concepts/mcp-tool-taxonomy-navigation.md
  - concepts/agent-approval-laundering-transitive-effects.md
  - briefs/2026-10-12_ccc-k445-k448-sip-ready.md
maturity: draft
read_status: deep-read
created: 2026-10-12
updated: 2026-10-12
---

## Relations

- `@concepts/cross-service-compositional-harm-graph.md`
- `@concepts/agent-data-injection-attacks.md`
- `@concepts/hybrid-mcp-tool-discovery-lazy-catalog.md`
- `@concepts/mcp-tool-taxonomy-navigation.md`
- `@concepts/agent-approval-laundering-transitive-effects.md`
- `@briefs/2026-10-12_ccc-k445-k448-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | X-AgentRed: Red-Teaming Personal Agents in Evolving Multi-Service Ecosystems |
| **arXiv** | 2610.13886 (2026-10) |
| **Retrieved** | 2026-10-12 |

## Narrative

**Verdict: ADOPT pattern (cross-service composition risk).**

**Compose many tools across services and the failure is compositional — so explore the composition graph, not the model's memory.** X-AgentRed red-teams **personal agents in a multi-service ecosystem** (30 services, 914 tools). The finding: when a benign request drives actions whose effects **accumulate across services**, unintended or harmful outcomes arise, and **an LLM asked to propose harmful paths is biased toward familiar tools**, leaving novel cross-service combinations unexplored. The fix is structural: a **HarmFlow graph** built from each tool's **preconditions, effects and potential harms** (an edge where one tool's effect satisfies another's precondition), from which recipes are sampled by **backward random walks** and instantiated as benign-looking scenarios; execution feedback then **diversifies** successful paths by substituting adjacent tools and **refines** blocked paths by repairing unmet preconditions. Results: **1.77× / 10.36× the harmful-path rate of STAC / TRACE** and **2.99× / 1.84× tool coverage**; diversification reaches **27.7%** HPR vs **18.0%** for random sampling. **CCC reading:** this is the multi-MCP composition risk the CCC harness lane trades on — *a per-tool analysis cannot see harm that exists only in the sequence*, and **graph traversal beats model recall** for finding those sequences. It also validates the K444/K447 principle that **the structure, not the model, is where you get coverage**. Pairs `agent-data-injection-attacks` / `hybrid-mcp-tool-discovery-lazy-catalog` / `mcp-tool-taxonomy-navigation`. Cross-domain REFERENCE. Runtime `wont_wire`; concept `policy_wired`.

## Snippets

> "an agent fulfilling a benign user request can leak information as its actions interact across services." [Source: arXiv 2610.13886 (retrieved 2026-10-12)]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2610.13886-x-agentred-red-teaming-personal-agents-in-evolvi.pdf` (local inbox **pending archive** — tailnet down 2026-10-12) |
