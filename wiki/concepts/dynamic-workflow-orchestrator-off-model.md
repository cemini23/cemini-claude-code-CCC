---
title: Dynamic workflow orchestrator off-model — six patterns (K107)
type: concept
tags: [concept, harness, orchestration, k107]
keywords: [pawelhuryn, ultracode, classify-and-act, fan-out, zero-token-glue]
related:
  - concepts/claude-harness-dynamic-workflows-k88.md
  - concepts/subagent-orchestration.md
  - concepts/token-economics-and-prompt-caching.md
  - entities/patterns/scatter-gather.md
  - sources/trading-posts-compilation-7-2026-06-09.md
  - concepts/agent-rubrics-self-correction.md
  - entities/tools/conductor-mcp.md
  - concepts/the-hive-loop-routines-pattern.md
  - sources/trading-posts-compilation-8-2026-06-09.md
  - concepts/recursive-agent-harness-harness-recursion.md
  - sources/arxiv-recursive-agent-harnesses-2606.13643.md
maturity: draft
created: 2026-06-09
updated: 2026-06-15
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-7-2026-06-09.md"
---

## Relations

- `@concepts/claude-harness-dynamic-workflows-k88.md` — K88/K97 prior dynamic-workflow cluster
- `@concepts/subagent-orchestration.md` — fan-out / Task tool mapping
- `@concepts/token-economics-and-prompt-caching.md` — zero-token glue loops
- `@entities/patterns/scatter-gather.md` — fan-out-and-synthesize pattern
- `@sources/trading-posts-compilation-7-2026-06-09.md` — K107 Post 0 (@PawelHuryn)

## Raw Concept

K107 Post 0 (@PawelHuryn): **orchestrator moved off the model into code** — 113-agent ultracode-style system; coordination loops spend **zero model tokens**. Anthropic @trq212 dynamic-workflows post cited in source.

## Narrative

### Six workflow patterns [TENTATIVE — single X post]

| Pattern | Harness mapping |
|---------|-----------------|
| Classify-and-act | Router script / conductor intent → subagent type |
| Fan-out-and-synthesize | Task tool scatter-gather (`@entities/patterns/scatter-gather.md`) |
| Adversarial verification | `@entities/patterns/glasswing-deliberate-disagreement.md` |
| Generate-and-filter | Rubric gate before merge (`@concepts/agent-rubrics-self-correction.md`) |
| Tournament | Best-of-N harness proposals (cf. RHO self-preference) |
| Loop-until-done | Ralph `/goal` acceptance envelope |

**Boundary:** dynamic workflows ≠ n8n replacement (explicit in K107 source). CCC uses **code orchestrator + thin harness** — not a new third-party workflow engine without Phase-0.

## Snippets

> "The orchestrator moved off the model and into code. The agents do the work; the code that coordinates them spends zero model tokens." [Source: Posts.docx K107, @PawelHuryn Post 0]
