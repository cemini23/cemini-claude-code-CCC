---
title: "Setup Complete, Now You Are Compromised — weaponizing setup docs vs coding agents"
type: source
tags: [source, arxiv, security, coding-agent, supply-chain, harness, k179]
keywords: [2607.15143, install gap, typosquat, registry redirect, Claude Code, Cursor, pre-install gate]
related:
  - concepts/coding-agent-install-gap-and-preinstall-gate.md
  - concepts/client-as-first-order-harness-factor.md
  - concepts/skill-vetting.md
  - concepts/cage-1-enterprise-agent-governance-eval.md
  - sources/brief-k179-coding-agent-preinstall-gate-2026-07-17.md
  - briefs/2026-07-17_ccc-handoff-setup-weaponization-armor-route.md
  - "@cybersecurity-wiki/sources/arxiv-weaponizing-setup-instructions-coding-agents-2607.15143.md"
  - "@cybersecurity-wiki/concepts/coding-agent-supply-chain-install-gap.md"
maturity: draft
created: 2026-07-17
updated: 2026-07-18
---

## Relations

- `@concepts/coding-agent-install-gap-and-preinstall-gate.md` — synthesized steal
- `@concepts/client-as-first-order-harness-factor.md` — harness-model interaction (K140 sibling)
- Cybersec deepen: `@cybersecurity-wiki/sources/arxiv-weaponizing-setup-instructions-coding-agents-2607.15143.md`
- `@cybersecurity-wiki/concepts/coding-agent-supply-chain-install-gap.md`
- `@sources/brief-k179-coding-agent-preinstall-gate-2026-07-17.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Setup Complete, Now You Are Compromised: Weaponizing Setup Instructions Against AI Coding Agents |
| **Author** | Aadesh Bagmar, Pushkar Saraf |
| **arXiv** | 2607.15143 |
| **Pages** | 19 |
| **Retrieved** | 2026-07-17 |
| **Code** | none public |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.15143-setup-complete-now-you-are-compromised-weaponizi.pdf` |

## Narrative

### Thesis

AI coding agents (Claude Code, Cursor, Copilot CLI, Codex) install deps from README/requirements/Makefile **without verifying names, sources, or versions**. Editing those docs redirects agents to untrusted registries, vulnerable versions, or plausible wrong names. Authors call this the **install gap**.

### Key results

- Same model catches an attack on one harness and installs it on another → **security is harness×model**, not model alone (Fisher p≪0.01 on harness ablations).
- Blatant typosquats caught; **separator-confusion** names (`azurecore` vs `azure-core`) slip through, rate harness-dependent.
- **Source/registry redirection** missed almost everywhere (pip/npm/Cargo).
- Security prompts help only the named dimension; a **deterministic pre-install gate** (verify name/source/version before any code runs) closes most of the gap.
- Auto-exec harnesses (`--yolo`, `--force`, `--no-ask-user`) are especially exposed; Claude Code's approval dialog helps but is not a package authenticity check.

### CCC steal

Pair with K140 (client-as-first-order) and K151 Prebind: **package install is a bind action**. Prefer hooks/gates that block `pip`/`npm`/`cargo` until allowlist/hash/registry checks pass — not prompt-only hardening.

## Snippets

> "install-time security rests on the harness-model combination, not the model alone" — Abstract

> "a deterministic pre-install check that verifies names, sources, and versions before any code runs closes most of it" — Abstract
