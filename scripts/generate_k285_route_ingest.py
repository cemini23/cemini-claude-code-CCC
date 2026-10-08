#!/usr/bin/env python3
"""Fill CCC pages for the k285 inbound route (2026-10-08).

Source: briefs/2026-10-08_k285-ccc-harness-{coevolution,resilience}.md — CCC's own pipeline briefs.
Two of their four arXiv items (2610.10478, 2610.10498) already landed this session as K438/K440.
The remaining two plus the two feed items get pages here. Canon stays on OSINT.
"""
from __future__ import annotations
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DATE = "2026-10-08"
BRIEF = "2026-10-08_k285-ccc-route.md"
RULE = "ccc-k285-route-wires.mdc"

ITEMS = [
 dict(slug="arxiv-cotrace-harness-fingerprint-routing-2610.10426", concept="harness-fingerprint-trajectory-routing",
      title="CoTrace — a harness-tuned agent does not travel",
      arxiv="2610.10426",
      osint="@osint-wiki/sources/arxiv-2610.10426-cotrace-2026-10-08.md",
      body="""**The training value of a trajectory depends on which harness produced it.** Pooling search
trajectories across harnesses **disconnects policy training from the deployed runtime** — the model
learns from traces recorded under a scaffold it will never run in. CoTrace routes trajectories by a
**harness fingerprint** and alternates harness and policy promotion. Qwen3.5-9B on Tmax: **78 → 88
(SFT) → 90 (RL)**, at **30–50 trajectories per iteration** against 149–308 for pooled training — so
the fingerprint both improves the result and cuts the data by ~4×.

**The caveat is the finding, and the brief states it plainly: on Terminal-Bench 2.1 and SWE-bench
Lite the gains largely vanish under a foreign runtime. A harness-tuned agent does not travel.**

**CCC reading.** This is a first-class harness claim and it cuts against a comfortable assumption —
that an improvement learned inside one scaffold transfers to another. CCC documents a *federation* of
harnesses (Claude Code, Cursor, Codex, Grok, and the `/route` lane). If tuning is harness-local, then
**an improvement measured in one lane is not evidence for another**, and every cross-lane claim needs
the runtime held fixed or the transfer measured. It pairs directly with K431 (**Grounded TSR** —
score the process, not the outcome) and K438 (**non-agentic benchmarks correlating as low as
−0.394**): three independent results this month saying *the measuring instrument is part of the
result*. Pairs `@concepts/harness-as-eval-artifact.md` /
`@concepts/agentic-meta-reasoning-control-plane.md` / `@concepts/code-as-agent-harness.md`.

**Boundary:** FILE only. No install, no clone.""",
      snippet="on Terminal-Bench 2.1 and SWE-bench Lite the gains largely vanish under a foreign runtime"),

 dict(slug="arxiv-task-progress-distillation-stage-scored-2610.10332", concept="stage-scored-distillation",
      title="TPD — score the stage, do not imitate the trace",
      arxiv="2610.10332",
      osint="@osint-wiki/sources/arxiv-2610.10332-task-progress-distillation-2026-10-08.md",
      body="""**Label each action with a task *stage*, then score stage–action pairs instead of
generating long traces.** The distinction matters: imitating a trace teaches a model to reproduce
*someone's* sequence; scoring stage–action pairs teaches it which action is right *at this stage*,
which generalises across orderings. ALFWorld, Qwen3-1.7B: **at 200 demos, 67.7% against 48.0%
(+19.7 pp)**. A **shuffled-stage control drops success 55.2% → 37.6%** — so the stage label is doing
real work, not decoration. A deterministic harness executes the chosen action.

**CCC reading.** This is the same move as K428 (CLIFT: certify a reusable question bank rather than
imitate a trajectory) and K431 (Grounded TSR: score the process, not the outcome), arriving from a
third direction: **decompose the task into named stages and score at stage granularity.** Two
reusable pieces — **the shuffled control** (prove the label carries information by destroying it) and
**the deterministic executor** (the model chooses, the harness acts). Pairs
`@concepts/verifiable-deterministic-agent-benchmarking.md` /
`@concepts/progressive-skill-discovery-access-control.md` / K431 / K428.

**Boundary:** FILE only. No install, no clone.""",
      snippet="A shuffled-stage control drops success 55.2% → 37.6%."),

 dict(slug="newsletter-newman-llms-not-world-models-2026-10-07", concept="llms-are-not-world-models",
      title="LLMs are not world models — so guardrails are not the answer",
      arxiv="",
      osint="@osint-wiki/sources/newsletter-rss-pragmatic-engineer-2026-10-07-sam-newman-resilience.md",
      body="""**The sharpest external statement of CCC's own doctrine, plus a concrete incident, from Sam
Newman** (*Building Microservices*; *Building Resilient Distributed Systems*) on The Pragmatic
Engineer:

> "Why did the LLM delete my database? Well, because it has no concept of causality. They have no
> concept that if I do A, B happens … **LLMs are not world models.**"

Newman's conclusion follows from the mechanism rather than from the outcome: **because the model
cannot be taught causation by instruction, guardrails are not the right long-term solution.** No
amount of prompt-level prohibition instils a causal model.

**The incident that pairs with it:** **Opus 5.5 formatted a developer's C: drive under
`--dangerously-skip-permissions`** — the same flag this workspace's own operators are warned about.
That is not a hypothetical; it is the failure mode arriving.

**Other claims worth holding:** put **module boundaries first, then let the AI roam freely only
inside them**; **hedge vendors** (multi-model) and **replace LLM functions with deterministic code
where it is cheaper**; resist **"cognitive surrender"**; most outages come from **resource
exhaustion**.

**From the companion item (Stacklok / Mecatl, two Kubernetes creators):** today's harnesses are
desktop-bound because **the agent loop, execution, and session state share one process** with state
as **JSONL on disk**; Mecatl separates them so the loop is independent of client, model, provider,
state store, and execution environment. Their second claim is directly about this workspace's
routing: **semantic routing belongs in the harness, not the gateway — "there's just more context
there."**

**CCC reading.** Newman supplies the *mechanism* for a rule CCC already enforces on evidence:
**hard boundaries beat prompt instructions** (`cemini-invariants.mdc` — enforcement is external and
fail-closed; model self-arbitration is not a boundary). "It has no concept of causality" is a better
argument for that rule than "it sometimes fails", and the C:-drive incident is the cost of ignoring
it. Pairs `@concepts/agent-completion-verification-gates.md` / K421 (the model is not a security
boundary) / K431 (topologies where the process silently never ran) /
`@concepts/step-level-tool-guardrails.md`.

**Confidence:** the podcast quotes and the incident are `[TENTATIVE]` — single-source, not
independently verified.

**Boundary:** FILE only. No install, no clone, no `/route` swap.""",
      snippet="LLMs are not world models … guardrails are not the right long-term solution."),
]

def yl(x): return "\n".join(f"  - {i}" for i in x)

for it in ITEMS:
    src = f"wiki/sources/{it['slug']}.md"
    if Path(src).exists():
        print(f"  exists {it['slug']}"); continue
    arxiv_row = f"| **arXiv** | {it['arxiv']} (2026-10) |\n" if it["arxiv"] else "| **Type** | Feed item (not arXiv) |\n"
    Path(src).write_text(f"""---
title: "{it['title']} (CCC k285 route)"
type: source
tags: [source, k285, cross-wiki]
keywords: [{it['arxiv'] or 'feed'}, k285]
related:
  - concepts/{it['concept']}.md
  - briefs/{BRIEF}
  - "{it['osint']}"
maturity: draft
read_status: skimming
cross-wiki-source: "{it['osint']}"
created: {DATE}
updated: {DATE}
---

## Relations

- `@concepts/{it['concept']}.md`
- `@briefs/{BRIEF}`
- `{it['osint']}` — cross-wiki canon

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | {it['title']} |
{arxiv_row}| **Canon** | `{it['osint']}` |
| **Routed by** | `briefs/2026-10-08_k285-ccc-harness-coevolution.md` / `..._resilience.md` |

## Narrative

{it['body']}

## Snippets

> "{it['snippet']}" [Source: `{it['osint']}` via k285 (retrieved {DATE})]
""", encoding="utf-8")
    Path(f"wiki/concepts/{it['concept']}.md").write_text(f"""---
title: "{it['title']} (CCC k285 route)"
type: concept
tags: [concept, k285, cross-wiki]
keywords: [{it['arxiv'] or 'feed'}, k285]
related:
  - sources/{it['slug']}.md
  - concepts/phase1-adopt-wire.md
  - briefs/{BRIEF}
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: {DATE}
updated: {DATE}
---

## Relations

- `@sources/{it['slug']}.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/{BRIEF}`

## Raw Concept

Routed from `@osint-wiki` via the k285 briefs. Canon stays on OSINT.

## Narrative

{it['body']}

## Snippets

> "See source page for locators." [Source: CCC k285 synthesis]
""", encoding="utf-8")
    print(f"  wrote {it['concept']}")

rel = [f"concepts/{i['concept']}.md" for i in ITEMS] + [f"sources/{i['slug']}.md" for i in ITEMS]
Path(f"wiki/briefs/{BRIEF}").write_text(f"""---
title: CCC — k285 inbound route (harness co-evolution + resilience)
type: brief
handoff: true
tags: [brief, handoff, k285, cross-wiki-route]
keywords: [cotrace, harness-fingerprint, task-progress-distillation, world-model, guardrails]
related:
{yl(rel + ['concepts/phase1-adopt-wire.md'])}
maturity: draft
created: {DATE}
updated: {DATE}
---

## Target

CCC pages for the items routed by `briefs/2026-10-08_k285-ccc-harness-coevolution.md` and
`..._resilience.md`.

## Summary

Two of the four arXiv items in the k285 batch (**2610.10478**, **2610.10498**) already landed as
**K438** and **K440** this session. This brief covers the remainder.

| Item | CCC takeaway |
|------|--------------|
| CoTrace | **A harness-tuned agent does not travel** — improvements vanish under a foreign runtime |
| TPD | Score stage–action pairs, not traces; shuffled-stage control proves the label carries signal |
| Newman | **LLMs are not world models** → guardrails are not the answer; C:-drive incident |
| Mecatl | Separate the loop from execution and state; **semantic routing belongs in the harness** |

**No install, no clone, no `/route` swap.**
""", encoding="utf-8")

p = REPO/".cursor/rules/cemini-phase1-policy-wires.mdc"; t = p.read_text(encoding="utf-8")
if "k285 inbound route" not in t:
    p.write_text(t.rstrip() + """

## CCC k285 inbound route (shared policy file)

- **A harness-tuned agent does not travel** (CoTrace). Trajectory value depends on the producing
  harness; gains **vanish under a foreign runtime**. Do not treat an improvement measured in one lane
  (Claude Code / Cursor / Codex / `/route`) as evidence for another without holding the runtime fixed.
- **Score the stage, not the trace** (TPD). Stage–action scoring: **+19.7 pp** at 200 demos; a
  **shuffled-stage control drops 55.2% → 37.6%**, so the label carries signal. Deterministic
  executor acts.
- **LLMs are not world models, so guardrails are not the answer** (Sam Newman). The mechanism is
  "no concept of causality", which is a stronger argument for external enforcement than "it sometimes
  fails". Incident: **Opus 5.5 formatted a C: drive under `--dangerously-skip-permissions`.**
  Pairs `cemini-invariants.mdc` and K421.
- **Separate the loop from execution and state** (Stacklok / Mecatl); **semantic routing belongs in
  the harness, not the gateway** — relevant to `/route`. Runtime **`wont_wire`** on all four.
""", encoding="utf-8")
    print("  policy appended")

log = REPO/"wiki/log.md"; lt = log.read_text(encoding="utf-8")
if "k285 inbound route" not in lt:
    log.write_text(f"""## [{DATE}] route | k285 inbound briefs (harness co-evolution + resilience)

- **Source briefs:** `briefs/2026-10-08_k285-ccc-harness-coevolution.md`, `..._resilience.md` (CCC's own pipeline briefs).
- **Overlap:** two of their four arXiv items already landed this session — **2610.10478 = K438**, **2610.10498 = K440**.
- **Pages written:** CoTrace (harness fingerprint; **a harness-tuned agent does not travel**), TPD (stage-scored distillation), and the Newman/Mecatl resilience concept (**LLMs are not world models**; guardrails are not the answer; C:-drive incident under `--dangerously-skip-permissions`).
- **Phase-1:** policy §k285 added. Runtime `wont_wire`.

""" + lt, encoding="utf-8")
    print("  log appended")
print("done k285")
