---
title: Agent skills progressive disclosure — SKILL.md three-level loading
type: concept
tags: [concept, agent-skills, skill-md, mcp, progressive-disclosure]
keywords: [2602.12430, level-1-metadata, level-2-instructions, level-3-resources, skills-vs-mcp]
related:
  - sources/arxiv-agent-skills-architecture-security-2602.12430.md
  - concepts/agent-skills-taxonomy.md
  - concepts/thin-harness-fat-skills-garrytan.md
  - concepts/skill-vetting.md
  - entities/mcp-servers/anthropic-skills.md
  - concepts/mcp-context-optimization.md
  - entities/tools/lazy-tool.md
  - concepts/muse-autoskill-skill-lifecycle.md
  - entities/tools/scienceaix-agentskills.md
  - concepts/agentic-memory-cross-scenario-generality.md
maturity: draft
created: 2026-06-04
updated: 2026-06-05
---

## Relations

- `@sources/arxiv-agent-skills-architecture-security-2602.12430.md` — arXiv 2602.12430 provenance
- `@concepts/agent-skills-taxonomy.md` — procedural-gap survey (2605.07358)
- `@concepts/thin-harness-fat-skills-garrytan.md` — social framing
- `@concepts/skill-vetting.md` — security gate before Level-2/3 load
- `@entities/mcp-servers/anthropic-skills.md` — Anthropic open standard
- `@concepts/mcp-context-optimization.md` — MCP as complementary connectivity layer
- `@entities/tools/lazy-tool.md` — deferred tool surface analog for MCP catalog

## Raw Concept

2602.12430 formalizes **progressive disclosure** as the defining Agent Skills architecture: load procedural knowledge in three stages to avoid context penalty while retaining deep resources on demand.

## Narrative

### Three levels [CONFIRMED via 2602.12430]

| Level | Content | Token cost | When loaded |
|-------|---------|------------|-------------|
| **1 — Metadata** | YAML frontmatter (`name`, `description`) | ~30 tokens/skill | Always in system prompt |
| **2 — Instructions** | Full SKILL.md body | 200–2k tokens | On semantic trigger |
| **3 — Resources** | Scripts, reference docs, assets | Unbounded | Only if Level-2 invokes |

Skills **modify agent preparation** (context + pre-approved tools), not direct function output — distinct from MCP tool calls.

### Skills vs MCP [CONFIRMED via 2602.12430 Table 1]

| Dimension | Agent Skills | MCP |
|-----------|--------------|-----|
| Role | Procedural knowledge | Tool connectivity |
| Unit | Directory + SKILL.md | Server + endpoints |
| Loaded | Agent on trigger | Client on config |
| Persistence | Filesystem | Session |

**Cemini mapping:** `.claude/skills/` + `@entities/tools/lazy-tool.md` for MCP catalog cost; `@concepts/skill-vetting.md` before community skill GO.

**Verdict:** **REFERENCE** — aligns with existing CCC skill/MCP split; no new framework install.

## Snippets

> "Level 1 serves as a table of contents; Level 2 provides the chapter content; Level 3 supplies the technical appendices."

> — [Source: arxiv-2602.12430 p.3, retrieved 2026-06-04]
