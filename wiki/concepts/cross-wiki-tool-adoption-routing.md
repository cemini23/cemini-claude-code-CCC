---
title: Cross-wiki tool adoption routing — Phase-0 trial matrix (2026-06-04)
type: concept
tags: [concept, cross-wiki-routing, phase-0, tool-eval, adoption]
keywords: [adoption routing, ccc-wiki, cybersecurity-wiki, osint-wiki, phase-0 trials]
related:
  - concepts/skill-vetting.md
  - concepts/cross-wiki-routing.md
  - concepts/cross-wiki-tool-eval-inventory.md
  - concepts/k73-phase0-audit-decisions.md
  - concepts/seclaw-agent-security-evaluation.md
  - entities/tools/defenseclaw.md
  - entities/tools/lazy-tool.md
  - entities/tools/skillnet.md
  - entities/tools/skill-seekers.md
  - entities/tools/webwright.md
  - entities/tools/revfactory-harness.md
  - entities/tools/openevolve.md
  - entities/tools/agents-best-practices.md
  - entities/tools/scienceaix-agentskills.md
  - "@cybersecurity-wiki/entities/tools/defenseclaw.md"
maturity: draft
created: 2026-06-04
updated: 2026-06-04
---

## Relations

- `@concepts/skill-vetting.md` — Phase-0 gate all wikis share
- `@concepts/cross-wiki-routing.md` — federation map
- `@concepts/k73-phase0-audit-decisions.md` — two-gate policy (eval ≠ adopt)
- `@entities/tools/defenseclaw.md` — CCC scanner adoption
- `@cybersecurity-wiki/entities/tools/defenseclaw.md` — runtime sidecar depth

## Raw Concept

Full trial run 2026-06-04 (`/tmp/ccc-trials-full-20260604/`) for nine Phase-0 backlog tools. This page records **which wiki owns each adoption** and what landed where.

## Narrative

### Routing matrix

| Tool | Primary wiki | Secondary | Trial result | Adoption landed |
|------|--------------|-----------|--------------|-----------------|
| **openevolve** | **ccc-wiki** | osint-wiki (harness token opt) | Smoke PASS; library-only (no CLI) | `scripts/openevolve-phase0-smoke.sh`; isolated venv |
| **Webwright** | **ccc-wiki** | osint-wiki (public URL verify) | Doctor 4/6; plugin SSH fail | `.claude/skills/webwright/` + pip CLI |
| **Skill_Seekers** | **ccc-wiki** | all domain wikis (export pipeline) | SKILL.md + package; enhance needs interactive Claude | CLI `skill-seekers create ./wiki/...` workflow |
| **SkillNet** | **ccc-wiki** (REFERENCE) | — | Search works; overlaps lazy-tool + conductor | **No install** — URL queue only |
| **revfactory/harness** | **ccc-wiki** | — | Plugin installed; generation blocked (org API) | `harness@harness-marketplace` user plugin |
| **agents-best-practices** | **ccc-wiki** | all wikis (pattern steals) | Dedup vs wiki; 4 refs copied | `.claude/skills/agents-best-practices/` + subagent steal |
| **defenseclaw** | **cybersecurity-wiki** (sidecar) + **ccc-wiki** (scanners) | — | `make all` PASS; doctor 13/26; scanners SAFE | `~/.local/bin/{defenseclaw,skill-scanner,mcp-scanner}`; vetting step 3b |
| **SeClaw** | **cybersecurity-wiki** (benchmark) | ccc-wiki (trajectory methodology) | NO LICENSE; README-only repo | **NO-GO install** — brief handoff only |
| **scienceaix/agentskills** | **ccc-wiki** (REFERENCE) | all wikis (skill discovery) | MIT; 8 top-level files; stale Feb 2026 | **No clone** — ingest queue for skill-vetting |

### Wiki-specific actions

**ccc-wiki (this repo) — DONE**

- Project skills: `webwright`, `agents-best-practices` (+ 4 reference files).
- `@concepts/skill-vetting.md` — optional `skill-scanner` pre-flight (step 3b).
- `@concepts/subagent-orchestration.md` — harness control-plane steal.
- Plugin: `harness@harness-marketplace` (user scope).

**cybersecurity-wiki — handoff (not edited this session)**

- `@cybersecurity-wiki/entities/tools/defenseclaw.md` — deepen with sidecar install + `DEFENSECLAW_LLM_KEY` trial.
- SeClaw stub when LICENSE + code ship — see `briefs/2026-06-04_cybersecurity-handoff-defenseclaw-seclaw.md`.

**osint-wiki — defer**

- openevolve token/routing optimization only if OSINT harness experiments need it.
- Webwright for prod-boundary browser tasks (not Cursor default).

**Domain wikis (gambling, seo, 3d-printing, image-gen) — defer**

- Skill_Seekers export pipeline when a domain wiki wants `.claude/skills/` from its `wiki/` tree.

### SkillNet vs lazy-tool (trial finding)

SkillNet `search "skill vetting"` returns community skills (e.g. `skill-vetter`) with quality scores — useful as **discovery**, not routing. `@entities/tools/lazy-tool.md` + `@entities/tools/conductor-mcp.md` already cover MCP/tool federation for Cemini. **No SkillNet routing layer** until a documented gap appears.

### Deployment scope — laptop vs prod vs projects [CONFIRMED 2026-06-04]

Adoptions **do not** fan out automatically.

| Surface | Applies | Does not apply |
|---------|---------|----------------|
| **Mac user Claude plugins** (`scope: user`) | All Claude Code sessions for that OS user on the Mac | `cemini-prod` (`root`), other OS users |
| **Project `.claude/skills/`** (CCC repo) | Sessions with CCC as project root | CeminiSuite `/opt/cemini`, sibling wiki folders |
| **Cursor** (`~/.cursor/`, built-in browser) | Cursor agent sessions | Claude Code CLI on prod |
| **cemini-prod** | Own plugins, `vet_skill.py`, `approved_skills.json` | Laptop harness/meta tools unless briefed + vetted |
| **cemini-librarian** | Wiki sync, stash MCP | Claude Code harness adoptions from this batch |

**Prod handoff:** `briefs/2026-06-04_phase0-adoption-scope-cemini-prod.md` → `cemini-prod:/opt/cemini/briefs/` — Phase 1 doc + optional `skill-scanner` trial; **NO-GO** on harness/openevolve/Skill_Seekers install.

## Snippets

> "Two-gate policy: doc-level eval verdicts are not adoption verdicts."
> — [Source: @concepts/k73-phase0-audit-decisions.md]
