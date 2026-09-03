---
title: "ARGUS — MCP-grounded root cause analysis for Kubernetes incidents"
type: source
tags: [source, arxiv, mcp, rca, kubernetes, observability, sre, k306]
keywords: [2608.23084, argus, prometheus, loki, nats, slack, diagnostic prescriptive asymmetry, chalmers]
related:
  - concepts/diagnostic-prescriptive-asymmetry-mcp-rca.md
  - entities/tools/argus-agentic-runtime.md
  - briefs/2026-08-25_ccc-k300-k309-sip-ready.md
  - concepts/evidence-grounded-structured-rca.md
  - sources/arxiv-llms-telecom-rca-structured-reasoning-2609.02805.md
maturity: draft
read_status: read
created: 2026-08-25
updated: 2026-09-03
---

## Relations

- `@concepts/diagnostic-prescriptive-asymmetry-mcp-rca.md`
- `@entities/tools/argus-agentic-runtime.md` (dual-ID: CCC K253 Argus persist/pivot — different product, do not merge)
- `@briefs/2026-08-25_ccc-k300-k309-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | ARGUS: MCP-Grounded Root Cause Analysis for Kubernetes Incidents |
| **arXiv** | 2608.23084 |
| **Authors** | Ergi Senja, Seyed Mohammad Reza Razavi Zadegan, Philipp Leitner (Chalmers / University of Gothenburg) |
| **Code** | none public → **policy only**, runtime `wont_wire` |
| **Retrieved** | 2026-08-25 |

## Narrative

K8s incident triage correlates metrics, logs, container state, and messaging across fragmented tools. ARGUS connects a commercial LLM to **live** observability through standardized MCP servers — Kubernetes state, Prometheus, Loki, NATS — and posts structured diagnostic summaries into the **Slack incident channel** where on-call engineers already work.

Evaluation triangulates three methods: fault injection across **10 Kubernetes incident scenarios**, rubric-based scoring of RCA summaries on three dimensions, and semi-structured interviews with **six on-call engineers** at an industrial partner. Results: correct root cause named in **10/10** scenarios; aggregate **MCP success ratio 0.91**. The central finding is the **diagnostic/prescriptive asymmetry**: practitioners trusted the diagnosis but consistently distrusted the recommended fixes.

Dual-ID note: this is **CCC K306**; CCC K253 is the *Argus persist/pivot runtime* (`lbx154/Argus`, `entities/tools/argus-agentic-runtime.md`). Same name, unrelated systems — resolve by file + wiki.

| Verdict | **ADOPT** diagnostic/prescriptive asymmetry as policy: agents may draft diagnoses for human verification; **never auto-apply agent remediations**. No public repo → `wont_wire` runtime. |
|---------|---------|

## Snippets

> "ARGUS named the correct root cause in all ten scenarios with an aggregate MCP success ratio of 0.91. Practitioners trusted the diagnostic output but consistently expressed scepticism toward the recommended fixes." [Source: arXiv 2608.23084 abstract]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.23084-argus-mcp-grounded-root-cause-analysis-for-kuber.pdf` |
|--------------|-------------------------------------------------------------------------------------------------------------------|
