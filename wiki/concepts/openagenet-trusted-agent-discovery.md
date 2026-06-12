---
title: OpenAgenet (OAN) — pre-connection trust for agent discovery
type: concept
tags: [concept, openagenet, trust, discovery, mcp, k109]
keywords: [2606.03161, did:oan, trusted-discovery, resource-first, governance-vc]
related:
  - sources/arxiv-openagenet-oan-white-paper-2606.03161.md
  - concepts/mcp-server-catalog-curation.md
  - concepts/skill-vetting.md
  - concepts/mcp-context-optimization.md
  - concepts/enterprise-mcp-adoption-practice.md
maturity: draft
created: 2026-06-10
updated: 2026-06-12
---

## Relations

- `@sources/arxiv-openagenet-oan-white-paper-2606.03161.md` — white paper provenance
- `@concepts/mcp-server-catalog-curation.md` — MCP registry vs resource-first discovery
- `@concepts/skill-vetting.md` — Phase-0 trust evidence before install

## Raw Concept

arXiv **2606.03161** — **OpenAgenet (OAN)** trust layer for open agent interconnection: identity provenance, governance state, discovery authorization, freshness, pre-connection trust evidence.

## Narrative

OAN sits **below** MCP, A2A, ANP — does not replace task semantics or tool protocols. Core primitives:

- `did:oan` resource identity
- Governance-backed Root admission + on-chain committee lifecycle
- Registrar-assisted onboarding
- Authorization-aware Discovery + signed invocation
- **Resource-first**: Skills, MCP servers, tool endpoints as verifiable discoverable resources

**Phase-0 verdict:** REFERENCE — `OpenAgenet/oan-public-docs` exists (0★, license **NOASSERTION** via API 2026-06-10). Steal-from for federation catalog trust model; do not depend on production OAN until SPDX license + prototype audit.

### vs Cemini lazy-tool / conductor

| Layer | Role |
|-------|------|
| lazy-tool | Token-efficient MCP proxy (laptop) |
| conductor | Cross-wiki query routing |
| OAN (proposed) | Federated trust + discovery for multi-operator agent networks |

## Snippets

> "When an Agent is discovered in an open environment, who says that this Agent is the one it claims to be?"

> — [Source: arxiv-openagenet-oan-white-paper-2606.03161.md §1, retrieved 2026-06-10]
