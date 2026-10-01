---
title: Replay Agent Recorder — local-first time-travel debugging for LLM agents
type: entity
tags: [tool, agent-debugging, replay, trace, mit, reference, k349]
keywords: [replay-agent-recorder, Futuresis, time-travel debugging, deterministic replay, fork from LLM call, trace graph, MIT]
related:
  - concepts/recoverable-agent-execution-checkpoints.md
  - concepts/agent-trace-tampering-audit-gap.md
wire_status: wont_wire
wire_target: ".local/adopts/replay-agent-recorder (REFERENCE clone)"
maturity: draft
created: 2026-10-01
updated: 2026-10-01
---

## Relations

- `@concepts/recoverable-agent-execution-checkpoints.md` — the concept that adopted its checkpoint/rewind model
- `@concepts/agent-trace-tampering-audit-gap.md` — same trace-record family, different purpose (this one is for debugging, not for audit integrity)

## Raw Concept

- **Repo:** `Futuresis/replay-agent-recorder`
- **Clone:** `.local/adopts/replay-agent-recorder` (REFERENCE shelf)
- **License:** MIT
- **Status:** Alpha (self-described)
- **Language:** Python 3.12+
- **Size:** ~3.7 MB

## Narrative

**Local-first time-travel debugging for LLM agents.** It records real agent runs, replays them
deterministically, lets you **fork from any LLM call**, and renders the model / tool / file trace as an
interactive graph.

**Why CCC cares — the checkpoint-and-rewind model, not the tool.** The transferable idea is that an
agent run becomes a **replayable artifact**: deterministic replay plus fork-from-any-step turns
"it failed once, I cannot reproduce it" into "branch here and try again". That is the same shape as
`@concepts/recoverable-agent-execution-checkpoints.md` and is adjacent to the trace-integrity cluster
(K394 agent trace tampering, K403 Tracekit, K406 Assay) — though those ask *whether a trace can be
trusted*, while this asks *how to walk back through one*.

**Verdict: REFERENCE, runtime `wont_wire`.** Self-described Alpha, Python-3.12-pinned, and not on the
CCC runtime path. Kept on the `.local/adopts/` shelf for the checkpoint/rewind pattern. No CCC hook,
policy, or MCP wire derives from it.

## Snippets

> "Record real agent runs, replay them deterministically, fork from any LLM call, and inspect the
> full model/tool/file trace as an interactive graph." [Source: `Futuresis/replay-agent-recorder`
> README (retrieved 2026-10-01)]

## Dead Ends

- **Not an audit tool.** Deterministic replay is for a developer re-running a trace, not for proving
  a trace was not altered. Do not cite it as a tamper-evidence mechanism — see
  `@concepts/agent-trace-tampering-audit-gap.md`.
