#!/usr/bin/env python3
"""Generate K390–K394 wiki ingest artifacts."""
from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DATE = "2026-09-25"
BRIEF = "2026-09-25_ccc-k390-k394-sip-ready.md"
EGRESS = "cemini-egress-fi:/opt/cemini-bulk/research/ccc"
RULE = "ccc-k390-k394-phase1-wires.mdc"

ENTRIES = [
    {
        "arxiv": "2609.28693",
        "concept": "progressive-skill-discovery-access-control",
        "k": 390,
        "narrative": "**Progressive skill disclosure as structural access control** for tool-using agents — "
        "governance through staged skill/tool exposure, not flat catalog dumps (pairs K274 CDH / K237 skill "
        "memory / K311 lazy tool load). **Never auto-evolve `.cursor/skills`.** No clone unless SPDX at Phase-0. "
        "Runtime **`wont_wire`**; concept **`policy_wired`**.",
        "pdf": "arxiv-2609.28693-progressive-skill-discovery-as-access-control-fo.pdf",
        "slug": "arxiv-progressive-skill-discovery-access-control-2609.28693",
        "title": "Progressive Skill Discovery as Access Control for Tool-Using LLM Agents: Structural Governance through Staged Disclosure",
        "verdict": "ADOPT policy",
        "wired": True,
        "no_clone": "progressive-skill-discovery-access-control",
    },
    {
        "arxiv": "2609.28926",
        "concept": None,
        "k": 391,
        "narrative": "**OOD** materials/instruments — LLM agent fits XRR curves with X-Ray Calc 3 (pairs K342 "
        "hierarchical SPM automation stub). **Source only** — no CCC concept page. No clone. Runtime **`wont_wire`**.",
        "pdf": "arxiv-2609.28926-teaching-an-llm-agent-to-fit-xrr-curves-with-x-r.pdf",
        "slug": "arxiv-xrr-curves-x-ray-calc-agent-2609.28926",
        "title": "Teaching an LLM agent to fit XRR curves with X-Ray Calc 3",
        "verdict": "OOD materials stub",
        "wired": True,
        "no_clone": "x-ray-calc-xrr",
    },
    {
        "arxiv": "2609.30012",
        "concept": "low-cost-cross-vendor-behavior-assays",
        "k": 392,
        "narrative": "**Cheap cross-vendor/release behavior probes** — eval-first measurement when models and harnesses "
        "churn (pairs K277 measurement integrity / K373 enterprise eval / K263 versioned model–harness pairs). "
        "Runtime **`wont_wire`**; concept **`policy_wired`**.",
        "pdf": "arxiv-2609.30012-low-cost-assays-for-measuring-model-behavior-acr.pdf",
        "slug": "arxiv-low-cost-cross-vendor-behavior-assays-2609.30012",
        "title": "Low-Cost Assays for Measuring Model Behavior Across Vendors and Releases",
        "verdict": "ADOPT eval-first",
        "wired": True,
        "no_clone": "low-cost-cross-vendor-behavior-assays",
    },
    {
        "arxiv": "2609.30217",
        "concept": "instrumental-monitor-evasion-under-task-pressure",
        "k": 393,
        "narrative": "**Cybersec-primary + ADOPT eval:** instrumental monitor evasion emerges under **ordinary task "
        "incentives**, not exotic attacks (pairs K326 external enforcement / K239 execution fidelity). "
        "**No PoCs.** Runtime **`wont_wire`**; concept **`policy_wired`**.",
        "pdf": "arxiv-2609.30217-instrumental-monitor-evasion-emerges-under-ordin.pdf",
        "slug": "arxiv-instrumental-monitor-evasion-task-pressure-2609.30217",
        "title": "Instrumental Monitor Evasion Emerges Under Ordinary Task Pressure",
        "verdict": "Cybersec + ADOPT eval",
        "wired": True,
        "no_clone": "instrumental-monitor-evasion",
    },
    {
        "arxiv": "2609.30266",
        "concept": "agent-trace-tampering-audit-gap",
        "k": 394,
        "narrative": "**Cybersec-primary + ADOPT policy:** agent-writable traces break audit — require **external "
        "append-only / tamper-evident logging** (pairs K277/K239/K327 Logos transcript). **No PoCs / no tamper "
        "recipes.** Runtime **`wont_wire`**; concept **`policy_wired`**.",
        "pdf": "arxiv-2609.30266-llm-agents-can-easily-tamper-with-their-own-trac.pdf",
        "slug": "arxiv-agent-trace-tampering-2609.30266",
        "title": "LLM Agents Can Easily Tamper With Their Own Traces",
        "verdict": "Cybersec + ADOPT policy",
        "wired": True,
        "no_clone": "agent-trace-tampering",
    },
]


def yaml_list(items: list[str]) -> str:
    return "\n".join(f"  - {x}" for x in items)


def write_source(e: dict) -> None:
    k = e["k"]
    related, relations = [f"briefs/{BRIEF}"], [f"@briefs/{BRIEF}"]
    if e["concept"]:
        related.insert(0, f"concepts/{e['concept']}.md")
        relations.insert(0, f"@concepts/{e['concept']}.md")
    body = f"""---
title: "{e['title']} (CCC K{k})"
type: source
tags: [source, arxiv, k{k}]
keywords: [{e['arxiv']}, k{k}]
related:
{yaml_list(related)}
maturity: draft
read_status: read
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

> "{e['title']} — CCC K{k} synthesis." [Source: arXiv {e['arxiv']} — paraphrase]

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
    checks = [f'check "source" test -f "${{REPO_ROOT}}/wiki/sources/{e["slug"]}.md"']
    if e["concept"]:
        checks += [
            f'check "concept" test -f "${{REPO_ROOT}}/wiki/concepts/{e["concept"]}.md"',
            f'check "concept wired" grep -q "wire_status: policy_wired" "${{REPO_ROOT}}/wiki/concepts/{e["concept"]}.md"',
        ]
    if e["wired"]:
        checks += [
            f'check "policy K{k}" grep -q "K{k}" "${{REPO_ROOT}}/.cursor/rules/cemini-phase1-policy-wires.mdc"',
            f'check "ccc-rule K{k}" grep -q "K{k}" "${{REPO_ROOT}}/.cursor/rules/{RULE}"',
        ]
    adopt_slug = e.get("no_clone") or e["concept"] or e["slug"].split("-")[1]
    checks.append(f'check "no clone" test ! -d "${{REPO_ROOT}}/.local/adopts/{adopt_slug}"')
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


def main() -> None:
    for e in ENTRIES:
        write_source(e)
        if e["concept"]:
            write_concept(e)
        write_phase0(e)
    print("done K390–K394")


if __name__ == "__main__":
    main()
