---
title: Coding-agent install gap and deterministic pre-install gate
type: concept
tags: [concept, security, coding-agent, supply-chain, harness, k179]
keywords: [2607.15143, install gap, typosquat, registry redirect, Prebind]
related:
  - sources/arxiv-weaponizing-setup-instructions-coding-agents-2607.15143.md
  - concepts/client-as-first-order-harness-factor.md
  - concepts/cage-1-enterprise-agent-governance-eval.md
  - concepts/skill-vetting.md
  - concepts/mcp-contract-grounded-synthesis-and-validation-gate.md
  - sources/brief-k179-coding-agent-preinstall-gate-2026-07-17.md
  - concepts/policy-as-code-layered-validation-for-agent-artifacts.md
  - sources/arxiv-satellite-mission-compiler-policy-as-code-2607.14798.md
  - "@cybersecurity-wiki/concepts/coding-agent-supply-chain-install-gap.md"
  - "@cybersecurity-wiki/sources/arxiv-weaponizing-setup-instructions-coding-agents-2607.15143.md"
  - sources/arxiv-flowguard-mcp-security-evidence-2607.14754.md
  - concepts/mcp-security-signals-vs-runtime-evidence.md
  - sources/arxiv-schema-bound-mcp-instrument-skills-2607.17012.md
maturity: draft
created: 2026-07-17
updated: 2026-07-21
---

## Relations

- `@sources/arxiv-weaponizing-setup-instructions-coding-agents-2607.15143.md` — K179 provenance
- `@concepts/client-as-first-order-harness-factor.md` — harness flips outcomes for same model
- `@concepts/cage-1-enterprise-agent-governance-eval.md` — Prebind before bind actions
- `@concepts/mcp-contract-grounded-synthesis-and-validation-gate.md` — validation-before-execute sibling (K172)
- `@cybersecurity-wiki/concepts/coding-agent-supply-chain-install-gap.md` — cybersec deepen

## Raw Concept

How should Claude Code / Cursor / Codex block malicious package installs driven by poisoned setup docs?

## Narrative

### Steal checklist

1. Treat `pip`/`npm`/`cargo`/`uv` install as **Prebind-class** actions (K151).
2. Prefer a **deterministic pre-install gate** (name ∈ allowlist or exact PyPI match; registry host allowlist; pin versions) over security prompts alone.
3. Never run coding agents with blanket auto-approve for package managers in untrusted repos.
4. Audit harness choice: same model can flip catch→install when swapping Cursor/Codex auto-exec vs Claude Code approval.
5. Watch separator-confusion typosquats and registry redirects — agents miss sources more than names.

### Verdict

**ADOPT** pre-install gate discipline for Cemini coding-agent sessions. **REFERENCE** paper empirics. **NO-GO** code (none published).

## Snippets

> "Neither a stronger model nor a better prompt substitutes for the right architecture" — Conclusion
