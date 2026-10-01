#!/usr/bin/env python3
"""Generate K411–K415 wiki ingest artifacts (2026-10-01 daily sweep) + K283 cross-route."""
from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DATE = "2026-10-01"
BRIEF = "2026-10-01_ccc-k411-k415-sip-ready.md"
EGRESS = "cemini-egress-fi:/opt/cemini-bulk/research/ccc"
RULE = "ccc-k411-k415-phase1-wires.mdc"
WAVE = "K411–K415"

ENTRIES = [
    {
        "arxiv": "2609.39544",
        "concept": "evolutionary-mcp-tool-interface-design",
        "k": 411,
        "narrative": (
            "**ROCQ-MCP-EVOLVE — grow the tool interface, do not design it by hand.** Agents reach "
            "proof assistants through an MCP server, and that interface sets what the agent receives "
            "and what each interaction costs. Today those interfaces are inherited from tools built "
            "for humans. This paper **evolves** one instead: a frontier model (Claude Fable 5) acts as "
            "**orchestrator**, proposing one new feature at a time; each mutation is evaluated by "
            "**smaller** models (Haiku 4.5, Sonnet 5 as testers) on a curated set and kept **only if it "
            "improves all three objectives** — accuracy, **cost per solve**, and wall time per solve. "
            "Starting from a server that exposes one tool (compile a file), the loop grows a full "
            "interface. On the miniF2F-Rocq held-out split it beats both the minimal baseline and an "
            "established MCP server across four models from two families. Sonnet: baseline .50 acc / "
            "$0.24 / 94 s → established .73 / $0.16 / 44 s → evolved **.82 / $0.11 / 36 s**. The "
            "evolved server is **ported to Lean** and improves cost and wall time there too, though it "
            "loses on solve rate to a Lean-specific server. Two things make this CCC-relevant: the "
            "**interface is the optimization target**, and the thing being optimized is **cost per "
            "solve**, not accuracy alone. The frontier model is not the solver — it is the tool "
            "designer for the weaker models that actually run. Pairs K402 MCP error surfaces / K311 "
            "lazy MCP / K409 meta-skills (Builder-Target) / K405 TokenCast + K320 cost accounting. "
            "**Phase-0: `LLM4Rocq/rocq-mcp-experiment` Apache-2.0**, 0★, 0 forks, pushed 2026-10-01 — "
            "brand new, no community vetting. Runtime **`wont_wire`**; concept **`policy_wired`**."
        ),
        "pdf": "arxiv-2609.39544-growing-an-agent-prover-interface-evolutionary-t.pdf",
        "slug": "arxiv-rocq-mcp-evolve-tool-interface-evolution-2609.39544",
        "title": "Growing an Agent/Prover Interface: Evolutionary Tool Design for Cost-Efficient Theorem Proving in Rocq and Lean",
        "verdict": "ADOPT pattern (Apache-2.0)",
        "no_clone": "rocq-mcp-experiment",
        "repo": "LLM4Rocq/rocq-mcp-experiment",
        "snippet": (
            "We propose an evolutionary method where a frontier model incrementally proposes new "
            "features and only keeps the ones that improve the overall performance of smaller models."
        ),
    },
    {
        "arxiv": "2609.40272",
        "concept": "claude-code-vs-agents-sdk-engineering-harness",
        "k": 412,
        "narrative": (
            "**PNNL runs a real engineering workflow on two agent harnesses and compares them.** The "
            "domain is power-system transmission planning; the tools are a **custom MCP server** "
            "exposing Siemens PSS®E functions (power flow, dynamic simulation, result extraction, "
            "model validation). Two implementation pathways were built on the same capability set: a "
            "**programmable OpenAI Agents SDK** harness, and the **Claude Code CLI** harness. Both use "
            "**reusable skills, subagents, MCP tools, data-repository connections, and local "
            "shell/Python execution** — the same four-part shape CCC ships. Both executed the "
            "representative study tasks successfully. Evaluation is by **task completion, output "
            "accuracy, and the need for human expert interventions** — that third metric is the one "
            "worth stealing: HITL burden measured as a first-class outcome, not as an afterthought. "
            "The paper's conclusion is a practice shift: agentic systems absorb routine simulation "
            "setup and result extraction, and engineers move to scenario design and interpretation. "
            "**This is the most directly CCC-relevant paper of the wave** — it is a head-to-head of "
            "Claude Code as a production engineering harness against a programmable SDK, in a domain "
            "with real correctness stakes. Pairs `@concepts/harness-as-eval-artifact.md` / K402 MCP "
            "error surfaces / `@concepts/subagent-orchestration.md` / "
            "`@concepts/skill-set-selection-under-budget.md`. **No repo surfaced.** Runtime "
            "**`wont_wire`**; concept **`policy_wired`**."
        ),
        "pdf": "arxiv-2609.40272-skill-based-ai-agents-for-power-system-studies.pdf",
        "slug": "arxiv-skill-based-agents-power-system-studies-2609.40272",
        "title": "Skill-Based AI Agents for Power-System Studies",
        "verdict": "ADOPT pattern (Claude Code harness eval)",
        "no_clone": "pnnl-power-agents",
        "repo": "",
        "snippet": (
            "Two implementation pathways built on a programmable OpenAI Agents software development "
            "kit (SDK) and a Claude Code command-line interface (CLI) were evaluated, both using "
            "reusable skills, subagents, MCP tools, data-repository connections, and local shell/Python "
            "execution."
        ),
    },
    {
        "arxiv": "2609.40306",
        "concept": "execution-contract-failure-attribution",
        "k": 413,
        "narrative": (
            "**DynaHarness — a command contract that records its own evidence.** A slow brain "
            "(Qwen3-VL-4B) proposes a capability and symbolic arguments; a **fast brain** grounds and "
            "monitors at 2 Hz, **refuses unresolved actions, substitutes capabilities, and requests "
            "replans**, while a 20 Hz controller executes. The invention is the **physical execution "
            "contract**: every robot-facing command is bounded by budget and lease, and every "
            "grounding, refusal, substitution, and completion is **recorded**. That record then does "
            "double duty — **offline failure attribution** localizes a fault to one of N ordered "
            "layers, and **paired regression checks** gate whether the resulting capability revision is "
            "admitted. The loop closes only when a revision passes regression; a later full-round "
            "confirmation **rejected** a candidate that had won on the targeted cells. On LIBERO-Pro: "
            "75.2% on 800 fresh states vs 17.5% for the frozen policy. **Cross-domain** (robotics), so "
            "REFERENCE — but three primitives transfer directly: a **bounded execution contract**, "
            "**attribution from recorded evidence rather than from episode outcome**, and "
            "**paired-regression admission** for any self-modification. That last one is the CCC "
            "lesson: the candidate that won on its target lost on the full round, and was correctly "
            "kept out. Pairs K406 Assay (mechanical gate) / K403 Tracekit (evidence ledger) / "
            "`test-time-world-model-validate-before-act` / K404 harness learning. **No code repo** — "
            "project page only. Runtime **`wont_wire`**; concept **`policy_wired`**."
        ),
        "pdf": "arxiv-2609.40306-dynaharness-a-dynamic-physical-harness-for-self.pdf",
        "slug": "arxiv-dynaharness-execution-contract-attribution-2609.40306",
        "title": "DynaHarness: A Dynamic Physical Harness for Self-Evolving Robot Agents",
        "verdict": "REFERENCE (cross-domain; 3 primitives transfer)",
        "no_clone": "dynaharness",
        "repo": "",
        "snippet": (
            "Failure attribution localizes faults in these records and directs targeted revisions of "
            "reusable capabilities or execution mechanisms. Paired regression checks govern admission "
            "or rejection, closing the self-evolution loop."
        ),
    },
    {
        "arxiv": "2609.40324",
        "concept": "verified-ledger-proof-orchestration",
        "k": 414,
        "narrative": (
            "**Cogentic — a research group, as a harness.** Google Research's multi-agent harness for "
            "open proof problems keeps **two separate stores**, and that separation is the design. The "
            "**record** holds every prover attempt with its verifier critiques and *why it failed*; "
            "the **verified ledger** holds only intermediate results that cleared adversarial "
            "verification, and **later rounds build only on the ledger**. An orchestrator assigns "
            "prover slots across distinct proof directions and spawns summarizers to condense history "
            "into per-prover **briefings**; an **advisor reads across rounds and tunes standing "
            "instructions**; verifiers attack each draft **alone and then alongside the others from "
            "the round**. Rounds repeat until a draft clears or the budget runs out. Budget is "
            "O(100)–O(1000) model calls per problem. It produced verified novel results on five open "
            "problems in online learning, auction theory, and mechanism design. **CCC relevance:** this "
            "is the K410 control/worker split with two additions worth wiring — a **promotion barrier** "
            "(failed attempts stay in the record and can never be built on) and **cross-round "
            "instruction tuning** by a separate advisor role. Pairs K410 agentic meta-reasoning / "
            "K406 Assay (claims vs verified claims) / K403 Tracekit / "
            "`@concepts/glasswing-deliberate-disagreement.md` (adversarial re-check) / "
            "`@concepts/subagent-orchestration.md`. **No code repo** (results site only). Runtime "
            "**`wont_wire`**; concept **`policy_wired`**."
        ),
        "pdf": "arxiv-2609.40324-cogentic-multi-agent-orchestration-for-automated.pdf",
        "slug": "arxiv-cogentic-verified-ledger-proof-orchestration-2609.40324",
        "title": "Cogentic: Multi-Agent Orchestration for Automated Proof Discovery",
        "verdict": "ADOPT pattern (Google Research)",
        "no_clone": "cogentic",
        "repo": "",
        "snippet": (
            "The record keeps track of prover attempts and their corresponding critiques from "
            "verifiers, and the ledger keeps track of verified intermediate lemmas that came out of "
            "proof attempts."
        ),
    },
    {
        "arxiv": "2609.40330",
        "concept": "instance-adaptive-harness-optimization",
        "k": 415,
        "narrative": (
            "**Turbo Harness — one global harness is not enough.** Harness optimization usually "
            "produces a single harness applied uniformly to every instance. This work recycles the "
            "artifacts a completed outer-loop search already produced, summarizes them into a "
            "**playbook** of both successful *and* unsuccessful editing strategies, and trains a small "
            "**harness editor** (Qwen3.5-9B) to patch the global harness **per instance**. The editor "
            "runs **once per instance**, so overhead is small, and the tailored harness often needs "
            "fewer execution steps from the much larger execution model. Gains are large: SWE-smith-MR "
            "50.7% → 64.0% with Claude Haiku 4.5, 70.7% → 88.0% with Gemini 3.7 Flash; top pass rate "
            "on Terminal-Bench 2.1. **The case studies carry the CCC lesson, and it is a sharp one:** "
            "the same harness knob has **opposite optima on different tasks**, and the editor's edits "
            "reach **executable loop code, not prompt wording** — it fires a verification gate at step "
            "6 instead of 8, relaxes an aggressive submit gate to buy a real fix-and-verify budget, "
            "and teaches an edit detector to also recognize append redirection. Critically: **forcing "
            "tool use globally is a documented playbook anti-pattern that regresses the whole suite by "
            "6.7%**, while being exactly right for one task. Pairs K404 harness learning / K409 "
            "meta-skills / K410 meta-reasoning / K169 harness-evolution baseline critique — note this "
            "is an *instance-adaptive* answer to that critique. **Phase-0: `Tyrion58/turbo-harness` "
            "MIT**, 3★, 0 forks, pushed 2026-09-30 — brand new. Runtime **`wont_wire`**; concept "
            "**`policy_wired`**."
        ),
        "pdf": "arxiv-2609.40330-turbo-harness-instance-adaptive-harness-optimiza.pdf",
        "slug": "arxiv-turbo-harness-instance-adaptive-2609.40330",
        "title": "Turbo Harness: Instance-Adaptive Harness Optimization",
        "verdict": "CONDITIONAL-GO (MIT)",
        "no_clone": "turbo-harness",
        "repo": "Tyrion58/turbo-harness",
        "snippet": (
            "The same control knob therefore has opposite optima on different tasks, which a single "
            "global harness cannot satisfy but instance-specific adaptation can."
        ),
    },
]

# K283 — inbound cross-wiki route from the SEO wiki (PrecogUI). No local PDF; no code.
K283 = {
    "arxiv": "2609.36923",
    "concept": "simulate-before-commit-experience-pool",
    "k": 283,
    "narrative": (
        "**PrecogUI — simulate before you commit.** Routed inbound from `@seo-wiki/` (SEO K283). A "
        "pre-cognitive GUI-agent architecture with three parts. A **Proactive Experience Pool (PEP)** "
        "caches recurring anomaly and success patterns as `state-action-result` tuples in dual memory. "
        "A **Proactive Simulation Executor (PSE)** learns to forecast the next symbolic UI layout "
        "given a candidate action, so it can **rank candidate actions by predicted reliability** and "
        "avoid anomalies before they happen. A **Pre-cognitive Execution Controller (PEC)** fuses "
        "priors and predictions, prioritizes foreseen anomalies, and closes the loop with error "
        "correction. Results: 79.2% SR low-interference / 52.7% high; 89.4% element-type accuracy. "
        "**CCC relevance is the discipline, not the domain:** rank candidate actions by predicted "
        "reliability and keep a pool of past failures so the same one is not repeated. That maps onto "
        "pre-flight checks, verify-before-publish gates, and failure memory — the same shape as "
        "`@concepts/test-time-world-model-validate-before-act.md` and K406 Assay's evidence gate. "
        "Pairs the failure-memory line and `@concepts/agent-completion-verification-gates.md`. "
        "**No code published** ('will be publicly available') → nothing to clone, no Phase-0. "
        "**Further implementation: none** (per the routing brief). Runtime **`wont_wire`**; concept "
        "**`policy_wired`**."
    ),
    "slug": "arxiv-precogui-pre-cognitive-simulation-2609.36923",
    "title": "PrecogUI: Pre-cognitive Simulation for Proactive GUI Agents",
    "verdict": "REFERENCE (cross-wiki steal; no code)",
    "no_clone": "precogui",
    "repo": "",
    "snippet": (
        "Proactive Simulation Executor (PSE) — learns to forecast the next symbolic UI layout given a "
        "candidate action, enabling early anomaly avoidance and ranking candidate actions by predicted "
        "reliability."
    ),
}


ALL = ENTRIES + [K283]


def yaml_list(items):
    return "\n".join(f"  - {x}" for x in items)


def write_source(e):
    k = e["k"]
    related = [f"concepts/{e['concept']}.md", f"briefs/{BRIEF}"]
    relations = [f"@concepts/{e['concept']}.md", f"@briefs/{BRIEF}"]
    if k == 283:
        related.insert(0, f"@seo-wiki/sources/arxiv-kang-2026-precogui-proactive-gui-agents-{e['arxiv']}-2026-09-30.md")
        relations.insert(0, f"@seo-wiki/sources/arxiv-kang-2026-precogui-proactive-gui-agents-{e['arxiv']}-2026-09-30.md — cross-wiki source")
    loc = (f"`{EGRESS}/{e['pdf']}`" if e.get("pdf")
           else "none — no PDF fetched; cross-wiki route from `@seo-wiki/`")
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
| **arXiv** | {e['arxiv']} (2026-09) |
{repo_row}| **Retrieved** | {DATE} |

## Narrative

**Verdict: {e['verdict']}.**

{e['narrative']}

## Snippets

> "{e['snippet']}" [Source: arXiv {e['arxiv']} (retrieved {DATE})]

| **Location** | {loc} |
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
        for e in ALL
    )
    bullets = "\n".join(
        f"- **K{e['k']}** {e['title'][:56]}… — **{e['verdict']}**: concept `{e['concept']}`."
        for e in ALL
    )
    text = f"""---
description: CCC Phase-1 wires from K411–K415 harness wave + K283 cross-route (CCC-only — do NOT federation-sync)
alwaysApply: false
---

# CCC — K411–K415 (+K283) Phase-1 wires

**Brief:** `docs/briefs/2026-10-01_k411-k415-harness-wave.md` · SIP: `wiki/briefs/{BRIEF}`

**IDs:** Resolve by arXiv id / slug / file path — K# is a log batch label only.

{bullets}

**Wires landed:**

| K | Verdict | Wire | wire_status |
|---|---|------|-------------|
{rows}

**Non-goals:** no federation sync; no PoCs; no clone of any repo this wave. K283 is a cross-wiki
steal from `@seo-wiki/` with no code and no further implementation.

**Propose-only:** rocq-mcp-experiment HITL clone (Apache-2.0, 0★) · turbo-harness HITL clone
(MIT, 3★) — both brand new, mature them before use.
"""
    (REPO / ".cursor/rules" / RULE).write_text(text, encoding="utf-8")


def append_policy():
    path = REPO / ".cursor/rules/cemini-phase1-policy-wires.mdc"
    text = path.read_text(encoding="utf-8")
    if f"CCC wave {WAVE}" in text:
        return
    block = f"""

## CCC wave {WAVE} + K283 (shared policy file)

ROCQ-MCP-EVOLVE tool-interface evolution (K411) + PNNL Claude Code vs Agents SDK engineering harness
(K412) + DynaHarness execution contract (K413) + Cogentic verified ledger (K414) + Turbo Harness
instance-adaptive optimization (K415) + PrecogUI simulate-before-commit (K283, cross-wiki). **Zero
clones.** CCC-only rule `{RULE}` — do **not** federation-sync.

## Evolutionary MCP tool interface design (CCC K411)

- **Evolve the tool interface; the frontier model designs tools for the smaller models that run.**
  Keep a mutation only if it improves **accuracy AND cost/solve AND wall time**. Interface is the
  optimization target, cost-per-solve is an objective (pairs K402/K311/K409/K405). Runtime
  **`wont_wire`**.

## Claude Code vs Agents SDK as engineering harness (CCC K412)

- **Measured HITL burden as a first-class eval metric** — count required human expert interventions
  alongside task completion and accuracy. Claude Code CLI is one of the two harnesses compared
  (pairs `harness-as-eval-artifact`). Runtime **`wont_wire`**.

## Execution contract + attribution (CCC K413)

- **Bound every command by budget and lease, record every grounding/refusal/completion**, then
  attribute failures from the record and gate revisions by **paired regression**. The rejected
  candidate had won on its target cells and lost on the full round (pairs K406/K403). Runtime
  **`wont_wire`**.

## Verified ledger + adversarial proof orchestration (CCC K414)

- **Two stores: attempts-with-critiques vs verified-only.** Later rounds build **only on the
  verified ledger** — a promotion barrier. A separate advisor tunes cross-round instructions (pairs
  K410/K406/K403). Runtime **`wont_wire`**.

## Instance-adaptive harness optimization (CCC K415)

- **One global harness is not optimal per instance.** Reuse the search archive as a playbook of
  successful *and* failed edits; a small editor patches the harness once per instance, reaching
  **executable loop code, not prompt wording**. Documented anti-pattern: forcing tool use globally
  regressed a whole suite 6.7% (pairs K404/K409/K410/K169). Runtime **`wont_wire`**.

## Simulate-before-commit experience pool (CCC K283, from SEO)

- **Rank candidate actions by predicted reliability; keep a failure pool so a known failure is not
  repeated.** Pre-flight + verify-before-publish discipline (pairs
  `test-time-world-model-validate-before-act`). No code. Runtime **`wont_wire`**.
"""
    path.write_text(text.rstrip() + block + "\n", encoding="utf-8")


def write_briefs():
    docs = REPO / "docs/briefs/2026-10-01_k411-k415-harness-wave.md"
    docs.write_text(
        f"""# {WAVE} harness wave — brief (CCC docs)

Date: {DATE} · SIP: `wiki/briefs/{BRIEF}`

## What changed

Five arXiv ingests from the 2026-10-01 sweep, plus one cross-wiki route from SEO (K283).
**Zero clones.**

1. **K411** ROCQ-MCP-EVOLVE — evolutionary MCP tool-interface design (Apache-2.0, 0★)
2. **K412** PNNL skill-based agents for power-system studies — Claude Code CLI vs OpenAI Agents SDK
3. **K413** DynaHarness — execution contract, failure attribution, paired-regression admission
4. **K414** Cogentic — verified ledger + adversarial proof orchestration (Google Research)
5. **K415** Turbo Harness — instance-adaptive harness optimization (MIT, 3★)
6. **K283** PrecogUI — simulate-before-commit experience pool (inbound from `@seo-wiki/`)

## Phase-0 / Phase-1

- `adopt_k411`…`k415` + `adopt_k283` — all exit 0
- `{RULE}` + policy §{WAVE}
- Phase-0 licenses: rocq-mcp-experiment **Apache-2.0** · turbo-harness **MIT**. No repo for K412,
  K413, K414, K283.

## Propose-only

- HITL clone of `LLM4Rocq/rocq-mcp-experiment` — Apache-2.0 but 0★, brand new
- HITL clone of `Tyrion58/turbo-harness` — MIT but 3★, brand new
- The K411 evolutionary-interface method is the reusable idea; the Rocq MCP server itself is not
  CCC's problem
""",
        encoding="utf-8",
    )
    sip = REPO / "wiki/briefs" / BRIEF
    entries = [f"concepts/{e['concept']}.md" for e in ALL]
    entries += [f"sources/{e['slug']}.md" for e in ALL]
    sip.write_text(
        f"""---
title: CCC SIP-ready — {WAVE} full ingest + K283
type: brief
tags: [brief, handoff, k283, k411, k412, k413, k414, k415]
keywords: [mcp-tool-evolution, claude-code-harness-eval, execution-contract, verified-ledger, instance-adaptive-harness, precogui]
related:
{yaml_list(entries + ['concepts/phase1-adopt-wire.md'])}
maturity: draft
created: {DATE}
updated: {DATE}
---

## Target

Full ingest of **5 NEW** inbox PDFs as **CCC {WAVE}**, plus the inbound **K283** cross-wiki route
from `@seo-wiki/`. Phase-0 + Phase-1, archive, lint, commit, push, CI green.

## Inbox

| K | arXiv | Verdict |
|---|-------|---------|
| K411 | 2609.39544 | ADOPT pattern — evolutionary MCP tool design |
| K412 | 2609.40272 | ADOPT pattern — Claude Code vs Agents SDK engineering harness |
| K413 | 2609.40306 | REFERENCE — DynaHarness execution contract |
| K414 | 2609.40324 | ADOPT pattern — Cogentic verified ledger |
| K415 | 2609.40330 | CONDITIONAL-GO (MIT) — Turbo Harness |
| K283 | 2609.36923 | REFERENCE — PrecogUI (cross-wiki, no code) |
""",
        encoding="utf-8",
    )


def patch_index():
    idx = REPO / "wiki/index.md"
    text = idx.read_text(encoding="utf-8")
    if ENTRIES[0]["slug"] in text:
        return
    anchor_c = "| [`assay-content-addressed-evidence-graphs`](concepts/assay-content-addressed-evidence-graphs.md)"
    if anchor_c not in text:
        anchor_c = "| [`htn-planning-mcp-multi-server-coordination`]"
    for e in ALL:
        row = (f"| [`{e['concept']}`](concepts/{e['concept']}.md) | draft | "
               f"{e['title'][:50]}… — {e['arxiv']} (K{e['k']}) |")
        text = text.replace(anchor_c, row + "\n" + anchor_c, 1)
    anchor_s = "| [`arxiv-assay-content-addressed-evidence-graphs-2609.36170`]"
    if anchor_s not in text:
        anchor_s = "| [`arxiv-htn-planning-mcp-multi-server-coordination-2609.33731`]"
    for e in ALL:
        row = (f"| [`{e['slug']}`](sources/{e['slug']}.md) | draft | "
               f"{e['title'][:55]}… — {e['arxiv']} |")
        text = text.replace(anchor_s, row + "\n" + anchor_s, 1)
    sweep_anchor = "| [`2026-09-30-daily`](sweeps/2026-09-30-daily.md) | Daily digest — 5 papers (K406–K410 wave) |"
    if sweep_anchor in text:
        text = text.replace(sweep_anchor, sweep_anchor +
            "\n| [`2026-10-01-daily`](sweeps/2026-10-01-daily.md) | Daily digest — 5 papers (K411–K415 wave) |", 1)
    idx.write_text(text, encoding="utf-8")


def prepend_log():
    log = REPO / "wiki/log.md"
    entry = f"""## [{DATE}] ingest | {WAVE} harness wave + K283 cross-route

- **Sources:** 2609.39544 ROCQ-MCP-EVOLVE, 2609.40272 PNNL power agents, 2609.40306 DynaHarness, 2609.40324 Cogentic, 2609.40330 Turbo Harness.
- **Inbound route:** K283 PrecogUI (2609.36923) from `@seo-wiki/` — steal only, no code, no further implementation.
- **Phase-0:** rocq-mcp-experiment Apache-2.0 (0★); turbo-harness MIT (3★). No repo for K412/K413/K414/K283.
- **Phase-1:** adopt_k411…k415 + adopt_k283; `{RULE}`; policy §{WAVE}. Zero clones.
- **Standouts:** K412 is a head-to-head of Claude Code CLI vs the OpenAI Agents SDK on a real engineering workflow, with HITL burden as a metric. K415 documents a global harness knob with opposite per-instance optima (forcing tool use regressed a suite 6.7%).
- **Archive:** egress bulk ccc (5 PDFs).

"""
    t = log.read_text(encoding="utf-8")
    if f"{WAVE} harness wave" not in t:
        log.write_text(entry + t, encoding="utf-8")


def patch_sweep():
    p = REPO / "wiki/sweeps/2026-10-01-daily.md"
    if not p.exists():
        return
    t = p.read_text(encoding="utf-8")
    if "INGESTED" in t:
        return
    p.write_text(f"> **INGESTED {DATE} as {WAVE}** — see `wiki/log.md`.\n\n" + t, encoding="utf-8")


def main():
    for e in ALL:
        write_source(e)
        write_concept(e)
        write_phase0(e)
    write_ccc_rule()
    append_policy()
    write_briefs()
    patch_index()
    prepend_log()
    patch_sweep()
    print(f"done {WAVE} + K283")


if __name__ == "__main__":
    main()
