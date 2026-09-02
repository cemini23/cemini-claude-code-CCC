---
title: "Delegation Without Trust — identity, authorization, runtime governance (CCC K333)"
type: source
tags: [source, arxiv, delegation, authorization, untrusted-model, governance, cybersec, policy, k333]
keywords: [2609.00267, Delegation Without Trust, untrusted model, authorization broker, scoped delegation, confused deputy, token theft, prompt injection, LangGraph, CrewAI, AutoGen, MCP]
related:
  - concepts/untrusted-model-delegation-governance.md
  - concepts/signed-mandate-mcp-protocol-enforcement.md
  - concepts/mandate-signature-vs-preauth-intent.md
  - concepts/recognition-vs-enforcement-instruction-arbitration.md
  - concepts/output-attestation-and-delegation-ancestry.md
  - briefs/2026-09-02_ccc-k333-k336-sip-ready.md
maturity: draft
read_status: read
created: 2026-09-02
updated: 2026-09-02
---

## Relations

- `@concepts/untrusted-model-delegation-governance.md`
- `@concepts/signed-mandate-mcp-protocol-enforcement.md`
- `@concepts/mandate-signature-vs-preauth-intent.md`
- `@concepts/recognition-vs-enforcement-instruction-arbitration.md`
- `@concepts/output-attestation-and-delegation-ancestry.md`
- `@briefs/2026-09-02_ccc-k333-k336-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Delegation Without Trust: Identity, Authorization, and Runtime Governance for Multi-Agent Systems |
| **arXiv** | 2609.00267 (cs.CR, 2026-09-02) |
| **Authors** | VotalAI / industry security authors (see paper) |
| **Venue** | arXiv preprint |
| **Code** | VotalAI LLM Shield production reference — **no public SPDX repo** → no clone |
| **Retrieved** | 2026-09-02 |

## Narrative

**Verdict: Cybersec-primary + CCC ADOPT policy — treat the model as untrusted; authorization must live outside model reasoning.**

The paper argues that multi-agent orchestration frameworks (LangGraph, CrewAI, AutoGen, MCP tool hosts) assume the model can safely gate its own delegated actions. Under **full prompt injection**, that assumption fails: bearer credentials plus model-gated tool calls cannot enforce scoped delegation.

**Core property — untrusted model:** security controls must hold when the LLM is fully compromised by prompt injection. Any authorization decision that depends on model reasoning is bypassable.

**External authorization broker:** a runtime layer outside the model evaluates each delegated action against scoped policy before execution. The broker issues **scoped sub-agent delegation** (task-bound, time-bound, tool-bound) instead of handing sub-agents bearer credentials the model can replay or widen.

**Four delegation threats (policy vocabulary only — no exploit text):**

1. **Confused deputy** — a trusted sub-agent executes an action on behalf of an unauthorized principal because the broker did not bind principal identity to the scoped request.
2. **Token theft / replay** — long-lived bearer tokens extracted from context are reused outside the intended delegation window.
3. **Prompt-injection privilege escalation** — injected instructions cause the model to invoke tools or delegate scopes beyond the operator's intent.
4. **Compromised sub-agents** — a sub-agent with excessive authority amplifies a single injection into fleet-wide effects.

**Framework gap:** surveyed stacks expose identity and tool wiring but lack a **non-bypassable external authorization broker** at the delegation boundary. MCP transports credentials and tool schemas; they do not, by themselves, enforce scoped delegation under an untrusted model.

**Production reference:** VotalAI LLM Shield reports broker decisions at ~2.6 µs per authorization check in their deployment narrative — illustrative latency only; CCC does not install the product.

CCC policy lines: **never gate authority inside model reasoning**; prefer external broker + scoped delegation over bearer credentials the model holds (pairs K285 signed mandates at MCP proxy, K310 pre-auth intent manipulation, K326 external reference monitor, K328 post-incident attestation ancestry). **No public repo → policy only;** runtime `policy_wired`. **Zero attack payloads or PoC text in wiki.**

| Confidence | `[CONFIRMED]` — threat taxonomy and framework survey from the paper; policy is CCC synthesis |
|------------|------------|

## Snippets

> "Security must hold when the model is fully prompt-injected — treating the LLM as a trusted authorization gate is architecturally unsound." [Source: arXiv 2609.00267 — paraphrase of core thesis; verify against PDF]

> "Bearer credentials combined with model-gated actions fail all four delegation threat classes under an untrusted-model assumption." [Source: arXiv 2609.00267 — policy summary]

> "An external authorization broker with scoped sub-agent delegation closes the architectural gap at sub-microsecond decision latency in production reference deployments." [Source: arXiv 2609.00267 — VotalAI LLM Shield reference]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2609.00267-delegation-without-trust-an-empirical-gap-analys.pdf` |
|--------------|------------------------------------------------------------------------|
