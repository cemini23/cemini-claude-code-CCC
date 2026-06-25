---
title: MemClaw
type: entity
tags: [entity, tool, fleet-memory, saas, k125]
keywords: [2606.24535, memclaw, governed-memory, caura]
related:
  - sources/arxiv-governed-shared-memory-2606.24535.md
  - concepts/governed-fleet-shared-memory.md
  - entities/tools/argusfleet.md
  - concepts/agent-memory-stack-comparison.md
  - sources/brief-k125-memclaw-fleet-governance-handoff-2026-06-25.md
maturity: draft
created: 2026-06-25
updated: 2026-06-25
---

## Relations

- `@sources/arxiv-governed-shared-memory-2606.24535.md`
- `@concepts/governed-fleet-shared-memory.md`
- `@entities/tools/argusfleet.md` — eval harness (paper-cited)

## Raw Concept

MemClaw — SaaS governed shared memory for multi-agent LLM fleets (https://memclaw.net). K125 ingest from 2606.24535.

## Narrative

| Field | Value |
|-------|-------|
| **Type** | SaaS memory layer |
| **URL** | https://memclaw.net |
| **License** | SaaS ToS — not Phase-0 cloned |
| **Verdict** | **REFERENCE** — eval ideas only; no prod until scope model + ToS audited |
| **Overlap** | claude-mem (single-user), conductor cross-wiki routing |

**Features (paper):** scope tags, provenance chains, supersession on shared facts across agent fleet.

**Cybersec handoff:** scope-enforcement gap checklist → `@cybersecurity-wiki/briefs/2026-06-25_k125-memclaw-fleet-memory-governance-handoff.md`.

## Snippets

> Governed shared memory with MemClaw as the fleet memory substrate.
> — [Source: arxiv-2606.24535-governed-shared-memory-for-multi-agent-llm-syste.pdf, retrieved 2026-06-25]
