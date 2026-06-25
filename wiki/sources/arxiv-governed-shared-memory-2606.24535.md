---
title: Governed shared memory for multi-agent LLM systems (arXiv 2606.24535)
type: source
tags: [source, arxiv, fleet-memory, governance, memclaw, k125]
keywords: [2606.24535, memclaw, argusfleet, scope, supersession, provenance]
related:
  - concepts/governed-fleet-shared-memory.md
  - entities/tools/memclaw.md
  - entities/tools/argusfleet.md
  - concepts/agent-memory-stack-comparison.md
  - concepts/etclovg-harness-layers.md
  - sources/brief-k125-memclaw-fleet-governance-handoff-2026-06-25.md
  - sources/brief-k125-memory-orchestration-cluster-2026-06-25.md
maturity: draft
read_status: read
created: 2026-06-25
updated: 2026-06-25
---

## Relations

- `@concepts/governed-fleet-shared-memory.md` — scope/provenance/supersession synthesis
- `@entities/tools/memclaw.md` — MemClaw SaaS eval harness
- `@sources/brief-k125-memclaw-fleet-governance-handoff-2026-06-25.md` — cybersec scope-enforcement handoff

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Governed Shared Memory for Multi-Agent LLM Systems |
| **Authors** | Caura / MemClaw team |
| **arXiv** | 2606.24535 |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2606.24535-governed-shared-memory-for-multi-agent-llm-syste.pdf` |
| **Retrieved** | 2026-06-25 |
| **Read status** | read (MemClaw + ArgusFleet eval) |

## Narrative

Defines **governed fleet memory** — shared store where writes carry **scope tags**, **provenance**, and **supersession** rules so multi-agent fleets don't clobber or leak facts across trust boundaries. **MemClaw** (https://memclaw.net) is the SaaS memory layer; **ArgusFleet** cited as open eval harness (public GitHub 404 at Phase-0 — treat as paper artifact until repo ships).

**CCC relevance:** Governance layer for ETCLOVG **Governance** + **Context** when conductor routes cross-wiki facts. Scope-enforcement gap → `@cybersecurity-wiki` handoff. **REFERENCE** for MemClaw; no prod fleet until scope model audited.

## Snippets

> Governed shared memory with scope, provenance, and supersession for multi-agent LLM fleets.
> — [Source: arxiv-2606.24535-governed-shared-memory-for-multi-agent-llm-syste.pdf abstract, retrieved 2026-06-25]
