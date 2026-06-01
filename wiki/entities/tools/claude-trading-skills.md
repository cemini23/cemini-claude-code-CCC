---
title: claude-trading-skills (tradermonty)
type: entity
tags: [tool, skills, trading, adopt]
keywords: [claude-trading-skills, tradermonty, skills, k92-eval]
related:
  - concepts/skill-vetting.md
  - entities/mcp-servers/anthropic-skills.md
  - concepts/claude-code-finance-research-setup.md
  - sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md
  - "@osint-wiki/sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md"
maturity: validated
created: 2026-06-01
updated: 2026-06-01
laptop_install: VERIFIED 2026-06-01 — 5 no-API skills at ~/.claude/skills/trading-* (market-breadth, uptrend, position-sizer, trader-memory-core, signal-postmortem); full catalog via tradermonty/claude-trading-skills
---

## Relations

- @concepts/skill-vetting.md — install discipline
- `@osint-wiki/sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md` — K92 eval

## Raw Concept

- **Repo**: `github.com/tradermonty/claude-trading-skills`
- **K92**: Adopt → CCC

## Narrative

Curated **trading-analysis skills** for Claude Code (SKILL.md bundles). Research prompts only — not execution authority on Cemini prod.

### Phase-0 audit (2026-06-01)

Clone: `/tmp/k92-phase0/claude-trading-skills`

| Check | Result |
|-------|--------|
| License | **MIT** |
| Maturity | 1712★ / push **2026-05-31** |
| Fit | CCC skill catalog — mirror into vetting workflow per @concepts/skill-vetting.md |
| Risk | Credential patterns in skills — scan before `~/.claude/skills/` copy |

**Verdict: GO (workflow adopt)** — skill-audit each file before install; no prod trading wiring.

### Adoption status [ADOPTED 2026-06-01]

Installed **no-API starter path** (5 skills, `trading-*` prefix in `~/.claude/skills/`). Re-run: `bash scripts/adopt_k92_phase0.sh` from OSINT WORKSPACE repo root. Paid-API skills (FMP, etc.) remain opt-in per `skills-index.yaml`.

## Snippets

> K92 v7 Adopt — claude-trading-skills. [Source: @osint-wiki/sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md]
