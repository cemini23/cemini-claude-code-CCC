---
title: "Domain-grounded tool orchestration — intent / execution / explanation split over MCP (CCC K329)"
type: concept
tags: [concept, mcp, tool-orchestration, ontology, plan-execute-interpret, scoped-retrieval, intent-execution-explanation, k329]
keywords: [domain ontology, Plan-Execute-Interpret, intent execution explanation, MCP tool layer, scoped retrieval, script generation failure, interpretation accuracy, 2608.30696]
related:
  - sources/arxiv-domain-grounded-tool-orchestration-2608.30696.md
  - concepts/mcp-claim-validation-and-parameter-grounding.md
  - concepts/domain-solvers-as-agent-callable-mcp-skills.md
  - concepts/structured-state-semantic-actions.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-09-01_ccc-k328-k332-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-09-01
updated: 2026-09-01
---

## Relations

- `@sources/arxiv-domain-grounded-tool-orchestration-2608.30696.md`
- `@concepts/mcp-claim-validation-and-parameter-grounding.md`
- `@concepts/domain-solvers-as-agent-callable-mcp-skills.md`
- `@concepts/structured-state-semantic-actions.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-09-01_ccc-k328-k332-sip-ready.md`

## Raw Concept

The question: LLM-guided scientific analysis keeps failing with code that *executes* but performs the wrong analysis. What architecture removes that class of failure by construction? Answer from K329 (Kitware) [Source: wiki/sources/arxiv-domain-grounded-tool-orchestration-2608.30696.md]: a **Plan–Execute–Interpret** loop that separates intent interpretation (LLM) from execution (deterministic domain tools) from explanation (LLM), connected by MCP and constrained by a domain ontology.

## Narrative

Script generation conflates two different tasks: deciding *what* to analyze (intent interpretation — LLMs excel) and *how* to execute it (procedural domain knowledge — deterministic tools are superior). Generated scripts fail with **API hallucination, missing pipeline stages, and wrong-strategy errors**; the hardest failures are strategic — code that executes but answers the wrong question. These are domain-knowledge failures that better code generation cannot fix.

**Plan–Execute–Interpret (ADOPT pattern):**

1. **Plan (intent resolution).** The LLM consults a small (~25–30 entries) **domain ontology** (phenomenon / indicators / tools / follow-ups / significance, authored by a domain expert in JSON) and emits an ordered sequence of named tool invocations from the subset the ontology declares valid. The ontology constrains planning to valid analysis chains.
2. **Execute.** MCP dispatches to **deterministic domain tools** that build/modify a persistent pipeline and return **structured quantitative data, not renders** — enabling quantitative reasoning and follow-up analysis in the interpret phase.
3. **Interpret.** The LLM receives structured results plus the scoped ontology entry and produces a grounded explanation with quantitative specifics; the ontology's follow-ups field proposes diagnostic chains, closing the loop.

**Where grounding acts (the empirical steal):** the ablation locates the ontology's effect precisely —

- **Tool selection is already reliable; the ontology does not change it** (null result — tool schemas already describe what each tool does).
- **Interpretation accuracy rises 0.41 → 0.91** with the relevant ontology fact in context (unaided, the model inverted shape-factor physics: separated flow H>3 and laminar H≈2.6 both labeled "turbulent").
- **Delivery is decisive and monotonic in how targeted the retrieval is:** full-ontology dump 0.56; fact mined from a tool response 0.74; single scoped fact directly in the reasoning context 0.91. **A bulk dump decays toward the unaided baseline — scope retrieved facts.**

**CCC policy lines (wire `policy_wired`):**

- Assign NL to the LLM, execution to **typed deterministic tools**, explanation back to the LLM (the LLM is the interface, not the engine).
- **Scope retrieved ontology/knowledge facts** — never bulk-dump context; deliver the single relevant fact (pairs `@concepts/mcp-claim-validation-and-parameter-grounding.md` K259 parameter grounding, `@concepts/domain-solvers-as-agent-callable-mcp-skills.md` K272 solver-as-MCP, `@concepts/structured-state-semantic-actions.md` K316 evidence acquisition).
- Marginal cost of a new domain = ontology + tool wrappers; architecture/protocol/deployment unchanged — a template for adding specialist tools.
- ParaView/TTK runtime **OOD** `wont_wire` (no ParaView stack); the pattern is what CCC adopts.

| Confidence | `[CONFIRMED]` — ablation reported in the paper; policy is CCC synthesis |
|------------|------------|
