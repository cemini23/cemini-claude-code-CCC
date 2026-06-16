---
title: conductor-mcp — cross-wiki query router
type: entity
tags: [tool, mcp-server, conductor, orchestration, cross-wiki, fastmcp]
keywords: [conductor, conductor mcp, conductor_query, cross-wiki routing, fastmcp, librarian, kb-server]
related:
  - entities/tools/claude-code.md
  - entities/mcp-servers/librarian-kb-server.md
  - concepts/cross-wiki-routing.md
  - entities/tools/osmedeus-acp-orchestration.md
  - entities/patterns/scatter-gather.md
  - entities/tools/cc-wf-studio.md
  - entities/patterns/citadel-agent-orchestration.md
  - concepts/cross-wiki-tool-eval-inventory.md
  - concepts/code-as-agent-harness.md
  - concepts/self-healing-agent-sessions.md
  - concepts/deep-research-evaluation-prompt.md
  - entities/tools/n8n-mcp.md
  - concepts/skillrae-retrieval-augmented-execution.md
  - concepts/graphflow-verifiable-agent-workflows.md
  - entities/tools/ai-engineering-roadmap.md
  - entities/tools/hermes-agent.md
  - concepts/kimi-agent-swarm-vs-claude-agent-teams.md
  - entities/tools/kimi-agent-swarm.md
  - concepts/claude-code-personal-os-scope.md
  - concepts/obsidian-trading-journal-workflow.md
  - entities/tools/rowboat.md
  - entities/tools/council-of-high-intelligence.md
  - concepts/agentic-programming-full-stack-thesis.md
  - concepts/claude-code-finance-research-setup.md
  - concepts/codex-side-fork-workflow.md
  - entities/tools/ruflo.md
  - entities/tools/skillnet.md
  - concepts/remote-hermes-access-pattern.md
  - entities/tools/agyn.md
  - concepts/mcp-server-runtime-fault-taxonomy.md
  - concepts/slm-agent-orchestration-gateway.md
  - sources/arxiv-slm-orchestration-gateway-2606.03557.md
  - entities/tools/aarri-bench.md
  - concepts/dynamic-workflow-orchestrator-off-model.md
  - concepts/agent-five-gate-org-chart.md
  - sources/trading-posts-compilation-18-2026-06-04.md
  - concepts/mcp-server-catalog-curation.md
  - concepts/seclaw-agent-security-evaluation.md
  - concepts/etclovg-harness-layers.md
  - sources/arxiv-aarri-research-intern-bench-2606-07462-2026-06-09.md
  - concepts/internet-of-agentic-ai-ioai.md
  - sources/arxiv-internet-of-agentic-ai-2606.12835.md
  - concepts/agents-k1-agent-native-knowledge-orchestration.md
  - sources/arxiv-agents-k1-knowledge-orchestration-2606.13669.md
  - concepts/orchestration-reward-modeling-orch-rm.md
  - sources/arxiv-orch-rm-multi-agent-orchestration-2606.13598.md
maturity: validated
created: 2026-05-13
updated: 2026-06-16
---

## Relations

- `@entities/tools/claude-code.md` — host harness; conductor is consumed as an MCP server
- `@entities/mcp-servers/librarian-kb-server.md` — backend it routes to
- `@concepts/cross-wiki-routing.md` — the workflow concept this tool implements
- `@entities/tools/osmedeus-acp-orchestration.md` — adjacent orchestration architecture: a YAML engine orchestrating ACP subprocess agents
- `@entities/patterns/scatter-gather.md` — the conductor's cross-wiki query routing is a scatter-gather application
- `@concepts/code-as-agent-harness.md` — conductor as harness-interface routing layer
- `@concepts/self-healing-agent-sessions.md` — conductor fan-out failures and fallback policy
- `@concepts/internet-of-agentic-ai-ioai.md` — bounded private IoAI slice vs open discovery
- `@concepts/agents-k1-agent-native-knowledge-orchestration.md` — KG substrate complement to conductor queries
- `@entities/tools/hermes-agent.md` — parallel personal-agent runtime (reference only; K64 routing)

Cross-wiki: `@osint-wiki/concepts/conductor-orchestrator.md` covers the design history and the FastMCP-based implementation.

## Narrative

`conductor` is a FastMCP server in the **private** `osint-wiki` workspace at `conductor/mcp_server.py` (canonical location; the federation reuses one conductor across all wikis). It exposes a single high-value tool — `conductor_query` — that fans a query out across one or more wikis (resolved by `wiki-alias`) and returns a synthesized answer with citation-tracked source page paths.

**Why it exists**: the federation has five wikis, each with its own `index.md` and entity tree. A naive cross-wiki query forces Claude Code to round-robin-read every `index.md`, then every matched page — burning context and tokens. The conductor offloads that fan-out into a **single subagent invocation** (`@concepts/subagent-orchestration.md`) backed by the librarian's kb-server, returning a synthesized brief to the parent session.

**Backend (2026-06-14):** `cemini-librarian` **deleted** — kb-server offline. Conductor must read local `wiki/` trees per `wiki-alias` (laptop paths). Historical: delegated to `librarian-kb-server` on Hetzner. See `@osint-wiki/meta/librarian-decommission-2026-06-14.md`.

**Cost vs benefit**: each conductor_query call costs one subagent's startup tokens (~1-3K). Worth it when the query genuinely needs ≥3 wikis or ≥10 pages; not worth it for a single-page lookup.

**AI Operating Systems essay** (@Suryanshti777, K57 Post 5): six-layer orchestration essay overlaps conductor + librarian + stash — **no new page**; treat as external framing only [Source: @osint-wiki/sources/trading-posts-llm-gustafsson-retail-weather-copy-2026-05-22.md].

**Adoption status** (2026-05-13): conductor is *available* and *occasionally used*. It is not part of every session because most Cemini work is single-wiki. When a query is genuinely cross-domain ("which of our wikis covers OSINT-overlap pentest tradecraft?"), conductor is the right primitive.

**Phase-0 caveats from history**: per OSINT's K30 audit log, two competing approaches were rejected — SwarmVault (hardcoded flat layout, broke nested wikis) and PageIndex (single-file API + agentic cost + lost graph/metadata). The conductor's value is precisely the graph-preserving fan-out those alternatives lacked.

**K98 five-gate mapping** (@Voxyz_ai Post 1): conductor implements **Lead + Specialist** gates in `@concepts/agent-five-gate-org-chart.md` — cross-wiki fan-out replaces single-chat persona cosplay. **Intake** and **Memo** remain parent-session responsibilities (`/goal`, `wiki/log.md`).

## Dead Ends

- **Using conductor for single-wiki queries** — direct `Read` + `Grep` on the target wiki's `index.md` is cheaper.
- **Treating conductor as a write path** — it's read-only by design. New pages go through the per-wiki ingest workflow.
