#!/usr/bin/env python3
"""Generate K421–K425 wiki ingest artifacts (2026-10-05 daily sweep)."""
from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DATE = "2026-10-05"
BRIEF = "2026-10-05_ccc-k421-k425-sip-ready.md"
EGRESS = "cemini-egress-fi:/opt/cemini-bulk/research/ccc"
RULE = "ccc-k421-k425-phase1-wires.mdc"
WAVE = "K421–K425"

ENTRIES = [
    {
        "arxiv": "2610.02861",
        "concept": "model-is-not-a-security-boundary",
        "k": 421,
        "narrative": (
            "**Containing the Autonomous Operator — agent safety as an infrastructure problem.** The "
            "thesis is one sentence and everything follows from it: **the model is not a security "
            "boundary.** Alignment, system prompts, and input classifiers lower the probability of "
            "misbehavior but guarantee nothing, and their failure modes are adversarially "
            "discoverable. So an agent that operates a Kubernetes cluster must be secured the way "
            "multi-tenant platform security is secured — **assume the workload is hostile and "
            "constrain what it can reach, do, and exfiltrate.** The paper names what breaks: agents "
            "**collapse the data/control separation** that cloud-native security rests on, because "
            "content the agent merely *reads* — a log line, a ticket field, an annotation, a "
            "third-party MCP tool description — can redirect what it *does*. Its central design rule "
            "is to **break the combination of untrusted input, sensitive access, and external "
            "egress**; each alone is survivable, the three together are not. The framework is "
            "seven layers mapped onto native Kubernetes controls: workload identity, RBAC plus "
            "`ValidatingAdmissionPolicy`, gVisor/Kata sandboxing, **FQDN-aware egress policy**, an "
            "**agent/MCP gateway applying policy-as-code over tool arguments**, and eBPF runtime "
            "enforcement. **CCC relevance:** this is the infrastructure-side statement of the same "
            "principle CCC holds at the harness level — *gate the tool step, enforcement is external "
            "and fail-closed, model self-arbitration is not a boundary* (`cemini-invariants.mdc`). "
            "Pairs K402 MCP error surfaces / K403 Tracekit / K395 approval laundering / "
            "`@concepts/schema-bound-mcp-tool-surface.md` / `@concepts/untrusted-model-delegation-"
            "governance.md`. **Routing: cybersec-primary** — brief written to `@cybersecurity-wiki/`; "
            "CCC keeps the tool-boundary-mediation principle. No repo, no measured results (the paper "
            "reports a threat–control matrix and four attack walkthroughs, explicitly no "
            "attack-success or overhead figures). Runtime **`wont_wire`**; concept **`policy_wired`**."
        ),
        "pdf": "arxiv-2610.02861-containing-the-autonomous-operator-a-defense-in.pdf",
        "slug": "arxiv-containing-autonomous-operator-k8s-agent-security-2610.02861",
        "title": "Containing the Autonomous Operator: A Defense-in-Depth Framework and Reference Architecture for Securing AI Agents on Kubernetes",
        "verdict": "ADOPT principle; cybersec-primary",
        "no_clone": "k8s-agent-security",
        "repo": "",
        "snippet": (
            "Content that an agent merely reads—a log line, a ticket, a tool description—can redirect "
            "what it does. This paper argues that the model must not be treated as a security boundary."
        ),
    },
    {
        "arxiv": "2610.03213",
        "concept": "intent-based-tool-call-oversight",
        "k": 422,
        "narrative": (
            "**Cisco — authorize the intent, not just the call.** Conventional authorization asks "
            "whether an agent *may* invoke a tool. It cannot ask whether calling that tool is a "
            "**logical step toward the task's intent**. An allowed call can still be irrelevant, and "
            "a rogue agent can steer a combination of individually-permitted calls away from the "
            "task. The paper extends **Task-Based Access Control** to **intent-based TBAC** and puts "
            "a **small language model in the per-call path**: an SLM scores each selected tool "
            "against the assigned task and emits a relevance signal for downstream enforcement. "
            "That framing is the contribution — **a per-call cognitive check, not a permission "
            "check**, positioned for low latency and on-prem deployment where frontier models are "
            "ruled out by privacy, cost, or policy. Results: a **Gemma-3-4B**, specialized through "
            "`GEPA → SFT → GRPO`, reaches **96.13% end-to-end accuracy / 96.90 F1** against a 95% "
            "operational bar, with FPR 5.42 / FNR 2.94 — from 87.48% base. The 1B model reaches "
            "89.60% and does not clear the bar, so **4B is the floor**. The staged pipeline matters "
            "independently: GEPA, SFT, and GRPO move **false positives and false negatives "
            "differently** — GEPA bought recall at a selectivity cost, SFT restored selectivity, GRPO "
            "balanced both. Pairs K395 approval laundering / K402 MCP error surfaces / K421 tool-boundary "
            "mediation / `@concepts/step-level-tool-guardrails.md`. **Phase-0: the paper's stated repo "
            "`outshift-open/outshift-casa-slm` returns 404** — not published under that name → "
            "**no repo to clone**. Runtime **`wont_wire`**; concept **`policy_wired`**."
        ),
        "pdf": "arxiv-2610.03213-toward-slm-based-agentic-task-tool-intent-matchi.pdf",
        "slug": "arxiv-slm-task-tool-intent-matching-2610.03213",
        "title": "Toward SLM-based agentic task-tool intent matching",
        "verdict": "ADOPT pattern (no repo — 404)",
        "no_clone": "outshift-casa-slm",
        "repo": "",
        "snippet": (
            "Conventional authorization schemes can determine whether an agent is allowed to invoke a "
            "tool, but cannot assess the agent's underlying cognition, specifically, whether the tool "
            "selection represents a logical, relevant step toward satisfying the intent of the task."
        ),
    },
    {
        "arxiv": "2610.03585",
        "concept": "threat-preserving-representation-sensitivity",
        "k": 423,
        "narrative": (
            "**Benchmark validity — the security score depends on how you phrase the threat.** The "
            "paper asks a measurement question with a surprising answer. Take an agent-security "
            "benchmark, change **only the agent-visible representation** — a tool's *name*, its "
            "description — while holding the task, the harmful action, the security policy, the "
            "ground truth, the environment, and the evaluation criteria **fixed**. How stable is the "
            "reported attack success rate? Across **28,904 agent runs** on three independent "
            "benchmarks it is **not stable, and not uniformly**: renaming `DNSPoisoning` to "
            "`DNSConfiguration` **raises** committed ASR by **11.67 points** on GPT-5-mini and "
            "**13.21** on Claude Haiku 4.5; on MCPTox, adding threat wording **lowers** ASR by 11.00 "
            "and 4.11 points. The two are directionally aligned — more threat-explicit naming means "
            "less measured attack success — and the effect is **larger, not smaller, when the threat "
            "is hidden.** A control arm is sharper still: a **threat-neutral** name matched on token "
            "count, length, and casing reproduced **8.54 of the 11.00 points**, so explicit threat "
            "vocabulary is **not** the driver. On AgentDojo the ASR effect was small (0.50 points) "
            "but benign utility fell 5.36 points — **changing the label changed capability too.** "
            "**CCC relevance is direct and it is the K407 lesson generalised:** a score measured "
            "under one representation may not survive a threat-preserving rewrite of the same "
            "problem, so **robustness claims need a controlled set of variants, not a single "
            "number**. Pairs `@concepts/verifiable-deterministic-agent-benchmarking.md` / K407 "
            "(judge variance on byte-identical answers) / K392 (behavior assays) / "
            "`@concepts/low-cost-cross-vendor-behavior-assays.md`. **Cybersec-relevant too** — noted "
            "in their brief. No repo. Runtime **`wont_wire`**; concept **`policy_wired`**."
        ),
        "pdf": "arxiv-2610.03585-threat-preserving-representation-sensitivity-in.pdf",
        "slug": "arxiv-threat-preserving-representation-sensitivity-2610.03585",
        "title": "Threat-Preserving Representation Sensitivity in Agent-Security Benchmarks",
        "verdict": "ADOPT eval-methodology",
        "no_clone": "tprs",
        "repo": "",
        "snippet": (
            "a security score measured under one representation may fail to generalize across "
            "threat-preserving representations of the same security problem."
        ),
    },
    {
        "arxiv": "2610.03631",
        "concept": "graded-reward-ladder-no-model-gates",
        "k": 424,
        "narrative": (
            "**NeutronGym — make the grader a simulator, and gate the tasks before you trust them.** "
            "An executable environment for neutron instrument design where agents build instruments "
            "through 22 validating MCP tools, **McStas ray-traces what they actually built**, and a "
            "**level-resolved ladder** grades it with **no LLM judge**: L1 syntax, L2 runtime, L3 "
            "structure, L4 science. The score **cannot be argued with** — it is a physics "
            "measurement, not an opinion. Two design lessons stand out, and both are about "
            "**distrusting your own benchmark**. First, **no-model admission probes**: before any "
            "pass rate is read as capability, a family must survive the best fixed answer, the best "
            "rule that reads the prompt, and every instance's solution applied to every other — "
            "decided on a one-sided confidence bound. Nine reward failures motivated the protocol and "
            "**four of the authors' own designs failed it.** Second, **contamination probes**: published "
            "instruments ship as example files, and in a pilot audit **4 of 7 agent episodes retrieved "
            "the reference file through ordinary, permitted tools**. Trained results: RL on the ladder "
            "takes Qwen3-8B from **11.3% → 76.7%** on held-out instances, past an untrained 32B; "
            "**removing partial credit collapses it by 60 points**; and imitation of the model's own "
            "successes degraded it three times. **CCC relevance:** the ladder and the no-model gate are "
            "directly transferable eval machinery, and the `wont_wire` finding is the honest one — "
            "frontier models still solve 98–99%, so the trained model matches a classical optimizer "
            "only when handed the closed-form physics. Pairs K406 Assay (mechanical gate) / "
            "`@concepts/verifiable-deterministic-agent-benchmarking.md` / K416 YouRA / K423 TPRS. "
            "No repo surfaced. Runtime **`wont_wire`**; concept **`policy_wired`**."
        ),
        "pdf": "arxiv-2610.03631-neutrongym-physics-graded-neutron-instrument-des.pdf",
        "slug": "arxiv-neutrongym-graded-reward-ladder-2610.03631",
        "title": "NeutronGym: Physics-Graded Neutron Instrument Design for LLM Agents",
        "verdict": "ADOPT eval methodology",
        "no_clone": "neutrongym",
        "repo": "",
        "snippet": (
            "No model is ever asked whether a design is good; the environment measures the design the "
            "agent actually built, which is why the score cannot be argued with."
        ),
    },
    {
        "arxiv": "2610.03675",
        "concept": "cost-aware-program-evolution",
        "k": 425,
        "narrative": (
            "**FrugalEvo — optimize gain per dollar, not gain per iteration.** LLM-guided "
            "evolutionary search (AlphaEvolve and successors) usually reports performance after a "
            "fixed number of iterations, which **conflates capability with spend** — more iterations "
            "means more money, and test-time scaling means a better number may just be a larger "
            "bill. The paper's first contribution is a **metric**: **Budget-Aware AUC**, the area "
            "under the best-so-far score curve plotted against **cumulative LLM cost** up to a "
            "budget. The second is the architecture, and it is the CCC-relevant part: **split "
            "generation across two models.** A strong, expensive LLM proposes **design strategies**; "
            "a cheap LLM **implements them as code and refines it**. The strong model never writes "
            "the bulk of the tokens. On top of that the harness and prompts are **designed to "
            "maximize prefix sharing across evolution steps**, so **prompt caching actually fires** "
            "and cost per iteration drops to **$0.0097 against $0.0210–$0.0435 for the baselines**. "
            "Results: it matches or beats OpenEvolve, ShinkaEvolve, AdaEvolve, and EvoX on final "
            "quality and **wins BA-AUC on 9 of 10** tasks; on circle packing it sets a new SOTA for "
            "**$0.55** (GLM-5.3 + Flash) where comparable multi-agent methods averaged **~$50**. "
            "**CCC relevance is high and it composes with several earlier pages:** the "
            "expensive-planner/cheap-implementer split is K409's Builder/Target and K411's "
            "frontier-designs-for-smaller-models, and the cache-aware harness is the practical "
            "version of `@concepts/token-economics-and-prompt-caching.md` — **structure the prompt "
            "so the cache can hit.** Pairs K405 TokenCast / K320 / K415 instance-adaptive harness / "
            "`@concepts/three-cache-architecture.md`. **Phase-0: `chchenhui/frugalevo` Apache-2.0**, "
            "3★, ~306 MB, pushed 2026-10-04. Licence is clean but the tree is large → **no clone this "
            "wave**; the *method* is the transferable part. Runtime **`wont_wire`**; concept "
            "**`policy_wired`**."
        ),
        "pdf": "arxiv-2610.03675-frugalevo-towards-cost-aware-llm-guided-program.pdf",
        "slug": "arxiv-frugalevo-cost-aware-program-evolution-2610.03675",
        "title": "FrugalEvo: Towards Cost-Aware LLM-Guided Program Evolution",
        "verdict": "ADOPT pattern (Apache-2.0)",
        "no_clone": "frugalevo",
        "repo": "chchenhui/frugalevo",
        "snippet": (
            "we design our harness and prompts to maximize the sharing of prefixes across different "
            "evolution steps, improving cache reuse."
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
description: CCC Phase-1 wires from K421–K425 harness wave (CCC-only — do NOT federation-sync)
alwaysApply: false
---

# CCC — K421–K425 Phase-1 wires

**Brief:** `docs/briefs/{DATE}_k421-k425-harness-wave.md` · SIP: `wiki/briefs/{BRIEF}`

**IDs:** Resolve by arXiv id / slug / file path — K# is a log batch label only.

{bullets}

**Wires landed:**

| K | Verdict | Wire | wire_status |
|---|---|------|-------------|
{rows}

**Non-goals:** no federation sync; no PoCs; no clone of any repo this wave. K421 is cybersec-primary —
brief written to `@cybersecurity-wiki/`.

**Propose-only:** FrugalEvo HITL clone (Apache-2.0, 3★, ~306 MB). `outshift-casa-slm` (K422) returns
404 — do not chase it.
"""
    (REPO / ".cursor/rules" / RULE).write_text(text, encoding="utf-8")


def append_policy():
    path = REPO / ".cursor/rules/cemini-phase1-policy-wires.mdc"
    text = path.read_text(encoding="utf-8")
    if f"CCC wave {WAVE}" in text:
        return
    block = f"""

## CCC wave {WAVE} (shared policy file)

Containing the autonomous operator (K421) + intent-based tool-call oversight (K422) + threat-preserving
representation sensitivity (K423) + graded reward ladder / no-model gates (K424) + cost-aware program
evolution (K425). **Zero clones.** CCC-only rule `{RULE}` — do **not** federation-sync.

## The model is not a security boundary (CCC K421, cybersec-primary)

- **Agent safety is an infrastructure problem.** Assume the agent is fully compromised by prompt
  injection; constrain reach, action, and egress. **Break the combination of untrusted input +
  sensitive access + external egress.** Mediate completely at the **tool boundary** with
  policy-as-code over tool *arguments*. Pairs `cemini-invariants.mdc` ("enforcement is external and
  fail-closed; model self-arbitration is not a boundary"). Runtime **`wont_wire`**.

## Intent-based tool-call oversight (CCC K422)

- **Authorize the intent, not only the call.** A per-call cognitive check asks whether a tool is a
  *relevant step toward the task*, which a permission check cannot. An SLM in the path makes it
  low-latency and on-prem; Gemma-3-4B post-GRPO hits 96.13% E2E vs a 95% bar (1B does not clear it,
  so 4B is the floor). GEPA/SFT/GRPO move FPR and FNR differently. Runtime **`wont_wire`**.

## Threat-preserving representation sensitivity (CCC K423)

- **A security score can move when only the *phrasing* moves.** Renaming a tool from
  `DNSPoisoning` to `DNSConfiguration` **raised** measured ASR by 11.67 points; a length-matched
  neutral control reproduced 8.54 of the 11.00 points, so threat vocabulary is not the driver.
  **Robustness claims need a controlled set of threat-preserving variants, not one number.**
  Generalises K407. Runtime **`wont_wire`**.

## Graded reward ladder + no-model gates (CCC K424)

- **Make the grader a simulator, and gate the tasks before trusting them.** Level-resolved ladder
  (syntax → runtime → structure → science) with **no LLM judge**; **partial credit is what makes it
  trainable** (removing it costs 60 points). Admission protocol: **no-model probes** — best fixed
  answer, best prompt-reading rule, every instance's solution on every other — plus contamination
  probes (4 of 7 pilot episodes retrieved a reference file). Four of the authors' own designs failed
  their gate. Runtime **`wont_wire`**.

## Cost-aware program evolution (CCC K425)

- **Optimize gain per dollar.** Split generation: an expensive model proposes **strategies**, a cheap
  model implements and refines **code**. **Structure the harness and prompts to maximize prefix
  sharing so prompt caching fires** — cost/iteration $0.0097 vs $0.0210–$0.0435. Measure with
  **Budget-Aware AUC** (best-so-far score against cumulative cost). pairs K405/K320/K415 and
  `token-economics-and-prompt-caching`. Runtime **`wont_wire`**.
"""
    path.write_text(text.rstrip() + block + "\n", encoding="utf-8")


def write_briefs():
    docs = REPO / "docs/briefs/2026-10-05_k421-k425-harness-wave.md"
    docs.write_text(
        f"""# {WAVE} harness wave — brief (CCC docs)

Date: {DATE} · SIP: `wiki/briefs/{BRIEF}`

## What changed

Five arXiv ingests from the 2026-10-05 sweep. **Zero clones.**

1. **K421** Containing the Autonomous Operator — K8s agent security (cybersec-primary)
2. **K422** SLM task-tool intent matching — intent-based TBAC (no repo; 404)
3. **K423** TPRS — benchmark validity under threat-preserving rewrites
4. **K424** NeutronGym — graded reward ladder + no-model gates
5. **K425** FrugalEvo — cost-aware program evolution (Apache-2.0)

## Phase-0 / Phase-1

- `adopt_k421`…`k425` — all exit 0
- `{RULE}` + policy §{WAVE}
- Phase-0: `chchenhui/frugalevo` **Apache-2.0** (3★, ~306 MB) · `outshift-open/outshift-casa-slm`
  **404 — not published**. No repo for K421/K423/K424.

## Cross-wiki

- **K421 is cybersec-primary** — brief written to `@cybersecurity-wiki/`. CCC keeps the
  tool-boundary-mediation principle.
- **K423 noted to Cybersec too** — benchmark-validity finding is theirs as well.

## Not routed

- **Minecraft / `dragon-rider-map` (K281 Basgiath)** — checked. None of K421–K425 is game-dev or
  map-design relevant; these are harness, eval, and security papers. No brief manufactured.
- **Game Dev wiki** — same; no match this wave.

## Propose-only

- HITL clone of `chchenhui/frugalevo` (Apache-2.0, ~306 MB) — method is the transferable part
""",
        encoding="utf-8",
    )
    sip = REPO / "wiki/briefs" / BRIEF
    rel = [f"concepts/{e['concept']}.md" for e in ENTRIES] + [f"sources/{e['slug']}.md" for e in ENTRIES]
    sip.write_text(
        f"""---
title: CCC SIP-ready — {WAVE} full ingest
type: brief
tags: [brief, handoff, k421, k422, k423, k424, k425]
keywords: [agent-security, intent-tbac, benchmark-validity, reward-ladder, cost-aware-evolution]
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
| K421 | 2610.02861 | ADOPT principle; cybersec-primary |
| K422 | 2610.03213 | ADOPT pattern (repo 404) |
| K423 | 2610.03585 | ADOPT eval-methodology |
| K424 | 2610.03631 | ADOPT eval methodology |
| K425 | 2610.03675 | ADOPT pattern (Apache-2.0) |
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
    sa = "| [`2026-10-01-daily`](sweeps/2026-10-01-daily.md) | Daily digest — 5 papers (K411–K415 wave) |"
    for d, lab in [("2026-10-02", "5 papers (K416–K420 wave)"),
                   ("2026-10-03", "digest"), ("2026-10-04", "digest"),
                   ("2026-10-05", "5 papers (K421–K425 wave)")]:
        pass
    if sa in text:
        add = "\n| [`2026-10-02-daily`](sweeps/2026-10-02-daily.md) | Daily digest — 5 papers (K416–K420 wave) |"
        add += "\n| [`2026-10-03-daily`](sweeps/2026-10-03-daily.md) | Daily digest |"
        add += "\n| [`2026-10-04-daily`](sweeps/2026-10-04-daily.md) | Daily digest |"
        add += "\n| [`2026-10-05-daily`](sweeps/2026-10-05-daily.md) | Daily digest — 5 papers (K421–K425 wave) |"
        text = text.replace(sa, sa + add, 1)
    idx.write_text(text, encoding="utf-8")


def prepend_log():
    log = REPO / "wiki/log.md"
    entry = f"""## [{DATE}] ingest | {WAVE} harness wave (Oct 5 daily sweep)

- **Sources:** 2610.02861 K8s agent security, 2610.03213 SLM task-tool intent, 2610.03585 TPRS, 2610.03631 NeutronGym, 2610.03675 FrugalEvo.
- **Phase-0:** `chchenhui/frugalevo` Apache-2.0 (3★, ~306 MB); `outshift-open/outshift-casa-slm` **404**. No repo for K421/K423/K424.
- **Phase-1:** adopt_k421…k425; `{RULE}`; policy §{WAVE}. Zero clones.
- **Cross-wiki:** **K421 cybersec-primary** (brief to `@cybersecurity-wiki/`); K423 noted there too.
- **Not routed:** checked the Minecraft project (`dragon-rider-map`, K281 Basgiath) and the Game Dev wiki — **no match this wave**; these are harness/eval/security papers.
- **Standouts:** K423 (a score moves when only the phrasing moves — generalises K407) and K425 (structure prompts so the cache fires; $0.0097 vs $0.0210/iteration).
- **Archive:** egress bulk ccc (5 PDFs). Inbox empty.

"""
    t = log.read_text(encoding="utf-8")
    if f"{WAVE} harness wave" not in t:
        log.write_text(entry + t, encoding="utf-8")


def patch_sweeps():
    for d in ("2026-10-03", "2026-10-04", "2026-10-05"):
        p = REPO / "wiki/sweeps" / f"{d}-daily.md"
        if not p.exists():
            continue
        t = p.read_text(encoding="utf-8")
        if "INGESTED" in t:
            continue
        note = (f"> **INGESTED {DATE} as {WAVE}** — see `wiki/log.md`.\n\n"
                if d == "2026-10-05" else
                f"> Reviewed {DATE} — no ingest (superseded by the {DATE} window).\n\n")
        p.write_text(note + t, encoding="utf-8")


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
    patch_sweeps()
    print(f"done {WAVE}")


if __name__ == "__main__":
    main()
