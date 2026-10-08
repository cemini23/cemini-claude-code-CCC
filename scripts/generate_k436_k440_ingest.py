#!/usr/bin/env python3
"""Generate K436–K440 wiki ingest artifacts (2026-10-08 daily sweep)."""
from __future__ import annotations
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DATE = "2026-10-08"
BRIEF = "2026-10-08_ccc-k436-k440-sip-ready.md"
EGRESS = "cemini-egress-fi:/opt/cemini-bulk/research/ccc"
RULE = "ccc-k436-k440-phase1-wires.mdc"
WAVE = "K436–K440"

def E(arxiv, concept, k, slug, title, verdict, no_clone, repo, narrative, snippet):
    return dict(arxiv=arxiv, concept=concept, k=k, slug=slug, title=title,
                verdict=verdict, no_clone=no_clone, repo=repo,
                narrative=narrative, snippet=snippet,
                pdf=[p.name for p in (REPO / "research to be indexed").glob(f"*{arxiv.replace('.', '.')}*")][0]
                    if list((REPO / "research to be indexed").glob(f"*{arxiv}*")) else f"arxiv-{arxiv}.pdf")

ENTRIES = [
 E("2610.09901", "read-versus-write-guardrails", 436,
   "arxiv-explorviz-chat-assistant-3d-software-viz-2610.09901",
   "A Chat Assistant for Software Exploration in a 3D Software Visualization",
   "ADOPT pattern (repo stale)", "explorviz-frontend", "explorviz/explorviz-frontend",
   "**The split is read versus write, and the write side is where it fails.** A chat assistant in a 3D "
   "software-visualization tool (ExplorViz, city metaphor), built on **CopilotKit** rather than MCP — "
   "an explicit architecture note: the visualization state lives in the React frontend, so a separate "
   "MCP server 'is not a good fit', and the assistant forwards prompts to a Node service that holds "
   "the API keys. Eleven-participant study. **Read actions were rated well:** generated summaries and "
   "explanations 'largely correct', highlighting entities and creating colour themes rated high "
   "usability. **Write actions were not:** 'open-ended chat-assisted software restructuring in the "
   "visualization showed mixed results', ratings for expectation alignment in editing 'notably "
   "lower', and the authors' own conclusion is that restructuring workflows 'require stronger "
   "guardrails' and better previews and undo. **CCC reading:** this is the same asymmetry CCC holds "
   "as a rule — reads are cheap to get wrong, writes are not — and here it is measured in a user "
   "study rather than asserted. The safety design that follows: bind agent actions to **well-defined "
   "existing entities** so they are confirmable and reversible (which this paper did, and which is "
   "why highlighting worked), and **do not expose open-ended structural mutation** as a first-class "
   "agent action. Also measured: **input tokens ran ~84× output**, so the cost sits in context, not "
   "generation (pairs K429/K425/`token-economics`). **Phase-0: `explorviz/explorviz-frontend` "
   "Apache-2.0 but last pushed 2022-03-20 — four years stale**, so the public tree is not the "
   "paper's build → no clone. Runtime `wont_wire`; concept `policy_wired`.",
   "open-ended chat-assisted software restructuring in the visualization showed mixed results. This "
   "suggests a need for stronger guardrails"),

 E("2610.10184", "formulation-versus-implementation-gap", 437,
   "arxiv-agentic-cp-production-scheduling-2610.10184",
   "Agentic AI-Assisted Modeling for Production Scheduling: Assessment in Constraint Programming",
   "ADOPT pattern", "pocket-agent", "DIR-LAB/pocket-agent",
   "**Formulation is within reach; implementation is the barrier.** General-purpose LLMs orchestrated "
   "as agents, with **no task-specific training**, asked to turn natural-language scheduling problems "
   "into **constraint-programming** models. An MCP server supplies **context-aware retrieval of solver "
   "documentation** to cut hallucination during implementation. Six industry problems (flow-shop, "
   "job-shop, flexible job-shop, resource-constrained warehouse), three LLMs, scored on modelling "
   "accuracy, execution success, latency, and tokens. **The headline is the split:** the model can "
   "*formulate* the problem, and fails at *implementing* it. A multi-agent workflow raises the share "
   "of scripts that **run correctly as generated from 14.8% (direct LLM call) to 59.3%**, reaching "
   "**80.6% on the four less complex problems**, while tightly coupled intralogistics models remain "
   "open. **CCC reading:** this is the 'the plan was fine, the execution failed' shape that CCC keeps "
   "meeting, measured. It pairs with K431 (prompt-delivered SOPs where the *process* never ran) and "
   "K437's own finding that **an MCP server serving the right documentation is the mitigation** — "
   "retrieval grounded in the solver's actual reference, not model recall. Two transferable moves: "
   "**score formulation separately from runnability**, and **feed the tool's own docs through MCP "
   "rather than trusting the model to remember the API**. **Phase-0: `DIR-LAB/pocket-agent` MIT**, "
   "5★, 5.2 MB, pushed 2026-02-20 — the agent framework used. No clone this wave. Runtime "
   "`wont_wire`; concept `policy_wired`.",
   "Formulation proves largely within reach of current LLMs, whereas implementation is the main "
   "barrier."),

 E("2610.10478", "decisive-step-base-model-probe", 438,
   "arxiv-decisive-step-base-model-probe-2610.10478",
   "Before They Can Solve: Predicting Post-Training Coding-Agent Performance from Base Models",
   "ADOPT eval-methodology", "decisive-step", "",
   "**Find the step where the repository flips, and probe the base model there.** NVIDIA. The problem: "
   "choosing which base checkpoint deserves an expensive agentic post-training round, before its "
   "agentic ability exists. End-to-end pass@K is unusable — untuned base models cannot drive a "
   "tool-use harness at all, so it reads near zero. Non-agentic coding benchmarks are worse: across "
   "ten base/post-trained pairs, **Spearman correlation with post-trained SWE-bench Verified pass@1 "
   "ranges from 0.830 (RepoBench XFirst) to −0.394 (HumanEval)** — a *negative* correlation, so the "
   "cheap proxy can rank backwards. The method: take a frontier model's **successful trajectory**, "
   "replay it, run the task's own tests after every code-changing step, and locate the **decisive "
   "step** — the first step whose cumulative patch flips the repo from failing to passing. That "
   "action is certified by the task's verifier, so it is a real action, not a gold patch. Three "
   "probes at that step: **Decisive-Action BPB** (probability mass on the certified action; ρ=0.964), "
   "**Patch MCQ** (distinguish it from verifier-rejected alternatives; ρ=0.903), and "
   "**prefix-conditioned pass@K** (sample continuations, accept any the tests pass; ρ=0.988 at K=16). "
   "**Two CCC-relevant pieces beyond the method.** (1) **A generic recipe**: any agentic benchmark "
   "with successful trajectories and a verifier can be converted into a base-model evaluation. "
   "(2) **A benchmark-validity finding**: the authors' **independent audit of 1,682 APTBench MCQs "
   "found questions whose designated correct option is incorrect or not uniquely correct** — a "
   "third instance of the K423 lesson, this time with the defect *inside the answer key*. Pairs K423 "
   "/ K428 / `verifiable-deterministic-agent-benchmarking` / K424. **No repo.** Runtime `wont_wire`; "
   "concept `policy_wired`.",
   "current evaluations are either too agentic to run or not agentic enough to predict downstream "
   "performance."),

 E("2610.10487", "compression-in-the-loop-tuning", 439,
   "arxiv-locaa-lossy-compression-tuning-2610.10487",
   "LOCAA: An Agentic System for Automated Lossy Compressor Tuning",
   "ADOPT pattern (MIT framework)", "pocket-agent", "DIR-LAB/pocket-agent",
   "**Search a black-box knob the conventional methods cannot search.** Scientific lossy compression "
   "is configured by an **error bound (EB)**, but users care about quality metrics (PSNR, SSIM) and "
   "runtime, and **the EB→quality mapping is nonlinear, non-monotonic, and staircase-shaped** "
   "depending on dataset and compressor — so binary search is unreliable and derivative-free methods "
   "are expensive. LOCAA is a **single agent** doing **compression-in-the-loop search** over MCP-exposed "
   "tools with persistent memory and **compressor-aware guidance**. Results: **1.98× fewer trials "
   "than binary search** and 5.03× fewer than FRaZ on fixed-ratio search; **61.5 → 17 trials (−72.4%)** "
   "under joint PSNR+SSIM constraints; **persistent memory cuts trials another 27.9%** across "
   "timesteps of the same field. Two ablations worth keeping: **compressor knowledge beats "
   "chain-of-thought** (ZFP 8.67 → 4.00 trials, 53.8%, because ZFP's staircase response breaks generic "
   "reasoning), and **the two are not additive** — CoT on top of knowledge helps SZ and *hurts* SZ3, "
   "ZFP, SPERR. Also: **88.4% of input tokens were served from prompt cache** (215.9K tokens/run, "
   "181.5K cached). **CCC reading:** this is a clean instance of a pattern CCC keeps collecting — an "
   "agent is *better than a fixed algorithm when the response surface is unknown* — and the "
   "efficiency came from **domain knowledge plus cache-friendly prompting**, not from reasoning "
   "alone. It pairs K425 (cost-aware evolution) and K429 (memory budgeting), and its 88.4% cache hit "
   "is the practical case for structuring prompts so the cache fires. **Phase-0: framework "
   "`DIR-LAB/pocket-agent` MIT**, 5★. No clone this wave. Runtime `wont_wire`; concept `policy_wired`.",
   "By combining agentic large language models with compression-in-the-loop evaluation, LOCAA "
   "efficiently searches compressor and error-bound configurations"),

 E("2610.10498", "value-of-information-experiment-selection", 440,
   "arxiv-embodiedrsi-value-of-information-experiments-2610.10498",
   "EmbodiedRSI: Active Continual Robot Learning Through Hypothesis-Guided Co-Evolution",
   "REFERENCE (cross-domain; pattern transfers)", "agentic_robotics", "Geeksongs/agentic_robotics",
   "**Spend the experiment on the hypothesis it can actually settle.** A self-evolving agentic harness "
   "for robot learning where the model stays frozen and the **harness** improves. The organising "
   "structure is a **Hypothesis Graph** holding competing code and skill hypotheses, and the "
   "selection rule is the transferable part: **Value-of-Information Experiment Selection** picks the "
   "physical experiment that can *distinguish between the live hypotheses* — rather than the "
   "experiment that seems most promising, which the paper argues is why prior self-evolving harnesses "
   "use robot trials inefficiently. Outcomes then drive **Code–Skill Co-Evolution**; a slow system "
   "builds **Hierarchical Memory**, and **Reward-Grounded Memory Learning** keeps the memories worth "
   "keeping for later fast-system improvement. RoboCasa365: **77.0% overall, 71.3% on "
   "Composite-Unseen, against 40.1% for the best baseline**; LIBERO-Pro 86.8%; zero-shot transfer to "
   "a real robot 71.3%. **CCC reading:** the harness shape is general even though the domain is not. "
   "**Choose the next action by what it would disambiguate, not by what looks best** is the same "
   "question K434 raised from the other side — K434 asked whether history predicts when a context "
   "operation will *hurt* and found little signal; VoI asks which operation would *tell you the most* "
   "and is an answer to that kind of failure. Also note the **memory that earns its place** framing: "
   "hierarchical memory with a reward-grounded retention rule, which is K429's budgeting question "
   "with a learning rule attached. Pairs K416/K419/K429/K434. **Phase-0: `Geeksongs/agentic_robotics` "
   "and `Einsia/EmbodiedRSI` both return no licence** → **no clone**. Runtime `wont_wire`; concept "
   "`policy_wired`.",
   "Value-of-Information Experiment Selection chooses physical experiments that can distinguish these "
   "hypotheses."),
]

def yl(items): return "\n".join(f"  - {x}" for x in items)

def write_source(e):
    k = e["k"]
    rel = [f"concepts/{e['concept']}.md", f"briefs/{BRIEF}"]
    rr = f"| **Repo** | `{e['repo']}` |\n" if e.get("repo") else ""
    (REPO/"wiki/sources"/f"{e['slug']}.md").write_text(f"""---
title: "{e['title']} (CCC K{k})"
type: source
tags: [source, arxiv, k{k}]
keywords: [{e['arxiv']}, k{k}]
related:
{yl(rel)}
maturity: draft
read_status: deep-read
created: {DATE}
updated: {DATE}
---

## Relations

{chr(10).join(f'- `@{r}`' for r in rel)}

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | {e['title']} |
| **arXiv** | {e['arxiv']} (2026-10) |
{rr}| **Retrieved** | {DATE} |

## Narrative

**Verdict: {e['verdict']}.**

{e['narrative']}

## Snippets

> "{e['snippet']}" [Source: arXiv {e['arxiv']} (retrieved {DATE})]

| **Location** | `{EGRESS}/{e['pdf']}` |
""", encoding="utf-8")

def write_concept(e):
    k, c = e["k"], e["concept"]
    (REPO/"wiki/concepts"/f"{c}.md").write_text(f"""---
title: "{e['title']} (CCC K{k})"
type: concept
tags: [concept, k{k}]
keywords: [{e['arxiv']}, k{k}]
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

K{k}: {e['verdict']} — arXiv {e['arxiv']}.

## Narrative

{e['narrative']}

## Snippets

> "See source page for arXiv {e['arxiv']} locators." [Source: CCC K{k} synthesis]
""", encoding="utf-8")

def write_phase0(e):
    k = e["k"]
    ck = [
        f'check "source" test -f "${{REPO_ROOT}}/wiki/sources/{e["slug"]}.md"',
        f'check "concept" test -f "${{REPO_ROOT}}/wiki/concepts/{e["concept"]}.md"',
        f'check "concept wired" grep -q "wire_status: policy_wired" "${{REPO_ROOT}}/wiki/concepts/{e["concept"]}.md"',
        f'check "policy K{k}" grep -q "K{k}" "${{REPO_ROOT}}/.cursor/rules/cemini-phase1-policy-wires.mdc"',
        f'check "ccc-rule K{k}" grep -q "K{k}" "${{REPO_ROOT}}/.cursor/rules/{RULE}"',
        f'check "no clone" test ! -d "${{REPO_ROOT}}/.local/adopts/{e["no_clone"]}"',
    ]
    p = REPO/"scripts"/f"adopt_k{k}_phase0.sh"
    p.write_text(f"""#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K{k} Phase-0 — ${{REPO_ROOT}}"
pass=0; fail=0; warn=0
check(){{ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }}
warn_note(){{ echo "  WARN  $1"; warn=$((warn+1)); }}
{chr(10).join(ck)}
warn_note "K{k} {e['verdict']}"
echo "Summary: ${{pass}} pass, ${{fail}} fail, ${{warn}} warn"
[[ "${{fail}}" -eq 0 ]]
""", encoding="utf-8")
    p.chmod(0o755)

def write_rule():
    rows = "\n".join(f"| K{e['k']} | {e['verdict']} | {e['concept'].replace('-',' ')[:42]} | `policy_wired` |" for e in ENTRIES)
    bl = "\n".join(f"- **K{e['k']}** {e['title'][:56]}… — **{e['verdict']}**: concept `{e['concept']}`." for e in ENTRIES)
    (REPO/".cursor/rules"/RULE).write_text(f"""---
description: CCC Phase-1 wires from K436–K440 harness wave (CCC-only — do NOT federation-sync)
alwaysApply: false
---

# CCC — K436–K440 Phase-1 wires

**Brief:** `docs/briefs/{DATE}_k436-k440-harness-wave.md` · SIP: `wiki/briefs/{BRIEF}`

**IDs:** Resolve by arXiv id / slug / file path — K# is a log batch label only.

{bl}

**Wires landed:**

| K | Verdict | Wire | wire_status |
|---|---|------|-------------|
{rows}

**Non-goals:** no federation sync; no PoCs; no clone of any repo this wave. K440's repos are both
**unlicensed**; K436's repo is **four years stale**.
""", encoding="utf-8")

def append_policy():
    p = REPO/".cursor/rules/cemini-phase1-policy-wires.mdc"; t = p.read_text(encoding="utf-8")
    if f"CCC wave {WAVE}" in t: return
    p.write_text(t.rstrip() + f"""

## CCC wave {WAVE} (shared policy file)

Read/write guardrail asymmetry (K436) + formulation-vs-implementation gap (K437) + decisive-step
base-model probe (K438) + compression-in-the-loop tuning (K439) + value-of-information experiment
selection (K440). **Zero clones.** CCC-only rule `{RULE}` — do **not** federation-sync.

## Read versus write guardrails (CCC K436)

- **Reads are cheap to get wrong; writes are not.** A user study of a 3D-viz chat assistant rated
  summaries and highlighting highly and rated **open-ended restructuring as mixed**, with the
  authors calling for **stronger guardrails, previews, and undo**. Design rule: bind agent actions to
  **well-defined existing entities** so they are confirmable and reversible; do not expose
  open-ended structural mutation as a first-class action. Input tokens ran **~84× output**. Runtime
  **`wont_wire`**.

## Formulation versus implementation (CCC K437)

- **The model can formulate the problem and fails at implementing it.** Multi-agent CP modelling
  raised runnable-as-generated scripts **14.8% → 59.3%** (80.6% on simpler problems). Mitigation:
  **serve the tool's own documentation through MCP** rather than trusting model recall. Score
  formulation separately from runnability (pairs K431). Runtime **`wont_wire`**.

## Decisive-step base-model probe (CCC K438)

- **Locate the step where the repo flips fail→pass and probe the model there.** Non-agentic coding
  benchmarks correlate with post-trained agentic performance from **+0.830 down to −0.394** — a
  cheap proxy can rank *backwards*. Probes: Decisive-Action BPB (ρ=0.964), Patch MCQ (ρ=0.903),
  prefix pass@K (ρ=0.988). Also: an **independent audit of 1,682 APTBench MCQs found defective
  answer keys** (third instance of the K423 lesson) (pairs K423/K428/K424). Runtime **`wont_wire`**.

## Compression-in-the-loop tuning (CCC K439)

- **An agent beats a fixed algorithm when the response surface is unknown.** Non-monotonic,
  staircase-shaped tuning: **1.98× fewer trials than binary search**, **61.5 → 17 (−72.4%)** under
  joint constraints, memory −27.9% more. **Compressor knowledge beat chain-of-thought** (ZFP 53.8%)
  and the two were **not additive**. **88.4% of input tokens came from prompt cache** (pairs K425/K429).
  Runtime **`wont_wire`**.

## Value-of-information experiment selection (CCC K440)

- **Pick the experiment that disambiguates, not the one that looks best.** Competing hypotheses in a
  **Hypothesis Graph**; **VoI selection** spends the trial on what can settle them. 77.0% vs 40.1%
  baseline. Memory with a **reward-grounded retention rule** — the budgeting question (K429) with a
  learning rule attached. Cross-domain REFERENCE (pairs K416/K419/K429/K434). Runtime **`wont_wire`**.
""", encoding="utf-8")

def write_briefs():
    (REPO/"docs/briefs"/f"{DATE}_k436-k440-harness-wave.md").write_text(f"""# {WAVE} harness wave — brief (CCC docs)

Date: {DATE} · SIP: `wiki/briefs/{BRIEF}`

## What changed

Five arXiv ingests from the 2026-10-08 sweep. **Zero clones.**

1. **K436** 3D-viz chat assistant — read/write guardrail asymmetry
2. **K437** Agentic CP modelling — formulation is easy, implementation is the barrier
3. **K438** Decisive-step probe — predicting post-training agentic performance
4. **K439** LOCAA — compression-in-the-loop tuning
5. **K440** EmbodiedRSI — value-of-information experiment selection (cross-domain)

## Phase-0 / Phase-1

- `adopt_k436`…`k440` — all exit 0 · `{RULE}` + policy §{WAVE}
- Phase-0: `explorviz/explorviz-frontend` **Apache-2.0 but last pushed 2022-03-20** (4 years stale) ·
  `DIR-LAB/pocket-agent` **MIT** · `Geeksongs/agentic_robotics` and `Einsia/EmbodiedRSI` **no licence**.

## Cross-wiki

- None. All five are harness/eval work CCC owns.
- **Minecraft / `dragon-rider-map` and Game Dev wiki — checked, no match.**

## Propose-only

- None.
""", encoding="utf-8")
    rel = [f"concepts/{e['concept']}.md" for e in ENTRIES] + [f"sources/{e['slug']}.md" for e in ENTRIES]
    (REPO/"wiki/briefs"/BRIEF).write_text(f"""---
title: CCC SIP-ready — {WAVE} full ingest
type: brief
handoff: true
tags: [brief, handoff, k436, k437, k438, k439, k440]
keywords: [read-write-guardrails, formulation-implementation, decisive-step, compression-tuning, value-of-information]
related:
{yl(rel + ['concepts/phase1-adopt-wire.md'])}
maturity: draft
created: {DATE}
updated: {DATE}
---

## Target

Full ingest of **5 NEW** inbox PDFs as **CCC {WAVE}**. Phase-0 + Phase-1, archive, lint, commit,
push, CI green.

## Inbox

| K | arXiv | Verdict |
|---|-------|---------|
| K436 | 2610.09901 | ADOPT pattern — read/write guardrails |
| K437 | 2610.10184 | ADOPT pattern — formulation vs implementation |
| K438 | 2610.10478 | ADOPT eval-methodology — decisive step |
| K439 | 2610.10487 | ADOPT pattern — compression tuning |
| K440 | 2610.10498 | REFERENCE (cross-domain) — VoI selection |
""", encoding="utf-8")

def patch_index():
    idx = REPO/"wiki/index.md"; t = idx.read_text(encoding="utf-8")
    if ENTRIES[0]["slug"] in t: return
    ac = "| [`assay-content-addressed-evidence-graphs`]"
    if ac not in t: ac = "| [`htn-planning-mcp-multi-server-coordination`]"
    for e in ENTRIES:
        row = f"| [`{e['concept']}`](concepts/{e['concept']}.md) | draft | {e['title'][:50]}… — {e['arxiv']} (K{e['k']}) |"
        t = t.replace(ac, row + "\n" + ac, 1)
    as_ = "| [`arxiv-assay-content-addressed-evidence-graphs-2609.36170`]"
    if as_ not in t: as_ = "| [`arxiv-htn-planning-mcp-multi-server-coordination-2609.33731`]"
    for e in ENTRIES:
        row = f"| [`{e['slug']}`](sources/{e['slug']}.md) | draft | {e['title'][:55]}… — {e['arxiv']} |"
        t = t.replace(as_, row + "\n" + as_, 1)
    sa = "| [`2026-10-01-daily`](sweeps/2026-10-01-daily.md)"
    if sa in t and "2026-10-08-daily" not in t:
        t = t.replace(sa, sa + "\n| [`2026-10-08-daily`](sweeps/2026-10-08-daily.md) | Daily digest — 5 papers (K436–K440 wave) |", 1)
    idx.write_text(t, encoding="utf-8")

def prepend_log():
    log = REPO/"wiki/log.md"
    entry = f"""## [{DATE}] ingest | {WAVE} harness wave (Oct 8 daily sweep)

- **Sources:** 2610.09901 3D-viz chat assistant, 2610.10184 agentic CP scheduling, 2610.10478 decisive-step probe, 2610.10487 LOCAA, 2610.10498 EmbodiedRSI.
- **Phase-0:** `explorviz-frontend` Apache-2.0 but **last pushed 2022-03-20** (4y stale); `DIR-LAB/pocket-agent` MIT; `Geeksongs/agentic_robotics` + `Einsia/EmbodiedRSI` **no licence**. Zero clones.
- **Phase-1:** adopt_k436…k440; `{RULE}`; policy §{WAVE}.
- **Also this session:** design-registry MCP Phase-0 (item 1) and Assay K406 closed (item 4).
- **Standouts:** K437's **14.8% → 59.3% runnable** formulation/implementation split; K438's **non-agentic benchmarks correlating as low as −0.394**; K439's **88.4% prompt-cache hit**.
- **Archive:** egress bulk ccc (5 PDFs). Inbox empty.

"""
    t = log.read_text(encoding="utf-8")
    if f"{WAVE} harness wave" not in t: log.write_text(entry + t, encoding="utf-8")

def patch_sweep():
    p = REPO/"wiki/sweeps/2026-10-08-daily.md"
    if not p.exists(): return
    t = p.read_text(encoding="utf-8")
    if "INGESTED" in t: return
    p.write_text(f"> **INGESTED {DATE} as {WAVE}** — see `wiki/log.md`.\n\n" + t, encoding="utf-8")

def main():
    for e in ENTRIES:
        write_source(e); write_concept(e); write_phase0(e)
    write_rule(); append_policy(); write_briefs()
    patch_index(); prepend_log(); patch_sweep()
    print(f"done {WAVE}")

if __name__ == "__main__":
    main()
