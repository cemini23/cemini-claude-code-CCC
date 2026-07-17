---
title: "Ground-Side Mission Plan Compilation with Policy-as-Code Guardrails"
type: source
tags: [source, arxiv, policy-as-code, opa, mcp, guardrails, k181]
keywords: [2607.14798, OPA, Rego, Argo, Kueue, satellite-mission-compiler, EUPL]
related:
  - concepts/policy-as-code-layered-validation-for-agent-artifacts.md
  - concepts/mcp-contract-grounded-synthesis-and-validation-gate.md
  - concepts/coding-agent-install-gap-and-preinstall-gate.md
  - entities/tools/satellite-mission-compiler.md
  - sources/brief-k181-policy-as-code-guardrails-2026-07-17.md
maturity: draft
created: 2026-07-17
updated: 2026-07-17
---

## Relations

- `@concepts/policy-as-code-layered-validation-for-agent-artifacts.md`
- `@entities/tools/satellite-mission-compiler.md` — EUPL-1.2 GO local adopt
- `@concepts/mcp-contract-grounded-synthesis-and-validation-gate.md` — K172 validation peer
- `@sources/brief-k181-policy-as-code-guardrails-2026-07-17.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Ground-Side Mission Plan Compilation with Policy-as-Code Guardrails for Cloud-Native Satellite Platforms |
| **Author** | Hsiu-Chi Tsai, Chia-Tung Chung (NYCU) |
| **arXiv** | 2607.14798 |
| **Code** | `github.com/thc1006/satellite-mission-compiler` — **EUPL-1.2** |
| **DOI** | 10.5281/zenodo.21228150 |
| **Retrieved** | 2026-07-17 |

## Narrative

Four-stage ground-side compiler: parse mission plan (Pydantic schema) → **OPA/Rego** policy package (10 deny rules with provenance tags) → typed WorkflowIntent IR → Argo Workflow DAGs + Kueue Job manifests. Layered validation framed as NASA-STD-8739.8B **safety** defense-in-depth (vs NIST security reading). Six **MCP tools** expose the pipeline to AI agents with path-traversal protection (CWE-22). Satellite domain off CCC day-to-day; **policy-as-code + MCP-gated compile** is the steal.

## Snippets

> "Six Model Context Protocol (MCP) tools expose the pipeline to AI agents through a path-traversal-protected interface" — Abstract region
