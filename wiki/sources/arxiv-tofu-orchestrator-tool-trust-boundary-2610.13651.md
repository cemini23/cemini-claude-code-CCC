---
title: "ToFu: Exploiting and Fuzzing the LLM-Orchestrator-Tool Trust Boundary (CCC K446)"
type: source
tags: [source, arxiv, k446]
keywords: [2610.13651, k446]
related:
  - concepts/tool-metadata-as-security-contract.md
  - concepts/implicit-trust-mcp-input-channels.md
  - concepts/mcp-tool-metadata-supply-chain-risk.md
  - concepts/mcp-contract-grounded-synthesis-and-validation-gate.md
  - concepts/hybrid-static-dynamic-mcp-tool-security.md
  - concepts/schema-bound-mcp-tool-surface.md
  - briefs/2026-10-12_ccc-k445-k448-sip-ready.md
maturity: draft
read_status: deep-read
created: 2026-10-12
updated: 2026-10-12
---

## Relations

- `@concepts/tool-metadata-as-security-contract.md`
- `@concepts/implicit-trust-mcp-input-channels.md`
- `@concepts/mcp-tool-metadata-supply-chain-risk.md`
- `@concepts/mcp-contract-grounded-synthesis-and-validation-gate.md`
- `@concepts/hybrid-static-dynamic-mcp-tool-security.md`
- `@concepts/schema-bound-mcp-tool-surface.md`
- `@briefs/2026-10-12_ccc-k445-k448-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | ToFu: Exploiting and Fuzzing the LLM-Orchestrator-Tool Trust Boundary |
| **arXiv** | 2610.13651 (2026-10) |
| **Retrieved** | 2026-10-12 |

## Narrative

**Verdict: ADOPT pattern (MCP tool security).**

**A tool call is a structured model output the orchestrator executes — so schema-valid arguments are untrusted by default.** ToFu attacks the **LLM–orchestrator–tool trust boundary**. The **Repeat-After-Me** attack: an attacker writes text that names a tool and its arguments, tells the model to repeat it verbatim, and the orchestration layer parses the model's output as a tool call and dispatches it — reproduced on six orchestrators (LangGraph, MAF, ADK 2.0, AutoGen, Strands, CrewAI). **Schema conformity is not trust.** The paper's insight: the **metadata that guides an LLM to use a tool can also guide a fuzzer to test it**. ToFu derives tool-specific **semantic security checks** from the tool's own description plus a **CWE-guided sanitizer corpus**, generates schema-valid fuzzing harnesses and **semantic oracles** (runtime introspection for in-process tools; **outcome oracles** for opaque ones), and finds **253 verified bugs across 343 tools in 118 of 273 MCP servers** (reflected output 115, path traversal 64, log injection 58, SSRF 7, exfiltration 5, command injection 3). The LLM is confined to **sanitizer mapping and seed generation** — it is never the oracle. **CCC reading:** three rules to keep. (1) **Treat every schema-valid tool argument as adversarial** — the orchestrator establishes structural validity, not semantic safety; a sandbox is not optional (four servers modified the *fuzzing host*). (2) **Tool metadata should be an enforceable security contract**, validated in the tool, not delegated to the model or the orchestration layer. (3) **LLM selection buys bug *classes*; seeds buy *reach*** — with both LLM stages removed ToFu still kept two-thirds of its bugs, so the structural corpus is the load-bearing part. Pairs `implicit-trust-mcp-input-channels` / `mcp-tool-metadata-supply-chain-risk` / `mcp-contract-grounded-synthesis-and-validation-gate` / `hybrid-static-dynamic-mcp-tool-security`. **No repo URL** (cs.CR). Runtime `wont_wire`; concept `policy_wired`.

## Snippets

> "real-world LLM tools frequently fail to enforce the semantic contracts exposed by their interfaces." [Source: arXiv 2610.13651 (retrieved 2026-10-12)]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2610.13651-tofu-exploiting-and-fuzzing-the-llm-orchestrator.pdf` (local inbox **pending archive** — tailnet down 2026-10-12) |
