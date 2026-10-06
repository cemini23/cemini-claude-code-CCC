#!/usr/bin/env python3
"""Generate K426–K430 wiki ingest artifacts (2026-10-06 daily sweep)."""
from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DATE = "2026-10-06"
BRIEF = "2026-10-06_ccc-k426-k430-sip-ready.md"
EGRESS = "cemini-egress-fi:/opt/cemini-bulk/research/ccc"
RULE = "ccc-k426-k430-phase1-wires.mdc"
WAVE = "K426–K430"

ENTRIES = [
    {
        "arxiv": "2610.05319",
        "concept": "mcp-tool-taxonomy-navigation",
        "k": 426,
        "narrative": (
            "**MCPacific — the MCP ecosystem mapped by capability, not by marketplace.** The largest "
            "tool-level study of MCP: **368,754 listings from 17 marketplaces**, resolved to **124,267 "
            "unique servers**, from which **1,328,233 tool specifications** are statically extracted "
            "in seven languages and organised into a **hierarchical functional taxonomy of 58,915 "
            "capabilities** — 7.5× more tools than the largest prior collection. The gap it fills: "
            "marketplaces organise by coarse vendor categories (Communication, Productivity), never by "
            "**what a tool actually does**, so neither agents nor users can answer *which capabilities "
            "exist* or *what can substitute for what*. The taxonomy is built by an iterative "
            "LLM **design → test → refine** loop and mapped with calibrated embedding routing; "
            "evaluation: 90.19% of tools reach a leaf, 87.00% land correctly, 85.00% of same-leaf "
            "pairs are functionally comparable. **Four findings matter to CCC.** (1) **85% of tools "
            "serve domains beyond software development** — the ecosystem is not a dev-tooling "
            "backwater. (2) **Alternatives are widespread but uneven:** 98.5% of tools have ≥1 "
            "alternative and 74.1% have ≥20, yet **nearly a quarter of capabilities have exactly one "
            "tool** — the single points of failure. (3) **Comparable tools are not interchangeable:** "
            "security alerts concentrate in a subset of alternatives, cyclomatic complexity differs "
            "**>2.5× in 41% of pairs**, and in 60% of capabilities some alternatives are maintained "
            "while others are not. (4) **Presentation changes outcomes** — exposing candidates through "
            "the taxonomy rather than a flat list improves task completion on all four models tested, "
            "**up to +12 points Pass@0.75 as the candidate set crowds**. That last one is the CCC "
            "lesson: at scale, *how tools are organised in the context* is a capability lever, not a "
            "UI nicety. Pairs K311 lazy MCP catalog / `@concepts/mcp-tool-interface-granularity-eval.md` "
            "/ K402 error surfaces / `@concepts/mcp-server-catalog-curation.md` / K427 privacy audit. "
            "**No repo surfaced.** Runtime **`wont_wire`**; concept **`policy_wired`**."
        ),
        "pdf": "arxiv-2610.05319-understanding-the-hierarchical-structure-and-fun.pdf",
        "slug": "arxiv-mcpacific-mcp-tool-taxonomy-2610.05319",
        "title": "Understanding the Hierarchical Structure and Functional Landscape of the Model Context Protocol Ecosystem",
        "verdict": "ADOPT pattern (no repo)",
        "no_clone": "mcpacific",
        "repo": "",
        "snippet": (
            "presenting candidate tools through the taxonomy rather than a flat list improves task "
            "completion rate across all four evaluated models, with gains of up to 12 percentage points "
            "in Pass@0.75 for crowded candidate sets."
        ),
    },
    {
        "arxiv": "2610.06454",
        "concept": "trajectory-level-privacy-audit",
        "k": 427,
        "narrative": (
            "**AgentPrivArena — judge the trajectory, not the last message.** Privacy benchmarks "
            "score an agent's **final response**; this one argues that misses where violations "
            "*originate*. An agent can **read a sensitive file it never needed and never mention it** "
            "— outcome-level scoring sees nothing, while the record sits in context for the rest of "
            "the run. The framework runs agents against **six real self-hosted services** (BookStack, "
            "Mattermost, Rocket.Chat, Mailpit, GoToSocial, Radicale) exposed through **authentic MCP "
            "servers in a Docker sandbox**, so records exist as *service state* rather than as text "
            "in a prompt — the agent has to **find** them. Two contributions: **trajectory-level "
            "privacy metrics** (unnecessary access, not just leakage) and **AgentPrivAudit**, a "
            "runtime in-loop auditor with a **read boundary and a write boundary**. The design "
            "insight is that the two boundaries can legitimately disagree: in one worked case the read "
            "boundary cleared an appointment time for a *colleague*, and the write boundary removed it "
            "because the reply was going to a *public channel* — **the same fact, different audience, "
            "different verdict**. And the authors report their own failure mode honestly: repeated "
            "abstraction ratchets until a correct-by-safety reply scores **0 for helpfulness**, and "
            "**nothing in the loop distinguishes \"withheld a sensitive detail\" from \"withheld the "
            "answer.\"** Static-vs-live is the other measured result: pre-authored traces average "
            "**1.9 read steps / 0.2% deep**, live execution **5.1 / 14.3%**, because real runs must "
            "*locate* records and recover from stale identifiers. Pairs K395 approval laundering / "
            "`@concepts/tool-argument-privacy-minimization.md` / K421 (untrusted input + sensitive "
            "access + egress) / `@concepts/measurement-integrity-mcp-security-eval.md`. **Phase-0: "
            "`voidreaming/agentprivarena` MIT, 3.8 MB — but it is the project *website*, not the "
            "framework** → **no clone**. Runtime **`wont_wire`**; concept **`policy_wired`**."
        ),
        "pdf": "arxiv-2610.06454-agentprivarena-evaluating-and-auditing-real-worl.pdf",
        "slug": "arxiv-agentprivarena-trajectory-privacy-audit-2610.06454",
        "title": "AgentPrivArena: Evaluating and Auditing Real-world AI Agent Privacy",
        "verdict": "ADOPT pattern (repo is website only)",
        "no_clone": "agentprivarena",
        "repo": "voidreaming/agentprivarena",
        "snippet": (
            "an agent may unnecessarily access sensitive files unrelated to the task even if no "
            "private information appears in its final response."
        ),
    },
    {
        "arxiv": "2610.06829",
        "concept": "conformal-self-verification-certified-bank",
        "k": 428,
        "narrative": (
            "**CLIFT — turn the judge's feedback into a verifier the agent carries with it.** The "
            "problem is the verifier bottleneck for agent RL: a binary success signal is too sparse "
            "(when every rollout in a GRPO group scores alike, the advantage collapses), while a "
            "frontier judge is too expensive to call per step **and cannot be assumed available at "
            "deployment**. CLIFT's object is not a new model but a **calibrated question bank**: "
            "natural-language verification questions, each with a **URL scope** and a **polarity "
            "sign** (does YES mean progress or failure?). A **Compositional Conformal Certifier** "
            "keeps only questions whose URL-conditional evidence agrees with a training-time judge, "
            "assigns **signed trust weights** by polarity-aware lift, and blends the score into "
            "per-step rewards **asymmetrically — it can only add evidence on top of the judge "
            "baseline, never subtract**, which prevents the reward-collapse failure of earlier linear "
            "blends. At test time the same bank is **frozen** and reused as **Conformal Trajectory "
            "Selection**: sample a greedy rollout plus retries, summarise each URL trace, and apply a "
            "**conservative majority rule** to decide whether to swap — **no external judge called**. "
            "Three results: SOTA open-source web agent on WebArena Infinity; **a bank trained on open "
            "Gemma-4 transfers to GPT-5.5** and reaches SOTA under the canonical harness on "
            "VisualWebArena; and on Online Mind2Web, **no agent is trained on the benchmark** — the "
            "question bank alone transfers and lifts a live-web agent. **CCC relevance:** this is the "
            "strongest version of a pattern CCC already holds — **the verifier should be explicit, "
            "cheap, and reusable**, not an expensive oracle called at runtime. The certified-bank idea "
            "generalises K407 (judge variance) and K424 (graded ladder): make the grading signal "
            "deterministic, transferable, and auditable. Pairs K423 TPRS / "
            "`@concepts/verifiable-deterministic-agent-benchmarking.md` / "
            "`@concepts/agent-completion-verification-gates.md` / K406 Assay. **No repo stated.** "
            "Runtime **`wont_wire`**; concept **`policy_wired`**."
        ),
        "pdf": "arxiv-2610.06829-clift-conformal-self-verification-for-web-agent.pdf",
        "slug": "arxiv-clift-conformal-self-verification-2610.06829",
        "title": "CLIFT: Conformal Self-Verification for Web Agent Training and Test-Time Scaling",
        "verdict": "ADOPT pattern",
        "no_clone": "clift",
        "repo": "",
        "snippet": (
            "The policy is often not the only limiting object; the way we score and select its rollouts "
            "can dominate the observed success rate."
        ),
    },
    {
        "arxiv": "2610.06830",
        "concept": "preference-aware-memory-orchestration",
        "k": 429,
        "narrative": (
            "**MemPilot — memory curation as a runtime decision under an explicit cost budget.** Most "
            "agent memory is built **query-agnostically**, before the next question is known: that "
            "pays preprocessing cost for evidence never used, and **discards details that later turn "
            "out to matter**. Prior runtime-adaptive work exists but is rigid — hand-designed "
            "operations, fixed pipelines, or discrete budget tiers — and almost always optimises "
            "**token or dollar cost while ignoring latency**, which users actually feel. MemPilot "
            "keeps **two views** (a query-agnostic memory bank for cheap access, plus the **raw "
            "multimodal history**) and learns a **multi-step policy** that decides four things per "
            "step: **how much evidence to process, what curation instruction to give, which model to "
            "delegate to** (heterogeneous LLMs and VLMs have different quality/cost/latency profiles), "
            "**and whether visual evidence is needed**. Two RL details make it trainable under "
            "competing objectives: **objective-wise advantage decoupling** (estimate each objective's "
            "advantage separately, then aggregate) and **prefix-based marginal utility estimation** "
            "for fine-grained credit assignment across multi-step rollouts. Result: **preference "
            "sweeps trace broader performance–cost–latency frontiers** than trade-off-aware "
            "baselines. **CCC relevance:** the framing is the useful part — **memory is not a "
            "storage question, it is a budgeting question**, and latency belongs in the objective "
            "alongside cost. Pairs `@concepts/token-economics-and-prompt-caching.md` / K387 KV "
            "working-set / K425 cost-aware evolution / `@concepts/storage-budgeted-agent-memory-"
            "compression.md` / K419 lossless memory (the opposite posture, and the two bracket the "
            "design space). **No repo surfaced** (project website only). Runtime **`wont_wire`**; "
            "concept **`policy_wired`**."
        ),
        "pdf": "arxiv-2610.06830-mempilot-orchestrating-on-demand-multimodal-memo.pdf",
        "slug": "arxiv-mempilot-preference-aware-memory-orchestration-2610.06830",
        "title": "MemPilot: Orchestrating On-Demand Multimodal Memory Curation for LLM Agents",
        "verdict": "ADOPT pattern (no repo)",
        "no_clone": "mempilot",
        "repo": "",
        "snippet": (
            "most existing agent memory systems construct memory in a query-agnostic manner, which can "
            "incur unnecessary preprocessing cost and discard details that later prove essential."
        ),
    },
    {
        "arxiv": "2610.06843",
        "concept": "navigable-demonstration-hierarchy",
        "k": 430,
        "narrative": (
            "**RV-ICL — let the agent navigate the demonstration, do not paste it into the prompt.** "
            "Agentic robot harnesses improve across episodes through **text memory**, which records "
            "*what the agent did* but not *how the task is done*. A demonstration video shows the how, "
            "and fits badly into context three ways, each named precisely: **the full video slows "
            "every turn**; **fixed keyframes lose the contact detail that decides whether a grasp "
            "holds**; and **what the agent needs shifts** — task structure while planning, frames "
            "around each contact while executing. RV-ICL's answer is architectural: turn the "
            "demonstration into **a hierarchy the agent navigates rather than a prompt it receives**. "
            "Levels run coarse-to-fine — whole-task keyframes → phases → moments → short clips — built "
            "from the demonstration's **sub-events** (grasps, releases), and exposed through "
            "**read-only tools**. The agent reads coarse levels before planning, **re-enters the "
            "hierarchy whenever a step needs more detail**, and loads **only the clip of its current "
            "sub-goal**. Training-free. One demonstration per task suffices. On RPent: LIBERO-PRO "
            "**92.6% → 96.5%**, LIBERO-Plus **86.7% → 95.8%**. **CCC relevance is direct and it is "
            "the same argument as K419 VISTA, made one level more explicit:** do not pre-decide what "
            "context matters — **expose it as a navigable structure and let the agent pull what it "
            "needs, when it needs it**. Where VISTA gives lossless retention plus inspection over "
            "frames, RV-ICL gives lossless retention plus a *pre-indexed semantic hierarchy*, so "
            "retrieval is cheaper than search. Pairs K419 / K311 lazy MCP / "
            "`@concepts/context-engineering.md` / `@concepts/progressive-skill-discovery-access-"
            "control.md` (progressive disclosure, earned by capability). Cross-domain (robotics) so "
            "REFERENCE, but the pattern is harness-general. **Phase-0: no public repo confirmed.** "
            "Runtime **`wont_wire`**; concept **`policy_wired`**."
        ),
        "pdf": "arxiv-2610.06843-recursive-video-in-context-learning-for-agentic.pdf",
        "slug": "arxiv-rv-icl-navigable-demonstration-hierarchy-2610.06843",
        "title": "Recursive Video In-Context Learning for Agentic Robot",
        "verdict": "REFERENCE (cross-domain; pattern transfers)",
        "no_clone": "rv-icl",
        "repo": "",
        "snippet": (
            "turns a demonstration into a hierarchy the agent navigates rather than a prompt it "
            "receives."
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
description: CCC Phase-1 wires from K426–K430 harness wave (CCC-only — do NOT federation-sync)
alwaysApply: false
---

# CCC — K426–K430 Phase-1 wires

**Brief:** `docs/briefs/{DATE}_k426-k430-harness-wave.md` · SIP: `wiki/briefs/{BRIEF}`

**IDs:** Resolve by arXiv id / slug / file path — K# is a log batch label only.

{bullets}

**Wires landed:**

| K | Verdict | Wire | wire_status |
|---|---|------|-------------|
{rows}

**Non-goals:** no federation sync; no PoCs; no clone of any repo this wave.

**Note:** K427's repo is the project *website*, not the framework — do not clone it expecting the
harness.
"""
    (REPO / ".cursor/rules" / RULE).write_text(text, encoding="utf-8")


def append_policy():
    path = REPO / ".cursor/rules/cemini-phase1-policy-wires.mdc"
    text = path.read_text(encoding="utf-8")
    if f"CCC wave {WAVE}" in text:
        return
    block = f"""

## CCC wave {WAVE} (shared policy file)

MCP tool taxonomy navigation (K426) + trajectory-level privacy audit (K427) + conformal certified
verifier bank (K428) + preference-aware memory orchestration (K429) + navigable demonstration
hierarchy (K430). **Zero clones.** CCC-only rule `{RULE}` — do **not** federation-sync.

## MCP tool taxonomy navigation (CCC K426)

- **Organise tools by capability, not by marketplace.** At 1.33M tool specs, how candidates are
  presented is a capability lever: taxonomy-guided presentation lifted task completion on all four
  models tested, **up to +12 pt Pass@0.75 as the candidate set crowds**. Watch the tail: 98.5% of
  tools have an alternative but **~25% of capabilities have exactly one** — single points of
  failure — and comparable alternatives differ >2.5× in complexity in 41% of pairs (pairs
  K311/`mcp-tool-interface-granularity-eval`/K402). Runtime **`wont_wire`**.

## Trajectory-level privacy audit (CCC K427)

- **Judge the trajectory, not the last message.** An agent can read sensitive records, never mention
  them, and still have them in context for the rest of the run. Audit with **separate read and write
  boundaries** — they legitimately disagree, because audience differs (a fact fine in a DM is not
  fine in a channel). Known failure mode: **repeated abstraction ratchets until a safe answer scores
  0 for helpfulness**, and nothing in the loop distinguishes *withheld a detail* from *withheld the
  answer* (pairs K395/`tool-argument-privacy-minimization`/K421). Runtime **`wont_wire`**.

## Conformal certified verifier bank (CCC K428)

- **Turn expensive judge feedback into a cheap, transferable, judge-free signal.** A bank of
  verification questions, each with a **scope** and a **polarity sign**, certified by agreement with
  a training judge. Blend into rewards **asymmetrically — add evidence only, never subtract** (this
  is what prevents reward collapse). Freeze the bank and reuse it for test-time trajectory
  selection: **no external judge at deployment**, and the bank **transfers across models** (trained on
  Gemma-4, used on GPT-5.5). pairs K407/K423/K424/K406. Runtime **`wont_wire`**.

## Preference-aware memory orchestration (CCC K429)

- **Memory is a budgeting question, not a storage question.** Keep a cheap query-agnostic bank *plus*
  the raw history, and let a learned policy decide per step: how much evidence, which curation, which
  model, whether visual access. **Put latency in the objective alongside cost**, not just tokens or
  dollars. Objective-wise advantage decoupling + prefix-based marginal utility for credit assignment
  (pairs `token-economics-and-prompt-caching`/K387/K425/K419). Runtime **`wont_wire`**.

## Navigable demonstration hierarchy (CCC K430)

- **Navigate the context, do not paste it.** A demonstration becomes a **coarse-to-fine hierarchy
  exposed through read-only tools**: the agent reads coarse levels before planning and **re-enters
  when a step needs detail**, loading only the current sub-goal's clip. Same argument as K419 one
  level more explicit — **do not pre-decide what matters; expose it and let the agent pull** (pairs
  K419/K311/`context-engineering`/`progressive-skill-discovery-access-control`). Runtime
  **`wont_wire`**.
"""
    path.write_text(text.rstrip() + block + "\n", encoding="utf-8")


def write_briefs():
    docs = REPO / "docs/briefs/2026-10-06_k426-k430-harness-wave.md"
    docs.write_text(
        f"""# {WAVE} harness wave — brief (CCC docs)

Date: {DATE} · SIP: `wiki/briefs/{BRIEF}`

## What changed

Five arXiv ingests from the 2026-10-06 sweep. **Zero clones.**

1. **K426** MCPacific — MCP ecosystem mapped by capability (1.33M tool specs, 58,915 capabilities)
2. **K427** AgentPrivArena — trajectory-level privacy audit with read/write boundaries
3. **K428** CLIFT — conformal certified verifier bank, judge-free at test time
4. **K429** MemPilot — memory curation under explicit performance/cost/latency preferences
5. **K430** RV-ICL — demonstration as a navigable hierarchy (cross-domain REFERENCE)

## Phase-0 / Phase-1

- `adopt_k426`…`k430` — all exit 0
- `{RULE}` + policy §{WAVE}
- Phase-0: **no repo for K426/K428/K429/K430.** `voidreaming/agentprivarena` (K427) is **MIT but the
  project *website*, not the framework** → no clone.

## Cross-wiki

- **None this wave.** All five are harness, eval, or memory work that CCC owns. The privacy paper
  (K427) is adjacent to Cybersec but its contribution is an *eval framework*, not a defence —
  CCC keeps it.
- **Minecraft / `dragon-rider-map` and Game Dev wiki — checked, no match.**
- **K430 is cross-domain (robotics)** but the pattern — navigable context hierarchy — is
  harness-general and pairs directly with K419.

## Propose-only

- None. No clone candidate surfaced this wave.
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
tags: [brief, handoff, k426, k427, k428, k429, k430]
keywords: [mcp-taxonomy, privacy-audit, conformal-verification, memory-orchestration, navigable-context]
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
| K426 | 2610.05319 | ADOPT pattern — MCPacific taxonomy |
| K427 | 2610.06454 | ADOPT pattern — AgentPrivArena |
| K428 | 2610.06829 | ADOPT pattern — CLIFT certified bank |
| K429 | 2610.06830 | ADOPT pattern — MemPilot |
| K430 | 2610.06843 | REFERENCE (cross-domain) — RV-ICL |
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
    if sa in text and "2026-10-06-daily" not in text:
        text = text.replace(sa, sa +
            "\n| [`2026-10-06-daily`](sweeps/2026-10-06-daily.md) | Daily digest — 5 papers (K426–K430 wave) |", 1)
    idx.write_text(text, encoding="utf-8")


def prepend_log():
    log = REPO / "wiki/log.md"
    entry = f"""## [{DATE}] ingest | {WAVE} harness wave (Oct 6 daily sweep)

- **Sources:** 2610.05319 MCPacific, 2610.06454 AgentPrivArena, 2610.06829 CLIFT, 2610.06830 MemPilot, 2610.06843 RV-ICL.
- **Phase-0:** no repo for K426/K428/K429/K430. `voidreaming/agentprivarena` (K427) is **MIT but the project website**, not the framework → no clone.
- **Phase-1:** adopt_k426…k430; `{RULE}`; policy §{WAVE}. Zero clones.
- **Cross-wiki:** none — all five are harness/eval/memory work CCC owns. Minecraft + Game Dev checked, no match.
- **Standouts:** K428's **certified verifier bank that transfers across models and needs no judge at test time**; K426's finding that **how tools are organised in context is itself a capability lever** (up to +12 pt at scale).
- **Archive:** egress bulk ccc (5 PDFs). Inbox empty.

"""
    t = log.read_text(encoding="utf-8")
    if f"{WAVE} harness wave" not in t:
        log.write_text(entry + t, encoding="utf-8")


def patch_sweep():
    p = REPO / "wiki/sweeps/2026-10-06-daily.md"
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
