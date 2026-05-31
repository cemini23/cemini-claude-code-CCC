---
title: everything-claude-code (ECC) — master Claude Code harness bundle (MIT, defer)
type: entity
tags: [tool, claude-code, cross-wiki-stub, defer, k63]
keywords: [everything-claude-code, ecc, affaan-m, agent-harness, defer]
related:
  - entities/tools/claude-code.md
  - concepts/skill-vetting.md
  - concepts/hooks-for-automation.md
  - entities/mcp-servers/anthropic-skills.md
  - concepts/cross-wiki-tool-eval-inventory.md
  - sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md
maturity: draft
created: 2026-05-24
updated: 2026-05-31
cross-wiki-source: "@osint-wiki/sources/multi-wiki-tool-eval-36url-wiki-ingestion-2026-05-24.md"
---

## Relations

- `@entities/tools/claude-code.md` — host harness
- `@concepts/skill-vetting.md` — 300+ skills require per-skill Phase-0 if ever imported
- `@concepts/hooks-for-automation.md` — ships hook recipes; collision risk with claude-mem
- `@entities/mcp-servers/anthropic-skills.md` — SKILL.md surface overlap

Cross-wiki: **canonical detail** on `@osint-wiki/entities/tools/everything-claude-code.md` (K50 Adopt-tier OSINT write-up). GitHub repo `affaan-m/everything-claude-code` (redirects from `affaan-m/ECC`). MIT [CONFIRMED 2026-05-24, ~190k★].

## Raw Concept

K63 URL #16 — eval labels **Defer**: scale demands full Phase-0 before any extract. CCC documents the pointer only; do not mirror the skill matrix (catalog churn risk per LESSONS.md).

## Narrative

### Why defer on CCC side

| Risk | Note |
|------|------|
| Hook collisions | May conflict with `@entities/tools/claude-mem.md` SessionStart |
| Skill volume | Cannot vet 300+ skills in one ingest |
| OSINT already Adopt-tier | Primary harness narrative lives in OSINT wiki |

### K90 v6 note [CONFIRMED 2026-05-31]

Gemini v6 batch lists **Adopt** for `affaan-m/everything-claude-code`. CCC posture **unchanged: DEFER** until dedicated Phase-0 — hook collision with claude-mem SessionStart and 300+ skill vetting queue. See `@sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md`.

### Adoption posture

| Verdict | **DEFER** — Phase-0 before cherry-picking hooks/skills; read OSINT entity first |

## Snippets

> "Defer (~190k★) — Phase-0 before any extract."
> — [Source: briefs/2026-05-24_k63-ccc-cursor-agent-tooling-from-osint.md]
