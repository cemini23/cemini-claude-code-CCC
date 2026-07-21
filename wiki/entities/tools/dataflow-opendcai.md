---
title: OpenDCAI DataFlow — Apache data-pipeline platform (NL2Pipeline peer)
type: entity
tags: [tool, data-pipeline, apache, mcp, k197]
keywords: [OpenDCAI/DataFlow, DataFlow-Harness, DAG, Apache-2.0]
related:
  - sources/arxiv-dataflow-harness-nl2pipeline-2607.16617.md
  - concepts/nl2pipeline-platform-grounded-mutations.md
  - concepts/code-as-agent-harness.md
maturity: draft
created: 2026-07-21
updated: 2026-07-21
---

## Relations

- `@sources/arxiv-dataflow-harness-nl2pipeline-2607.16617.md` — paper
- `@concepts/nl2pipeline-platform-grounded-mutations.md` — pattern
- `@concepts/code-as-agent-harness.md` — harness peer

## Raw Concept

`github.com/OpenDCAI/DataFlow` — Apache-2.0 (~6.7k★). Local clone `.local/adopts/DataFlow` (~11MB). Paper's DataFlow-WebUI has **no SPDX** — do not adopt WebUI.

## Narrative

### Phase-0

| Check | Result |
|-------|--------|
| DataFlow license | **Apache-2.0** [CONFIRMED] |
| DataFlow-WebUI | **NOASSERTION** — **NO-GO** |
| Size | ~11MB — OK |

### Verdict

**CONDITIONAL-GO (REFERENCE)** — study operator registry / DAG mutation patterns. Not a default TipDrop/prod dependency.
