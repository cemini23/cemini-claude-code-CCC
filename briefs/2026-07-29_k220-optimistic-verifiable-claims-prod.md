---
title: K220 — Optimistic verifiable claims for agent assertion adjudication (prod harness steal)
type: brief
target: cemini-prod
created: 2026-07-29
tags: [k220, harness, claim-adjudication, optimistic-verification, agent-assertions]
source: arXiv:2607.25517 OVC
---

## Target

`cemini-prod:/opt/cemini/briefs/` — agent harness / claim-verification lane (not equity MAPPO; not blockchain deploy).

## Summary

**Steal:** bind an agent’s *claim* at commit time; accept optimistically unless challenged; on challenge run a **deterministic verifier** (typed tool / predicate), not another free-form LLM vote. OVC (arXiv:2607.25517) does this for manufacturing G-code bids — the pattern transfers to harness assertions (cost, schema conformance, “I fetched X”, numeric features).

## Steal for Cemini harness

1. **Separate claim from witness** — publish `f_claim` + commitment; keep expensive evidence private until dispute.
2. **Optimistic path is the default** — pay for full verification only when challenged (mirrors cheap accept / expensive audit).
3. **Predicate library beats general “is this true?”** — Access / Identity / Conformance / Feature-style typed checks; each has a clear fail mode.
4. **Execution-layer cost matters** — if verification is O(n) in artifact size, budget it; prefer chunked / incremental checks over one-shot megabyte proofs in the agent loop.
5. **Withhold outcome** — allow a party to abandon rather than disclose when forced open (privacy-preserving abort).

## Anti-steals

- Do **not** deploy Ethereum/Solidity manufacturing marketplace on prod.
- Do **not** tipdrop/David or poker-route this.
- Do **not** treat optimistic confidentiality as encryption against MATE/side-channels.

## Sources

- https://arxiv.org/abs/2607.25517
- `@3d-printing-wiki/sources/2026-corn-optimistic-verifiable-claims.md`
- `@3d-printing-wiki/briefs/2026-07-29_ovc-phase0.md`
- Related prior: K122 claim-drift (complementary — drift detection vs optimistic bind+challenge)
