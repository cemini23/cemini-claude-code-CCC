---
title: Deep research multi-wiki evaluation prompt — version lineage
type: concept
tags: [concept, prompt, gemini-deep-research, tool-evaluation, multi-wiki, cursor, claude-code]
keywords: [v3, v4, v5, seven surfaces, CCC wiki, tier classification, anti-hallucination, cross-wiki routing, license posture, world-cup-bot]
related:
  - concepts/cursor-ide-workspace.md
  - concepts/cross-wiki-routing.md
  - concepts/tools-we-dont-use.md
  - entities/tools/lazy-tool.md
  - entities/tools/conductor-mcp.md
  - entities/mcp-servers/librarian-kb-server.md
  - entities/tools/claude-code.md
  - sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md
maturity: validated
created: 2026-05-21
updated: 2026-05-31
---

## Relations

- `@concepts/cursor-ide-workspace.md` — Cursor as primary laptop harness (v4 surface 7)
- `@concepts/cross-wiki-routing.md` — post-eval stub/brief routing
- `@concepts/tools-we-dont-use.md` — Phase-0 NO-GO registry cross-check (v5)
- `@entities/tools/lazy-tool.md` — OSINT project MCP router
- `@entities/tools/conductor-mcp.md` — cross-wiki query
- `@entities/mcp-servers/librarian-kb-server.md` — wiki serving
- `@entities/tools/claude-code.md` — secondary harness (v4)
- `@osint-wiki/sources/multi-wiki-gemini-eval-prompt-2026-05-12.md` — v2 archive on OSINT wiki
- `@osint-wiki/concepts/tool-evaluation-framework.md` — methodology (bidirectional)

## Raw Concept

Question: **Where is the canonical copy-paste prompt for bulk URL / repo evaluation across all six domain wikis + CCC, and how did it evolve?**

## Narrative

Bulk tool evaluation uses **seven surfaces** (six domain wikis + **CCC wiki** as harness meta). There is **no** separate Cursor wiki — Cursor operational detail lives in CCC surface 7 as of v4.

### Version lineage

| Version | Date | Surfaces | Canonical path | Notes |
|---------|------|----------|----------------|-------|
| v1 | 2026-04-28 | 3 (Cemini / librarian / workflow) | `briefs/2026-04-28_gemini-deep-research-link-evaluation-prompt.md` (OSINT, gitignored) | Drove false NO-GO on cybersec/image-gen/SEO tools |
| v2 | 2026-05-12 | 7 (mislabeled surface 7 as "Workflow") | `@osint-wiki/sources/multi-wiki-gemini-eval-prompt-2026-05-12.md` | Compact table; archived |
| v3 | 2026-05-18+ | 7 (**CCC wiki** = surface 7) | `prompts/deep-research-multi-wiki-eval-v3-2026-05-21.md` | Used for K53/K54/K55 batches; frozen for reproducibility |
| v4 | 2026-05-21 | 7 (CCC = Cursor primary + Claude Code secondary) | `prompts/deep-research-multi-wiki-eval-v4-2026-05-21.md` | Frozen for reproducing K55–K84 batches |
| **v5** | **2026-05-30** | **7 + world-cup-bot inventory + inline license API** | **`prompts/deep-research-multi-wiki-eval-v5-2026-05-30.md`** | **Current default** — NO-GO registry, `gh` license lookup, sports LP `[TIME-VOLATILE]` |

**First v5 production batch:** K88 (2026-05-31, 29 URLs) — `@sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md`. Residual ~40% Gemini `NO LICENSE` false negatives on `gh api` spot-check.

### v5 deltas vs v4 [CONFIRMED 2026-05-30]

1. **Shipped stack inventory** — `world-cup-bot` modules 1–7; Polymarket LP evals default Reference-only unless named gap.
2. **Inline license lookup** — mandatory `gh api repos/<owner>/<repo> --jq '.license.spdx_id'` before tier assignment; `NO LICENSE FOUND` only after API + LICENSE file both fail.
3. **Phase-0 NO-GO registry** — explicit table (PageIndex, SwarmVault, Claude-OSINT, poly_data); cross-check `@concepts/tools-we-dont-use.md`.
4. **`[TIME-VOLATILE]`** flag for sports LP claims (re-run ≤7d pre-tournament).

### Runtime workflow

1. Paste **v5** + URL list into **Gemini Deep Research**.
2. On return, open **OSINT WORKSPACE** in Cursor; spot-check Adopt licenses via `gh` / Exa.
3. Ingest per `@osint-wiki/CLAUDE.md` ingest ops; cross-wiki briefs land in sibling `briefs/` folders.

### Anti-hallucination lesson (K53/K54)

Gemini's `NO LICENSE FOUND` layer was unreliable on 9–22% of URLs in two v3 batches; K84 reconfirmed ~30% false negatives when retrieval truncated. **Never ingest Adopt without LICENSE verification** on IP-sale-bearing surfaces — v5 makes GitHub API lookup mandatory.

## Snippets

- **v5 canonical:** `../prompts/deep-research-multi-wiki-eval-v5-2026-05-30.md` (relative to this wiki root's parent CCC repo)
- **v4 frozen:** `../prompts/deep-research-multi-wiki-eval-v4-2026-05-21.md`
- **v3 frozen:** `../prompts/deep-research-multi-wiki-eval-v3-2026-05-21.md`
