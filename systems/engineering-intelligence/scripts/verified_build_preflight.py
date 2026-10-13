#!/usr/bin/env python3
"""
Read-only preflight for the GwapOS Solana Verified Builds module.

This script does NOT deploy, sign, modify upgrade authority, or submit
verification transactions. It checks local release prerequisites and can
optionally compute hashes when the necessary CLI is available.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path


def run(cmd: list[str], cwd: Path) -> tuple[int, str]:
    p = subprocess.run(
        cmd,
        cwd=str(cwd),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        check=False,
    )
    return p.returncode, p.stdout.strip()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--workspace", default=".")
    ap.add_argument("--program-lib", required=True)
    ap.add_argument("--program-id")
    ap.add_argument("--network-url")
    ap.add_argument("--artifact")
    ap.add_argument("--require-clean-git", action="store_true")
    args = ap.parse_args()

    workspace = Path(args.workspace).resolve()
    artifact = (
        Path(args.artifact).resolve()
        if args.artifact
        else workspace / "target" / "deploy" / f"{args.program_lib}.so"
    )

    result = {
        "workspace": str(workspace),
        "program_lib": args.program_lib,
        "program_id": args.program_id,
        "network_url": args.network_url,
        "checks": {},
        "status": "READY_FOR_BUILD",
    }

    required_files = ["Cargo.toml", "Cargo.lock"]
    for name in required_files:
        result["checks"][name] = (workspace / name).is_file()

    for exe in ["git", "cargo", "docker", "solana-verify"]:
        result["checks"][f"tool_{exe}"] = bool(shutil.which(exe))

    if shutil.which("git"):
        code, out = run(["git", "rev-parse", "HEAD"], workspace)
        if code == 0:
            result["repo_sha"] = out
        code, out = run(["git", "status", "--porcelain"], workspace)
        if code == 0:
            clean = not bool(out.strip())
            result["checks"]["git_clean"] = clean
            if args.require_clean_git and not clean:
                result["status"] = "NOT_READY"

    if shutil.which("solana-verify"):
        code, out = run(["solana-verify", "--version"], workspace)
        if code == 0:
            result["solana_verify_version"] = out

    if artifact.is_file():
        result["artifact"] = str(artifact)
        result["artifact_sha256"] = sha256_file(artifact)
        if shutil.which("solana-verify"):
            code, out = run(
                ["solana-verify", "get-executable-hash", str(artifact)],
                workspace,
            )
            result["checks"]["executable_hash_command"] = (code == 0)
            if code == 0:
                result["executable_hash_output"] = out

    if (
        args.program_id
        and args.network_url
        and shutil.which("solana-verify")
    ):
        code, out = run(
            [
                "solana-verify",
                "get-program-hash",
                "-u",
                args.network_url,
                args.program_id,
            ],
            workspace,
        )
        result["checks"]["program_hash_command"] = (code == 0)
        if code == 0:
            result["program_hash_output"] = out

    hard_requirements = [
        result["checks"].get("Cargo.toml", False),
        result["checks"].get("Cargo.lock", False),
        result["checks"].get("tool_cargo", False),
        result["checks"].get("tool_docker", False),
        result["checks"].get("tool_solana-verify", False),
    ]

    if not all(hard_requirements):
        result["status"] = "BLOCKED"

    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "READY_FOR_BUILD" else 1


if __name__ == "__main__":
    sys.exit(main())
