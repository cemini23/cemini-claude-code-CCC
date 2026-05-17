# ROADMAP — CCC Wiki

Active workstreams, open decisions, and the done log for the Cemini Claude Code meta-wiki.

## Active

- **Deepen seed pages** — first 16 pages are bootstrap-grade. Each should be deepened with concrete examples (real `.claude/settings.json` snippets, real hook payloads, real `/goal` invocations from past sessions) as those examples surface.
- **Ingest pipeline calibration** — `preingest_check.py` matches the OSINT version. Confirm its arXiv/DOI/URL regexes still hit reasonable signals on Claude Code source material (mostly markdown docs + repo READMEs, less paper-shaped than OSINT corpus).
- **Add per-pattern brief templates** — `briefs/templates/` for: new-hook-recipe, new-mcp-adoption, new-skill-skeleton, new-slash-command-skeleton. Deferred until first 3 real briefs exist.

## Open decisions

- **Skill catalog scope** — do we mirror catalog content (anthropic-skills, claude-mem skills, finance-skills) or only document the spec + our internal skills? Decision pinned 2026-05-13 in CCC LESSONS.md: spec-only, no catalog content dependency. Revisit if a downstream consumer needs a per-skill catalog page.
- **Tier-2 sweep** — OSINT's wiki_gap_detect Tier-2 sweep is roadmapped there. Not wired here yet; defer until the corpus is large enough that gaps are non-obvious by inspection (likely > 50 pages).
- **Librarian sync** — by design this wiki is laptop-only. If a future consumer (e.g., a unified MCP query layer across all 5 wikis) needs CCC to be served, mirror the OSINT pattern: rsync to `cemini-librarian:/opt/cemini-wiki/ccc-wiki/wiki/`. Out of scope today.

## Follow-ups (parked)

- **Hook-test harness** — write a fixture that drives Claude Code with a controlled `settings.json` and observes hook firings. Deferred; today we lint hook *documentation*, not hook behavior.
- **`/goal` invocation history** — capture every past `/goal` prompt + its outcome in `wiki/sources/goal-invocations-*.md`. Provides a corpus to mine for the `goal-recipe-` family of patterns.
- **OpenSpec end-to-end** — once 3+ real OpenSpec runs land, write `concepts/openspec-end-to-end-workflow.md`.

## Known limitations (by design)

- **No librarian sync** — laptop-only. Not a bug; matches Cybersecurity / 3D-printing / Image-gen / SEO posture.
- **No Tier-2 outbound sweep** — descriptive lint only, no autonomous external research.
- **Seed corpus is bootstrap-thin** — 16 pages ≠ comprehensive. The corpus grows passively as Cemini's Claude Code work generates source material worth ingesting.
- **Catalog content (third-party skills/MCP) intentionally minimal** — we cover the *spec* (SKILL.md), our *audit pattern* (Phase-0), and our *internal use*. Per LESSONS.md 2026-05-13, catalog content has too high churn to mirror.

## Done

- **2026-05-13** — Bootstrap. CLAUDE.md schema, root meta files, scripts ported from OSINT, 16 seed pages, cross-wiki integration with OSINT, git repo initialized.
- **2026-05-13** — Public repo + CI. `cemini-claude-code-CCC` created, GitHub Actions lint workflow added, lint green on first run, pushed.
- **2026-05-13** — Cross-wiki deep-dive sweep. Mined OSINT/Cybersec/SEO/3D-printing/Image-gen for Claude Code material. 16 new pages + 8 deepened pages + 10 sibling-wiki backlinks added. ccc-wiki registered in SEO and Cybersec Related Wikis tables. 32 pages total; lint clean.
- **2026-05-17** — Parked-followup batch. 10 of 11 deep-dive follow-ups cleared as cross-wiki stubs: agent-vm-sandboxing, skill-vetting, twelve-rule-claude-md-template, claude-obsidian, cpr-context-compression, autoresearch-loop, scatter-gather, stash, llm-wiki-compiler, polymarket-mcp-server. Backlinks added on 17 existing CCC pages. structured-findings-schema deferred (no primary); kb-server closed as duplicate of librarian-kb-server.

## Follow-ups from the deep-dive (parked)

These surfaced in the cross-wiki sweep but didn't make this batch. Each warrants its own page when a Cemini workstream demands it:

- `entities/patterns/structured-findings-schema.md` — JSON schema for findings (cybersec inheritance; generalizes to skill-audit + Phase-0 audit JSON outputs). Deferred 2026-05-17 — no primary page in OSINT/Cybersec yet; revisit when Cemini ships its own structured-findings shape.
