---
title: Kimi Agent Swarm — Moonshot parallel agent product (reference only, K65)
type: entity
tags: [tool, kimi, moonshot, multi-agent, reference-only, k65, cross-wiki-route]
keywords: [kimi agent swarm, k2.6, 300 sub-agents, moonshot ai, agent-swarm]
related:
  - concepts/kimi-agent-swarm-vs-claude-agent-teams.md
  - concepts/subagent-orchestration.md
  - entities/patterns/scatter-gather.md
  - entities/tools/conductor-mcp.md
  - concepts/cross-wiki-tool-eval-inventory.md
  - concepts/five-layer-operator-stack.md
  - sources/trading-posts-compilation-6-2026-05-29.md
  - "@osint-wiki/entities/tools/kimi-agent-swarm.md"
maturity: draft
created: 2026-05-24
updated: 2026-05-30
cross-wiki-source: "@osint-wiki/entities/tools/kimi-agent-swarm.md"
---

## Relations

- `@concepts/kimi-agent-swarm-vs-claude-agent-teams.md` — comparison vs Claude Agent Teams
- `@concepts/subagent-orchestration.md` — CCC harness choice for repo work
- `@entities/patterns/scatter-gather.md` — bounded Cemini parallel pattern
- `@entities/tools/conductor-mcp.md` — prod orchestration layer
- `@concepts/five-layer-operator-stack.md` — K78 long-horizon coding layer (reference only)
- `@sources/trading-posts-compilation-6-2026-05-29.md` — K78 provenance

Cross-wiki: `@osint-wiki/entities/tools/kimi-agent-swarm.md`, `@osint-wiki/entities/models/kimi-k2-6.md`.

## Raw Concept

Moonshot **Kimi Agent Swarm** — consumer web product (`kimi.com/agent-swarm`). K65 OSINT entity + CCC brief. **NO-GO** for Cemini prod; **REFERENCE** for prompt decomposition patterns.

## Narrative

### Architecture (vendor-documented) [TENTATIVE]

K2.6 coordinator → decompose prompt → ≤300 parallel sub-agents → ≤4,000 steps → coordinator synthesizes deliverable (report, spreadsheet, file bundle).

### Adoption posture

| Check | Status |
|-------|--------|
| Prod trading / conductor | **NO-GO** — no MCP, no audit trail parity |
| CCC Cursor / Claude Code | **REFERENCE** — external UI for batch research only |
| `.cursor/mcp.json` | **Do not add** Moonshot server |
| Verdict | **REFERENCE (K65)** |

### vs CCC stack

Use `@entities/tools/claude-code.md` Agent Teams for codebase and wiki. Use Kimi only when task is **hosted parallel content factory**, not harness or market ops.

## Snippets

> "Not a Claude Code replacement."
> — [Source: briefs/2026-05-24_k65-kimi-agent-swarm-vs-claude-teams.md]
