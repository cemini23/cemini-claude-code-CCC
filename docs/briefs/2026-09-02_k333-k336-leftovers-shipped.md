# K333–K336 leftovers shipped (CCC docs)

Date: 2026-09-02

## Shipped (operator-invoked federation skills)

| Skill | Helper | K |
|-------|--------|---|
| `untrusted-delegation-precheck` | `delegation_broker_precheck.py` | K333 |
| `harness-eval-gate` | `harness_eval_checklist.py` | K334 |
| `agent-queue-labels` | `agent_queue_labels.py` | Osmani k244 |
| `external-reference-monitor` v1.1 | pairs K333 + K326 | K326/K333 |

## Scripts

- `spdx_watch_harness_wave.sh` — CordisBench / HarnessDev / InstructionArbitrationBench / DelegationWithoutTrust GitHub SPDX re-hunt (report only)
- All helpers include `selftest`; wired into `adopt_k333` / `adopt_k334` phase0

## Cross-wiki

- Cybersec: `../Cybersecurity wiki/briefs/2026-09-02_k333-untrusted-model-delegation-steal-from-ccc.md`
- Atto: `../atto/briefs/2026-09-02_k333-untrusted-delegation-steal-from-ccc.md`

## Still propose-only (HITL / blocked)

- **HoH runtime wrap** — REFERENCE only; do not replace Cursor/`/route`
- **Dense+RRF SCOUT** over live MCP catalog
- **CordisBench / HarnessDev clones** — SPDX watch until repos publish
- **2608.30083 ZK agent proofs** — Cybersec-primary, cap-skipped
- **VotalAI / authorization broker product** — no install without ticket
