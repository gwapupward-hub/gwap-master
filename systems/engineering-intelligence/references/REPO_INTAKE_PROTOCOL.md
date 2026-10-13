# Repository Intake Protocol

Use this protocol every time a new GitHub repository is proposed for GwapOS.

## 0. Preserve Current Reality

Before evaluating the external repository:

- identify the GwapOS repository and target branch;
- record current commit SHA;
- inspect installed framework/tool versions;
- inspect repository-local skills and instructions;
- inspect existing implementation that may already solve the same problem.

Do not create a second system merely because the external repository has a cleaner README.

## 1. Identify the Source

Record:

- repository owner/name;
- canonical URL;
- whether it is official, foundation-maintained, vendor-maintained, community-maintained, forked, archived, or experimental;
- latest reviewed tag/commit;
- last meaningful maintenance signal;
- applicable license **before copying code**;
- security/disclosure guidance when present.

## 2. Define the Capability

Answer in one sentence:

> What concrete problem could this repository help GwapOS solve?

Then list:
- the exact feature/workflow worth adopting;
- what is not needed;
- whether the capability belongs in code, CI, documentation, security policy, testing, infrastructure, or another skill.

If the useful idea can be implemented with existing GwapOS dependencies, do not add a new dependency only to mirror upstream.

## 3. Trust Classification

Classify the source:

- `T1_OFFICIAL` — canonical protocol/framework/foundation/vendor source.
- `T2_ESTABLISHED` — mature, widely used project with strong provenance.
- `T3_SPECIALIST` — useful specialized project requiring deeper review.
- `T4_UNVERIFIED` — unknown/early/stale source; reference only until proven.

Trust tier affects how much verification is required. It never eliminates verification.

## 4. Security Review

Before adopting executable code or CI:

- inspect scripts for network downloads and shell execution;
- inspect GitHub Actions for third-party actions and unpinned refs;
- inspect install commands;
- inspect secret usage;
- inspect permissions;
- inspect release artifacts;
- inspect transitive dependencies;
- inspect signer / wallet / RPC assumptions;
- inspect whether commands are read-only or state-changing.

Never run an external repository's setup script with privileged credentials merely because its README says to.

### Skill-package pre-install scan

If the proposed repository contains an Agent Skill, `SKILL.md`, executable skill bundle, MCP skill package, or other package intended to be installed into an agent runtime:

- scan the exact pinned candidate with the approved SkillSpector version before installation;
- require execution-successful and complete analysis;
- apply the GwapOS strict recommendation policy;
- triage/suppress findings explicitly;
- preserve the security report with the intake evidence.

Reference-only repositories do not require a SkillSpector pass unless their skill package will actually be installed or executed.

### Copyleft / license boundary

If an intake repository uses GPL, AGPL, or another strong copyleft license:
- record the license before recommending code reuse;
- default to architecture/reference extraction;
- require explicit license review before copying implementation code into differently licensed GwapOS software;
- prefer independent reimplementation of the learned pattern.

## 5. Compatibility Review

Compare against the current GwapOS stack:

- Solana/Agave version
- Anchor version
- Rust toolchain
- Cargo.lock
- Node version
- package manager
- Next.js/React version
- wallet stack
- RPC providers
- CI runners
- deployment environment
- operating system / architecture assumptions

Prefer adaptation over forced migration.

## 6. Choose the Integration Pattern

Use one:

- `REFERENCE_ONLY` — knowledge/rules, no new runtime dependency.
- `DEV_TOOL` — local developer tool.
- `CI_TOOL` — automated build/test/release tool.
- `LIBRARY` — runtime/build dependency.
- `SERVICE` — external API/service.
- `CODE_ADOPTION` — selected upstream code copied/forked with provenance.
- `WORKFLOW` — process/runbook without dependency.

Record the choice in the source registry.

## 7. Pin and Record

Before production use:
- pin exact release/tag/commit as appropriate;
- pin CI actions to immutable commits where practical;
- commit lockfiles;
- record the source in `SOURCE_REGISTRY.yaml`;
- add/update a module file.

Do not use `latest` as a production provenance record.

## 8. Implement Minimally

- preserve current architecture;
- make the smallest correct change;
- avoid unrelated refactors;
- keep network/cluster explicit;
- keep destructive/state-changing operations behind gates;
- add tests near the new behavior;
- make rollback possible.

## 9. Verify

Minimum evidence depends on integration type.

For code:
- lint/typecheck/build/tests as applicable.

For CI:
- workflow syntax and dry/read-only path where possible;
- actual successful run before relying on it.

For Solana deployment:
- localnet/devnet first;
- exact program ID/cluster;
- transaction/program state evidence;
- reproducible artifact evidence where applicable.

For security tooling:
- prove findings against real repository state;
- do not report tool output as an independent audit.

## 10. Promote or Reject

Use one status:

- `ADOPTED`
- `PILOT`
- `REFERENCE_ONLY`
- `REJECTED`
- `SUPERSEDED`

Record why.

## Module Template

Every new module should contain:

```text
# <Capability Name>

Source:
Reviewed:
Pinned source:
Trust tier:
Integration pattern:

## Problem it solves
## GwapOS use
## What we adopt
## What we do not adopt
## Required workflow
## Security rules
## Compatibility notes
## Verification
## Failure / rollback
## Upstream caveats
## Re-review triggers
```
