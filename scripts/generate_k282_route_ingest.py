#!/usr/bin/env python3
"""Fill CCC pages for the k282 inbound OSINT route (2026-10-05 batch).

Source: `briefs/2026-10-05_k282-ccc-agent-eval.md` — routes 4 OSINT-ingested papers that
touch surfaces CCC owns. Their canon stays on OSINT; CCC holds the harness/eval takeaways.
"""
from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DATE = "2026-10-06"
BRIEF = "2026-10-05_k282-ccc-agent-eval-route.md"
RULE = "ccc-k282-route-wires.mdc"

ENTRIES = [
    {
        "arxiv": "2610.03153",
        "concept": "harness-security-axis-comparison",
        "slug": "arxiv-evoriskbench-harness-security-axis-2610.03153",
        "title": "EvoRiskBench — a security metric for the harness",
        "osint": "@osint-wiki/sources/arxiv-2610.03153-evoriskbench-runtime-2026-10-05.md",
        "narrative": (
            "**Nine model × harness configurations, scored on inbound injection through the surfaces "
            "the harness itself exposes — MCP tools, skills, and subagents.** Aggregate attack "
            "success **37.46%**; worst configuration **68.44%** (DeepSeek-V4-Pro-0813 × Codex). The "
            "headline number is the decomposition: **model spread is 54.37 pp; harness spread is "
            "5.41 pp.** **CCC reading:** the harness is a *second-order* factor in absolute terms — "
            "but 5.41 pp is still real, and it is the factor **we control**. Model choice is mostly "
            "fixed for a given operator; harness configuration is not. This gives CCC a way to "
            "compare harness variants on a **security axis** rather than only a capability axis, "
            "which the existing benchmark set does not offer. Pairs K402 MCP error surfaces / "
            "`@concepts/schema-bound-mcp-tool-surface.md` / K421 tool-boundary mediation / "
            "`@concepts/measurement-integrity-mcp-security-eval.md`. **Routing:** the full brief goes "
            "to the cybersec lane; CCC keeps the harness-comparison framing. **No clone, no install.**"
        ),
        "snippet": (
            "Model spread (54.37 pp) ≫ harness spread (5.41 pp)."
        ),
    },
    {
        "arxiv": "2610.03243",
        "concept": "gate-separation-theorem-skill-density",
        "slug": "arxiv-kinetic-gated-evolution-separation-2610.03243",
        "title": "Kinetic theory of the gated self-evolving agent",
        "osint": "@osint-wiki/sources/arxiv-2610.03243-kinetic-gated-evolution-2026-10-05.md",
        "narrative": (
            "**The mathematics of a validation gate over a population of skills.** Two results. "
            "First, fluctuation scaling is **flat at sparse density (β = −0.04)** but **−0.58 once "
            "density triples** — a gate that behaves one way at low skill density can behave "
            "differently when the skill set grows. Second, a **separation theorem** requiring the "
            "evaluator to stay **outside the population it judges**. **CCC reading:** the separation "
            "theorem is the formal statement of a rule CCC already enforces — *the evaluator is not "
            "in the population* — and it converts a practice into a provable constraint. The density "
            "result is the genuinely new part and it has a **concrete trigger**: the federated skill "
            "count. CCC's skill set has grown (52 → 72 federated skills in the last cycle alone, plus "
            "36 sibling skills). A gate validated at low density should be **re-checked as the count "
            "climbs**, not assumed to hold. Pairs `@concepts/validation-ratchet-skill-evolution.md` / "
            "`@concepts/skill-misevolution.md` / `@concepts/progressive-skill-discovery-access-"
            "control.md` / K428 CLIFT (certified verifier, same family). **No clone, no install.**"
        ),
        "snippet": (
            "a gate that holds at low skill density can behave differently when the skill set triples."
        ),
    },
    {
        "arxiv": "2610.03574",
        "concept": "browsing-agent-eval-bar",
        "slug": "arxiv-hyperbrowsecomp-browsing-eval-bar-2610.03574",
        "title": "HyperBrowseComp — the bar for browsing agents",
        "osint": "@osint-wiki/sources/arxiv-2610.03574-hyperbrowsecomp-2026-10-05.md",
        "narrative": (
            "**423 questions, 13 languages, multimodal.** Strongest configuration reaches **31.68%** "
            "accuracy; humans score **15/30**; and **57.68% of failures are shared across "
            "configurations**. **CCC reading:** the shared-failure number is the one that matters. "
            "When a majority of failures are common to every configuration, **the bottleneck is the "
            "task type, not any single model or harness** — which means a better model will not fix "
            "it and a better harness may not either. That is a useful ceiling to know before "
            "commissioning a browsing-agent eval. The benchmark also **exercises Exa**, the "
            "workspace's external-research path, so it is the reference shape if CCC ever builds one. "
            "Pairs `@concepts/deep-research-evaluation-prompt.md` / "
            "`@concepts/verifiable-search-agent-environment.md` / K426 MCPacific (tool discovery at "
            "scale). **No clone, no install.**"
        ),
        "snippet": (
            "shared failure across configs means the bottleneck is the task type, not a single model."
        ),
    },
    {
        "arxiv": "2610.03564",
        "concept": "curated-vs-self-generated-skills",
        "slug": "arxiv-finskillsbench-curated-vs-self-generated-2610.03564",
        "title": "FinSkillsBench — curated skills beat self-generated ones",
        "osint": "@osint-wiki/sources/arxiv-2610.03564-finskillsbench-2026-10-05.md",
        "narrative": (
            "**A numbers argument for the skill-audit discipline.** Ablation on a financial-agent "
            "benchmark: **curated skills +16.2 pts; self-generated skills +0.5; tools alone +19.5; "
            "docs alone +5.6** — and the components are **subadditive**, so the whole is less than "
            "the sum. Separately, a nine-stage composed workflow shows **\"silent competence\"**: "
            "optimality **0.934** while **mandate adherence is 0/33** — the agent solves the stated "
            "problem while violating the actual constraint. **CCC reading:** *curated beats "
            "self-generated by ~32×* is the quantitative case for vetting skills before adoption, "
            "which is exactly what Phase-0 exists to do, and it is a direct counter to the "
            "self-improving-skill line (`@concepts/skill-misevolution.md`, "
            "`@concepts/vague-goal-self-evolution.md`). The silent-competence result is the sharper "
            "warning: **a high objective score says nothing about constraint adherence**, which is "
            "the K423 lesson arriving from a different direction. Pairs "
            "`@concepts/skill-vetting.md` / `@concepts/validation-ratchet-skill-evolution.md` / "
            "K409 meta-skills / K428 CLIFT. **No clone, no install.**"
        ),
        "snippet": (
            "Curated skills beat self-generated ones — the argument for our skill-audit discipline, in numbers."
        ),
    },
]


def yaml_list(items):
    return "\n".join(f"  - {x}" for x in items)


def write_source(e):
    body = f"""---
title: "{e['title']} (CCC k282 route)"
type: source
tags: [source, arxiv, k282, cross-wiki]
keywords: [{e['arxiv']}, k282]
related:
  - concepts/{e['concept']}.md
  - briefs/{BRIEF}
  - "{e['osint']}"
maturity: draft
read_status: skimming
cross-wiki-source: "{e['osint']}"
created: {DATE}
updated: {DATE}
---

## Relations

- `@concepts/{e['concept']}.md`
- `@briefs/{BRIEF}`
- `{e['osint']}` — cross-wiki canon (deep read lives there)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | {e['title']} |
| **arXiv** | {e['arxiv']} (2026-10) |
| **Canon** | `{e['osint']}` |
| **Routed by** | `@briefs/{BRIEF}` |

## Narrative

{e['narrative']}

## Snippets

> "{e['snippet']}" [Source: arXiv {e['arxiv']} via `{e['osint']}` (retrieved {DATE})]
"""
    (REPO / "wiki/sources" / f"{e['slug']}.md").write_text(body, encoding="utf-8")


def write_concept(e):
    c = e["concept"]
    body = f"""---
title: "{e['title']} (CCC k282 route)"
type: concept
tags: [concept, k282, cross-wiki]
keywords: [{e['arxiv']}, k282]
related:
  - sources/{e['slug']}.md
  - concepts/phase1-adopt-wire.md
  - briefs/{BRIEF}
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: {DATE}
updated: {DATE}
---

## Relations

- `@sources/{e['slug']}.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/{BRIEF}`

## Raw Concept

Routed from `@osint-wiki` via `@briefs/{BRIEF}` (arXiv {e['arxiv']}). Canon stays on OSINT.

## Narrative

{e['narrative']}

## Snippets

> "See source page for arXiv {e['arxiv']} locators." [Source: CCC k282 synthesis]
"""
    (REPO / "wiki/concepts" / f"{c}.md").write_text(body, encoding="utf-8")


def write_route_brief():
    p = REPO / "wiki/briefs" / BRIEF
    rel = [f"concepts/{e['concept']}.md" for e in ENTRIES] + [f"sources/{e['slug']}.md" for e in ENTRIES]
    p.write_text(
        f"""---
title: CCC — k282 inbound route from OSINT (agent-eval batch)
type: brief
tags: [brief, handoff, k282, cross-wiki-route]
keywords: [evoriskbench, kinetic-gate, hyperbrowsecomp, finskillsbench]
related:
{yaml_list(rel + ['concepts/phase1-adopt-wire.md'])}
maturity: draft
created: {DATE}
updated: {DATE}
---

## Target

CCC pages for the 4 papers routed by `briefs/2026-10-05_k282-ccc-agent-eval.md`.

## Summary

OSINT ingested four papers in its K282 batch that touch surfaces CCC owns. Canon stays on OSINT;
CCC holds the harness/eval takeaways. **No install, no clone.**

| Paper | CCC takeaway |
|-------|--------------|
| EvoRiskBench | Harness is second-order (5.41 pp vs model 54.37 pp) but it is the part we control |
| Kinetic gated evolution | Separation theorem formalises "evaluator not in population"; density result is a re-check trigger |
| HyperBrowseComp | 57.68% shared failure ⇒ bottleneck is the task type, not a model |
| FinSkillsBench | Curated skills +16.2 vs self-generated +0.5 — the audit argument, in numbers |
""",
        encoding="utf-8",
    )


def append_policy():
    path = REPO / ".cursor/rules/cemini-phase1-policy-wires.mdc"
    text = path.read_text(encoding="utf-8")
    if "k282 inbound route" in text:
        return
    block = """

## CCC k282 inbound route from OSINT (shared policy file)

Four papers routed from OSINT's K282 batch. Canon on OSINT; CCC holds the harness/eval reading.

## Harness security axis comparison (CCC k282)

- **Harness spread 5.41 pp vs model spread 54.37 pp.** The harness is second-order in absolute
  terms but it is **the factor we control**. Compare harness variants on a security axis, not only a
  capability axis. Runtime **`wont_wire`**.

## Gate separation theorem + skill density (CCC k282)

- **The evaluator must sit outside the population it judges** — now provable, not just practice.
  Fluctuation scaling is **flat at sparse density and −0.58 at tripled density**, so a gate validated
  at low skill density must be **re-checked as the skill count climbs** (CCC federated skills grew
  52 → 72 in one cycle). Runtime **`wont_wire`**.

## Browsing-agent eval bar (CCC k282)

- **57.68% of failures are shared across configurations**, so the bottleneck is the **task type**,
  not a model or harness. Know the ceiling before commissioning a browsing-agent eval. Runtime
  **`wont_wire`**.

## Curated vs self-generated skills (CCC k282)

- **Curated skills +16.2 pts; self-generated +0.5; tools alone +19.5; docs alone +5.6** — and
  subadditive. Curated beats self-generated by ~32×, which is the Phase-0 audit argument in numbers.
  Separately, **"silent competence"**: optimality 0.934 while **mandate adherence 0/33** — a high
  score says nothing about constraint adherence. Runtime **`wont_wire`**.
"""
    path.write_text(text.rstrip() + block + "\n", encoding="utf-8")


def patch_index():
    idx = REPO / "wiki/index.md"
    text = idx.read_text(encoding="utf-8")
    if ENTRIES[0]["slug"] in text:
        return
    anchor_c = "| [`assay-content-addressed-evidence-graphs`]"
    if anchor_c not in text:
        anchor_c = "| [`htn-planning-mcp-multi-server-coordination`]"
    for e in ENTRIES:
        row = (f"| [`{e['concept']}`](concepts/{e['concept']}.md) | draft | "
               f"{e['title'][:50]}… — {e['arxiv']} (k282 route) |")
        text = text.replace(anchor_c, row + "\n" + anchor_c, 1)
    anchor_s = "| [`arxiv-assay-content-addressed-evidence-graphs-2609.36170`]"
    if anchor_s not in text:
        anchor_s = "| [`arxiv-htn-planning-mcp-multi-server-coordination-2609.33731`]"
    for e in ENTRIES:
        row = (f"| [`{e['slug']}`](sources/{e['slug']}.md) | draft | "
               f"{e['title'][:55]}… — {e['arxiv']} (k282 route) |")
        text = text.replace(anchor_s, row + "\n" + anchor_s, 1)
    idx.write_text(text, encoding="utf-8")


def prepend_log():
    log = REPO / "wiki/log.md"
    entry = f"""## [{DATE}] route | k282 inbound from OSINT (agent-eval batch)

- **Source brief:** `briefs/2026-10-05_k282-ccc-agent-eval.md` (OSINT K282, 4 papers).
- **Pages written:** 4 sources + 4 concepts, cross-wiki canon on OSINT (`cross-wiki-source` set, so lint section 5 stays at zero).
- **Takeaways:** harness security spread 5.41 pp vs model 54.37 pp (K426-adjacent); gate separation theorem + density re-check trigger; browsing-agent **57.68% shared failure** ⇒ task-type bottleneck; curated skills **+16.2** vs self-generated **+0.5**.
- **Phase-1:** policy §k282 inbound route added. Runtime `wont_wire` on all four. No install, no clone.

"""
    t = log.read_text(encoding="utf-8")
    if "k282 inbound from OSINT" not in t:
        log.write_text(entry + t, encoding="utf-8")


def main():
    for e in ENTRIES:
        write_source(e)
        write_concept(e)
    write_route_brief()
    append_policy()
    patch_index()
    prepend_log()
    print("done k282 route")


if __name__ == "__main__":
    main()
