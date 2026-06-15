---
title: Claude harness dynamic workflows — AGENTS.md + plugin patterns (K88 cluster)
type: concept
tags: [concept, claude-code, agents-md, plugins, harness, k88]
keywords: [agents-md, dynamic-workflow, plugin-discipline, token-discipline, k88-posts]
related:
  - concepts/harness-de-bloat-4x4-pattern.md
  - concepts/claude-plugins-catalog-patterns.md
  - concepts/agent-token-discipline-openclaw-hermes.md
  - concepts/claude-md-five-section-template.md
  - entities/tools/claude-code.md
  - sources/trading-posts-compilation-42-2026-05-31.md
  - concepts/thin-harness-fat-skills-garrytan.md
  - concepts/runtime-context-mcp-file-refs.md
  - sources/trading-posts-compilation-17-2026-06-03.md
  - concepts/dynamic-workflow-orchestrator-off-model.md
  - sources/trading-posts-compilation-7-2026-06-09.md
  - concepts/the-hive-loop-routines-pattern.md
  - concepts/ship-subagent-writer-reviewer-tester.md
  - sources/trading-posts-compilation-8-2026-06-09.md
  - concepts/recursive-agent-harness-harness-recursion.md
  - sources/arxiv-recursive-agent-harnesses-2606.13643.md
maturity: draft
created: 2026-05-31
updated: 2026-06-15
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-42-2026-05-31.md"
---

## Relations

- `@concepts/harness-de-bloat-4x4-pattern.md` — complexity ceiling
- `@concepts/claude-plugins-catalog-patterns.md` — marketplace install discipline
- `@concepts/agent-token-discipline-openclaw-hermes.md` — token waste anti-patterns (K88 posts 8, 15)
- `@concepts/claude-md-five-section-template.md` — CLAUDE.md vs AGENTS.md split
- `@entities/tools/claude-code.md` — host harness
- `@sources/trading-posts-compilation-42-2026-05-31.md` — Posts 8, 15, 27–29, 32–34, 38
- `@sources/trading-posts-compilation-17-2026-06-03.md` — K97 Post 3 (@0xCodez Anthropic engineer dynamic workflows)

## Raw Concept

K88 **Claude harness post cluster** (multiple authors): dynamic workflows via **AGENTS.md**, plugin catalogs, and session discipline. CCC synthesizes as **pattern references** — no new third-party install without Phase-0.

## Narrative

| Theme | CCC take |
|-------|----------|
| AGENTS.md routing | Parallel to `.cursor/rules/` + `CLAUDE.md`; keep one schema owner per repo |
| Plugin sprawl | `@concepts/claude-plugins-catalog-patterns.md` + `@concepts/skill-vetting.md` |
| Token discipline | `@concepts/agent-token-discipline-openclaw-hermes.md` |
| Dynamic mode switches | Compare to `/loop` and Plan agent — document in brief, don't fork harness |
| Runtime grounding (K97 Post 3–4) | Pair with `@concepts/runtime-context-mcp-file-refs.md` — MCP + file refs before dynamic routing |

**Verdict:** **REFERENCE** — mine posts for brief-ready snippets; file deltas into existing concept pages.

## Snippets

> K88 harness cluster — AGENTS.md, plugins, token discipline (Posts 8, 15, 27–34, 38).
> — [Source: briefs/2026-05-31_k88-ccc-workflows-and-tool-eval-from-osint.md]
