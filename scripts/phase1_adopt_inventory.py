#!/usr/bin/env python3
"""Phase-1 adopt inventory — scan .local/adopts and join wiki wire_status.

Usage:
  python3 scripts/phase1_adopt_inventory.py
  python3 scripts/phase1_adopt_inventory.py --write-brief
  python3 scripts/phase1_adopt_inventory.py --roots ccc,osint
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path

CCC = Path(__file__).resolve().parents[1]
OSINT = Path("/Users/claudiobarone/Projects/OSINT WORKSPACE")

ROOTS = {
    "ccc": CCC,
    "osint": OSINT,
}

# Surfaces we never inventory for local wire backlog
SKIP_LABELS = ("image-gen", "3d-printing", "3d printing")

WIRE_RE = re.compile(r"^wire_status:\s*(\S+)", re.M)
TARGET_RE = re.compile(r"^wire_target:\s*(.+)$", re.M)
TITLE_RE = re.compile(r"^title:\s*[\"']?(.+?)[\"']?\s*$", re.M)
VERDICT_RE = re.compile(
    r"\*\*(GO|NO-GO|CONDITIONAL-GO|REFERENCE|ADOPT|WATCH)\*\*", re.I
)

# Clone dir name → wiki entity path relative to wiki/
CLONE_ENTITY_ALIASES = {
    "ccc": {
        "MemHarness": "entities/tools/memharness.md",
        "Tycho": "entities/tools/tycho-arc-agi.md",
        "AgentRadio": "entities/tools/agentradio.md",
        "askchem": "entities/tools/askchem.md",
        "shard-demo": "entities/tools/shard-secure-harness-distribution.md",
        "agent-security-lab": "entities/tools/shard-secure-harness-distribution.md",
        "AIH-Infra": "entities/tools/aih-infra.md",
        "euclid-mcp": "entities/tools/euclid-mcp.md",
        "RRBench": "entities/tools/rrbench.md",
    },
    "osint": {
        "agentradio": "entities/tools/agentradio.md",
    },
}


@dataclass
class CloneRow:
    surface: str
    name: str
    path: Path
    size_mb: float
    has_git: bool
    license_hint: str
    entity: str | None
    wire_status: str
    wire_target: str
    recommended: str


def dir_size_mb(path: Path) -> float:
    total = 0
    try:
        for p in path.rglob("*"):
            if p.is_file():
                try:
                    total += p.stat().st_size
                except OSError:
                    pass
    except OSError:
        return 0.0
    return total / (1024 * 1024)


def license_hint(path: Path) -> str:
    for name in ("LICENSE", "LICENSE.md", "COPYING"):
        f = path / name
        if f.is_file():
            try:
                head = f.read_text(errors="ignore")[:200]
            except OSError:
                return "?"
            if "MIT" in head:
                return "MIT"
            if "Apache" in head:
                return "Apache-2.0"
            if "GPL" in head:
                return "GPL?"
            return "see LICENSE"
    return "none"


def index_entities(wiki: Path) -> dict[str, Path]:
    out: dict[str, Path] = {}
    tools = wiki / "entities" / "tools"
    if not tools.is_dir():
        return out
    for p in tools.glob("*.md"):
        key = p.stem.lower().replace("-", "").replace("_", "")
        out[key] = p
        out[p.stem.lower()] = p
    return out


def match_entity(name: str, entities: dict[str, Path]) -> Path | None:
    n = name.lower()
    compact = re.sub(r"[^a-z0-9]", "", n)
    for key, path in entities.items():
        if key == n or key == compact:
            return path
        if compact in key or key in compact:
            return path
    # fuzzy: memharness <-> MemHarness
    for key, path in entities.items():
        if compact[:6] and compact[:6] in key:
            return path
    return None


def parse_entity(path: Path | None) -> tuple[str, str, str]:
    if path is None or not path.is_file():
        return "unwired", "", ""
    text = path.read_text(errors="ignore")
    ws = WIRE_RE.search(text)
    wt = TARGET_RE.search(text)
    status = ws.group(1) if ws else "unwired"
    target = wt.group(1).strip() if wt else ""
    verd = VERDICT_RE.findall(text)
    verd_s = ",".join(dict.fromkeys(v.upper() for v in verd[:3]))
    return status, target, verd_s


def recommend(status: str, size_mb: float, name: str, verd: str) -> str:
    if status in ("policy_wired", "runtime_wired"):
        return "done"
    if status == "wont_wire":
        return "keep REFERENCE"
    n = name.lower()
    trainers = (
        "memharness",
        "agentradio",
        "shard-demo",
        "rrbench",
        "openevolve",
        "biosec",
    )
    if any(t in n for t in trainers) or size_mb > 30:
        if "MCP" in verd or "drop-in" in verd.lower():
            return "policy_or_runtime"
        return "wont_wire (trainer/repro?)"
    if "REFERENCE" in verd and "GO" in verd:
        return "policy if ADOPT pattern; else wont_wire"
    return "classify: policy vs runtime vs wont_wire"


def scan_root(label: str, root: Path) -> list[CloneRow]:
    adopts = root / ".local" / "adopts"
    wiki = root / "wiki"
    rows: list[CloneRow] = []
    if not adopts.is_dir():
        return rows
    entities = index_entities(wiki)
    aliases = CLONE_ENTITY_ALIASES.get(label, {})
    for child in sorted(adopts.iterdir()):
        if not child.is_dir() or child.name.startswith("."):
            continue
        ent = None
        if child.name in aliases:
            cand = wiki / aliases[child.name]
            if cand.is_file():
                ent = cand
        if ent is None:
            ent = match_entity(child.name, entities)
        status, target, verd = parse_entity(ent)
        size = dir_size_mb(child)
        rows.append(
            CloneRow(
                surface=label,
                name=child.name,
                path=child,
                size_mb=round(size, 1),
                has_git=(child / ".git").exists(),
                license_hint=license_hint(child),
                entity=str(ent.relative_to(wiki)) if ent else None,
                wire_status=status,
                wire_target=target,
                recommended=recommend(status, size, child.name, verd),
            )
        )
    return rows


def render_md(rows: list[CloneRow]) -> str:
    lines = [
        f"# Phase-1 adopt inventory — {date.today().isoformat()}",
        "",
        "Generated by `scripts/phase1_adopt_inventory.py`.",
        "Skip Image-gen / 3D local wire backlog (operator policy).",
        "",
        f"**Clones scanned:** {len(rows)}",
        f"**Unwired:** {sum(1 for r in rows if r.wire_status == 'unwired')}",
        f"**Policy wired:** {sum(1 for r in rows if r.wire_status == 'policy_wired')}",
        f"**Runtime wired:** {sum(1 for r in rows if r.wire_status == 'runtime_wired')}",
        f"**Wont wire:** {sum(1 for r in rows if r.wire_status == 'wont_wire')}",
        "",
        "| Surface | Clone | MB | SPDX | Entity | wire_status | Recommended |",
        "|---------|-------|----|------|--------|-------------|-------------|",
    ]
    for r in rows:
        ent = r.entity or "—"
        lines.append(
            f"| {r.surface} | `{r.name}` | {r.size_mb} | {r.license_hint} | "
            f"{ent} | `{r.wire_status}` | {r.recommended} |"
        )
    lines.append("")
    lines.append("## Next")
    lines.append("")
    lines.append("1. `/phase1` — classify Top N unwired → policy or wont_wire.")
    lines.append("2. Prefer one thematic Cursor rule over one rule per paper.")
    lines.append("3. Runtime wire only for drop-in MCP/skill clients (operator OK).")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--roots",
        default="ccc,osint",
        help="Comma-separated: ccc,osint",
    )
    ap.add_argument(
        "--write-brief",
        action="store_true",
        help="Write briefs/YYYY-MM-DD_phase1-adopt-inventory.md under CCC",
    )
    args = ap.parse_args()
    rows: list[CloneRow] = []
    for key in args.roots.split(","):
        key = key.strip().lower()
        if key in SKIP_LABELS:
            continue
        root = ROOTS.get(key)
        if root is None or not root.is_dir():
            print(f"WARN: skip missing root {key}", file=sys.stderr)
            continue
        rows.extend(scan_root(key, root))
    md = render_md(rows)
    print(md)
    if args.write_brief:
        out = CCC / "briefs" / f"{date.today().isoformat()}_phase1-adopt-inventory.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(md)
        print(f"\nWrote {out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
