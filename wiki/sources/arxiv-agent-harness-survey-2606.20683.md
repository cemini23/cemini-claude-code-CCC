---
title: Agent system and harness design survey (arXiv 2606.20683)
type: source
tags: [source, arxiv, survey, harness-engineering, k124]
keywords: [2606.20683, model-harness, six-responsibilities, awesome-agent-engineering]
related:
  - concepts/model-harness-six-responsibilities.md
  - concepts/code-as-agent-harness.md
  - concepts/etclovg-harness-layers.md
  - concepts/agent-harness-operational-definition.md
  - entities/tools/awesome-agent-engineering.md
  - entities/tools/claude-code.md
maturity: draft
read_status: read
created: 2026-06-24
updated: 2026-06-24
---

## Relations

- `@concepts/model-harness-six-responsibilities.md` — six runtime responsibilities synthesis
- `@concepts/etclovg-harness-layers.md` — finer-grained CCC taxonomy mapped from survey
- `@entities/tools/awesome-agent-engineering.md` — companion curated paper list (MIT)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | From Question Answering to Task Completion: A Survey on Agent System and Harness Design |
| **Authors** | Guo et al. (CityU HK, Sydney, PKU, TokenRhythm) |
| **arXiv** | 2606.20683v1 [cs.AI] |
| **Companion** | https://github.com/ggjy/Awesome-Agent-Engineering (MIT) |
| **Location** | `raw-sources/arxiv-2606.20683-pdf-a-survey-on-agent-system-and-harness-design.pdf` |
| **Retrieved** | 2026-06-24 |
| **Read status** | read (intro + six-responsibility decomposition) |

## Narrative

Model–harness survey arguing agent quality emerges from **foundation model + execution harness coupling**, not model capability alone. Traces four agent-engineering paradigms (prompt → workflow → context/harness engineering → agent-native training + co-evolution).

**Six coupled runtime responsibilities** of the execution harness: observation, context, control, action, state, verification/governance. Maps task properties and domain pressures to harness configurations; reviews benchmarks and model–harness co-evolution evidence.

**CCC relevance:** vocabulary bridge between coarse three-layer harness model (`@concepts/code-as-agent-harness.md`) and ETCLOVG seven-layer taxonomy. Explicitly cites Claude Code, OpenHands, OpenClaw as exemplars. **REFERENCE** — steal evaluation framing and responsibility checklist; no install.

## Snippets

> "Rather than treating agents as models with auxiliary tools, this survey argues that agent quality—including success, efficiency, safety, and generalization—emerges from the interaction between model capability, runtime infrastructure, task structure, and evaluation design."
> — [Source: arxiv-2606.20683-pdf-a-survey-on-agent-system-and-harness-design.pdf, retrieved 2026-06-24]

> "We decompose the execution harness into six coupled runtime responsibilities: observation, context, control, action, state, and verification/governance."
> — [Source: arxiv-2606.20683-pdf-a-survey-on-agent-system-and-harness-design.pdf abstract, retrieved 2026-06-24]
