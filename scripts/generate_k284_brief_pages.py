#!/usr/bin/env python3
"""Fill CCC pages for the k284 daily brief (2026-10-07).

Source: `briefs/2026-10-07_k284-ccc-design-registries.md` — CCC's own pipeline brief.
Two threads warrant pages: the design-contract MCP lead (Integrate, zero CCC coverage) and
the industry snapshot (claims about the ecosystem that bear on CCC doctrine).
"""
from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DATE = "2026-10-07"
BRIEF = "2026-10-07_k284-ccc-design-registries.md"

PAGES = [
    {
        "path": "wiki/entities/mcp-servers/design-registry-mcp.md",
        "title": "Design-registry MCP servers — design contract for coding agents",
        "type": "entity",
        "tags": "[entity, mcp-server, design-system, k284, lead]",
        "keywords": "[refero, 21st.dev, uiverse, DESIGN.md, design tokens, shadcn, design contract]",
        "related": [
            "concepts/agent-authored-frontend-drift.md",
            "concepts/mcp-server-catalog-curation.md",
        ],
        "wire_status": "unwired",
        "body": """## Narrative

**The gap.** Agent-written frontends drift because the agent has **no design contract** — it
composes plausible markup with no reference to the project's tokens, spacing scale, or component
library. Three MCP connectors address it, surfaced by `@briefs/2026-10-07_k284-ccc-design-registries.md`:

| Connector | What it exposes |
|-----------|-----------------|
| `styles.refero.design` (Refero Styles) | Streams a **`DESIGN.md`** design-token file into Cursor / Claude / Codex |
| `21st.dev` | **shadcn** component registry over MCP |
| `uiverse.io` | CSS / Tailwind controls (also used by CeminiDFS and CeminiParlays UI) |

**Status: LEAD, not adoption.** The k284 brief sets the boundary explicitly — **"MCP install =
human-gated. Treat as a lead."** No Phase-0 has run: no license check, no transport/auth read, no
review of what these servers read or where they send data. **Do not install.**

**Why it is worth tracking.** The shape is the interesting part, not the vendors: **a design token
file as an MCP-served artifact** is a *contract* the agent can be held to, which is the same
movement as `@concepts/schema-bound-mcp-tool-surface.md` — move the constraint out of the prompt and
into something checkable. If CCC ever does frontend work with an agent, the question is whether the
design system is *stated* in a prompt or *served* as a contract.

**Phase-0 to run before any install:** SPDX licence per connector; stdio vs HTTP transport; what
credentials it reads; whether it transmits the project's design tokens anywhere; and whether the
registry content is mirrored or fetched live (catalog-churn risk — see
`@concepts/mcp-server-catalog-curation.md`).

## Snippets

> "Agent-written frontends drift because the agent has no design contract." [Source:
> `@briefs/2026-10-07_k284-ccc-design-registries.md`]

## Dead Ends

- **Not installed, not cloned.** Recorded as a lead so the next frontend-facing workstream does not
  rediscover it.
""",
    },
    {
        "path": "wiki/concepts/agent-pr-volume-exceeds-human.md",
        "title": "Agent-authored PRs exceed human-authored PRs — the review-capacity gap",
        "type": "concept",
        "tags": "[concept, ecosystem, code-review, k284, audit]",
        "keywords": "[agent PRs, code review, LGTM, review capacity, deterministic gates, audit change set]",
        "related": [
            "concepts/agent-completion-verification-gates.md",
            "concepts/evidence-gated-delivery.md",
            "concepts/repo-level-verified-code-proof-eval.md",
        ],
        "body": """## Narrative

**A measured change in the shape of software work**, reported in the k284 brief from The Pragmatic
Engineer's LDX3 keynote (GitHub / Linear / Factory data):

- **Agent-authored pull requests exceeded human-authored ones on GitHub in August 2026** — a **9×
  rise in 8 months**.
- **"Code reviews are dead"** — review has degraded into a **theatre of LGTM stamps**, and quality
  and reliability are **falling**.
- Migrations collapse from **years to weeks**.
- Old practices are returning: **tests, tracer bullets, planning**.
- **AI cost is a top concern** — open models plus smart routing cut Uber's per-token cost 50%+.

**Why CCC cares: this is the empirical case for the wiki's own doctrine.** If agent-authored change
arrives faster than human review capacity can absorb it, then **review cannot be the gate**. The
consequence is the position CCC already holds in several places — **audit the change set with
deterministic gates, not by reviewing harder**. See
`@concepts/agent-completion-verification-gates.md`, `@concepts/evidence-gated-delivery.md`, and the
mechanical-gate work in K406 Assay and K424's graded ladder.

**The pairing worth noting:** the same brief that reports review degrading also reports the
*mechanical* answers improving — K431's step-level process delivery (adherence 76–95% → 95–99%),
K434's honest measurement that we do **not** yet know history-based compaction timing beats a token
budget, and K428's certified verifier bank. **Deterministic, checkable signals are the direction;
"review more carefully" is not.**

**Confidence `[TENTATIVE]`:** these are **conference-keynote figures cited in a brief**, not a paper
with a released methodology. The direction is consistent with other sources CCC holds; the specific
numbers (9×, 50%+) are single-source and unreproduced here. Treat as a trend signal, not a measured
rate.

## Snippets

> "Agent-authored PRs exceeded human-authored ones on GitHub in August 2026 (9× in 8 months)." [Source:
> `@briefs/2026-10-07_k284-ccc-design-registries.md`, citing The Pragmatic Engineer LDX3 keynote]

> "**Code reviews are dead** — a theater of LGTM stamps. **Quality and reliability falling.**"
> [Source: same]
""",
    },
]


def yaml_list(items):
    return "\n".join(f"  - {x}" for x in items)


for p in PAGES:
    f = REPO / p["path"]
    if f.exists():
        print(f"  exists, skipping: {p['path']}")
        continue
    extra = ""
    if p.get("wire_status"):
        extra = f'wire_status: {p["wire_status"]}\n'
    body = f"""---
title: "{p['title']} (CCC k284)"
type: {p['type']}
tags: {p['tags']}
keywords: {p['keywords']}
related:
{yaml_list(p['related'])}
{extra}maturity: draft
created: {DATE}
updated: {DATE}
---

## Relations

{chr(10).join(f'- `@{r}`' for r in p['related'])}

## Raw Concept

Filed from `@briefs/{BRIEF}` (CCC k284 daily brief, {DATE}). Not paper-derived — the brief is the
source, and the brief's own boundary applies.

{p['body']}"""
    f.write_text(body, encoding="utf-8")
    print(f"  wrote {p['path']}")

# reciprocal backlinks on the older pages
BACK = {
    "wiki/concepts/agent-completion-verification-gates.md": ["concepts/agent-pr-volume-exceeds-human.md"],
    "wiki/concepts/mcp-server-catalog-curation.md": ["entities/mcp-servers/design-registry-mcp.md"],
}
for rel, adds in BACK.items():
    f = REPO / rel
    if not f.exists():
        print(f"  MISS {rel}")
        continue
    t = f.read_text(encoding="utf-8")
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
    for off, a in enumerate(adds):
        if f"  - {a}" not in "\n".join(lines[ri:end]):
            lines.insert(j + off, f"  - {a}")
    f.write_text("\n".join(lines), encoding="utf-8")
    print(f"  backlinked {rel}")

# log entry
log = REPO / "wiki/log.md"
entry = f"""## [{DATE}] route | k284 daily brief — design-registry lead + the review-capacity gap

- **Source brief:** `briefs/{BRIEF}` (CCC's own pipeline brief, not an OSINT route).
- **Pages written:** `entities/mcp-servers/design-registry-mcp.md` (Refero Styles / 21st.dev /
  uiverse.io — **LEAD, not adoption**; the brief says "MCP install = human-gated") and
  `concepts/agent-pr-volume-exceeds-human.md` (agent PRs > human PRs Aug 2026; "code reviews are
  dead" — the empirical case for deterministic gates over "review harder"; `[TENTATIVE]`, keynote
  figures).
- **Overlap confirmed:** k284 independently cites **VeriFine** and **compaction harm**, both landed
  this session as K435 and K434.

"""
t = log.read_text(encoding="utf-8")
if "k284 daily brief" not in t:
    log.write_text(entry + t, encoding="utf-8")
    print("  log entry added")
print("done k284 pages")
