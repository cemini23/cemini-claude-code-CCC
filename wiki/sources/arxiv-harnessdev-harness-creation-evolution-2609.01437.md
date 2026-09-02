---
title: "HarnessDev — can LLMs create and evolve their own harness? (CCC K334)"
type: source
tags: [source, arxiv, harness-evolution, harness-creation, eval-first, self-evolving-harness, policy, k334]
keywords: [2609.01437, HarnessDev, harness creation, harness evolution, eval artifact, held-out transfer, state never fires, self-developing-agents]
related:
  - concepts/harness-as-eval-artifact.md
  - concepts/meta-harness-optimization-hitl-eval-contract.md
  - concepts/stratified-harness-evolution.md
  - concepts/vague-goal-self-evolution.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - briefs/2026-09-02_ccc-k333-k336-sip-ready.md
maturity: draft
read_status: read
created: 2026-09-02
updated: 2026-09-02
---

## Relations

- `@concepts/harness-as-eval-artifact.md`
- `@concepts/meta-harness-optimization-hitl-eval-contract.md`
- `@concepts/stratified-harness-evolution.md`
- `@concepts/vague-goal-self-evolution.md`
- `@concepts/bounded-self-refinement-vs-rsi-taxonomy.md`
- `@briefs/2026-09-02_ccc-k333-k336-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | HarnessDev: Can LLMs Create and Evolve Their Own Agent Harness? |
| **arXiv** | 2609.01437 (cs.CL, 2026-09-02) |
| **Authors** | Self-developing-agents research group (see paper) |
| **Venue** | arXiv preprint |
| **Code** | Project page (`self-developing-agents.github.io`) — **no public benchmark repo / no SPDX** → no clone |
| **Retrieved** | 2026-09-02 |

## Narrative

**Verdict: ADOPT eval-first — evaluate the runnable harness, not only task output.**

HarnessDev is a benchmark with two stages:

1. **Creation** — given a task specification, the agent must produce a **runnable harness** (orchestration, tools, memory/state hooks) that can execute the task class.
2. **Evolution** — given feedback on harness behavior, the agent iterates the harness infrastructure itself.

The unit of evaluation shifts from **final answer quality** to **harness infrastructure quality**: does the generated loop run, compose tools correctly, and improve under evolution pressure?

**Findings (the steals):**

- **Creation lags human references** on code and search task families — LLMs can scaffold harnesses but miss integration details human engineers embed by default.
- **Evolution gains are unstable** — visible feedback loops show improvement that **partially fails held-out transfer**; gains are **model-dependent** and can vanish when the executor model swaps.
- **State/memory components often never fire** — harness code defines state variables and memory hooks that **never trigger at runtime**; the harness "exists" in source but not in behavior. **Integration verify is mandatory** — do not trust harness self-report or static structure alone.
- **Creation ≠ Evolution** — distinct skills; an agent strong at one stage may not retain gains on the other.

CCC policy lines: **evaluate harness infrastructure, not only answers**; treat visible feedback ≠ held-out transfer; require execution/integration checks before trusting evolved harness state (pairs K281 meta-harness optimization, K292 retention on held-out packs, K313 stratified hidden selection, K332 vague-goal proxy failure). **Never auto-evolve `.cursor/skills`.** No public SPDX → no clone; runtime `wont_wire`.

| Confidence | `[CONFIRMED]` — benchmark design and results from the paper; policy is CCC synthesis |
|------------|------------|

## Snippets

> "The evaluation unit is the runnable harness — orchestration, tool wiring, and state hooks — not the terminal task output alone." [Source: arXiv 2609.01437 — HarnessDev design thesis]

> "Evolution gains on visible feedback do not reliably transfer to held-out evaluation; executor swap can negate improvements." [Source: arXiv 2609.01437 — evolution stability finding]

> "State and memory components defined in harness code often never fire at runtime — integration verification is required." [Source: arXiv 2609.01437 — integration gap finding]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2609.01437-harnessdev-can-llms-create-and-evolve-their-own.pdf` |
|--------------|------------------------------------------------------------------------|
