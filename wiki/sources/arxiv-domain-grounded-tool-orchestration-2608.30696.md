---
title: "Domain-Grounded Tool Orchestration for LLM-Guided Scientific Analysis (CCC K329)"
type: source
tags: [source, arxiv, mcp, tool-orchestration, ontology, intent-execute-explain, plan-execute-interpret, policy, k329]
keywords: [2608.30696, Kitware, ParaView, TTK, MCP, domain ontology, Plan-Execute-Interpret, script generation failure, scoped retrieval, interpretation accuracy]
related:
  - concepts/domain-grounded-tool-orchestration.md
  - concepts/mcp-claim-validation-and-parameter-grounding.md
  - concepts/domain-solvers-as-agent-callable-mcp-skills.md
  - concepts/structured-state-semantic-actions.md
  - briefs/2026-09-01_ccc-k328-k332-sip-ready.md
maturity: draft
read_status: read
created: 2026-09-01
updated: 2026-09-01
---

## Relations

- `@concepts/domain-grounded-tool-orchestration.md`
- `@concepts/mcp-claim-validation-and-parameter-grounding.md`
- `@concepts/domain-solvers-as-agent-callable-mcp-skills.md`
- `@concepts/structured-state-semantic-actions.md`
- `@briefs/2026-09-01_ccc-k328-k332-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Domain-Grounded Tool Orchestration for LLM-Guided Scientific Analysis |
| **arXiv** | 2608.30696 (cs.CE, 2026-08-31) |
| **Authors** | Jeff Lee, Sebastien Jourdain, Corey Quammen, Patrick O'Leary, Berk Geveci (Kitware, Inc.) |
| **Venue** | arXiv preprint, 27 pages |
| **Code** | BSD 3-Clause per paper (trame / trame-llm infra) — **OOD** (ParaView/TTK stack) → no clone |
| **Retrieved** | 2026-09-01 |

## Narrative

**Verdict: ADOPT pattern — separate intent (LLM) / execution (deterministic domain tools) / explanation (LLM) over MCP; domain ontology constrains planning.**

Script generation (the dominant LLM-assisted-visualization paradigm) fails in three ways per Zhao et al. (2025): **API hallucination, missing pipeline stages, and wrong-strategy errors** — the hardest class is strategic: code that executes but answers the wrong question. These are domain-knowledge failures, not code-quality failures.

The **Plan–Execute–Interpret loop** (Kitware, on ParaView server infra): the LLM plans an ordered sequence of named tool invocations constrained by a small (~25–30 entries) **domain ontology** (five fields: phenomenon / indicators / tools / follow-ups / significance, authored in JSON by a domain expert); MCP dispatches to **deterministic domain tools** that return **structured quantitative data, not renders**; the LLM interprets the results grounded by the ontology's scoped entry and can propose follow-ups. Tools return data; the pipeline persists across invocations.

**Ablation finding (the steal):** the ontology does **not** change tool *selection* — precision/recall unchanged with ontology present vs removed (null result; tool schemas already suffice). It corrects **result interpretation**: 34-case benchmark, accuracy **0.41 → 0.91** with the relevant ontology fact in context (unaided, the model had shape-factor physics inverted, labeling separated flow H>3 and laminar H≈2.6 alike as "turbulent"). **Delivery is decisive and monotonic in how targeted retrieval is:** full-ontology dump 0.56; fact mined from a tool response 0.74; single scoped fact directly in the reasoning context **0.91**. **Scope retrieved ontology facts; a bulk dump decays toward the unaided baseline.**

Generalization: adding the TTK (topological data analysis) domain required only an ontology + tool wrappers around existing filters — no change to architecture/protocol/deployment. Cross-solver robustness: dynamic field resolution maps semantic names ("skin friction") to solver-specific arrays (Cfin / wallShearStress) at runtime.

CCC policy lines: NL → LLM, execution → typed deterministic tools, explanation → LLM; scope retrieved facts (pairs K259 parameter grounding, K272 solver-as-MCP). ParaView/TTK runtime **OOD** `wont_wire` — do not stand up a ParaView stack. `policy_wired` (pattern).

| Confidence | `[CONFIRMED]` — ablation reported in the paper; policy is CCC synthesis |
|------------|------------|

## Snippets

> "The LLM is the interface, not the engine. Domain workflows are the engine. MCP is the protocol. The ontology is the knowledge." [Source: arXiv 2608.30696 §11]

> "Ontology grounding does not measurably affect tool selection … grounding sharply improves interpretation … accuracy rose from 0.41 unaided to 0.91 with the relevant ontology fact in context." [Source: arXiv 2608.30696 §8.2]

> "The ontology's content is only as useful as the retrieval that delivers it: a bulk dump decays toward the unaided baseline, while a scoped lookup of the one hinted key realizes most of the benefit." [Source: arXiv 2608.30696 §8.2]

> "Adding the second domain required only an ontology file and MCP tool wrappers around existing TTK filters; no changes to the architecture, protocol, deployment, or user interface." [Source: arXiv 2608.30696 §1]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.30696-domain-grounded-tool-orchestration-for-llm-guide.pdf` |
|--------------|-------------------------------------------------------------------------------------------------------------------|
