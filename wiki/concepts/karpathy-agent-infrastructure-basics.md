---
title: Karpathy agent infrastructure basics — seven foundational layers
type: concept
tags: [concept, karpathy, agent-harness, infrastructure, k88]
keywords: [scottybeamio, karpathy, agent-basics, state, tools, eval, orchestration]
related:
  - concepts/karpathy-token-efficiency-patterns.md
  - concepts/twelve-rule-claude-md-template.md
  - concepts/code-as-agent-harness.md
  - concepts/subagent-orchestration.md
  - sources/trading-posts-compilation-42-2026-05-31.md
maturity: draft
created: 2026-05-31
updated: 2026-05-31
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-42-2026-05-31.md"
---

## Relations

- `@concepts/karpathy-token-efficiency-patterns.md` — sibling Karpathy post cluster (K72 savings vs K88 infrastructure)
- `@concepts/twelve-rule-claude-md-template.md` — durable context layer
- `@concepts/code-as-agent-harness.md` — three-layer harness mapping
- `@concepts/subagent-orchestration.md` — delegation boundary
- `@sources/trading-posts-compilation-42-2026-05-31.md` — K88 Post 0 provenance

Cross-wiki: `@osint-wiki/sources/trading-posts-compilation-42-2026-05-31.md` Post 0 (@ScottyBeamIO).

## Raw Concept

K88 Post 0 (@ScottyBeamIO): **Karpathy-style seven basics** for agent infrastructure — foundational layers before stacking tools (Obsidian, Hermes, swarms). CCC treats as a **pre-flight checklist** for harness design, not a product install list **`[TENTATIVE]`** — post is synthesis, not Anthropic canon.

## Narrative

| Layer (numbered framing) | CCC mapping |
|--------------------------|-------------|
| Clear task + eval | `@entities/patterns/full-prompt-goal-template.md`, `@concepts/agent-completion-verification-gates.md` |
| Tool surface discipline | `@entities/tools/lazy-tool.md`, MCP allowlists |
| State / memory ownership | `@entities/tools/claude-mem.md`, `hot.md`, Obsidian git vault — one owner per layer |
| Model routing | Tier-1/Tier-2, `@concepts/subagent-orchestration.md` |
| Harness feedback | Hooks (`Stop`, verification gates), not unbounded loops |
| Human checkpoint | Brief-before-ingest, Phase-0 audits |
| Simplicity budget | `@concepts/harness-de-bloat-4x4-pattern.md` |

**Verdict:** **REFERENCE** — use as onboarding scaffold for new harness contributors; verify each layer against CCC pages before Adopt.

## Snippets

> Karpathy 7 basics — agent infrastructure before tool stack sprawl.
> — [Source: Posts.docx K88 Post 0, @ScottyBeamIO; briefs/2026-05-31_k88-ccc-workflows-and-tool-eval-from-osint.md]
