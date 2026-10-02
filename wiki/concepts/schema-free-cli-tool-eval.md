---
title: "KaliBench: A Fine-Grained Benchmark for Cybersecurity Tool Use on Kali Linux with Runtime-Free Verifiable Rewards (CCC K420)"
type: concept
tags: [concept, k420]
keywords: [2610.02206, k420]
related:
  - sources/arxiv-kalibench-schema-free-cli-tool-eval-2610.02206.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-10-02_ccc-k416-k420-sip-ready.md
  - concepts/mcp-tool-interface-granularity-eval.md
  - concepts/verifiable-deterministic-agent-benchmarking.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-10-02
updated: 2026-10-02
---

## Relations

- `@sources/arxiv-kalibench-schema-free-cli-tool-eval-2610.02206.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-10-02_ccc-k416-k420-sip-ready.md`

## Raw Concept

K420: ADOPT method; cybersec-primary; NO-GO clone (no license) — arXiv 2610.02206.

## Narrative

**KaliBench — tool use without schemas, graded down to the flag.** A benchmark for **natural-language → CLI** translation on Kali Linux: 8,504 query–command pairs across **1,642 tools**, 23 capability dimensions, 5 security phases. The framing is the contribution: existing tool-calling benchmarks assume **schema-defined tools** with JSON parameters, but real cybersecurity tooling is **schema-free CLI**, where enumerating hundreds of flag surfaces in a prompt is impractical — so the model must infer the tool *and* construct a syntactically valid command. Scoring is correspondingly fine-grained: **tool accuracy, optional-argument F1, positional-argument F1, exact-command match**, with **alias-aware** canonicalization so `-sT` and its long form compare equal. The finding is stark: **no evaluated open-weight model exceeds 42% exact-command accuracy** in the unrestricted setting, and **argument construction, not tool selection, is the bottleneck**. Adding tool hints lifts the ceiling sharply (up to ~84%), which locates the difficulty in recall of flag semantics rather than in choosing the tool. A second result for CCC: deterministic CLI structure enables **runtime-free verifiable rewards**, so SFT + RLVR lifts an 8B model to roughly 685B-MoE parity without executing commands. **CCC relevance:** the schema-free case is the honest description of most real tool surfaces — including MCP servers that wrap CLIs — and the measurement discipline (decompose tool vs. args, grade with alias awareness, reward without execution) is directly reusable. **Routing: cybersec-primary** — Kali tooling is the Cybersec wiki's domain; brief staged in their `briefs/`, CCC keeps the tool-eval method. Pairs K402 MCP error surfaces / `@concepts/verifiable-deterministic-agent-benchmarking.md` / `@concepts/mcp-tool-interface-granularity-eval.md`. **Phase-0: `RISys-Lab/KaliBench` has no license file** (`SPDX=NONE`) → **no clone**. Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "See source page for arXiv 2610.02206 locators." [Source: CCC K420 synthesis]

## Cross-wiki

**Cybersec-primary.** A brief is staged at `@cybersecurity-wiki/briefs/2026-10-02_k420-kalibench-schema-free-cli-eval.md`. CCC cannot link the page yet: the Cybersec-side concept does not exist (checked 2026-10-02), and a cross-wiki edge to a missing file fails wiki lint. Once their session creates it, link it here.
