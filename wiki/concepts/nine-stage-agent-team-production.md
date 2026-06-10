---
title: Nine-stage AI agent team — production pipeline pattern
type: concept
tags: [concept, agent-team, production, k90]
keywords: [0xcodez, nine-stage, agent-team, software-factory]
related:
  - concepts/claude-code-software-factory.md
  - concepts/subagent-orchestration.md
  - concepts/agent-completion-verification-gates.md
  - concepts/claude-prompt-engineering-techniques.md
  - sources/trading-posts-compilation-16-2026-05-31.md
  - concepts/progressive-autonomy-incident-resolution.md
  - sources/arxiv-autonomous-hyperscale-incident-resolution-2606.09122.md
maturity: draft
created: 2026-05-31
updated: 2026-06-10
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-16-2026-05-31.md"
---

## Relations

- `@concepts/claude-code-software-factory.md` — sibling multi-agent codegen metaphor (K67)
- `@concepts/subagent-orchestration.md` — bounded fan-out
- `@concepts/agent-completion-verification-gates.md` — stage exit criteria
- `@concepts/claude-prompt-engineering-techniques.md` — same author cluster (K72 Post 5)
- `@sources/trading-posts-compilation-16-2026-05-31.md` — K90 Post 10 (@0xCodez)

## Raw Concept

K90 Post 10 (@0xCodez): **9-stage agent team** for shipping production software — role-specialized agents per stage with handoff contracts **`[TENTATIVE]`** — post is workflow marketing, not verified Cemini pipeline.

## Narrative

Map stages to CCC primitives without adopting a new framework:

1. **Plan / spec** — OpenSpec or `/goal`
2. **Implement** — Claude Code primary session
3. **Review** — Tier-2 subagent or `@entities/patterns/glasswing-deliberate-disagreement.md`
4. **Verify** — lint + tests + `@concepts/agent-completion-verification-gates.md`

**Verdict:** **REFERENCE** — compare stage count to `@concepts/harness-de-bloat-4x4-pattern.md` before copying.

## Snippets

> 9-stage AI agent team production (@0xCodez) — K90 Post 10.
> — [Source: briefs/2026-05-31_k90-ccc-agent-harness-from-osint.md]
