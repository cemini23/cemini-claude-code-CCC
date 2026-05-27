---
title: open-design — modular skill Markdown + BYOK agent wiring (Apache-2.0)
type: entity
tags: [tool, skills, byok, cross-wiki-route, steal-from]
keywords: [open-design, nexu-io, composable-skills, markdown-skills, byok, claude-code, design-systems]
related:
  - entities/mcp-servers/anthropic-skills.md
  - concepts/skill-vetting.md
  - concepts/twelve-rule-claude-md-template.md
  - concepts/context-engineering.md
  - entities/tools/claude-code.md
  - concepts/cross-wiki-tool-eval-inventory.md
  - entities/tools/the-architect.md
  - entities/tools/awesome-cursorrules.md
  - entities/tools/mercury-agent-skills.md
maturity: draft
created: 2026-05-22
updated: 2026-05-27
cross-wiki-source: "@osint-wiki/sources/tool-eval-70urls-k57-2026-05-22.md"
---

## Relations

- `@entities/mcp-servers/anthropic-skills.md` — SKILL.md spec; open-design is a parallel modular-skill *pattern* library
- `@concepts/skill-vetting.md` — any borrowed skill file still passes Phase-0 before install
- `@concepts/twelve-rule-claude-md-template.md` — 31 composable Markdown skills inform CLAUDE.md modularity
- `@concepts/context-engineering.md` — structured skill files reduce ad-hoc prompt bloat
- `@entities/tools/claude-code.md` — one of 12 supported CLI agent targets in upstream BYOK wiring

Cross-wiki: K45 `@osint-wiki/sources/more-links-5-2-arch-eval.md` steal-from note; K57 license **CONFIRMED** Apache-2.0 (`nexu-io/open-design`, ~49.5k★).

## Raw Concept

Routed from `briefs/2026-05-22_k57-local-llm-and-agent-infra-from-osint.md`. Eval tier **Adopt (steal-from)** — extract patterns, do not mirror the 72 design-system catalog.

## Narrative

`nexu-io/open-design` publishes **composable agent skills and design systems as explicit Markdown files**, with BYOK wiring into many CLI coding agents (including Claude Code). CCC interest is **modularity mechanics**, not dependency on remote catalog content (per LESSONS.md spec-only posture).

### Steal-from targets

1. **Skill Markdown modularity** — small, named skill files vs monolithic CLAUDE.md sections.
2. **BYOK agent wiring** — how upstream documents attaching skills to multiple harnesses without forking the core repo.

### Adoption posture

| Check | Status |
|-------|--------|
| License (API) | Apache-2.0 [CONFIRMED 2026-05-22] |
| Phase-0 README | **Pending** — steal-from only until README + last commits reviewed |
| Verdict | **CONDITIONAL-GO (patterns)** — no wholesale catalog mirror |

## Snippets

> "31 composable skills and 72 design systems managed via explicit, highly structured Markdown files... BYOK approach wiring into 12 supported CLI-based coding agents."
> — [Source: @osint-wiki/sources/more-links-5-2-arch-eval.md]
