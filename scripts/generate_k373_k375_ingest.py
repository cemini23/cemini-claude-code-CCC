#!/usr/bin/env python3
"""Generate K373–K375 wiki ingest artifacts."""
from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DATE = "2026-09-21"
BRIEF = "2026-09-21_ccc-k373-k375-sip-ready.md"
EGRESS = "cemini-egress-fi:/opt/cemini-bulk/research/ccc"

ENTRIES = [
    {
        "k": 373,
        "arxiv": "2609.21841",
        "slug": "arxiv-enterpriseval-enterprise-genai-evaluation-2609.21841",
        "concept": "enterprise-use-case-genai-evaluation",
        "title": "EnterpriseVal: Quantifying the Efficacy, Reliability and Value of Generative AI in the Enterprise",
        "pdf": "arxiv-2609.21841-enterpriseval-quantifying-the-efficacy-reliabili.pdf",
        "verdict": "ADOPT eval-first",
        "narrative": (
            "Public benchmarks answer “what can the model do?” — enterprise deployment needs "
            "“is this workflow fit, reliable, safe and worth scaling on our data under our controls?”. "
            "**EnterpriseVal** freezes the **socio-technical configuration** (model, prompts, retrieval, tools, "
            "guardrails, human oversight) and scores a metric catalogue spanning fidelity, utility, efficiency, "
            "reliability, assurance, and oversight. A two-tier **REJECT / CONDITIONAL / SCALE** gate maps "
            "metric vectors with confidence bounds to deployment decisions; reviewer catch rate is a measured "
            "parameter. Pilot: credit-memo drafting 88% citation precision / 1.6% hallucination vs gates 70% / 5%; "
            "procedure transformation analyst effort 27.4→2.9 h/doc. Pairs K331 rubric-before-run / K289 evidence-tree "
            "eval / K277 measurement integrity / K151 CAGE-1 governance. No public product repo → no clone. "
            "Runtime **`wont_wire`**."
        ),
        "wired": True,
    },
    {
        "k": 374,
        "arxiv": "2609.21843",
        "slug": "arxiv-industrial-test-failure-rca-llm-agents-2609.21843",
        "concept": "industrial-test-failure-rca-agents",
        "title": "Supporting Industrial Test-Failure Analysis with LLM-Based Systems: An Experience Report",
        "pdf": "arxiv-2609.21843-supporting-industrial-test-failure-analysis-with.pdf",
        "verdict": "ADOPT pattern",
        "narrative": (
            "Industrial nightly regression failures require **multi-source RCA** across controller and device logs. "
            "Westermo case study: tool-augmented LLM workflows in **single-agent** vs **orchestrated multi-agent** "
            "configurations on two real failure scenarios; six practitioners + 120 repeated runs. "
            "Neither configuration showed consistent practitioner-perceived quality advantage — **single-agent was "
            "faster and cheaper**, making it the practical baseline; multi-agent benefits need harder scenarios. "
            "Eval axes: perceived correctness, reasoning quality, fix realism, clarity, usefulness, trust, cost, "
            "duration, consistency. Pairs K341 evidence-grounded RCA / K306 ARGUS diagnose-not-auto-remediate. "
            "Industrial domain OOD for CCC runtime; pattern **`policy_wired`**. No clone."
        ),
        "wired": True,
    },
    {
        "k": 375,
        "arxiv": "2609.22000",
        "slug": "arxiv-recreationworld-hybrid-cua-environments-2609.22000",
        "concept": "hybrid-cua-recreation-environments",
        "title": "RecreationWorld: Scalable and Verifiable Environments for Hybrid Computer-Use Agents",
        "pdf": "arxiv-2609.22000-recreationworld-scalable-and-verifiable-environm.pdf",
        "verdict": "ADOPT eval-first",
        "narrative": (
            "**Hybrid CUAs** interleave GUI exploration, code implementation, and visual verification — neither "
            "GUI-only nor terminal-only agents suffice. **Recreation** task: given a running reference app, discover "
            "behavior and build a faithful implementation (reference = oracle for hidden behavioral tests). "
            "**RECREATIONWORLD**: five-platform reproducible envs (Ubuntu, macOS, Windows, Android, Web) + unified "
            "harness with native GUI control and coding tools. **RECREATIONBENCH**: 250 tasks (50/platform) with "
            "programmatic + visual assertions validated on reference then frozen; GPT-6 Astra leads at 58.1% overall "
            "but full programmatic pass on only 2.8% of tasks. Training trajectories transfer +17.9 pp on OOD benchmarks. "
            "Pairs K348 CUA-Universe hybrid GUI+CLI / K321 ASIL structured actions over screenshots. "
            "GitHub/HuggingFace cited — **WATCH** until SPDX verified; no clone at Phase-0. GUI runtime **`wont_wire`** "
            "— keep cursor-ide-browser."
        ),
        "wired": True,
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
    rule = "ccc-k373-k375-phase1-wires.mdc"
    checks = [f'check "source" test -f "${{REPO_ROOT}}/wiki/sources/{e["slug"]}.md"']
    if e["concept"]:
        checks += [
            f'check "concept" test -f "${{REPO_ROOT}}/wiki/concepts/{e["concept"]}.md"',
            f'check "concept wired" grep -q "wire_status: policy_wired" "${{REPO_ROOT}}/wiki/concepts/{e["concept"]}.md"',
        ]
    if e["wired"]:
        checks += [
            f'check "policy K{k}" grep -q "K{k}" "${{REPO_ROOT}}/.cursor/rules/cemini-phase1-policy-wires.mdc"',
            f'check "ccc-rule K{k}" grep -q "K{k}" "${{REPO_ROOT}}/.cursor/rules/{rule}"',
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
    print("done K373–K375")


if __name__ == "__main__":
    main()
