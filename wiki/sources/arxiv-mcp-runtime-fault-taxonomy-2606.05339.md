---
title: MCP server runtime fault taxonomy (arXiv 2606.05339)
type: source
tags: [source, arxiv, mcp, reliability, fault-taxonomy]
keywords: [2606.05339, mcp-faults, json-rpc, fault-injection, repository-mining]
related:
  - concepts/mcp-server-runtime-fault-taxonomy.md
  - concepts/self-healing-agent-sessions.md
  - concepts/mcp-context-optimization.md
  - concepts/mcp-server-catalog-curation.md
  - concepts/seclaw-agent-security-evaluation.md
  - entities/tools/lazy-tool.md
  - entities/tools/defenseclaw.md
  - concepts/skill-vetting.md
maturity: draft
read_status: read
created: 2026-06-06
updated: 2026-06-06
---

## Relations

- `@concepts/mcp-server-runtime-fault-taxonomy.md` — CCC synthesis + Cemini Phase-0 mapping
- `@concepts/self-healing-agent-sessions.md` — session failure taxonomy extension for MCP disconnect classes
- `@concepts/mcp-context-optimization.md` — cost stack now has named reliability fault classes beneath it
- `@concepts/mcp-server-catalog-curation.md` — catalog Phase-0 failure-mode checklist
- `@concepts/seclaw-agent-security-evaluation.md` — security subcategory (54 threads) complements trajectory eval
- `@entities/tools/lazy-tool.md` — proxy layer adds transport/session indirection surface
- `@entities/tools/defenseclaw.md` — admission-control parallel for Security category faults

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | A Taxonomy of Runtime Faults in Model Context Protocol Servers |
| **Authors** | Joshua Owotogbe, Indika Kumara, Willem-Jan van den Heuvel, Damian Andrew Tamburri, Antonio Ken Iannillo, Roberto Natella |
| **arXiv** | 2606.05339v1 [cs.SE] |
| **Replication** | https://figshare.com/s/c1e1e802e1b9f38fddf0 |
| **Location** | `raw-sources/arxiv-2606.05339-a-taxonomy-of-runtime-faults-in-model-context-pr.pdf` |
| **Retrieved** | 2026-06-06 |
| **Read status** | read (methodology, taxonomy structure, validation survey) |

## Narrative

First empirical **runtime fault taxonomy for MCP servers** — not build failures or infra outages, but **protocol-contract violations** while the server remains operational. Built from **837 confirmed fault threads** across **473 GitHub MCP server repos** (from 2,016 MCP-keyword threads after filtering). Bottom-up open coding → **11 top-level categories**, **27 subcategories**, **73 leaf fault types**. Practitioner survey (**n=55** MCP server developers): average **20/27** subcategories encountered; no subcategory unobserved; open-ended responses did not reveal missing classes.

**CCC relevance:** names the failure modes behind "MCP disconnect" and silent tool failures in long Claude Code sessions; informs Phase-0 MCP catalog curation, regression test design, and SeClaw-style fault injection — distinct from context-cost optimization.

## Snippets

> "We define an MCP fault as a defect that causes a server to violate its coordination obligations under the protocol contract or schema constraints."

> "The final taxonomy comprises 11 top-level categories, 27 sub-categories, and 73 leaf nodes."

> "Participants reported experiencing, on average, 20 of the 27 subcategories, and no category remained unobserved."

> — [Source: arxiv-2606.05339-a-taxonomy-of-runtime-faults-in-model-context-pr.pdf p.1–7, retrieved 2026-06-06]
