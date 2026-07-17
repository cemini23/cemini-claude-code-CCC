---
title: Policy-as-code layered validation for agent-emitted artifacts
type: concept
tags: [concept, policy-as-code, opa, guardrails, mcp, k181]
keywords: [2607.14798, Rego, deny rules, schema, defense-in-depth]
related:
  - sources/arxiv-satellite-mission-compiler-policy-as-code-2607.14798.md
  - entities/tools/satellite-mission-compiler.md
  - concepts/mcp-contract-grounded-synthesis-and-validation-gate.md
  - concepts/coding-agent-install-gap-and-preinstall-gate.md
  - concepts/cage-1-enterprise-agent-governance-eval.md
  - sources/brief-k181-policy-as-code-guardrails-2026-07-17.md
maturity: draft
created: 2026-07-17
updated: 2026-07-17
---

## Relations

- `@sources/arxiv-satellite-mission-compiler-policy-as-code-2607.14798.md` — K181 provenance
- `@concepts/mcp-contract-grounded-synthesis-and-validation-gate.md` — schema+gate sibling
- `@concepts/coding-agent-install-gap-and-preinstall-gate.md` — K179 pre-exec gate sibling

## Raw Concept

How should agent-generated plans/configs be validated before they become live artifacts?

## Narrative

### Steal

1. **Schema parse** first (typed structural errors).
2. **Policy-as-code deny rules** second (semantic/safety), with provenance on each rule.
3. Compile to IR then render target manifests — don't let the LLM emit final YAML unchecked.
4. Expose the pipeline via MCP with path-traversal / input hygiene.
5. Severity tiers for pre-deploy loss events.

### Cemini mapping

| Surface | Use |
|---------|-----|
| Claude Code / Cursor | Hooks that lint agent-written `settings.json` / compose files before apply |
| TipDrop | Policy checks on Discord post templates / scanner config before deploy |
| Prod | OPA-style deny for bankroll-touching configs (pair Prebind) |

### Verdict

**ADOPT** layered schema+policy checklist. **GO** local clone EUPL compiler as reference (`.local/adopts/satellite-mission-compiler`). Not for satellite prod ops.

## Snippets

> layered validation catches both structural errors (at schema parse time) and semantic violations (via OPA policy) — Conclusion
