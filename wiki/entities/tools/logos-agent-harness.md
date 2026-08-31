---
title: "Logos — cross-process agent harness (AAMAS 2027)"
type: entity
tags: [entity, tool, agent-harness, cross-process, plugins, append-only, no-spdx, k327]
keywords: [k327, Logos, plugin-as-process, append-only transcript, cold switching, ROS-like bus, wont_wire]
related:
  - sources/arxiv-logos-cross-process-agent-harness-2608.28553.md
  - concepts/cross-process-plugin-agent-harness.md
  - concepts/recoverable-agent-execution-checkpoints.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-08-31_ccc-k325-k327-sip-ready.md
maturity: draft
wire_status: wont_wire
created: 2026-08-31
updated: 2026-08-31
---

## Relations

- `@sources/arxiv-logos-cross-process-agent-harness-2608.28553.md`
- `@concepts/cross-process-plugin-agent-harness.md`
- `@concepts/recoverable-agent-execution-checkpoints.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-08-31_ccc-k325-k327-sip-ready.md`

## Raw Concept

What prompted this page: K327 (arXiv 2608.28553) — a ROS-like cross-process agent harness whose ADOPT value is architectural (plugin=process, append-only transcript), not a runtime to install.

## Narrative

**Verdict: ADOPT policy — `wont_wire` runtime.** No public SPDX found → no clone; Logos stays a design reference for CCC. Do not replace Cursor or `/route` with it.

Why it matters (pattern, not product):

- **Plugin = process** on a cross-process bus; router holds only the routing table; one fault ends at one node vs a single-process SPOF that kills every co-resident session.
- **Only shared state = append-only transcript** (JSONL, owned by no process); recovery = cold switching: rebuild the session from the transcript and continue.
- **80/80 sessions** resume with no repeated effect after kills at the four tool-call-cycle boundaries (during execution / after return before persistence / after persistence before announcement / after announcement).
- Measured: 0.215 ms median bus hop (1/823 of first-token latency); 3,500 calls / 200 concurrent callers with no loss or duplication; routing restores automatically after router kill; mixed-language (Go router, Python/Node.js peers) by construction.

CCC wires the principles into policy: isolate plugins; append-only durable state; do not re-execute a retained prefix. Pairs K282 AgentRewind recovery-boundary honesty and K239 execution-fidelity invariants.

| Wire | Target | Status |
|------|--------|--------|
| Logos runtime | none (no SPDX, no clone) | `wont_wire` |
| Cross-process + append-only principles | `.cursor/rules/ccc-k325-k327-phase1-wires.mdc` + shared policy §K327 | policy |
