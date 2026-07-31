---
title: "AskChem — claim-centered infrastructure for literature synthesis"
type: source
tags: [source, arxiv, claims, provenance, mcp, chemistry, k233]
keywords: [2607.28618, AskChem, claim store, DOI, MCP, askchem.org]
related:
  - concepts/claim-centered-retrieval-with-provenance.md
  - concepts/traceable-scholarship-citation-first-generation.md
  - concepts/multi-agent-evidence-artifact-layers.md
  - concepts/claim-drift-automated-research.md
  - entities/tools/askchem.md
  - sources/brief-k230-k233-memharness-tycho-agentradio-askchem-2026-07-31.md
maturity: draft
created: 2026-07-31
updated: 2026-07-31
---

## Relations

- `@concepts/claim-centered-retrieval-with-provenance.md`
- `@entities/tools/askchem.md`
- `@concepts/traceable-scholarship-citation-first-generation.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | AskChem: Claim-Centered Infrastructure for Chemistry Literature Synthesis |
| **Author** | Yan, Wolfe, Martiniani, Cho (NYU / Matterstack) |
| **arXiv** | 2607.28618 |
| **Pages** | 10 |
| **Retrieved** | 2026-07-31 |
| **Code** | `bingyan4science/askchem` MIT (~9.3MB); live https://askchem.org — **GO** REFERENCE |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.28618-askchem-claim-centered-infrastructure-for-chemis.pdf` |

## Narrative

Unit of retrieval = **provenance-carrying claim** (DOI + verbatim quote/locator), not paper. 2.4M claims / 147K papers; web + REST + SDK + **MCP**. AskChem-Bench: GPT-5.5 + AskChem → **100%** resolvable DOIs vs 88.3% without. Chemistry domain OOD for Cemini ops — **ADOPT** claim-unit + MCP grounding pattern (pairs with K210 Traceable Scholarship); **GO** MIT client/REFERENCE clone; do not treat as Cemini chemistry product.
