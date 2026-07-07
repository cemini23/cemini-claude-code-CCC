---
title: CCC handoff — HexStrike client-first-order orchestration ingest
type: brief
tags: [brief, ccc-handoff, harness, tool-orchestration, evaluation]
created: 2026-07-07
related:
  - meta/ccc-cross-wiki-handoff-briefs.md
  - concepts/client-as-first-order-harness-factor.md
  - sources/brief-k140-hexstrike-client-orchestration-2026-07-07.md
updated: 2026-07-07
---

## Target

Claude Desktop / Claude Code | model-selection + eval discipline

## Summary

Cybersec-wiki ingest 2026-07-07: arXiv **2607.02873** (HexStrike-AI, 774 picoCTF trials) — the **driving client/harness is a first-order capability factor** (2.1× solve-rate gap, same model). Empirically upgrades the CCC "harness is everything" thesis. Phase-0 **Reference**.

## Body

### Why CCC cares

David compares models for super-audit slots, subagents, and bot backends. This paper proves a model number is meaningless without the harness named — the same model swung 2.1× across clients.

### Operating changes

- Record `(model, client/harness, tool-regime)` in every model comparison, not model alone.
- Fix **tool descriptions + agent behavior** before swapping models — that produced the 55.4%→72.0% lift.
- Expose fewer, sharper tools (residual failures were reasoning-bound) — corroborates lazy-tool least-privilege.

### Eval stack

| Lane | Wiki |
|------|------|
| Harness-first evidence | **NEW** `@concepts/client-as-first-order-harness-factor.md` |
| Primary synthesis | `@cybersecurity-wiki/concepts/security-tool-orchestration-determinants.md` |
| Least-privilege tools | `@cybersecurity-wiki/concepts/agent-least-privilege-tool-selection.md` |
| Completion proof | `@ccc-wiki/concepts/agent-completion-verification-gates.md` |

### Staged brief

- `@cybersecurity-wiki/briefs/2026-07-07_hexstrike-client-first-order-orchestration-checklist.md`

## Sources

- @cybersecurity-wiki/sources/arxiv-2607-02873-hexstrike-security-tool-orchestration.md
- @cybersecurity-wiki/concepts/security-tool-orchestration-determinants.md
