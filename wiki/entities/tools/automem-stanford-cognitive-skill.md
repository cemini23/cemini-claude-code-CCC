---
title: autoLearnMem/AutoMem — Stanford metamemory training framework
type: entity
tags: [entity, tool, memory, research, k137]
keywords: [2607.01224, autolearnmem, balrog, crafter, nethack]
related:
  - sources/arxiv-automem-metamemory-cognitive-skill-2607.01224.md
  - concepts/metamemory-scaffold-proficiency-training.md
  - concepts/agentic-memory-cross-scenario-generality.md
  - sources/brief-k137-automem-metamemory-cognitive-skill-2026-07-02.md
maturity: draft
created: 2026-07-02
updated: 2026-07-02
---

## Relations

- `@sources/arxiv-automem-metamemory-cognitive-skill-2607.01224.md` — paper provenance
- `@concepts/metamemory-scaffold-proficiency-training.md` — synthesis

## Raw Concept

Reference implementation for arXiv 2607.01224 — BALROG-based long-horizon game agents with file-system memory and two meta-LLM outer loops.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | https://github.com/autoLearnMem/AutoMem |
| **Project site** | https://autolearnmem.github.io/ |
| **License** | **None** (no LICENSE file) [CONFIRMED gh api 2026-07-02] |
| **Stars** | 0 (new release) |
| **Last push** | 2026-07-02 |
| **Verdict** | **REFERENCE** — study scaffold/proficiency loops; **NO-GO** prod install until SPDX license |

### Not the same as verygoodplugins/automem

| | Stanford AutoMem | verygoodplugins/automem |
|--|------------------|-------------------------|
| arXiv | 2607.01224 | — |
| Purpose | Research: train memory skill on games | Production MCP memory service |
| License | None | MIT |
| Stack | BALROG + vLLM + LoRA memory specialist | FalkorDB + Qdrant + Flask API |

Do **not** conflate in Phase-0 audits or MCP wiring.

## Dead Ends

- **2026-07-02 Phase-0:** `gh api` reports `license: null` on autoLearnMem/AutoMem — NO-GO adopt until LICENSE appears.
