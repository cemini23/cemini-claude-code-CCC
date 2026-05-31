---
title: Kimi Agent Swarm vs Claude Agent Teams — topology and CCC fit (K65)
type: concept
tags: [concept, multi-agent, kimi, claude-code, orchestration, k65, cross-wiki-route]
keywords: [kimi agent swarm, claude agent teams, moonshot, coordinator, peer-to-peer, subagent, scatter-gather]
related:
  - concepts/subagent-orchestration.md
  - entities/patterns/scatter-gather.md
  - entities/tools/conductor-mcp.md
  - entities/tools/kimi-agent-swarm.md
  - entities/tools/claude-code.md
  - concepts/cross-wiki-tool-eval-inventory.md
  - concepts/code-as-agent-harness.md
  - entities/tools/ruflo.md
maturity: draft
created: 2026-05-24
updated: 2026-05-31
cross-wiki-source: "@osint-wiki/concepts/kimi-agent-swarm-vs-claude-agent-teams.md"
---

## Relations

- `@concepts/subagent-orchestration.md` — Claude Code `Agent` tool + Agent Teams align with mesh/isolated subagents
- `@entities/patterns/scatter-gather.md` — bounded parallel fan-out vs vendor 300-agent hub
- `@entities/tools/conductor-mcp.md` — prod routing; neither Kimi nor Teams replaces conductor
- `@entities/tools/kimi-agent-swarm.md` — Moonshot product reference (NO-GO prod)
- `@entities/tools/claude-code.md` — host for Agent Teams and Task/subagent types
- `@concepts/cross-wiki-tool-eval-inventory.md` — K65 receipt row

Cross-wiki: `@osint-wiki/concepts/kimi-agent-swarm-vs-claude-agent-teams.md`, `@osint-wiki/sources/x-kirillk-kimi-agent-swarm-guide-2026-05-24.md`.

## Raw Concept

K65 brief (`briefs/2026-05-24_k65-kimi-agent-swarm-vs-claude-teams.md`) — CCC operators choosing between **Moonshot Kimi Agent Swarm** (hosted web, hub coordinator) and **Anthropic Claude Agent Teams** (terminal/code, peer mesh). Synthesized from OSINT K65 ingest.

## Narrative

### Topology [TENTATIVE — curator source + vendor claims]

| | Kimi Agent Swarm | Claude Agent Teams / CCC `Agent` tool |
|--|------------------|--------------------------------------|
| Coordination | Central coordinator only | Peers + lead; isolated subagents return to parent |
| Scale | Up to ~300 sub-agents, ~4k steps [vendor] | ~4–6 typical; Cursor Task tool similar isolation |
| Interface | `kimi.com` web | Claude Code / Cursor agent |
| Sweet spot | N homogeneous tasks → one synthesis (papers, CVs, landing pages) | Repo refactor, parallel review, multi-service debug |

### Decision matrix (CCC)

| Task | Use |
|------|-----|
| Refactor, parallel review, wiki ingest, harness work | **Claude Agent Teams** + `@concepts/subagent-orchestration.md` |
| Embarrassingly parallel external research (no repo write) | Kimi Swarm UI **or** bounded `@entities/patterns/scatter-gather.md` + Exa |
| Cemini prod trading | **Neither** — `@entities/tools/conductor-mcp.md` + prod MCP |

### CCC takeaways [CONFIRMED 2026-05-24]

1. **Closer to Teams than Swarm:** Cursor/Claude `Agent` / Task subagents = isolated context, parent merge — not 300-agent hub fan-out.
2. **Port patterns, not product:** Swarm quality depends on **output schema** in prompts — steal into slash commands / skills; **no** Moonshot dependency in `.cursor/mcp.json`.
3. **Cost discipline:** Do not mirror 300-LLM-call fan-out on market or ingest paths; verification at scale multiplies errors.

### Verdict

| Product | CCC disposition |
|---------|-----------------|
| Kimi Agent Swarm | **REFERENCE** — decomposition + coordinator-merge patterns only |
| Claude Agent Teams | **In use** — primary for codebase and wiki work |

## Snippets

> "Swarm = star; Teams = mesh. CCC Agent tool is closer to Teams."
> — [Source: briefs/2026-05-24_k65-kimi-agent-swarm-vs-claude-teams.md]

> "All outputs flow to the coordinator. There's no direct agent-to-agent communication."
> — [Source: @osint-wiki/sources/x-kirillk-kimi-agent-swarm-guide-2026-05-24.md]
