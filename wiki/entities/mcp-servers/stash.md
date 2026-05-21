---
title: "stash — persistent memory MCP server (Go, Apache-2.0, Wave 5A Adopt-but-fork)"
type: entity
tags: [mcp-server, ai-memory, episodic-memory, postgres-pgvector, go, apache-2-0, claude-code, cross-wiki-stub]
keywords: [stash, alash3al-stash, persistent-memory-mcp, episodic-memory, fact-extraction, 8-stage-consolidation, claude-desktop, cursor, windsurf, single-binary]
related:
  - entities/tools/claude-mem.md
  - entities/mcp-servers/librarian-kb-server.md
  - entities/mcp-servers/anthropic-skills.md
  - entities/patterns/cpr-context-compression.md
  - entities/mcp-servers/llm-wiki-compiler.md
  - entities/tools/everos.md
  - concepts/code-as-agent-harness.md
  - concepts/self-healing-agent-sessions.md
  - concepts/cursor-ide-workspace.md
maturity: draft
created: 2026-05-17
updated: 2026-05-21
cross-wiki-source: "@osint-wiki/sources/alash3al-stash.md"
---

## Relations

- @entities/tools/claude-mem.md — Cemini's adopted laptop-side memory layer; stash is the deployed server-side complement (semantic injection vs persistent multi-session episodes)
- @entities/mcp-servers/librarian-kb-server.md — same Hetzner deployment surface; stash sits on the librarian alongside the kb-server retrieval layer
- @entities/mcp-servers/anthropic-skills.md — stash is an MCP server, surfaces via the SKILL.md / MCP protocol the marketplace catalogues
- @entities/patterns/cpr-context-compression.md — stash's 8-stage consolidation is a reference implementation of the CPR "compress" leg at the durable-storage layer
- @entities/mcp-servers/llm-wiki-compiler.md — sibling MCP server on the same Karpathy-pattern compiler / durable-store lineage; both candidates for the librarian-adjacent surface
- @concepts/code-as-agent-harness.md — episodic memory in harness mechanisms layer
- @concepts/self-healing-agent-sessions.md — execution traces + outcomes for integrated monitoring
- @osint-wiki/sources/alash3al-stash.md — cross-wiki primary source page; full Phase-0 audit, 8-stage consolidation detail, and Hetzner deployment notes live there

## Raw Concept

CCC-side stub for the stash MCP server. `github.com/alash3al/stash` — single-binary Go MCP server backed by PostgreSQL + pgvector, with an 8-stage consolidation pipeline for episodic memory. Apache-2.0. OSINT verdict: Wave 5A **Adopt-but-fork-and-pin** (single contributor, 6 days old at evaluation, bus-factor risk). Deployed on `cemini-librarian` (Hetzner CPX21). This stub catalogues the Claude-Code-side relevance; full audit lives in the OSINT source page.

## Narrative

### What it does (CCC-relevant slice)

- **MCP-protocol-compatible** with Claude Desktop, Cursor, Windsurf, Cline, Continue, plus OpenRouter / Ollama backends. Claude Code is the primary CCC consumer.
- **Episodic memory** — durable storage of "what happened in this session" across runs, accessible to the agent via MCP tool calls.
- **Fact extraction + 8-stage consolidation** — turns raw conversation into stable facts that survive recall noise.
- **Self-hosted, single binary, no cloud** — matches Cemini's laptop-server posture (binary lives on the Hetzner librarian, the laptop talks to it over MCP).

### How it relates to Cemini's existing memory stack

| Layer | Tool | Scope |
|-------|------|-------|
| Working-memory cache | `hot.md` | This session's open decisions / position; rewritten at session end |
| Session-bridge memory | @entities/tools/claude-mem.md | Cross-session observation index; semantic injection on SessionStart |
| Persistent episodic memory | **stash** (this page) | Long-horizon facts / episodes; survives many sessions |
| Retrieval-from-corpus | @entities/mcp-servers/librarian-kb-server.md | Wiki content over HTTP; not session memory |

The four layers are complementary, not competing. claude-obsidian was rejected partly because it tried to do all four with overlapping hooks (see @entities/tools/claude-obsidian.md).

### Phase-0 caveats (from OSINT)

- **License**: Apache-2.0 root verified.
- **Bus factor**: 1 contributor, 6 days old at OSINT evaluation. Adoption means **fork-and-pin** — pin a SHA, host the fork, accept upstream lag.
- **Transitive Go deps** require a sweep before commit (`jackc/pgx`, `mark3labs/mcp-go` flagged clean-by-reputation but not formally audited).
- **Operational fit**: Go binary ~50-100 MB + dedicated Postgres ~150-200 MB fits comfortably on the CPX21 (4 GB RAM / 80 GB NVMe).

## Snippets

> Persistent memory layer for AI agents. Episodes, facts, and working context stored in Postgres. MCP server included. Self-hosted, single binary, no cloud required.
[Source: @osint-wiki/sources/alash3al-stash.md]
