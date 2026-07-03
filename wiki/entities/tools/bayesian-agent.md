---
title: Bayesian-Agent — posterior-guided skill evolution framework
type: entity
tags: [entity, tool, bayesian-agent, skill-evolution, harness, k109]
keywords: [bayesian-agent, dataarctech, mit, claude-code-backend, incremental-repair]
related:
  - sources/arxiv-bayesian-agent-posterior-skill-evolution-2606.08348.md
  - concepts/bayesian-posterior-guided-skill-evolution.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/skill-vetting.md
  - entities/tools/claude-code.md
  - sources/brief-k109-bayesian-agent-harness-cluster-prod-2026-06-10.md
maturity: draft
created: 2026-06-10
updated: 2026-07-03
---

## Relations

- `@sources/arxiv-bayesian-agent-posterior-skill-evolution-2606.08348.md` — arXiv provenance
- `@concepts/bayesian-posterior-guided-skill-evolution.md` — methodology synthesis
- `@concepts/skill-vetting.md` — install gate before posterior layer trusts new skills
- `@entities/tools/claude-code.md` — optional execution backend

## Raw Concept

Reference implementation for arXiv **2606.08348** — Bayesian evidence layer + native harness with adapters for GenericAgent, mini-swe-agent, Claude Code.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | https://github.com/DataArcTech/Bayesian-Agent |
| **License** | MIT (GitHub API 2026-06-10) |
| **Stars** | ~27 (2026-06-10) |
| **Phase-0** | `scripts/adopt_k109_phase0.sh` — PASS 2026-06-10 (`pip install -e`, CLI `--help`) |
| **Datasets** | `JinyiHan99/GA-Technical-Report` — GA paper eval bundle (SOP-Bench, Lifelong, RealFin); not Cemini domain data — clone as `GA-Technical-Report/datasets` beside Bayesian-Agent parent |
| **Live trial** | 2026-06-10 — SOP-Bench full **20/20** baseline + bayesian-full on `deepseek-v4-flash`; incremental repair **60%→100%** on 5-task slice; ~48k tokens/task avg |

**Verdict:** CONDITIONAL-GO laptop trial — posterior audit for skill registry; not a replacement for `@concepts/skill-vetting.md` Phase-0 or OpenSpec acceptance.

### vs openevolve / RHO

| Tool | Optimizes |
|------|-----------|
| openevolve | Harness artifacts via evolution |
| retro-harness (RHO) | Full harness from trajectories |
| Bayesian-Agent | Per-skill posterior + rewrite policy |

## Snippets

> "Claude Code are treated as optional backends behind the same trajectory-evidence boundary."

> — [Source: arxiv-bayesian-agent-posterior-skill-evolution-2606.08348.md, retrieved 2026-06-10]

## Dead Ends

- Expecting posterior layer to vet **license/security** of third-party skills — still requires Phase-0 skill audit.
