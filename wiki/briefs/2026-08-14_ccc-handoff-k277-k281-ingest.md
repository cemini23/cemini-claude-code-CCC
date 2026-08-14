---
title: CCC handoff — K277–K281 trust + verification wave
type: brief
tags: [brief, handoff, k277, k278, k279, k280, k281]
related:
  - sources/brief-k277-k281-trust-verification-wave-2026-08-14.md
  - briefs/2026-08-14_ccc-k277-k281-sip-ready.md
  - concepts/measurement-integrity-mcp-security-eval.md
  - concepts/intersage-trust-native-ioa-protocol.md
  - concepts/marc-clinical-multi-agent-coordination.md
  - concepts/repo-level-verified-code-proof-eval.md
  - concepts/meta-harness-optimization-hitl-eval-contract.md
  - entities/patterns/treatment-blind-endpoint-integrity.md
  - entities/tools/intersage.md
  - entities/tools/marc-v1.md
  - entities/tools/vero.md
  - entities/tools/autodesign.md
  - sources/arxiv-labels-not-endpoints-treatment-leakage-2608.12880.md
  - sources/arxiv-intersage-trust-native-ioa-protocol-2608.13030.md
  - sources/arxiv-marc-v1-clinical-multi-agent-2608.13476.md
  - sources/arxiv-vero-repo-verified-code-proof-2608.13522.md
  - sources/arxiv-autodesign-meta-harness-2608.13560.md
  - concepts/phase1-adopt-wire.md
created: 2026-08-14
updated: 2026-08-14
---

## Summary

Five-paper batch (K277–K281): K277 treatment-leakage measurement audit → **ADOPT** Integrity Chain (labels ≠ endpoints); K278 InterSAGE IoA trust protocol → **ADOPT** AIC 4-D identity + DID-bound capability VCs (Atto-priority, policy only); K279 MARC-v1 → **GO REFERENCE** MIT clone; K280 Vero → **GO REFERENCE** Apache-2.0 clone; K281 AutoDesign → steal meta-harness **with HITL/external eval contract** (pairs K162), MIT clone if <500MB. Dual-ID note: Cybersec **K277 = RSM**; this batch's K277 = Labels-Are-Not-Endpoints.

## Local

- `.local/adopts/MARC-v1` (MIT ~30MB) — GO REFERENCE
- `.local/adopts/vero` (Apache-2.0 ~2MB) — GO REFERENCE
- `.local/adopts/AutoDesign` (MIT on disk; ~43MB) — GO REFERENCE
- InterSAGE: **no public SPDX clone** → policy only

## Routing

- Prod + hands-on (`briefs/2026-08-14_k277-k281-*` + `docs/briefs/2026-08-14_k277-k281-*`)
- **Atto** (priority): InterSAGE — AIC identity / capability-bound discovery / audit trails for extract solvers
- Cybersec: K277 treatment-leakage + InterSAGE identity (TipDrop kit retired)
- GuruWatcher: identity/persona vs service callers
- Poker: light — eval integrity, not EV
