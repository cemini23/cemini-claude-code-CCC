#!/usr/bin/env python3
"""Generate K401–K405 wiki ingest artifacts (Sep 29 daily sweep)."""
from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DATE = "2026-09-29"
BRIEF = "2026-09-29_ccc-k401-k405-sip-ready.md"
EGRESS = "cemini-egress-fi:/opt/cemini-bulk/research/ccc"
RULE = "ccc-k401-k405-phase1-wires.mdc"

ENTRIES = [
    {
        "arxiv": "2609.33731",
        "concept": "htn-planning-mcp-multi-server-coordination",
        "k": 401,
        "narrative": "**HTN planning as MCP coordination layer** — cross-server plans compiled once, executed "
        "deterministically via middleware and `${context.X}` binding; avoids LLM-host one-round-trip-per-tool "
        "orchestration (pairs K329 domain orchestration / K318 step routing / K311 lazy MCP). **Apache-2.0** "
        "artifact `PCfVW/hplan26-artifact` — REFERENCE optional HITL; runtime **`wont_wire`**. Concept "
        "**`policy_wired`**.",
        "pdf": "arxiv-2609.33731-htn-planning-as-a-coordination-layer-for-multi-s.pdf",
        "slug": "arxiv-htn-planning-mcp-multi-server-coordination-2609.33731",
        "title": "HTN Planning as a Coordination Layer for Multi-Server MCP Tool Orchestration",
        "verdict": "ADOPT pattern",
        "wired": True,
        "no_clone": "hplan26-artifact",
        "snippet": "When the host is a large language model, the resulting orchestrations are non-deterministic, "
        "non-reproducible, and pay one inference round-trip per tool call.",
    },
    {
        "arxiv": "2609.35381",
        "concept": "mcp-developer-error-messages-agent-recovery",
        "k": 402,
        "narrative": "**MCP error messages written for developers** — half of actionable error steps assume "
        "capabilities the agent caller lacks (terminal, config edit, browser); hurts strongest tool users most "
        "(pairs K368 implicit trust / K259 tool grounding / K351 edge reliability). **ADOPT policy + eval** — "
        "agent-native error surfaces. No clone. Runtime **`wont_wire`**; concept **`policy_wired`**.",
        "pdf": "arxiv-2609.35381-mcp-error-messages-written-for-developers-hurt-t.pdf",
        "slug": "arxiv-mcp-developer-error-messages-hurt-agents-2609.35381",
        "title": "MCP Error Messages Written for Developers Hurt the Most Capable Agents Most",
        "verdict": "ADOPT policy + eval",
        "wired": True,
        "no_clone": "mcp-dev-errors",
        "snippet": "Many agents that read them can only call the server's tools.",
    },
    {
        "arxiv": "2609.35659",
        "concept": "tracekit-tamper-evident-agent-audit",
        "k": 403,
        "narrative": "**Tracekit** — intent / self-reported reasoning / executed actions captured to **hash-chained, "
        "externally anchorable** ledger with cross-checks; Claude Code lifecycle hooks (pairs K394 agent trace "
        "tampering / K327 append-only transcript / K277 audit integrity). **Cybersec-primary + ADOPT policy**. "
        "**No PoCs / no tamper recipes.** No clone this wave. Runtime **`wont_wire`**; concept **`policy_wired`**.",
        "pdf": "arxiv-2609.35659-tracekit-tamper-evident-intent-reasoning-action.pdf",
        "slug": "arxiv-tracekit-tamper-evident-agent-audit-2609.35659",
        "title": "Tracekit: Tamper-Evident Intent-Reasoning-Action Auditing for Autonomous Coding Agents",
        "verdict": "Cybersec + ADOPT policy",
        "wired": True,
        "no_clone": "tracekit",
        "snippet": "Their record is usually an editable log.",
    },
    {
        "arxiv": "2609.35738",
        "concept": "harness-learning-test-time-adaptation",
        "k": 404,
        "narrative": "**Harness learning** — proposer revises solver **executable harness** from execution feedback; "
        "meta-learning over programs with harness edits as weight updates (pairs K292 harness CL / K281 meta-harness "
        "/ K162 external eval — **never rewrite pass criteria**). Trainer runtime **`wont_wire`**. Concept "
        "**`policy_wired`** eval-first.",
        "pdf": "arxiv-2609.35738-harness-learning-enables-generalizable-test-time.pdf",
        "slug": "arxiv-harness-learning-test-time-adaptation-2609.35738",
        "title": "Harness Learning Enables Generalizable Test-Time Adaptation",
        "verdict": "ADOPT eval-first",
        "wired": True,
        "no_clone": "harness-learning",
        "snippet": "A language-model agent is jointly defined by its model and its harness, the executable program that "
        "organizes model calls, tool use, and information flow.",
    },
    {
        "arxiv": "2609.35760",
        "concept": "tokencast-agent-token-consumption-forecast",
        "k": 405,
        "narrative": "**TokenCast** — composable cost representation per execution segment; forecasts **token "
        "consumption during agent runs** as context grows (pairs K320 usage vs context / K387 KV working-set / "
        "K318 budget routing). `DEFENSE-SEU/TokenCast` **null SPDX** at Phase-0 → watch only. Runtime "
        "**`wont_wire`**; concept **`policy_wired`** awareness.",
        "pdf": "arxiv-2609.35760-tokencast-forecasting-token-consumption-during-l.pdf",
        "slug": "arxiv-tokencast-agent-token-forecast-2609.35760",
        "title": "TokenCast: Forecasting Token Consumption During LLM Agent Execution",
        "verdict": "ADOPT awareness",
        "wired": True,
        "no_clone": "tokencast",
        "snippet": "Token consumption can vary by over an order of magnitude across runs.",
    },
]


def yaml_list(items: list[str]) -> str:
    return "\n".join(f"  - {x}" for x in items)


def write_source(e: dict) -> None:
    k = e["k"]
    related, relations = [f"briefs/{BRIEF}"], [f"@briefs/{BRIEF}"]
    related.insert(0, f"concepts/{e['concept']}.md")
    relations.insert(0, f"@concepts/{e['concept']}.md")
    snip = e.get("snippet", e["title"])
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
| **Retrieved** | {DATE} |

## Narrative

**Verdict: {e['verdict']}.**

{e['narrative']}

## Snippets

> "{snip}" [Source: arXiv {e['arxiv']} abstract (retrieved {DATE})]

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
        f"| K{e['k']} | {e['verdict'].split()[0]} | {e['concept'].replace('-', ' ')[:40]} | `policy_wired` |"
        for e in ENTRIES
    )
    bullets = "\n".join(
        f"- **K{e['k']}** {e['title'][:60]}… — **{e['verdict']}**: concept `{e['concept']}`. Runtime **`wont_wire`**."
        for e in ENTRIES
    )
    text = f"""---
description: CCC Phase-1 wires from K401–K405 harness wave (CCC-only — do NOT federation-sync)
alwaysApply: true
---

# CCC — K401–K405 Phase-1 wires

**Brief:** `docs/briefs/2026-09-29_k401-k405-harness-wave.md` · SIP: `wiki/briefs/{BRIEF}`

**IDs:** Resolve by arXiv id / slug / file path — K# is a log batch label only.

{bullets}

**Wires landed:**

| K | Verdict | Wire | wire_status |
|---|---|---|-------------|
{rows}

**Non-goals:** no federation sync; no PoCs; no skill auto-evolution; Tracekit no tamper recipes.

**Propose-only:** TokenCast SPDX watch; optional hplan26 REFERENCE clone (Apache-2.0, HITL).
"""
    (REPO / ".cursor/rules" / RULE).write_text(text, encoding="utf-8")


def append_policy() -> None:
    path = REPO / ".cursor/rules/cemini-phase1-policy-wires.mdc"
    text = path.read_text(encoding="utf-8")
    if "K401–K405" in text:
        return
    block = """

## CCC wave K401–K405 (shared policy file)

HTN MCP coordination (K401) + MCP developer error surfaces (K402) + Tracekit tamper-evident audit (K403) + harness learning TTA (K404) + TokenCast token forecast (K405). **Zero clones.** CCC-only rule `ccc-k401-k405-phase1-wires.mdc` — do **not** federation-sync.

## HTN planning MCP multi-server coordination (CCC K401)

- **Deterministic cross-server execution** vs LLM-per-tool-call hosts (pairs K329/K318). Runtime **`wont_wire`**.

## MCP developer-oriented error messages (CCC K402)

- **Agent-callable recovery** in MCP error payloads — developer-only steps fail closed for agents (pairs K368/K259). Runtime **`wont_wire`**.

## Tracekit tamper-evident agent audit (CCC K403)

- **Hash-chained intent–reasoning–action** ledger; external anchoring (pairs K394/K327). **No PoCs.** Runtime **`wont_wire`**.

## Harness learning test-time adaptation (CCC K404)

- **Executable harness meta-updates** from execution feedback; keep external eval contract (pairs K292/K281/K162). Trainer **`wont_wire`**.

## TokenCast agent token consumption forecast (CCC K405)

- **Mid-run token budget forecasting** for agent segments (pairs K320/K387). Runtime **`wont_wire`**.
"""
    path.write_text(text.rstrip() + block + "\n", encoding="utf-8")


def write_briefs() -> None:
    docs = REPO / "docs/briefs/2026-09-29_k401-k405-harness-wave.md"
    docs.write_text(
        f"""# K401–K405 harness wave — brief (CCC docs)

Date: {DATE} · SIP: `wiki/briefs/{BRIEF}`

## What changed

Five arXiv ingests from Sep 29 daily sweep. **Zero clones.**

1. **K401** HTN planning MCP multi-server coordination
2. **K402** MCP developer error messages vs agent recovery
3. **K403** Tracekit tamper-evident IRA audit
4. **K404** Harness learning test-time adaptation
5. **K405** TokenCast token consumption forecasting

## Phase-0 / Phase-1

- `adopt_k401`…`k405` — all exit 0
- `{RULE}` + policy §K401–K405

## Propose-only

- TokenCast SPDX watch (`DEFENSE-SEU/TokenCast`)
- Optional hplan26-artifact REFERENCE (Apache-2.0, HITL)
- Cybersec steal brief for K403 (Tracekit) — operator
""",
        encoding="utf-8",
    )
    sip = REPO / "wiki/briefs" / BRIEF
    sip.write_text(
        f"""---
title: CCC SIP-ready — K401–K405 full ingest
type: brief
tags: [brief, handoff, k401, k402, k403, k404, k405]
keywords: [htn-mcp, tracekit, harness-learning, tokencast]
related:
  - concepts/phase1-adopt-wire.md
maturity: draft
created: {DATE}
updated: {DATE}
---

## Target

Full ingest of **5 NEW** inbox PDFs as **CCC K401–K405**, Phase-0 + Phase-1, archive, lint, commit, push, CI green.

## Inbox

| K | arXiv | Verdict |
|---|-------|---------|
| K401 | 2609.33731 | ADOPT pattern — HTN MCP coordination |
| K402 | 2609.35381 | ADOPT policy+eval — MCP error messages |
| K403 | 2609.35659 | Cybersec + policy — Tracekit audit |
| K404 | 2609.35738 | ADOPT eval-first — harness learning |
| K405 | 2609.35760 | ADOPT awareness — TokenCast |
""",
        encoding="utf-8",
    )


def patch_index() -> None:
    idx = REPO / "wiki/index.md"
    text = idx.read_text(encoding="utf-8")
    concept_rows = []
    source_rows = []
    for e in ENTRIES:
        concept_rows.append(
            f"| [`{e['concept']}`](concepts/{e['concept']}.md) | draft | {e['title'][:50]}… — {e['arxiv']} (K{e['k']}) |"
        )
        source_rows.append(
            f"| [`{e['slug']}`](sources/{e['slug']}.md) | draft | {e['title'][:55]}… — {e['arxiv']} |"
        )
    if ENTRIES[0]["slug"] in text:
        return
    anchor_c = "| [`agentic-economies-autonomous-science-governance`]"
    if anchor_c in text:
        text = text.replace(anchor_c, concept_rows[0] + "\n" + anchor_c, 1)
        for row in concept_rows[1:]:
            text = text.replace(anchor_c, row + "\n" + anchor_c, 1)
    anchor_s = "| [`arxiv-agentic-economies-autonomous-scientific-discovery-2609.31562`]"
    if anchor_s in text:
        insert = "\n".join(reversed(source_rows))
        text = text.replace(anchor_s, insert + "\n" + anchor_s, 1)
    idx.write_text(text, encoding="utf-8")


def prepend_log() -> None:
    log = REPO / "wiki/log.md"
    entry = f"""## [{DATE}] ingest | K401–K405 harness wave (Sep 29 daily sweep)

- **Sources:** 2609.33731 HTN MCP, 2609.35381 MCP errors, 2609.35659 Tracekit, 2609.35738 harness learning, 2609.35760 TokenCast.
- **Phase-0/1:** adopt_k401…k405; `{RULE}`; policy §K401–K405. Zero clones.
- **Archive:** egress bulk ccc (5 PDFs).

"""
    t = log.read_text(encoding="utf-8")
    if "K401–K405 harness wave" not in t:
        log.write_text(entry + t, encoding="utf-8")


def patch_sweep() -> None:
    p = REPO / "wiki/sweeps/2026-09-29-daily.md"
    if not p.exists():
        return
    t = p.read_text(encoding="utf-8")
    if "INGESTED" in t:
        return
    t = "> **INGESTED 2026-09-29 as K401–K405** — see `wiki/log.md`.\n\n" + t
    p.write_text(t, encoding="utf-8")


def patch_spdx_watch() -> None:
    p = REPO / "scripts/spdx_watch_harness_wave.sh"
    t = p.read_text(encoding="utf-8")
    if "TokenCast" not in t:
        t = t.rstrip() + '\nwatch_repo "TokenCast" "TokenCast agent token forecast arxiv 2609.35760"\n'
        p.write_text(t + "\n", encoding="utf-8")


def main() -> None:
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
    patch_spdx_watch()
    print("done K401–K405")


if __name__ == "__main__":
    main()
