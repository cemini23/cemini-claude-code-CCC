---
title: Context engineering — managing what's in the model's window
type: concept
tags: [concept, context, context-window, prompt-engineering, claude-code, summarization]
keywords: [context engineering, context window, summarization, compaction, lazy injection, ToolSearch, deferred tools, hot.md]
related:
  - entities/tools/claude-code.md
  - entities/tools/claude-mem.md
  - entities/patterns/ralph-loop.md
  - entities/patterns/full-prompt-goal-template.md
  - concepts/token-economics-and-prompt-caching.md
  - concepts/subagent-orchestration.md
  - concepts/hooks-for-automation.md
  - concepts/mcp-context-optimization.md
  - concepts/three-cache-architecture.md
  - entities/tools/everos.md
  - entities/tools/lazy-tool.md
  - entities/tools/ttok.md
  - concepts/nested-learning.md
  - entities/tools/polyterm-tui-pattern.md
  - concepts/twelve-rule-claude-md-template.md
  - entities/patterns/cpr-context-compression.md
  - entities/tools/repomix.md
  - entities/tools/anything-llm.md
  - concepts/html-as-claude-code-output-format.md
  - concepts/local-llm-mechanics-primer.md
  - entities/tools/open-design.md
  - concepts/skillrae-retrieval-augmented-execution.md
  - concepts/llm-engineering-stack-curriculum.md
  - concepts/rag-binary-quantization.md
  - concepts/claude-code-large-codebase-workflow.md
  - concepts/agent-token-discipline-openclaw-hermes.md
  - entities/tools/claude-subconscious.md
  - concepts/claude-prompt-engineering-techniques.md
  - concepts/karpathy-token-efficiency-patterns.md
  - concepts/harness-de-bloat-4x4-pattern.md
  - concepts/claude-code-skills-md-institutional-memory.md
  - concepts/claude-md-five-section-template.md
  - concepts/runtime-context-mcp-file-refs.md
  - concepts/claude-code-cheat-sheet-shortcuts.md
  - concepts/interaction-native-knowledge-harness.md
  - sources/arxiv-interaction-native-knowledge-harness-2606.01886.md
  - concepts/long-thread-context-decay.md
  - concepts/agent-backpressure-loop.md
  - sources/trading-posts-compilation-19-2026-06-07.md
maturity: validated
created: 2026-05-13
updated: 2026-06-07
---

## Relations

- `@entities/tools/claude-code.md` — the harness this concept applies to
- `@entities/tools/claude-mem.md` — passive observation layer; one input to the model context
- `@entities/patterns/ralph-loop.md` — Ralph's fresh-context-per-iteration is one extreme of context engineering
- `@entities/patterns/full-prompt-goal-template.md` — `/goal` pins durable context across summarization
- `@concepts/token-economics-and-prompt-caching.md` — context-engineering decisions are governed by cache + window economics
- `@concepts/subagent-orchestration.md` — subagents are how Cemini offloads context that doesn't need to land in the parent session
- `@concepts/hooks-for-automation.md` — hooks inject durable state into the session lifecycle
- `@concepts/mcp-context-optimization.md` — the four-layer stack Cemini uses to keep MCP-heavy sessions affordable
- `@concepts/three-cache-architecture.md` — the cache mechanism behind the discipline
- `@entities/tools/lazy-tool.md`, `@entities/tools/ttok.md` — concrete tools that make the discipline cheap
- `@concepts/nested-learning.md` — literature anchor: multi-timescale memory framing (Update Frequency) for the "context at different update rates" pattern
- `@entities/tools/polyterm-tui-pattern.md` — text-native (ASCII) visualization keeps tool output inside the model's context window
- `@entities/tools/repomix.md` — one-shot repo pack for LLM context (stale after edits)
- `@entities/tools/anything-llm.md` — reference local document-RAG workspace (not Claude Code harness)
- `@concepts/llm-engineering-stack-curriculum.md` — K69 engineering project path
- `@concepts/rag-binary-quantization.md` — K69 vector memory optimization
- `@concepts/claude-code-large-codebase-workflow.md` — K69 monorepo discipline

## Raw Concept

Question this page answers: **how does Cemini decide what enters and leaves Claude Code's context window?**

## Narrative

Claude Code's context is a finite token budget (1M on Opus 4.7 / Sonnet 4.6 long-context at the time of writing). The model reads tool-call results, file contents, harness instructions, user messages, and prior assistant turns — all from that budget. When the budget gets tight the harness summarizes older content. **Context engineering is the discipline of deciding what to keep, what to summarize, what to offload, and what to never load.**

### The four levers Cemini pulls

1. **Durable goal (`/goal`)** — survives summarization because the Stop hook re-evaluates it every turn. Use the `/goal` template (`@entities/patterns/full-prompt-goal-template.md`) for anything multi-step.
2. **Fresh context per iteration (Ralph)** — instead of one degrading window, run N short windows each re-reading the same persistent files. Trade prompt-cache amortization for context cleanliness.
3. **Subagent offload** — heavy reads (codebase exploration, large repo audit, deep research) go to a subagent. Only the subagent's brief result lands in the parent context. See `@concepts/subagent-orchestration.md`.
4. **Deferred / lazy tool surfaces** — `ToolSearch` keeps MCP tool definitions out of the prompt until needed. Saves ~10-30K tokens per session for the full Cemini MCP surface (Exa + Brave + Playwright + claude-mem + stash + finance-* + …).

### Cemini's curated state surfaces

The wiki itself is a context-engineering tool — it externalizes durable facts so the model can `Read` only the slice it needs:

- **`hot.md`** — last-position + open-decisions + pending-actions. Re-read at session-start. Rewritten at session-end. Gitignored.
- **`ROADMAP.md`** — active workstreams + done log. Committed.
- **`wiki/index.md`** — page catalog. The Query workflow says "read index first."
- **`wiki/log.md`** — chronological operations log. Append-only.
- **`LESSONS.md`** — meta-lessons. Read on-demand when a sibling-wiki pattern surfaces.

The hierarchy when they disagree: `ROADMAP.md` > `hot.md` > `claude-mem` injections (see `@entities/tools/claude-mem.md`).

### What burns context (avoid)

- Pasting raw HTML / PDF bytes — use `crawling_exa` instead
- Reading full files when `Grep`/`smart_explore`/sub-section reads would do
- Enumerating MCP tool definitions in the prompt — use `ToolSearch` deferred-tool pattern
- Long single-context sessions past ~300-400K tokens — switch to Ralph

### What saves context (use)

- `Read` with `offset` + `limit` for targeted slices of large files
- `Grep` + `Glob` for symbol/file lookup over full-file reads
- Subagent dispatch for codebase exploration > 3 queries deep
- `claude-mem:smart-explore` for tree-sitter AST-aware code search

### Cross-cutting principle

**Externalize durable state, ingest only the slice you need.** The wiki's three-layer architecture (raw / wiki / schema) and the curated `hot.md`/`ROADMAP.md`/`LESSONS.md` surfaces are all expressions of this principle. Per-session context becomes a working set, not a long-term store.

## Dead Ends

- **Treating context as a knowledge base** — gets summarized away. Use the wiki.
- **Loading the whole MCP tool surface up front** — wastes 10-30K tokens. Use `ToolSearch`.
- **Re-loading the same file across many turns** — wastes cache invalidations. Edit in place; the harness tracks file state.
