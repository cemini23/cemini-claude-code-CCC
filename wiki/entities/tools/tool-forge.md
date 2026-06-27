---
title: Tool Forge — validation-carrying agent toolchain (Apache-2.0)
type: entity
tags: [tool, agent-harness, mcp, adopt-candidate, k94]
keywords: [tool-forge, nextmoca, validation-carrying, governed-execution]
related:
  - sources/arxiv-tool-forge-governed-agentic-2605-28000-2026-06-02.md
  - concepts/skill-vetting.md
  - entities/tools/lazy-tool.md
  - "@osint-wiki/sources/arxiv-tool-forge-governed-agentic-2605-28000-2026-06-02.md"
  - concepts/recoverable-tool-reliability-hazards.md
maturity: draft
created: 2026-06-02
updated: 2026-06-27
phase_0_verdict: NO-GO install 2026-06-02 — steal validation-carrying only; Apache-2.0; 187 pytest pass; Alpha + Docker/Postgres stack
---

## Relations

- `@sources/arxiv-tool-forge-governed-agentic-2605-28000-2026-06-02.md` — arXiv 2605.28000
- `@concepts/skill-vetting.md` — audit gates before tool/skill promotion
- `@entities/tools/lazy-tool.md` — token-efficient tool routing peer

## Raw Concept

`github.com/nextmoca/tool-forge` — **validation-carrying** tool definitions for governed agentic execution (Rao, May 2026). arXiv 2605.28000.

## Narrative

| Check | Result |
|-------|--------|
| License | **Apache-2.0** `[CONFIRMED 2026-06-02]` via `gh api` |
| Stars / maturity | ~2★, Alpha (`Development Status :: 3`); pushed 2026-06-02 |
| Tests | **187 passed** (`pip install -e ".[dev]"` + pytest) |
| vs lazy-tool + conductor | **Collision** — second MCP router + Postgres + webapp |
| Prod install | **NO-GO** — sandboxed tool generation unsafe on prod VM |

**Verdict:** **NO-GO install** — steal validation-carrying + `approve/block` governance into `skill-vetting.md` and prod `docs/mcp-tool-governance.md` (see OSINT prod brief).

## Snippets

> "Validation-carrying tools and token-efficient routing are necessary for governed production execution." [Source: arxiv-2605.28000…pdf, Abstract]
