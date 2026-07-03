---
title: Queen-Bee BeeSpec — governed enterprise MCP orchestration
type: concept
tags: [concept, queen-bee, beespec, mcp, governance, enterprise, k109]
keywords: [2606.06545, beespec, tenant-scope, allowed-tools, policy-profile]
related:
  - sources/arxiv-queen-bee-beespec-enterprise-mcp-2606.06545.md
  - concepts/subagent-orchestration.md
  - entities/patterns/tier1-tier2-agent-model.md
  - concepts/skill-vetting.md
  - entities/tools/defenseclaw.md
  - concepts/mcp-server-catalog-curation.md
  - concepts/mcp-context-optimization.md
  - concepts/enterprise-mcp-adoption-practice.md
  - sources/brief-k109-bayesian-agent-harness-cluster-prod-2026-06-10.md
maturity: draft
created: 2026-06-10
updated: 2026-07-03
---

## Relations

- `@sources/arxiv-queen-bee-beespec-enterprise-mcp-2606.06545.md` — prototype + eval provenance
- `@concepts/subagent-orchestration.md` — Queen control plane vs Bee workers
- `@entities/patterns/tier1-tier2-agent-model.md` — tenant_scope + allowed_tools as compile-time scope
- `@concepts/skill-vetting.md` — policy_profile before tool invocation
- `@entities/tools/defenseclaw.md` — enterprise admission-control parallel

## Raw Concept

arXiv **2606.06545** — **Queen-Bee** architecture with **BeeSpec** intermediate representation between planning and execution in enterprise MCP environments.

## Narrative

Four layers: Queen control plane → **BeeSpec** IR → Bee execution plane → tenant-scoped MCP connectors.

**BeeSpec** compiles execution boundary before any tool call:

| Field | Purpose |
|-------|---------|
| `tenant_scope` | MCP calls confined to tenant |
| `allowed_tools` | MCP tools authorized for this Bee |
| `attached_skills` | Skills driving local plans |
| `policy_profile` | Guardrails checked per invocation |
| `approval_gate` | Optional human gate (chemistry workflow) |

Prototype results (59 tasks): retrieval-driven Queen-Bee **96.4%** success, **zero governance failures** vs permissive single-agent baseline [TENTATIVE — prototype scale].

### Cemini steal-from [TENTATIVE]

Compile a **scope envelope** (analogous to BeeSpec) in parent prompt before `Task` / subagent dispatch: allowed MCP servers, skill list, Tier, rollback path. Maps to `@entities/patterns/tier1-tier2-agent-model.md` + `@concepts/ship-subagent-writer-reviewer-tester.md` approval gates.

## Snippets

> "The Queen decides what a Bee is allowed to do; the Bee runtime carries out the task under those constraints."

> — [Source: arxiv-queen-bee-beespec-enterprise-mcp-2606.06545.md §4.2, retrieved 2026-06-10]
