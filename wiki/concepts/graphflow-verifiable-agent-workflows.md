---
title: GraphFlow — proof-carrying visual workflows for agent automation
type: concept
tags: [concept, agent-workflows, formal-verification, durability, cross-wiki-route]
keywords: [graphflow, requires-ensures, proof-carrying, durable-execution, event-log, swimlanes, verified-core]
related:
  - sources/arxiv-graphflow-2605.14968.md
  - concepts/code-as-agent-harness.md
  - entities/tools/openspec.md
  - entities/patterns/scatter-gather.md
  - entities/tools/cc-wf-studio.md
  - entities/tools/the-architect.md
  - entities/patterns/glasswing-deliberate-disagreement.md
  - entities/tools/conductor-mcp.md
  - "@osint-wiki/concepts/graphflow-verifiable-agent-workflows.md"
  - "@osint-wiki/sources/arxiv-graphflow-verifiable-workflows-2605.14968.md"
  - concepts/plan-then-execute-topological-orchestration.md
  - sources/arxiv-dynamo-topological-orchestration-2606.19382.md
maturity: draft
created: 2026-05-23
updated: 2026-06-20
cross-wiki-source: "@osint-wiki/sources/arxiv-graphflow-verifiable-workflows-2605.14968.md"
---

## Relations

- `@sources/arxiv-graphflow-2605.14968.md` — primary arXiv source (K59)
- `@concepts/code-as-agent-harness.md` — diagram-as-spec vs empirical harness evolution
- `@entities/tools/openspec.md` — markdown spec + acceptance criteria (unverified contracts)
- `@entities/patterns/scatter-gather.md` — LangGraph durability without compile-time proofs
- `@entities/tools/cc-wf-studio.md` — visual CC workflow editor (no proof layer)
- `@entities/tools/the-architect.md` — blueprint generator (no formal verification)
- `@entities/patterns/glasswing-deliberate-disagreement.md` — runtime adversarial gating vs compile-time requires/ensures
- `@entities/tools/conductor-mcp.md` — side-effecting cross-wiki fan-out is a high-stakes workflow candidate

Cross-wiki: `@osint-wiki/concepts/graphflow-verifiable-agent-workflows.md` (stub); `@osint-wiki/sources/agentic-harness-engineering.md` (AHE — observability-driven harness tuning, contrasting philosophy).

## Raw Concept

Routed from `briefs/2026-05-23_k59-skillrae-graphflow-from-osint.md`. Question: **what does formal workflow verification offer Cemini that OpenSpec, LangGraph scatter-gather, and empirical harness search do not?**

## Narrative

GraphFlow (arXiv:2605.14968) treats the **workflow diagram as executable spec** with two modes:

| Mode | Purpose |
|------|---------|
| **Verified core** | Restricted acyclic/sequential subgraphs; **requires/ensures** contracts; proof-checked before library admission |
| **Durable runtime** | Full production graphs (cycles, retries); append-only **event log** + replay (Temporal-like semantics) |

**Pilot [TENTATIVE]:** 8,728 clinical runs, 97.08% completion — prototype **without** verified core; failures attributed to external integrations. Verified core **specified, under development** per source.

### Reliability math (why verification matters)

Independent 90% per-step success → ~35% success over 10 steps [Source: 2605.14968 p.1]. Cemini multi-step sessions (`/goal`, Ralph, conductor fan-out) face the same compounding unless gates exist.

### CCC comparison matrix

| Mechanism | Guarantees | Cemini artifact |
|-----------|------------|-----------------|
| GraphFlow verified core | Compile-time proof before admission | — (not adopted) |
| OpenSpec | Human-readable acceptance criteria | `@entities/tools/openspec.md` |
| Glasswing | Runtime adversarial disagreement | `@entities/patterns/glasswing-deliberate-disagreement.md` |
| AHE | Observability → harness evolution | OSINT source only |
| cc-wf-studio | Visual export, conditional branches | `@entities/tools/cc-wf-studio.md` |
| Scatter-gather | Parallel fan-out + merge | `@entities/patterns/scatter-gather.md` |

### Adoption posture

**Pattern reference only** — design language for high-stakes agent workflows (conductor writes, Tier-2 MCP execution), not a near-term MedFlow port. SkillsVote (2605.18401) deferred per brief.

## Snippets

> "GraphFlow shifts planning into diagrams and contracts, then executes those diagrams under durable semantics with auditable traces."
> — [Source: 2605.14968_graphflow-verifiable-workflows.pdf p.2]

> "Proof-carrying workflow automations … must be satisfied before admission to the automation library."
> — [Source: 2605.14968_graphflow-verifiable-workflows.pdf p.5]
