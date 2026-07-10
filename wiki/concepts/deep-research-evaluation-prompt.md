---
title: Deep research multi-wiki evaluation prompt — version lineage
type: concept
tags: [concept, prompt, gemini-deep-research, tool-evaluation, multi-wiki, cursor, claude-code]
keywords: [v3, v4, v5, v6, v7, v8, v9, v10, ten surfaces, game-dev-wiki, gambling-wiki, CCC wiki, tier classification, anti-hallucination, cross-wiki routing, revenue lens, genealogy, family-tree, world-cup-bot, wc-ticket-monitor, CeminiDFS, federation-hub, xsp-killer, poker-arena, tipdrop]
related:
  - concepts/cursor-ide-workspace.md
  - concepts/cross-wiki-routing.md
  - concepts/tools-we-dont-use.md
  - entities/tools/lazy-tool.md
  - entities/tools/conductor-mcp.md
  - entities/mcp-servers/librarian-kb-server.md
  - entities/tools/claude-code.md
  - sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md
  - sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md
  - @osint-wiki/concepts/game-dev-wiki-federation.md
  - concepts/multi-agent-evidence-artifact-layers.md
  - "@osint-wiki/concepts/computational-genealogy-archival-automation.md"
  - "@osint-wiki/concepts/italian-regional-genealogy-archive-playbook.md"
  - "@osint-wiki/concepts/active-project-research-routing.md"
  - "@osint-wiki/concepts/tool-evaluation-framework.md"
  - entities/tools/awesome-agent-engineering.md
maturity: validated
created: 2026-05-21
updated: 2026-07-10
---

## Relations

- `@concepts/cursor-ide-workspace.md` — Cursor as primary laptop harness (v4 surface 7+)
- `@concepts/cross-wiki-routing.md` — post-eval stub/brief routing
- `@concepts/tools-we-dont-use.md` — Phase-0 NO-GO registry cross-check (v5)
- `@entities/tools/lazy-tool.md` — OSINT project MCP router
- `@entities/tools/conductor-mcp.md` — cross-wiki query
- `@entities/mcp-servers/librarian-kb-server.md` — wiki serving
- `@entities/tools/claude-code.md` — secondary harness (v4)
- `@osint-wiki/concepts/active-project-research-routing.md` — ingest brief routing (K156 family-tree pivot)
- `@osint-wiki/concepts/tool-evaluation-framework.md` — methodology (bidirectional)

## Raw Concept

Question: **Where is the canonical copy-paste prompt for bulk URL / repo evaluation across all eight domain/specialist wikis + CCC, and how did it evolve?**

## Narrative

Bulk tool evaluation uses **ten surfaces** (Cemini **active prod bots** — XSP killer, poker arena, PM/Kalshi exploratory — + seven specialist wikis including **gambling-wiki** and **game-dev-wiki** + **CCC wiki** as harness meta + **TipDrop.io** friend project). Co-primary hobby slot (Jul 2026): **family-tree / computational genealogy** (`Desktop/family/`, OSINT K153/K154) — **castle-sim deprioritized**.

### Version lineage

| Version | Date | Surfaces | Canonical path | Notes |
|---------|------|----------|----------------|-------|
| v1 | 2026-04-28 | 3 (Cemini / librarian / workflow) | `briefs/2026-04-28_gemini-deep-research-link-evaluation-prompt.md` (OSINT, gitignored) | Drove false NO-GO on cybersec/image-gen/SEO tools |
| v2 | 2026-05-12 | 7 (mislabeled surface 7 as "Workflow") | `@osint-wiki/sources/multi-wiki-gemini-eval-prompt-2026-05-12.md` | Compact table; archived |
| v3 | 2026-05-18+ | 7 (**CCC wiki** = surface 7) | `prompts/deep-research-multi-wiki-eval-v3-2026-05-21.md` | Used for K53/K54/K55 batches; frozen |
| v4 | 2026-05-21 | 7 (CCC = Cursor primary + Claude Code secondary) | `prompts/deep-research-multi-wiki-eval-v4-2026-05-21.md` | Frozen for reproducing K55–K84 batches |
| v5 | 2026-05-30 | 7 + world-cup-bot inventory + inline license API | `prompts/deep-research-multi-wiki-eval-v5-2026-05-30.md` | Frozen after K88; NO-GO registry, `gh` license lookup |
| v6 | 2026-05-31 | 8 (+ `gambling-wiki` surface 3) | `prompts/deep-research-multi-wiki-eval-v6-2026-05-31.md` | Frozen after K114; sports betting / casino / DFS split |
| v7 | 2026-06-13 | 9 (+ `game-dev-wiki` surface 8) | `prompts/deep-research-multi-wiki-eval-v7-2026-06-13.md` | Frozen after K120; game-dev surface |
| **v8** | **2026-06-21** | **9 (same surfaces)** | **`prompts/deep-research-multi-wiki-eval-v8-2026-06-21.md`** | Frozen after 2026-06-27 batches; librarian offline |
| **v9** | **2026-06-28** | **10 (+ TipDrop.io surface 10)** | **`prompts/deep-research-multi-wiki-eval-v9-2026-06-28.md`** | Frozen after 2026-06-28 batches; license-first lens |
| **v10** | **2026-07-06** | **10 (same surfaces)** | **`prompts/deep-research-multi-wiki-eval-v10-2026-07-06.md`** | **Current default** — revenue-first lens; license/ToS demoted to implementation notes |

**First v6 production batch:** K90 (2026-05-31, 41 URLs) — `@sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md` (adds gambling-wiki surface).

**First v7 note:** K115 (2026-06-13) — `@game-dev-wiki` bootstrap; no bulk URL batch yet.

### v10.1 delta (2026-07-10) [CONFIRMED]

1. **castle-sim demoted** to legacy deprioritized (Jul 2026 operator pivot).
2. **family-tree / computational genealogy** promoted to co-primary #4 — private `Desktop/family/` + OSINT wiki K153/K154 methodology.
3. **`genealogy overlap`** field added (8 shipped modules: archival ladder, Gramps/GEDCOM, FS API, Antenati IIIF, HTR, entity resolution, regional playbook, US census staging).
4. Personal projects use **value hypothesis** when `Revenue confidence: none`.

### v10 deltas vs v9 [CONFIRMED 2026-07-06]

1. **Primary lens** — **"how does this make us money?"** replaces **"can we use this?"** License, ToS, compliance are implementation friction notes — never tier drivers.
2. **Per-URL revenue fields** — `Revenue hypothesis`, `Revenue confidence`, `Revenue timeline`, `Project fit`, `Integration play`, `Improvement`, `Combo plays`.
3. **Tiers redefined** — Integrate / Extract / Watch / Context / Pass (maps to v9 Adopt / Steal-from / Defer / Reference-only / Reject for ingest compat).
4. **TipDrop compliance** reframed as **business-continuity risk** (MRR threat), not moral gate.
5. **Post-run** — revenue-path validation, not mandatory license audit.

### v9 deltas vs v8 [CONFIRMED 2026-06-28]

1. **Surface 1 reframed** — "Cemini financial suite" → **Cemini active prod bots** (XSP killer, dev.fun poker arena, PM/Kalshi exploratory); MAPPO/Riskfolio/conductor equity **legacy deprioritized**.
2. **Surface 10: TipDrop.io** — David's Discord signals SaaS; compliance-first eval (CFTC/NFA/AI-washing).
3. **Shipped inventories** — xsp-killer, devfun-poker-arena, castle-sim, tipdrop-workspace-kit added.
4. **Overlap fields** — `poker-arena overlap`, `xsp-killer overlap`, `tipdrop overlap` in per-URL template.
5. **Active project map** — co-primary canon: poker-arena, CeminiDFS, xsp-killer, castle-sim.

### v8 deltas vs v7 [CONFIRMED 2026-06-21]

1. **Shipped stack inventory** — `wc-ticket-monitor`, `CeminiDFS`, `cemini-federation-hub` alongside `world-cup-bot`.
2. **Overlap fields** — `wc-ticket-monitor overlap` + `CeminiDFS overlap` in per-URL template (mirror world-cup-bot).
3. **Librarian offline** — `cemini-librarian` deleted 2026-06-14; egress-fi raw archive; laptop `federation_paths.yaml` for cross-wiki reads.
4. **Cross-routing** — FIFA ticket alerts, NFL nflverse pipelines, federation morning-summary tools.

### v7 deltas vs v6 [CONFIRMED 2026-06-13]

1. **`game-dev-wiki` surface 8** — public repo for hobby castle/RTS research, engine Phase-0, vertical slices (`@game-dev-wiki/concepts/game-dev-wiki-scope.md`).
2. **game-dev vs CCC split** — game-dev-wiki = game design + game-specific harness; ccc-wiki (surface 9) = generic subagent/MCP.
3. **Nine-column fit matrix** — Game-dev wiki column in per-URL template + aggregate summary.
4. **Cross-routing examples** — Godot RTS kits, engine Phase-0 audits, Claude-Code-Game-Studios steal-from, sprite pipelines → image-gen primary.

### v6 deltas vs v5 [CONFIRMED 2026-05-31]

1. **`gambling-wiki` surface 3** — public repo for sports betting, casino, poker, DFS, best ball, PM **retail** strategy (`@gambling-wiki/concepts/gambling-wiki-scope.md`).
2. **OSINT vs gambling split** — osint-wiki = PM/Kalshi **bots/LP**; gambling-wiki = *how to bet* (Kelly, CLV, bankroll, line shopping).
3. **Eight-column fit matrix** — Gambling wiki column in per-URL template + aggregate summary.
4. **Cross-routing examples** — DFS optimizers, sportsbook arb alerts, poker solvers → gambling primary.

### v5 deltas vs v4 [CONFIRMED 2026-05-30]

1. **Shipped stack inventory** — `world-cup-bot` modules 1–7; Polymarket LP evals default Reference-only unless named gap.
2. **Inline license lookup** — mandatory `gh api repos/<owner>/<repo> --jq '.license.spdx_id'` before tier assignment.
3. **Phase-0 NO-GO registry** — explicit table; cross-check `@concepts/tools-we-dont-use.md`.
4. **`[TIME-VOLATILE]`** flag for sports LP claims.

### Runtime workflow

1. Paste **`prompts/deep-research-multi-wiki-eval-v10-gemini-runtime.md`** + **≤20 URLs** (or a pre-split file under `prompts/batches/`) into **Gemini Deep Research**. Do **not** paste the full v10 canon with large URL lists — Deep Research often blanks before producing a plan.
2. On return, open **OSINT WORKSPACE** in Cursor; validate Integrate/Extract revenue hypotheses + project paths (license spot-check optional).
3. Ingest per `@osint-wiki/CLAUDE.md` ingest ops; cross-wiki briefs land in sibling `briefs/` folders; gambling-primary stubs → `@gambling-wiki/`; game-dev-primary stubs → `python3 scripts/cross_wiki_route.py --target-wiki game-dev-wiki` from OSINT.

### Anti-hallucination lesson (K53/K54)

Gemini's `NO LICENSE FOUND` layer was unreliable on 9–22% of URLs in two v3 batches. v5–v9 made license lookup mandatory before tier assignment. **v10 demotes license to implementation notes** — tier on revenue + project fit; note license friction when discovered but do not Pass solely on SPDX.

## Snippets

- **v10 Gemini runtime (paste this into Deep Research):** `../prompts/deep-research-multi-wiki-eval-v10-gemini-runtime.md`
- **v10 full canon (Cursor spot-check only):** `../prompts/deep-research-multi-wiki-eval-v10-2026-07-06.md`
- **v9 frozen:** `../prompts/deep-research-multi-wiki-eval-v9-2026-06-28.md`
- **v9 Gemini runtime (frozen):** `../prompts/deep-research-multi-wiki-eval-v9-gemini-runtime.md`
- **v8 frozen:** `../prompts/deep-research-multi-wiki-eval-v8-2026-06-21.md`
- **v7 frozen:** `../prompts/deep-research-multi-wiki-eval-v7-2026-06-13.md`
- **v6 frozen:** `../prompts/deep-research-multi-wiki-eval-v6-2026-05-31.md`
- **v5 frozen:** `../prompts/deep-research-multi-wiki-eval-v5-2026-05-30.md`
- **v4 frozen:** `../prompts/deep-research-multi-wiki-eval-v4-2026-05-21.md`
- **v3 frozen:** `../prompts/deep-research-multi-wiki-eval-v3-2026-05-21.md`
