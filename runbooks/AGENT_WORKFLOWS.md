# Agent Workflows

**Status:** PROPOSED (see `registries/DECISION_REGISTRY.yaml`, `GWAP-AGENT-001`)
**Used by:** `.claude/agents/` (gwap-lead, gwap-solana, gwap-backend, gwap-frontend, gwap-devops, gwap-reviewer)

One routing table, one workflow per task type. Use the lightest workflow that still meets its gates.

Gates come from `MASTER.md`, the runbooks, and `systems/engineering-intelligence/SKILL.md`. If this file conflicts with any of them, they win.

---

## 1. Route the task

The lead runs this first. Check top to bottom. The first match wins. State the workflow and the reason in one line.

| Order | Workflow | Match when |
|---|---|---|
| 0 | **HALT: Authority** | Mainnet deploy, upgrade-authority change, custody activation, multisig execution, automated spending, or production credential changes |
| 1 | **D: Decide** | Architecture, product ownership, payment rail choice, digital-asset model, adopting a repo, tool, SDK, or standard |
| 2 | **A: Audit** | Review or assessment with no requested change |
| 3 | **O: On-chain** | Changes to Anchor/Rust programs, IDL, or client transaction construction |
| 4 | **S: Ship** | Release, deploy, CI, environment variables, domains |
| 5 | **X: Fix** | Reproducible bug confined to one layer |
| 6 | **U: UI** | UI-only change in one app |
| 7 | **V: Service** | Worker, bot, API route, MCP server, or indexer change |
| 8 | **F: Feature** | Anything spanning two or more layers |

If a task matches HALT and another row, HALT wins. Prepare the evidence and stop.

If the owning product is not listed in `registries/PRODUCT_TRUTH.yaml`, route to **D** before any code.

---

## 2. Gates every workflow shares

- **Repo reality first.** Record the current SHA, check for a dirty tree, and inspect the target files and CI. Read `CLAUDE.md`, `MASTER.md`, and `PRODUCT_TRUTH.yaml`.
- **Ownership.** Name the owning subsystem from `PRODUCT_TRUTH.yaml` in every brief.
- **Smallest correct change.** No unrelated refactors. No framework or toolchain upgrades unless the task requires them.
- **Tests before claims.** Use precise claim language:
  - `tested locally`
  - `verified on devnet`
  - `hash matched`
  - `remote verification submitted`
  - `remote verification confirmed`
  
  Do not collapse these into "verified."
- **Final report.** Use the STATUS block from `systems/engineering-intelligence/SKILL.md`. An unknown or skipped gate means NOT_READY.
- **Secrets.** Never print, commit, or log keys, seed phrases, signer bytes, tokens, or webhook secrets.

---

## 3. Workflows

### D: Decide
**Goal:** a decision record. No code.

1. State the user outcome and the owning system (`PRODUCT_TRUTH.yaml`).
2. Inspect current reality: the repo and any deployed system.
3. Find the highest-authority sources. Pin versions and commits.
4. Compare alternatives. Do not force a stack change because it is fashionable.
5. Define the security, authority, and value boundary.
6. Write the record to `registries/DECISION_REGISTRY.yaml` with status `PROPOSED`. Include the fields required by `schemas/decision-record.schema.json`.
7. Stop. The founder's approval promotes the status.

**Repo or tool intake** also requires `runbooks/NEW_REPO_INTAKE.md` and `systems/engineering-intelligence/references/REPO_INTAKE_PROTOCOL.md`. Review the license before copying any code. Any executable agent skill must pass the SkillSpector gate (`systems/engineering-intelligence/scripts/skillspector_gate.py`: SAFE, complete, successful) before it is installed.

**Agents:** gwap-lead. Specialists may give read-only feasibility notes.
**Gate:** the record is complete, sources are pinned, and the approval status is accurate.

### A: Audit
**Goal:** findings backed by evidence. No edits.

1. gwap-reviewer runs its checklist against the named scope and runs the existing checks.
2. A domain specialist is consulted only if the reviewer needs an answer. Read-only.
3. Report findings by severity, each with file and line and evidence.

**Gate:** every finding has evidence, and `git status` is clean when the audit ends.

### O: On-chain
**Goal:** a program change proven on localnet and devnet.

1. The lead writes the contract: instructions, accounts, PDAs and seeds, events, IDL impact, and target cluster (localnet or devnet).
2. gwap-solana implements on `feat/<slug>-onchain`. Tests: unit tests (Bankrun or LiteSVM), `anchor test` on localnet, and devnet acceptance.
3. Regenerate the IDL. Confirm the IDL and generated clients match. Only then may gwap-backend or gwap-frontend update their clients.
4. gwap-reviewer checks signers, owners, PDAs, mints, checked math, and upgrade safety of account layouts.
5. For a deployable release candidate, go to **S**. Mainnet is HALT.

**Gate:** localnet tests pass, devnet acceptance is recorded, the IDL is consistent, and the reviewer returns PASS.

### S: Ship
**Goal:** an exact, reproducible artifact deployed with recorded evidence.

**Web or app release:** record the SHA. Run lint, typecheck, build, and tests. Map env vars by name (never values). Record preview evidence, the deploy target, and the rollback target. Production deploy needs approval.

**Solana program release:** follow the Solana Release Integrity section of `systems/engineering-intelligence/SKILL.md` in order.

1. Freeze the target: branch, SHA, cluster, program ID, library name, mount path, and upgrade authority.
2. Check prerequisites: root `Cargo.lock`, Docker, Cargo, and tests already passing.
3. Run `solana-verify build`, then `get-executable-hash`. Record the SHA-256.
4. Preserve the exact `.so`. Do not recompile between build and deploy.
5. Deploy that artifact. Read the on-chain hash with `get-program-hash`.
6. Compare the hashes. **Mismatch means BLOCK.**
7. Run `verify-from-repo`. Use the `remote submit-job` path for mainnet only, with the correct authority or approved multisig process.
8. Record the evidence.

Pin the `solana-verify` version. Never use an unbounded latest install. Remote verification is mainnet-only per upstream docs. Do not use the legacy `--remote` flag.

**Agents:** gwap-devops owns the release. gwap-reviewer checks config diffs for secret exposure and for preview builds pointing at mainnet.
**Gate:** the STATUS block is complete. For Solana, it includes both hashes and `HASH_MATCH=yes`.

### X: Fix
**Goal:** the smallest diff that makes the failing case pass.

1. Reproduce the bug. Record the failing test or exact steps.
2. Write a regression test that fails before the fix.
3. One specialist owns the change. No refactors.
4. gwap-reviewer returns PASS.

A production hotfix is still **S**, and deploying it needs approval.

### U: UI
**Goal:** a UI change that matches the design system.

1. gwap-frontend reads the existing tokens and components. Reuse before creating.
2. Keep Next.js App Router. Do not add Ionic or a second router. Preserve GwapSpot design tokens (see the Cross-Platform UI policy in `systems/engineering-intelligence/SKILL.md`).
3. Handle loading, empty, and error states. Check at phone width.
4. For wallet or transaction UI, gwap-solana reviews transaction construction and exactly what the user is shown to sign.
5. gwap-reviewer returns PASS with screenshots or Playwright output.

### V: Service
**Goal:** a backend change with a fixed, documented contract.

1. The lead writes the contract: request and response shapes, auth, idempotency key, rate limit, and failure codes.
2. gwap-backend implements. Tests: unit tests, Miniflare or local D1 for Workers, and recorded fixtures for external APIs.
3. Webhooks verify signatures. Retried writes are idempotent. Secrets live in platform secret stores only.
4. Payment paths keep **Stripe**, **MPP/x402 + Pay Kit**, **Kora**, and **PPV** separate (`GWAP-PAY-001`). Do not merge them into one subsystem.
5. AI or agent features follow `systems/engineering-intelligence/references/AI_AGENT_RELEASE_GATE.md`: outcome contract, eval set, baseline vs treatment, per-case regressions, tool boundaries, and redacted observability. Untrusted content grants no authority. State-changing tools need approval.
6. gwap-reviewer returns PASS. Production deploy or webhook registration goes to **S**, with approval.

### F: Feature
**Goal:** a cross-layer change merged as one reviewed unit.

1. The lead writes the plan: outcome, owning subsystems, interface contracts, acceptance criteria, and risks. If the change is material, route to **D** first.
2. Specialists work in parallel. Each uses its own branch, `feat/<slug>-<layer>`, and touches disjoint files only.
3. Every task goes through gwap-reviewer. A BLOCK goes back to its owner.
4. The lead integrates on `feat/<slug>`, reruns every gate, and opens a draft PR. Never merge.
5. Release goes through **S**.

**Gate:** every acceptance criterion has evidence, the reviewer returns PASS on each task, and the integrated checks pass.

---

## 4. Output

Use the STATUS block from `systems/engineering-intelligence/SKILL.md`:

```text
STATUS, SCOPE, REPO_SHA, UPSTREAM_SOURCE, NETWORK, PROGRAM_ID, PROGRAM_LIB,
ARTIFACT, ARTIFACT_SHA256, EXECUTABLE_HASH, ONCHAIN_HASH, HASH_MATCH,
PUBLIC_VERIFICATION, TESTS, SECURITY_GATES, BLOCKERS, NEXT
```

Reviewer verdict mapping:

- **PASS** becomes READY, once every gate is known.
- **BLOCK** becomes NOT_READY.
- An unauthorized side effect becomes BLOCKED.

---

## 5. Always escalate to the founder

- Mainnet deploy or mainnet verification upload
- Upgrade-authority or multisig changes
- Custody activation or automated mainnet spending
- DNS or domain changes
- Deleting data
- Product ownership changes
- Production credential or webhook changes

For each one, give a recommendation and the trade-off. Do not hand over a neutral list of options.
