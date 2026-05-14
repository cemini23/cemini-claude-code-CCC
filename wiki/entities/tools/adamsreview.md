---
title: "adamsreview — async Claude-Code code-review plugin with PEP 723 inline-script architecture"
type: entity
category: tool
tags: [entity, tool, claude-code-plugin, async-code-review, pep-723, artifact-json-state, k44, k37-orthogonal-not-convergent, conditional-go-phase-0-2026-05-14]
keywords: [adamsreview, artifact-patch-py, artifact-json-schema, pep-723-inline-script, persistent-state-tracking, gh-cli, mit-license, multi-lens-l1-l7-pipeline, opus-sonnet-codex-orchestration, bash-primary-runtime]
related: []
maturity: validated
created: 2026-05-14
updated: 2026-05-14
cross-wiki-source: "@osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md"
---

## Relations

- @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md — K44 source (doc-level verdict)

## Raw Concept

A Python 3.10+ Claude Code plugin for **asynchronous code review** with persistent JSON state tracking via `artifact.json` schema and **PEP 723 inline-script shebangs** (eliminates venv overhead). Uses `artifact-patch.py`, `uv`, `jq`, `gh CLI`. MIT, claimed 188 stars. K44 verdict: **Adopt**. Primary fit: CCC. Cross-route: Cemini-financial (PR review automation).

## Narrative

### Phase-0 audit verdict (2026-05-14): CONDITIONAL-GO

| # | Gate | Status | Finding |
|---|------|--------|---------|
| G0 | Repo discovery | **PASS** | `adamjgmiller/adamsreview` resolved; single author, no satellite repos |
| G1 | Star + maturity | **CONDITIONAL** | 189★ verified (+1 drift vs claimed 188), 227 commits in 3.5 weeks (active dev), but **single-maintainer bus factor** (claude account = 1 test commit only) |
| G2 | License | **PASS** | MIT verbatim, copyright 2026 Adam Miller |
| G3 | PEP 723 architecture | **PASS** | Genuine PEP 723 inline scripts (`#!/usr/bin/env -S uv run --quiet --script`); uv 0.7+ caches deps; cold-start <100ms after first run. **Primary runtime is Bash 3.2** (macOS-portable); Python only for `artifact-patch.py` + `artifact-render.py` |
| G4 | artifact.json schema | **PASS** | Production-grade JSON Schema 2020-12 at `bin/schema-v1.json`. 11-state disposition FSM, scoring phases (3/4/4a/4b), validation with blast-radius, fix attempts with regression tracking. **Atomic writes** (tmp→rename), not append-only. Path: `~/.adams-reviews/<slug>/<branch>/<review_id>/` (outside `.claude/` to avoid permission prompts) |
| G5 | K37 architectural comparison | **DIVERGENT — DO NOT REBASE** | See dedicated section below. K37 = inference-time gate (call-level, ephemeral). adamsreview = post-hoc code review (finding-level, persistent FSM). **Orthogonal, not convergent.** |
| G6 | Cemini-financial PR-review fit | **CONDITIONAL** | Multi-language support exists (Python/TypeScript/Go/SQL mentioned in lens prompts). **No domain-specific rule injection path** — lenses (L1–L7) hard-coded in `fragments/lens-prompts/`. Finance customization requires fork or future config-driven lens API |
| G7 | Plugin install path | **PASS** | `/plugin marketplace add adamjgmiller/adamsreview` → `/plugin install adamsreview@adamsreview`. Installs to `~/.claude/plugins/`. Per-repo or system-wide. No conflicts with existing Claude Code skills detected |
| G8 | Failure-mode audit | **CONDITIONAL** | Comprehensive smoke tests (`test/smoke.sh`, 40+ assertions). Phase 4 validation pass (Opus deep / Sonnet light). **No published false-positive baseline** (anecdotal n=1 claim); cost auto-tally via `subagent_tokens` but no hard cap or rollback trigger |
| G9 | "Definitive SKILL.md template" claim | **FAIL — UNSUPPORTED** | **No SKILL.md file exists in the repo.** `.claude-plugin/plugin.json` is standard Claude Code plugin metadata, not a template. K44 eval claim is marketing overreach; restate as "well-documented Claude Code plugin with extensive helper library" |

**Verdict: CONDITIONAL-GO** (pending Cemini-specific evaluation; do NOT rebase K37).

### K37 vs adamsreview — CRITICAL FINDING (G5 deep dive)

The Phase-0 audit found **architectural mismatch** between K37 reviewer-agent v2 and adamsreview. **They are orthogonal, not convergent.**

| Dimension | K37 spec | adamsreview | Convergence? |
|-----------|----------|-------------|--------------|
| Problem space | Inference-time tool-call gating | Post-hoc code-review automation | **Orthogonal** |
| State model | Ephemeral call-level audit JSONL with reviewer block | Persistent finding-level FSM (11-state disposition) | **Divergent** |
| Trigger mechanism | Static side-effect allowlist + confidence-threshold gate (fail-closed) | Multi-lens detection (L1–L7 parallel) + score gate (45/60/75 bands) | **Divergent** |
| Reviewer model | Single DeepSeek-R1 invoke, 8s timeout, fallback-to-approve | Opus deep + Sonnet light ensemble across multi-phase pipeline | **Partially overlapping** |
| Async pattern | Intra-call middleware (block on trigger, non-blocking on read-only) | Inter-phase pipeline orchestration (phases serial, lenses parallel) | **Divergent** |
| Tool surface | FastMCP / Conductor middleware (proprietary Cemini infra) | `gh CLI` + `jq` + `git` + optional Codex CLI (open-source) | **Divergent** |
| LLM invocation sequencing | Single reviewer invoke per triggered call | Multi-phase multi-invoke (Phase 1 lens fan-out, Phase 4 validation, Phase 8 fix agents, Phase 9 re-review) | **Orders-of-magnitude divergent** |
| Harmfulness audit harness | Shadow-mode Phase 1 + 25% harmfulness rollback dashboard | **Not present** — anecdotal n=1 claim only | **Missing in adamsreview** |

**Recommendation: K37 remains standalone Conductor middleware. adamsreview remains standalone Claude Code plugin. Do NOT attempt to merge codebases — incompatible insertion points + state models.**

**Future integration possibility (deferred)**: Use adamsreview as a **post-hoc audit layer** after K37 gates a tool call — operating on different timescales (K37 real-time, adamsreview async). No code rebase required, just orchestration.

### Cemini-financial CONDITIONAL-GO conditions

Before broad adoption on `/opt/cemini`:

1. **Phase 0 eval (1-2 weeks)** — Run `:adamsreview:review` on 10 recent Cemini PRs (mix Python + TypeScript). Set NO-GO bars:
   - False-positive rate: ≤10% (vs built-in `/review`)
   - False-negative rate: <5% on finance-domain patterns (secret logging, slippage bounds, position limits)
2. **Plugin install smoke test (immediate)** — `/plugin marketplace add adamjgmiller/adamsreview`, run on a docs-only PR, verify artifact path + PR-comment posting
3. **Domain customization roadmap (deferred)** — If Phase 0 passes, fork lens prompts or negotiate rule-injection API with adamjgmiller (~50-100 LOC refactor for config-driven lens list)
4. **K37 decision: STAY SEPARATE** — Mark K37 Sprint 5 as resuming with standalone Conductor middleware path (no rebase onto adamsreview)

### Correction to K44 source eval

The K44 eval claim that adamsreview is "the definitive template for structuring SKILL.md specifications" is **unsupported by the source repo** (no SKILL.md file present). Restate as: "well-documented Claude Code plugin with clear phase-based architecture and extensive helper library." Update K44 source page to flag this correction.

## Snippets

> "This represents the definitive template for structuring SKILL.md specifications within the CCC-wiki and should be immediately adopted to enforce rigorous code quality gates on the /opt/cemini PostgreSQL and LangGraph pipelines."
[Source: @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md ¶277]
