---
title: omnifs — projected filesystem for APIs (/omnifs)
type: entity
tags: [tool, agent-infrastructure, mcp-adjacent, k108]
keywords: [omnifs, 0xff-ai, fuse, wasm-providers, path-namespace]
related:
  - sources/trading-posts-compilation-8-2026-06-09.md
  - concepts/mcp-context-optimization.md
  - entities/tools/lazy-tool.md
  - concepts/skill-vetting.md
  - "@osint-wiki/entities/tools/omnifs.md"
  - concepts/cross-wiki-tool-eval-inventory.md
maturity: draft
created: 2026-06-09
updated: 2026-06-09
phase_0_verdict: "CONDITIONAL-GO 2026-06-09 — Apache-2.0; laptop eval only; not prod/kb-server"
---

## Relations

- `@sources/trading-posts-compilation-8-2026-06-09.md` — K108 Post 1 (@raulvk)
- `@concepts/mcp-context-optimization.md` — path namespace vs MCP catalog overhead
- `@entities/tools/lazy-tool.md` — overlap on fetch/github; omnifs adds shell ergonomics
- `@osint-wiki/entities/tools/omnifs.md` — canonical Phase-0 audit

## Raw Concept

- **URL:** https://github.com/0xff-ai/omnifs
- **Site:** omnifs.dev
- **License:** Apache-2.0 [CONFIRMED 2026-06-09 via `gh api`]
- **Stars / push:** ~57★ / 2026-06-09

## Narrative

Projects external APIs into FUSE paths (`/github`, `/linear`, `/arxiv`, …). **Wasm providers** declare callouts; **host acts** on capability-gated network/credentials ("providers ask, host acts").

| Check | Result |
|-------|--------|
| Overlap | Partial — lazy-tool already proxies MCP; omnifs = path-NS + `cat`/`grep` ergonomics |
| Ops | Alpha; Docker+FUSE; read-only v0.2.1 |
| Failure mode | Credential store `~/.omnifs`; not kb-server replacement |

**Verdict:** **CONDITIONAL-GO** laptop trial via `scripts/adopt_k108_phase0.sh`. **NO-GO** prod/librarian/conductor until design brief.

**Steal-from (no install):** path namespace as agent handoff primitive; Wasm/host-callout trust boundary for MCP hardening.

## Phase-0 Audit (2026-06-09)

Clone + `gh api` license; full `omnifs setup` not run (Docker+FUSE). See OSINT entity for install steps.

## Snippets

> "The common layer is the path namespace." [Source: Posts.docx K108, @raulvk Post 1]
