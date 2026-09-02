---
title: "Cross-process plugin agent harness — plugin=process, append-only transcript (CCC K327)"
type: concept
tags: [concept, agent-harness, cross-process, plugins, append-only, recovery, fault-isolation, k327]
keywords: [Logos, plugin-as-process, append-only transcript, cold switching, four tool-call boundaries, fault isolation, composability, 2608.28553]
related:
  - sources/arxiv-logos-cross-process-agent-harness-2608.28553.md
  - concepts/recoverable-agent-execution-checkpoints.md
  - concepts/execution-fidelity-irreversible-agent-invariants.md
  - entities/tools/logos-agent-harness.md
  - briefs/2026-08-31_ccc-k325-k327-sip-ready.md
  - concepts/harness-component-lifecycle-reasoning.md
  - sources/arxiv-cordisbench-component-lifecycle-2609.01600.md
maturity: draft
created: 2026-08-31
updated: 2026-09-02
---

## Relations

- `@sources/arxiv-logos-cross-process-agent-harness-2608.28553.md`
- `@concepts/recoverable-agent-execution-checkpoints.md`
- `@concepts/execution-fidelity-irreversible-agent-invariants.md`
- `@entities/tools/logos-agent-harness.md`
- `@briefs/2026-08-31_ccc-k325-k327-sip-ready.md`

## Raw Concept

The question: plugin-based agent composition (spatiotemporal-composability calculus) assumes one process = one failure domain. What does an agent harness look like when each plugin is its own process? Answer from K327 Logos [Source: wiki/sources/arxiv-logos-cross-process-agent-harness-2608.28553.md]: a ROS-like bus where the only shared state is an append-only transcript, and recovery rebuilds sessions from it without repeating effects.

## Narrative

The calculus's reversibility guarantee is complete within a single-process implementation — but one process is a **single point of failure** for everything it hosts: a crash, memory exhaustion, or a blocked event loop terminates every co-resident session; upgrading one plugin tears down every dependent.

**Logos pattern (ADOPT policy):**

1. **Plugin = process.** Each capability runs as a peer OS process on a cross-process bus; the router holds only its routing table. One fault ends at one node; a same-fault comparison shows the single-process reference interrupting every co-resident session. Router death narrows the failure domain to the routing-change window, and routing restores automatically.
2. **Only shared state = append-only transcript.** A JSONL file owned by no process records every session step as it happens. Nothing is removed from it. Recovery (**cold switching**) = a new process rebuilds the session from the transcript and continues.
3. **Resume without repeated effect at the four tool-call-cycle boundaries** — during tool execution; after return before persistence; after persistence before announcement; after announcement. 80/80 sessions resume with no repeated effect; the work redone after recovery equals exactly the work the transcript had not yet recorded.
4. **Mixed-language by construction** (Go router, Python + Node.js peers) — removes the single-language confinement of in-process frameworks.

Positioning: MCP moves tool *servers* out of the process but keeps composition + session state in the host; Temporal moves *execution* out but keeps assembly in the workflow definition; AutoGen/LangGraph keep everything in-process. Logos moves **composition and assembly themselves** out of the process.

**CCC policy lines:**

- **Isolate plugins as processes** for high-blast tool surfaces; a fault must end at one node, not the whole session (pairs `@concepts/recoverable-agent-execution-checkpoints.md`, K282).
- **Keep durable state in an append-only transcript** — never re-execute a retained prefix (pairs `@concepts/execution-fidelity-irreversible-agent-invariants.md`, K239: effects must not repeat).
- Kill boundaries: persist before announce, and define resumption at the four tool-call-cycle boundaries — that is where idempotency is decided.

Policy only: no public SPDX → no clone. Runtime `wont_wire` — Logos is a design reference, not a replacement for Cursor or `/route`.

| Confidence | `[CONFIRMED]` — measurements reported in the AAMAS 2027 paper; policy is CCC synthesis |
|------------|------------|
