---
title: "KaliBench: A Fine-Grained Benchmark for Cybersecurity Tool Use on Kali Linux with Runtime-Free Verifiable Rewards (CCC K420)"
type: source
tags: [source, arxiv, k420]
keywords: [2610.02206, k420]
related:
  - concepts/schema-free-cli-tool-eval.md
  - briefs/2026-10-02_ccc-k416-k420-sip-ready.md
maturity: draft
read_status: deep-read
created: 2026-10-02
updated: 2026-10-02
---

## Relations

- `@concepts/schema-free-cli-tool-eval.md`
- `@briefs/2026-10-02_ccc-k416-k420-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | KaliBench: A Fine-Grained Benchmark for Cybersecurity Tool Use on Kali Linux with Runtime-Free Verifiable Rewards |
| **arXiv** | 2610.02206 (2026-10) |
| **Repo** | `RISys-Lab/KaliBench` |
| **Retrieved** | 2026-10-02 |

## Narrative

**Verdict: ADOPT method; cybersec-primary; NO-GO clone (no license).**

**KaliBench — tool use without schemas, graded down to the flag.** A benchmark for **natural-language → CLI** translation on Kali Linux: 8,504 query–command pairs across **1,642 tools**, 23 capability dimensions, 5 security phases. The framing is the contribution: existing tool-calling benchmarks assume **schema-defined tools** with JSON parameters, but real cybersecurity tooling is **schema-free CLI**, where enumerating hundreds of flag surfaces in a prompt is impractical — so the model must infer the tool *and* construct a syntactically valid command. Scoring is correspondingly fine-grained: **tool accuracy, optional-argument F1, positional-argument F1, exact-command match**, with **alias-aware** canonicalization so `-sT` and its long form compare equal. The finding is stark: **no evaluated open-weight model exceeds 42% exact-command accuracy** in the unrestricted setting, and **argument construction, not tool selection, is the bottleneck**. Adding tool hints lifts the ceiling sharply (up to ~84%), which locates the difficulty in recall of flag semantics rather than in choosing the tool. A second result for CCC: deterministic CLI structure enables **runtime-free verifiable rewards**, so SFT + RLVR lifts an 8B model to roughly 685B-MoE parity without executing commands. **CCC relevance:** the schema-free case is the honest description of most real tool surfaces — including MCP servers that wrap CLIs — and the measurement discipline (decompose tool vs. args, grade with alias awareness, reward without execution) is directly reusable. **Routing: cybersec-primary** — Kali tooling is the Cybersec wiki's domain; brief written there (`@cybersecurity-wiki/`), CCC keeps the tool-eval method. Pairs K402 MCP error surfaces / `@concepts/verifiable-deterministic-agent-benchmarking.md` / `@concepts/mcp-tool-interface-granularity-eval.md`. **Phase-0: `RISys-Lab/KaliBench` has no license file** (`SPDX=NONE`) → **no clone**. Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "CLIs are unforgiving: minor errors in argument order, flag spelling, alias misuse, or tool misinterpretation can invalidate execution." [Source: arXiv 2610.02206 (retrieved 2026-10-02)]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2610.02206-kalibench-a-fine-grained-benchmark-for-cybersecu.pdf` |
