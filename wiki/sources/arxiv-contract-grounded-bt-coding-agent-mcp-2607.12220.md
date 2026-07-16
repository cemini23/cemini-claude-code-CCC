---
title: "Contract-Grounded Behavior Tree Synthesis via Coding Agents"
type: source
tags: [source, arxiv, mcp, coding-agent, validation-gate, contract, k172]
keywords: [2607.12220, behavior tree, MCP server, skill library, rootstock, Claude Code]
related:
  - concepts/mcp-contract-grounded-synthesis-and-validation-gate.md
  - concepts/cage-1-enterprise-agent-governance-eval.md
  - concepts/mcp-context-optimization.md
  - concepts/client-as-first-order-harness-factor.md
  - concepts/hierarchical-skill-stack-lazy-orchestration.md
  - entities/tools/jsalfity-agentic-bt-mcp-artifacts.md
  - sources/brief-k172-mcp-contract-validation-gate-2026-07-16.md
maturity: draft
created: 2026-07-16
updated: 2026-07-16
---

## Relations

- `@concepts/mcp-contract-grounded-synthesis-and-validation-gate.md` — synthesized steal
- `@concepts/cage-1-enterprise-agent-governance-eval.md` — Prebind sibling (bind only after contract check)
- `@entities/tools/jsalfity-agentic-bt-mcp-artifacts.md` — Phase-0 (NO-GO paper artifacts; ros-mcp-server Apache sibling noted)
- `@sources/brief-k172-mcp-contract-validation-gate-2026-07-16.md` — prod brief stub

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Contract-Grounded Behavior Tree Synthesis via Coding Agent |
| **Author** | Jonathan Salfity, Robert Blake Anderson, Mitch Pryor |
| **Type** | arXiv, robotics + coding agents |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.12220-contract-grounded-behavior-tree-synthesis-via-co.pdf` | **Retrieved** | 2026-07-16 |
| **arXiv** | 2607.12220 |
| **Pages** | 8 |
| **Read status** | read |
| **Artifacts** | webviewer `jsalfity/agentic-bt-gen-webviewer`; MCP demo `jsalfity/tb3-mcp-server` (no LICENSE); related `jsalfity/ros-mcp-server` Apache-2.0 |

## Narrative

### Thesis

NL→robot behavior-tree (BT) synthesis fails when grounding is left to the prompt author. Fix: a **robot-side MCP server** exposes an explicit **contract** (skill library + permitted BT operators + optional rootstock templates); a coding agent (Claude Code / Codex class) queries the contract, synthesizes a BT, and a **validation gate** rejects ungrounded/malformed trees before execution.

### Architecture steal (Fig. 1)

1. Operator issues NL without knowing robot internals.
2. Coding agent MCP-queries contract.
3. Validation gate checks schema / skills / params.
4. Runtime executes; retry if invalid.

Empirics: Sonnet 4.6 + Gemma4:31b; 110 PyRoboSim + 14 physical Panther/Nav2 tasks. Contract grounding → near-perfect BT validation; rootstocks help smaller model on reactive control-flow; transfers to opaque Nav2 stack. OOC refusal still imperfect (50–70%) — contract ≠ full safety.

### CCC mapping (robotics off-domain; MCP pattern on-domain)

| Pattern | Cemini use |
|---------|------------|
| MCP as **authority of truth** for allowed tools/skills | TipDrop / prod bots: expose allowlisted skills + schemas via MCP, not free-form invent |
| Validation gate before bind | Pair K151 Prebind — synthesized actions must pass schema/skill checks |
| Rootstock templates for smaller models | Pair K168 — plan skeletons + filtered tools for SLMs |
| Claude Code as synthesizer | Coding agent already in stack; contract MCP is the missing piece |

## Snippets

> "a coding agent queries a robot-side Model Context Protocol (MCP) server to retrieve an explicit contract" — Abstract

> "the validation gate catches malformed or ungrounded BTs" — Discussion

> — [Source: arxiv-2607.12220, retrieved 2026-07-16]
