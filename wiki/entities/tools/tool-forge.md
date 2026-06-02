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
maturity: draft
created: 2026-06-02
updated: 2026-06-02
phase_0_verdict: CONDITIONAL-GO 2026-06-02 — Apache-2.0 verified; ~2★ immature; steal validation-carrying pattern for skill_audit + MCP catalog
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
| Stars / maturity | ~2★, pushed 2026-06-02 — **immature** |
| vs lazy-tool + skill_audit | **Steal pattern** — metadata on tools/skills at definition time |
| Prod install | **NO-GO** until Phase-0 clone + hook collision audit |

**Verdict:** **CONDITIONAL-GO** — document validation-carrying discipline in `skill-vetting.md`; do not vendor Tool Forge into Cemini prod without dedicated audit.

## Snippets

> "Validation-carrying tools and token-efficient routing are necessary for governed production execution." [Source: arxiv-2605.28000…pdf, Abstract]
