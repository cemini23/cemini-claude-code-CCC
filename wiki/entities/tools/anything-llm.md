---
title: AnythingLLM — private local document AI workspace (MIT)
type: entity
tags: [tool, local-llm, rag, documents, cross-wiki-route]
keywords: [anything-llm, mintplex-labs, local-ai, document-rag, private-chat]
related:
  - entities/tools/claude-mem.md
  - entities/mcp-servers/stash.md
  - entities/mcp-servers/librarian-kb-server.md
  - concepts/local-llm-mechanics-primer.md
  - concepts/context-engineering.md
  - concepts/cross-wiki-tool-eval-inventory.md
maturity: draft
created: 2026-05-22
updated: 2026-05-22
cross-wiki-source: "@osint-wiki/sources/trading-posts-oil-polymarket-html-dex-sniping-2026-05-21.md"
---

## Relations

- `@entities/tools/claude-mem.md` — Claude Code-native observation memory; AnythingLLM is a separate local chat+RAG UI
- `@entities/mcp-servers/stash.md` — server-side episodic memory; different deployment shape
- `@entities/mcp-servers/librarian-kb-server.md` — wiki serving layer; AnythingLLM is generic doc RAG, not wiki-schema-aware
- `@concepts/local-llm-mechanics-primer.md` — local inference economics when running bundled models
- `@concepts/context-engineering.md` — document chunking + retrieval as context strategy

Cross-wiki: K55-2 ridark #47; license **MIT CONFIRMED** 2026-05-22 (~60.5k★).

## Raw Concept

`Mintplex-Labs/anything-llm` — self-hosted **private document chat** (alternative to ChatGPT Enterprise / Claude for Work for local docs). CCC documents it as a **reference architecture** for local RAG UX, not a replacement for Claude Code + wiki conductor stack.

## Narrative

### Why CCC cares (reference only)

- **BYOK / local model** wiring patterns overlap open-design + stash backends
- **Workspace-per-collection** mirrors multi-wiki federation at UI level — different implementation than `@entities/tools/conductor-mcp.md`

### Adoption posture

| Check | Status |
|-------|--------|
| License | MIT [CONFIRMED 2026-05-22] |
| Phase-0 | **Deferred** — large surface; Cemini already has claude-mem + librarian path |
| Verdict | **REFERENCE** — steal UI/RAG patterns; no production dependency |

## Dead Ends

- **Replacing Claude Code for coding tasks** — wrong tool class; document chat ≠ agent harness.
