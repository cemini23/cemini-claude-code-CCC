---
title: SkillNet (zjunlp) — skill network routing (Phase-0 pending)
type: entity
tags: [tool, skills, routing, adopt-candidate, k88]
keywords: [skillnet, zjunlp, agent-skills, skill-routing]
related:
  - entities/tools/lazy-tool.md
  - entities/tools/conductor-mcp.md
  - concepts/skillrae-retrieval-augmented-execution.md
  - sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md
  - "@osint-wiki/entities/tools/skillnet.md"
  - concepts/skill-vetting.md
maturity: draft
created: 2026-05-31
updated: 2026-05-31
cross-wiki-source: "@osint-wiki/entities/tools/skillnet.md"
---

## Relations

- `@entities/tools/lazy-tool.md` — deferred MCP tool catalog (compare routing model)
- `@entities/tools/conductor-mcp.md` — prod cross-wiki router
- `@concepts/skillrae-retrieval-augmented-execution.md` — post-retrieval skill compilation
- `@sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md` — K88 Adopt

## Raw Concept

K88 **Adopt** — `github.com/zjunlp/SkillNet`. MIT. Skill network / agent skill routing framework (ZJU NLP).

## Narrative

Compare vs **lazy-tool** `search_tools` + **conductor** before prod adopt. Risk: parallel routing layer duplicates federation map in `CLAUDE.md`.

**Verdict:** **CONDITIONAL-GO** — Phase-0 must prove gap vs existing lazy-tool + skill audit stack.

## Snippets

> Skill routing vs lazy-tool catalog — do not duplicate federation router.
> — [Source: @osint-wiki/entities/tools/skillnet.md]
