---
title: Agent personality file — OpenClaw/Hermes de-genericization pattern
type: concept
tags: [concept, hermes, openclaw, personality, k90]
keywords: [voxyz, personality-file, hermes, openclaw, generic-assistant]
related:
  - concepts/agent-token-discipline-openclaw-hermes.md
  - entities/tools/hermes-agent.md
  - entities/tools/build-your-own-openclaw.md
  - concepts/agent-memory-stack-comparison.md
  - sources/trading-posts-compilation-16-2026-05-31.md
  - sources/trading-posts-compilation-12-2026-06-01.md
maturity: draft
created: 2026-05-31
updated: 2026-06-01
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-16-2026-05-31.md"
---

## Relations

- `@concepts/agent-token-discipline-openclaw-hermes.md` — token waste when personality + memory reload unbounded
- `@entities/tools/hermes-agent.md` — reference runtime (not prod)
- `@entities/tools/build-your-own-openclaw.md` — OpenClaw successor framing
- `@sources/trading-posts-compilation-16-2026-05-31.md` — K90 Post 2 (@Voxyz_ai)
- `@sources/trading-posts-compilation-12-2026-06-01.md` — K92 Post 12 (@Voxyz_ai, reaffirm)

## Raw Concept

K90 Post 2 / **K92 Post 12** (@Voxyz_ai): **agent personality file** — structured markdown (voice, boundaries, anti-patterns) so OpenClaw/Hermes agents stop sounding like generic assistants. CCC maps to **Skills.md / CLAUDE.md patterns**, not Hermes install **`[TENTATIVE]`**.

## Narrative

| Personality layer | CCC equivalent |
|-------------------|----------------|
| Voice + tone | `@concepts/claude-md-five-section-template.md` Style section |
| Hard boundaries | `.cursor/rules/` + hook allowlists |
| Anti-patterns | `@concepts/tools-we-dont-use.md` |
| Session memory | `@entities/tools/claude-mem.md` — not Hermes `MEMORY.md` in prod |

**Verdict:** **REFERENCE** — steal file structure into project rules; Hermes/OpenClaw remain reference-only.

## Snippets

> "5 Lessons for an Agent Personality File: Get OpenClaw and Hermes Past the Generic Assistant"
> — [Source: Posts.docx K90 Post 2, @Voxyz_ai]
