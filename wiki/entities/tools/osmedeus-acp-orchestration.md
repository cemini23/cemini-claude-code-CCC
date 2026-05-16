---
title: "Osmedeus — ACP subagent-orchestration pattern for the CCC conductor"
type: entity
tags: [entity, tool, pattern, subagent-orchestration, acp-agents, yaml-workflow-engine, conductor-architecture, cross-wiki-stub, cross-wiki-route-2026-05-16]
keywords: [osmedeus, acp-orchestration, go-yaml-workflow-engine, agent-tool-calling-loops, memory-management, claude-code-codex-subprocess, conductor-pattern, mit-license, j3ssie]
related:
  - concepts/subagent-orchestration.md
  - entities/tools/conductor-mcp.md
  - entities/patterns/tier1-tier2-agent-model.md
maturity: draft
created: 2026-05-16
updated: 2026-05-16
cross-wiki-source: "@cybersecurity-wiki/entities/tools/osmedeus.md"
---

## Relations

- @concepts/subagent-orchestration.md — Osmedeus's YAML-driven ACP agent loops are a concrete reference implementation of the subagent-dispatch model
- @entities/tools/conductor-mcp.md — the CCC conductor routes cross-wiki queries; Osmedeus's engine orchestrates subprocess agents — adjacent orchestration architecture
- @entities/patterns/tier1-tier2-agent-model.md — Osmedeus is a security-orchestration engine, the canonical home of execution-capable Tier-2 agents
- @cybersecurity-wiki/entities/tools/osmedeus.md — cross-wiki primary page (full tool write-up + audit lives in Cybersecurity)

## Raw Concept

Cross-routed from OSINT workspace tool-eval ingest 2026-05-16. Osmedeus is a security-orchestration engine (MIT, https://github.com/j3ssie/osmedeus). The CCC-relevant slice is its orchestration architecture, not its security-scanning payload. Primary page: `@cybersecurity-wiki/entities/tools/osmedeus.md` — the offensive-security detail belongs in the Cybersecurity wiki; this stub documents only the subagent-orchestration pattern.

## Narrative

**Pattern: a YAML-workflow engine natively orchestrating ACP subprocess agents — a reference architecture for the CCC conductor.**

Osmedeus is a Go-based engine driven by YAML workflow definitions. The CCC-relevant capability: it natively orchestrates **ACP (Agent Client Protocol) subprocess agents** — Claude Code, Codex, and others — running them as subprocesses with tool-calling agent loops and memory management built in.

This is a concrete reference implementation of the subagent-orchestration model CCC documents at `@concepts/subagent-orchestration.md` and the conductor architecture at `@entities/tools/conductor-mcp.md`:

- **Declarative orchestration** — the workflow is YAML, not imperative glue code. Agents, their inputs, and their sequencing are data.
- **ACP subprocess agents** — Claude Code and Codex run as managed subprocesses, each with its own tool-calling loop. This is the multi-agent-as-subprocess pattern, not the in-session `Agent`-tool pattern.
- **Memory management** — the engine handles per-agent memory across the workflow, the orchestration-side concern CCC's conductor and Tier-1/Tier-2 model also have to solve.

Osmedeus is **not** a tool CCC adopts — it is a security engine and its scanning payload is the Cybersecurity wiki's. It is catalogued here as an architectural reference: when CCC deepens the conductor design, Osmedeus's Go YAML-engine + ACP-subprocess model is a worked example to compare against. Full tool detail and any Phase-0 verdict are in the Cybersecurity primary page.

## Snippets

> Osmedeus's Go-based YAML-workflow engine natively orchestrates ACP subprocess agents (Claude Code, Codex) with tool-calling agent loops and memory management — a subagent-orchestration pattern for the CCC conductor architecture.
[Source: @cybersecurity-wiki/entities/tools/osmedeus.md]
