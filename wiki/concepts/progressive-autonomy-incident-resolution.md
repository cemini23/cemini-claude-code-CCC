---
title: Progressive autonomy for incident resolution — agentic AIOps pattern
type: concept
tags: [concept, aiops, progressive-autonomy, multi-agent, k109]
keywords: [2606.09122, incident-resolution, skills-mcp, closed-loop-verification]
related:
  - sources/arxiv-autonomous-hyperscale-incident-resolution-2606.09122.md
  - concepts/subagent-orchestration.md
  - concepts/agent-completion-verification-gates.md
  - concepts/nine-stage-agent-team-production.md
  - concepts/agent-harness-operational-definition.md
  - "@cybersecurity-wiki/concepts/agentic-aiops-autonomous-incident-resolution.md"
maturity: draft
created: 2026-06-10
updated: 2026-06-10
---

## Relations

- `@sources/arxiv-autonomous-hyperscale-incident-resolution-2606.09122.md` — production architecture paper
- `@concepts/subagent-orchestration.md` — hierarchical specialist agents
- `@concepts/agent-completion-verification-gates.md` — closed-loop verification before close
- `@concepts/nine-stage-agent-team-production.md` — production agent-team staging
- `@cybersecurity-wiki/concepts/agentic-aiops-autonomous-incident-resolution.md` — SRE primary domain stub

## Raw Concept

arXiv **2606.09122** — hyperscale **autonomous incident resolution** via multi-agent orchestration, MCP-inspired **skills**, runbook encoding, **progressive autonomy** with promotion/demotion and rollback.

## Narrative

Five operational generations ending in **autonomous** detect → diagnose → remediate → verify. Architectural principles:

1. Hierarchical agent decomposition (specialists, not one monolith)
2. Skills-based tool invocation (composable, governed, MCP-shaped)
3. Structured knowledge from operational runbooks
4. **Progressive autonomy** — increment authority with safety invariants
5. Closed-loop verification + rollback

Production claim: **>90%** autonomous resolution for common incident classes [TENTATIVE — vendor paper, undisclosed provider].

### CCC steal-from

| Pattern | Cemini analogue |
|---------|-----------------|
| Progressive promotion | Tier-1 → Tier-2 scope expansion with telemetry |
| Skills as MCP packages | SKILL.md + MCP tool bundles per workflow |
| Closed-loop verify | `@concepts/agent-completion-verification-gates.md` |
| Rollback | git revert + harness flaw records |

Primary SRE/AIOps synthesis: `@cybersecurity-wiki/concepts/agentic-aiops-autonomous-incident-resolution.md`.

## Snippets

> "Rather than proposing a binary shift from manual to fully autonomous, the architecture enables organizations to incrementally increase agent authority while maintaining safety invariants at every level."

> — [Source: arxiv-autonomous-hyperscale-incident-resolution-2606.09122.md §I, retrieved 2026-06-10]
