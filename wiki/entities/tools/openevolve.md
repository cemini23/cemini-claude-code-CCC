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
maturity: draft
created: 2026-05-24
updated: 2026-05-24
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
| Phase-0 | **Required** — README, Docker blast radius, what it writes to disk |
| Verdict | **CONDITIONAL-GO (Adopt intent)** — no prod wiring until Phase-0 + sandboxed trial |

### Explicit non-actions

- Do not run against production `~/.claude/` or live wiki trees without snapshot restore.
- Not a substitute for `@concepts/skill-vetting.md` on third-party skills.

## Snippets

> "open-source implementation of AlphaEvolve… optimizing token budgets."
> — [Source: @osint-wiki/sources/multi-wiki-tool-eval-36url-wiki-ingestion-2026-05-24.md K63]
