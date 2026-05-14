---
title: "optillm — OpenAI-API-compatible LLM proxy with Z3 theorem prover + MCP support"
type: entity
category: tool
tags: [entity, tool, llm-proxy, litellm, mcp-host, z3-theorem-prover, spacy-offline, lora-adapter, k44, adopt-doc-level-pending-phase-0]
keywords: [optillm, litellm-gateway, openai-api-compatible, z3-solver, mcp-server-host, hf-lora-adapter, apache-2-license, multi-provider-routing]
related: []
maturity: adopt-doc-level-pending-phase-0
created: 2026-05-14
updated: 2026-05-14
cross-wiki-source: "@osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md"
---

## Relations

- @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md — K44 source (doc-level verdict)

## Raw Concept

A Python+Flask OpenAI-API-compatible proxy that gateways multiple LLM providers via LiteLLM, with native MCP server support and **Z3 theorem-prover integration for symbolic reasoning**. Apache-2.0, claimed 3,800 stars. K44 verdict: **Adopt**. Primary fit: CCC. Cross-route: OSINT (bridging disparate threat-intelligence models).

## Narrative

Three architectural features make this CCC-relevant:

1. **Multi-provider routing via LiteLLM** — single OpenAI-API surface backed by Claude, GPT, Gemini, local Ollama, HF LoRA adapters
2. **MCP server hosting** — external MCP tools callable from inside an inference call
3. **Z3 theorem prover** — when the LLM needs to verify a logical chain, the request can be routed through Z3 rather than relying on chain-of-thought

**Offline Docker variant** with pre-downloaded spaCy models is the lever for local-first deployment.

**Phase-0 gates**:
- G1: Star + maturity verification (`gh api repos/algorithmicsuperintelligence/optillm`)
- G2: License (Apache-2.0 confirmed)
- G3: Z3 integration smoke test — submit a logic puzzle and verify Z3 actually fires
- G4: `os.environ` integration points (K44 NEEDS VERIFICATION) for centralized vault credentials
- G5: HF LoRA-adapter loading round-trip on a local model

**Cross-route to OSINT**: the LiteLLM gateway + multi-provider routing is the missing piece for an "ask multiple frontier models the same threat-intel question and reconcile" workflow.

## Snippets

> "OptiLLM functions as an OpenAI API-compatible proxy utilizing LiteLLM to gateway multiple LLM providers, notably supporting complex inference tasks via the Z3 theorem prover for rigid logical reasoning."
[Source: @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md ¶169]
