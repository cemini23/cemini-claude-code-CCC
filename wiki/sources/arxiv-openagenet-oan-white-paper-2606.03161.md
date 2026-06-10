---
title: OpenAgenet / OAN trusted agent interconnection (arXiv 2606.03161)
type: source
tags: [source, arxiv, openagenet, oan, trust, discovery, k109]
keywords: [2606.03161, openagenet, did:oan, trusted-discovery, agent-internet]
related:
  - concepts/openagenet-trusted-agent-discovery.md
  - concepts/mcp-server-catalog-curation.md
  - concepts/skill-vetting.md
maturity: draft
read_status: read
created: 2026-06-10
updated: 2026-06-10
---

## Relations

- `@concepts/openagenet-trusted-agent-discovery.md` — trust-layer synthesis
- `@concepts/mcp-server-catalog-curation.md` — resource-first registry vs MCP-only catalogs
- `@concepts/skill-vetting.md` — pre-connection trust evidence parallel to skill Phase-0

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | OpenAgenet / OAN White Paper: Open Infrastructure for Trusted Agent Interconnection |
| **Author** | Jinliang Xu (CAICT) |
| **arXiv** | 2606.03161 |
| **Project** | https://github.com/OpenAgenet/oan-public-docs (0★, NOASSERTION license API 2026-06-10) |
| **Location** | `raw-sources/arxiv-2606.03161-openagenet-oan-white-paper-open-infrastructure-f.pdf` |
| **Retrieved** | 2026-06-10 |
| **Read status** | read (executive summary, roles, MCP/A2A/ANP positioning) |

## Narrative

**OAN** is a protocol-neutral **pre-connection trust layer** for open agent networks: `did:oan` identity, governance-backed admission, Registrar onboarding, Root-verified package publication, authorization-aware Discovery, infrastructure authorization VCs, signed trusted invocation. **Resource-first** stance — Agent Services, Skills, MCP Servers, Tool/API endpoints as discoverable verifiable resources. Does not replace MCP, A2A, or ANP; sits beneath task semantics.

**CCC relevance:** catalog curation + federation trust model for multi-operator MCP; prototype status — REFERENCE until open repo + license verified.

## Snippets

> "OAN is designed as a protocol-neutral trust layer. It does not replace Agent interaction protocols, tool protocols, model orchestration frameworks, or application-level workflows."

> "OAN instead treats Agent Services, Skills, MCP Servers, and Tool/API endpoints as first-class discoverable resources whose identities, lifecycle, packages, and discovery responses must be verifiable."

> — [Source: arxiv-2606.03161-openagenet-oan-white-paper-open-infrastructure-f.pdf §1, retrieved 2026-06-10]
