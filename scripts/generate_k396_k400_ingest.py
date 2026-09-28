#!/usr/bin/env python3
"""Generate K396–K400 wiki ingest artifacts."""
from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DATE = "2026-09-28"
BRIEF = "2026-09-28_ccc-k396-k400-sip-ready.md"
EGRESS = "cemini-egress-fi:/opt/cemini-bulk/research/ccc"
RULE = "ccc-k396-k400-phase1-wires.mdc"

ENTRIES = [
    {
        "arxiv": "2609.30717",
        "concept": "recommendation-tool-orchestration-fuzzy-intent-eval",
        "k": 396,
        "narrative": "**RecToolBench** evaluates **recommendation-specific tool orchestration** when user intent is "
        "**fuzzy** — not generic tool-use alone (pairs K316 LifePlanner constraint integration / K259 tool grounding / "
        "K318 step-wise routing). Treat rec-domain orchestration as its own harness axis. No clone unless SPDX. Runtime "
        "**`wont_wire`**; concept **`policy_wired`**.",
        "pdf": "arxiv-2609.30717-rectoolbench-benchmarking-recommendation-specifi.pdf",
        "slug": "arxiv-rectoolbench-fuzzy-intent-tool-orchestration-2609.30717",
        "title": "RecToolBench: Benchmarking Recommendation-Specific Tool Orchestration under Fuzzy User Intent",
        "verdict": "ADOPT eval-first",
        "wired": True,
        "no_clone": "rectoolbench",
    },
    {
        "arxiv": "2609.31358",
        "concept": "safety-bounded-sdc-mcp-gateway",
        "k": 397,
        "narrative": "**Safety-bounded SDC-to-MCP gateway** for medical agents — bounded envelope between structured clinical "
        "data/control (SDC) and MCP tool surface (pairs K337 capability leases / K271 MCP auth gateway / K377 clinical "
        "MCP tool-surface steal). **Clinical runtime OOD** for CCC; policy awareness only. **No PoCs.** No clone. Runtime "
        "**`wont_wire`**; concept **`policy_wired`**.",
        "pdf": "arxiv-2609.31358-a-safety-bounded-sdc-to-mcp-gateway-for-medical.pdf",
        "slug": "arxiv-safety-bounded-sdc-mcp-gateway-medical-2609.31358",
        "title": "A Safety-Bounded SDC-to-MCP Gateway for Medical AI Agents",
        "verdict": "ADOPT policy awareness",
        "wired": True,
        "no_clone": "sdc-mcp-gateway",
    },
    {
        "arxiv": "2609.31511",
        "concept": None,
        "k": 398,
        "narrative": "**OOD** deployed Arabic **voice** platform for grounded religious Q&A — product/domain stub only; no CCC "
        "harness runtime. **Source only.** No clone. Runtime **`wont_wire`**.",
        "pdf": "arxiv-2609.31511-muslim-a-deployed-arabic-voice-ai-platform-for-g.pdf",
        "slug": "arxiv-muslim-arabic-voice-ai-platform-2609.31511",
        "title": "Muslim: A Deployed Arabic Voice AI Platform for Grounded Islamic Knowledge",
        "verdict": "OOD voice domain stub",
        "wired": True,
        "no_clone": "muslim-voice",
    },
    {
        "arxiv": "2609.31524",
        "concept": None,
        "k": 399,
        "narrative": "**OOD** medical/surgical **Critical View of Safety** assessment — structured reasoning agent framework for "
        "interpretable safety-critical workflows. CCC steal limited to **structured reasoning trace** vocabulary only; no "
        "clinical deploy. **Source only.** No clone. Runtime **`wont_wire`**.",
        "pdf": "arxiv-2609.31524-structured-reasoning-agentic-framework-for-inter.pdf",
        "slug": "arxiv-structured-reasoning-cvsa-safety-2609.31524",
        "title": "Structured Reasoning Agentic Framework for Interpretable Critical View of Safety Assessment",
        "verdict": "OOD medical safety stub",
        "wired": True,
        "no_clone": "cvsa-reasoning",
    },
    {
        "arxiv": "2609.31562",
        "concept": "agentic-economies-autonomous-science-governance",
        "k": 400,
        "narrative": "**Agentic economies** for autonomous scientific discovery — market-like coordination among research agents "
        "raises **commons governance + measurement integrity** questions (pairs K345 research swarm commons / K277 "
        "construct validity). Eval and policy awareness; **no PoCs.** No clone. Runtime **`wont_wire`**; concept "
        "**`policy_wired`**.",
        "pdf": "arxiv-2609.31562-agentic-economies-for-autonomous-scientific-disc.pdf",
        "slug": "arxiv-agentic-economies-autonomous-scientific-discovery-2609.31562",
        "title": "Agentic Economies for Autonomous Scientific Discovery",
        "verdict": "ADOPT eval + policy",
        "wired": True,
        "no_clone": "agentic-economies",
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
    print("done K396–K400")


if __name__ == "__main__":
    main()
