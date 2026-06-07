---
title: claude-skill-registry — skill registry index pattern (Phase-0 pending)
type: entity
tags: [tool, skills, registry, adopt-candidate, k88]
keywords: [claude-skill-registry, majiayu000, skill-index, catalog]
related:
  - concepts/claude-plugins-catalog-patterns.md
  - concepts/skill-vetting.md
  - entities/mcp-servers/anthropic-skills.md
  - sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md
  - entities/tools/agent-skill-manager.md
maturity: draft
created: 2026-05-31
updated: 2026-06-07
---

## Relations

- `@concepts/claude-plugins-catalog-patterns.md` — discovery discipline (K88 @polydao overlap)
- `@concepts/skill-vetting.md` — never install from registry without Phase-0
- `@entities/mcp-servers/anthropic-skills.md` — spec-only catalog policy
- `@sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md` — K88 Adopt

## Raw Concept

K88 **Adopt** — `github.com/majiayu000/claude-skill-registry`. Registry index pattern for Claude skills. License: verify on Phase-0 **`[NEEDS VERIFICATION 2026-05-31]`** if not in K88 spot-check table.

## Narrative

**Steal-from:** index UX for internal skill inventory — do **not** mirror remote registry content into wiki (LESSONS.md churn policy). Wire as **discovery pointer** only.

Prior OSINT eval (`links-5-2`) flagged **license contamination risk** on similarly named registries — re-verify SPDX before any install.

**Verdict:** **CONDITIONAL-GO** — index pattern only until license + sample skill audit pass.

## Snippets

> Registry index pattern — spec + audit, not catalog mirror.
> — [Source: briefs/2026-05-31_k88-ccc-workflows-and-tool-eval-from-osint.md]
