---
title: SkillRAE — retrieval-augmented execution via skill-graph compilation
type: concept
tags: [concept, agent-skills, context-engineering, skill-graph, rae, cross-wiki-route]
keywords: [skillrae, retrieval-augmented-execution, skill-graph, context-compilation, skillsbench, subunit-compilation, rescue-aware]
related:
  - sources/arxiv-skillrae-2605.10114.md
  - concepts/code-as-agent-harness.md
  - concepts/context-engineering.md
  - concepts/mcp-context-optimization.md
  - entities/tools/lazy-tool.md
  - entities/tools/conductor-mcp.md
  - concepts/skill-vetting.md
  - entities/mcp-servers/anthropic-skills.md
  - entities/tools/openspec.md
  - entities/tools/the-architect.md
  - "@osint-wiki/concepts/skillrae-retrieval-augmented-execution.md"
  - "@osint-wiki/sources/arxiv-skillrae-agent-skills-2605.10114.md"
  - entities/tools/skillnet.md
maturity: draft
created: 2026-05-23
updated: 2026-05-31
cross-wiki-source: "@osint-wiki/sources/arxiv-skillrae-agent-skills-2605.10114.md"
---

## Relations

- `@sources/arxiv-skillrae-2605.10114.md` — primary arXiv source (K59)
- `@concepts/code-as-agent-harness.md` — harness substrate; SkillRAE compiles *into* executor context after harness tool/skill selection
- `@concepts/context-engineering.md` — post-selection context budget discipline
- `@concepts/mcp-context-optimization.md` — lazy-tool compresses *tool* catalogs; SkillRAE addresses *skill* libraries
- `@entities/tools/lazy-tool.md` — complementary layer (which tools) vs SkillRAE (how to compile chosen skills)
- `@entities/tools/conductor-mcp.md` — routing picks wikis/pages; SkillRAE would compile skill subunits for execution
- `@concepts/skill-vetting.md` — Phase-0 before any skill enters the graph
- `@entities/mcp-servers/anthropic-skills.md` — SKILL.md spec for procedural bundles SkillRAE assumes
- `@entities/tools/openspec.md` — spec-as-contract vs compiled skill context

Cross-wiki: `@osint-wiki/concepts/skillrae-retrieval-augmented-execution.md` (stub); `@osint-wiki/sources/arxiv-skillrae-agent-skills-2605.10114.md`.

## Raw Concept

Routed from `briefs/2026-05-23_k59-skillrae-graphflow-from-osint.md` (K59 Tier-B sweep). Question: **after Cemini selects skills/tools, how should executor context be compiled so the window isn't wasted on globally relevant but locally under-resolved skill text?**

## Narrative

**Retrieval-Augmented Execution (RAE)** extends RAG from facts to **procedural skills** (SKILL.md bundles with scripts, assets, conventions). Prior work optimizes *which* skills to retrieve; SkillRAE (arXiv:2605.10114) optimizes **compilation** — turning a coarse retrieved set into compact, dependency-ordered, executor-ready context.

### Pipeline (survey-level)

| Phase | Content |
|-------|---------|
| Offline | Multi-level **skill graph**: communities → skills → reusable **subunits** with dependency edges |
| Online | Ranked retrieval → subunit export → **rescue-aware compilation** (recover dropped evidence) |
| Claim | +11.7% on SkillsBench vs prior SOTA; gains from compilation, not prompt stuffing [TENTATIVE — skimmed source only] |

### Cemini stack mapping

| Layer | Cemini today | SkillRAE would add |
|-------|--------------|-------------------|
| Tool catalog | `@entities/tools/lazy-tool.md`, harness `ToolSearch` | — |
| Skill library | Installed skills + `@concepts/skill-vetting.md` | Graph + compiler over vetted skills |
| Cross-wiki retrieval | `@entities/tools/conductor-mcp.md` | — |
| Executor context | Manual `hot.md`, claude-mem injection | Automated subunit compilation |

### Adoption posture

**Not a near-term production port** — research reference for wiki skill-library design and future conductor context shaping. No new npm/pip dependency from this paper.

Contrast: `@entities/tools/open-design.md` modular Markdown skills (authoring pattern) vs SkillRAE (runtime compilation theory).

## Snippets

> "A retrieved skill set may be globally relevant, but still under-resolved for execution."
> — [Source: arXiv:2605.10114 via @sources/arxiv-skillrae-2605.10114.md]

> "SKILLRAE compiles a coarse-ranked skill set into a task-specific context that is compact, grounded, and immediately usable."
> — [Source: 2605.10114_skillrae-agent-skills.pdf p.1]
