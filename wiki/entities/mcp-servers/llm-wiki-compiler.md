---
title: "llm-wiki-compiler — Karpathy-pattern wiki compiler with MCP server (npm, Wave 4B Adopt)"
type: entity
tags: [mcp-server, wiki-compiler, karpathy-pattern, knowledge-base, llmwiki, hash-incremental, fastmcp, cross-wiki-stub]
keywords: [llm-wiki-compiler, llmwiki, atomicmemory, karpathy, two-phase-compile, hash-incremental, candidate-review-queue, confidence-metadata, contradicted-by, mcp]
related:
  - entities/mcp-servers/librarian-kb-server.md
  - entities/mcp-servers/stash.md
  - entities/mcp-servers/anthropic-skills.md
  - concepts/cross-wiki-routing.md
maturity: draft
created: 2026-05-17
updated: 2026-05-17
cross-wiki-source: "@osint-wiki/sources/atomicmemory-llm-wiki-compiler.md"
---

## Relations

- @entities/mcp-servers/librarian-kb-server.md — the deployed wiki-serving layer; llm-wiki-compiler is the candidate upstream compiler that would feed the librarian's index
- @entities/mcp-servers/stash.md — complementary memory layer (compiler outputs static markdown; stash holds dynamic episodic memory)
- @entities/mcp-servers/anthropic-skills.md — both are MCP servers reachable via the same SKILL.md / MCP protocol surface
- @concepts/cross-wiki-routing.md — the compiler's "raw → wiki → schema" pipeline mirrors the federation's cross-wiki routing decision (where new content belongs)
- @osint-wiki/sources/atomicmemory-llm-wiki-compiler.md — cross-wiki primary source page; full Phase-0 audit, Karpathy-pattern coverage matrix, and 4-doc cross-evaluation history live there

## Raw Concept

CCC-side stub for the llm-wiki-compiler MCP server. `github.com/atomicmemory/llm-wiki-compiler` (also at llmwiki.app) — open-source compiler implementing Karpathy's late-2025 LLM Wiki pattern. Ships an MCP server (`llmwiki serve`) alongside the compile pipeline. OSINT verdict: Wave 4B Adopt, **primary adoption candidate for the workspace librarian**; covers 7 of 10 Karpathy-pattern components. This stub catalogues the Claude-Code-side relevance.

## Narrative

### What it does (CCC-relevant slice)

- **Two-phase compile** — raw sources → wiki pages → schema-extracted entities. Each phase is hash-incremental (only recompile what changed).
- **MCP server** — `llmwiki serve` exposes the compiled wiki to any MCP client. Parallels Cemini's `cemini_mcp` FastMCP container (different transport / endpoint; can coexist).
- **Multi-provider LLM backend** — `LLMWIKI_PROVIDER=openai` + `OPENAI_BASE_URL` swap works with DeepSeek, LocalAI, Ollama, OpenRouter. Matches Cemini's brain-agnostic pattern.
- **Candidate-review queue** — flagged claims surface to a human review queue rather than auto-merging. Matches Cemini's `[NEEDS VERIFICATION YYYY-MM-DD]` discipline.

### Why catalogued here, not just in OSINT

The compiler is an upstream tool for any of Cemini's wikis, not just OSINT. If Cemini ever needs to recompile CCC's wiki into a different output format (LLM-friendly index, schema-extracted entity graph, candidate-review queue), llm-wiki-compiler is the most evaluated candidate. Even though CCC is laptop-only and not synced to the librarian by default, the compiler runs locally on a markdown tree — no server needed.

### Phase-0 caveats (from OSINT)

- **Maturity**: ethanj + 5 contributors; healthy contributor count (not a bus-factor risk like @entities/mcp-servers/stash.md).
- **Karpathy-pattern coverage**: 7 of 10 components. The 3 gaps (per OSINT) are areas where Cemini's existing librarian + claude-mem already cover the gap.
- **Karpathy lineage**: implements the foundational pattern from Karpathy's 2025 gist (`@osint-wiki/sources/llm-wiki.md`). Two sibling Karpathy-pattern implementations exist: `wastedcode/memex` (simpler, filesystem-only) and claude-obsidian (vault-overlay, rejected). llm-wiki-compiler is the headless / MCP variant.
- **Cross-evaluation**: 4 independent OSINT evaluations across waves 2/4a/4b/5b. Most cross-evaluated item in the OSINT corpus.

### CCC-side decision

Not currently adopted in CCC. The wiki is small enough (<50 pages) that the manual ingest workflow (`scripts/preingest_check.py` + LLM synthesis) is faster than running a compile pipeline. Adoption would make sense if (a) the wiki crosses ~200 pages, or (b) Cemini wires CCC into the librarian and wants automated re-indexing.

## Snippets

> The knowledge compiler. Raw sources in, interlinked wiki out.
[Source: @osint-wiki/sources/atomicmemory-llm-wiki-compiler.md]
