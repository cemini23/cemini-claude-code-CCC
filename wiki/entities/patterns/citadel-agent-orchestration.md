---
title: "Citadel — agent-orchestration OS layer for Claude Code (Steal-from)"
type: entity
tags: [pattern, agent-orchestration, subagent, citadel, conductor, lifecycle-hooks, campaign-persistence, cross-wiki-route]
keywords: [citadel, sethgammon, agent-orchestration, do-routing, campaign-persistence, lifecycle-hooks, circuit-breaker, worktree-isolation, discovery-relay]
related:
  - concepts/subagent-orchestration.md
  - entities/tools/conductor-mcp.md
  - entities/patterns/scatter-gather.md
  - entities/patterns/tier1-tier2-agent-model.md
  - entities/patterns/glasswing-deliberate-disagreement.md
maturity: draft
created: 2026-05-21
updated: 2026-05-21
cross-wiki-source: "@osint-wiki/sources/multi-wiki-tool-eval-prompt-2026-05-18.md"
---

## Relations

- @concepts/subagent-orchestration.md — the concept this pattern directly extends; Citadel is the most complete operationalisation seen to date
- @entities/tools/conductor-mcp.md — Cemini's existing cross-wiki conductor; Citadel's `/do` routing is a superset of conductor semantics
- @entities/patterns/scatter-gather.md — parallel fan-out; Citadel's "discovery relay between waves" is scatter-gather gated by dependency chains
- @entities/patterns/tier1-tier2-agent-model.md — Citadel's lifecycle-hooks-and-circuit-breaker pattern is Tier-2 scope enforcement realised as infrastructure
- @osint-wiki/sources/multi-wiki-tool-eval-prompt-2026-05-18.md (cross-wiki source)

## Raw Concept

Cross-wiki brief routed from the OSINT K51 multi-wiki tool eval (36 repos, May 2026). Citadel surfaced as **the apex agent-orchestration artifact** in that batch — a four-tier `/do` routing engine with campaign persistence, parallel isolated worktrees, discovery relay, lifecycle hooks, and a circuit breaker. MIT license pending verification. Steal-from architecturally; do not adopt until license is confirmed.

## Narrative

`SethGammon/Citadel` describes itself as an "OS layer" for Claude Code agent orchestration. The K51 eval flagged it as the single highest-value CCC artifact in a 36-repo batch.

### Architecture (from eval + README)

- **Four-tier `/do` routing** — tasks classified by scope/complexity, routed to the appropriate agent tier
- **Campaign persistence across sessions** — agent state survives Claude Code session boundaries
- **Parallel agents in isolated worktrees** — git-worktree isolation per agent mirrors Claude Code's built-in `isolation: "worktree"` mode
- **Discovery relay between waves** — agent outputs from wave N feed as discovery inputs to wave N+1; dependency-aware scheduling
- **Lifecycle hooks** — pre-flight / post-flight / on-error hooks per agent invocation
- **Circuit breaker** — halts the campaign if error rate crosses threshold; prevents cascading agent failures
- **6 production-quality skills** — shipped with the repo, usable as design exemplars

### Why CCC cares

Citadel validates the conductor/librarian architecture direction Cemini has been building. The specific primitives worth extracting (clean-room, from documented architecture only):

1. **Campaign persistence** — subagent state surviving session boundaries is the missing piece in Cemini's current hot.md + claude-mem stack
2. **Discovery relay** — dependency-aware wave scheduling is a more sophisticated model than scatter-gather's flat fan-out
3. **Circuit breaker** — no current Cemini conductor primitive prevents cascading subagent failure; Citadel's model is referenceable
4. **Lifecycle hooks per agent** — finer-grained than Claude Code's session-level hooks; per-invocation hooks are a pattern worth studying

### Constraint

License not yet GitHub-API verified at time of routing. If MIT/Apache: promote to Adopt for pattern extraction. If unlicensed: Steal-from architecturally only; no code.

[NEEDS VERIFICATION 2026-05-21] upstream license.
