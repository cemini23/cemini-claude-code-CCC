---
title: Schema-bound MCP tool surface — validate before vendor dispatch
type: concept
tags: [concept, mcp, schema, skills, safety, k198]
keywords: [2607.17012, schema-bound, physical bounds, MCP prompts as skills]
related:
  - sources/arxiv-schema-bound-mcp-instrument-skills-2607.17012.md
  - entities/tools/nuance-mcp.md
  - concepts/mcp-contract-grounded-synthesis-and-validation-gate.md
  - concepts/cage-1-enterprise-agent-governance-eval.md
  - concepts/mcp-security-signals-vs-runtime-evidence.md
  - sources/brief-k197-k201-harness-solver-pruner-2026-07-21.md
  - concepts/mcp-context-optimization.md
  - concepts/deterministic-mcp-symbolic-reasoning.md
  - sources/arxiv-euclid-mcp-prolog-reasoning-2607.21412.md
  - concepts/hybrid-static-dynamic-mcp-tool-security.md
  - sources/arxiv-mtguard-hybrid-mcp-tool-security-2607.25297.md
maturity: draft
created: 2026-07-21
updated: 2026-07-30
---

## Relations

- `@sources/arxiv-schema-bound-mcp-instrument-skills-2607.17012.md` — provenance
- `@entities/tools/nuance-mcp.md` — MIT reference
- `@concepts/mcp-contract-grounded-synthesis-and-validation-gate.md` — K172 peer
- `@concepts/cage-1-enterprise-agent-governance-eval.md` — Prebind peer (K151)
- `@concepts/mcp-security-signals-vs-runtime-evidence.md` — evidence bar peer

## Raw Concept

K198: LLM agents emit physically unreasonable args. Fix at the **tool protocol**: schema-bound validation before any side-effecting call; skills as MCP-prompt compositions of typed tools; long jobs as first-class typed lifecycle.

## Narrative

### Steal (ADOPT)

1. Every high-risk MCP tool: JSON schema + **domain bounds** (not just types) before dispatch.
2. Separate language-side planning from execution adapters.
3. Promote long-running work to typed live-jobs, not opaque background shells.
4. Implement multi-step protocols as **MCP prompt skills** with parameterized tool sequences.
5. Local clone `nuance-mcp` for study — microscopy domain, pattern generalizes to TipDrop LIVE / trading / shell.

| Verdict | **ADOPT** schema-bound + skill-composition checklist; **GO** MIT clone REFERENCE |

## Snippets

> "schema-bound tool surface validates every request against physical bounds before any vendor call is dispatched"
> — [Source: arxiv-2607.17012]
