---
title: scienceaix/agentskills — Agent Skills survey resource catalog
type: entity
tags: [tool, agent-skills, catalog, reference-only]
keywords: [scienceaix, agentskills, 2602.12430, skill-resources]
related:
  - sources/arxiv-agent-skills-architecture-security-2602.12430.md
  - concepts/agent-skills-progressive-disclosure.md
  - concepts/skill-vetting.md
  - entities/mcp-servers/anthropic-skills.md
  - concepts/agent-skills-taxonomy.md
maturity: draft
created: 2026-06-04
updated: 2026-06-04
---

## Relations

- `@sources/arxiv-agent-skills-architecture-security-2602.12430.md` — companion paper (2602.12430)
- `@concepts/agent-skills-progressive-disclosure.md` — architecture synthesis
- `@concepts/skill-vetting.md` — Phase-0 before any catalog install
- `@entities/mcp-servers/anthropic-skills.md` — official Anthropic skills surface

## Raw Concept

`github.com/scienceaix/agentskills` — curated **agent skills resources** linked from AgentSkills '26 survey (2602.12430). Discovery catalog, not a Cemini dependency.

## Narrative

| Check | Status |
|-------|--------|
| License | **MIT** — GitHub API + root `LICENSE` [CONFIRMED 2026-06-04] |
| Overlap | `@entities/mcp-servers/anthropic-skills.md`, `@concepts/cross-wiki-tool-eval-inventory.md` |
| Verdict | **REFERENCE** — URL queue for skill_audit; no bulk clone into `~/.claude/skills/` |

## Phase-0 Audit (2026-06-04)

**Method:** GitHub API + LICENSE file verify. No clone.

| Check | Result |
|-------|--------|
| License | **MIT** — API + `LICENSE` file [CONFIRMED] |
| Maturity | **71★**; last push **2026-02-16** — stale vs paper (2602.12430) |
| Purpose | Curated agent-skills resource links from AgentSkills '26 survey — discovery catalog |
| Failure mode | **Catalog churn** — third-party skill URLs require per-URL Phase-0 |

**Decision — REFERENCE (unchanged).** License cleared; adoption posture unchanged. Use as ingest queue for `@concepts/skill-vetting.md`, not as installed dependency.

## Snippets

> "An accompanying collection of agent skills resources is available at https://github.com/scienceaix/agentskills."
> — [Source: arxiv-2602.12430 p.1]
