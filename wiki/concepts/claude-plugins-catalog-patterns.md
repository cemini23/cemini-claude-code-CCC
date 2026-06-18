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
  - concepts/claude-harness-dynamic-workflows-k88.md
  - sources/trading-posts-compilation-42-2026-05-31.md
  - concepts/cross-wiki-tool-eval-inventory.md
  - entities/tools/claude-skill-registry.md
  - entities/tools/pegasus-ai-plugin-marketplace.md
  - sources/arxiv-specification-to-execution-scientific-workflow-2606.18425.md
maturity: draft
created: 2026-05-27
updated: 2026-06-18
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-25-2026-05-27.md"
---

## Relations

- `@entities/commands/plugin.md` — `/plugin install` operational path
- `@entities/tools/cursor-community-plugins.md` — Cursor-side discovery (no LICENSE)
- `@concepts/skill-vetting.md` — every plugin passes Phase-0
- `@entities/tools/claude-code.md` — host harness

Cross-wiki: K72 Post 4 (@aiedge_); K88 Post 4 (@polydao skills ecosystem map — overlaps v5 tool eval).

## Raw Concept

K72 — **Claude plugins guide** patterns: how to browse community marketplaces, evaluate plugin scope, and install without polluting `~/.claude/` with unaudited skills.

K88 Post 4 (@polydao) — **Claude Skills ecosystem map** with GitHub links; cross-ref `@sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md` Adopt rows and `@concepts/claude-harness-dynamic-workflows-k88.md`.

## Narrative

### CCC discipline

1. Prefer **named marketplaces** with SPDX in repo over anonymous zip installs.
2. Run `@concepts/skill-vetting.md` before `/plugin install`.
3. Document adopted plugins in wiki — no silent `settings.json` drift.

| Verdict | **REFERENCE** |

## Snippets

> "Claude plugins catalog patterns."
> — [Source: briefs/2026-05-27_k72-ccc-workflows-from-osint.md, Post 4]
