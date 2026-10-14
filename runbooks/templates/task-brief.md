# Task brief: <slug>

```text
ROUTE=<HALT|D|A|O|S|X|U|V|F>
REASON=<one line: why this row of AGENT_WORKFLOWS.md section 1>
OWNER=<subsystem name from registries/PRODUCT_TRUTH.yaml>
BRANCH=feat/<slug>-<layer>
GATES=<the gates from the workflow that apply>
```

**GOAL:** one sentence on the user outcome.

**OUT OF SCOPE:** files, systems, and behaviors this task must not touch.

**FILES IN SCOPE:** explicit paths. Parallel tasks must not overlap.

**INTERFACE CONTRACT:** request and response shapes, account layouts, IDL, events, env var names. Name each one and whether it changes.

**ACCEPTANCE CRITERIA:**
- [ ] each criterion as a checkable statement

**PROOF COMMANDS:** the exact commands whose output shows the criteria are met.

**RISKS AND HALT CHECKS:** anything that touches mainnet, authority, custody, spending, or production credentials. If one applies, stop and escalate.

**REPORT BACK:** the status template in `runbooks/templates/status-report.md`.
