---
title: Governed fleet shared memory
type: concept
tags: [concept, fleet-memory, governance, scope, k125]
keywords: [2606.24535, memclaw, scope, provenance, supersession]
related:
  - sources/arxiv-governed-shared-memory-2606.24535.md
  - entities/tools/memclaw.md
  - entities/tools/argusfleet.md
  - concepts/agent-memory-stack-comparison.md
  - concepts/etclovg-harness-layers.md
  - concepts/mcp-trust-orchestration-collaboration.md
  - sources/brief-k125-memclaw-fleet-governance-handoff-2026-06-25.md
  - sources/brief-k125-memory-orchestration-cluster-2026-06-25.md
maturity: draft
created: 2026-06-25
updated: 2026-06-25
---

## Relations

- `@sources/arxiv-governed-shared-memory-2606.24535.md` — MemClaw paper
- `@concepts/agent-memory-stack-comparison.md` — memory backend taxonomy
- `@concepts/etclovg-harness-layers.md` — Governance + Context layers

## Raw Concept

Question: how do multi-agent fleets share memory without cross-scope leaks, stale facts, or ungoverned overwrites?

## Narrative

**Governed fleet shared memory** [TENTATIVE — 2606.24535]: every write carries **scope** (agent/team/tenant), **provenance** (source session/tool), and **supersession** rules (new fact retires old under same key). Evaluated via MemClaw SaaS + ArgusFleet harness.

**Steal-from for Cemini harness:**

1. **Scope tags on wiki facts** — maturity + `related:` edges as lightweight scope; supersession via `[RETRACTED]` + date.
2. **Fleet ≠ laptop** — claude-mem + hot.md are single-operator; fleet patterns REFERENCE until scope enforcement audited.
3. **Cybersec handoff** — scope-enforcement gap analysis → `@cybersecurity-wiki/briefs/2026-06-25_k125-memclaw-fleet-memory-governance-handoff.md`.

**Verdict:** MemClaw **REFERENCE**; ArgusFleet **REFERENCE** pending public repo.

## Snippets

> Scope, provenance, and supersession as first-class metadata on shared multi-agent memory.
> — [Source: arxiv-2606.24535-governed-shared-memory-for-multi-agent-llm-syste.pdf, retrieved 2026-06-25]
