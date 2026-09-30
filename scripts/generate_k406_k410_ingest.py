#!/usr/bin/env python3
"""Generate K406–K410 wiki ingest artifacts (Sep 30 daily sweep)."""
from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DATE = "2026-09-30"
BRIEF = "2026-09-30_ccc-k406-k410-sip-ready.md"
EGRESS = "cemini-egress-fi:/opt/cemini-bulk/research/ccc"
RULE = "ccc-k406-k410-phase1-wires.mdc"
WAVE = "K406–K410"

ENTRIES = [
    {
        "arxiv": "2609.36170",
        "concept": "assay-content-addressed-evidence-graphs",
        "k": 406,
        "narrative": (
            "**Assay — claims decay with the code.** Every agent claim (tests pass, no secrets, "
            "behavior preserved) is bound to the **Merkle hash of the dependency cone** of the code it "
            "covers. Staleness becomes a hash comparison, not a judgment. **Blast radius == staleness "
            "frontier** (Prop. 3): the reach an agent wants before editing and the evidence a gate "
            "wants voided after are the same set, from one traversal. Adds a **merge gate that consults "
            "no model** — eight mechanical checks: coverage, freshness, signatures, exit codes, "
            "plausibility, **evidence monotonicity** (the mechanical form of \"do not delete the failing "
            "test\"), and review status. Blocks 9/9 scripted adversarial behaviors (self-approval, "
            "forged ledger, deleted failing test, stale evidence). A **600-token brief costs 14×–114× "
            "less** than an exploration proxy. Ships a **dependency-free Python CLI, git hooks, and an "
            "MCP server**. Pairs K403 Tracekit (tamper-evident audit) / K394 trace tampering / K402 MCP "
            "error surfaces / K405 TokenCast + K320 context cost / reward-tampering literature. "
            "**Phase-0: Apache-2.0**, 0 stars, pushed 2026-09-27, no community vetting yet. "
            "Runtime **`wont_wire`** — MCP server transport/auth needs its own audit before wiring. "
            "Concept **`policy_wired`**."
        ),
        "pdf": "arxiv-2609.36170-assay-claims-that-decay-with-the-code-content-ad.pdf",
        "slug": "arxiv-assay-content-addressed-evidence-graphs-2609.36170",
        "title": "Assay: Claims That Decay With the Code. Content-Addressed Evidence Graphs for Accountable AI-Assisted Software Delivery",
        "verdict": "CONDITIONAL-GO (Apache-2.0)",
        "wired": True,
        "no_clone": "assay-research",
        "repo": "OmShiv/assay-research",
        "snippet": (
            "Every claim an agent makes (tests pass, no secrets, behavior preserved) is bound to the "
            "Merkle hash of the dependency cone of the code it covers, so the claim is stale exactly "
            "when that code or anything it depends on changes."
        ),
    },
    {
        "arxiv": "2609.38021",
        "concept": "deterministic-retrieval-chain-reader-swap",
        "k": 407,
        "narrative": (
            "**Auditable long-term memory.** Every stage below the final answer is deterministic code — "
            "hybrid candidate retrieval, cross-encoder reranking, packet compilation, mechanical "
            "reasoning scaffolds. The LLM appears **once, as a replaceable reader**. Because the lower "
            "stages are frozen, the same packets can be handed to any reader and the artifacts "
            "released for inspection. Scores 479/475 of 500 on LongMemEval-S, **bracketing** the "
            "published 478 — overlapping CIs, so neither superiority nor equivalence is established. "
            "**CCC-critical: the headline Opus reader route is the Claude Code CLI with the built-in "
            "tools disabled.** **Methodology claim:** the official judge flips 3 verdicts when "
            "re-scoring *byte-identical* answers, so **the reportable quantity is the noise band, not "
            "the rank**. A pre-committed negative control rejected a verifier that repaired 3 wrong "
            "drafts but broke 11 correct ones. Retrieval/rerank/scaffold sources are **held** — the "
            "chain is not independently reproducible. Evidence repo `cjchanh/longmemeval-evidence` is "
            "**MIT**. Pairs K392 cross-vendor behavior assays / K162 external eval / "
            "`verifiable-deterministic-agent-benchmarking` / `anytime-valid-agent-eval-stopping`. "
            "Runtime **`wont_wire`**; concept **`policy_wired`** eval-methodology."
        ),
        "pdf": "arxiv-2609.38021-auditable-long-term-memory-a-deterministic-retri.pdf",
        "slug": "arxiv-auditable-long-term-memory-deterministic-chain-2609.38021",
        "title": "Auditable Long-Term Memory: A Deterministic Retrieval Chain Measured at 479/475 of 500 on LongMemEval-S",
        "verdict": "REFERENCE + eval-methodology",
        "wired": True,
        "no_clone": "longmemeval-evidence",
        "repo": "cjchanh/longmemeval-evidence",
        "snippet": (
            "The headline Opus reader's route: the Claude Code command line, with the built-in tools "
            "disabled."
        ),
    },
    {
        "arxiv": "2609.38078",
        "concept": "vlm-mid-level-action-harness",
        "k": 408,
        "narrative": (
            "**MotorMind — VLM as robot controller.** A general-purpose VLM is equipped with a compact "
            "**mid-level action representation** (parameterized translations, rotations, gripper ops) "
            "plus a **deterministic embodiment-specific control layer** that converts proposals into "
            "physical motion. **Asynchronous monitoring** checks updated observations during execution "
            "and can cancel pending commands **at the next action boundary** — monitoring never blocks "
            "execution. Memory summaries are written in the background for later planning. 66.7% on "
            "LIBERO-PRO base and 53.8% under perturbation vs 13.3%/19.2% for the strongest prior "
            "zero-shot method; 95% average on a real xArm6. Swapping the backbone (Qwen3.8-Flash-Next → "
            "GPT-6 Sol) lifts base from 66.7% to 83.3%, showing **harness and backbone decouple**. "
            "**Cross-domain:** robotics is outside the CCC scope, so this is REFERENCE. No public repo "
            "surfaced. CCC value is the *pattern instance*: async monitor + non-blocking verification + "
            "boundary-only cancellation. Pairs K404 harness learning / `test-time-world-model-validate-"
            "before-act` / `world-acting-systems-taxonomy` / `system-scaling-harness-agentic-ai`. "
            "Runtime **`wont_wire`**; concept **`policy_wired`** awareness only."
        ),
        "pdf": "arxiv-2609.38078-motormind-scaffolding-general-vision-language-mo.pdf",
        "slug": "arxiv-motormind-vlm-mid-level-action-harness-2609.38078",
        "title": "MotorMind: Scaffolding General Vision Language Models for Zero-Shot Robot Manipulation",
        "verdict": "REFERENCE (cross-domain)",
        "wired": True,
        "no_clone": "motormind",
        "repo": "",
        "snippet": (
            "Can a general-purpose VLM itself operate a robot more like the human teleoperator by "
            "reasoning directly from observations, issuing actions, and continuously adapting to "
            "execution feedback, without relying on external models such as learned action experts, "
            "coding agents or grounding tools like SAM3?"
        ),
    },
    {
        "arxiv": "2609.38143",
        "concept": "meta-skill-bank-harness-construction",
        "k": 409,
        "narrative": (
            "**Learning meta-skills for harness design.** A **Builder** constructs execution "
            "environments for a **Target**; both sets of model weights stay **frozen**. A **meta-skill** "
            "is a three-field principle: **`when`** (observable trigger), **`provide`** (capability or "
            "resource to supply), **`use`** (how the Target should employ it, and which judgments stay "
            "its own). The Builder learns these from Target execution feedback on a development set, "
            "then **freezes the bank** and uses it to build harnesses for unseen tasks. Full-bank "
            "meta-skills beat no-skill construction by **8.95 points** and beat **delivering the same "
            "bank directly to the Target** by 12.02 points — **teaching the Builder beats teaching the "
            "Target**. When one model plays both roles, scores rise 18.71 points. **Phase-0: "
            "`qiancheng-apodex/MetaSkill-AI4AI` returns null SPDX** (no license file) → **NO-GO on "
            "clone**, watch only. Pairs K404 harness learning / `harness-as-eval-artifact` / "
            "`thin-harness-fat-skills-garrytan` / `skill-set-selection-under-budget` / "
            "`progressive-skill-discovery-access-control`. Runtime **`wont_wire`**; concept "
            "**`policy_wired`**."
        ),
        "pdf": "arxiv-2609.38143-learning-meta-skills-for-agent-harness-design-in.pdf",
        "slug": "arxiv-meta-skills-agent-harness-design-2609.38143",
        "title": "Learning Meta-Skills for Agent Harness Design in Test-Time AI4AI",
        "verdict": "ADOPT pattern; NO-GO clone (null SPDX)",
        "wired": True,
        "no_clone": "MetaSkill-AI4AI",
        "repo": "qiancheng-apodex/MetaSkill-AI4AI",
        "snippet": (
            "Teaching the Builder to translate experience into executable support can therefore be more "
            "beneficial than directly teaching the Target additional task skills."
        ),
    },
    {
        "arxiv": "2609.38147",
        "concept": "agentic-meta-reasoning-control-plane",
        "k": 410,
        "narrative": (
            "**Agentic meta-reasoning — control as its own agentic task.** Existing agents entangle "
            "control with object-level work: each control decision is a single step over an "
            "ever-growing history, so useful work is hard to compose and stops early as budgets grow. "
            "This harness **separates the controller from the workers**. Each control cycle runs four "
            "full agentic stages: **assess** (recompute compact state) → **propose** (enumerate "
            "candidate computations) → **evaluate** (choose under the remaining budget, or stop) → "
            "**dispatch** (spawn workers with selected context). **The controller carries a compact "
            "account of the run, not a replay of its history** — full worker outputs live in persistent "
            "memory as an action surface. Runs are recorded as an **artifact graph** (nodes = outputs, "
            "edges = context supply), which diagnoses a run by the work it produced. Controller calls "
            "are charged against the same budget as workers. Gains 3.6–4.2 points over a Direct Control "
            "Agent across 12 matched comparisons; ProgramBench 71.5% (GPT-5.5) vs 58.0% for Codex; keeps "
            "scaling where direct control plateaus, **though overhead hurts at small budgets**. "
            "**CCC-critical: it evaluates headless Claude Code (`claude -p`) with built-in tools off and "
            "a single MCP `container_bash` tool as the only channel.** Pairs `subagent-orchestration` / "
            "`token-economics-and-prompt-caching` (bounded controller context) / K387 KV working-set / "
            "K405 TokenCast / K318 budget routing. Runtime **`wont_wire`**; concept **`policy_wired`**."
        ),
        "pdf": "arxiv-2609.38147-thinking-before-thinking-scaling-agentic-inferen.pdf",
        "slug": "arxiv-agentic-meta-reasoning-control-plane-2609.38147",
        "title": "Thinking Before Thinking: Scaling Agentic Inference Through Meta-Reasoning",
        "verdict": "ADOPT pattern",
        "wired": True,
        "no_clone": "agentic-meta-reasoning",
        "repo": "",
        "snippet": (
            "Between decisions the controller carries only a compact account of the run rather than "
            "replaying its full history."
        ),
    },
]

# Cross-cutting concept spanning K407 + K410 (both use headless Claude Code as a controlled lane).
CROSS_CONCEPT = {
    "slug": "headless-claude-code-controlled-eval-lane",
    "title": "Headless Claude Code as a controlled evaluation lane",
    "tags": "[concept, evaluation, claude-code, harness, k407, k410]",
    "keywords": "[claude -p, headless, built-in tools disabled, MCP-only lane, eval lane, reader swap, budget injection]",
    "sources": [
        "sources/arxiv-auditable-long-term-memory-deterministic-chain-2609.38021.md",
        "sources/arxiv-agentic-meta-reasoning-control-plane-2609.38147.md",
    ],
    "narrative": """**Two independent September-2026 papers use headless Claude Code as a controlled
evaluation lane.** This is the point of this page: a research practice, observed twice, that CCC
should know about when designing its own evals or interpreting others'.

**The pattern (4 parts `[CONFIRMED]` — 2 independent sources):**

1. **Run Claude Code headless** — `claude -p` / non-interactive CLI, not the IDE or interactive session.
2. **Disable the built-in tools.** K407 calls this the "CLI lane": "the Claude Code command line,
   with the built-in tools disabled." K410 disables native tools so that every action flows through
   one channel.
3. **Expose exactly one capability.** K410 allows a **single MCP tool** (`container_bash`) so both
   the coding agent and the research harness see identical truncation, memory limits, and recovery
   behavior. File edits then happen through heredocs and shell commands — exactly as for the other
   arms.
4. **Inject an explicit model-call budget.** K410 prefixes a budget line to the next tool result
   each time another tenth of the allowance is consumed, and at 90% forces submission.

**Why it matters for CCC.** A headless, tools-disabled Claude Code is a **fixed, comparable
substrate**. It makes the harness the only variable. That is the same discipline CCC applies when it
treats a harness as an eval artifact (`@concepts/harness-as-eval-artifact.md`) and when it insists
that external eval contracts never be rewritten by the thing under test.

**Caveat from K407 — the lane is not the whole answer.** The lane fixes the reader, but the *judge*
still moved: the official GPT-4o judge flipped 3 verdicts when re-scoring byte-identical answers.
Fixing the execution lane does not fix the scoring lane. Pair this page with
`@concepts/verifiable-deterministic-agent-benchmarking.md`.

**Status:** policy/awareness only. No hook, tool, or runtime wire derives from this page.""",
    "snippet": (
        "Claude Code runs with its built-in tools off and only the MCP tool allowed; Codex runs with "
        "--sandbox read-only, so its own shell cannot write anything scored, with the MCP tool "
        "approved per-call."
    ),
}

CONCEPT_BRIEF_NOTE = (
    "K407 and K410 both run headless Claude Code with the built-in tools disabled as a controlled "
    "comparison lane (K410 via a single MCP tool, with budget injection)."
)


def yaml_list(items: list[str]) -> str:
    return "\n".join(f"  - {x}" for x in items)


def write_source(e: dict) -> None:
    k = e["k"]
    related = [f"concepts/{e['concept']}.md", f"briefs/{BRIEF}"]
    relations = [f"@concepts/{e['concept']}.md", f"@briefs/{BRIEF}"]
    snip = e.get("snippet", e["title"])
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

> "{snip}" [Source: arXiv {e['arxiv']} (retrieved {DATE})]

| **Location** | `{EGRESS}/{e['pdf']}` |
"""
    (REPO / "wiki/sources" / f"{e['slug']}.md").write_text(body, encoding="utf-8")


def write_concept(e: dict) -> None:
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


def write_cross_concept() -> None:
    cc = CROSS_CONCEPT
    related = list(cc["sources"]) + [
        "concepts/harness-as-eval-artifact.md",
        "concepts/verifiable-deterministic-agent-benchmarking.md",
        "concepts/phase1-adopt-wire.md",
        f"briefs/{BRIEF}",
    ]
    body = f"""---
title: "{cc['title']} (CCC K407/K410)"
type: concept
tags: {cc['tags']}
keywords: {cc['keywords']}
related:
{yaml_list(related)}
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: {DATE}
updated: {DATE}
---

## Relations

{chr(10).join(f'- `@{x}`' for x in related)}

## Raw Concept

{CONCEPT_BRIEF_NOTE}

## Narrative

{cc['narrative']}

## Snippets

> "{cc['snippet']}" [Source: arXiv 2609.38147 implementation details (retrieved {DATE})]
"""
    (REPO / "wiki/concepts" / f"{cc['slug']}.md").write_text(body, encoding="utf-8")


def write_phase0(e: dict) -> None:
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


def write_ccc_rule() -> None:
    rows = "\n".join(
        f"| K{e['k']} | {e['verdict']} | {e['concept'].replace('-', ' ')[:44]} | `policy_wired` |"
        for e in ENTRIES
    )
    bullets = "\n".join(
        f"- **K{e['k']}** {e['title'][:58]}… — **{e['verdict']}**: concept `{e['concept']}`."
        for e in ENTRIES
    )
    text = f"""---
description: CCC Phase-1 wires from K406–K410 harness wave (CCC-only — do NOT federation-sync)
alwaysApply: true
---

# CCC — K406–K410 Phase-1 wires

**Brief:** `docs/briefs/2026-09-30_k406-k410-harness-wave.md` · SIP: `wiki/briefs/{BRIEF}`

**IDs:** Resolve by arXiv id / slug / file path — K# is a log batch label only.

{bullets}

**Cross-cutting:** `headless-claude-code-controlled-eval-lane` — K407 + K410 both run headless
Claude Code with the built-in tools disabled as a controlled comparison lane.

**Wires landed:**

| K | Verdict | Wire | wire_status |
|---|---|------|-------------|
{rows}

**Non-goals:** no federation sync; no PoCs; no skill auto-evolution; no clone of any repo this wave.

**Propose-only:** Assay HITL clone (Apache-2.0, MCP server transport/auth audit first);
MetaSkill-AI4AI SPDX watch (null license).
"""
    (REPO / ".cursor/rules" / RULE).write_text(text, encoding="utf-8")


def append_policy() -> None:
    path = REPO / ".cursor/rules/cemini-phase1-policy-wires.mdc"
    text = path.read_text(encoding="utf-8")
    if f"CCC wave {WAVE}" in text:
        return
    block = f"""

## CCC wave {WAVE} (shared policy file)

Assay content-addressed evidence graphs (K406) + deterministic retrieval chain / reader swap (K407)
+ VLM mid-level action harness (K408) + meta-skill bank harness construction (K409) + agentic
meta-reasoning control plane (K410). **Zero clones.** CCC-only rule `{RULE}` — do **not**
federation-sync.

## Assay content-addressed evidence graphs (CCC K406)

- **Claims bound to the Merkle hash of the dependency cone**; staleness = hash comparison; blast
  radius == staleness frontier. Merge gate consults **no model** — 8 mechanical checks including
  **evidence monotonicity** (never delete the failing test) (pairs K403/K394/K402). Apache-2.0, MCP
  server. Runtime **`wont_wire`** pending transport/auth audit.

## Deterministic retrieval chain + reader swap (CCC K407)

- **All stages below the reader are deterministic code**; the LLM is a replaceable reader. Ingest
  the **eval-methodology** lesson: the judge flipped 3 verdicts on byte-identical answers, so report
  the **noise band, not the rank** (pairs K392/K162). Runtime **`wont_wire`**.

## VLM mid-level action harness (CCC K408)

- **Async monitor + non-blocking verification + boundary-only cancellation**; harness and backbone
  decouple (pairs K404). Cross-domain REFERENCE — robotics is outside CCC scope. Runtime
  **`wont_wire`**.

## Meta-skill bank harness construction (CCC K409)

- **Meta-skill = (`when`, `provide`, `use`)**; Builder learns principles from Target execution, bank
  frozen. **Teaching the Builder beats teaching the Target.** Repo returns **null SPDX** → **NO-GO
  clone**, watch only. Runtime **`wont_wire`**.

## Agentic meta-reasoning control plane (CCC K410)

- **Separate the controller from the workers**; 4-stage control cycle (assess/propose/evaluate/
  dispatch); **compact controller state, not history replay**; artifact graph for diagnosis.
  Overhead hurts at small budgets (pairs `subagent-orchestration`/K387/K405/K318). Runtime
  **`wont_wire`**.

## Headless Claude Code controlled eval lane (CCC K407/K410)

- **`claude -p` + built-in tools disabled + one MCP tool + injected model-call budget** = a fixed,
  comparable substrate. Two independent sources. Policy/awareness only.
"""
    path.write_text(text.rstrip() + block + "\n", encoding="utf-8")


def write_briefs() -> None:
    docs = REPO / "docs/briefs/2026-09-30_k406-k410-harness-wave.md"
    docs.write_text(
        f"""# {WAVE} harness wave — brief (CCC docs)

Date: {DATE} · SIP: `wiki/briefs/{BRIEF}`

## What changed

Five arXiv ingests from the Sep 30 daily sweep, plus one cross-cutting concept.
**Zero clones.**

1. **K406** Assay — content-addressed evidence graphs (CONDITIONAL-GO, Apache-2.0)
2. **K407** Auditable long-term memory — deterministic retrieval chain (REFERENCE + eval-methodology)
3. **K408** MotorMind — VLM mid-level action harness (REFERENCE, cross-domain)
4. **K409** Meta-skills for agent harness design (ADOPT pattern; NO-GO clone, null SPDX)
5. **K410** Agentic meta-reasoning control plane (ADOPT pattern)
6. **K407/K410 cross-cut** — headless Claude Code controlled eval lane

## Phase-0 / Phase-1

- `adopt_k406`…`k410` — all exit 0
- `{RULE}` + policy §{WAVE}
- Phase-0 license results: assay-research **Apache-2.0** · longmemeval-evidence **MIT** ·
  MetaSkill-AI4AI **null SPDX (NO-GO clone)**

## Propose-only

- Assay HITL clone — Apache-2.0, but the MCP server needs a transport/auth audit first
- MetaSkill-AI4AI SPDX watch — no license file
- Cybersec steal brief for K406 (Assay evidence monotonicity) — operator
""",
        encoding="utf-8",
    )
    sip = REPO / "wiki/briefs" / BRIEF
    sip.write_text(
        f"""---
title: CCC SIP-ready — {WAVE} full ingest
type: brief
tags: [brief, handoff, k406, k407, k408, k409, k410]
keywords: [assay, evidence-graph, retrieval-chain, motormind, meta-skills, meta-reasoning, headless-eval-lane]
related:
  - concepts/phase1-adopt-wire.md
  - concepts/headless-claude-code-controlled-eval-lane.md
maturity: draft
created: {DATE}
updated: {DATE}
---

## Target

Full ingest of **5 NEW** inbox PDFs as **CCC {WAVE}**, Phase-0 + Phase-1, archive, lint, commit,
push, CI green.

## Inbox

| K | arXiv | Verdict |
|---|-------|---------|
| K406 | 2609.36170 | CONDITIONAL-GO — Assay content-addressed evidence graphs |
| K407 | 2609.38021 | REFERENCE + eval-methodology — deterministic retrieval chain |
| K408 | 2609.38078 | REFERENCE (cross-domain) — MotorMind VLM action harness |
| K409 | 2609.38143 | ADOPT pattern; NO-GO clone (null SPDX) — meta-skills |
| K410 | 2609.38147 | ADOPT pattern — agentic meta-reasoning control plane |

## Cross-cutting

`headless-claude-code-controlled-eval-lane` — K407 and K410 independently run headless Claude Code
with the built-in tools disabled as a controlled evaluation lane. Two independent sources →
`[CONFIRMED]`.
""",
        encoding="utf-8",
    )


def patch_index() -> None:
    idx = REPO / "wiki/index.md"
    text = idx.read_text(encoding="utf-8")
    if ENTRIES[0]["slug"] in text:
        return

    anchor_c = "| [`htn-planning-mcp-multi-server-coordination`](concepts/htn-planning-mcp-multi-server-coordination.md)"
    concept_rows = [
        f"| [`{e['concept']}`](concepts/{e['concept']}.md) | draft | {e['title'][:50]}… — {e['arxiv']} (K{e['k']}) |"
        for e in ENTRIES
    ]
    cross_row = (
        f"| [`{CROSS_CONCEPT['slug']}`](concepts/{CROSS_CONCEPT['slug']}.md) | draft | "
        f"{CROSS_CONCEPT['title']} — K407/K410 |"
    )
    for row in concept_rows + [cross_row]:
        text = text.replace(anchor_c, row + "\n" + anchor_c, 1)

    anchor_s = "| [`arxiv-htn-planning-mcp-multi-server-coordination-2609.33731`]"
    for e in ENTRIES:
        row = (
            f"| [`{e['slug']}`](sources/{e['slug']}.md) | draft | "
            f"{e['title'][:55]}… — {e['arxiv']} |"
        )
        text = text.replace(anchor_s, row + "\n" + anchor_s, 1)

    # Sweep rows: append after the newest existing sweep row.
    sweep_anchor = "| [`2026-09-25-daily`](sweeps/2026-09-25-daily.md) | Daily digest — 5 papers (K390–K394 wave) |"
    sweep_rows = (
        "\n| [`2026-09-29-daily`](sweeps/2026-09-29-daily.md) | Daily digest — 5 papers (K401–K405 wave) |"
        "\n| [`2026-09-30-daily`](sweeps/2026-09-30-daily.md) | Daily digest — 5 papers (K406–K410 wave) |"
    )
    if sweep_anchor in text:
        text = text.replace(sweep_anchor, sweep_anchor + sweep_rows, 1)

    idx.write_text(text, encoding="utf-8")


def prepend_log() -> None:
    log = REPO / "wiki/log.md"
    entry = f"""## [{DATE}] ingest | {WAVE} harness wave (Sep 30 daily sweep)

- **Sources:** 2609.36170 Assay evidence graphs, 2609.38021 auditable LTM, 2609.38078 MotorMind, 2609.38143 meta-skills, 2609.38147 agentic meta-reasoning.
- **Cross-cutting concept:** `headless-claude-code-controlled-eval-lane` (K407 + K410 — two independent sources run headless Claude Code with built-in tools disabled as a controlled eval lane). `[CONFIRMED]`
- **Phase-0:** assay-research Apache-2.0; longmemeval-evidence MIT; MetaSkill-AI4AI **null SPDX → NO-GO clone**.
- **Phase-1:** adopt_k406…k410; `{RULE}`; policy §{WAVE}. Zero clones.
- **Fix:** repaired malformed 2609.35472 cross-route stub (duplicate sections, empty frontmatter) + backlink on `orchestration-reward-modeling-orch-rm`.
- **Archive:** egress bulk ccc (5 PDFs).

"""
    t = log.read_text(encoding="utf-8")
    if f"{WAVE} harness wave" not in t:
        log.write_text(entry + t, encoding="utf-8")


def patch_sweep() -> None:
    p = REPO / "wiki/sweeps/2026-09-30-daily.md"
    if not p.exists():
        return
    t = p.read_text(encoding="utf-8")
    if "INGESTED" in t:
        return
    t = f"> **INGESTED {DATE} as {WAVE}** — see `wiki/log.md`.\n\n" + t
    p.write_text(t, encoding="utf-8")


def patch_spdx_watch() -> None:
    """Fix the licenseInfo bug and register this wave's repos.

    `gh search repos --json licenseInfo` is rejected by the installed gh version; the
    `2>/dev/null || echo '[]'` guard swallowed the error, so every repo reported
    "no public GitHub repo found". Use `license` instead.
    """
    p = REPO / "scripts/spdx_watch_harness_wave.sh"
    t = p.read_text(encoding="utf-8")

    if "licenseInfo" in t:
        t = t.replace("licenseInfo", "license")
        t = t.replace("(r.get('license') or {}).get('spdxId')", "(r.get('license') or {}).get('spdxId')")

    new_repos = (
        '\nwatch_repo "Assay" "assay claims that decay with the code arxiv 2609.36170"\n'
        'watch_repo "MetaSkill-AI4AI" "learning meta-skills agent harness design arxiv 2609.38143"\n'
        'watch_repo "MotorMind" "motormind vision language robot manipulation arxiv 2609.38078"\n'
        'watch_repo "AuditableLTM" "auditable long-term memory deterministic retrieval chain arxiv 2609.38021"\n'
    )
    if "MetaSkill-AI4AI" not in t:
        t = t.replace("\nwatch_repo \"TokenCast\"", new_repos + "\nwatch_repo \"TokenCast\"")

    # Move any watch_repo call that landed after the "Done." banner back above it.
    lines = t.split("\n")
    done_idx = next(
        (i for i, ln in enumerate(lines) if ln.startswith('echo "Done.')), None
    )
    if done_idx is not None:
        after = lines[done_idx + 1:]
        moved = [ln for ln in after if ln.startswith("watch_repo ")]
        if moved:
            kept = [ln for ln in after if not ln.startswith("watch_repo ")]
            lines = lines[:done_idx] + moved + [lines[done_idx]] + kept
        t = "\n".join(lines)
    p.write_text(t.rstrip() + "\n", encoding="utf-8")


def main() -> None:
    for e in ENTRIES:
        write_source(e)
        write_concept(e)
        write_phase0(e)
    write_cross_concept()
    write_ccc_rule()
    append_policy()
    write_briefs()
    _repatch_sip_related()
    add_backlinks()
    patch_index()
    prepend_log()
    patch_sweep()
    patch_spdx_watch()
    print(f"done {WAVE}")


CROSS_SLUG = CROSS_CONCEPT["slug"]


def _add_related(path: Path, entry: str, note: str) -> None:
    """Add `entry` to a page's related: frontmatter and Relations body, once."""
    t = path.read_text(encoding="utf-8")
    if entry in t:
        return
    lines = t.split("\n")
    # frontmatter ends at the second '---'
    end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    rel = next(i for i in range(1, end) if lines[i].startswith("related:"))
    j = rel + 1
    while j < end and lines[j].startswith("  - "):
        j += 1
    lines.insert(j, f"  - {entry}")
    end += 1
    lines.insert(end, "")
    # Relations body block
    try:
        relhdr = next(i for i in range(end, len(lines)) if lines[i].strip() == "## Relations")
        k = relhdr + 1
        while k < len(lines) and not lines[k].startswith("## "):
            k += 1
        lines.insert(k - 1 if k - 1 > relhdr else relhdr + 1, f"- `@{entry}` — {note}")
    except StopIteration:
        pass
    t = "\n".join(lines)
    t = t.replace(f"updated: {DATE}", f"updated: {DATE}")  # keep wave date
    path.write_text(t, encoding="utf-8")


def add_backlinks() -> None:
    """Close bidirectional gaps opened by the new cross-cutting concept."""
    note = "headless Claude Code controlled eval lane (K407/K410)"
    for target in [
        "concepts/harness-as-eval-artifact.md",
        "concepts/verifiable-deterministic-agent-benchmarking.md",
    ]:
        _add_related(REPO / "wiki" / target, f"concepts/{CROSS_SLUG}.md", note)
    for e in ENTRIES:
        if e["k"] in (407, 410):
            _add_related(
                REPO / "wiki/sources" / f"{e['slug']}.md",
                f"concepts/{CROSS_SLUG}.md",
                note,
            )


def _repatch_sip_related() -> None:
    """SIP brief must list every page it is referenced from (bidirectional)."""
    p = REPO / "wiki/briefs" / BRIEF
    t = p.read_text(encoding="utf-8")
    entries = [f"concepts/{e['concept']}.md" for e in ENTRIES]
    entries += [f"sources/{e['slug']}.md" for e in ENTRIES]
    entries.append(f"concepts/{CROSS_SLUG}.md")
    missing = [x for x in entries if f"  - {x}" not in t]
    if not missing:
        return
    lines = t.split("\n")
    end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    rel = next(i for i in range(1, end) if lines[i].startswith("related:"))
    j = rel + 1
    while j < end and lines[j].startswith("  - "):
        j += 1
    for off, x in enumerate(missing):
        lines.insert(j + off, f"  - {x}")
    p.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
