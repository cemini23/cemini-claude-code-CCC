---
title: "StarHarness — evolving harnesses with stratified search (CCC K313)"
type: source
tags: [source, arxiv, harness-evolution, stratified-search, enterprise, k313]
keywords: [2608.24804, StarHarness, ServiceNow, ITBench, EnterpriseOps-Gym, AutomationBench, frozen weights, held-out]
related:
  - concepts/stratified-harness-evolution.md
  - entities/tools/starharness.md
  - briefs/2026-08-26_ccc-k310-k314-sip-ready.md
maturity: draft
read_status: skimmed
created: 2026-08-26
updated: 2026-08-26
---

## Relations

- `@concepts/stratified-harness-evolution.md`
- `@entities/tools/starharness.md`
- `@briefs/2026-08-26_ccc-k310-k314-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | StarHarness: Evolving Harnesses with Stratified Search for Enterprise Environments |
| **arXiv** | 2608.24804 |
| **Authors** | Esakkivel Esakkiraja, Denis Akhiyarov, Vikas Yadav, Sai Rajeswar, Patrice Bechard, Sridhar Nemala, Sagar Davasam (ServiceNow + Mila) |
| **Code** | `github.com/ServiceNow/StarHarness` — **MIT**, ~3.4MB → **GO REFERENCE** clone `.local/adopts/StarHarness` (SPDX verified via API + LICENSE on disk) |
| **Retrieved** | 2026-08-26 |

## Narrative

Evolves environment-specific agent harnesses with **model weights frozen**. Search space covers prompt/task framing, tool interfaces, skills, MCP-backed providers, subagent structure, and agent-loop configuration — i.e., everything except the model and the pass criteria.

Method is the steal: build a **compact evolution pool by stratifying tasks on baseline failure behavior**, separate proposer-visible search tasks from proposer-hidden selection tasks, reserve held-out tasks for generalization measurement. Across ITBench SRE, EnterpriseOps-Gym ITSM, and AutomationBench Finance, evolution improves full-benchmark performance by **20–35 pp** after only **4–12 accepted changes** per environment; gains persist on excluded tasks and transfer without re-evolution across GPT and Qwen families.

Trace analysis finds three recurring specialization forms: **interface repair** (fix MCP argument handling), **environment conventions**, and **operational knowledge that compresses search**. This directly answers the harness-evolution eval discipline CCC has been converging on since K162/K281/K292/K298: search tasks ≠ selection tasks ≠ held-out; external evaluation contract; no closed rewrite of `## Verify`.

| Verdict | **ADOPT** the stratified protocol; MIT REFERENCE clone; trainer/runtime `wire_status: wont_wire`. Do **not** auto-evolve `.cursor/skills` (pairs K237/K298/K307). |
|---------|---------|

## Snippets

> "StarHarness constructs a compact evolution pool by stratifying tasks by baseline failure behavior, separates proposer-visible search tasks from proposer-hidden selection tasks, and reserves held-out tasks for evaluating generalization." [Source: arXiv 2608.24804 abstract]

> "harness evolution improves full-benchmark performance by 20–35 percentage points over the default harness, after 4–12 accepted changes per environment … transfer without re-evolution across GPT and Qwen model families." [Source: arXiv 2608.24804 abstract]

> "Trace analysis links them to interface repairs, environment conventions, and operational knowledge that compresses search." [Source: arXiv 2608.24804 abstract]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.24804-starharness-evolving-harnesses-with-stratified-s.pdf` |
|--------------|-------------------------------------------------------------------------------------------------------------------|
