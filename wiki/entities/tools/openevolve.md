---
title: openevolve — evolutionary coding agent (AlphaEvolve-class, Apache-2.0)
type: entity
tags: [tool, agent-harness, evolution, token-optimization, cross-wiki-route]
keywords: [openevolve, algorithmicsuperintelligence, alphaevolve, evolutionary-agent, harness-optimization]
related:
  - concepts/token-economics-and-prompt-caching.md
  - concepts/code-as-agent-harness.md
  - concepts/agent-vm-sandboxing.md
  - entities/tools/claude-code.md
  - concepts/cursor-ide-workspace.md
  - concepts/cross-wiki-tool-eval-inventory.md
  - entities/tools/adaptive-auto-harness.md
  - concepts/adaptive-auto-harness-open-ended-streams.md
  - concepts/cross-wiki-tool-adoption-routing.md
  - concepts/failed-trajectory-harness-repair.md
  - concepts/retrospective-harness-optimization-rho.md
  - entities/tools/retro-harness.md
maturity: draft
created: 2026-05-24
updated: 2026-06-07
cross-wiki-source: "@osint-wiki/sources/multi-wiki-tool-eval-36url-wiki-ingestion-2026-05-24.md"
---

## Relations

- `@concepts/token-economics-and-prompt-caching.md` — primary CCC motivation (harness token/routing optimization)
- `@concepts/code-as-agent-harness.md` — evolves harness configuration, not application code only
- `@concepts/agent-vm-sandboxing.md` — run in isolated Docker for Phase-0 experiments
- `@entities/tools/claude-code.md` — target harness for optimized prompts/routing
- `@concepts/cursor-ide-workspace.md` — laptop-side eval surface alongside Claude Code

Cross-wiki: `@osint-wiki/entities/tools/openevolve.md` (OSINT entity stub); K63 URL #2.

## Raw Concept

`algorithmicsuperintelligence/openevolve` — open-source **AlphaEvolve-class** evolutionary coding agent. K63 **Adopt** for CCC after Phase-0 in **isolated Docker** (per brief). Apache-2.0 [CONFIRMED 2026-05-24, ~6.4k★].

## Narrative

### What it does

Evolves code/prompt configurations via search — eval positions it for **optimizing token budgets and agent routing** rather than replacing Claude Code or Cursor.

### Adoption posture

| Check | Status |
|-------|--------|
| License | Apache-2.0 [CONFIRMED] |
| Phase-0 | **PASS** — `scripts/openevolve-phase0-smoke.sh` 2026-06-04 (isolated temp venv; import ok; no wiki/`~/.claude/` writes) |
| Verdict | **CONDITIONAL-GO** — smoke only; no prod harness wiring until dedicated Docker eval |

### Explicit non-actions

- Do not run against production `~/.claude/` or live wiki trees without snapshot restore.
- Not a substitute for `@concepts/skill-vetting.md` on third-party skills.

## Phase-0 Audit (2026-06-04)

**Method:** GitHub API + `scripts/openevolve-phase0-smoke.sh` (isolated `/tmp/openevolve-smoke.*` venv). No writes to wiki or `~/.claude/`.

| Check | Result |
|-------|--------|
| License | **Apache-2.0** — `gh api repos/algorithmicsuperintelligence/openevolve` [CONFIRMED] |
| Maturity | **6,487★**; last push **2026-03-18** — active but not daily-shipping |
| Smoke | `pip install openevolve` → `import openevolve` OK; CLI not on PATH (module import path only) |
| Failure mode | Evolving against prod harness trees — **blast radius** if run outside Docker/snapshot |

**Decision — CONDITIONAL-GO.** Smoke passes in isolated venv. Next gate: Docker eval on a snapshot harness before any token/routing optimization against live `~/.claude/`. Stale push cadence acceptable for research tooling.

## Adoption trial (2026-06-04)

| Step | Result |
|------|--------|
| `scripts/openevolve-phase0-smoke.sh` | **PASS** (re-run during adoption batch) |
| `pip install openevolve` in `/tmp/ccc-adopt-trials-20260604/.venv` | **PASS** — import OK |
| Prod harness wiring | **Not done** — Docker eval still gated |

**Posture:** **ADOPTED (smoke tier only)** — safe for isolated venv experiments; not wired to live `~/.claude/`.

## Snippets

> "open-source implementation of AlphaEvolve… optimizing token budgets."
> — [Source: @osint-wiki/sources/multi-wiki-tool-eval-36url-wiki-ingestion-2026-05-24.md K63]
