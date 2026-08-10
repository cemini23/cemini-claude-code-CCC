---
title: MCP claim-level validation + NL→tool parameter grounding (CASCADE / K259)
type: concept
tags: [concept, mcp, validation, tool-grounding, langgraph, k259]
keywords: [2608.05359, CASCADE, claim-validation, resolve_alias, schema-adherence, confident-wrong-default]
related:
  - sources/arxiv-cascade-agentic-regulatory-network-2608.05359.md
  - entities/tools/cascade-mcp.md
  - concepts/schema-bound-mcp-tool-surface.md
  - concepts/mcp-contract-grounded-synthesis-and-validation-gate.md
  - concepts/canary-tools-mcp-selection-diagnosis.md
  - concepts/claim-centered-retrieval-with-provenance.md
  - sources/brief-k259-cascade-mcp-claim-validation-2026-08-08.md
  - briefs/2026-08-08_ccc-handoff-k259-cascade-ingest.md
  - concepts/adversarial-curriculum-structured-reward-doc-fidelity.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-08
updated: 2026-08-10
---

## Relations

- `@concepts/adversarial-curriculum-structured-reward-doc-fidelity.md`
- `@sources/arxiv-cascade-agentic-regulatory-network-2608.05359.md`
- `@entities/tools/cascade-mcp.md`
- `@concepts/mcp-contract-grounded-synthesis-and-validation-gate.md`
- `@concepts/schema-bound-mcp-tool-surface.md`

## Raw Concept

How do we know an MCP-exposed tool’s *claim* is trustworthy, and that agents ground NL into the right parameters?

## Narrative

K259 CASCADE (arXiv **2608.05359**) separates two questions:

1. **Claim-level validation** — membership (“is this a known cancer gene?”) ≠ directional claim trust. Prefer held-out real-world / patient-data proxies that test the specific up/down (or analogous) claim the tool surfaces to the agent/user.
2. **Parameter grounding** — three failure modes on NL→MCP args:
   - Schema-adherence (unset/misrouted required fields) — largely fixed by stronger models
   - Alias / informal names — fixable with **server-side** alias resolution before lookup
   - Confident wrong defaults on ambiguous queries — server-side “if unset” guards **fail** because the model *sets* the wrong value

### Cemini steal (ADOPT)

1. Before LIVE exposure of high-blast MCP tools: define what claim the tool report repeats; validate that claim class against ground truth or a stated proxy (pairs Traceable Scholarship / K172 contract gates).
2. Prefer server-side normalization (aliases, enums) over trusting model-filled strings.
3. For ambiguous required fields: do not default silently — clarify or refuse (pairs K244 clarify-before-act). “Unset-only” guards miss confident wrong fills.
4. Small local models need stricter schema enforcement; larger models reduce schema fails but not confident-wrong defaults.

| Verdict | **ADOPT** policy. Bio CASCADE runtime **wont_wire**. Entity `cascade-mcp` REFERENCE. |
