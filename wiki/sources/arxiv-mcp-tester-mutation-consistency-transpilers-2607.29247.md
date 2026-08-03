---
title: "MCP-Tester — mutation consistency for transpiler testing"
type: source
tags: [source, arxiv, metamorphic-testing, transpiler, k235]
keywords: [2607.29247, MCP-Tester, mutation consistency, Zenodo, NOT Model Context Protocol]
related:
  - concepts/mutation-consistency-metamorphic-transpiler-testing.md
  - entities/tools/mcp-tester-transpiler.md
  - sources/brief-k234-k238-cyberneuro-mcp-tester-ham-accel-toktier-2026-08-03.md
  - briefs/2026-08-03_ccc-handoff-k234-k238-ingest.md
maturity: draft
created: 2026-08-03
updated: 2026-08-03
---

## Relations

- `@concepts/mutation-consistency-metamorphic-transpiler-testing.md`
- `@entities/tools/mcp-tester-transpiler.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Metamorphic Testing of Transpilers via Mutation Consistency of Programs |
| **Author** | (arXiv metadata) |
| **arXiv** | 2607.29247 |
| **Pages** | 11 |
| **Retrieved** | 2026-08-03 |
| **Code/Availability** | Tool named **MCP-Tester** (NOT Model Context Protocol) — Java, Zenodo https://doi.org/10.5281/zenodo.19340835 CC-BY-4.0. Local clone: `.local/adopts/mcp-tester-transpiler` (~3.3MB unzipped) — **GO** REFERENCE |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.29247-metamorphic-testing-of-transpilers-via-mutation.pdf` |

## Narrative

Metamorphic testing for **transpilers** when binaries cannot execute and differential testing is unavailable. Core property: **mutation consistency** — DSL mutations must induce predictable structural changes in transpiled source. Beats pure fuzzing at revealing faults in an industrial case study (partner transpiler confidential).

| Verdict | **ADOPT** mutation-consistency metamorphic relations for codegen/transpiler/agent-output structural testing. **GO** Zenodo REFERENCE clone |
