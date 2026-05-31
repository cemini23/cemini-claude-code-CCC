---
title: Claude Code subagent templates — 15-minute dispatch patterns
type: concept
tags: [concept, subagents, claude-code, templates, k88]
keywords: [0x_rody, subagent, task-tool, agent-template, bounded-scope]
related:
  - concepts/subagent-orchestration.md
  - entities/patterns/tier1-tier2-agent-model.md
  - entities/patterns/scatter-gather.md
  - concepts/agent-completion-verification-gates.md
  - entities/tools/claude-code.md
  - sources/trading-posts-compilation-42-2026-05-31.md
maturity: draft
created: 2026-05-31
updated: 2026-05-31
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-42-2026-05-31.md"
---

## Relations

- `@concepts/subagent-orchestration.md` — when to dispatch vs inline work
- `@entities/patterns/tier1-tier2-agent-model.md` — scope envelope for subagents
- `@entities/patterns/scatter-gather.md` — parallel fan-out variant
- `@concepts/agent-completion-verification-gates.md` — done criteria before merge
- `@entities/tools/claude-code.md` — host harness
- `@sources/trading-posts-compilation-42-2026-05-31.md` — K88 Post 2 provenance

Cross-wiki: K88 Post 2 (@0x_rody).

## Raw Concept

K88 Post 2 (@0x_rody): **15-minute subagent template** — bounded Task/Agent invocations with explicit inputs, outputs, and time box. CCC maps to existing Tier-1/Tier-2 + verification gate patterns rather than a new framework **`[TENTATIVE]`**.

## Narrative

### Template shape (steal-from)

1. **Scope lock** — one deliverable (file, brief section, lint fix batch)
2. **Time box** — ~15 min wall clock; abort with partial + handoff note
3. **Context budget** — point subagent at ≤3 wiki pages + one raw source
4. **Return contract** — structured summary + `@path` pages touched + open questions
5. **Parent verification** — parent runs `wiki_lint.py` or test before accepting

### vs Cemini defaults

| Pattern | CCC already has |
|---------|-----------------|
| Bounded subagent | Cursor Task tool + `tier1-tier2-agent-model` |
| Parallel research | `scatter-gather` with conductor |
| Long-horizon | `/goal` + OpenSpec, not 15-min boxes |

**Verdict:** **REFERENCE** — paste template into `briefs/` when delegating repetitive wiki ingest slices.

## Snippets

> Subagent 15-min template (@0x_rody) — bounded dispatch with explicit return contract.
> — [Source: briefs/2026-05-31_k88-ccc-workflows-and-tool-eval-from-osint.md, Post 2]
