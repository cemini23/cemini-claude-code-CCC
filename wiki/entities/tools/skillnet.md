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
updated: 2026-06-04
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

**Verdict:** **CONDITIONAL-GO (REFERENCE-first)** — must prove gap vs lazy-tool + conductor before any routing layer.

## Phase-0 Audit (2026-06-04)

**Method:** GitHub API + README skim. No install.

| Check | Result |
|-------|--------|
| License | **MIT** — API verified [CONFIRMED] |
| Maturity | **1,014★**; PyPI `skillnet-ai`; last push **2026-05-27**; arXiv 2603.04448 |
| Claims | "500,000+ community skills" — **catalog churn risk** (same class as SkillKit marketplace inflation) |
| Failure mode | **Parallel routing layer** duplicates `@entities/tools/lazy-tool.md` + `@entities/tools/conductor-mcp.md` federation map |

**Decision — CONDITIONAL-GO (REFERENCE).** Clean license and active research repo. **No prod adopt** until a documented gap exists that lazy-tool `search_tools` + conductor cannot cover. Acceptable use: discovery URL queue for `@concepts/skill-vetting.md` — never one-line install from community index without Phase-0 per skill.

## Snippets

> Skill routing vs lazy-tool catalog — do not duplicate federation router.
> — [Source: @osint-wiki/entities/tools/skillnet.md]
