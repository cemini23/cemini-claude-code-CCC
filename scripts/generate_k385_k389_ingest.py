#!/usr/bin/env python3
"""Generate K385–K389 wiki ingest artifacts."""
from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DATE = "2026-09-24"
BRIEF = "2026-09-24_ccc-k385-k389-sip-ready.md"
EGRESS = "cemini-egress-fi:/opt/cemini-bulk/research/ccc"
RULE = "ccc-k385-k389-phase1-wires.mdc"

ENTRIES = [
    {
        "arxiv": "2609.27340",
        "concept": None,
        "k": 385,
        "narrative": "**OOD** robotics navigation via MCP. CCC steal is **MCP tool packaging for embodied agents** only — "
        "spatial/semantic tool surfaces, not robot runtime or sim deploy. No clone. Runtime **`wont_wire`**.",
        "pdf": "arxiv-2609.27340-spatial-and-semantic-reasoning-for-llm-driven-ro.pdf",
        "slug": "arxiv-spatial-semantic-robot-navigation-mcp-2609.27340",
        "title": "Spatial and Semantic Reasoning for LLM-Driven Robot Navigation via MCP",
        "verdict": "OOD robotics stub",
        "wired": True,
        "no_clone": "spatial",
    },
    {
        "arxiv": "2609.27636",
        "concept": "regulated-enterprise-multi-agent-governance",
        "k": 386,
        "narrative": "**Governed multi-agent under regulatory constraints** — Solvency II–style audit, oversight, and "
        "role-boundary vocabulary for enterprise agent stacks. **Finance domain OOD** for CCC product runtime; "
        "policy awareness for harness governance discussions (pairs K373 EnterpriseVal / K325 bounded authority). "
        "No clone. Runtime **`wont_wire`**.",
        "pdf": "arxiv-2609.27636-multi-agent-ai-architecture-for-regulated-insure.pdf",
        "slug": "arxiv-regulated-insurers-multi-agent-solvency-2609.27636",
        "title": "Multi-Agent AI Architecture for Regulated Insurers: A Generic AI Framework under Solvency II",
        "verdict": "ADOPT policy awareness",
        "wired": True,
        "no_clone": "regulated-enterprise-multi-agent-governance",
    },
    {
        "arxiv": "2609.27746",
        "concept": "kv-cache-working-set-serving",
        "k": 387,
        "narrative": "**Working-set view of KV cache** for LLM inference — online capacity planning treats cache occupancy "
        "as a dynamic working set, not a fixed prefix (pairs K228 cross-model KV awareness / K320 token economics / "
        "K364 tool-progress-aware serving). Serving and routing awareness only. Runtime **`wont_wire`**.",
        "pdf": "arxiv-2609.27746-the-kv-cache-working-set-online-capacity-plannin.pdf",
        "slug": "arxiv-kv-cache-working-set-capacity-2609.27746",
        "title": "The KV Cache Working Set: Online Capacity Planning for LLM Inference Systems",
        "verdict": "ADOPT awareness",
        "wired": True,
        "no_clone": "kv-cache-working-set-serving",
    },
    {
        "arxiv": "2609.28372",
        "concept": "agent-heuristic-surrogate-consumer-eval",
        "k": 388,
        "narrative": "Agentic shopping systems **operationalize human heuristics** as a **surrogate consumer** — eval and "
        "policy must treat **construct validity** when benchmarks score agents as consumer proxies (pairs K277 "
        "labels ≠ endpoints / K371 overclaiming propensity). **No PoCs.** Runtime **`wont_wire`**; concept "
        "**`policy_wired`**.",
        "pdf": "arxiv-2609.28372-shopping-by-algorithm-how-agentic-ai-deploys-hum.pdf",
        "slug": "arxiv-shopping-algorithm-agent-heuristic-surrogate-2609.28372",
        "title": "Shopping by Algorithm: How Agentic AI Deploys Human Heuristics as a Surrogate Consumer",
        "verdict": "ADOPT eval + policy",
        "wired": True,
        "no_clone": "agent-heuristic-surrogate-consumer-eval",
    },
    {
        "arxiv": "2609.28416",
        "concept": "agent-editing-world-model",
        "k": 389,
        "narrative": "LLM agents **maintain and edit explicit world models** for planning — harness pattern distinct from "
        "implicit context-only state (pairs K283 Twin validate-before-act / K296 terminal-state eval / K334 "
        "harness-as-eval-artifact). **No clone** unless SPDX verified at Phase-0. Runtime **`wont_wire`**.",
        "pdf": "arxiv-2609.28416-agent-editing-world-model-rethinking-world-model.pdf",
        "slug": "arxiv-agent-editing-world-model-2609.28416",
        "title": "Agent-Editing World Model: Rethinking World Modeling for LLM Agents",
        "verdict": "ADOPT pattern",
        "wired": True,
        "no_clone": "agent-editing-world-model",
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
    print("done K385–K389")


if __name__ == "__main__":
    main()
