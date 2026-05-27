---
title: Claude plugins catalog patterns — marketplace discovery discipline
type: concept
tags: [concept, claude-code, plugins, marketplace, k72]
keywords: [aiedge, claude-plugins, marketplace, plugin-catalog]
related:
  - entities/commands/plugin.md
  - entities/tools/cursor-community-plugins.md
  - concepts/skill-vetting.md
  - entities/tools/claude-code.md
  - concepts/cross-wiki-tool-eval-inventory.md
maturity: draft
created: 2026-05-27
updated: 2026-05-27
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-25-2026-05-27.md"
---

## Relations

- `@entities/commands/plugin.md` — `/plugin install` operational path
- `@entities/tools/cursor-community-plugins.md` — Cursor-side discovery (no LICENSE)
- `@concepts/skill-vetting.md` — every plugin passes Phase-0
- `@entities/tools/claude-code.md` — host harness

Cross-wiki: K72 Post 4 (@aiedge_).

## Raw Concept

K72 — **Claude plugins guide** patterns: how to browse community marketplaces, evaluate plugin scope, and install without polluting `~/.claude/` with unaudited skills.

## Narrative

### CCC discipline

1. Prefer **named marketplaces** with SPDX in repo over anonymous zip installs.
2. Run `@concepts/skill-vetting.md` before `/plugin install`.
3. Document adopted plugins in wiki — no silent `settings.json` drift.

| Verdict | **REFERENCE** |

## Snippets

> "Claude plugins catalog patterns."
> — [Source: briefs/2026-05-27_k72-ccc-workflows-from-osint.md, Post 4]
