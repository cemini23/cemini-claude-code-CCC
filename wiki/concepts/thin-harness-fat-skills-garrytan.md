---
title: Thin harness, fat skills — garrytan agent factory pattern
type: concept
tags: [concept, harness, skills, k93]
keywords: [garrytan, thin-harness, fat-skills, gstack, gbrain, resolver, agent-factory]
related:
  - concepts/harness-updating-vs-benefit-nonmonotonic.md
  - concepts/claude-harness-dynamic-workflows-k88.md
  - concepts/harness-de-bloat-4x4-pattern.md
  - entities/tools/revfactory-harness.md
  - concepts/skill-vetting.md
  - sources/trading-posts-compilation-31-2026-06-01.md
  - entities/tools/agents-best-practices.md
  - concepts/system-scaling-harness-agentic-ai.md
  - sources/arxiv-system-scaling-harness-2605.26112.md
  - concepts/agent-skills-taxonomy.md
  - sources/arxiv-agent-skills-survey-2605-07358-2026-06-02.md
  - concepts/runtime-harness-interface-adaptation.md
maturity: draft
created: 2026-06-01
updated: 2026-06-03
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-31-2026-06-01.md"
---

## Relations

- `@concepts/harness-updating-vs-benefit-nonmonotonic.md` — arXiv: harness **benefit** needs executor that follows artifacts
- `@concepts/claude-harness-dynamic-workflows-k88.md` — AGENTS.md / plugin cluster
- `@concepts/harness-de-bloat-4x4-pattern.md` — opposite de-bloat move (4×4 simplification)
- `@entities/tools/revfactory-harness.md` — K93 Adopt meta-team generator
- `@concepts/skill-vetting.md` — fat skills still Phase-0 per skill
- `@sources/trading-posts-compilation-31-2026-06-01.md` — K93 Posts (@garrytan)

## Raw Concept

K93 Posts (@garrytan): **thin harness + fat skills** — minimal routing/orchestration layer; bulk of behavior in **skills** and resolvers (GStack / `gbrain` framing) **`[TENTATIVE]`** — social thread, not Cemini-validated prod architecture.

## Narrative

| Layer | CCC mapping |
|-------|-------------|
| Thin harness | `.cursor/rules/` + `CLAUDE.md` + conductor routing — avoid duplicate orchestrators |
| Fat skills | `~/.claude/skills/` + project skills — `@concepts/skill-vetting.md` per install |
| Resolvers | Task-tool / subagent dispatch tables — `@concepts/subagent-orchestration.md` |

**Verdict:** **REFERENCE** — align with arXiv 2605.30621: invest executor discipline + skill quality over harness churn.

## Snippets

> "Thin Harness, Fat Skills" — @garrytan (K93 Posts.docx).
