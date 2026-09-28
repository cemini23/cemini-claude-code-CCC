---
title: "A Safety-Bounded SDC-to-MCP Gateway for Medical AI Agents (CCC K397)"
type: source
tags: [source, arxiv, k397]
keywords: [2609.31358, k397]
related:
  - concepts/safety-bounded-sdc-mcp-gateway.md
  - briefs/2026-09-28_ccc-k396-k400-sip-ready.md
maturity: draft
read_status: deep-read
created: 2026-09-28
updated: 2026-09-28
---

## Relations

- `@concepts/safety-bounded-sdc-mcp-gateway.md`
- `@briefs/2026-09-28_ccc-k396-k400-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | A Safety-Bounded SDC-to-MCP Gateway for Medical AI Agents |
| **arXiv** | 2609.31358 (2026-09) |
| **Retrieved** | 2026-09-28 |

## Narrative

**Verdict: ADOPT policy awareness.**

**Safety-bounded SDC-to-MCP gateway** for medical agents — bounded envelope between structured clinical data/control (SDC) and MCP tool surface (pairs K337 capability leases / K271 MCP auth gateway / K377 clinical MCP tool-surface steal). **Clinical runtime OOD** for CCC; policy awareness only. **No PoCs.** No clone. Runtime **`wont_wire`**; concept **`policy_wired`**.

**Deep-read note:** **No-execution boundary** on agent path — dry-run / policy-validated affordances only; narrative fluency ≠ structured compliance (pairs K337 execution gate / K326 external enforcement).


## Snippets

> "In medical environments, however, exposing device state and action affordances requires deterministic constraints on possible effects." [Source: arXiv 2609.31358 abstract (retrieved 2026-09-28)]

> "The term safety-bounded denotes a narrow no-execution property: agent-facing requests dispatch no SDC device operation." [Source: arXiv 2609.31358 abstract (retrieved 2026-09-28)]

> "The results show semantically explicit resource exposure, visible rejection of invalid or outdated state, and preservation of the no-execution boundary across resource, proposal, and authorization paths." [Source: arXiv 2609.31358 abstract (retrieved 2026-09-28)]

> "Explicit semantic metadata improved conformity to required metric identifiers in structured alarm outputs relative to a generic representation, while retained structured-output failures reveal a distinction between plausible narrative answers and task-compliant machine-readable results." [Source: arXiv 2609.31358 abstract (retrieved 2026-09-28)]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2609.31358-a-safety-bounded-sdc-to-mcp-gateway-for-medical.pdf` (local inbox pending archive) |

