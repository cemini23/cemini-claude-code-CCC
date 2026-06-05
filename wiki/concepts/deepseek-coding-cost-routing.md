---
title: DeepSeek coding cost routing — cheap model for codegen slices
type: concept
tags: [concept, token-economics, deepseek, routing, k92]
keywords: [peterom, deepseek, cost, routing, 2.5-percent]
related:
  - concepts/llm-routing-deepseek-openrouter-failover.md
  - concepts/token-economics-and-prompt-caching.md
  - entities/tools/claude-code-router.md
  - entities/tools/ttok.md
  - entities/tools/ai-token-monitor.md
  - concepts/karpathy-token-efficiency-patterns.md
  - sources/trading-posts-compilation-12-2026-06-01.md
maturity: draft
created: 2026-06-01
updated: 2026-06-04
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-12-2026-06-01.md"
---

## Relations

- `@concepts/llm-routing-deepseek-openrouter-failover.md` — automatic OpenRouter when DeepSeek balance/quota fails
- `@concepts/token-economics-and-prompt-caching.md` — API-side economics
- `@entities/tools/claude-code-router.md` — local proxy routing pattern
- `@entities/tools/ttok.md` — pre-paste token preview
- `@entities/tools/ai-token-monitor.md` — usage dashboards
- `@concepts/karpathy-token-efficiency-patterns.md` — complementary checklist
- `@sources/trading-posts-compilation-12-2026-06-01.md` — K92 Post 10 (@peterom)

## Raw Concept

K92 Post 10 (@peterom): route **boilerplate codegen** to DeepSeek at ~**2.5%** of frontier cost; keep Opus/Sonnet for architecture and verification **`[TENTATIVE]`** — marketing ratio, not measured in Cemini sessions.

## Narrative

CCC already uses **model tiering** via Claude Code fast/slow + subagent models. Steal **task routing discipline** (cheap draft → expensive review), not a mandatory DeepSeek dependency.

**Verdict:** **REFERENCE** — align with `@concepts/karpathy-token-efficiency-patterns.md`; verify cost claims before policy change.

## Snippets

> DeepSeek coding at ~2.5% cost — K92 Post 10 (@peterom).
