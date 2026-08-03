---
title: Mutation-consistency metamorphic transpiler testing
type: concept
tags: [concept, testing, metamorphic, transpiler, codegen, k235]
keywords: [2607.29247, MCP-Tester, mutation consistency, structural testing]
related:
  - sources/arxiv-mcp-tester-mutation-consistency-transpilers-2607.29247.md
  - entities/tools/mcp-tester-transpiler.md
  - sources/brief-k234-k238-cyberneuro-mcp-tester-ham-accel-toktier-2026-08-03.md
  - briefs/2026-08-03_ccc-handoff-k234-k238-ingest.md
maturity: draft
created: 2026-08-03
updated: 2026-08-03
---

## Relations

- `@sources/arxiv-mcp-tester-mutation-consistency-transpilers-2607.29247.md` — K235 MCP-Tester paper
- `@entities/tools/mcp-tester-transpiler.md` — Zenodo REFERENCE clone

## Raw Concept

How do we test transpilers (or codegen pipelines) when binaries cannot run and differential testing is unavailable?

## Narrative

K235 (arXiv **2607.29247**) introduces **mutation consistency**: DSL mutations must induce predictable structural changes in transpiled output. The tool **MCP-Tester** (Java, Zenodo CC-BY-4.0 — **not** Model Context Protocol) generates metamorphic relations and beats pure fuzzing on an industrial transpiler case study.

### Cemini steal (ADOPT)

Apply mutation-consistency relations to:

- Codegen / transpiler pipelines (TipDrop, harness skill emitters)
- Agent-output structural testing when execution is blocked
- Schema-bound MCP tool output validation (pairs K198)

Local REFERENCE: `.local/adopts/mcp-tester-transpiler` (~3.3MB). Phase-1: policy wire in `cemini-phase1-policy-wires.mdc`.

| Verdict | **ADOPT** metamorphic relations. **GO** Zenodo REFERENCE clone |

## Snippets

> Property: mutation consistency — DSL mutations must induce predictable structural changes in transpiled source.
> — [Source: arxiv-2607.29247, retrieved 2026-08-03]
