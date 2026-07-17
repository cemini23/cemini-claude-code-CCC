---
title: MCP contract-grounded synthesis + validation gate
type: concept
tags: [concept, mcp, coding-agent, validation, prebind, k172]
keywords: [2607.12220, skill library, contract, rootstock, behavior tree]
related:
  - sources/arxiv-contract-grounded-bt-coding-agent-mcp-2607.12220.md
  - concepts/cage-1-enterprise-agent-governance-eval.md
  - concepts/mcp-context-optimization.md
  - concepts/client-as-first-order-harness-factor.md
  - concepts/hierarchical-skill-stack-lazy-orchestration.md
  - concepts/failure-mode-harness-adaptation-mapping.md
  - entities/tools/jsalfity-agentic-bt-mcp-artifacts.md
  - sources/brief-k172-mcp-contract-validation-gate-2026-07-16.md
  - concepts/mcp-multi-agent-graceful-degradation-stack.md
  - sources/arxiv-jw-astclaw-solar-telescope-multi-agent-mcp-2607.13549.md
  - concepts/acp-mcp-three-layer-human-agent-execution.md
  - concepts/coding-agent-install-gap-and-preinstall-gate.md
  - concepts/policy-as-code-layered-validation-for-agent-artifacts.md
  - sources/arxiv-agent-client-protocol-hri-genai-2607.14919.md
  - sources/arxiv-satellite-mission-compiler-policy-as-code-2607.14798.md
maturity: draft
created: 2026-07-16
updated: 2026-07-17
---

## Relations

- `@sources/arxiv-contract-grounded-bt-coding-agent-mcp-2607.12220.md` — K172 provenance (robot BT domain)
- `@concepts/cage-1-enterprise-agent-governance-eval.md` — Prebind Assurance sibling
- `@concepts/mcp-context-optimization.md` — MCP surface discipline
- `@concepts/hierarchical-skill-stack-lazy-orchestration.md` — K164 skill tree / fencing
- `@concepts/acp-mcp-three-layer-human-agent-execution.md` — K182 ACP+MCP topology sibling
- `@concepts/coding-agent-install-gap-and-preinstall-gate.md` — K179 pre-exec gate sibling
- `@concepts/policy-as-code-layered-validation-for-agent-artifacts.md` — K181 schema+policy sibling
- `@sources/arxiv-agent-client-protocol-hri-genai-2607.14919.md` — ACP+MCP three-layer provenance
- `@sources/arxiv-satellite-mission-compiler-policy-as-code-2607.14798.md` — policy-as-code MCP pipeline provenance

## Raw Concept

How should a coding agent synthesize structured actions so every reference is in the live capability set?

## Narrative

### Contract = three surfaces

1. **Skill library** — names, typed params, semantics
2. **Allowed operators / control structures** — exclusive set the runtime accepts
3. **Optional templates (rootstocks)** — scaffolds that help weaker models

### Validation gate

Synthesized artifact is checked **before** execution/bind. Fail → retry with feedback; do not rely on the model to self-censor.

### Verdict

**ADOPT** MCP-as-contract + validation-before-bind for any Cemini coding-agent that emits configs/hooks/tool calls. **REFERENCE** robotics BT empirics. **NO-GO** unlicensed paper webviewer/MCP demos; Apache `ros-mcp-server` is optional robotics reference only (not adopted this ingest — off CCC day-to-day).

## Snippets

> "grounding requires every synthesized BT to reference only skills the robot can execute with valid parameters" — §I
