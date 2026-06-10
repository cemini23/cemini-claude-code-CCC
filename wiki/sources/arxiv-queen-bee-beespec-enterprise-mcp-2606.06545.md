---
title: Queen-Bee BeeSpec enterprise MCP orchestration (arXiv 2606.06545)
type: source
tags: [source, arxiv, queen-bee, beespec, mcp, enterprise, governance, k109]
keywords: [2606.06545, queen-bee, beespec, tenant-isolation, tool-governance]
related:
  - concepts/queen-bee-beespec-enterprise-orchestration.md
  - concepts/subagent-orchestration.md
  - concepts/skill-vetting.md
  - entities/tools/defenseclaw.md
  - concepts/mcp-server-catalog-curation.md
maturity: draft
read_status: read
created: 2026-06-10
updated: 2026-06-10
---

## Relations

- `@concepts/queen-bee-beespec-enterprise-orchestration.md` — BeeSpec IR + Cemini Tier mapping
- `@concepts/subagent-orchestration.md` — Queen control plane vs Bee execution plane
- `@concepts/skill-vetting.md` — policy profile + allowed_tools as governance gate
- `@entities/tools/defenseclaw.md` — admission-control parallel for enterprise MCP
- `@concepts/mcp-server-catalog-curation.md` — MCP + skill registries in prototype

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Queen-Bee Agents: A BeeSpec-Centered Architecture for Governed Enterprise MCP Orchestration |
| **Authors** | Dutao Zhang, Liaotian (Macao Polytechnic University) |
| **arXiv** | 2606.06545v1 [cs.SE] |
| **Location** | `raw-sources/arxiv-2606.06545-queen-bee-agents-a-beespec-centered-architecture.pdf` |
| **Retrieved** | 2026-06-10 |
| **Read status** | read (architecture, BeeSpec schema, eval metrics) |

## Narrative

**Queen-Bee** separates **Queen control plane** (capability retrieval, blueprint planning, BeeSpec compilation, governance) from **Bee execution plane** (scoped tool use under BeeSpec). **BeeSpec** IR fields: `bee_id`, `role`, `domain`, `tenant_scope`, `memory_scope`, `attached_skills`, `allowed_tools`, `policy_profile`, `approval_gate`. Python prototype with real stdio MCP adapters, tenant-scoped connectors, audit-backed policy checks. On 59 enterprise-style tasks: retrieval-driven variant **0.964** success, **zero governance failures** vs permissive single-agent baseline.

**CCC relevance:** steal-from pattern for Tier-1/Tier-2 scope compilation — explicit execution boundary before subagent dispatch.

## Snippets

> "Rather than sending a request directly to an execution agent, the Queen first retrieves relevant capabilities, plans the execution boundary, and compiles a BeeSpec containing the role, attached skills, allowed MCP-backed tools, tenant scope, memory scope, and policy profile for a Bee."

> "The retrieval-driven Queen-Bee variant achieves a task success rate of 0.964, zero governance failures."

> — [Source: arxiv-2606.06545-queen-bee-agents-a-beespec-centered-architecture.pdf §1, §6, retrieved 2026-06-10]
