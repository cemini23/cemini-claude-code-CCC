---
title: pydantic-ai — typed LLM agent framework
type: entity
tags: [tool, agents, python, adopt, k103]
keywords: [pydantic-ai, structured-output, mcp, monty-sandbox, agpl-gateway]
related:
  - sources/multi-wiki-tool-eval-v8-k103-2026-06-07.md
  - concepts/code-as-agent-harness.md
  - concepts/skill-vetting.md
  - "@osint-wiki/entities/tools/pydantic-ai.md"
  - concepts/cross-wiki-tool-eval-inventory.md
maturity: draft
created: 2026-06-07
updated: 2026-06-07
phase_0_verdict: "GO 2026-06-07 — MIT core; reject pydantic-ai-gateway (AGPL-3.0)"
---

## Relations

- `@sources/multi-wiki-tool-eval-v8-k103-2026-06-07.md` — K103 Adopt
- `@concepts/code-as-agent-harness.md` — typed tool I/O vs free-text parsing
- `@concepts/skill-vetting.md` — license split: core vs gateway
- `@osint-wiki/entities/tools/pydantic-ai.md` — canonical Phase-0 audit

## Raw Concept

- **URL:** https://github.com/pydantic/pydantic-ai
- **Tier:** Adopt (CCC laptop prototypes; prod via staged brief)
- **License:** MIT (core) [CONFIRMED 2026-06-07]
- **Reject companion:** `pydantic/pydantic-ai-gateway` — **AGPL-3.0** — never install on prod perimeter

## Narrative

Python agent framework with Pydantic-typed tool I/O, provider abstraction, MCP/A2A surfaces, Monty sandboxed execution. Reduces hallucinated tool arguments vs parsing free-text tool calls in hand-rolled orchestrators.

**Phase-0 GO:** `pip install pydantic-ai` via `scripts/adopt_k103_phase0.sh`. Prod integration targets **modules** (typed schemas for specific agents), not a framework-wide rewrite.

**Failure mode:** Accidentally adopting AGPL gateway for routing — violates `@concepts/tools-we-dont-use.md` AGPL posture.

## Snippets

> "Shift away from fragile free-text parsing toward strongly-typed Pydantic models for LLM outputs." [Source: Tool Evaluation and Wiki Fit.docx URL 27; K103]
