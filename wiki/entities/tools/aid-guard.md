---
title: "AID-Guard — stateful authorization-to-effect closure (policy only)"
type: entity
tags: [entity, tool, security, authorization, policy-only, k302]
keywords: [2608.21159, AID-Guard, no public repo, commit revalidation, reservation]
related:
  - sources/arxiv-aid-guard-stateful-authorization-2608.21159.md
  - concepts/authorization-to-effect-closure.md
  - entities/skills/aid-guard-commit.md
  - entities/tools/mandato.md
  - briefs/2026-08-25_ccc-k300-k309-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-25
updated: 2026-08-25
---

## Relations

- `@sources/arxiv-aid-guard-stateful-authorization-2608.21159.md`
- `@concepts/authorization-to-effect-closure.md`
- `@entities/skills/aid-guard-commit.md`
- `@entities/tools/mandato.md` (K285 pair — mandates at admission, closure at effect)
- `@briefs/2026-08-25_ccc-k300-k309-sip-ready.md`

## Raw Concept

Phase-0 entity for CCC K302 — AID-Guard stateful authorization protocol; no public repo → policy only.

## Narrative

| Artifact | Repo | Verdict |
|----------|------|---------|
| AID-Guard protocol | none public | **policy only** — Python/SQLite prototype described in paper |

**Phase-0:** `scripts/adopt_k302_phase0.sh` — source + concept + policy grep checks; **no clone possible** (null SPDX hunt found nothing).

Commit-time revalidation of exact approved request + provider state; one reservation while ambiguous; ≤1 successor after certified no-effect + delivery fence. Evidence: 13 live mutations clean, 210/210 Stripe trials matched, 44/44 compromise attacks blocked at 35.4–43.8 pp strict-profile utility cost.

## Phase-1

`policy_wired` protocol + HITL skill `aid-guard-commit` / `scripts/aid_guard_commit.py` (selftest). Dual-ID: Cybersec K302 = PsychJail. Pairs K239 / K285. Not a Stripe/LIVE proxy.
