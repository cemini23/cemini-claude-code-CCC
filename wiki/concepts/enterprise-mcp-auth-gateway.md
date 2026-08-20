---
title: Enterprise MCP auth gateway — persona × credential (K271)
type: concept
tags: [concept, mcp, auth, gateway, k271]
keywords: [2608.10760, BYOT, GYOT, SSO, service-account]
related:
  - sources/arxiv-enterprise-mcp-auth-gateway-2608.10760.md
  - entities/tools/enterprise-mcp-auth-gateway.md
  - concepts/schema-bound-mcp-tool-surface.md
  - concepts/mcp-claim-validation-and-parameter-grounding.md
  - sources/brief-k270-k273-mcp-acm-wave-2026-08-12.md
  - briefs/2026-08-12_ccc-handoff-k270-k273-ingest.md
  - concepts/phase1-adopt-wire.md
  - concepts/signed-mandate-mcp-protocol-enforcement.md
  - sources/arxiv-mandato-signed-mandates-mcp-2608.14074.md
  - sources/arxiv-enterprise-multi-agent-analytics-2608.18740.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-12
updated: 2026-08-20
---

## Relations

- `@sources/arxiv-enterprise-mcp-auth-gateway-2608.10760.md`
- `@entities/tools/enterprise-mcp-auth-gateway.md`
- `@concepts/schema-bound-mcp-tool-surface.md`

## Raw Concept

How should fleets of MCP servers share authentication and identity without per-server snowflakes?

## Narrative

K271 industry pattern: **central gateway** + two axes (persona × credential) + BYOT/GYOT/token-exchange + explicit user vs service-account flows.

### Steal (ADOPT)

1. Prefer one auth aggregation layer in front of many MCP servers for prod/enterprise.
2. Classify callers as **user vs non-user** before picking credential path.
3. Support BYOT vs gateway-issued tokens; plan offboarding across the fleet.
4. Do not invent a Cemini gateway product from this paper alone — policy/architecture only.

| Verdict | **ADOPT** policy. |
