#!/usr/bin/env python3
"""Generate K369–K372 wiki ingest artifacts."""
from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DATE = "2026-09-18"
BRIEF = "2026-09-18_ccc-k369-k372-sip-ready.md"
EGRESS = "cemini-egress-fi:/opt/cemini-bulk/research/ccc"

ENTRIES = [
    {
        "k": 369,
        "arxiv": "2609.19425",
        "slug": "arxiv-closed-world-resolution-tool-hallucination-2609.19425",
        "concept": "closed-world-tool-hallucination-resolution",
        "title": "Closed-World Resolution Against Tool Hallucination in LLM Agents",
        "pdf": "arxiv-2609.19425-closed-world-resolution-against-tool-hallucinati.pdf",
        "verdict": "ADOPT policy",
        "narrative": (
            "Tool-selection and tool-gating presuppose the emitted call refers to a **real tool** — "
            "**hallucinated tools/arguments** bypass both (not a gate decision at all). Closed-world resolution "
            "validates calls against an explicit tool registry/schema before execution. Pairs K259 tool affordances / "
            "K368 implicit trust / K274 CDH. Runtime **`wont_wire`** — schema validation belongs in broker/harness."
        ),
        "wired": True,
        "cybersec": False,
    },
    {
        "k": 370,
        "arxiv": "2609.20804",
        "slug": "arxiv-harness-design-coding-agents-empirical-2609.20804",
        "concept": "coding-agent-harness-component-design",
        "title": "An Empirical Study of Harness Design for Coding Agents",
        "pdf": "arxiv-2609.20804-an-empirical-study-of-harness-design-for-coding.pdf",
        "verdict": "ADOPT eval-first",
        "narrative": (
            "Coding harnesses are usually evaluated **monolithically** — component contributions unclear. "
            "Lightweight fixed execution loop with **three varied components**: planning, action space, context management. "
            "Four models × component ablations → component-level harness design evidence. CCC steal: decompose harness "
            "eval (pairs K334 harness-as-eval-artifact / K281 five-component audit / K350 supply-chain). "
            "No public SPDX at Phase-0 → no clone. Runtime **`wont_wire`**."
        ),
        "wired": True,
        "cybersec": False,
    },
    {
        "k": 371,
        "arxiv": "2609.20812",
        "slug": "arxiv-overclaiming-propensity-frontier-agents-2609.20812",
        "concept": "overclaiming-propensity-agent-measurement",
        "title": "Quantifying Overclaiming Propensity in Frontier LLM Agents",
        "pdf": "arxiv-2609.20812-quantifying-overclaiming-propensity-in-frontier.pdf",
        "verdict": "ADOPT eval + policy",
        "narrative": (
            "Frontier agents **overclaim** — assert success, capability, or completion beyond available evidence. "
            "Quantified **overclaiming propensity (OCP)** as a measurable agent trait for eval and routing. "
            "Pairs K277 measurement integrity / K122 claim drift / K325 bounded eval. Eval axis `policy_wired`; "
            "runtime **`wont_wire`**."
        ),
        "wired": True,
        "cybersec": False,
    },
    {
        "k": 372,
        "arxiv": "2609.20822",
        "slug": "arxiv-obstacle-aware-harness-robot-manipulation-2609.20822",
        "concept": None,
        "title": "Obstacle-Aware Harness for Safe Robot Manipulation (Coding Agents)",
        "pdf": "arxiv-2609.20822-coding-agents-with-an-obstacle-aware-harness-for.pdf",
        "verdict": "OOD stub",
        "narrative": (
            "Coding agents write robot controllers without robot-specific training; evaluated under **safety constraints** "
            "(manipulation goal + obstacle must not be touched). Standard agents collide with obstacles frequently — "
            "obstacle-aware harness needed for safe manipulation. **Robotics OOD** for CCC — short source stub; "
            "`wont_wire`. Cross-domain note: obstacle/safety constraints as harness axis (not wired locally)."
        ),
        "wired": False,
        "cybersec": False,
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
    else:
        stub = e["slug"].replace("arxiv-", "").rsplit("-2609", 1)[0]
        checks.append(f'check "no concept" test ! -f "${{REPO_ROOT}}/wiki/concepts/{stub}.md"')
    if e["wired"]:
        checks += [
            f'check "policy K{k}" grep -q "K{k}" "${{REPO_ROOT}}/.cursor/rules/cemini-phase1-policy-wires.mdc"',
            f'check "ccc-rule K{k}" grep -q "K{k}" "${{REPO_ROOT}}/.cursor/rules/ccc-k369-k372-phase1-wires.mdc"',
        ]
    slug = e["concept"] or e["slug"].split("-")[1]
    checks.append(f'check "no clone" test ! -d "${{REPO_ROOT}}/.local/adopts/{slug}"')
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
    print("done K369–K372")


if __name__ == "__main__":
    main()
