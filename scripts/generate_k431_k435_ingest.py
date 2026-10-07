#!/usr/bin/env python3
"""Generate K431–K435 wiki ingest artifacts (2026-10-07 daily sweep)."""
from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DATE = "2026-10-07"
BRIEF = "2026-10-07_ccc-k431-k435-sip-ready.md"
EGRESS = "cemini-egress-fi:/opt/cemini-bulk/research/ccc"
RULE = "ccc-k431-k435-phase1-wires.mdc"
WAVE = "K431–K435"

ENTRIES = [
    {
        "arxiv": "2610.07817",
        "concept": "step-level-process-delivery",
        "k": 431,
        "narrative": (
            "**One Step at a Time — deliver the procedure, do not describe it.** AWS + Bundeswehr. "
            "The setting is regulated operational work: an SOP goes into the system prompt, the agent "
            "runs autonomously, and a final answer comes back. Two failures follow, and the second is "
            "the dangerous one. First, **behaviour is unpredictable** — a lightweight executor "
            "produced on average **20 distinct tool-call sequences per domain** (up to 44 on one "
            "procedure), so no supervisor can anticipate the path. Second, and worse, **the model can "
            "hallucinate the process itself**: on a KYC-style domain, **31–49% of correct answers "
            "were produced without executing a single prescribed verification tool** — including "
            "**48% of a frontier model's**. Standard accuracy counts every one as a success. The fix "
            "is to externalise process control: an MCP server **releases one step at a time**, the "
            "agent executes it, returns a structured `step_output`, and the server advances. The "
            "agent's autonomy is scoped to the current step; **it cannot see ahead**. Across 15,475 "
            "trials / 13 domains / 4 executors: process adherence **76–95% → 95–99%**, ungrounded "
            "answers **2.1–4.5% → 0.2–0.3%**, and a new metric — **Grounded TSR**, accuracy "
            "*conditioned on* process adherence — exposes what plain accuracy hides. The accuracy "
            "effect is capability-dependent and honestly reported: the **lightweight executor gains "
            "+6.5 pp** grounded accuracy (externalising the process removes a reconstruction burden "
            "it cannot carry), while capable executors **trade −2.5 to −4.7 pp raw accuracy for full "
            "process visibility** and branching domains that need look-ahead lose outright. Also "
            "measured: a **token tax of 2.1–2.9× without prompt caching**, which the paper notes "
            "would substantially reduce. **CCC relevance:** three transferable ideas — **ground the "
            "metric in the process, not the outcome**; **scope autonomy to the step** as a deliberate "
            "trade; and **a per-step structured record is simultaneously an audit trail and an "
            "optimisation substrate** (it repaired an SOP defect in under a minute). Pairs "
            "`@concepts/agent-completion-verification-gates.md` / K428 CLIFT / "
            "`@concepts/verifiable-deterministic-agent-benchmarking.md` / K409 / "
            "`@concepts/token-economics-and-prompt-caching.md`. **No repo.** Runtime **`wont_wire`**; "
            "concept **`policy_wired`**."
        ),
        "pdf": "arxiv-2610.07817-one-step-at-a-time-trading-llm-autonomy-for-proc.pdf",
        "slug": "arxiv-one-step-at-a-time-step-level-sop-2610.07817",
        "title": "One Step at a Time: Trading LLM Autonomy for Process Predictability",
        "verdict": "ADOPT pattern",
        "no_clone": "sop-mcp",
        "repo": "",
        "snippet": (
            "31–49% of an LLM agent's correct answers—including 48% of a frontier model's—are produced "
            "without executing a single one of the prescribed verification tools."
        ),
    },
    {
        "arxiv": "2610.07937",
        "concept": "two-level-retrieval-generation-eval",
        "k": 432,
        "narrative": (
            "**Evaluate retrieval and generation separately, or the score tells you nothing.** A "
            "vendor report (Redpine) on a literature-access MCP, and the methodological point "
            "transfers even though the product does not. A RAG pipeline **conflates two effects** — "
            "whether the right passage surfaced, and whether the model turned it into a grounded "
            "answer — and most evaluations report **one blended number**. A win on that number can "
            "come from better retrieval, better generation over similar evidence, or both, and the "
            "score alone does not say which. The report's structure is the contribution: **four "
            "evaluations across two levels** (retrieval vs generation) × **two benchmark provenances** "
            "(public vs expert-validated). The provenance axis exists because **public benchmarks "
            "risk saturation and memorisation** — a model can score well by having seen the answers. "
            "Headline: 94.4% correct claims with the tool vs 87.6% with no retrieval; 83.1% Recall@10 "
            "placing the gold paper in the top ten *stripped of any model reasoning* (the retrieval-"
            "only cell); blinded expert panel puts Precision@5 at 75.2% vs 39.8% for the incumbent. "
            "**CCC relevance is the separation discipline, not the product:** when CCC measures a "
            "retrieval-ish surface, **report the retrieval cell and the generation cell separately** "
            "and **state the benchmark's provenance**. This is the same lesson as K423 (representation) "
            "and K407 (judge variance) applied to RAG. **Caveat: this is a vendor report about the "
            "vendor's own product** — read the numbers as a company's own measurements, and note the "
            "release includes the expert-validated question set and reproduction instructions. "
            "**Phase-0: `redpine-ai/benchmarks` MIT**, 0★, 2.7 MB — the released benchmarks. Pairs "
            "`@concepts/deep-research-evaluation-prompt.md` / "
            "`@concepts/claim-centered-retrieval-with-provenance.md` / K426 MCP tool taxonomy. "
            "Runtime **`wont_wire`**; concept **`policy_wired`**."
        ),
        "pdf": "arxiv-2610.07937-leveraging-a-four-quadrant-approach-for-evaluati.pdf",
        "slug": "arxiv-four-quadrant-rag-eval-2610.07937",
        "title": "Leveraging a four-quadrant approach for evaluating Redpine Science",
        "verdict": "ADOPT eval-methodology (vendor report)",
        "no_clone": "redpine-benchmarks",
        "repo": "redpine-ai/benchmarks",
        "snippet": (
            "Most published evaluations report one blended score for both. A win on that score can "
            "come from better retrieval, a better-written answer drawn from similar evidence, or a "
            "mix of the two, and the number alone does not say which."
        ),
    },
    {
        "arxiv": "2610.08668",
        "concept": "semantic-action-cluster-watermarking",
        "k": 433,
        "narrative": (
            "**Watermark the action, not the string — and check for forgery, not only removal.** "
            "Behavioural watermarking embeds an owner identifier in an agent's **high-level action "
            "choices**, so provenance survives without touching output tokens. Prior schemes bind the "
            "signal to **raw strings** and break three ways, all measured here rather than asserted: "
            "(1) **AgentMark's own robustness test paraphrases only the observation** and bit-recovery "
            "collapses to **16.8%** — and its released script holds the per-step key fixed, so that "
            "experiment measures **distribution drift, not the key desynchronisation its own "
            "context-hash design admits**. (2) **Renaming a tool desynchronises decoding** even when "
            "the observation is untouched — the axis this paper measures and closes. (3) **Every "
            "prior agent watermark studies only removal; none asks whether an adversary can forge a "
            "trajectory that verifies as someone else's** — a question already answered "
            "*affirmatively* for text watermarks. SBW's answer: watermark over **semantic action "
            "clusters** under history conditioning, and replace the public-cluster bin with **keyed "
            "collision-resistant binning** whose fresh-bucket assignment is provably unpredictable in "
            "the random-oracle model. Results across five models (3B–14B, four vendors) and three "
            "encoders: on ToolBench detection under rewriting is **0.49–0.66 cluster-level vs "
            "0.05–0.17 exact-symbol** at 1% FPR; on ALFWorld **0.92–0.97 vs 0.00–0.01**. Keyed "
            "binning takes **adaptive forgery from 100% to the false-positive floor**. And the "
            "authors mark the boundary their guarantee does not cover: **chained replay remains "
            "0.76–0.98 across all five models, reported as open**. **CCC relevance:** this lands on "
            "the audit-integrity line — **an agent-writable trace is not evidence** (K394), and here "
            "the *positive* construction is given: bind provenance to something paraphrase-stable, "
            "and **test forgery, not just removal**. Pairs `@concepts/agent-trace-tampering-audit-gap.md` "
            "/ K403 Tracekit / K406 Assay / K427 trajectory audit. **No repo.** Runtime "
            "**`wont_wire`**; concept **`policy_wired`**."
        ),
        "pdf": "arxiv-2610.08668-semantic-behavioral-watermarking-paraphrase-robu.pdf",
        "slug": "arxiv-semantic-behavioral-watermarking-2610.08668",
        "title": "Semantic Behavioral Watermarking: Paraphrase-Robust and Forgery-Resistant Provenance for LLM Agents",
        "verdict": "ADOPT pattern",
        "no_clone": "sbw",
        "repo": "",
        "snippet": (
            "every prior agent watermark studies only removal: none asks whether an adversary can "
            "forge a trajectory that verifies as someone else's."
        ),
    },
    {
        "arxiv": "2610.08722",
        "concept": "compaction-harm-predictability",
        "k": 434,
        "narrative": (
            "**Does an agent's history tell you when compaction will hurt? Mostly no — and that is "
            "the finding.** Salesforce. Long-horizon harnesses compact on a **global rule, usually a "
            "token budget, blind to what the agent is doing**. The natural next step is to defer "
            "compaction where recent history says it is about to hurt. This paper tests that on "
            "TRACE's public corpus of **590 harness-triggered compaction boundaries**, where each "
            "boundary is **replayed from a re-executed prefix** under both the pre-compaction context "
            "and the summary, and the **burden of the next actions** (calls that error, or repeat a "
            "call already made) is recorded. That paired-replay design is what makes a per-boundary "
            "counterfactual possible at all — task success cannot say whether a given compaction "
            "hurt. **The result is a carefully-reported null with a real ceiling.** Pre-boundary "
            "history predicts post-compaction harm **only weakly**: the prespecified placement "
            "contrast is a **wide null** (−0.062 [−0.209, +0.079]), and the naive `has-written` "
            "label behind it turns out to measure **trajectory phase** — of 494 \"write-prefixed\" "
            "boundaries, **368 have no write beyond login or session calls**. The best trigger "
            "reaches **held-out AUROC 0.66 against a 0.72 same-boundary replicate**; the best frozen "
            "interpretable trigger **avoids 21% of harmful boundaries while keeping 84% of "
            "opportunities**, and **beats the random-rule expectation on count but not on burden "
            "mass** (a post hoc comparison). And the question you would actually want answered — "
            "**does any trigger beat a token-budget rule at matched retention? — cannot be evaluated "
            "on this release**, because token counts were not published. The paper says what corpora "
            "should ship to answer it. **CCC relevance is high and the direction is useful:** CCC "
            "holds a whole compaction line "
            "(`@concepts/truncate-only-long-horizon-compaction.md`, `context-engineering`, K387 KV "
            "working-set, K410 bounded controller state, K429 memory budgeting, K419 lossless "
            "memory) — and this is the **measurement that line has been missing**. The honest reading "
            "is *we do not yet know that history-based compaction timing beats a token budget*, and "
            "**a trajectory-phase proxy will look like signal if you do not control for it**. Pairs "
            "the full compaction cluster. **No repo** (TRACE is the source corpus). Runtime "
            "**`wont_wire`**; concept **`policy_wired`**."
        ),
        "pdf": "arxiv-2610.08722-does-an-agent-s-history-tell-you-when-compaction.pdf",
        "slug": "arxiv-compaction-harm-predictability-2610.08722",
        "title": "Does an Agent's History Tell You When Compaction Will Hurt? A Modest, Bounded Effect on the TRACE Paired-Replay Corpus",
        "verdict": "ADOPT eval-methodology (bounded null)",
        "no_clone": "trace-corpus",
        "repo": "",
        "snippet": (
            "Pre-boundary history predicts post-compaction harm only weakly."
        ),
    },
    {
        "arxiv": "2610.08761",
        "concept": "judge-policy-co-evolution",
        "k": 435,
        "narrative": (
            "**VeriFine — the judge is not fixed infrastructure; it is a co-evolving component.** "
            "NVIDIA. The premise is precise: **self-improving policies continually expose new "
            "failure patterns, which changes what their judges must be able to verify.** A **static "
            "judge becomes the bottleneck** as the policy improves — once the policy approaches the "
            "judge's effective verification boundary, feedback degrades into **reward hacking, "
            "distribution shift, and outright performance loss**. Meanwhile the training data goes "
            "stale: as earlier scenarios get solved, the distribution fills with well-solved samples "
            "and the learning signal thins. VeriFine answers with **two coupled loops**: a **Policy "
            "Improvement Loop** uses a **reference-free rubric judge** to diagnose recurring failures, "
            "build an **adaptive curriculum**, and optimise the policy; when progress plateaus, a "
            "**Judge Improvement Loop** activates and **selectively queries human guidance on "
            "informative failure cases**, refining the judge through **coactive calibration** — "
            "humans and agents resolve disagreements and converge, **human as participant rather "
            "than infallible oracle**. The revised judge then drives the next round of data selection "
            "and policy optimisation. Concrete protocol: boundary checks every 150 steps; rubric "
            "revision **keeps the dimensions and changes sub-rubrics and examples**; revisions "
            "accepted on Pearson/MAE; human review requested when average correlation improvement "
            "stays under 0.2 for 10+ iterations. Demonstrated on driving and robot navigation under "
            "RL and SFT. **CCC relevance:** this is the strongest answer yet to the *who grades the "
            "grader* problem, and it is the **constructive counterpart to K428 CLIFT** — CLIFT makes "
            "the verifier cheap and transferable and *frozen*; VeriFine says a frozen judge "
            "eventually throttles the system and **the verifier must co-evolve, with a small, "
            "targeted human channel** rather than a broad one. It is the *selective* human channel "
            "that makes this affordable. Pairs K424 (no LLM judge) / K423 (representation) "
            "/ `@concepts/validation-ratchet-skill-evolution.md` / "
            "`@concepts/agent-rubrics-self-correction.md` / K416 YouRA. **No repo.** Runtime "
            "**`wont_wire`**; concept **`policy_wired`**."
        ),
        "pdf": "arxiv-2610.08761-verifine-scaling-verification-for-self-improveme.pdf",
        "slug": "arxiv-verifine-judge-policy-co-evolution-2610.08761",
        "title": "VeriFine: Scaling Verification for Self-Improvement in Embodied Reasoning",
        "verdict": "ADOPT pattern",
        "no_clone": "verifine",
        "repo": "",
        "snippet": (
            "Self-improving policies continually expose new failure patterns, changing what their "
            "judges must be able to verify."
        ),
    },
]


def yaml_list(items):
    return "\n".join(f"  - {x}" for x in items)


def write_source(e):
    k = e["k"]
    related = [f"concepts/{e['concept']}.md", f"briefs/{BRIEF}"]
    relations = [f"@concepts/{e['concept']}.md", f"@briefs/{BRIEF}"]
    repo_row = f"| **Repo** | `{e['repo']}` |\n" if e.get("repo") else ""
    body = f"""---
title: "{e['title']} (CCC K{k})"
type: source
tags: [source, arxiv, k{k}]
keywords: [{e['arxiv']}, k{k}]
related:
{yaml_list(related)}
maturity: draft
read_status: deep-read
created: {DATE}
updated: {DATE}
---

## Relations

{chr(10).join(f'- `{r}`' for r in relations)}

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | {e['title']} |
| **arXiv** | {e['arxiv']} (2026-10) |
{repo_row}| **Retrieved** | {DATE} |

## Narrative

**Verdict: {e['verdict']}.**

{e['narrative']}

## Snippets

> "{e['snippet']}" [Source: arXiv {e['arxiv']} (retrieved {DATE})]

| **Location** | `{EGRESS}/{e['pdf']}` |
"""
    (REPO / "wiki/sources" / f"{e['slug']}.md").write_text(body, encoding="utf-8")


def write_concept(e):
    k, c = e["k"], e["concept"]
    body = f"""---
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
"""
    (REPO / "wiki/concepts" / f"{c}.md").write_text(body, encoding="utf-8")


def write_phase0(e):
    k = e["k"]
    checks = [
        f'check "source" test -f "${{REPO_ROOT}}/wiki/sources/{e["slug"]}.md"',
        f'check "concept" test -f "${{REPO_ROOT}}/wiki/concepts/{e["concept"]}.md"',
        f'check "concept wired" grep -q "wire_status: policy_wired" "${{REPO_ROOT}}/wiki/concepts/{e["concept"]}.md"',
        f'check "policy K{k}" grep -q "K{k}" "${{REPO_ROOT}}/.cursor/rules/cemini-phase1-policy-wires.mdc"',
        f'check "ccc-rule K{k}" grep -q "K{k}" "${{REPO_ROOT}}/.cursor/rules/{RULE}"',
        f'check "no clone" test ! -d "${{REPO_ROOT}}/.local/adopts/{e["no_clone"]}"',
    ]
    script = f"""#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K{k} Phase-0 — ${{REPO_ROOT}}"
pass=0; fail=0; warn=0
check(){{ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }}
warn_note(){{ echo "  WARN  $1"; warn=$((warn+1)); }}
{chr(10).join(checks)}
warn_note "K{k} {e['verdict']}"
echo "Summary: ${{pass}} pass, ${{fail}} fail, ${{warn}} warn"
[[ "${{fail}}" -eq 0 ]]
"""
    p = REPO / "scripts" / f"adopt_k{k}_phase0.sh"
    p.write_text(script, encoding="utf-8")
    p.chmod(0o755)


def write_ccc_rule():
    rows = "\n".join(
        f"| K{e['k']} | {e['verdict']} | {e['concept'].replace('-', ' ')[:42]} | `policy_wired` |"
        for e in ENTRIES
    )
    bullets = "\n".join(
        f"- **K{e['k']}** {e['title'][:56]}… — **{e['verdict']}**: concept `{e['concept']}`."
        for e in ENTRIES
    )
    text = f"""---
description: CCC Phase-1 wires from K431–K435 harness wave (CCC-only — do NOT federation-sync)
alwaysApply: false
---

# CCC — K431–K435 Phase-1 wires

**Brief:** `docs/briefs/{DATE}_k431-k435-harness-wave.md` · SIP: `wiki/briefs/{BRIEF}`

**IDs:** Resolve by arXiv id / slug / file path — K# is a log batch label only.

{bullets}

**Wires landed:**

| K | Verdict | Wire | wire_status |
|---|---|------|-------------|
{rows}

**Non-goals:** no federation sync; no PoCs; no clone of any repo this wave.

**Read with care:** K432 is a **vendor report about the vendor's own product**. K434 is a
**bounded null** — do not read it as evidence that history-based compaction timing works.
"""
    (REPO / ".cursor/rules" / RULE).write_text(text, encoding="utf-8")


def append_policy():
    path = REPO / ".cursor/rules/cemini-phase1-policy-wires.mdc"
    text = path.read_text(encoding="utf-8")
    if f"CCC wave {WAVE}" in text:
        return
    block = f"""

## CCC wave {WAVE} (shared policy file)

Step-level process delivery (K431) + two-level retrieval/generation eval (K432) + semantic action
watermarking (K433) + compaction-harm predictability (K434) + judge/policy co-evolution (K435).
**Zero clones.** CCC-only rule `{RULE}` — do **not** federation-sync.

## Step-level process delivery (CCC K431)

- **Deliver the procedure, do not describe it.** Under prompt-delivered SOPs, **31–49% of correct
  answers (48% for a frontier model) never executed a single prescribed tool** — and plain accuracy
  counts them all as successes. Serve one step at a time over MCP; scope autonomy to the step.
  Adherence 76–95% → 95–99%; ungrounded 2.1–4.5% → 0.2–0.3%. Use **Grounded TSR** (accuracy
  conditioned on adherence). Small executors gain (+6.5 pp), capable ones trade −2.5 to −4.7 pp raw
  for visibility. **Token tax 2.1–2.9× without prompt caching** (pairs K428/K409/`token-economics`).
  Runtime **`wont_wire`**.

## Two-level retrieval/generation eval (CCC K432)

- **Report the retrieval cell and the generation cell separately**, or the blended score cannot say
  which improved. **State the benchmark's provenance** — public benchmarks risk saturation and
  memorisation; complement with expert-validated sets. **Caveat: vendor report about its own
  product** (pairs `deep-research-evaluation-prompt`/`claim-centered-retrieval-with-provenance`).
  Runtime **`wont_wire`**.

## Semantic action-cluster watermarking (CCC K433)

- **Bind provenance to paraphrase-stable semantics, and test forgery, not only removal.** Renaming a
  tool desynchronises exact-symbol watermarks even when the observation is untouched. Cluster-level
  detection **0.49–0.66 vs 0.05–0.17** (ToolBench) and **0.92–0.97 vs 0.00–0.01** (ALFWorld). Keyed
  binning takes **adaptive forgery from 100% to the FPR floor**. **Open boundary: chained replay
  remains 0.76–0.98** (pairs `agent-trace-tampering-audit-gap`/K403/K406). Runtime **`wont_wire`**.

## Compaction-harm predictability (CCC K434)

- **We do not yet know that history-based compaction timing beats a token budget.** On TRACE's 590
  paired-replay boundaries, pre-boundary history predicts harm **only weakly**; the prespecified
  contrast is a **wide null**; the `has-written` label actually measures **trajectory phase** (368 of
  494 "write-prefixed" boundaries have no real write). Best trigger **AUROC 0.66 vs a 0.72
  replicate**; beats random on **count but not burden mass**; **cannot be compared to a token-budget
  rule on this release**. **Do not let a phase proxy read as signal** (pairs the whole compaction
  cluster). Runtime **`wont_wire`**.

## Judge/policy co-evolution (CCC K435)

- **A fixed judge becomes the bottleneck as the policy improves** — reward hacking, distribution
  shift, degradation. Co-evolve: a policy loop with a **reference-free rubric judge** plus a judge
  loop that **selectively queries humans on informative failures** (coactive calibration; human as
  participant, not oracle). Keep rubric **dimensions** fixed, revise **sub-rubrics and examples**.
  Constructive counterpart to K428 (which freezes the verifier) (pairs K424/K423/K416). Runtime
  **`wont_wire`**.
"""
    path.write_text(text.rstrip() + block + "\n", encoding="utf-8")


def write_briefs():
    docs = REPO / "docs/briefs/2026-10-07_k431-k435-harness-wave.md"
    docs.write_text(
        f"""# {WAVE} harness wave — brief (CCC docs)

Date: {DATE} · SIP: `wiki/briefs/{BRIEF}`

## What changed

Five arXiv ingests from the 2026-10-07 sweep. **Zero clones.**

1. **K431** One Step at a Time — step-level SOP delivery; Grounded TSR
2. **K432** Four-quadrant RAG eval (vendor report — Redpine)
3. **K433** Semantic behavioral watermarking — paraphrase-robust, forgery-resistant
4. **K434** Compaction-harm predictability — a bounded null
5. **K435** VeriFine — judge/policy co-evolution

## Phase-0 / Phase-1

- `adopt_k431`…`k435` — all exit 0
- `{RULE}` + policy §{WAVE}
- Phase-0: `redpine-ai/benchmarks` **MIT** (K432's released benchmark). No repo for
  K431/K433/K434/K435.

## Read with care

- **K432 is a vendor report about the vendor's own product.** The methodological point
  (separate retrieval from generation; vary benchmark provenance) transfers; the numbers are the
  company's own.
- **K434 is a bounded null, not a positive result.** It does *not* show history-based compaction
  timing works.

## Cross-wiki

- None. All five are harness/eval/verification work CCC owns.
- **Minecraft / `dragon-rider-map` and Game Dev wiki — checked, no match.**

## Propose-only

- None.
""",
        encoding="utf-8",
    )
    sip = REPO / "wiki/briefs" / BRIEF
    rel = [f"concepts/{e['concept']}.md" for e in ENTRIES] + [f"sources/{e['slug']}.md" for e in ENTRIES]
    sip.write_text(
        f"""---
title: CCC SIP-ready — {WAVE} full ingest
type: brief
handoff: true
tags: [brief, handoff, k431, k432, k433, k434, k435]
keywords: [step-level-sop, rag-eval, watermarking, compaction, judge-co-evolution]
related:
{yaml_list(rel + ['concepts/phase1-adopt-wire.md'])}
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
| K431 | 2610.07817 | ADOPT pattern — step-level SOP delivery |
| K432 | 2610.07937 | ADOPT eval-methodology (vendor report) |
| K433 | 2610.08668 | ADOPT pattern — semantic watermarking |
| K434 | 2610.08722 | ADOPT eval-methodology — bounded null |
| K435 | 2610.08761 | ADOPT pattern — judge/policy co-evolution |
""",
        encoding="utf-8",
    )


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
               f"{e['title'][:50]}… — {e['arxiv']} (K{e['k']}) |")
        text = text.replace(anchor_c, row + "\n" + anchor_c, 1)
    anchor_s = "| [`arxiv-assay-content-addressed-evidence-graphs-2609.36170`]"
    if anchor_s not in text:
        anchor_s = "| [`arxiv-htn-planning-mcp-multi-server-coordination-2609.33731`]"
    for e in ENTRIES:
        row = (f"| [`{e['slug']}`](sources/{e['slug']}.md) | draft | "
               f"{e['title'][:55]}… — {e['arxiv']} |")
        text = text.replace(anchor_s, row + "\n" + anchor_s, 1)
    sa = "| [`2026-10-01-daily`](sweeps/2026-10-01-daily.md)"
    if sa in text and "2026-10-07-daily" not in text:
        text = text.replace(sa, sa +
            "\n| [`2026-10-07-daily`](sweeps/2026-10-07-daily.md) | Daily digest — 5 papers (K431–K435 wave) |", 1)
    idx.write_text(text, encoding="utf-8")


def prepend_log():
    log = REPO / "wiki/log.md"
    entry = f"""## [{DATE}] ingest | {WAVE} harness wave (Oct 7 daily sweep)

- **Sources:** 2610.07817 step-level SOP, 2610.07937 four-quadrant RAG eval, 2610.08668 semantic watermarking, 2610.08722 compaction predictability, 2610.08761 VeriFine.
- **Phase-0:** `redpine-ai/benchmarks` **MIT** (K432 released benchmark). No repo for K431/K433/K434/K435.
- **Phase-1:** adopt_k431…k435; `{RULE}`; policy §{WAVE}. Zero clones.
- **Read with care:** K432 is a **vendor report about its own product**; K434 is a **bounded null**, not evidence that history-based compaction timing works.
- **Standouts:** K431's finding that **31–49% of correct answers never ran the prescribed tools** under prompt-delivered SOPs; K435's argument that **a fixed judge becomes the bottleneck** as the policy improves.
- **Cross-wiki:** none. Minecraft + Game Dev checked, no match.
- **Archive:** egress bulk ccc (5 PDFs). Inbox empty.

"""
    t = log.read_text(encoding="utf-8")
    if f"{WAVE} harness wave" not in t:
        log.write_text(entry + t, encoding="utf-8")


def patch_sweep():
    p = REPO / "wiki/sweeps/2026-10-07-daily.md"
    if not p.exists():
        return
    t = p.read_text(encoding="utf-8")
    if "INGESTED" in t:
        return
    p.write_text(f"> **INGESTED {DATE} as {WAVE}** — see `wiki/log.md`.\n\n" + t, encoding="utf-8")


def main():
    for e in ENTRIES:
        write_source(e)
        write_concept(e)
        write_phase0(e)
    write_ccc_rule()
    append_policy()
    write_briefs()
    patch_index()
    prepend_log()
    patch_sweep()
    print(f"done {WAVE}")


if __name__ == "__main__":
    main()
