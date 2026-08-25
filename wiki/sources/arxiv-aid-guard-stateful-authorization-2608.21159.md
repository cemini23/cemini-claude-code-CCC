---
title: "AID-Guard — stateful authorization for delegated agent effects"
type: source
tags: [source, arxiv, security, authorization, mcp, effects, commit, k302]
keywords: [2608.21159, AID-Guard, authorization-to-effect, reservation lineage, delivery fence, stripe, compromise]
related:
  - concepts/authorization-to-effect-closure.md
  - entities/tools/aid-guard.md
  - concepts/execution-fidelity-irreversible-agent-invariants.md
  - briefs/2026-08-25_ccc-k300-k309-sip-ready.md
maturity: draft
read_status: read
created: 2026-08-25
updated: 2026-08-25
---

## Relations

- `@concepts/authorization-to-effect-closure.md`
- `@entities/tools/aid-guard.md`
- `@concepts/execution-fidelity-irreversible-agent-invariants.md`
- `@briefs/2026-08-25_ccc-k300-k309-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | AID-Guard: Stateful Authorization for Delegated Agent Effects |
| **arXiv** | 2608.21159 |
| **Authors** | Yingzhe Tong, Leyu Dai, Songhui Guo (Information Engineering University) |
| **Code** | none public — Python/SQLite prototype described in paper only → **policy only** |
| **Retrieved** | 2026-08-25 |

## Narrative

Authorization commonly **ends at admission** while mutable provider state, delivery, retry, and recovery continue. A request can change before commit; an effect can occur while its response is lost; a naive replacement then creates a **second effect from one approval**. AID-Guard is a stateful **authorization-to-effect closure** protocol:

1. **Revalidate at commit** — the exact approved request *and* current provider state.
2. **One reservation while ambiguous** — outcome unknown ⇒ hold the reservation.
3. **At most one successor** — release or a single successor only after a terminal result **or certified no-effect with a delivery fence**, through the declared recovery horizon.

Evaluation (loopback MCP domain): 13 live mutations → zero unauthorized provider effects; 4 outcome traces preserved commit/recovery semantics; 3 concurrent histories linearizable; all **210 Stripe provider-contract trials** matched predeclared outcomes; 40 terminalize-then-successor + 30 overlapping confirm/cancel races + 10 crash-recovery schedules with **no duplicate effect**. Under complete proposer compromise: **blocked all 44 attacks while admitting all 44 matched legitimate proposals**. Cost: strict exact-manifest profile cut benign utility by 35.4–43.8 pp.

Pairs K239 execution-fidelity invariants (irreversible actions) and K285 Mandato (signed mandates): admission-time approval ≠ effect-time authority.

| Verdict | **ADOPT policy** — revalidate at commit; one reservation under ambiguity; ≤1 successor after certified no-effect + fence. No public SPDX repo → **policy_wired** only. |
|---------|---------|

## Snippets

> "It revalidates the exact approved request and current provider state at commit, retains one reservation while the outcome is ambiguous, and permits release or one successor only after a terminal result or certified no effect with a delivery fence." [Source: arXiv 2608.21159 abstract]

> "Under complete proposer compromise, AID-Guard blocked all 44 submitted attacks while admitting all 44 matched legitimate proposals." [Source: arXiv 2608.21159 abstract]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.21159-aid-guard-stateful-authorization-for-delegated-a.pdf` |
|--------------|-------------------------------------------------------------------------------------------------------------------|
