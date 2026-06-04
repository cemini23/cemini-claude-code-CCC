---
title: agents-best-practices — Claude agent workflow patterns (MIT, cherry-pick Adopt)
type: entity
tags: [tool, reference, adopt-candidate, k63, k93]
keywords: [agents-best-practices, denissergeevitch, mit, cherry-pick]
related:
  - concepts/skill-vetting.md
  - entities/tools/ai-engineering-roadmap.md
  - concepts/cross-wiki-tool-eval-inventory.md
  - concepts/thin-harness-fat-skills-garrytan.md
  - sources/multi-wiki-tool-eval-v5-k93-2026-06-01.md
  - "@osint-wiki/entities/tools/agents-best-practices.md"
maturity: draft
created: 2026-05-24
updated: 2026-06-04
cross-wiki-source: "@osint-wiki/sources/multi-wiki-tool-eval-36url-wiki-ingestion-2026-05-24.md"
---

## Relations

- `@concepts/skill-vetting.md` — per-pattern Phase-0 before paste into rules/skills
- `@concepts/thin-harness-fat-skills-garrytan.md` — harness vs skills framing (K93)
- `@sources/multi-wiki-tool-eval-v5-k93-2026-06-01.md` — K93 promoted Adopt
- `@osint-wiki/entities/tools/agents-best-practices.md` — OSINT canon

## Raw Concept

`DenisSergeevitch/agents-best-practices` — MIT `[CONFIRMED 2026-06-01]` (~1.5k★). K63 **Defer** → K93 **Adopt (cherry-pick)** — not bulk install.

## Narrative

| Era | Verdict |
|-----|---------|
| K63 | DEFER — overlap with existing CCC patterns |
| K93 | **CONDITIONAL-GO** — steal workflow markdown into wiki/concepts after dedup vs OpenSpec + subagent pages |

**Do not** mirror entire repo into `~/.claude/skills/` — catalog churn + `.cursor/rules/ccc-rejected-cursor-tools.mdc` still says read-only pointer until patterns land in wiki.

### K93 action

Cherry-pick 3–5 non-duplicative patterns per Phase-0 file audit; link steals on target concept pages.

## Phase-0 Audit (2026-06-04)

**Method:** GitHub API + README skim. No `npx skills add`.

| Check | Result |
|-------|--------|
| License | **MIT** — API verified [CONFIRMED] |
| Maturity | **1,774★**; last push **2026-05-30**; single `SKILL.md` meta-skill |
| Install path | `npx skills add DenisSergeevitch/agents-best-practices -g` — global user skills dir |
| Failure mode | **Catalog churn + dedup** — overlaps OpenSpec, subagent-orchestration, skill-vetting pages already in CCC wiki |

**Decision — CONDITIONAL-GO (cherry-pick only).** Per `@concepts/tools-we-dont-use.md` defer cluster and `.cursor/rules/ccc-rejected-cursor-tools.mdc`: **do not bulk install**. Audit `SKILL.md` + supporting markdown for 3–5 patterns not already canon on `@concepts/subagent-orchestration.md` / `@concepts/skill-vetting.md`; file steals as concept snippets. **NO-GO** for `-g` global install until dedup checklist complete.

## Adoption trial (2026-06-04)

| Step | Result |
|------|--------|
| Project skill | **PASS** — `.claude/skills/agents-best-practices/` (SKILL.md + `references/tools-and-permissions.md`) |
| `skill-scanner scan` | **OK** — 1 MEDIUM (review before prod sessions) |
| Wiki steal | **PASS** — harness control plane loop filed on `@concepts/subagent-orchestration.md` |

**Posture:** **ADOPTED (project-scoped cherry-pick)** — not global `-g` install.

## Snippets

> "Promoted Defer → Adopt (MIT verified)" — K93 v5 eval.
> — [Source: @osint-wiki/sources/multi-wiki-tool-eval-v5-k93-2026-06-01.md]
