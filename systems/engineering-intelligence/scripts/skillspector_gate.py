#!/usr/bin/env python3
"""
Strict GwapOS policy gate for NVIDIA SkillSpector JSON reports.

Pass only when:
  - execution_successful is true
  - analysis_completeness.is_complete is true
  - risk_assessment.recommendation is SAFE

This script is deliberately stricter than SkillSpector's default CLI exit
contract in v2.11.2, which can return 0 for both SAFE and CAUTION.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def fail(msg: str, code: int = 1) -> int:
    print(f"GWAPOS_SKILLSPECTOR_GATE=BLOCKED")
    print(f"REASON={msg}")
    return code


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("report", help="SkillSpector JSON report")
    args = ap.parse_args()

    path = Path(args.report)
    if not path.is_file():
        return fail("report_missing", 2)

    try:
        report = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return fail(f"report_unparseable:{type(exc).__name__}", 2)

    if not isinstance(report, dict):
        return fail("report_not_object", 2)

    if report.get("execution_successful") is not True:
        return fail("execution_unsuccessful")

    completeness = report.get("analysis_completeness")
    if not isinstance(completeness, dict):
        return fail("analysis_completeness_missing")

    if completeness.get("is_complete") is not True:
        status = completeness.get("status", "unknown")
        exceptions = completeness.get("ledger_exceptions")
        count = len(exceptions) if isinstance(exceptions, list) else "unknown"
        return fail(f"analysis_incomplete:status={status}:exceptions={count}")

    risk = report.get("risk_assessment")
    if not isinstance(risk, dict):
        return fail("risk_assessment_missing")

    recommendation = risk.get("recommendation")
    score = risk.get("score")
    severity = risk.get("severity")

    if recommendation != "SAFE":
        return fail(
            f"recommendation={recommendation}:severity={severity}:score={score}"
        )

    metadata = report.get("metadata")
    scanner_version = None
    if isinstance(metadata, dict):
        scanner_version = metadata.get("skillspector_version")

    print("GWAPOS_SKILLSPECTOR_GATE=PASS")
    print(f"RECOMMENDATION={recommendation}")
    print(f"SEVERITY={severity}")
    print(f"RISK_SCORE={score}")
    print(f"SCANNER_VERSION={scanner_version or 'unknown'}")
    print("ANALYSIS_COMPLETE=true")
    print("EXECUTION_SUCCESSFUL=true")
    return 0


if __name__ == "__main__":
    sys.exit(main())
