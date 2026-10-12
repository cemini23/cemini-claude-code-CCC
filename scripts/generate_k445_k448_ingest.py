#!/usr/bin/env python3
"""Generate K445–K448 wiki ingest artifacts + K286/K288 inbound pages (2026-10-12)."""
from __future__ import annotations
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DATE = "2026-10-12"
BRIEF = "2026-10-12_ccc-k445-k448-sip-ready.md"
ROUTE = "2026-10-12_k286-k288-ccc-route.md"
EGRESS = "cemini-egress-fi:/opt/cemini-bulk/research/ccc"
RULE = "ccc-k445-k448-phase1-wires.mdc"
WAVE = "K445–K448"


def E(arxiv, concept, k, slug, title, verdict, no_clone, narrative, snippet, extra):
    pdfs = list((REPO / "research to be indexed").glob(f"*{arxiv}*"))
    return dict(arxiv=arxiv, concept=concept, k=k, slug=slug, title=title, verdict=verdict,
                no_clone=no_clone, narrative=narrative, snippet=snippet, extra=extra,
                pdf=pdfs[0].name if pdfs else f"arxiv-{arxiv}.pdf")


ENTRIES = [
 E("2610.13623", "shared-workspace-injection-task-completion-not-safety", 445,
   "arxiv-apex-harm-shared-workspace-agent-safety-2610.13623",
   "APEX-Harm: Evaluating Agent Safety in Shared Professional Workspaces",
   "ADOPT eval-methodology (shared-workspace injection)",
   "apex-harm",
   "**Completing the task is not evidence of safe behavior.** A benchmark for **prompt and script "
   "injection against long-horizon CLI agents in shared professional workspaces** (investment "
   "banking, law, consulting) — 115–328 files per task, 63 tools over MCP (mail, chat, calendar, "
   "docs, sheets, PDFs, code-exec), 12 frontier models, 180 instances. **Six attack categories**: "
   "static prompt injection, static script injection, **dynamic** prompt/script injection (a "
   "background `inotify` watcher hides a file after the agent reads it and plants a corrupted "
   "replacement that points at attacker code), task-specific script replacement, and "
   "attacker-provided generic script. **Headline:** Opus 5 and Sonnet 5 are most robust (**8% / 20%** "
   "average ASR), but **task-specific replacement and attacker-provided generic scripts stay "
   "effective at 81–84% and 73% ASR**. Gemini 3.8 Flash has the highest task score (**0.877**) with a "
   "**33% ASR** — the two axes are independent: *an agent can produce a correct deliverable while "
   "performing an unauthorized action*. **Two transferable findings for the harness:** (1) "
   "**readability governs refusal** — Python scripts have the lowest ASR because the agent can `cat` "
   "the source, while **PYC/ELF are executed unread** (they must be decompiled), so *do not hand an "
   "agent an unreadable artifact plus permission to run it*; (2) **internal leakage is under-guarded** "
   "— agents refuse email / external-link disclosure but treat sharing through shared folders and "
   "calendars as a benign workflow step. **CCC reading:** the shared-workspace threat model is the "
   "multi-MCP reality, and the core rule — *task success and safety are separate measurements* — is "
   "the same conclusion as K441 (score conformance, not just absence of failure) and K442 (accuracy ≠ "
   "humility). Pairs `agent-approval-laundering-transitive-effects` / `agent-data-injection-attacks`. "
   "**Code released** (Apex-Agents harness); no install this wave. Runtime `wont_wire`; concept "
   "`policy_wired`.",
   "an agent can produce a correct deliverable while also performing an unauthorized action in the workspace.",
   ["concepts/agent-approval-laundering-transitive-effects.md",
    "concepts/agent-data-injection-attacks.md",
    "concepts/mcp-app-hitl-approval-gap.md",
    "concepts/authorization-to-effect-closure.md"]),

 E("2610.13651", "tool-metadata-as-security-contract", 446,
   "arxiv-tofu-orchestrator-tool-trust-boundary-2610.13651",
   "ToFu: Exploiting and Fuzzing the LLM-Orchestrator-Tool Trust Boundary",
   "ADOPT pattern (MCP tool security)",
   "ToFu",
   "**A tool call is a structured model output the orchestrator executes — so schema-valid arguments "
   "are untrusted by default.** ToFu attacks the **LLM–orchestrator–tool trust boundary**. The "
   "**Repeat-After-Me** attack: an attacker writes text that names a tool and its arguments, tells "
   "the model to repeat it verbatim, and the orchestration layer parses the model's output as a tool "
   "call and dispatches it — reproduced on six orchestrators (LangGraph, MAF, ADK 2.0, AutoGen, "
   "Strands, CrewAI). **Schema conformity is not trust.** The paper's insight: the **metadata that "
   "guides an LLM to use a tool can also guide a fuzzer to test it**. ToFu derives tool-specific "
   "**semantic security checks** from the tool's own description plus a **CWE-guided sanitizer "
   "corpus**, generates schema-valid fuzzing harnesses and **semantic oracles** (runtime "
   "introspection for in-process tools; **outcome oracles** for opaque ones), and finds **253 verified "
   "bugs across 343 tools in 118 of 273 MCP servers** (reflected output 115, path traversal 64, log "
   "injection 58, SSRF 7, exfiltration 5, command injection 3). The LLM is confined to **sanitizer "
   "mapping and seed generation** — it is never the oracle. **CCC reading:** three rules to keep. (1) "
   "**Treat every schema-valid tool argument as adversarial** — the orchestrator establishes "
   "structural validity, not semantic safety; a sandbox is not optional (four servers modified the "
   "*fuzzing host*). (2) **Tool metadata should be an enforceable security contract**, validated in "
   "the tool, not delegated to the model or the orchestration layer. (3) **LLM selection buys bug "
   "*classes*; seeds buy *reach*** — with both LLM stages removed ToFu still kept two-thirds of its "
   "bugs, so the structural corpus is the load-bearing part. Pairs `implicit-trust-mcp-input-"
   "channels` / `mcp-tool-metadata-supply-chain-risk` / `mcp-contract-grounded-synthesis-and-"
   "validation-gate` / `hybrid-static-dynamic-mcp-tool-security`. **No repo URL** (cs.CR). Runtime "
   "`wont_wire`; concept `policy_wired`.",
   "real-world LLM tools frequently fail to enforce the semantic contracts exposed by their interfaces.",
   ["concepts/implicit-trust-mcp-input-channels.md",
    "concepts/mcp-tool-metadata-supply-chain-risk.md",
    "concepts/mcp-contract-grounded-synthesis-and-validation-gate.md",
    "concepts/hybrid-static-dynamic-mcp-tool-security.md",
    "concepts/schema-bound-mcp-tool-surface.md"]),

 E("2610.13862", "code-enforces-decisions-multi-fidelity-eval", 447,
   "arxiv-bt-agent-behavior-trees-onboard-2610.13862",
   "BT-Agent: Deploying Onboard Robot Agents with Behavior Trees and Multi-Fidelity Evaluation",
   "ADOPT pattern (harness split + multi-fidelity eval)",
   "BT-Agent",
   "**Let code enforce the conditions and let the model decide — then evaluate on more than one "
   "fidelity.** BT-Agent separates **task-level model reasoning** from **reactive execution** through "
   "predefined **behavior-tree (BT) skills**. An onboard **Actor** (ReAct loop) selects a skill and "
   "arguments; a **supervisor BT** runs one skill at a time; and each skill's **local guards recheck "
   "cancellation, time and preconditions on every tick and can interrupt a running action without "
   "another model call** — measured **19 ms** to commanded-zero velocity vs **3.2–3.9 s** for the "
   "next model decision. **The Actor cannot modify a skill's implementation or its guards**, so the "
   "logic is reviewable and testable independently of the policy. **Ablations name the two harness "
   "levers:** replacing **structured tool calls** with textual commands lowers success at every size "
   "(smallest models worst), and **removing informative failure feedback costs 2–6 points**. "
   "**Multi-fidelity evaluation:** a 161-task **text** benchmark vs 39 paired **Habitat** tasks — "
   "text runs **10.9× faster** (950 vs 87 episodes/hour), but **text success does not establish "
   "completion under sensing and motion** (only **57.3%** of text successes succeed in Habitat; "
   "Spearman ρ = 0.61), and **fault injection exposes failures that nominal success hides** (at 27B a "
   "nominal tie with ReAct becomes a BT-Agent lead under injected faults). A 9B model runs fully "
   "onboard on a Spot. **CCC reading:** the split is K436/K447's 'code enforces, model decides' shape "
   "— the same family as K444's L3 gate and K443's explicit-state policy — and the multi-fidelity "
   "lesson is the cheap-proxy caveat: **a fast text proxy ranks well but does not prove the "
   "deployable behavior** (pairs K438's cheap-proxy correlation finding). Reported under "
   "**Apache-2.0** (promised). Runtime `wont_wire`; concept `policy_wired`.",
   "text supports 10.9 higher evaluation throughput, while simulation reveals how perception and motion failures change task outcomes.",
   ["concepts/agent-completion-verification-gates.md",
    "concepts/agent-harness-operational-definition.md",
    "concepts/harness-security-axis-comparison.md",
    "concepts/test-time-world-model-validate-before-act.md"]),

 E("2610.13886", "cross-service-compositional-harm-graph", 448,
   "arxiv-x-agentred-cross-service-red-teaming-2610.13886",
   "X-AgentRed: Red-Teaming Personal Agents in Evolving Multi-Service Ecosystems",
   "ADOPT pattern (cross-service composition risk)",
   "X-AgentRed",
   "**Compose many tools across services and the failure is compositional — so explore the "
   "composition graph, not the model's memory.** X-AgentRed red-teams **personal agents in a "
   "multi-service ecosystem** (30 services, 914 tools). The finding: when a benign request drives "
   "actions whose effects **accumulate across services**, unintended or harmful outcomes arise, and "
   "**an LLM asked to propose harmful paths is biased toward familiar tools**, leaving novel "
   "cross-service combinations unexplored. The fix is structural: a **HarmFlow graph** built from "
   "each tool's **preconditions, effects and potential harms** (an edge where one tool's effect "
   "satisfies another's precondition), from which recipes are sampled by **backward random walks** "
   "and instantiated as benign-looking scenarios; execution feedback then **diversifies** successful "
   "paths by substituting adjacent tools and **refines** blocked paths by repairing unmet "
   "preconditions. Results: **1.77× / 10.36× the harmful-path rate of STAC / TRACE** and **2.99× / "
   "1.84× tool coverage**; diversification reaches **27.7%** HPR vs **18.0%** for random sampling. "
   "**CCC reading:** this is the multi-MCP composition risk the CCC harness lane trades on — *a "
   "per-tool analysis cannot see harm that exists only in the sequence*, and **graph traversal beats "
   "model recall** for finding those sequences. It also validates the K444/K447 principle that **the "
   "structure, not the model, is where you get coverage**. Pairs `agent-data-injection-attacks` / "
   "`hybrid-mcp-tool-discovery-lazy-catalog` / `mcp-tool-taxonomy-navigation`. Cross-domain "
   "REFERENCE. Runtime `wont_wire`; concept `policy_wired`.",
   "an agent fulfilling a benign user request can leak information as its actions interact across services.",
   ["concepts/agent-data-injection-attacks.md",
    "concepts/hybrid-mcp-tool-discovery-lazy-catalog.md",
    "concepts/mcp-tool-taxonomy-navigation.md",
    "concepts/agent-approval-laundering-transitive-effects.md"]),
]

# ---- inbound pages (K286 typed-judgement desk; K288 decision-models + NOMOS) ----
INBOUND = [
 dict(
   concept="typed-judgement-desk-pattern",
   title="Typed-judgement desk — code fetches, the model judges, code decides (K286 + K288)",
   tags="[concept, k286, k288, decision-models]",
   keywords="[jev, typed-judgement, decision-model, pplx-decider, unsloth]",
   extra=["concepts/nomos-compiled-tool-call-gate.md",
          "concepts/overclaiming-propensity-agent-measurement.md"],
   narrative=(
   "**Code fetches, the model judges, code decides.** A **typed decision engine** replaces the agent "
   "seat's prose opinion: send state + typed questions, receive typed answers with probabilities. "
   "Three question types are the whole API — `noul` (an if, with probability), `choice` (a switch), "
   "`score` (a rank). The caller reads a number, applies a threshold, and writes **no parser**. "
   "**Four rules:** arithmetic stays in code; **facts kill before judgements** (cheap free/trade/"
   "chain kills before one soft-kill judgement call); **question sets, not single questions** (state "
   "is charged once per call, output is free); and **shadow mode with disagreement rows** (log "
   "would-be actions plus what the old logic did, and read only the disagreements). **K288 update — "
   "it became a category:** the pattern went industry-wide in two days (OpenAI Decisions API, "
   "Microsoft-Decision-1, Perplexity `pplx-decider-v1.1-27b`, Cloudflare `clef`, Liquid `d1`, vLLM "
   "Semantic Router Decision 2.0, LangSmith), and the recipe is now **portable to a 4B model on 8GB "
   "VRAM** (Unsloth) — the desk does **not** need a vendor API. **Two numbers to keep:** routing each "
   "task to the cheapest adequate model cut median Open SWE cost per task by **64%**; and **agent "
   "teams cost 1.8–5.1× more for little gain** (Vals AI: only Sol at medium effort improved) — *the "
   "judge is worth it; a bigger team of judges is not*. **The gap it names in our desk:** we run Jev "
   "(`jev-mcp`) and the Grok Bot charters, but **no charter routes its judgement through the engine** "
   "— every seat judges in prose. **Boundary:** advisory only; **no trading egress** (Jev is a "
   "judgement service, not execution); no `/route` swap. Runtime `wont_wire`; concept "
   "`policy_wired`."),
   snippet="The judge row is the gap. Our seats take the model's opinion; the pattern replaces it with a typed probability."),

 dict(
   concept="nomos-compiled-tool-call-gate",
   title="NOMOS — compile the policy, verify it statically, gate the call (K288)",
   tags="[concept, k288, mcp, security]",
   keywords="[2610.11030, nomos, tool-call-gate, deterministic]",
   extra=["concepts/streaming-trajectory-monitor-pre-execution-gate.md",
          "concepts/llms-are-not-world-models.md",
          "concepts/implicit-trust-mcp-input-channels.md"],
   narrative=(
   "**Compile the policy once, verify it statically, enforce it in code — a deterministic, LLM-free "
   "tool-call gate.** NOMOS answers K285's 'guardrails are not the answer': a compiler turns a "
   "**written agent policy** into a **runtime gate with no LLM** in four passes — PARSE → EXTRACT "
   "(the *only* LLM pass; N=5 majority vote) → **RESOLVE** (deterministic static checks: "
   "self-blocking reachability, argument–signature consistency, domain satisfiability, state "
   "contradictions, write-scope correctness) → MATERIALIZE. The runtime gate evaluates each proposed "
   "tool call against **facts taken only from real tool results and user turns** and returns "
   "allow/block in **microseconds with zero LLM**. **Results:** violations among state-changing calls "
   "**66.3% → 2.6%** (airline) and **30.8% → 6.9%** (retail); **AgentDojo banking ASR 0.0%** (288 "
   "pairs) vs **46.5%** undefended; pass^5/pass^1 **0.51 → 0.67**. A prompt-level reimplementation "
   "costs **+74% wall-clock and 347 LLM calls** vs **3 µs and zero**. **The caution that matters:** "
   "RESOLVE **repairs 37% and rejects 13%** of extracted rules — **generated policy is wrong about a "
   "third of the time**, so **policy extraction must be statically verified, never trusted**: *an "
   "LLM-written policy is an input to a checker, not a control*. **CCC reading:** this is the "
   "mechanism-level twin of K444's **L3 pre-execution gate** — the same shape (block an irreversible "
   "call whose prerequisites are missing), but NOMOS is the *compiler* that turns prose policy into "
   "that gate and the *static verifier* that makes it trustworthy. Pairs `streaming-trajectory-"
   "monitor-pre-execution-gate` (K444) / `llms-are-not-world-models` (K285) / `implicit-trust-mcp-"
   "input-channels`. Cross-wiki: cybersec-primary. **Implementation proprietary, not released** "
   "(DOI `10.5281/zenodo.22123419`). Runtime `wont_wire`; concept `policy_wired`."),
   snippet="An LLM-written policy is an input to a checker, not a control."),
]


def yl(items): return "\n".join(f"  - {x}" for x in items)


def write_source(e):
    k = e["k"]
    rel = [f"concepts/{e['concept']}.md"] + e["extra"] + [f"briefs/{BRIEF}"]
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
| **Retrieved** | {DATE} |

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


def write_inbound(p):
    rel = list(p["extra"]) + ["concepts/phase1-adopt-wire.md", f"briefs/{ROUTE}"]
    (REPO/"wiki/concepts"/f"{p['concept']}.md").write_text(f"""---
title: "{p['title']}"
type: concept
tags: {p['tags']}
keywords: {p['keywords']}
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

Routed inbound via `@osint-wiki` K286 / K288 (CCC-home desks), delivered in `briefs/`. Canon stays
on OSINT.

## Narrative

{p['narrative']}

## Snippets

> "{p['snippet']}" [Source: OSINT K286/K288 briefs (retrieved {DATE})]
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
description: CCC Phase-1 wires from K445–K448 wave + K286/K288 inbound (CCC-only — do NOT federation-sync)
alwaysApply: false
---

# CCC — K445–K448 Phase-1 wires

**Brief:** `docs/briefs/{DATE}_k445-k448-harness-wave.md` · SIP: `wiki/briefs/{BRIEF}`

**IDs:** Resolve by arXiv id / slug / file path — K# is a log batch label only.

{bl}
- **K286/K288 inbound** — typed judgement desk (`typed-judgement-desk-pattern`) + NOMOS gate
  (`nomos-compiled-tool-call-gate`), routed via `briefs/`.

**Wires landed:**

| K | Verdict | Wire | wire_status |
|---|---|------|-------------|
{rows}
| K286/K288 | FILE (inbound) | typed judgement desk + NOMOS gate | `policy_wired` |

**Non-goals:** no federation sync; no PoCs; no clone of any repo this wave. K445/K446/K448 are
**cs.CR** (cybersec-adjacent) — CCC keeps the harness/MCP angle; K447 reports **Apache-2.0**
(promised). NOMOS implementation is **proprietary, not released**.
""", encoding="utf-8")


def append_policy():
    p = REPO/".cursor/rules/cemini-phase1-policy-wires.mdc"; t = p.read_text(encoding="utf-8")
    if f"CCC wave {WAVE}" in t: return
    p.write_text(t.rstrip() + f"""

## CCC wave {WAVE} (shared policy file)

Shared-workspace injection (K445) + tool-metadata-as-security-contract (K446) + code-enforces /
multi-fidelity eval (K447) + cross-service compositional harm (K448) + K286/K288 inbound
(typed-judgement desk, NOMOS gate). **Zero clones.** CCC-only rule `{RULE}` — do **not**
federation-sync.

## Task completion is not safety evidence (CCC K445)

- **A correct deliverable can hide an unauthorized action.** Shared-workspace prompt/script
  injection: Opus 5 / Sonnet 5 most robust (8% / 20% ASR), but **task-specific script replacement and
  attacker-provided generic scripts stay at 81–84% / 73% ASR**. **Readability governs refusal** — the
  agent can `cat` Python but not PYC/ELF, so **never hand the agent an unreadable artifact plus
  permission to run it**. **Internal leakage is under-guarded** (shared folders/calendars read as
  benign). Runtime **`wont_wire`**.

## Tool metadata as security contract (CCC K446)

- **A tool call is model output the orchestrator executes.** Repeat-After-Me (repeat a tool-call
  string verbatim) works on six orchestrators. ToFu finds **253 bugs in 118 of 273 MCP servers** from
  the tool's own metadata + a CWE sanitizer corpus. **Treat every schema-valid argument as
  adversarial**; the tool must enforce its documented contract, not the model. Sandbox the fuzzer.
  Runtime **`wont_wire`**.

## Code enforces, model decides + multi-fidelity eval (CCC K447)

- **Local guards interrupt without a model call** (19 ms vs 3.2–3.9 s). Structured tool calls and
  informative failure feedback are the two named levers. **Text eval 10.9× faster but does not prove
  deployable behavior** (57.3% of text successes transfer; ρ = 0.61); fault injection exposes what
  nominal success hides. Runtime **`wont_wire`**.

## Cross-service compositional harm (CCC K448)

- **Harm that exists only in the sequence is invisible per-tool.** A **HarmFlow graph** (preconditions
  ↔ effects) sampled by backward walks beats LLM-proposed paths: **1.77× / 10.36×** the harmful-path
  rate, **2.99×** tool coverage. Graph traversal, not model recall, is where coverage comes from.
  Runtime **`wont_wire`**.

## Typed judgement desk + NOMOS gate (CCC K286/K288 inbound)

- **Code fetches, a typed engine judges, code decides.** `noul`/`choice`/`score`; facts kill before
  judgements; question sets not single questions; shadow mode with disagreement rows. K288: it became
  a category and is portable to a **4B / 8GB** model. **NOMOS**: compile prose policy → **deterministic
  LLM-free tool-call gate** (violations 66.3% → 2.6%; AgentDojo ASR 0.0%). **Caution:** RESOLVE
  repairs 37% / rejects 13% of rules — *an LLM-written policy is an input to a checker, not a
  control*. Runtime **`wont_wire`**.
""", encoding="utf-8")


def write_route_brief():
    (REPO/"wiki/briefs"/ROUTE).write_text(f"""---
title: CCC route — K286/K288 inbound (typed-judgement desk + NOMOS)
type: brief
handoff: true
tags: [brief, handoff, route, k286, k288]
keywords: [typed-judgement, decision-models, nomos, tool-call-gate]
related:
{yl(['concepts/typed-judgement-desk-pattern.md',
      'concepts/nomos-compiled-tool-call-gate.md',
      'concepts/streaming-trajectory-monitor-pre-execution-gate.md',
      'concepts/phase1-adopt-wire.md'])}
maturity: draft
created: {DATE}
updated: {DATE}
---

## Target

CCC wiki — two inbound briefs delivered by OSINT (K286 typed-judgement desk, K288 decision-models +
NOMOS), filed as concept pages.

## Inbound briefs

| Brief (repo `briefs/`) | Filed as |
|---|---|
| `2026-10-08_jev-typed-judgement-desk.md` | `concepts/typed-judgement-desk-pattern.md` |
| `2026-10-10_k288-decision-models.md` | `concepts/typed-judgement-desk-pattern.md` (K288 update) |
| `2026-10-10_k288-nomos-toolcall-gates.md` | `concepts/nomos-compiled-tool-call-gate.md` |

## Note

K288 also delivered a cybersec-home copy of the NOMOS brief; the gate pairs the K444 L3 pre-execution
gate and is filed in CCC as a concept (`wont_wire` runtime; cybersec is canonical for the exploit
side).
""", encoding="utf-8")


def write_briefs():
    (REPO/"docs/briefs"/f"{DATE}_k445-k448-harness-wave.md").write_text(f"""# {WAVE} harness wave — brief (CCC docs)

Date: {DATE} · SIP: `wiki/briefs/{BRIEF}` · Route: `wiki/briefs/{ROUTE}`

## What changed

Four arXiv ingests from the 2026-10-12 sweep, plus two inbound-brief pages (K286/K288). **Zero clones.**

1. **K445** APEX-Harm — shared-workspace injection; task completion is not safety evidence
2. **K446** ToFu — LLM–orchestrator–tool trust boundary; metadata as an enforceable contract
3. **K447** BT-Agent — code enforces / model decides; multi-fidelity evaluation
4. **K448** X-AgentRed — cross-service compositional harm via a dependency graph
5. **K286/K288** typed-judgement desk + NOMOS deterministic gate

## Phase-0 / Phase-1

- `adopt_k445`…`k448` — all exit 0 · `{RULE}` + policy §{WAVE}
- Phase-0: K445 **code released** (Apex-Agents harness); K446/K448 **no repo URL**; K447
  **Apache-2.0** (promised); NOMOS **proprietary, not released**.

## Cross-wiki

- **K445, K446, K448 are cs.CR (cybersec-adjacent)** → steal briefs to `@cybersecurity-wiki/`
  (CCC keeps the harness/MCP-orchestration angle).

## Propose-only

- A **read-before-execute** rule for opaque script artifacts (PYC/ELF) from K445.
- A **tool-metadata contract check** on the CCC MCP surface from K446.
""", encoding="utf-8")
    rel = [f"concepts/{e['concept']}.md" for e in ENTRIES] + [f"sources/{e['slug']}.md" for e in ENTRIES]
    rel += ["concepts/typed-judgement-desk-pattern.md", "concepts/nomos-compiled-tool-call-gate.md"]
    (REPO/"wiki/briefs"/BRIEF).write_text(f"""---
title: CCC SIP-ready — {WAVE} full ingest + K286/K288 inbound
type: brief
handoff: true
tags: [brief, handoff, k445, k446, k447, k448, k286, k288]
keywords: [shared-workspace-injection, tool-metadata-contract, multi-fidelity, compositional-harm, typed-judgement, nomos]
related:
{yl(rel + ['concepts/phase1-adopt-wire.md'])}
maturity: draft
created: {DATE}
updated: {DATE}
---

## Target

Full ingest of **4 NEW** inbox PDFs as **CCC {WAVE}**, plus two inbound-brief pages (K286/K288).
Phase-0 + Phase-1, archive, lint, commit, push, CI green.

## Inbox

| K | arXiv | Verdict |
|---|-------|---------|
| K445 | 2610.13623 | ADOPT eval-methodology — shared-workspace injection |
| K446 | 2610.13651 | ADOPT pattern — tool metadata as contract |
| K447 | 2610.13862 | ADOPT pattern — code enforces / multi-fidelity eval |
| K448 | 2610.13886 | ADOPT pattern — cross-service compositional harm |
""", encoding="utf-8")


def patch_index():
    idx = REPO/"wiki/index.md"; t = idx.read_text(encoding="utf-8")
    if ENTRIES[0]["slug"] in t: return
    ac = "| [`assay-content-addressed-evidence-graphs`]"
    if ac not in t: ac = "| [`htn-planning-mcp-multi-server-coordination`]"
    for e in ENTRIES:
        row = f"| [`{e['concept']}`](concepts/{e['concept']}.md) | draft | {e['title'][:48]}… — {e['arxiv']} (K{e['k']}) |"
        t = t.replace(ac, row + "\n" + ac, 1)
    for p in INBOUND:
        row = f"| [`{p['concept']}`](concepts/{p['concept']}.md) | draft | {p['title'][:48]}… (K286/K288 inbound) |"
        t = t.replace(ac, row + "\n" + ac, 1)
    as_ = "| [`arxiv-assay-content-addressed-evidence-graphs-2609.36170`]"
    if as_ not in t: as_ = "| [`arxiv-htn-planning-mcp-multi-server-coordination-2609.33731`]"
    for e in ENTRIES:
        row = f"| [`{e['slug']}`](sources/{e['slug']}.md) | draft | {e['title'][:52]}… — {e['arxiv']} |"
        t = t.replace(as_, row + "\n" + as_, 1)
    sa = "| [`2026-10-09-daily`](sweeps/2026-10-09-daily.md)"
    if sa in t and "2026-10-12-daily" not in t:
        t = t.replace(sa, sa + "\n| [`2026-10-12-daily`](sweeps/2026-10-12-daily.md) | Daily digest — K445–K448 wave |", 1)
    idx.write_text(t, encoding="utf-8")


def prepend_log():
    log = REPO/"wiki/log.md"
    entry = f"""## [{DATE}] ingest | {WAVE} wave (Oct 12 sweep) + K286/K288 inbound

- **Sources:** 2610.13623 APEX-Harm (shared-workspace injection), 2610.13651 ToFu (orchestrator–tool trust boundary), 2610.13862 BT-Agent (behavior trees + multi-fidelity eval), 2610.13886 X-AgentRed (cross-service compositional harm).
- **New pages:** 4 arxiv sources + 4 concepts (shared-workspace-injection-task-completion-not-safety, tool-metadata-as-security-contract, code-enforces-decisions-multi-fidelity-eval, cross-service-compositional-harm-graph); **2 inbound pages** (typed-judgement-desk-pattern [K286+K288], nomos-compiled-tool-call-gate [K288]); SIP `wiki/briefs/{BRIEF}` + route `wiki/briefs/{ROUTE}`.
- **Phase-0:** `adopt_k445`…`k448` all exit 0. K447 **Apache-2.0** (promised); K445 code released; K446/K448 no repo URL; NOMOS proprietary. **Zero clones.**
- **Phase-1:** `{RULE}` + policy §{WAVE}. Runtime `wont_wire` for all; concepts `policy_wired`.
- **Standouts:** K445's **task completion ≠ safety** (81–84% ASR on script-replacement attacks; readability governs refusal); K446's **253 bugs in 118/273 MCP servers** and metadata-as-contract; K447's **19 ms guard interrupt** + text→Habitat **57.3%** transfer; K448's **1.77×/10.36×** harmful-path rate via the HarmFlow graph; K288's **NOMOS** deterministic gate (66.3% → 2.6%).
- **Cross-wiki:** K445/K446/K448 cs.CR → steal briefs to `@cybersecurity-wiki/` (CCC keeps the harness/MCP angle).
- **Archive:** pending — see below.

"""
    t = log.read_text(encoding="utf-8")
    if f"{WAVE} wave (Oct 12 sweep)" not in t: log.write_text(entry + t, encoding="utf-8")


def patch_sweep():
    p = REPO/"wiki/sweeps/2026-10-12-daily.md"
    if not p.exists(): return
    t = p.read_text(encoding="utf-8")
    if "INGESTED" in t: return
    p.write_text(f"> **INGESTED {DATE} as {WAVE}** — see `wiki/log.md`.\n\n" + t, encoding="utf-8")


def write_cybersec_briefs():
    base = REPO.parent / "Cybersecurity wiki" / "briefs"
    if not base.exists(): return
    common = f"**Date:** {DATE} · `@ccc-wiki` harness/MCP angle kept in CCC\n\n## NO-GO\n\n- No exploit payloads or PoC code.\n\n"
    (base/f"{DATE}_k445-apex-harm-shared-workspace-steal-from-ccc.md").write_text(f"""# K445 — Shared-workspace injection against long-horizon agents (from CCC)

**Date:** {DATE} · arXiv 2610.13623 · CCC `@ccc-wiki/concepts/shared-workspace-injection-task-completion-not-safety.md`

## Summary
APEX-Harm: prompt/script injection against CLI agents in shared professional workspaces (115–328 files,
63 MCP tools). Opus 5 / Sonnet 5 most robust (8% / 20% ASR); **script-replacement and
attacker-provided generic scripts stay 81–84% / 73% ASR**; Gemini 3.8 Flash highest task score (0.877)
at 33% ASR.

## Steal for the cyber lab
1. **Task completion is not safety evidence** — a correct deliverable can hide an unauthorized action.
2. **Readability governs refusal** — Python is `cat`-able (low ASR); **PYC/ELF execute unread** (high
   ASR). Never hand an agent an opaque artifact plus run permission.
3. **Internal leakage is under-guarded** — shared folders / calendars read as benign workflow.
4. **Dynamic attacks** — an `inotify` watcher hides a file after read and plants a corrupted
   replacement pointing at attacker code.

## NO-GO
- No exploit payloads or PoC code.

## Cross-wiki
Primary: `@ccc-wiki/concepts/shared-workspace-injection-task-completion-not-safety.md`
""", encoding="utf-8")
    (base/f"{DATE}_k446-tofu-orchestrator-tool-boundary-steal-from-ccc.md").write_text(f"""# K446 — The LLM–orchestrator–tool trust boundary (from CCC)

**Date:** {DATE} · arXiv 2610.13651 · CCC `@ccc-wiki/concepts/tool-metadata-as-security-contract.md`

## Summary
ToFu: a tool call is model output the orchestrator executes. The **Repeat-After-Me** attack (repeat a
tool-call string verbatim) works on six orchestrators. Semantic, not crash-based, bugs: **253 verified
bugs across 343 tools in 118 of 273 MCP servers** (reflected output 115, path traversal 64, log
injection 58, SSRF 7, exfiltration 5, command injection 3).

## Steal for the cyber lab
1. **Treat every schema-valid tool argument as adversarial** — the orchestrator gives structural
   validity, not semantic safety.
2. **Tool metadata is an enforceable security contract**, validated in the tool.
3. **Sandbox the fuzzer** — four servers modified the fuzzing host during evaluation.

## NO-GO
- No exploit payloads or PoC code.

## Cross-wiki
Primary: `@ccc-wiki/concepts/tool-metadata-as-security-contract.md`
""", encoding="utf-8")
    (base/f"{DATE}_k448-x-agentred-compositional-harm-steal-from-ccc.md").write_text(f"""# K448 — Cross-service compositional harm in personal agents (from CCC)

**Date:** {DATE} · arXiv 2610.13886 · CCC `@ccc-wiki/concepts/cross-service-compositional-harm-graph.md`

## Summary
X-AgentRed red-teams personal agents over 30 services / 914 tools. **Harm that exists only in the
sequence is invisible per-tool.** A **HarmFlow graph** (preconditions ↔ effects) sampled by backward
walks beats LLM-proposed paths: **1.77× / 10.36×** the harmful-path rate of STAC / TRACE, **2.99×** tool
coverage.

## Steal for the cyber lab
1. **Per-tool analysis cannot see compositional harm** — trace the dependency graph.
2. **Graph traversal beats model recall** for novel cross-service combinations.
3. Execution feedback **diversifies** successful paths (tool substitution) and **refines** blocked ones
   (repair unmet preconditions).

## NO-GO
- No exploit payloads or PoC code.

## Cross-wiki
Primary: `@ccc-wiki/concepts/cross-service-compositional-harm-graph.md`
""", encoding="utf-8")


def main():
    for e in ENTRIES:
        write_source(e); write_concept(e); write_phase0(e)
    for p in INBOUND:
        write_inbound(p)
    write_rule(); append_policy(); write_briefs(); write_route_brief()
    patch_index(); prepend_log(); patch_sweep(); write_cybersec_briefs()
    print(f"done {WAVE} + inbound")


if __name__ == "__main__":
    main()
