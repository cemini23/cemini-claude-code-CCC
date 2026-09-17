#!/usr/bin/env python3
"""Generate K363–K367 wiki ingest artifacts."""
from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
WIKI = REPO / "wiki"
SCRIPTS = REPO / "scripts"
BRIEF = "2026-09-17_ccc-k363-k367-sip-ready.md"
DATE = "2026-09-17"
EGRESS = "cemini-egress-fi:/opt/cemini-bulk/research/ccc"

ENTRIES = [
    {
        "k": 363,
        "arxiv": "2609.18844",
        "slug": "arxiv-refigbench-scientific-figure-harness-2609.18844",
        "concept": "harness-attribution-multimodal-eval",
        "title": "ReFigBench: Scientific Figure Reconstruction as Editable Artifacts",
        "pdf": "arxiv-2609.18844-refigbench-benchmarking-scientific-figure-recons.pdf",
        "verdict": "ADOPT eval-first",
        "narrative": (
            "Multimodal coding agents act through a **harness** (tools, context, execution env). Short proxy scores "
            "(tool traces, screenshot resemblance) cannot attribute failure to model vs harness. ReFigBench evaluates "
            "figure→editable artifact reconstruction as a harness-aware axis. Pairs K334 harness-as-eval-artifact / "
            "K289 evidence-tree eval. Bench runtime **`wont_wire`**."
        ),
        "wired": True,
        "cybersec": False,
        "no_clone": True,
    },
    {
        "k": 364,
        "arxiv": "2609.18849",
        "slug": "arxiv-ask-the-tool-serving-progress-2609.18849",
        "concept": "tool-call-progress-aware-serving",
        "title": "Ask the Tool, Don't Guess: Tool Calls Hold Their Progress",
        "pdf": "arxiv-2609.18849-ask-the-tool-don-t-guess-agent-tool-calls-hold-t.pdf",
        "verdict": "ADOPT policy",
        "narrative": (
            "Agentic requests spend wall-clock time in tools while KV cache holds GPU memory. Serving systems evict/retain "
            "cache by **pre-call duration guesses** (name, history, declared duration) — but no pre-call estimate can know "
            "true tool duration or rank tools reliably. **Serving should read progress from the tool call itself**, not guess. "
            "Pairs K320 usage vs context / token economics / K327 resume boundaries. Awareness only; runtime **`wont_wire`**."
        ),
        "wired": True,
        "cybersec": False,
        "no_clone": True,
    },
    {
        "k": 365,
        "arxiv": "2609.18864",
        "slug": "arxiv-asleval-privacy-exposure-displacement-2609.18864",
        "concept": "privacy-exposure-displacement-eval",
        "title": "ASLEval: Privacy Exposure Displacement in LLM Agent Sessions",
        "pdf": "arxiv-2609.18864-asleval-measuring-privacy-exposure-displacement.pdf",
        "verdict": "Cybersec-primary + ADOPT eval",
        "narrative": (
            "Local privacy proxies (single action, final response, attacker report) miss **unauthorized exposure elsewhere** "
            "in multi-step sessions. **Privacy exposure displacement** = mismatch between local proxy and target-grounded "
            "session exposure. ASLEval = authorization-aware session-level framework. Pairs K315 ToolMinimize PSD / "
            "K277 measurement integrity. **No PoCs.** Runtime **`wont_wire`**."
        ),
        "wired": True,
        "cybersec": True,
        "no_clone": True,
    },
    {
        "k": 366,
        "arxiv": "2609.19091",
        "slug": "arxiv-mcp-traffic-nids-beacon-evasion-2609.19091",
        "concept": "mcp-traffic-network-detection-blind-spot",
        "title": "When Agents Look Like Beacons: NIDS Evasion by MCP Traffic",
        "pdf": "arxiv-2609.19091-when-agents-look-like-beacons-nids-evasion-by-mo.pdf",
        "verdict": "Cybersec-primary + ADOPT policy",
        "narrative": (
            "MCP Streamable HTTP introduces authenticated, high-frequency JSON-RPC agent traffic into enterprise networks. "
            "Without explicit rules, this traffic can resemble **beacon-like cadence** — breaking historical NIDS IoC "
            "assumptions. CCC steal: treat MCP/agent egress as first-class observability surface (pairs K353 registry / "
            "K367 remote MCP observability). **No PoCs / no evasion recipes.** `policy_wired`."
        ),
        "wired": True,
        "cybersec": True,
        "no_clone": True,
    },
    {
        "k": 367,
        "arxiv": "2609.19100",
        "slug": "arxiv-remote-mcp-centralization-observability-2609.19100",
        "concept": "remote-mcp-ecosystem-observability",
        "title": "Network Centralization and Observability in the Remote MCP Ecosystem",
        "pdf": "arxiv-2609.19100-characterizing-network-centralization-and-observ.pdf",
        "verdict": "ADOPT measurement + policy",
        "narrative": (
            "Remote Streamable HTTP MCP shifts from local process execution to **centralized remote deployments** — "
            "three-tier observability framework: catalog metadata (O₀), passive compliance signals (O₁), active probes (O₂). "
            "Unmeasured architectural/security constraints at scale. Pairs K271 MCP auth gateway / K353 unbiased registry "
            "sample / K366 NIDS blind spots. No clone at Phase-0. Runtime **`wont_wire`**."
        ),
        "wired": True,
        "cybersec": False,
        "no_clone": True,
    },
]


def yaml_list(items: list[str]) -> str:
    return "\n".join(f"  - {x}" for x in items)


def write_source(e: dict) -> None:
    k = e["k"]
    related = [f"briefs/{BRIEF}"]
    relations = [f"@briefs/{BRIEF}"]
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
    (WIKI / "sources" / f"{e['slug']}.md").write_text(body, encoding="utf-8")
    print(f"wrote wiki/sources/{e['slug']}.md")


def write_concept(e: dict) -> None:
    k, c = e["k"], e["concept"]
    related = [f"sources/{e['slug']}.md", "concepts/phase1-adopt-wire.md", f"briefs/{BRIEF}"]
    body = f"""---
title: "{e['title']} (CCC K{k})"
type: concept
tags: [concept, k{k}]
keywords: [{e['arxiv']}, k{k}]
related:
{yaml_list(related)}
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

K{k}: {e['verdict']} — synthesized from arXiv {e['arxiv']}.

## Narrative

{e['narrative']}

## Snippets

> "See source page for arXiv {e['arxiv']} locators." [Source: CCC K{k} synthesis]
"""
    (WIKI / "concepts" / f"{c}.md").write_text(body, encoding="utf-8")
    print(f"wrote wiki/concepts/{c}.md")


def write_phase0(e: dict) -> None:
    k = e["k"]
    checks = [f'check "source" test -f "${{REPO_ROOT}}/wiki/sources/{e["slug"]}.md"']
    checks += [
        f'check "concept" test -f "${{REPO_ROOT}}/wiki/concepts/{e["concept"]}.md"',
        f'check "concept wired" grep -q "wire_status: policy_wired" "${{REPO_ROOT}}/wiki/concepts/{e["concept"]}.md"',
    ]
    checks += [
        f'check "policy K{k}" grep -q "K{k}" "${{REPO_ROOT}}/.cursor/rules/cemini-phase1-policy-wires.mdc"',
        f'check "ccc-rule K{k}" grep -q "K{k}" "${{REPO_ROOT}}/.cursor/rules/ccc-k363-k367-phase1-wires.mdc"',
        f'check "no clone" test ! -d "${{REPO_ROOT}}/.local/adopts/{e["concept"]}"',
    ]
    if e["cybersec"]:
        src = f"${{REPO_ROOT}}/wiki/sources/{e['slug']}.md"
        con = f"${{REPO_ROOT}}/wiki/concepts/{e['concept']}.md"
        checks.append(
            f"check \"no attack text\" bash -c \"! grep -rEi 'jailbreak|attack prompt|exploit template' '{src}' '{con}'\""
        )
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
    path = SCRIPTS / f"adopt_k{k}_phase0.sh"
    path.write_text(script, encoding="utf-8")
    path.chmod(0o755)
    print(f"wrote scripts/adopt_k{k}_phase0.sh")


def main() -> None:
    for e in ENTRIES:
        write_source(e)
        write_concept(e)
        write_phase0(e)


if __name__ == "__main__":
    main()
