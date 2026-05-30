---
title: Obsidian contribution-rate workflow — three-zone vault + five Claude flows
type: concept
tags: [concept, obsidian, claude-code, vault, contribution-rate, k78]
keywords: [cyrilxbt, capture-zone, active-zone, archive, output-folder, note-quality-metric]
related:
  - concepts/obsidian-vellum-second-brain-stack.md
  - concepts/obsidian-agent-maintenance-workflow.md
  - concepts/claude-obsidian-notebooklm-bridge.md
  - concepts/five-layer-operator-stack.md
  - entities/tools/claude-obsidian.md
  - entities/tools/claude-code.md
  - sources/trading-posts-compilation-6-2026-05-29.md
maturity: draft
created: 2026-05-30
updated: 2026-05-30
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-6-2026-05-29.md"
---

## Relations

- `@concepts/obsidian-vellum-second-brain-stack.md` — sibling second-brain framing (K72); this page adds **contribution metric**
- `@concepts/obsidian-agent-maintenance-workflow.md` — vault hygiene vs output-oriented workflows
- `@concepts/claude-obsidian-notebooklm-bridge.md` — DamiDefi vault-thinking path (K69)
- `@concepts/five-layer-operator-stack.md` — Obsidian as memory layer in five-tool map (K78 Post 4)
- `@entities/tools/claude-obsidian.md` — **DO NOT ADOPT** — implement flows via Claude Code + git vault
- `@entities/tools/claude-code.md` — harness for the five workflows below
- `@sources/trading-posts-compilation-6-2026-05-29.md` — provenance (K78 Post 6)

Cross-wiki: `@osint-wiki/sources/trading-posts-compilation-6-2026-05-29.md`; SEO `@seo-wiki/concepts/obsidian-integration.md` (offline stack, separate ingest).

## Raw Concept

K78 Post 6 (@cyrilXBT): structure an Obsidian vault into **three zones** plus an **Output** folder, then run **five Claude-assisted workflows** optimized for notes that **produce output** — measured by **contribution rate** (how often a note led to a decision, write-up, or action), not raw note count.

## Narrative

### Three zones + Output

| Zone | Role |
|------|------|
| **Capture** | Fast inbox — unprocessed inputs |
| **Active** | Notes under refinement / linked thinking |
| **Archive** | Settled reference material |
| **Output** | Artifacts that left the vault (posts, decisions, shipped work) |

### Five workflows (pattern names)

1. **Daily processing** — triage Capture → Active or Archive
2. **Decision feeder** — link notes into explicit decision records
3. **Writing activator** — promote Active notes toward Output drafts
4. **Connection surface** — graph/backlinks to surface latent links
5. **Output generator** — Claude helps produce deliverables from vault context

**CCC implementation:** use Claude Code on git-backed markdown (wiki folders qualify). Same K67 guardrail: do not install `@entities/tools/claude-obsidian.md` (SessionStart collision with claude-mem).

### Contribution rate metric

Replace vanity metrics (note count, graph size) with **contribution events** — each time a note materially affected a decision, document, or action. Aligns with Cemini's ingest discipline (file insights into wiki/briefs, not chat-only synthesis).

## Snippets

> "The only metric that matters is the number of times a note contributed to something."
> — [Source: Posts.docx K78 Post 6, @cyrilXBT; @osint-wiki/sources/trading-posts-compilation-6-2026-05-29.md]
