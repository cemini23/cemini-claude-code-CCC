---
title: "Assay: Claims That Decay With the Code. Content-Addressed Evidence Graphs for Accountable AI-Assisted Software Delivery (CCC K406)"
type: concept
tags: [concept, k406]
keywords: [2609.36170, k406]
related:
  - sources/arxiv-assay-content-addressed-evidence-graphs-2609.36170.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-09-30_ccc-k406-k410-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-09-30
updated: 2026-09-30
---

## Relations

- `@sources/arxiv-assay-content-addressed-evidence-graphs-2609.36170.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-09-30_ccc-k406-k410-sip-ready.md`

## Raw Concept

K406: CONDITIONAL-GO (Apache-2.0) — arXiv 2609.36170.

## Narrative

**Assay — claims decay with the code.** Every agent claim (tests pass, no secrets, behavior preserved) is bound to the **Merkle hash of the dependency cone** of the code it covers. Staleness becomes a hash comparison, not a judgment. **Blast radius == staleness frontier** (Prop. 3): the reach an agent wants before editing and the evidence a gate wants voided after are the same set, from one traversal. Adds a **merge gate that consults no model** — eight mechanical checks: coverage, freshness, signatures, exit codes, plausibility, **evidence monotonicity** (the mechanical form of "do not delete the failing test"), and review status. Blocks 9/9 scripted adversarial behaviors (self-approval, forged ledger, deleted failing test, stale evidence). A **600-token brief costs 14×–114× less** than an exploration proxy. Ships a **dependency-free Python CLI, git hooks, and an MCP server**. Pairs K403 Tracekit (tamper-evident audit) / K394 trace tampering / K402 MCP error surfaces / K405 TokenCast + K320 context cost / reward-tampering literature. **Phase-0: Apache-2.0**, 0 stars, pushed 2026-09-27, no community vetting yet. Runtime **`wont_wire`** — see the MCP audit below. Concept **`policy_wired`**.

## MCP server audit (Phase-0, 2026-09-30)

Completed against `OmShiv/assay-research` at `main` (101 files, `src/assay/` package).

**Transport — clean.** `src/assay/mcp.py` is documented as "Minimal MCP over **stdio**, newline-delimited JSON-RPC 2.0". Registered as `claude mcp add assay -- python -m assay --root "$PWD" mcp`. Stdio is the safest MCP transport class: no listening socket, no remote attack surface, no credential store. No auth is needed or read.

**Dependencies — confirmed zero.** `pyproject.toml` has `dependencies = []`. The paper's "dependency-free" claim holds. `pytest`, `matplotlib`, `networkx`, `numpy`, `tiktoken` are dev/experiments extras only.

**Ruling — `wont_wire` at runtime.** The blocker is one tool. `attest` accepts a model-supplied `command` string and executes it:

```python
def run_evidence(command: str, cwd: str, timeout: int = 900, tail_chars: int = 600) -> dict:
    proc = subprocess.run(command, shell=True, cwd=cwd, capture_output=True, timeout=timeout)
```

That is **arbitrary shell execution with `shell=True`, a 900-second timeout, as the invoking user**. Three consequences for CCC:

1. **The permission prompt lies by omission.** A user approving a tool call named `attest` is authorizing a shell command. CCC's permission surface distinguishes `Bash` from everything else; this re-labels shell as a domain tool.
2. **`shell=True` on a model-controlled string** is command injection by construction — pipes, redirects, `&&`, and `$(...)` all evaluate.
3. **No bounding in the transport.** By design, "the separation of duties and every other invariant are enforced by the ledger, not by the transport." The ledger governs claim *verdicts*, not command *execution*.

The design is defensible on its own terms — attesting "tests pass" requires running the tests. The objection is scope and labeling, not intent.

**Also repo-mutating:** `assay init --hook --agents` writes a pre-commit hook into `.git/hooks` and appends an `AGENTS.md` block. Install must be opt-in.

**What is adoptable now, without the code:** the protocol. Cone-hash claim binding, the mechanical 8-check gate, and evidence monotonicity are all implementable as a CCC policy rule with no MCP server and no shell execution. See `@concepts/agent-completion-verification-gates.md` and `@concepts/harness-as-eval-artifact.md`.

**Unblock condition:** re-classify `attest` as a shell-equivalent capability, or bound it to an operator-approved command allowlist. Until then, no runtime wire.

## Snippets

> "See source page for arXiv 2609.36170 locators." [Source: CCC K406 synthesis]

## Resolution (2026-10-08)

**Runtime `wont_wire`, protocol adopted.** The `attest` finding stands — `subprocess.run(...,
shell=True)` behind a non-`Bash` tool name — so no runtime wire without an operator ticket plus an
allowlist or fail-closed bound. **The protocol is adopted as policy instead**, because it needs no
code: bind a claim to the content it covers; staleness is drift of that subject, not passage of time;
the gate consults no model; and **evidence monotonicity — never delete the failing test.** Full text
in `@.cursor/rules/cemini-phase1-policy-wires.mdc` § "Assay protocol adopted". This closes the item.
