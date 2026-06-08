---
title: Time-series-native agent harness — modality workspace pattern (TimeClaw)
type: concept
tags: [concept, harness, time-series, mcp, etclovg]
keywords: [timeclaw, 2606.05404, datatype-misalignment, workspace, capability-evolution, episodic-memory]
related:
  - sources/arxiv-timeclaw-contextualized-time-series-2606.05404.md
  - entities/tools/timeclaw.md
  - concepts/code-as-agent-harness.md
  - concepts/mcp-context-optimization.md
  - concepts/runtime-context-mcp-file-refs.md
  - concepts/muse-autoskill-skill-lifecycle.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/etclovg-harness-layers.md
  - entities/tools/claude-mem.md
  - entities/mcp-servers/stash.md
  - "@osint-wiki/concepts/contextualized-time-series-agent-harness.md"
maturity: draft
created: 2026-06-08
updated: 2026-06-08
---

## Relations

- `@sources/arxiv-timeclaw-contextualized-time-series-2606.05404.md` — arXiv 2606.05404 provenance
- `@entities/tools/timeclaw.md` — reference repo (CONDITIONAL-GO)
- `@concepts/code-as-agent-harness.md` — general harness layering
- `@concepts/mcp-context-optimization.md` — MCP as modality interface
- `@concepts/runtime-context-mcp-file-refs.md` — ground truth via tools not guessing
- `@concepts/muse-autoskill-skill-lifecycle.md` — capability evolution peer
- `@concepts/etclovg-harness-layers.md` — Tool Interface + Verification mapping

## Raw Concept

arXiv **2606.05404** (TimeClaw, UIUC): generalist LLM agents fail on **contextualized time series** when data is tokenized as text. Fix: a **modality-native harness** — server-side workspace, runtime tools, evolving toolbox, episodic multimodal memory.

## Narrative

### Two misalignments [CONFIRMED paper claim]

| Misalignment | Symptom | Harness fix |
|--------------|---------|-------------|
| **Datatype** | Serialized numbers lose proximity, resolution, long-range structure | Keep series in workspace `W` at full precision; tools return compact observations |
| **Agentic process** | Slice/aggregate/decompose become language reasoning | Runtime-native temporal ops + auditable trajectories |

### ETCLOVG mapping [TENTATIVE CCC mapping]

| TimeClaw component | ETCLOVG layer |
|--------------------|---------------|
| MCP workspace + temporal tools | **Tool Interface** |
| Capability evolution operator `E` | **Execution** + **Governance** (admit new tools after verification) |
| Episodic multimodal memory | **Context** + **Observability** |
| Solution verifier / grounded claims | **Verification** |

### Cemini steal-from (no TimeClaw install required) [TENTATIVE]

| Pattern | CCC analogue |
|---------|--------------|
| Task-local workspace via MCP | `@entities/tools/lazy-tool.md` + domain MCP holds heavy state; agent passes op + params only |
| Auditable trajectories | `@concepts/failed-trajectory-harness-repair.md`, OpenSpec acceptance criteria |
| Evolving toolbox | `@concepts/muse-autoskill-skill-lifecycle.md`, `@concepts/skilladaptor-step-level-skill-adaptation.md` |
| Episodic retrieval | `@entities/tools/claude-mem.md`, `@entities/mcp-servers/stash.md` |

**Finance benchmarks** (TSAIA, CiK finance slices) → `@osint-wiki/concepts/contextualized-time-series-agent-harness.md`.

**Name collision:** arXiv **2605.10038** is a different "TimeClaw" (exploratory execution learning) — do not merge pages.

## Snippets

> "How to build time-series-native agent harness?" — central RQ of 2606.05404. [Source: arxiv-timeclaw-contextualized-time-series-2606.05404.md]
