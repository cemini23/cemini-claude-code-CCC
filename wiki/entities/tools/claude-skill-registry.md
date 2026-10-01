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
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
---

## Relations

- `@concepts/claude-plugins-catalog-patterns.md` — discovery discipline (K88 @polydao overlap)
- `@concepts/skill-vetting.md` — never install from registry without Phase-0
- `@entities/mcp-servers/anthropic-skills.md` — spec-only catalog policy
- `@sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md` — K88 Adopt

## Raw Concept

K88 **Adopt** — `github.com/majiayu000/claude-skill-registry`. Registry index pattern for Claude skills. **License RESOLVED 2026-09-30: MIT** — 658★, pushed 2026-09-30 (actively maintained). [CONFIRMED via GitHub API 2026-09-30] The Adopt verdict stands; license is no longer a blocker. **Phase-0 maturity read 2026-09-30:** 658★, 102 forks, 2 open issues, HTML, pushed 2026-09-30. **Repo size 28,078,272 KB ≈ 28 GB** — it is a generated-artifact/GitHub-Pages catalog, not source. Do **not** clone wholesale; read the generated pages over HTTP instead.

## Narrative

**Steal-from:** index UX for internal skill inventory — do **not** mirror remote registry content into wiki (LESSONS.md churn policy). Wire as **discovery pointer** only.

Prior OSINT eval (`links-5-2`) flagged **license contamination risk** on similarly named registries — re-verify SPDX before any install.

**Verdict:** **CONDITIONAL-GO** — index pattern only until license + sample skill audit pass.

## Snippets

> Registry index pattern — spec + audit, not catalog mirror.
> — [Source: briefs/2026-05-31_k88-ccc-workflows-and-tool-eval-from-osint.md]

## Phase-1 wire (2026-09-30)

`wire_status: policy_wired` → `.cursor/rules/cemini-phase1-policy-wires.mdc`. Index/discovery UX pattern only; do not mirror registry content and do not clone the 28 GB tree.
 **Clone decision 2026-10-01: NO CLONE** (independent of the size problem). The K88 Adopt is for the *index/discovery UX pattern*, and the repo is a generated catalog — the artifact is the data, not the code. Read pages over HTTP.
