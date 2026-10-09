#!/usr/bin/env python3
"""Generate K441–K444 wiki ingest artifacts (2026-10-09 daily sweep)."""
from __future__ import annotations
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DATE = "2026-10-09"
BRIEF = "2026-10-09_ccc-k441-k444-sip-ready.md"
EGRESS = "cemini-egress-fi:/opt/cemini-bulk/research/ccc"
RULE = "ccc-k441-k444-phase1-wires.mdc"
WAVE = "K441–K444"


def E(arxiv, concept, k, slug, title, verdict, no_clone, repo, narrative, snippet, extra=None):
    pdfs = list((REPO / "research to be indexed").glob(f"*{arxiv}*"))
    return dict(arxiv=arxiv, concept=concept, k=k, slug=slug, title=title,
                verdict=verdict, no_clone=no_clone, repo=repo,
                narrative=narrative, snippet=snippet, extra=extra or [],
                pdf=pdfs[0].name if pdfs else f"arxiv-{arxiv}.pdf")


ENTRIES = [
 E("2610.10659", "specification-versus-capability-failure-attribution", 441,
   "arxiv-security-by-design-point-of-execution-2610.10659",
   "Applying Security by Design at the Point of Execution: How Governed Security Requirements Affect the Security of AI-Generated Code",
   "ADOPT pattern (MCP-delivered governed requirements)", "sbd-toe-mcp", "SbD-ToE/sbd-toe-mcp",
   "**The gap is often specification, not capability — deliver the requirements at the point of "
   "execution.** A coding agent is given a governed, versioned security-by-design knowledge base "
   "(SbD-ToE) through an **MCP server** whose selector returns the requirements that apply to a task; "
   "the agent calls it at the moment it writes code. Two benchmarks, two evaluators (a GPT-4o judge "
   "and executed exploits in containers). **DualGauge (59 Python tasks):** tasks passing all security "
   "tests **44.1% → 78.0%**; security tests passed **77.4% → 93.0%** (both p<0.001). **BaxBench (28 "
   "backend scenarios):** among functionally correct solutions the share with **no successful exploit "
   "rose 65% → 86%** — comparable to the authors' own **Oracle Security Reminder (85%)**, which they "
   "call an *unrealistic upper bound* because it names the weaknesses the tests check. The delivery "
   "reached that level **without knowing the tests**. **The cost:** the stricter code failed functional "
   "tests that assume values the task never states (short passwords, non-Luhn card numbers, undeclared "
   "fields), so the *joint* secure-and-functional metric did **not** improve significantly. **CCC "
   "reading:** a clean statement of a pattern CCC keeps meeting — *a benchmark score conflates three "
   "failure causes*: the model could not implement a property (**capability**), the knowledge base had "
   "no requirement for the weakness (**coverage**), or the test rejects a conforming implementation "
   "(**oracle**). Delivering the requirements makes the causes separable, the same move as K437's "
   "score-formulation-separately and K436's read/write split. Two harness observations to keep: (1) the "
   "MCP tool returned **45,000–76,000 characters** and Claude Code **saved it to a file in 41 of 59 "
   "sessions**, the agent reading part of it — a concrete tool-output-too-large datapoint (pairs "
   "`mcp-context-optimization`); (2) the runs are a **headless Claude Code lane** (`claude -p "
   "--permission-mode bypassPermissions --strict-mcp-config --setting-sources project`). **Phase-0: "
   "`SbD-ToE/sbd-toe-mcp` Apache-2.0** (0★, 2026-09-28); manual `SbD-ToE/sbd-toe-manual` "
   "**CC-BY-SA-4.0**. A PoC MCP server; no CCC workstream needs it → no clone. Runtime `wont_wire`; "
   "concept `policy_wired`.",
   "the share of tasks passing all security tests rose from 44.1% to 78.0% and the share of security "
   "tests passed from 77.4% to 93.0%",
   extra=["entities/tools/sbd-toe-mcp.md",
          "concepts/mcp-context-optimization.md",
          "concepts/mcp-contract-grounded-synthesis-and-validation-gate.md"]),

 E("2610.12360", "epistemic-humility-identify-solve-escalate", 442,
   "arxiv-epistemic-humility-knowledge-conflict-2610.12360",
   "Accurate but Not Humble: Evaluating Epistemic Humility in LLM Agents under Knowledge Conflict",
   "ADOPT eval-methodology (Claude Code harness eval)", "EpistemicHumilityLLMAgents",
   "KaiserWhoLearns/EpistemicHumilityLLMAgents",
   "**Accuracy and epistemic humility are two different curves.** Defines **epistemic humility (EH)** "
   "as three trajectory-level behaviours, **Identify, Solve, Escalate (ISE)**: notice the knowledge "
   "gap, act on it with bounded tool use, and tell the user when uncertainty is unresolved. Elicits it "
   "through **knowledge conflict** (parametric belief vs. retrieved evidence, or two sources "
   "disagreeing) with matched no-conflict controls. Four harnesses evaluated, **one of them Claude Code "
   "(Sonnet 4.6, WebSearch/WebFetch/Bash)** alongside Nemotron-ToolOrchestra, OpenHands, and "
   "Qwen-Agent. **Three findings:** (1) **higher task accuracy does not imply greater EH** — some "
   "high-accuracy configs *identify* the conflict but do not acknowledge unresolved uncertainty in "
   "their incorrect final answers; (2) conflict-relevant mentions **peak in the first 10% of "
   "execution** then fall — agents detect early but do not follow up; (3) a **one-clause system-prompt "
   "intervention raises Escalate while lowering accuracy** (MoNaCo Escalate 1.6 → 60.7 for GPT-5, "
   "**13.9 → 60.8 for Claude Code**), landing most configs in the *humble-but-inaccurate* quadrant. "
   "Claude Code posts the **highest Identify rate (F1 90.0% on BrowseComp)** yet its wrong finals still "
   "do not escalate. **CCC reading:** the paper's recommendation is a **harness affordance** — *expose "
   "an explicit abstain-or-escalate action so a conflict raised mid-trajectory survives into the final "
   "answer instead of being overwritten by the next tool call*, and score trajectories, not final "
   "answers. That is CCC's position on verification gates and on `clarify-before-act`, here measured "
   "across four harnesses and shown to be a *system property*, not a model property ('epistemic "
   "humility emerges from the interaction among the backbone model, the agent harness, and the "
   "evaluation environment'). Pairs `clarify-before-act-evidence-aligned-close`, "
   "`overclaiming-propensity-agent-measurement`, `trajectory-error-lifecycle-attribution`. "
   "**Phase-0: `KaiserWhoLearns/EpistemicHumilityLLMAgents` Apache-2.0** (1★, pushed 2026-10-09) — "
   "released trajectories + per-turn ISE judgments; REFERENCE clone optional. Runtime `wont_wire`; "
   "concept `policy_wired`.",
   "higher task accuracy does not necessarily correspond to greater epistemic humility",
   extra=["concepts/clarify-before-act-evidence-aligned-close.md",
          "concepts/overclaiming-propensity-agent-measurement.md",
          "concepts/trajectory-error-lifecycle-attribution.md"]),

 E("2610.12369", "code-only-policy-shared-library", 443,
   "arxiv-code-only-as-policy-embodied-turing-2610.12369",
   "Embodied Turing Machines: Stateful Code for Robot Recursive Self-Improvement",
   "REFERENCE (cross-domain; pattern transfers)", "COAP", "",
   "**When the state is explicit and the code is robust, no model needs to run at test time.** "
   "Robotics (RoboDojo, 42 bimanual tasks) — but the harness shape is the transferable part. "
   "**Code-Only-as-Policy (COAP):** the embodied world is modelled as an **Embodied Turing Machine** "
   "whose *tape* is the robot+environment state and whose *rules* are code; code measures and tracks "
   "the state, makes every decision from it, and **one program runs every episode**. A **shared code "
   "library** is developed offline by coding agents (Opus 5.5 Max), and **83% of the code a new task "
   "runs is reused from the library**. Three claimed advantages over VLAs and agent harnesses — "
   "**Explicit State** (inspectable, persistent, measured), **Execution** (controllable, recoverable by "
   "backtracking, ~0.3 ms/step on CPU, 0.8–2.4% of a VLA's compute), **Extensibility** (reuse / "
   "inherit / extend; capabilities accumulate without regressing old tasks). **Two mechanisms worth "
   "stealing:** (1) an **offline RSI loop over git worktrees** — each agent works in its own worktree, "
   "inspects the recorded state of failed runs, proposes a diff, and the diffs form a *search frontier "
   "of runnable branches* evaluated in parallel under identical conditions; acceptance is a "
   "**non-regression gate** `J(θ+Δ) ≥ J(θ) + ε` with ε above rerun noise. (2) a **default-off "
   "parameter compatibility guarantee** (Eq. 3): an extension must leave the execution trace of every "
   "task that does *not* pass the new argument byte-identical, so earlier tasks keep their behaviour "
   "*by construction* and only the adopting task changes. Result: 70.24% vs 31.38% SOTA. **CCC "
   "reading:** K436/K437's 'explicit beats implicit' argument taken to its end, and it converges with "
   "CCC's own harness-evolution lane — the **non-regression gate** is "
   "`agent-optimizer-compounding-and-regression-control`, and the **git-worktree parallel branch "
   "search** is the concrete mechanism behind CCC's 'keep the change iff it wins' rule (pairs K411's "
   "mutation-keep loop and K415's harness editor). It also cites **Anthropic's 'Code execution with "
   "MCP'** and **Cloudflare's 'Code Mode'** — code as the agent's action interface. Cross-domain "
   "REFERENCE. **No public repo.** Runtime `wont_wire`; concept `policy_wired`.",
   "If this state can be represented accurately, the decision making can be written entirely in code.",
   extra=["concepts/agent-optimizer-compounding-and-regression-control.md",
          "concepts/recursive-agent-harness-harness-recursion.md"]),

 E("2610.12375", "streaming-trajectory-monitor-pre-execution-gate", 444,
   "arxiv-ontrack-streaming-monitor-2610.12375",
   "OnTrack: Real-Time Monitoring and Intervention in LLM Agent Trajectories via Streaming Structure-Aware Optimal Transport",
   "ADOPT pattern (real-time process monitor + pre-execution gate)", "ontrack", "",
   "**A monitor that decides, not scores — and blocks irreversible actions before they run.** OnTrack "
   "is a **streaming** process monitor: it models the agent's execution as a growing **DAG** (each step "
   "a node; an edge when one step consumes another's output) and aligns it against recorded successful "
   "runs with **structure-aware optimal transport**, at **~1 ms/step**. Three tiers that switch off as "
   "inputs disappear: **L1 vital signs** (loop, stall, information-gain — reference-free, always on), "
   "**L2 transport alignment** (needs references), **L3 pre-execution policy gate** (needs tool "
   "schemas; the only *synchronous* component — it checks an **irreversible** tool call's declared "
   "prerequisites *before* the tool runs and can **BLOCK**). Verdicts are actions — `OK / EXPLORING / "
   "WARN / LOOP / STALLED / CAUSAL INVERSION / OFF TRACK / BLOCK` — never a thresholded score, because "
   "**'a score value means different things at different trajectory lengths'** (its challenge S4). On "
   "**2,294 SWE-agent trajectories**: **+0.057 AUROC over cosine similarity at the first 8 steps** "
   "(the early-trajectory regime an in-flight monitor lives in), and a severe-flag-density **abort "
   "policy** saves **~18% of compute** with **83% of aborted runs genuinely heading to failure**. "
   "**Honest boundaries kept:** it is a *process monitor, not an outcome predictor* — once trace "
   "length is controlled, no task-generic signal predicts patch correctness; on homogeneous traces, "
   "loops/stalls are carried by the reference-free L1 heuristics and the transport layer's "
   "contribution is a *lower false-alarm operating point*, not better ranking; and the L3 gate is *a "
   "policy gate, not a soundness guarantee*. **CCC reading:** the clearest design doc CCC has for a "
   "**hook-like checkpoint layer** inside the agent loop — the L3 pre-execution gate is exactly a "
   "`PreToolUse`-style block on irreversible actions, and 'per-step signals, short grace window, never "
   "the aggregate score' is a rule for writing hooks and gates. It also names the harness dependency: "
   "the dependency metadata `ζt` **comes from the harness's own logs** (full / partial / none), so "
   "monitor quality is bounded by what the harness records — the same affordance argument as K442. "
   "Pairs `instrumental-monitor-evasion-under-task-pressure`, "
   "`agent-completion-verification-gates`, `execution-fidelity-irreversible-agent-invariants`, "
   "`intent-based-tool-call-oversight`. **No public repo URL.** Runtime `wont_wire`; concept "
   "`policy_wired`.",
   "compares its steps and the dependencies between them against recorded successful runs and alerts "
   "the user of potential issues or blocks the agent, taking about a millisecond per step",
   extra=["concepts/instrumental-monitor-evasion-under-task-pressure.md",
          "concepts/agent-completion-verification-gates.md",
          "concepts/execution-fidelity-irreversible-agent-invariants.md",
          "concepts/intent-based-tool-call-oversight.md"]),
]


def yl(items): return "\n".join(f"  - {x}" for x in items)


def write_source(e):
    k = e["k"]
    rel = [f"concepts/{e['concept']}.md"] + e["extra"] + [f"briefs/{BRIEF}"]
    rr = f"| **Repo** | `{e['repo']}` |\n" if e.get("repo") else ""
    (REPO/"wiki/sources"/f"{e['slug']}.md").write_text(f"""---
title: "{e['title'][:70]} (CCC K{k})"
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
    rel = [f"sources/{e['slug']}.md"] + e["extra"] + ["concepts/phase1-adopt-wire.md", f"briefs/{BRIEF}"]
    (REPO/"wiki/concepts"/f"{c}.md").write_text(f"""---
title: "{e['title'][:70]} (CCC K{k})"
type: concept
tags: [concept, k{k}]
keywords: [{e['arxiv']}, k{k}]
related:
{yl(rel)}
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: {DATE}
updated: {DATE}
---

## Relations

{chr(10).join(f'- `@{r}`' for r in rel)}

## Raw Concept

K{k}: {e['verdict']} — arXiv {e['arxiv']}.

## Narrative

{e['narrative']}

## Snippets

> "See source page for arXiv {e['arxiv']} locators." [Source: CCC K{k} synthesis]
""", encoding="utf-8")


def write_entity_sbdtoe():
    (REPO/"wiki/entities/tools"/"sbd-toe-mcp.md").write_text(f"""---
title: "sbd-toe-mcp — governed security-by-design requirements over MCP (PoC, no install)"
type: entity
tags: [entity, tool, mcp, security, codegen, k441]
keywords: [2610.10659, SbD-ToE, sbd-toe-mcp, security-by-design, requirements, Apache-2.0]
related:
  - sources/arxiv-security-by-design-point-of-execution-2610.10659.md
  - concepts/specification-versus-capability-failure-attribution.md
  - concepts/mcp-context-optimization.md
  - concepts/mcp-contract-grounded-synthesis-and-validation-gate.md
maturity: draft
wire_status: wont_wire
wire_target: "PoC MCP server (0★) — REFERENCE only; no CCC security-by-design workstream"
created: {DATE}
updated: {DATE}
---

## Relations

- `@sources/arxiv-security-by-design-point-of-execution-2610.10659.md`
- `@concepts/specification-versus-capability-failure-attribution.md`
- `@concepts/mcp-context-optimization.md`

## Raw Concept

Phase-0 entity for K441 — `@shiftleftpt/sbd-toe-mcp`, an MCP server that serves governed
security-by-design requirements (SbD-ToE) to a coding agent at the point of execution.

## Narrative

| Artifact | Availability | Verdict |
|----------|--------------|---------|
| `SbD-ToE/sbd-toe-mcp` | **Apache-2.0**, 0★, pushed 2026-09-28 | **REFERENCE** (PoC) |
| `SbD-ToE/sbd-toe-manual` | **CC-BY-SA-4.0**, 0★, pushed 2026-09-30 | Doc source |
| npm `@shiftleftpt/sbd-toe-mcp` 0.10.1 | Published 2026-06-25 | Pinned release |

**What it is:** the selector tool `prepare_sbd_toe_codegen_context(task, mode, risk_level)` returns
the activated security requirements (control objectives, base requirements, controls, evidence
expectations) for a task. The paper's own runs used `claude -p --permission-mode bypassPermissions
--strict-mcp-config --setting-sources project`.

**Why `wont_wire`:** it is a single-author PoC with 0★. CCC has no security-by-design workstream, and
the transferable content is the *pattern* (deliver governed requirements at the point of execution so
failures become attributable), captured in the K441 concept. The one runtime datapoint CCC cares
about is the payload size: the tool returns **45,000–76,000 characters**, which Claude Code saved to
a file in 41 of 59 sessions.

## Snippets

> "Given a task, a mode and a risk level, it returns the requirements that it activates for that task."
> [Source: arXiv 2610.10659 (retrieved {DATE})]

## Phase-1

Runtime `wont_wire`. Concept `policy_wired` (see `concepts/specification-versus-capability-failure-attribution.md`).
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
    rows = "\n".join(f"| K{e['k']} | {e['verdict']} | {e['concept'].replace('-',' ')[:40]} | `policy_wired` |" for e in ENTRIES)
    bl = "\n".join(f"- **K{e['k']}** {e['title'][:52]}… — **{e['verdict']}**: concept `{e['concept']}`." for e in ENTRIES)
    (REPO/".cursor/rules"/RULE).write_text(f"""---
description: CCC Phase-1 wires from K441–K444 harness wave (CCC-only — do NOT federation-sync)
alwaysApply: false
---

# CCC — K441–K444 Phase-1 wires

**Brief:** `docs/briefs/{DATE}_k441-k444-harness-wave.md` · SIP: `wiki/briefs/{BRIEF}`

**IDs:** Resolve by arXiv id / slug / file path — K# is a log batch label only.

{bl}

**Wires landed:**

| K | Verdict | Wire | wire_status |
|---|---|------|-------------|
{rows}

**Non-goals:** no federation sync; no PoCs; no clone of any repo this wave. K441's repo is a 0★
**Apache-2.0 PoC**; K442's repo is **Apache-2.0** (1★, REFERENCE clone optional); K443/K444 name **no
public repo**.
""", encoding="utf-8")


def append_policy():
    p = REPO/".cursor/rules/cemini-phase1-policy-wires.mdc"; t = p.read_text(encoding="utf-8")
    if f"CCC wave {WAVE}" in t: return
    p.write_text(t.rstrip() + f"""

## CCC wave {WAVE} (shared policy file)

Specification-vs-capability failure attribution (K441) + epistemic-humility Identify/Solve/Escalate
(K442) + code-only-as-policy shared library (K443) + streaming trajectory monitor with a
pre-execution gate (K444). **Zero clones.** CCC-only rule `{RULE}` — do **not** federation-sync.

## Specification versus capability attribution (CCC K441)

- **A benchmark score conflates three failure causes.** Deliver the governed requirements at the
  point of execution and they separate: **capability** (model could not implement), **coverage**
  (knowledge base had no requirement), **oracle** (the test rejects a conforming implementation).
  MCP-served security-by-design requirements raised DualGauge secure@1 **44.1% → 78.0%** and BaxBench
  no-exploit **65% → 86%** — comparable to the *unrealistic* oracle reminder, without knowing the
  tests. The joint metric did **not** improve (stricter code failed tests that fix unstated values).
  Runtime **`wont_wire`**.

## Epistemic humility: identify / solve / escalate (CCC K442)

- **Higher accuracy ≠ more humble, and humility is a harness property.** Three trajectory-level
  behaviours (Identify, Solve, Escalate); conflict mentions **peak in the first 10%** then fall; a
  one-clause prompt raises Escalate but lowers accuracy. Design rule: **expose an explicit
  abstain-or-escalate action so a mid-trajectory conflict survives into the final answer**, and score
  trajectories not final answers. Claude Code has the highest Identify rate yet its wrong finals do
  not escalate. Runtime **`wont_wire`**.

## Code-only-as-policy shared library (CCC K443)

- **Explicit state + robust code ⇒ no model at test time.** A shared library built offline by coding
  agents (**83% code reuse**); two stealable mechanisms: an **offline RSI loop over git worktrees**
  producing a *search frontier of runnable branches* with a **non-regression gate** `J(θ+Δ) ≥ J(θ)+ε`,
  and a **default-off parameter compatibility guarantee** (non-adopting tasks run byte-identical).
  Cross-domain REFERENCE; pairs the compounding/regression-control lane. Runtime **`wont_wire`**.

## Streaming monitor + pre-execution gate (CCC K444)

- **Decide, don't score.** A streaming DAG monitor with three tiers: **L1 vital signs** (loop/stall,
  reference-free), **L2 transport alignment** (needs references), **L3 pre-execution gate** (block an
  **irreversible** tool call whose prerequisites are missing, before it runs). Per-step signals with a
  grace window, never the aggregate score — *a score means different things at different lengths*.
  ~18% compute saved, 83% of aborts correct. Harness metadata (`ζt`) bounds monitor quality. The L3
  gate is the `PreToolUse` shape. Runtime **`wont_wire`**.
""", encoding="utf-8")


def write_briefs():
    (REPO/"docs/briefs"/f"{DATE}_k441-k444-harness-wave.md").write_text(f"""# {WAVE} harness wave — brief (CCC docs)

Date: {DATE} · SIP: `wiki/briefs/{BRIEF}`

## What changed

Four arXiv ingests from the 2026-10-09 sweep. **Zero clones.**

1. **K441** Security by design at the point of execution — specification vs capability attribution
2. **K442** Accurate but Not Humble — epistemic humility (Identify/Solve/Escalate) across four harnesses
3. **K443** Embodied Turing Machines / COAP — code-only-as-policy shared library, offline RSI loop
4. **K444** OnTrack — streaming trajectory monitor with an L3 pre-execution gate

## Phase-0 / Phase-1

- `adopt_k441`…`k444` — all exit 0 · `{RULE}` + policy §{WAVE}
- Phase-0: `SbD-ToE/sbd-toe-mcp` **Apache-2.0** (0★) · `SbD-ToE/sbd-toe-manual` **CC-BY-SA-4.0** ·
  `KaiserWhoLearns/EpistemicHumilityLLMAgents` **Apache-2.0** (1★). K443/K444 name no public repo.

## Cross-wiki

- K441 security-requirements content is **cybersec-adjacent** → steal brief to `@cybersecurity-wiki/`
  (CCC keeps the MCP-delivery / attribution angle).

## Propose-only

- `EpistemicHumilityLLMAgents` REFERENCE clone (Apache-2.0) if CCC wants to reproduce the ISE eval on
  Claude Code.
""", encoding="utf-8")
    rel = [f"concepts/{e['concept']}.md" for e in ENTRIES] + [f"sources/{e['slug']}.md" for e in ENTRIES]
    rel += ["entities/tools/sbd-toe-mcp.md"]
    (REPO/"wiki/briefs"/BRIEF).write_text(f"""---
title: CCC SIP-ready — {WAVE} full ingest
type: brief
handoff: true
tags: [brief, handoff, k441, k442, k443, k444]
keywords: [specification-capability, epistemic-humility, code-only-policy, streaming-monitor]
related:
{yl(rel + ['concepts/phase1-adopt-wire.md'])}
maturity: draft
created: {DATE}
updated: {DATE}
---

## Target

Full ingest of **4 NEW** inbox PDFs as **CCC {WAVE}**. Phase-0 + Phase-1, archive, lint, commit,
push, CI green.

## Inbox

| K | arXiv | Verdict |
|---|-------|---------|
| K441 | 2610.10659 | ADOPT pattern — spec vs capability attribution |
| K442 | 2610.12360 | ADOPT eval-methodology — epistemic humility (Claude Code harness) |
| K443 | 2610.12369 | REFERENCE (cross-domain) — code-only-as-policy shared library |
| K444 | 2610.12375 | ADOPT pattern — streaming monitor + pre-execution gate |
""", encoding="utf-8")


def patch_index():
    idx = REPO/"wiki/index.md"; t = idx.read_text(encoding="utf-8")
    if ENTRIES[0]["slug"] in t: return
    # tool entity row
    te_anchor = "| [`datumpont-execution-fidelity`]"
    if te_anchor in t:
        row = f"| [`sbd-toe-mcp`](entities/tools/sbd-toe-mcp.md) | draft | Governed security-by-design requirements over MCP — PoC Apache-2.0, `wont_wire` (K441) |"
        t = t.replace(te_anchor, row + "\n" + te_anchor, 1)
    ac = "| [`assay-content-addressed-evidence-graphs`]"
    if ac not in t: ac = "| [`htn-planning-mcp-multi-server-coordination`]"
    for e in ENTRIES:
        row = f"| [`{e['concept']}`](concepts/{e['concept']}.md) | draft | {e['title'][:48]}… — {e['arxiv']} (K{e['k']}) |"
        t = t.replace(ac, row + "\n" + ac, 1)
    as_ = "| [`arxiv-assay-content-addressed-evidence-graphs-2609.36170`]"
    if as_ not in t: as_ = "| [`arxiv-htn-planning-mcp-multi-server-coordination-2609.33731`]"
    for e in ENTRIES:
        row = f"| [`{e['slug']}`](sources/{e['slug']}.md) | draft | {e['title'][:52]}… — {e['arxiv']} |"
        t = t.replace(as_, row + "\n" + as_, 1)
    sa = "| [`2026-10-08-daily`](sweeps/2026-10-08-daily.md)"
    if sa in t and "2026-10-09-daily" not in t:
        t = t.replace(sa, sa + "\n| [`2026-10-09-daily`](sweeps/2026-10-09-daily.md) | Daily digest — 4 papers (K441–K444 wave) |", 1)
    idx.write_text(t, encoding="utf-8")


def prepend_log():
    log = REPO/"wiki/log.md"
    entry = f"""## [{DATE}] ingest | {WAVE} harness wave (Oct 9 daily sweep)

- **Sources:** 2610.10659 security-by-design at the point of execution, 2610.12360 epistemic humility under knowledge conflict, 2610.12369 Embodied Turing Machines (COAP), 2610.12375 OnTrack streaming monitor.
- **New pages:** 4 arxiv sources, 4 concepts (specification-versus-capability-failure-attribution, epistemic-humility-identify-solve-escalate, code-only-policy-shared-library, streaming-trajectory-monitor-pre-execution-gate), 1 entity (`sbd-toe-mcp` `wont_wire`); SIP `wiki/briefs/{BRIEF}`.
- **Phase-0:** `adopt_k441`…`k444` all exit 0. `SbD-ToE/sbd-toe-mcp` **Apache-2.0** (0★); `SbD-ToE/sbd-toe-manual` **CC-BY-SA-4.0**; `KaiserWhoLearns/EpistemicHumilityLLMAgents` **Apache-2.0** (1★, pushed 2026-10-09). K443/K444 name no public repo. **Zero clones.**
- **Phase-1:** `{RULE}` + policy §{WAVE}. Runtime `wont_wire` for all four; concepts `policy_wired`.
- **Standouts:** K441's **44.1% → 78.0%** secure@1 with the joint metric flat (spec-vs-capability); K442's **higher accuracy ⇒ lower escalation**, Claude Code highest Identify yet no escalation; K443's **non-regression gate** + default-off compatibility guarantee with **83% library reuse**; K444's **L3 pre-execution block** on irreversible calls, **~18% compute saved**.
- **Cross-wiki:** K441 routed to `@cybersecurity-wiki/` as a steal (CCC keeps the MCP-delivery angle).
- **Archive:** egress bulk ccc (4 PDFs). Inbox empty.

"""
    t = log.read_text(encoding="utf-8")
    if f"{WAVE} harness wave" not in t: log.write_text(entry + t, encoding="utf-8")


def patch_sweep():
    p = REPO/"wiki/sweeps/2026-10-09-daily.md"
    if not p.exists(): return
    t = p.read_text(encoding="utf-8")
    if "INGESTED" in t: return
    p.write_text(f"> **INGESTED {DATE} as {WAVE}** — see `wiki/log.md`.\n\n" + t, encoding="utf-8")


def main():
    for e in ENTRIES:
        write_source(e); write_concept(e); write_phase0(e)
    write_entity_sbdtoe()
    write_rule(); append_policy(); write_briefs()
    patch_index(); prepend_log(); patch_sweep()
    print(f"done {WAVE}")


if __name__ == "__main__":
    main()
