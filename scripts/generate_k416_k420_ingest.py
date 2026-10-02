#!/usr/bin/env python3
"""Generate K416–K420 wiki ingest artifacts (2026-10-02 daily sweep)."""
from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DATE = "2026-10-02"
BRIEF = "2026-10-02_ccc-k416-k420-sip-ready.md"
EGRESS = "cemini-egress-fi:/opt/cemini-bulk/research/ccc"
RULE = "ccc-k416-k420-phase1-wires.mdc"
WAVE = "K416–K420"

ENTRIES = [
    {
        "arxiv": "2610.01097",
        "concept": "persistent-state-evidence-traceable-research",
        "k": 416,
        "narrative": (
            "**YouRA — research state as a durable object, not a byproduct of chat.** The paper's "
            "diagnosis: end-to-end research agents produce fluent papers whose claims diverge from "
            "the experiments actually run. It names three causes, and all three reduce to one absence "
            "— **the trajectory is never held as explicit, persistent, verifiable structure**: (1) "
            "context and evidence fragmentation, where state buried in conversation is vulnerable to "
            "truncation and hallucination; (2) **no structured failure memory**, so failures never "
            "become constraints on later work; (3) unreliable workflow control, because the same "
            "dialogue both does the work and decides when to stop, retry, or redesign. Three "
            "components answer it: a **Verification State Architecture (VSA)** holding hypotheses, "
            "gates, and evidence pointers; an **Independent Controller** that reads that state to "
            "drive lifecycle, recovery, and review while **separating control from execution**; and "
            "**Stateful Reflection** that logs failures as structured lessons and routes recovery "
            "through **bounded repair → redesign → reset**. Ablating any component lowers the score, "
            "and the two *core-state* removals (VSA, Controller) drop it below both baselines on two "
            "of three backbones. failure profiles differ by component: no-VSA produces numbers that "
            "disagree across sections and claims contradicting execution logs; no-Controller produces "
            "crashed runs reported as completed findings. **CCC relevance is direct** — this is K410's "
            "control/worker split plus K414's verified ledger plus K413's execution contract, applied "
            "to research rather than proofs, with the strongest claim being that "
            "**externalization is load-bearing, not stylistic**. Pairs K406 Assay (claim–evidence "
            "binding) / K409 meta-skills / `@concepts/specification-driven-scientific-workflow-"
            "management.md`. **Phase-0: `PrayPrey/Your-Research-Agent` NOASSERTION**, 1★, **~508 MB** "
            "— no license and a large tree → **no clone**. Runtime **`wont_wire`**; concept "
            "**`policy_wired`**."
        ),
        "pdf": "arxiv-2610.01097-youra-a-persistent-state-architecture-for-eviden.pdf",
        "slug": "arxiv-youra-persistent-state-evidence-traceable-2610.01097",
        "title": "YouRA: A Persistent-State Architecture for Evidence-Traceable Autonomous Research Agents",
        "verdict": "ADOPT pattern; NO-GO clone (no license)",
        "no_clone": "Your-Research-Agent",
        "repo": "PrayPrey/Your-Research-Agent",
        "snippet": (
            "the research trajectory is not maintained as explicit, persistent, verifiable structure "
            "across the pipeline."
        ),
    },
    {
        "arxiv": "2610.01364",
        "concept": "state-injection-over-history-reconstruction",
        "k": 417,
        "narrative": (
            "**Siemens — inject the state, do not make the agent reconstruct it.** A six-module "
            "simulated factory where **each module gets its own LLM agent and its own MCP tool server** "
            "wrapping that module's OPC UA skills; agents coordinate over **MQTT**. Three "
            "architectures are compared head-to-head across nine production challenges: "
            "**orchestrator** (central agent, global view), **peer-to-peer** (direct agent-to-agent), "
            "and **monolithic** (one agent, all modules). Monolithic and P2P tie at **93% mean solve "
            "rate**; the orchestrator scores 87% but **uniquely solves the silent conveyor-belt fault "
            "in all 10 runs** by rerouting around the blocked segment from its global view. The "
            "headline CCC finding is the **state-injection ablation**: prepending the current factory "
            "state as a structured context block raises solve rate **88% → 93%**, and without it the "
            "agent cannot distinguish a real hardware fault from state it inferred wrongly. Injection "
            "also lets the harness trim conversation history aggressively, because the state block is "
            "authoritative rather than reconstructed. Two more transferable mechanisms: **dynamic tool "
            "constraint** (a manager publishes only the *physically valid* tools before each call, so "
            "the model cannot attempt a rejected operation) and the finding that **92–98% of tokens "
            "are input** — the cost sits in state + history injection, not output. Fault diagnosis was "
            "**emergent**, with no explicit failure-handling logic written for it. Cross-domain "
            "(industrial), so REFERENCE — but the three primitives are pure harness design. Pairs "
            "K402 MCP error surfaces / K318 step routing / `@concepts/context-engineering.md` / K415 "
            "instance-adaptive harness. **No repo surfaced.** Runtime **`wont_wire`**; concept "
            "**`policy_wired`**."
        ),
        "pdf": "arxiv-2610.01364-llm-driven-multi-agent-control-for-skill-based-s.pdf",
        "slug": "arxiv-state-injection-multi-agent-manufacturing-2610.01364",
        "title": "LLM-Driven Multi-Agent Control for Skill-Based Smart Manufacturing",
        "verdict": "REFERENCE (cross-domain; 3 primitives transfer)",
        "no_clone": "siemens-factory-agents",
        "repo": "",
        "snippet": (
            "This relieves LLMs from having to reconstruct the state themselves from the conversation "
            "history, with the added benefit of enabling aggressive token-conserving context-history "
            "trimming."
        ),
    },
    {
        "arxiv": "2610.02181",
        "concept": "active-evidence-acquisition-multimodal",
        "k": 418,
        "narrative": (
            "**OmniSeek — make evidence acquisition part of the reasoning, not a preprocessing step.** "
            "Omni-LLMs normally ingest an entire audio-visual stream in one forward pass; as context "
            "grows, brief acoustic events and fine visual details are diluted and the model falls back "
            "on language priors. OmniSeek instead runs an explicit "
            "**`<think>` → `<tool_call>` → `<observe>` loop**, deciding *which* modality to inspect "
            "and *which* time window, then appending the retrieved raw segment back into context. The "
            "training contribution worth noting is the **Audio-Visual Necessity objective**: an RL "
            "reward that credits trajectories whose answer genuinely depends on **both** modalities, "
            "which **discourages single-modality shortcuts** without extra rollouts. The paper also "
            "documents a clean **failure mode under context overflow**: past the window, the agent "
            "**loses tool invocation entirely** and degenerates into a repetitive `<think>` loop, "
            "**hallucinating observations it never retrieved** rather than calling the tool. That is "
            "the same failure K410 warns about — control state collapsing under unbounded history. "
            "**CCC relevance is partial** — the domain is audio-visual, so this is REFERENCE, but two "
            "ideas transfer: **modality-decoupled retrieval as an explicit loop**, and an "
            "**anti-shortcut reward term**. Pairs K410 agentic meta-reasoning (bounded controller "
            "state) / `@concepts/context-engineering.md` / K418's own failure mode with K387 KV "
            "working-set. **No repo surfaced.** Runtime **`wont_wire`**; concept **`policy_wired`** "
            "awareness."
        ),
        "pdf": "arxiv-2610.02181-omniseek-native-tool-integration-for-multi-turn.pdf",
        "slug": "arxiv-omniseek-active-evidence-acquisition-2610.02181",
        "title": "OmniSeek: Native Tool Integration for Multi-turn Audio-Visual Reasoning",
        "verdict": "REFERENCE (multimodal; 2 ideas transfer)",
        "no_clone": "omniseek",
        "repo": "",
        "snippet": (
            "As the context overflows, the agent loses the ability to invoke tools. Instead, it falls "
            "into a repetitive <think> loop, hallucinating sensory evidence directly within its "
            "internal reasoning blocks."
        ),
    },
    {
        "arxiv": "2610.02200",
        "concept": "lossless-visual-memory-harness",
        "k": 419,
        "narrative": (
            "**VISTA — lossless memory plus a way to look again.** A visual harness giving a "
            "general-purpose multimodal model long-horizon vision. The design rests on a diagnosis: "
            "existing VLMs **encode each observation once** and then discard the raw input, so the "
            "representation may omit **details that only turn out to matter later** — and the model "
            "cannot know at encoding time which they are. VISTA answers with three components: "
            "**visual observation** (perceive the environment directly), a **lossless visual memory** "
            "that keeps every frame *including intermediate animation frames* in original form, "
            "indexed by turn and frame, and **visual inspection tools** that let the model "
            "**revisit any frame or magnify any region** as its reasoning evolves. The framing is "
            "sharp: this is an **explicit attention mechanism over the interaction history**, letting "
            "the model choose what to look at instead of hoping the initial encoding kept it. Results "
            "are strong — **Claude Opus 5.0 goes from RHAE 40.68 to a perfect 100.00** on ARC-AGI-3 "
            "with xhigh effort, completing all 25 public games using **57.4% fewer actions than "
            "first-time humans**; GPT-5.6 Sol reaches 99.00. The harness transfers with minimal "
            "adaptation to three further benchmarks. **CCC relevance:** the general lesson is that "
            "**lossless retention plus cheap retrieval beats clever compression**, and that the "
            "agent should control what it re-reads rather than the harness pre-deciding. That "
            "contrasts productively with the compression-heavy line (K411 CLI truncation, K387 KV "
            "working-set, `@concepts/truncate-only-long-horizon-compaction.md`). Pairs K410 "
            "(compact controller state) / `@concepts/context-engineering.md` / "
            "`@concepts/test-time-world-model-validate-before-act.md`. **Phase-0: "
            "`joshhhhhan/VISTA` MIT**, 126★, 4 forks, 2.8 MB, pushed 2026-09-05 — healthy and "
            "**clone-eligible**. Runtime **`wont_wire`**; concept **`policy_wired`**."
        ),
        "pdf": "arxiv-2610.02200-vista-a-visual-harness-for-reasoning-in-an-inter.pdf",
        "slug": "arxiv-vista-lossless-visual-memory-harness-2610.02200",
        "title": "VISTA: A Visual Harness for Reasoning in an Interactive World",
        "verdict": "ADOPT pattern (MIT)",
        "no_clone": "VISTA",
        "repo": "joshhhhhan/VISTA",
        "snippet": (
            "Instead of relying solely on visual representations retained in the model's context, "
            "which may be compressed, lossy, and insufficient for subsequent reasoning, VISTA "
            "maintains a lossless visual memory."
        ),
    },
    {
        "arxiv": "2610.02206",
        "concept": "schema-free-cli-tool-eval",
        "k": 420,
        "narrative": (
            "**KaliBench — tool use without schemas, graded down to the flag.** A benchmark for "
            "**natural-language → CLI** translation on Kali Linux: 8,504 query–command pairs across "
            "**1,642 tools**, 23 capability dimensions, 5 security phases. The framing is the "
            "contribution: existing tool-calling benchmarks assume **schema-defined tools** with JSON "
            "parameters, but real cybersecurity tooling is **schema-free CLI**, where enumerating "
            "hundreds of flag surfaces in a prompt is impractical — so the model must infer the tool "
            "*and* construct a syntactically valid command. Scoring is correspondingly fine-grained: "
            "**tool accuracy, optional-argument F1, positional-argument F1, exact-command match**, "
            "with **alias-aware** canonicalization so `-sT` and its long form compare equal. The "
            "finding is stark: **no evaluated open-weight model exceeds 42% exact-command accuracy** "
            "in the unrestricted setting, and **argument construction, not tool selection, is the "
            "bottleneck**. Adding tool hints lifts the ceiling sharply (up to ~84%), which locates "
            "the difficulty in recall of flag semantics rather than in choosing the tool. A second "
            "result for CCC: deterministic CLI structure enables **runtime-free verifiable rewards**, "
            "so SFT + RLVR lifts an 8B model to roughly 685B-MoE parity without executing commands. "
            "**CCC relevance:** the schema-free case is the honest description of most real tool "
            "surfaces — including MCP servers that wrap CLIs — and the measurement discipline "
            "(decompose tool vs. args, grade with alias awareness, reward without execution) is "
            "directly reusable. **Routing: cybersec-primary** — Kali tooling is the Cybersec wiki's "
            "domain; brief written there (`@cybersecurity-wiki/`), CCC keeps the tool-eval method. "
            "Pairs K402 MCP error surfaces / `@concepts/verifiable-deterministic-agent-"
            "benchmarking.md` / `@concepts/mcp-tool-interface-granularity-eval.md`. **Phase-0: "
            "`RISys-Lab/KaliBench` has no license file** (`SPDX=NONE`) → **no clone**. Runtime "
            "**`wont_wire`**; concept **`policy_wired`**."
        ),
        "pdf": "arxiv-2610.02206-kalibench-a-fine-grained-benchmark-for-cybersecu.pdf",
        "slug": "arxiv-kalibench-schema-free-cli-tool-eval-2610.02206",
        "title": "KaliBench: A Fine-Grained Benchmark for Cybersecurity Tool Use on Kali Linux with Runtime-Free Verifiable Rewards",
        "verdict": "ADOPT method; cybersec-primary; NO-GO clone (no license)",
        "no_clone": "KaliBench",
        "repo": "RISys-Lab/KaliBench",
        "snippet": (
            "CLIs are unforgiving: minor errors in argument order, flag spelling, alias misuse, or "
            "tool misinterpretation can invalidate execution."
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
description: CCC Phase-1 wires from K416–K420 harness wave (CCC-only — do NOT federation-sync)
alwaysApply: false
---

# CCC — K416–K420 Phase-1 wires

**Brief:** `docs/briefs/{DATE}_k416-k420-harness-wave.md` · SIP: `wiki/briefs/{BRIEF}`

**IDs:** Resolve by arXiv id / slug / file path — K# is a log batch label only.

{bullets}

**Wires landed:**

| K | Verdict | Wire | wire_status |
|---|---|------|-------------|
{rows}

**Non-goals:** no federation sync; no PoCs; no clone of any repo this wave. K420 is
cybersec-primary — brief written to `@cybersecurity-wiki/`.

**Propose-only:** VISTA HITL clone (MIT, 126★ — the one healthy repo this wave); YouRA and KaliBench
are NO-GO on clone (no license; YouRA is also ~508 MB).
"""
    (REPO / ".cursor/rules" / RULE).write_text(text, encoding="utf-8")


def append_policy():
    path = REPO / ".cursor/rules/cemini-phase1-policy-wires.mdc"
    text = path.read_text(encoding="utf-8")
    if f"CCC wave {WAVE}" in text:
        return
    block = f"""

## CCC wave {WAVE} (shared policy file)

YouRA persistent research state (K416) + state injection over history reconstruction (K417) +
OmniSeek active evidence acquisition (K418) + VISTA lossless visual memory (K419) + KaliBench
schema-free CLI tool eval (K420). **Zero clones.** CCC-only rule `{RULE}` — do **not**
federation-sync.

## Persistent state, evidence-traceable research (CCC K416)

- **Externalize the trajectory as durable state**: hypotheses, gates, and evidence pointers in a
  VSA; a controller that reads that state and **stays separate from execution**; failures logged as
  structured lessons routing to **bounded repair → redesign → reset**. Ablating either core-state
  component drops the system below baseline (pairs K410/K414/K413/K406). Runtime **`wont_wire`**.

## Inject state, do not reconstruct it (CCC K417)

- **Prepend authoritative state as a structured block** instead of making the model rebuild it from
  history: solve rate 88% → 93%, and it permits aggressive history trimming. Also: **filter the tool
  list to physically valid operations before each call**. 92–98% of tokens are input (pairs
  `context-engineering`/K318/K415). Runtime **`wont_wire`**.

## Active evidence acquisition, anti-shortcut reward (CCC K418)

- **Make retrieval an explicit `<think>→<tool_call>→<observe>` loop** over modality and time window,
  and **reward trajectories that need both modalities** to discourage single-source shortcuts. Under
  context overflow the agent loses tool calls entirely and **hallucinates observations** (pairs K410).
  Runtime **`wont_wire`**.

## Lossless memory beats clever compression (CCC K419)

- **Keep every observation in original form and let the agent decide what to re-inspect.** Encoding
  once loses details that only matter later, and the model cannot know at encoding time which they
  are. Lossless retention + cheap retrieval is an **explicit attention mechanism over history**
  (pairs K410/K387/`truncate-only-long-horizon-compaction`). Runtime **`wont_wire`**.

## Schema-free CLI tool eval (CCC K420, cybersec-primary)

- **Most real tool surfaces are schema-free CLI, not JSON schema.** Grade tool choice and argument
  construction **separately**, canonically and **alias-aware**. Argument construction is the
  bottleneck; no open-weight model exceeds **42% exact-command accuracy** unhinted. Deterministic CLI
  structure enables **runtime-free verifiable rewards**. Cybersec-primary; brief routed there
  (pairs K402/`mcp-tool-interface-granularity-eval`). Runtime **`wont_wire`**.
"""
    path.write_text(text.rstrip() + block + "\n", encoding="utf-8")


def write_briefs():
    docs = REPO / "docs/briefs/2026-10-02_k416-k420-harness-wave.md"
    docs.write_text(
        f"""# {WAVE} harness wave — brief (CCC docs)

Date: {DATE} · SIP: `wiki/briefs/{BRIEF}`

## What changed

Five arXiv ingests from the 2026-10-02 sweep. **Zero clones.**

1. **K416** YouRA — persistent state, evidence-traceable research (no licence → no clone)
2. **K417** Siemens factory agents — state injection beats history reconstruction
3. **K418** OmniSeek — active evidence acquisition + anti-shortcut reward
4. **K419** VISTA — lossless visual memory harness (MIT, 126★)
5. **K420** KaliBench — schema-free CLI tool eval (cybersec-primary; no licence → no clone)

## Phase-0 / Phase-1

- `adopt_k416`…`k420` — all exit 0
- `{RULE}` + policy §{WAVE}
- Phase-0: `joshhhhhan/VISTA` **MIT** (126★, healthy, clone-eligible) ·
  `PrayPrey/Your-Research-Agent` **NOASSERTION** + ~508 MB (no clone) ·
  `RISys-Lab/KaliBench` **no licence** (no clone)

## Cross-wiki

- **K420 KaliBench is cybersec-primary** — brief written to `@cybersecurity-wiki/`. CCC keeps the
  schema-free tool-eval *method*.

## Propose-only

- HITL clone of `joshhhhhan/VISTA` — the only healthy repo this wave
""",
        encoding="utf-8",
    )
    sip = REPO / "wiki/briefs" / BRIEF
    rel = [f"concepts/{e['concept']}.md" for e in ENTRIES] + [f"sources/{e['slug']}.md" for e in ENTRIES]
    sip.write_text(
        f"""---
title: CCC SIP-ready — {WAVE} full ingest
type: brief
tags: [brief, handoff, k416, k417, k418, k419, k420]
keywords: [persistent-state, state-injection, evidence-acquisition, lossless-memory, schema-free-cli]
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
| K416 | 2610.01097 | ADOPT pattern — YouRA persistent state |
| K417 | 2610.01364 | REFERENCE — state injection (cross-domain) |
| K418 | 2610.02181 | REFERENCE — OmniSeek (multimodal) |
| K419 | 2610.02200 | ADOPT pattern (MIT) — VISTA |
| K420 | 2610.02206 | ADOPT method; cybersec-primary — KaliBench |
""",
        encoding="utf-8",
    )


def patch_index():
    idx = REPO / "wiki/index.md"
    text = idx.read_text(encoding="utf-8")
    if ENTRIES[0]["slug"] in text:
        return
    anchor_c = "| [`persistent-state-evidence-traceable-research`]"
    if anchor_c not in text:
        for cand in ["| [`assay-content-addressed-evidence-graphs`]",
                     "| [`htn-planning-mcp-multi-server-coordination`]"]:
            if cand in text:
                anchor_c = cand; break
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
    if sa in text:
        text = text.replace(sa, sa +
            "\n| [`2026-10-02-daily`](sweeps/2026-10-02-daily.md) | Daily digest — 5 papers (K416–K420 wave) |", 1)
    idx.write_text(text, encoding="utf-8")


def prepend_log():
    log = REPO / "wiki/log.md"
    entry = f"""## [{DATE}] ingest | {WAVE} harness wave (Oct 2 daily sweep)

- **Sources:** 2610.01097 YouRA, 2610.01364 Siemens factory agents, 2610.02181 OmniSeek, 2610.02200 VISTA, 2610.02206 KaliBench.
- **Phase-0:** VISTA **MIT** (126★, healthy, clone-eligible); YouRA **NOASSERTION** + ~508 MB (no clone); KaliBench **no licence** (no clone).
- **Phase-1:** adopt_k416…k420; `{RULE}`; policy §{WAVE}. Zero clones.
- **Cross-wiki:** K420 KaliBench is **cybersec-primary** — brief routed to `@cybersecurity-wiki/`; CCC keeps the schema-free tool-eval method.
- **Standouts:** K417's state-injection ablation (88%→93%) and K419's lossless-memory argument against encode-once compression are the two most transferable harness findings.
- **Archive:** pending.

"""
    t = log.read_text(encoding="utf-8")
    if f"{WAVE} harness wave" not in t:
        log.write_text(entry + t, encoding="utf-8")


def patch_sweep():
    p = REPO / "wiki/sweeps/2026-10-02-daily.md"
    if not p.exists():
        return
    t = p.read_text(encoding="utf-8")
    if "INGESTED" in t:
        return
    p.write_text(f"> **INGESTED {DATE} as {WAVE}** — see `wiki/log.md`.\n\n" + t, encoding="utf-8")


def add_backlinks():
    """Close the bidirectional gaps the new pages open."""
    idx = f"concepts/phase1-adopt-wire.md"
    for rel, add in [
        ("wiki/concepts/context-engineering.md", ["concepts/state-injection-over-history-reconstruction.md",
                                                  "concepts/lossless-visual-memory-harness.md",
                                                  "concepts/active-evidence-acquisition-multimodal.md"]),
        ("wiki/concepts/subagent-orchestration.md", ["concepts/state-injection-over-history-reconstruction.md"]),
        ("wiki/concepts/agentic-meta-reasoning-control-plane.md", ["concepts/lossless-visual-memory-harness.md",
                                                                   "concepts/persistent-state-evidence-traceable-research.md"]),
        ("wiki/concepts/mcp-tool-interface-granularity-eval.md", ["concepts/schema-free-cli-tool-eval.md"]),
        ("wiki/concepts/verifiable-deterministic-agent-benchmarking.md", ["concepts/schema-free-cli-tool-eval.md"]),
        ("wiki/concepts/cogentic-verified-ledger-proof-orchestration.md", ["concepts/persistent-state-evidence-traceable-research.md"]),
    ]:
        p = Path(rel)
        if not p.exists():
            continue
        t = p.read_text(encoding="utf-8")
        lines = t.split("\n")
        end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
        if end is None:
            continue
        ri = next((i for i in range(1, end) if lines[i].startswith("related:")), None)
        if ri is None:
            continue
        j = ri + 1
        while j < end and lines[j].startswith("  - "):
            j += 1
        for off, a in enumerate(add):
            if f"  - {a}" not in "\n".join(lines[ri:end]):
                lines.insert(j + off, f"  - {a}")
        p.write_text("\n".join(lines), encoding="utf-8")


def main():
    for e in ENTRIES:
        write_source(e)
        write_concept(e)
        write_phase0(e)
    add_backlinks()
    write_ccc_rule()
    append_policy()
    write_briefs()
    patch_index()
    prepend_log()
    patch_sweep()
    print(f"done {WAVE}")


if __name__ == "__main__":
    main()
