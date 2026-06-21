---
title: claude-mem — passive observation memory for Claude Code
type: entity
tags: [tool, memory, claude-code, plugin, observation, sqlite, chromadb]
keywords: [claude-mem, observation memory, sessionstart hook, semantic recall, bun, sqlite, chromadb, lazy injection]
related:
  - entities/tools/claude-code.md
  - concepts/context-engineering.md
  - concepts/hooks-for-automation.md
  - concepts/mcp-context-optimization.md
  - entities/tools/thuki.md
  - concepts/nested-learning.md
  - entities/tools/skillkit.md
  - entities/tools/claude-obsidian.md
  - entities/patterns/cpr-context-compression.md
  - entities/tools/everos.md
  - entities/mcp-servers/stash.md
  - concepts/code-as-agent-harness.md
  - concepts/self-healing-agent-sessions.md
  - concepts/retrospective-harness-optimization-rho.md
  - entities/tools/anything-llm.md
  - concepts/obsidian-agent-maintenance-workflow.md
  - concepts/agent-token-discipline-openclaw-hermes.md
  - concepts/claude-obsidian-notebooklm-bridge.md
  - entities/tools/claude-subconscious.md
  - concepts/agent-memory-stack-comparison.md
  - entities/tools/obsidian-second-brain-eugeniughelbur.md
  - concepts/autosci-memory-centric-research-agents.md
  - sources/arxiv-autosci-2605.31468.md
  - concepts/worldmemarena-multimodal-agent-memory-eval.md
  - sources/arxiv-worldmemarena-agent-memory-2605.29341.md
  - concepts/interaction-native-knowledge-harness.md
  - concepts/agentic-memory-cross-scenario-generality.md
  - concepts/long-thread-context-decay.md
  - concepts/time-series-native-agent-harness.md
  - sources/arxiv-timeclaw-contextualized-time-series-2606.05404.md
  - concepts/multi-factor-agentic-memory-value-model.md
  - sources/arxiv-multi-factor-agentic-memory-2606.12945.md
  - concepts/storage-budgeted-agent-memory-compression.md
  - sources/arxiv-memrefine-storage-budgeted-memory-2606.13177.md
  - concepts/executable-user-memory-user-as-code.md
  - sources/arxiv-user-as-code-executable-memory-2606.16707.md
  - entities/tools/user-as-code.md
  - entities/tools/lightmem2.md
maturity: validated
created: 2026-05-13
updated: 2026-06-21
---

## Relations

- `@entities/tools/claude-code.md` — host harness; claude-mem hooks on `SessionStart`
- `@concepts/context-engineering.md` — second layer of memory on top of `hot.md` curation
- `@concepts/hooks-for-automation.md` — claude-mem ships a canonical `SessionStart` hook
- `@concepts/mcp-context-optimization.md` — claude-mem's injection cap interacts with the four-layer cost stack
- `@entities/tools/thuki.md` — local-SQLite conversation-history overlay; K44 mis-framed it as a CC persistence layer (SKIP verdict) — contrast with claude-mem, which actually is one
- `@entities/tools/claude-obsidian.md` — competing tool rejected for SessionStart-hook collision with claude-mem
- `@entities/patterns/cpr-context-compression.md` — preserve/resume legs claude-mem operationalises
- `@entities/mcp-servers/stash.md` — durable-storage MCP layer complementing claude-mem's session-bridge memory
- `@concepts/nested-learning.md` — literature frame: claude-mem (per-session observations) is one update-frequency layer in Cemini's multi-timescale memory stack
- `@entities/tools/skillkit.md` — skillkit's session memory captures transient architectural insights, conceptually adjacent to claude-mem's passive observation layer
- `@concepts/code-as-agent-harness.md` — passive observation memory in harness mechanisms layer
- `@concepts/self-healing-agent-sessions.md` — cross-session failure-pattern recall

## Raw Concept

Installed at Cemini's laptop level on 2026-05-10 (K35 GO verdict). Apache-2.0. The corresponding OSINT LESSONS entry (OSINT WORKSPACE root `LESSONS.md`, 2026-05-10) is the authoritative narrative on why Cemini accepted it; this page is the Claude-Code-specific surface.

## Narrative

`claude-mem` is a Bun + SQLite + ChromaDB worker that **passively observes Claude Code tool calls and file edits**, stores them as embedded observations in a local vector DB, and injects the top-N semantically-relevant observations on `SessionStart`. It is exposed as a Claude Code plugin — `mcp__plugin_claude-mem_mcp-search__*` MCP tools (search, query_corpus, smart_outline, timeline, etc.) plus a set of skills (`claude-mem:timeline-report`, `claude-mem:make-plan`, `claude-mem:do`, `claude-mem:learn-codebase`).

Cemini's posture on claude-mem follows the **two-layer memory model** documented in OSINT's `LESSONS.md` (2026-05-10 entry — file lives at the OSINT workspace root, outside the wiki/ alias surface):

| Layer | Source of truth for | Update cadence | Reliability |
|-------|---------------------|----------------|-------------|
| `hot.md` | curated intentional state — decisions, next-step pointers, sprint mode | end of every session (LLM rewrites) | high — user-reviewed |
| `claude-mem` | passive observation — what files were read, what commands ran, what was tried | continuous (worker daemon) | medium — semantic recall, not curated |
| `ROADMAP.md` | active workstream truth — DONE log, decisions, pending workstreams | after significant operations | high — committed to git |

When the three disagree, hierarchy is `ROADMAP.md` > `hot.md` > `claude-mem`. Treat claude-mem injections as advisory ("we may have looked at X before") and confirm against the curated layers before acting.

**Critical sanity gate**: the default `CLAUDE_MEM_SEMANTIC_INJECT_LIMIT=5` cap is what makes this safe to leave running. Raising it past ~20 changes the token-budget calculus — recheck the session-start token impact before doing so. Lazy injection (`SEMANTIC_INJECT=false` default) means observations only surface on user-prompt relevance match, not blanket dump.

**Where claude-mem helps**: the "did we already try this?" question that `hot.md` won't capture because Cemini didn't think it worth recording. The `claude-mem:learn-codebase` skill front-loads a repo into observation memory (~5 min on a typical repo); the timeline-report skill compiles narrative project histories.

**Where claude-mem does not help**: workflow-rule decisions (those live in CLAUDE.md / LESSONS.md / ROADMAP.md), and anything user-facing (claude-mem is a tool, not a writer).

## Dead Ends

- **Treating claude-mem as a substitute for `hot.md`** — it isn't curated; reverse direction would lose the human-reviewed gating that makes `hot.md` reliable.
- **Trusting claude-mem injections that contradict `hot.md`** — see the layer-hierarchy rule above.
