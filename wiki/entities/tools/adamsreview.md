---
title: "adamsreview — async Claude-Code code-review plugin with PEP 723 inline-script architecture"
type: entity
category: tool
tags: [entity, tool, claude-code-plugin, async-code-review, pep-723, artifact-json-state, k44, k37-convergent, adopt-doc-level-pending-phase-0]
keywords: [adamsreview, artifact-patch-py, artifact-json-schema, pep-723-inline-script, persistent-state-tracking, gh-cli, mit-license]
related: []
maturity: adopt-doc-level-pending-phase-0
created: 2026-05-14
updated: 2026-05-14
cross-wiki-source: "@osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md"
---

## Relations

- @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md — K44 source (doc-level verdict)

## Raw Concept

A Python 3.10+ Claude Code plugin for **asynchronous code review** with persistent JSON state tracking via `artifact.json` schema and **PEP 723 inline-script shebangs** (eliminates venv overhead). Uses `artifact-patch.py`, `uv`, `jq`, `gh CLI`. MIT, claimed 188 stars. K44 verdict: **Adopt**. Primary fit: CCC. Cross-route: Cemini-financial (PR review automation).

## Narrative

This is **directly convergent with the K37 reviewer-agent v2 work** (currently in Sprint 5 deferred state per OSINT-wiki hot.md). The K44 eval positions adamsreview as a "definitive template for structuring SKILL.md specifications" — Phase-0 audit should explicitly compare against the K37 spec to identify shared patterns vs. divergent choices.

**Phase-0 gates**:
- G1: Star + maturity verification (`gh api repos/adamjgmiller/adamsreview`)
- G2: License (MIT confirmed)
- G3: Architectural comparison vs K37 reviewer-agent v2 spec — identify shared abstractions (artifact.json analogue?) and divergent design choices
- G4: PEP 723 inline-script pattern audit — confirm Python 3.10+ requirement is acceptable for Cemini stack
- G5: `artifact.json` schema portability — could it adopt the K37 audit-harness schema?

**Reconsideration framing**: if adamsreview's architecture is materially better than K37's current spec, the right move may be to **rebase K37 onto adamsreview** rather than implement two parallel reviewer plugins. Phase-0 makes that call.

## Snippets

> "This represents the definitive template for structuring SKILL.md specifications within the CCC-wiki and should be immediately adopted to enforce rigorous code quality gates on the /opt/cemini PostgreSQL and LangGraph pipelines."
[Source: @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md ¶277]
