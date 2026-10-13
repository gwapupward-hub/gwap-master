# Module: NVIDIA SkillSpector

**Source:** https://github.com/NVIDIA/SkillSpector  
**Reviewed:** 2026-09-29  
**Pinned stable release:** `v2.11.2`  
**Pinned commit:** `69dcdfb74487d361ba4c811d088cfdea2ff3a9dc`  
**Pinned wheel:** `skillspector-2.11.2-py3-none-any.whl`  
**Wheel SHA-256:** `9e0eb261d63e7ae92f94177a44aeb8fef5e0ceeaa4d09135780baf94cbc420ec`  
**Latest observed release:** `v2.12.0` — upstream release notes say `candidate; publication pending`  
**Trust tier:** T1_OFFICIAL  
**License:** Apache-2.0  
**Integration pattern:** CI_TOOL + SECURITY_REFERENCE  
**GwapOS status:** ADOPTED

## Problem It Solves

Agent skills can contain instructions, scripts, references, nested artifacts, dependency redirects, MCP configuration, and tool behavior that deserve security review before installation or release.

SkillSpector provides a specialized scanner for AI agent skills with deterministic/static analysis plus optional semantic LLM analysis. Its reported coverage includes prompt injection, data exfiltration, privilege escalation, supply-chain behavior, excessive agency, dangerous code, taint flow, memory poisoning, tool misuse, MCP least privilege/tool poisoning, and related skill-specific risks.

For GwapOS, its job is:

```text
skill source/package
      ↓
pinned SkillSpector scan
      ↓
machine-readable report
      ↓
GwapOS strict policy parser
      ↓
SAFE + complete + successful ?
      ↓
yes → continue release evaluation
no  → review / block
```

## Version Policy

Do not automatically track `latest`.

At review time:
- `v2.12.0` existed but its own release notes described it as a candidate pending publication.
- GwapOS therefore pins the previous explicitly released stable version: `v2.11.2`.

Upgrade only after:
1. upstream marks the target version released/stable;
2. changelog/security behavior is reviewed;
3. report schema/gate compatibility is tested;
4. the GwapOS baseline is re-triaged where fingerprints are version-bound.

## Required GwapOS Gate

Routine CI uses **static analysis first**:

```bash
skillspector scan ./path/to/skill \
  --no-llm \
  --format json \
  --output skillspector-report.json
```

Then run:

```bash
python scripts/skillspector_gate.py skillspector-report.json
```

The GwapOS gate requires all of the following:

```text
execution_successful == true
analysis_completeness.is_complete == true
risk_assessment.recommendation == "SAFE"
```

Anything else is not release-ready.

### Why the GwapOS gate is stricter

In stable v2.11.2, the normal CLI exit contract allows both `SAFE` and `CAUTION` to return exit code 0 when the risk score is at most 50.

GwapOS does **not** treat that exit code as an installation/release verdict.

Policy:
- `SAFE` + complete + successful → pass security scanner gate.
- `CAUTION` → review required; do not release until resolved or explicitly baselined and rescanned.
- `DO_NOT_INSTALL` → block.
- incomplete analysis → block.
- unsuccessful execution / malformed report → block.
- scanner unavailable → block release unless an explicitly approved exception is recorded.

## Static vs Semantic Analysis

### Required: static scan

Use `--no-llm` in ordinary PR/release CI because it is:
- deterministic enough for gating;
- independent of model credentials;
- cheaper;
- easier to reproduce;
- less likely to send skill content to external inference providers.

### Optional: semantic scan

Use the LLM-backed pass when:
- releasing a high-risk skill;
- adopting a third-party skill with meaningful executable/tool authority;
- static findings require semantic context;
- a security reviewer explicitly requests it.

Semantic scanning is defense-in-depth. It does not replace static analysis or manual review.

Before sending private/proprietary skill content to a hosted model provider:
- verify the provider is approved;
- verify data-handling requirements;
- do not pass secrets;
- prefer local/approved inference when required.

## Baseline / Suppression Policy

SkillSpector supports accepted findings through a baseline.

GwapOS rules:

1. Never generate a baseline and merge it without human triage.
2. Prefer exact fingerprints for individual accepted findings.
3. Broad glob/rule suppressions require:
   - narrow scope;
   - written reason;
   - security review.
4. Baseline changes are security-sensitive code review changes.
5. Scanner-version upgrades require re-review because exact fingerprints are version-bound.
6. Run with `--show-suppressed` periodically and remove stale suppressions.
7. A baseline exists to document accepted risk/false positives, not to make the dashboard green.

## Skill Intake Rule

Before installing or adopting a third-party repository as an executable Agent Skill:

1. pin/ref the source;
2. inspect license/provenance;
3. run SkillSpector against the exact candidate package;
4. require successful and complete analysis;
5. triage findings;
6. compare skill-declared permissions/behavior with actual requested authority;
7. only then install or merge.

If the repository is merely being read as documentation/reference, SkillSpector is optional unless it contains skill packages we plan to execute/install.

## Release Rule for GwapOS Skills

Every releasable GwapOS skill bundle should produce:

- JSON security report;
- optional SARIF report;
- scanner version;
- scanned source/package SHA;
- baseline SHA when used;
- strict gate result.

Security scanning is one layer. The skill must still pass the GwapOS AI/Agent/Skill Release Gate for routing, behavior, script correctness, safety/authority, and portability.

## CI Installation Integrity

Prefer installation from the pinned release artifact.

Verify the wheel digest before installation:

```text
skillspector-2.11.2-py3-none-any.whl
sha256:9e0eb261d63e7ae92f94177a44aeb8fef5e0ceeaa4d09135780baf94cbc420ec
```

Do not use an unbounded Git install from `main` in the release gate.

## SARIF

SkillSpector can emit SARIF. GwapOS may:
- retain SARIF as a workflow artifact;
- upload to GitHub Code Scanning when repository permissions/policy allow.

Do not grant `security-events: write` to a workflow merely to make the scan run. The scanner gate can operate with read-only repository permissions and upload artifacts separately.

## Fail-Closed Resource Bounds

SkillSpector documents bounded scanning and explicit completeness reporting.

GwapOS must inspect:

```text
execution_successful
analysis_completeness.is_complete
analysis_completeness.status
analysis_completeness.ledger_exceptions
risk_assessment.recommendation
```

A low risk score or zero findings is **not** sufficient when analysis is incomplete.

## What SkillSpector Does Not Prove

A passing scan does not prove:
- a skill is useful;
- routing is correct;
- the skill improves task outcomes;
- every vulnerability class is absent;
- its scripts are logically correct;
- external services are trustworthy;
- runtime sandbox/permission controls are sufficient;
- the skill is portable across hosts.

That is why SkillSpector augments, rather than replaces, the GwapOS six-layer skill release gate.

## Re-review Triggers

Re-review when:
- NVIDIA publishes a new stable release;
- the JSON/completeness schema changes;
- risk-score semantics change;
- new scanner categories materially affect GwapOS;
- a baseline begins accumulating broad suppressions;
- the skill runtime/packaging format changes;
- GwapOS starts publishing skills externally.
