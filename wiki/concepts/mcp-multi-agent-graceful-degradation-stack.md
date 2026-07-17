---
title: MCP multi-agent stack with cloud→local→rules graceful degradation
type: concept
tags: [concept, mcp, multi-agent, resilience, k173]
keywords: [2607.13549, JW-ASTClaw, fallback, perception-decision-execution]
related:
  - sources/arxiv-jw-astclaw-solar-telescope-multi-agent-mcp-2607.13549.md
  - concepts/mcp-contract-grounded-synthesis-and-validation-gate.md
  - concepts/subagent-orchestration.md
  - concepts/client-as-first-order-harness-factor.md
  - concepts/operator-model-selection.md
  - sources/brief-k173-mcp-graceful-degradation-2026-07-16.md
  - sources/arxiv-searchos-v1-open-domain-agent-collaboration-2607.15257.md
maturity: draft
created: 2026-07-16
updated: 2026-07-17
---

## Relations

- `@sources/arxiv-jw-astclaw-solar-telescope-multi-agent-mcp-2607.13549.md` — K173 provenance
- `@concepts/operator-model-selection.md` — model-tier routing sibling
- `@concepts/subagent-orchestration.md` — agent fan-out

## Raw Concept

How should a multi-agent MCP system keep operating when the frontier cloud model is unavailable?

## Narrative

### Steal

1. **Decouple** perception / decision / execution; connect via MCP.
2. Encode domain expertise as **callable rules** inside perception agents (not only free-form LLM).
3. Plan **three-tier fallback**: cloud LLM → local SLM → deterministic rules.
4. Keep execution adapters thin so decision logic ports across surfaces.

### Cemini mapping

| Surface | Use |
|---------|-----|
| TipDrop / prod bots | Explicit offline/local/rule path when API flaky — don't hard-fail the loop |
| Poker arena | Rule-based legal-action fallback if LLM decide path errors |
| CCC laptop | Same pattern already partial in operator model selection — make fallback tiers explicit in agent READMEs |

### Verdict

**ADOPT** graceful-degradation checklist. **REFERENCE** astronomy deployment. **NO-GO** install (no public code).

## Snippets

> "perception and decision logic are reused unchanged across instruments, requiring only telescope-specific command interfaces" — Abstract
