# ROADMAP — CCC Wiki

Active workstreams, open decisions, and the done log for the Cemini Claude Code meta-wiki.

## Active

- **Federated daily digest (K93)** — `scripts/daily_research_config.yaml` + LaunchAgent `com.cemini.daily-research-digest.ccc`; weekly Monokern topic in config. Load agent when ready.
- **Deepen seed pages** — first 16 pages are bootstrap-grade. Each should be deepened with concrete examples (real `.claude/settings.json` snippets, real hook payloads, real `/goal` invocations from past sessions) as those examples surface.
- **Ingest pipeline calibration** — `preingest_check.py` matches the OSINT version. Confirm its arXiv/DOI/URL regexes still hit reasonable signals on Claude Code source material (mostly markdown docs + repo READMEs, less paper-shaped than OSINT corpus).
- **Add per-pattern brief templates** — `briefs/templates/` for: new-hook-recipe, new-mcp-adoption, new-skill-skeleton, new-slash-command-skeleton. Deferred until first 3 real briefs exist.

## Open decisions

- **Skill catalog scope** — do we mirror catalog content (anthropic-skills, claude-mem skills, finance-skills) or only document the spec + our internal skills? Decision pinned 2026-05-13 in CCC LESSONS.md: spec-only, no catalog content dependency. Revisit if a downstream consumer needs a per-skill catalog page.
- **Tier-2 sweep** — OSINT's wiki_gap_detect Tier-2 sweep is roadmapped there. Not wired here yet; defer until the corpus is large enough that gaps are non-obvious by inspection (likely > 50 pages).
- **Librarian sync** — **closed 2026-06**: `cemini-librarian` decommissioned. Earlier 2026-05-21 wire is historical only. Workspace stays laptop-only; raw archives go to `cemini-egress-fi` (see `CLAUDE.md`).

## Follow-ups (parked)

- **Harness-evolution claim re-audit (K169, 2026-07-15)** — `concepts/harnessx-composable-evolution-foundry.md`, `concepts/retrospective-harness-optimization-rho.md`, and `concepts/hierarchical-skill-stack-lazy-orchestration.md` (K164) all carry `[NEEDS VERIFICATION 2026-07-15]` tags per `concepts/harness-evolution-vs-test-time-scaling-baseline.md` — none were checked against a test-time-scaling baseline or held-out generalization split. Revisit before any of those three graduate past `draft`/`CONDITIONAL-GO`.

- **SPDX watch (K333–K336 leftovers)** — run `bash scripts/spdx_watch_harness_wave.sh` periodically. Clone only after SPDX + Phase-0. **2026-09-30: the watch was broken and is now rewritten.** Three separate defects: (1) `--json licenseInfo` is rejected by the installed `gh`, and `2>/dev/null || echo '[]'` swallowed the error; (2) `gh search repos` matches on **name/description only**, so the arXiv-title queries could never hit — every repo reported "no repo found" as a false negative; (3) `gh search` returns `license.key`, not `license.spdxId`, so even a hit would print `NOASSERTION`. The script now takes an explicit `owner/repo` slug via `gh api` when the paper names its repo, and falls back to name-shaped search otherwise. **Results (2026-09-30):** `QwenLM/RecreationWorld` **MIT** (89★) and `RUCAIBox/Agent-Editing-World-Model` **Apache-2.0** (9★) — both SPDX watches now cleared, clone gated only on a Phase-0 maturity read. `ShawnChenn/RecToolBench` re-confirmed **MIT**. `ustc-time-series/TokenCast` is a **name collision** (pushed 2025-11 — a year before the paper) and is not the K405 repo; TokenCast stays unwatched. No repo surfaced for InstructionArbitrationBench, HarnessDesignCodingAgents, AgentApprovalLaundering, or MotorMind.

- **Assay HITL clone (K406, 2026-09-30)** — `OmShiv/assay-research` is Apache-2.0 and ships an MCP server. **MCP audit done 2026-09-30** (detail on `wiki/concepts/assay-content-addressed-evidence-graphs.md`): stdio transport is clean, `dependencies = []` confirmed, **but `attest` runs a model-supplied command via `subprocess.run(..., shell=True)` with a 900s timeout** — shell execution behind a non-`Bash` tool name. Verdict: `wont_wire`. **Unblock condition:** re-classify `attest` as shell-equivalent, or bound it to an operator-approved allowlist. The *protocol* (cone-hash claim binding + the 8-check mechanical gate + evidence monotonicity) needs no code and is adoptable as a CCC policy rule now.

- **MetaSkill-AI4AI SPDX watch (K409, 2026-09-30)** — `qiancheng-apodex/MetaSkill-AI4AI` returns **null SPDX** (no license file). NO-GO on clone. Watch for a license file. The meta-skill `(when, provide, use)` pattern is adoptable as policy without the code.

- **Dense+RRF SCOUT over live MCP catalog (K311 leftover)** — HITL; local BM25 SCOUT shipped 2026-08-31.

- **HoH runtime wrap (K335)** — REFERENCE clone only; meta-harness must not replace Cursor/`/route` without HITL eval contract.

- **Hook-test harness** — write a fixture that drives Claude Code with a controlled `settings.json` and observes hook firings. Deferred; today we lint hook *documentation*, not hook behavior.
- **`/goal` invocation history** — capture every past `/goal` prompt + its outcome in `wiki/sources/goal-invocations-*.md`. Provides a corpus to mine for the `goal-recipe-` family of patterns.
- **OpenSpec end-to-end** — once 3+ real OpenSpec runs land, write `concepts/openspec-end-to-end-workflow.md`.

## Known limitations (by design)

- **No librarian sync** — laptop-only. Not a bug; matches Cybersecurity / 3D-printing / Image-gen / SEO posture.
- **No Tier-2 outbound sweep** — descriptive lint only, no autonomous external research.
- **Seed corpus is bootstrap-thin** — 16 pages ≠ comprehensive. The corpus grows passively as Cemini's Claude Code work generates source material worth ingesting.
- **Catalog content (third-party skills/MCP) intentionally minimal** — we cover the *spec* (SKILL.md), our *audit pattern* (Phase-0), and our *internal use*. Per LESSONS.md 2026-05-13, catalog content has too high churn to mirror.

## Done
- **2026-09-28** — K396–K400 harness wave: 5 arXiv ingests + Phase-0/1, archive, lint, CI.
- **2026-09-25** — K395 approval laundering ingest + K390/K392 federation precheck helpers.

- **2026-09-25** — K390–K394 harness wave: 5 arXiv ingests + Phase-0/1, archive, lint, CI. Progressive skill access control + behavior assays + monitor evasion + trace tampering policy. Zero clones.
- **2026-09-24** — K385–K389 harness wave: 5 arXiv ingests + Phase-0/1, archive, lint, CI. KV working-set + surrogate consumer eval + agent-editing world model. Zero clones.
- **2026-09-23** — K376–K384 harness wave: 9 arXiv ingests + Phase-0/1, archive, lint, CI. MCP granularity + RRSI + A2M metadata policy + truncate-only compaction. Zero clones.
- **2026-09-21** — K373–K375 harness wave: 3 arXiv ingests + Phase-0/1, archive, lint, CI green. EnterpriseVal + RCA pattern + RecreationWorld hybrid CUA. Zero clones.
- **2026-09-19** — Full ingest check: Sep 19 daily digest (0 new PDFs); preingest 4 DUPLICATE (K369–K372); phase0 re-pass; lint green. Archive to egress-fi **blocked** (SSH timeout) — 4 PDFs remain in inbox.
- **2026-09-30** — K406–K410 harness wave: 5 arXiv ingests + Phase-0/1, one cross-cutting concept (`headless-claude-code-controlled-eval-lane`, confirmed by 2 independent sources), archive, lint, CI green. Repaired malformed 2609.35472 cross-route stub. Fixed silent `licenseInfo` bug in `spdx_watch_harness_wave.sh`. Phase-0: Assay Apache-2.0 (CONDITIONAL-GO), longmemeval-evidence MIT, MetaSkill-AI4AI null SPDX (NO-GO clone). Zero clones.
- **2026-09-18** — K369–K372 harness wave: 4 arXiv ingests + Phase-0/1, lint, CI green. Archive attempted; egress-fi flaky. Zero clones.
- **2026-09-17** — K368 implicit-trust MCP (2609.18217 digest-cap follow-up) + K363–K367 harness wave. Phase-0/1, archive, lint, CI green. Cybersec steals. Zero clones.
- **2026-09-16** — K358–K362 harness wave: 5 arXiv ingests + Phase-0/1, archive, lint, CI green. Cybersec steal K360/K362. Zero clones.
- **2026-09-11** — K346–K357 harness wave: 12 arXiv ingests + Phase-0/1, archive, lint, CI green. Cybersec steal K350. Zero clones.
- **2026-06-05** — K100 deep-read: HarnessFix/ETCLOVG synthesized; memory paper routed OSINT; flaw-record template + workflow rule adopted.
- **2026-05-13** — Public repo + CI. `cemini-claude-code-CCC` created, GitHub Actions lint workflow added, lint green on first run, pushed.
- **2026-05-13** — Cross-wiki deep-dive sweep. Mined OSINT/Cybersec/SEO/3D-printing/Image-gen for Claude Code material. 16 new pages + 8 deepened pages + 10 sibling-wiki backlinks added. ccc-wiki registered in SEO and Cybersec Related Wikis tables. 32 pages total; lint clean.
- **2026-05-17** — Parked-followup batch. 10 of 11 deep-dive follow-ups cleared as cross-wiki stubs: agent-vm-sandboxing, skill-vetting, twelve-rule-claude-md-template, claude-obsidian, cpr-context-compression, autoresearch-loop, scatter-gather, stash, llm-wiki-compiler, polymarket-mcp-server. Backlinks added on 17 existing CCC pages. structured-findings-schema deferred (no primary); kb-server closed as duplicate of librarian-kb-server.

## Follow-ups from the deep-dive (parked)

These surfaced in the cross-wiki sweep but didn't make this batch. Each warrants its own page when a Cemini workstream demands it:

- `entities/patterns/structured-findings-schema.md` — JSON schema for findings (cybersec inheritance; generalizes to skill-audit + Phase-0 audit JSON outputs). Deferred 2026-05-17 — no primary page in OSINT/Cybersec yet; revisit when Cemini ships its own structured-findings shape.
