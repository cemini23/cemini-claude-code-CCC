#!/usr/bin/env python3
"""AID-Guard commit-revalidation prototype (CCC K302).

Admission approval is not effect authority. This helper stores one reservation
for a canonical (tool, args) payload, revalidates the exact bytes at commit,
and refuses blind retries / in-flight successors.

Low-risk demo path: local.hot_md (gitignored session cache). Same protocol
applies to github.create_or_update_file and stash writes — preview/HITL still
required (K239). Not a Stripe/LIVE proxy.

Store: <repo>/.local/aid-guard/  (gitignored). Override with AID_GUARD_STORE.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_STORE = REPO_ROOT / ".local" / "aid-guard"

ALLOWED_TOOLS = frozenset(
    {
        "local.hot_md",
        "github.create_or_update_file",
        "stash.write",
    }
)


def _store_dir() -> Path:
    raw = os.environ.get("AID_GUARD_STORE")
    p = Path(raw) if raw else DEFAULT_STORE
    p.mkdir(parents=True, exist_ok=True)
    return p


def canonical_hash(tool: str, args: Any) -> str:
    blob = json.dumps({"tool": tool, "args": args}, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _path(rid: str) -> Path:
    if not rid or "/" in rid or rid.startswith("."):
        raise SystemExit("invalid reservation id")
    return _store_dir() / f"{rid}.json"


def _load(rid: str) -> dict:
    p = _path(rid)
    if not p.is_file():
        raise SystemExit(f"no reservation {rid}")
    return json.loads(p.read_text(encoding="utf-8"))


def _save(rec: dict) -> None:
    p = _path(rec["id"])
    rec["updated"] = _now()
    p.write_text(json.dumps(rec, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _load_args(args_json: str | None, args_file: str | None) -> Any:
    if bool(args_json) == bool(args_file):
        raise SystemExit("pass exactly one of --args-json or --args-file")
    if args_file:
        return json.loads(Path(args_file).read_text(encoding="utf-8"))
    return json.loads(args_json)


def cmd_reserve(rid: str, tool: str, args: Any) -> None:
    if tool not in ALLOWED_TOOLS:
        raise SystemExit(f"tool not on the low-risk allowlist: {tool}")
    p = _path(rid)
    if p.exists():
        raise SystemExit(f"reservation {rid} already exists")
    rec = {
        "id": rid,
        "tool": tool,
        "args": args,
        "hash": canonical_hash(tool, args),
        "state": "reserved",
        "created": _now(),
        "updated": _now(),
        "outcome": None,
    }
    _save(rec)
    print(f"RESERVED {rid} {rec['hash'][:12]}")


def cmd_commit(rid: str, tool: str, args: Any) -> None:
    rec = _load(rid)
    if rec["state"] == "ambiguous":
        raise SystemExit("hold: outcome ambiguous — do not retry or mint a successor")
    if rec["state"] != "reserved":
        raise SystemExit(f"cannot commit from state={rec['state']}")
    if rec["tool"] != tool or rec["hash"] != canonical_hash(tool, args):
        raise SystemExit("unauthorized: request mutated after approval")
    rec["state"] = "committed"
    rec["outcome"] = "effect-pending-observe"
    _save(rec)
    print(f"COMMITTED {rid}")


def cmd_ambiguous(rid: str) -> None:
    rec = _load(rid)
    if rec["state"] not in ("reserved", "committed"):
        raise SystemExit(f"cannot mark ambiguous from state={rec['state']}")
    rec["state"] = "ambiguous"
    _save(rec)
    print(f"AMBIGUOUS {rid} — hold one reservation")


def cmd_certify_no_effect(rid: str) -> None:
    rec = _load(rid)
    if rec["state"] not in ("reserved", "committed", "ambiguous"):
        raise SystemExit(f"cannot certify no-effect from state={rec['state']}")
    rec["state"] = "no-effect"
    rec["outcome"] = "certified-no-effect"
    rec["fence"] = True
    _save(rec)
    print(f"NO-EFFECT {rid} fenced")


def cmd_release(rid: str, outcome: str) -> None:
    rec = _load(rid)
    if rec["state"] not in ("committed", "no-effect"):
        raise SystemExit(f"cannot release from state={rec['state']}")
    rec["state"] = "released"
    rec["outcome"] = outcome
    _save(rec)
    print(f"RELEASED {rid} outcome={outcome}")


def cmd_successor(old_id: str, new_id: str, tool: str, args: Any) -> None:
    rec = _load(old_id)
    if rec["state"] != "no-effect" or not rec.get("fence"):
        raise SystemExit("successor denied: need certified no-effect + delivery fence")
    cmd_reserve(new_id, tool, args)
    succ = _load(new_id)
    succ["predecessor"] = old_id
    _save(succ)
    print(f"SUCCESSOR {old_id} -> {new_id}")


def selftest() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        os.environ["AID_GUARD_STORE"] = tmp
        args_ok = {"path": "hot.md", "sha256": "abc"}
        args_mut = {"path": "hot.md", "sha256": "evil"}
        cmd_reserve("a1", "local.hot_md", args_ok)
        try:
            cmd_commit("a1", "local.hot_md", args_mut)
            raise SystemExit("selftest FAIL: mutation was committed")
        except SystemExit as e:
            if "unauthorized" not in str(e):
                raise
        cmd_commit("a1", "local.hot_md", args_ok)
        try:
            cmd_commit("a1", "local.hot_md", args_ok)
            raise SystemExit("selftest FAIL: duplicate commit")
        except SystemExit as e:
            if "cannot commit" not in str(e):
                raise
        cmd_release("a1", "observed-ok")

        cmd_reserve("a2", "local.hot_md", args_ok)
        cmd_ambiguous("a2")
        try:
            cmd_commit("a2", "local.hot_md", args_ok)
            raise SystemExit("selftest FAIL: commit while ambiguous")
        except SystemExit as e:
            if "ambiguous" not in str(e):
                raise
        cmd_certify_no_effect("a2")
        try:
            cmd_successor("a1", "a3", "local.hot_md", args_ok)
            raise SystemExit("selftest FAIL: successor from released-with-effect")
        except SystemExit as e:
            if "successor denied" not in str(e):
                raise
        cmd_successor("a2", "a3", "local.hot_md", args_ok)
        print("selftest PASS")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p_res = sub.add_parser("reserve")
    p_res.add_argument("--id", required=True)
    p_res.add_argument("--tool", required=True)
    p_res.add_argument("--args-json")
    p_res.add_argument("--args-file")
    p_c = sub.add_parser("commit")
    p_c.add_argument("--id", required=True)
    p_c.add_argument("--tool", required=True)
    p_c.add_argument("--args-json")
    p_c.add_argument("--args-file")
    p_a = sub.add_parser("ambiguous")
    p_a.add_argument("--id", required=True)
    p_n = sub.add_parser("certify-no-effect")
    p_n.add_argument("--id", required=True)
    p_r = sub.add_parser("release")
    p_r.add_argument("--id", required=True)
    p_r.add_argument("--outcome", required=True)
    p_s = sub.add_parser("successor")
    p_s.add_argument("--from-id", required=True)
    p_s.add_argument("--id", required=True)
    p_s.add_argument("--tool", required=True)
    p_s.add_argument("--args-json")
    p_s.add_argument("--args-file")
    sub.add_parser("selftest")
    ns = ap.parse_args()
    if ns.cmd == "selftest":
        selftest()
        return
    if ns.cmd == "reserve":
        cmd_reserve(ns.id, ns.tool, _load_args(ns.args_json, ns.args_file))
    elif ns.cmd == "commit":
        cmd_commit(ns.id, ns.tool, _load_args(ns.args_json, ns.args_file))
    elif ns.cmd == "ambiguous":
        cmd_ambiguous(ns.id)
    elif ns.cmd == "certify-no-effect":
        cmd_certify_no_effect(ns.id)
    elif ns.cmd == "release":
        cmd_release(ns.id, ns.outcome)
    elif ns.cmd == "successor":
        cmd_successor(ns.from_id, ns.id, ns.tool, _load_args(ns.args_json, ns.args_file))
    else:
        ap.error("unknown command")


if __name__ == "__main__":
    main()
