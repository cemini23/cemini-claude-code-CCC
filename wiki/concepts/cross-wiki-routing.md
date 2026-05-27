---
title: Cross-wiki routing — where new content belongs in the federation
type: concept
tags: [concept, cross-wiki, routing, federation, librarian, conductor, claude-code]
keywords: [cross-wiki routing, federation, wiki alias, ccc-wiki, osint-wiki, brief vs stub, on-topic check]
related:
  - entities/tools/conductor-mcp.md
  - entities/mcp-servers/exa.md
  - entities/mcp-servers/librarian-kb-server.md
  - concepts/subagent-orchestration.md
  - entities/mcp-servers/llm-wiki-compiler.md
  - concepts/cross-wiki-tool-eval-inventory.md
  - concepts/deep-research-evaluation-prompt.md
  - concepts/cursor-ide-workspace.md
  - concepts/tools-we-dont-use.md
  - entities/tools/ai-engineering-roadmap.md
  - entities/tools/awesome-cursorrules.md
  - entities/tools/hermes-agent.md
  - concepts/claude-code-personal-os-scope.md
  - concepts/obsidian-agent-maintenance-workflow.md
  - concepts/obsidian-trading-journal-workflow.md
  - concepts/agent-sandbox-unikraft.md
  - concepts/claude-obsidian-notebooklm-bridge.md
  - concepts/claude-code-finance-research-setup.md
maturity: validated
created: 2026-05-13
updated: 2026-05-27
---

## Relations

- `@entities/tools/conductor-mcp.md` — the runtime cross-wiki query router
- `@entities/mcp-servers/exa.md` — alternative fan-out via Exa for external sources
- `@entities/mcp-servers/librarian-kb-server.md` — backend the conductor reads from
- `@concepts/subagent-orchestration.md` — cross-wiki routing is a canonical multi-subagent dispatch
- `@entities/mcp-servers/llm-wiki-compiler.md` — candidate compiler whose raw→wiki→schema pipeline mirrors the routing decision
- `@concepts/cross-wiki-tool-eval-inventory.md` — the consolidated receipt of all CCC-routed tool-eval items; this page describes the routing pattern; that page is the output
- `@concepts/deep-research-evaluation-prompt.md` — bulk eval prompt (v4) drives tier + cross-routing fields
- `@concepts/cursor-ide-workspace.md` — Cursor-primary ingest spot-check path
- `@concepts/tools-we-dont-use.md` — reject register for routed-but-toxic tools (ridark lists, ToS bypass)

Cross-wiki: `@osint-wiki/concepts/librarian-server-architecture.md` carries the federation's serving-layer design history.

## Raw Concept

Question this page answers: **a new source landed in the inbox — which wiki(s) does it belong in, and how do we keep all five federation members coherent?**

## Narrative

The federation has six members (CCC + five domain wikis):

| Alias | Domain |
|-------|--------|
| `ccc-wiki` | Meta — how Cemini operates Claude Code |
| `osint-wiki` | Financial / quant / OSINT research |
| `cybersecurity-wiki` | Offensive + defensive security, certifications |
| `image-gen-wiki` | Uncensored image generation, model catalogs |
| `seo-wiki` | Local SEO, GBP, GEO/AEO |
| `3d-printing-wiki` | FDM/FFF printing, slicers, store ops |

Every wiki's CLAUDE.md has a "Related Wikis" table listing the other five with relative paths. The lint scripts parse this table to resolve `@<alias>/path` references.

### Decision: where does this source go?

The ingest workflow's **cross-wiki routing check** (step 4b in every wiki's CLAUDE.md) asks: does this source belong here, or somewhere else, or in multiple places?

- **Squarely on-topic** (≥80% of body content) → ingest here.
- **Tangentially on-topic** (10-50%) → write a brief in the most relevant wiki citing the source. Do not create a full entity page.
- **Off-topic** (≤10%) → route to the right wiki via a stub or brief.

The bias is **prefer brief over stub**. Briefs are cheap, scoped, time-stamped. Stubs create maintenance burden — orphan pages that need future deepening. OSINT's `cross_wiki_route.py` script encodes this preference by defaulting to `--type brief` unless the operator explicitly chooses `--type page`.

### Cross-link convention

When CCC page A references OSINT page B:

1. CCC page A includes the cross-wiki link (form: `@<alias>/<path>`) in body Relations + `related:` frontmatter.
2. OSINT page B gets a matching body @-mention back at the CCC source path (and ideally a frontmatter relation, though cross-wiki relations sometimes live in body-only).
3. Both sides' lint passes confirm the cross-wiki path resolves.

The lint script's check #8 (cross-wiki `@wiki-alias/path`) validates resolution. A missing backlink doesn't fail check #8 (because there's no symmetry expected on `body @-mentions`) but **good hygiene says add the backlink anyway** — future readers of B should be told that A references it.

### Routing tools

- **Manual routing** — read the source, decide, write the page or brief. Modal for solo-dev Cemini cadence.
- **`cross_wiki_route.py`** (OSINT) — creates a stub or brief in the target wiki from stdin content. Used when batch-routing.
- **`conductor_query` (MCP)** — runtime fan-out across wikis. Use when answering a query, not when ingesting.

### Multi-wiki sources

Some sources legitimately belong in 2+ wikis (e.g., a Claude Code skill for finance research belongs in both CCC + OSINT). The pattern:

1. Pick a *primary* wiki (the one with deeper coverage of the source's main topic).
2. Write the full source page in the primary wiki.
3. Write a *brief* in each secondary wiki citing the primary page's path via cross-wiki link.
4. Add bidirectional cross-wiki links between all touched pages.

Avoid duplicating full source pages across wikis — drift becomes inevitable.

### CCC-specific routing rules

CCC is the meta-wiki. Most material that lands here originates as a sibling-wiki insight ("we learned this while doing OSINT work"). The reverse — content originating in CCC and routing out — is rarer. When it happens, the route is usually to OSINT (Cemini's most active wiki) and the brief takes the form "OSINT-side example of CCC pattern X."

## Dead Ends

- **Creating a stub instead of a brief by default** — bias is brief unless the topic genuinely needs a durable page.
- **Forgetting the backlink** — lint won't catch it for body-only mentions; manual hygiene required.
- **Duplicating a full source page across wikis** — drift inevitable. Use briefs that cite the primary.
