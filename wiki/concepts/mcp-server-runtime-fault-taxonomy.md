---
title: MCP server runtime fault taxonomy — 11 categories from 837 GitHub threads
type: concept
tags: [concept, mcp, reliability, fault-taxonomy, arxiv]
keywords: [2606.05339, mcp-faults, json-rpc, session-lifecycle, tool-execution, fault-injection]
related:
  - sources/arxiv-mcp-runtime-fault-taxonomy-2606.05339.md
  - concepts/self-healing-agent-sessions.md
  - concepts/mcp-context-optimization.md
  - concepts/mcp-server-catalog-curation.md
  - concepts/seclaw-agent-security-evaluation.md
  - concepts/skill-vetting.md
  - entities/tools/lazy-tool.md
  - entities/tools/defenseclaw.md
  - entities/tools/conductor-mcp.md
  - "@cybersecurity-wiki/concepts/mcp-security-posture.md"
maturity: draft
created: 2026-06-06
updated: 2026-06-06
---

## Relations

- `@sources/arxiv-mcp-runtime-fault-taxonomy-2606.05339.md` — arXiv 2606.05339 provenance
- `@concepts/self-healing-agent-sessions.md` — extends MCP disconnect row with named fault classes
- `@concepts/mcp-context-optimization.md` — four-layer cost stack; this page is the **reliability** complement
- `@concepts/mcp-server-catalog-curation.md` — Phase-0 checklist gains empirical failure-mode vocabulary
- `@concepts/seclaw-agent-security-evaluation.md` — Security category (54 threads) + fault-injection test design
- `@entities/tools/lazy-tool.md` — proxy adds stdio/HTTP transport indirection
- `@entities/tools/defenseclaw.md` — admission control for Security-category faults
- `@cybersecurity-wiki/concepts/mcp-security-posture.md` — canonical security hardening (this page = reliability taxonomy)

## Raw Concept

arXiv **2606.05339** — first empirical taxonomy of **MCP server runtime faults**: defects violating protocol contract or schema constraints while the server still runs. **837 threads / 473 repos** → **11 categories / 27 subcategories / 73 leaves**. Validated by **55 practitioner survey** (avg 20/27 subcategories seen).

## Narrative

### Definition

An **MCP fault** = cause of incorrect service at the MCP coordination interface — omission, incorrect content, or timing violations — **not** compile failures, infra outages, or client/agent bugs (out of scope for this paper).

### 11 top-level categories (thread counts)

| Category | Threads | CCC symptom examples |
|----------|---------|---------------------|
| **Tool** | 194 | Silent success on failed op; schema mismatch; result lost before model |
| **Data & Schema** | 147 | Runtime schema drift; unexpected null fields |
| **State & Configuration** | 143 | Stale session ID; ignored config flag; resource not persisted |
| **Session Lifecycle** | 65 | Init before `initialized`; async/sync mix (fastmcp pattern) |
| **Security** | 54 | Missing auth check; expired credential; token forwarded upstream |
| **Resource** | 58 | Invalid URI; non-resolvable path |
| **Model & Provider** | 48 | Provider unavailable; invalid model ID |
| **Base Protocol** | 45 | Empty `id` on tool response; mismatched stream event IDs |
| **Transport Layer** | 45 | Non-protocol stdout on stdio; SSE resumption failure |
| **Prompt** | 22 | Missing prompt registration; bad template substitution |
| **Timeout & Cancellation** | 16 | Timeout too short; cancel without notification |

### High-salience subcategories for Cemini sessions

1. **Tool Execution — input not validated against schema (46)** — model sends malformed args; server throws instead of structured JSON-RPC error.
2. **Tool Result — result lost before model injection (23)** — looks like "MCP worked but agent ignored output."
3. **Session State — stale/reused session identifier (22)** — tunnel reconnect without fresh session header.
4. **Stdio Transport — non-protocol output on stdout (36)** — logging/debug prints break Claude Code stdio MCP parsing.
5. **Configuration Handling — invalid parameter value (56)** — server accepts but mis-enforces config (silent default behavior).

### Cemini Phase-0 MCP checklist (derived)

Before GO on any new MCP server:

| Check | Taxonomy anchor |
|-------|-----------------|
| Stdio: only JSON-RPC on stdout | Transport → Stdio |
| Tool schemas match handler validation | Tool → Execution |
| Structured errors, not unhandled exceptions | Tool → Execution |
| Session ID stable across streaming turns | State → Session State |
| Timeouts match transport + workload | Timeout & Cancellation |
| Auth headers validated before tool dispatch | Security → Authentication |
| SeClaw or defenseclaw scan for write tools | Security → Authorization |

### vs context optimization

`@concepts/mcp-context-optimization.md` answers **token cost**. This page answers **why MCP calls fail silently or corrupt sessions** — orthogonal layers. A cheap session can still hit Tool Result propagation faults.

### Cross-wiki routing

- **CCC-primary:** reliability taxonomy, Phase-0 checklist, self-healing session mapping.
- **Cybersecurity-primary:** Security category fault injection, auth/token validation hardening → `@cybersecurity-wiki/concepts/mcp-security-posture.md`.

**Verdict:** **ADOPT (checklist)** — embed taxonomy rows in MCP Phase-0 curation; no framework install.

## Phase-0 Audit (2026-06-06)

**Method:** Paper methodology review + replication URL cited in source. Not a third-party install candidate.

| Check | Result |
|-------|--------|
| Artifact type | Academic taxonomy + GitHub thread corpus (837 threads / 473 repos) |
| Replication | [figshare.com/s/c1e1e802e1b9f38fddf0](https://figshare.com/s/c1e1e802e1b9f38fddf0) — cited in paper §4.7 |
| Practitioner validation | n=55 survey; avg 20/27 subcategories observed [TENTATIVE — paper claim] |
| CCC install | **N/A** — no MCP server binary; **ADOPT** checklist rows in `@concepts/mcp-server-catalog-curation.md` + `@concepts/skill-vetting.md` step 7 |
| Security routing | Security category faults → `@cybersecurity-wiki/concepts/mcp-security-posture.md` |

**Decision — ADOPT (checklist only).** Use 11-category vocabulary when logging MCP failures in `wiki/log.md` and Phase-0 MCP evals. Fetch figshare datasets when building regression fixtures (optional; not blocking).

## Snippets

> "An MCP server may compile and start successfully while still violating MCP-specific runtime expectations during execution."

> "Fault categories can guide tests that check whether invalid tool schemas, missing message identifiers, or timeout violations are handled correctly."

> — [Source: arxiv-2606.05339-a-taxonomy-of-runtime-faults-in-model-context-pr.pdf p.1–2, retrieved 2026-06-06]
