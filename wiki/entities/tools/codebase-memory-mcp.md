---
title: DeusData/codebase-memory-mcp — Tree-sitter code intelligence MCP
type: entity
tags: [entity, tool, mcp, federation, k134]
keywords: [codebase-memory-mcp, tree-sitter, sqlite, call-graph, token-reduction, federation-mcp]
related:
  - "@osint-wiki/entities/tools/codebase-memory-mcp.md"
  - sources/eval-github-repos-plan-multi-wiki-2026-06-29.md
  - sources/brief-k134-codebase-memory-cursor-federation-prod-2026-06-29.md
  - concepts/cursor-ide-workspace.md
  - entities/tools/lazy-tool.md
  - entities/tools/mattpocock-skills.md
maturity: validated
created: 2026-06-29
updated: 2026-06-29
cross-wiki-eval: "@osint-wiki/sources/eval-github-repos-plan-multi-wiki-2026-06-29.md"
---

## Relations

- `@osint-wiki/entities/tools/codebase-memory-mcp.md` — K134 Phase-0 eval (MIT, 20.7k★)
- `@sources/brief-k134-codebase-memory-cursor-federation-prod-2026-06-29.md` — prod + laptop deploy brief
- `@concepts/cursor-ide-workspace.md` — federation MCP surface

## Raw Concept

K134 **CONDITIONAL-GO** adoption of [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) — C + Tree-sitter + SQLite knowledge graph exposed via MCP for structural repo comprehension across federation workspaces.

## Narrative

| Field | Value |
|-------|-------|
| **License** | MIT [CONFIRMED gh api 2026-06-29] |
| **Verdict** | **CONDITIONAL-GO** — laptop federation only; read-tool allowlist |
| **Binary** | `~/.local/bin/codebase-memory-mcp` v0.8.1 (checksum-verified release) |
| **Sync** | `bash scripts/sync_federation_codebase_memory_mcp.sh` (OSINT WORKSPACE) |
| **Prod** | Awareness brief on `cemini-prod:/opt/cemini/briefs/` — **no trading-runtime dependency** |

Indexes repo ASTs into a persistent graph; **14 MCP tools** for call-graph, architecture overview, HTTP route discovery. Eval claims ~99% token reduction vs file-by-file Read loops for `get_architecture` (~1,500 vs ~100,000 tokens).

### Allowlist (P2 gate)

**Allow:** `get_architecture`, `search_graph`, `trace_path`, `get_code_snippet`, `index_status`, `detect_changes`

**Deny for now:** `delete_project`, write-heavy ADR tools until policy review

### Explicit NO-GO

- Prod Lane A/B executors, Redis, order egress
- Agent-Reach (cookie/ToS), stealth-browser-mcp (Playwright overlap)
- deepsec investigate pass on live trading paths without change window

### Re-deploy checklist

1. `codebase-memory-mcp update -y`
2. `bash scripts/sync_federation_codebase_memory_mcp.sh` (OSINT)
3. `bash scripts/sync_federation_cursor_skills.sh` (CCC)
4. `bash scripts/scp_harness_briefs_to_prod.sh`

## Snippets

> "get_architecture enables comprehensive codebase overviews at ~1,500 tokens vs ~100,000 file-by-file."
> — [Source: @osint-wiki/sources/eval-github-repos-plan-multi-wiki-2026-06-29.md]
