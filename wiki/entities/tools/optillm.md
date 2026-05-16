---
title: "optillm — OpenAI-API-compatible LLM proxy with Z3 theorem prover + MCP support"
type: entity
category: tool
tags: [entity, tool, llm-proxy, litellm, mcp-client, z3-theorem-prover, spacy-offline, lora-adapter, k44, go-phase-0-2026-05-14]
keywords: [optillm, litellm-gateway, openai-api-compatible, z3-solver-real, mcp-client-not-host, hf-lora-adapter, apache-2-license, multi-provider-routing, codelion-asankhaya-sharma, cerebras-contributors]
related:
  - concepts/mcp-context-optimization.md
maturity: validated
created: 2026-05-14
updated: 2026-05-15
cross-wiki-source: "@osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md"
---

## Relations

- @concepts/mcp-context-optimization.md — multi-provider LLM proxy + MCP client; a routing-layer option adjacent to the four-layer stack
- @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md — K44 source (doc-level verdict)

## Raw Concept

A Python+Flask OpenAI-API-compatible proxy that gateways multiple LLM providers via LiteLLM, with native MCP server support and **Z3 theorem-prover integration for symbolic reasoning**. Apache-2.0, claimed 3,800 stars. K44 verdict: **Adopt**. Primary fit: CCC. Cross-route: OSINT (bridging disparate threat-intelligence models).

## Narrative

Three architectural features make this CCC-relevant:

1. **Multi-provider routing via LiteLLM** — single OpenAI-API surface backed by Claude, GPT, Gemini, local Ollama, HF LoRA adapters
2. **MCP server hosting** — external MCP tools callable from inside an inference call
3. **Z3 theorem prover** — when the LLM needs to verify a logical chain, the request can be routed through Z3 rather than relying on chain-of-thought

**Offline Docker variant** with pre-downloaded spaCy models is the lever for local-first deployment.

**Phase-0 audit verdict (2026-05-14): GO** with Cemini-specific caveats. Production-ready CCC-wiki Adopt-tier.

| # | Gate | Status | Finding |
|---|------|--------|---------|
| G0 | Repo discovery | **PASS** | `algorithmicsuperintelligence/optillm` resolved; primary author `codelion` (Asankhaya Sharma, 830 commits), Cerebras staff among contributors |
| G1 | Star + maturity | **PASS** | 3,761 stars verified (vs claimed 3,800, 1% inflation — negligible); 305 forks; 22 open issues; repo created 2024-08-22; actively maintained (last push 2026-05-07) |
| G2 | License | **PASS** | Apache-2.0 verbatim; declared in pyproject.toml |
| G3 | **Z3 integration** | **PASS — REAL** | `z3_solver.py` uses actual `z3` PyPI package; LLM generates Z3/SymPy code, subprocess executes with 30s timeout; **not a wrapper that just prompts about Z3** |
| G4 | MCP architecture | **QUALIFIED PASS** | optillm is an MCP **client** (consumer), not MCP **server** (provider). Integrates with external MCP servers via stdio/SSE/WebSocket. K44 framing of "MCP server hosting" is marketing nuance — technically it consumes, not hosts |
| G5 | LiteLLM gateway | **PASS** | All claimed providers wired (Claude, GPT, Gemini, Ollama, HF LoRA). LiteLLM unpinned (uses latest). Env-var config (`OPENAI_API_KEY`, `GEMINI_API_KEY`, etc.) |
| G6 | Credential vault | **FLAG** | **Only `os.environ.get()` integration**. No Vault/Secrets Manager hookpoints. Rotation requires re-deploy / env-var re-injection. For Cemini IP-sale: buyer inherits env-var credential model |
| G7 | HF LoRA loading | **PASS** | PEFT library; runtime adapter swap via `active_adapter` param; CPU/GPU auto-detect; test fixtures present |
| G8 | Offline Docker | **PASS** | `Dockerfile.offline` with spaCy model pre-download; Python 3.12-slim multi-stage build; ~2GB estimated |
| G9 | Failure modes / log hygiene | **CAUTION** | Retry + timeout handling clean. **conversation_logger copies requests/responses as-is — no explicit API key sanitization in debug logs**. Production deployment requires log-redaction hook before SaaS use |
| G10 | Org legitimacy | **YELLOW FLAG** | Org `algorithmicsuperintelligence` created 2025-10-17, but optillm repo predates org by 7 weeks (created 2024-08-22). Temporal anomaly — likely repo was transferred into org. Secondary org repo `openevolve` (6,274★) validates legitimacy. Not disqualifying. |

**Cross-route to OSINT**: the LiteLLM gateway + multi-provider routing is the missing piece for an "ask multiple frontier models the same threat-intel question and reconcile" workflow.

### Critical caveats for Cemini IP-sale

1. **Credential management** — No HashiCorp Vault / AWS Secrets Manager hookpoints. Buyers rotate credentials via env-var re-injection only. Document this for IP-sale due-diligence.
2. **MCP framing** — Update Cemini docs: optillm is an **MCP client**, not an MCP server host. The distinction matters when integrating with the existing kb-server / conductor MCP topology.
3. **Log sanitization** — Add a `conversation_logger` redaction hook before deploying to a production SaaS surface; the default logging captures full request/response payloads including API keys.
4. **Org timestamp anomaly** — Note the 7-week gap between org-creation and repo-creation; ask the author for clarification or trust the secondary-repo signal.

## Snippets

> "OptiLLM functions as an OpenAI API-compatible proxy utilizing LiteLLM to gateway multiple LLM providers, notably supporting complex inference tasks via the Z3 theorem prover for rigid logical reasoning."
[Source: @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md ¶169]
