#!/usr/bin/env python3
"""Generate K358–K362 wiki ingest artifacts."""
from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
WIKI = REPO / "wiki"
SCRIPTS = REPO / "scripts"
BRIEF = "2026-09-16_ccc-k358-k362-sip-ready.md"
DATE = "2026-09-16"
EGRESS = "cemini-egress-fi:/opt/cemini-bulk/research/ccc"

ENTRIES = [
    {
        "k": 358,
        "arxiv": "2609.16635",
        "slug": "arxiv-echopath-gui-replayable-memory-2609.16635",
        "concept": "execution-level-replayable-gui-memory",
        "title": "EchoPath: Execution-Level Replayable Memory for GUI Agents",
        "pdf": "arxiv-2609.16635-echopath-execution-level-replayable-memory-for-g.pdf",
        "verdict": "ADOPT pattern",
        "narrative": (
            "Model-agnostic harness converts **artifact-validated GUI trajectories** into replayable execution-level "
            "memory — reduces redundant observe-plan-act loops on repetitive enterprise GUI workflows (forms, exports, "
            "record updates). Pairs K282 AgentRewind recovery / K321 ASIL structured actions / K348 hybrid GUI+CLI. "
            "GUI runtime **`wont_wire`** — keep cursor-ide-browser; no CUA stack."
        ),
        "wired": True,
        "cybersec": False,
        "no_clone": True,
    },
    {
        "k": 359,
        "arxiv": "2609.17247",
        "slug": "arxiv-drivemcp-adas-agentic-framework-2609.17247",
        "concept": None,
        "title": "DriveMCP: Agentic AI Framework for Advanced Driver Assistance",
        "pdf": "arxiv-2609.17247-drivemcp-an-agentic-ai-framework-for-advanced-dr.pdf",
        "verdict": "OOD stub",
        "narrative": (
            "Modular ADAS agentic pipeline: perception stack + DriveLM VLM front-end → graph-structured scene "
            "understanding + compliance/world_state + safety arbitration. Automotive domain OOD for CCC — "
            "short source stub; `wont_wire`. Steal naming only: domain MCP-style modular orchestration."
        ),
        "wired": False,
        "cybersec": False,
        "no_clone": True,
    },
    {
        "k": 360,
        "arxiv": "2609.17320",
        "slug": "arxiv-emergence-world-multi-agent-stress-test-2609.17320",
        "concept": "long-horizon-multi-agent-adversarial-eval",
        "title": "Emergence World: Adversarial Stress-Testing of Long-Horizon Multi-Agent Systems",
        "pdf": "arxiv-2609.17320-emergence-world-adversarial-stress-testing-of-lo.pdf",
        "verdict": "Cybersec-primary + ADOPT eval",
        "narrative": (
            "Persistent multi-agent deployments propagate failures through memory, tools, other agents, and environment "
            "state — not capturable by isolated response eval. Continuously running adversarial stress-test environment "
            "(eight parallel worlds, ten agents). CCC eval steal: long-horizon **system-level** red-team axis (pairs K260 "
            "adversarial curriculum / K345 commons / K227 Zawinski messaging). **No PoCs.** Runtime **`wont_wire`**."
        ),
        "wired": True,
        "cybersec": True,
        "no_clone": True,
    },
    {
        "k": 361,
        "arxiv": "2609.17523",
        "slug": "arxiv-sciencebuddy-recursive-self-improvement-2609.17523",
        "concept": "recursive-in-recursive-harness-improvement",
        "title": "ScienceBuddy: Recursive-in-Recursive Self-Improvement for Interactive Scientific Agents",
        "pdf": "arxiv-2609.17523-sciencebuddy-recursive-in-recursive-self-improve.pdf",
        "verdict": "ADOPT pattern",
        "narrative": (
            "Interactive scientific workspace couples harness evolution with model RL — **recursive-in-recursive** "
            "self-improvement from user requests, feedback, and execution evidence → tasks + rubrics for continual learning. "
            "Pairs K355 Ecdysis / K331 AutoSciRub rubric-first / K237 misevolution gates. **Never auto-evolve "
            "`.cursor/skills`.** Product release cited — no public SPDX at Phase-0 → no clone. Trainer **`wont_wire`**."
        ),
        "wired": True,
        "cybersec": False,
        "no_clone": True,
    },
    {
        "k": 362,
        "arxiv": "2609.17527",
        "slug": "arxiv-agentic-societies-social-harness-2609.17527",
        "concept": "social-harness-multi-agent-trust",
        "title": "Agentic Societies Need a Social Harness",
        "pdf": "arxiv-2609.17527-agentic-societies-need-a-social-harness.pdf",
        "verdict": "Cybersec-primary + ADOPT policy",
        "narrative": (
            "Agentic societies = agents coordinating across **trust boundaries** for partially aligned principals. "
            "Honest competent agents fail with existing harnesses/messaging; faulty/malicious agents exploit comms "
            "vulnerabilities. CCC steal: **social harness** layer for inter-agent messaging governance (pairs K227 "
            "Zawinski / K277 measurement / K345 commons / K326 external enforcement). **No PoCs.** `policy_wired`."
        ),
        "wired": True,
        "cybersec": True,
        "no_clone": True,
    },
]


def yaml_list(items: list[str]) -> str:
    return "\n".join(f"  - {x}" for x in items)


def write_source(e: dict) -> None:
    k, related = e["k"], [f"briefs/{BRIEF}"]
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
    path = WIKI / "sources" / f"{e['slug']}.md"
    path.write_text(body, encoding="utf-8")
    print(f"wrote {path.relative_to(REPO)}")


def write_concept(e: dict) -> None:
    c, k = e["concept"], e["k"]
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
    path = WIKI / "concepts" / f"{c}.md"
    path.write_text(body, encoding="utf-8")
    print(f"wrote {path.relative_to(REPO)}")


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
            f'check "ccc-rule K{k}" grep -q "K{k}" "${{REPO_ROOT}}/.cursor/rules/ccc-k358-k362-phase1-wires.mdc"',
        ]
    if e["no_clone"]:
        slug = e["concept"] or e["slug"].split("-")[1]
        checks.append(f'check "no clone" test ! -d "${{REPO_ROOT}}/.local/adopts/{slug}"')
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
    print(f"wrote {path.relative_to(REPO)}")


def main() -> None:
    for e in ENTRIES:
        write_source(e)
        if e["concept"]:
            write_concept(e)
        write_phase0(e)


if __name__ == "__main__":
    main()
