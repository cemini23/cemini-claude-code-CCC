---
title: Code as agent harness — Claude Code mapping of the three-layer model
type: concept
tags: [concept, agent-harness, claude-code, conductor, mcp, verification, cross-wiki-route]
keywords: [code-as-agent-harness, harness-interface, harness-mechanisms, executable-agents, verifiable-agents, stateful-agents, regression-free-harness]
related:
  - concepts/self-healing-agent-sessions.md
  - entities/tools/claude-code.md
  - entities/tools/conductor-mcp.md
  - concepts/subagent-orchestration.md
  - concepts/hooks-for-automation.md
  - entities/mcp-servers/stash.md
  - entities/tools/lazy-tool.md
  - entities/tools/claude-mem.md
  - entities/patterns/glasswing-deliberate-disagreement.md
  - entities/patterns/full-prompt-goal-template.md
  - entities/tools/openspec.md
  - concepts/skill-vetting.md
  - concepts/skillrae-retrieval-augmented-execution.md
  - concepts/graphflow-verifiable-agent-workflows.md
  - sources/arxiv-graphflow-2605.14968.md
  - sources/arxiv-skillrae-2605.10114.md
  - entities/tools/openevolve.md
  - concepts/kimi-agent-swarm-vs-claude-agent-teams.md
  - concepts/claude-code-software-factory.md
  - concepts/claude-premortem-skill.md
maturity: draft
created: 2026-05-21
updated: 2026-05-26
cross-wiki-source: "@osint-wiki/sources/arxiv-code-as-agent-harness-survey-2605.18747.md"
---

## Relations

- `@concepts/self-healing-agent-sessions.md` — runtime failure detection + retry atop harness execution
- `@entities/tools/claude-code.md` — the harness this concept maps onto
- `@entities/tools/conductor-mcp.md` — cross-wiki fan-out as harness-interface routing
- `@concepts/subagent-orchestration.md` — scaling layer via isolated subagent contexts
- `@concepts/hooks-for-automation.md` — feedback control on harness lifecycle events
- `@entities/mcp-servers/stash.md` — episodic state across turns
- `@entities/tools/lazy-tool.md` — deferred MCP tool surface (harness mechanisms)
- `@entities/tools/claude-mem.md` — passive observation memory
- `@entities/patterns/glasswing-deliberate-disagreement.md` — adversarial verification lens (complements survey taxonomy)
- `@entities/patterns/full-prompt-goal-template.md` — durable goal pinning + Stop-hook gating
- `@entities/tools/openspec.md` — spec-as-contract for regression-aware iteration
- `@concepts/skill-vetting.md` — Phase-0 gate before harness surface changes
- `@concepts/skillrae-retrieval-augmented-execution.md` — post-retrieval skill-graph compilation (K59)
- `@concepts/graphflow-verifiable-agent-workflows.md` — proof-carrying workflows vs empirical harness (K59)

Cross-wiki: `@osint-wiki/concepts/code-as-agent-harness.md` holds finance-adjacent synthesis; `@osint-wiki/sources/arxiv-code-as-agent-harness-survey-2605.18747.md` is the 102pp primary; `@osint-wiki/sources/agentic-harness-engineering.md` (AHE) covers observability-driven harness *evolution*.

## Raw Concept

Routed from `briefs/2026-05-21_k48-code-as-harness-and-self-healing-from-osint.md` (OSINT K48 arXiv ingest). Question: **how does the "code as agent harness" survey map onto Cemini's Claude Code / conductor / MCP stack without duplicating the 102-page taxonomy?**

## Narrative

arXiv:2605.18747 frames **code as operational substrate** — not only generated output. Agents reason, act, model environments, and verify execution through executable artifacts (tool calls, shell, file edits, MCP). CCC owns the **harness-engineering slice** for laptop-side Claude Code; OSINT owns the survey hub and Cemini AI product mapping.

### Three-layer model → Cemini stack

| Layer | Survey content | Cemini / Claude Code mapping |
|-------|----------------|------------------------------|
| **Harness interface** | Code linking reasoning ↔ action ↔ environment | MCP tool surface (`Read`/`Edit`/`Bash`), `@entities/tools/conductor-mcp.md` `conductor_query`, file-backed wiki reads |
| **Harness mechanisms** | Planning, memory, tools, feedback control | `@concepts/subagent-orchestration.md`, `@entities/mcp-servers/stash.md`, `@entities/tools/lazy-tool.md`, `@entities/tools/claude-mem.md`, `@concepts/hooks-for-automation.md`, `/goal` + `@entities/patterns/full-prompt-goal-template.md` |
| **Scaling the harness** | Multi-agent shared artifacts + review | Parallel `Agent` tool calls; server-Claude on prod vs laptop wiki curator; `@entities/patterns/glasswing-deliberate-disagreement.md` for adversarial gating |

### Design imperatives [CONFIRMED against CCC practice]

- **Executable** — every proposed action must resolve to a tool call the harness can run (or an explicit human approval gate per `@entities/patterns/tier1-tier2-agent-model.md`).
- **Verifiable** — harness changes (new skills, MCP servers, hooks) pass `@concepts/skill-vetting.md` Phase-0 before adoption.
- **Stateful** — durable state lives in git-tracked wiki + `hot.md` + stash/claude-mem; not only in the ephemeral context window.

### Three complementary lenses (do not conflate)

| Lens | Source | CCC use |
|------|--------|---------|
| Taxonomy | 2605.18747 survey | Structure conductor + MCP docs |
| Evolution methodology | AHE (`@osint-wiki/sources/agentic-harness-engineering.md`) | Observability-driven harness improvement |
| Adversarial verification | Glasswing / evilsocket audit (K56) | Multi-agent disagreement before execution |

### Open problems → existing CCC workflows

| Survey open problem | CCC workflow anchor |
|---------------------|---------------------|
| Regression-free harness improvement | OpenSpec acceptance criteria + `@entities/tools/openspec.md`; skill retrofit audits |
| Evaluation beyond final success bit | Glasswing deliberate disagreement; reviewer subagent |
| Multi-agent shared state consistency | Syncthing wiki sync + conductor read-only fan-out |
| Human oversight for high-impact actions | Tier 1/Tier 2 model; `/goal` Stop hook |

**Explicit non-action:** no new packages from the survey. Distinct from K56 Karpathy system-prompt-learning — that optimizes prompts; this concept covers runtime harness infrastructure.

## Snippets

> "In emerging agentic systems, code is no longer only a target output. It increasingly serves as an operational substrate for agent reasoning, acting, environment modeling, and execution-based verification."
> — [Source: arXiv:2605.18747 via @osint-wiki/sources/arxiv-code-as-agent-harness-survey-2605.18747.md]
