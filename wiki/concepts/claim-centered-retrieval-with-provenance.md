---
title: Claim-centered retrieval with provenance
type: concept
tags: [concept, claims, provenance, mcp, retrieval, k233]
keywords: [AskChem, DOI, quote, claim store, MCP]
related:
  - sources/arxiv-askchem-claim-centered-literature-2607.28618.md
  - entities/tools/askchem.md
  - concepts/traceable-scholarship-citation-first-generation.md
  - concepts/multi-agent-evidence-artifact-layers.md
  - concepts/claim-drift-automated-research.md
  - concepts/externalized-research-synthesis-validation.md
  - concepts/mcp-contract-grounded-synthesis-and-validation-gate.md
  - sources/brief-k230-k233-memharness-tycho-agentradio-askchem-2026-07-31.md
  - concepts/phase1-adopt-wire.md
  - concepts/interpretable-agentic-document-ops.md
  - sources/arxiv-beyond-topk-read-agentic-retrieval-2608.06305.md
  - concepts/mcp-claim-validation-and-parameter-grounding.md
maturity: draft
created: 2026-07-31
updated: 2026-08-07
---

## Relations

- `@sources/arxiv-askchem-claim-centered-literature-2607.28618.md`
- `@entities/tools/askchem.md`
- `@concepts/traceable-scholarship-citation-first-generation.md`
- `@concepts/multi-agent-evidence-artifact-layers.md`

## Raw Concept

Should literature/agent retrieval return documents, or atomic provenance-carrying claims?

## Narrative

**AskChem** indexes claims (DOI + quote/locator), exposes taxonomy + evidence graph + MCP/SDK. Grounding lifts resolvable citation rate to 100% on their bench.

**Cemini steal (domain-agnostic):** Wiki ingest + research agents should prefer **claim units** over paper dumps — pairs with K210 citation-first / NO_EVIDENCE and evidence artifact layers. Chemistry corpus itself is OOD.

**Verdict:** **ADOPT** claim-unit + MCP grounding. **GO** MIT REFERENCE `.local/adopts/askchem`. Chemistry product **NO-GO** for Cemini ops.
