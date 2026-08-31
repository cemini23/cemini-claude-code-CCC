---
title: "Logos: An Agent Harness on a Cross-Process Bus (CCC K327)"
type: source
tags: [source, arxiv, agent-harness, cross-process, plugins, append-only, recovery, k327]
keywords: [2608.28553, Logos, ROS-like, plugin-as-process, append-only transcript, cold switching, fault isolation, composability]
related:
  - concepts/cross-process-plugin-agent-harness.md
  - concepts/recoverable-agent-execution-checkpoints.md
  - concepts/execution-fidelity-irreversible-agent-invariants.md
  - entities/tools/logos-agent-harness.md
  - briefs/2026-08-31_ccc-k325-k327-sip-ready.md
maturity: draft
read_status: skimmed
created: 2026-08-31
updated: 2026-08-31
---

## Relations

- `@concepts/cross-process-plugin-agent-harness.md`
- `@concepts/recoverable-agent-execution-checkpoints.md`
- `@concepts/execution-fidelity-irreversible-agent-invariants.md`
- `@entities/tools/logos-agent-harness.md`
- `@briefs/2026-08-31_ccc-k325-k327-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Logos: An Agent Harness on a Cross-Process Bus |
| **arXiv** | 2608.28553 (cs.AI, 2026-08-28) |
| **Authors** | Hanzhang Jia, Liheng Zeng, Hao Cheng, Yi Gao, Bo Ma (University of Sussex / Zhejiang Gongshang University / Shanghai Shuyuan) |
| **Venue** | AAMAS 2027 (research track), 10 pages |
| **Code** | No public repo found — Phase-0 SPDX hunt: no hit → **policy only, no clone** |
| **Retrieved** | 2026-08-31 |

## Narrative

**Verdict: ADOPT policy — plugin = process; only shared state = append-only transcript.** Logos builds on the spatiotemporal-composability calculus (plugin assembly with tracked inverses) but moves composition out of the single hosting process. Four lemmas (orchestration externality, carrier substitution, recovery localization, external resolution) show the calculus's reversibility guarantee survives the process boundary: a stateless LLM keeps all cross-step state outside the model, so the carrier (any persistent store) and the recovery discipline can be externalized without new hypotheses.

Architecture:

- **Plugin = process** on a ROS-like cross-process bus. A Go router holds only its routing table; harnesses and tools run as peer processes (Python, Node.js — mixed-language by construction). The router is a single process whose death narrows the failure domain to the routing-change window, with routing restoring automatically after router kill.
- **Only shared state = an append-only transcript** (a JSONL file owned by no process). Every session step is recorded as it happens; after any process dies, a new process rebuilds the session from the transcript and continues — **cold switching**.
- **Resume without repeated effect.** 12 end-to-end sessions resume through 6 process kills with no previously-executed action repeated; 80 further sessions cover kills at the **four boundaries of the tool-call cycle** (during tool execution; after return before persistence; after persistence before announcement; after announcement) — all resume and complete, and the work redone after recovery equals exactly the work the transcript had not yet recorded.
- **Fault isolation:** same-fault comparison — one fault interrupts every co-resident session in the single-process reference, while under the peer-process construction one fault ends at one node.
- **Measured:** bus hop median 0.215 ms (1/823 of a 177 ms first-token latency); 3,500 calls from up to 200 concurrent callers with no loss/duplication/misattribution; one registration wins among 100 simultaneous claims with 99 explicit denials; supply-change sequences identical across 30 churn rounds; a tool comes online mid-task with first autonomous call 8.4 s after registry broadcast.

CCC adoption: isolate plugins; keep durable state in an append-only transcript; do not re-execute a retained prefix (pairs K282 AgentRewind recovery-boundary honesty and K239 execution-fidelity invariants). **Policy only** — no public SPDX → no clone. Runtime `wont_wire`: this is a design reference, not a replacement for Cursor or `/route`.

| Confidence | `[CONFIRMED]` — measurements reported in the AAMAS 2027 paper; not reproduced in CCC |
|------------|------------|

## Snippets

> "In Logos a plugin is a process, the router holds only its routing table, and all shared state lives in an append-only transcript owned by no process." [Source: arXiv 2608.28553 abstract / §1]

> "Eighty sessions resume with no repeated effect after kills placed at the four boundaries of the tool-call cycle … the work redone after recovery equals exactly the work the transcript had not yet recorded." [Source: arXiv 2608.28553 §1]

> "A same-fault comparison with a single-process reference configuration shows one fault interrupting every co-resident session while under the peer-process construction one fault ends at one node." [Source: arXiv 2608.28553 abstract]

> "The median cost of a bus hop is 0.215 ms, 1/823 of the model's 177 ms first-token latency, invisible at the model's time scale." [Source: arXiv 2608.28553 §1]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.28553-logos-an-agent-harness-on-a-cross-process-bus.pdf` |
|--------------|-------------------------------------------------------------------------------------------------------------------|
