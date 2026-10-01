---
title: "Cogentic: Multi-Agent Orchestration for Automated Proof Discovery (CCC K414)"
type: concept
tags: [concept, k414]
keywords: [2609.40324, k414]
related:
  - sources/arxiv-cogentic-verified-ledger-proof-orchestration-2609.40324.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-10-01_ccc-k411-k415-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-10-01
updated: 2026-10-01
---

## Relations

- `@sources/arxiv-cogentic-verified-ledger-proof-orchestration-2609.40324.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-10-01_ccc-k411-k415-sip-ready.md`

## Raw Concept

K414: ADOPT pattern (Google Research) — arXiv 2609.40324.

## Narrative

**Cogentic — a research group, as a harness.** Google Research's multi-agent harness for open proof problems keeps **two separate stores**, and that separation is the design. The **record** holds every prover attempt with its verifier critiques and *why it failed*; the **verified ledger** holds only intermediate results that cleared adversarial verification, and **later rounds build only on the ledger**. An orchestrator assigns prover slots across distinct proof directions and spawns summarizers to condense history into per-prover **briefings**; an **advisor reads across rounds and tunes standing instructions**; verifiers attack each draft **alone and then alongside the others from the round**. Rounds repeat until a draft clears or the budget runs out. Budget is O(100)–O(1000) model calls per problem. It produced verified novel results on five open problems in online learning, auction theory, and mechanism design. **CCC relevance:** this is the K410 control/worker split with two additions worth wiring — a **promotion barrier** (failed attempts stay in the record and can never be built on) and **cross-round instruction tuning** by a separate advisor role. Pairs K410 agentic meta-reasoning / K406 Assay (claims vs verified claims) / K403 Tracekit / `@concepts/glasswing-deliberate-disagreement.md` (adversarial re-check) / `@concepts/subagent-orchestration.md`. **No code repo** (results site only). Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "See source page for arXiv 2609.40324 locators." [Source: CCC K414 synthesis]
