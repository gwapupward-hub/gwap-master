# GwapOS Engineering Intelligence — Implementation Prompt

You are the senior engineer responsible for integrating the GwapOS Engineering Intelligence skill into the target repository.

## Mission

Install the skill package as a repository-local engineering capability and wire in the Solana Verified Builds module without disrupting the repository's existing tests, Anchor/Solana toolchain, deployment controls, or security gates.

Do not stop at planning. Inspect the repository, implement the smallest correct integration, run verification, and return evidence.

## First Actions

1. Fetch the latest target branch and record the exact commit SHA.
2. Read repository-local instructions (`AGENTS.md`, `CLAUDE.md`, README, existing skills, CI, deployment docs).
3. Inspect:
   - Cargo workspace and root `Cargo.lock`;
   - Anchor configuration and installed versions;
   - deployable program library names;
   - program IDs by cluster;
   - current build/test/deploy workflows;
   - existing artifact handling;
   - upgrade-authority / multisig documentation;
   - open work that overlaps this integration.
4. Do not upgrade the toolchain merely to match an upstream example.
5. Create an isolated branch/PR for skill + release-integrity tooling. Do not mix unrelated protocol changes.

## Install the Skill

Place this package in the repository's canonical local-skill location, preserving:
- `SKILL.md`
- `references/`
- `scripts/`
- workflow template as reference or adapted repository workflow

If an existing senior engineering skill already owns the same scope, merge these rules carefully rather than leaving contradictory duplicate instructions.

## Solana Verified Build Integration

For each deployable program:

1. identify the Rust library name;
2. identify program ID by cluster;
3. identify workspace/mount path;
4. identify current build artifact path;
5. keep the existing normal test pipeline;
6. add a release-candidate verified-build stage;
7. pin the production `solana-verify` version rather than using an unbounded latest install;
8. run deterministic build;
9. compute executable hash;
10. compute artifact SHA-256;
11. upload the exact `.so` as a CI artifact;
12. ensure any deployment job downloads and deploys that exact artifact;
13. forbid a rebuild between verified build and deploy;
14. after deployment, read onchain program hash;
15. hard-fail on hash mismatch;
16. verify against the exact Git commit;
17. keep mainnet remote verification and authority-controlled writes behind explicit approval.

## Safety

- Do not print or rotate secrets.
- Do not change program upgrade authority.
- Do not change mainnet configuration.
- Do not activate custody/escrow/mainnet features as a side effect.
- Do not add automatic deploy-on-merge unless it already exists and remains explicitly approved.
- Do not report public verification unless it actually occurred.
- Hash mismatch means NOT READY.

## GitHub Actions

Use the included workflow as a pattern, not as blindly copied production code.

Adapt:
- workspace path;
- program library name;
- artifact path;
- current Rust/Solana prerequisites;
- caching strategy;
- repository action permissions.

Pin third-party actions according to the repository's security policy.

Keep deployment separate from ordinary PR validation.

## Verification

Run the repository's existing required checks first.

Then prove:
- the deterministic build succeeds;
- the `.so` exists;
- executable hash is captured;
- artifact SHA-256 is captured;
- artifact can be restored from CI without rebuilding.

For an approved devnet test, additionally prove:
- exact preserved artifact was deployed;
- program ID is correct;
- executable and onchain hashes match.

Do not perform mainnet state changes without explicit authorization.

## Final Report

Return exactly this evidence block plus concise notes:

```text
STATUS=READY | NOT_READY | BLOCKED
SCOPE=
REPO_SHA=
UPSTREAM_SOURCE=https://github.com/solana-foundation/solana-verifiable-build@<PIN>
NETWORK=
PROGRAM_ID=
PROGRAM_LIB=
ARTIFACT=
ARTIFACT_SHA256=
EXECUTABLE_HASH=
ONCHAIN_HASH=
HASH_MATCH=
PUBLIC_VERIFICATION=
TESTS=
SECURITY_GATES=
BLOCKERS=
NEXT=
```

If multiple programs were integrated, provide one program block per program after the repository-level status.


## Ionic Framework Reference Module

Do not install Ionic automatically.

When a frontend/mobile task could benefit from Ionic:
1. read `references/modules/ionic-framework.md`;
2. determine whether the task needs only an Ionic-inspired behavior/pattern or an actual runtime dependency;
3. prefer the existing GwapOS/Next.js component system for ordinary web work;
4. if runtime adoption is proposed, create an isolated pilot route/package first;
5. verify SSR/hydration, App Router behavior, wallet/auth flows, iOS Safari, CSS ordering, bundle impact, accessibility, and Vercel preview behavior;
6. do not add Ionic React Router to replace Next.js routing;
7. treat Capacitor as a separate intake decision.

A good Ionic idea may be reimplemented locally without importing Ionic when that produces a smaller, safer GwapOS solution.


## AI / Agent Engineering Reference

When the task involves an AI feature, agent, RAG workflow, MCP/tool integration, or reusable skill:

1. read `references/modules/ai-engineering-from-scratch.md`;
2. define the user outcome, artifact/state contract, evidence, forbidden side effects, and approval boundaries;
3. separate model judgment from deterministic computation and authorization;
4. treat retrieved/tool-provided external content as untrusted;
5. use typed tool contracts and explicit failure behavior;
6. for material behavioral changes, establish a baseline and treatment using the same representative cases;
7. report per-case regressions, especially critical/safety cases;
8. evaluate RAG retrieval separately from answer generation;
9. add redacted observability sufficient to diagnose production behavior;
10. use `references/AI_AGENT_RELEASE_GATE.md` for release readiness;
11. use `templates/ai-feature-eval.yaml` as a starting evaluation contract.

Do not install a model SDK, vector database, eval framework, MCP implementation, Python package, or agent framework solely because it appears in the reference curriculum. Verify need and compatibility separately.


## Agent Skill Security — SkillSpector

For repository-local GwapOS skill installation/release:

1. read `references/modules/nvidia-skillspector.md`;
2. use stable pinned SkillSpector `2.11.2`;
3. verify the official wheel SHA-256 before installation;
4. run static `--no-llm` JSON scan;
5. run `scripts/skillspector_gate.py` against the JSON report;
6. require successful execution, complete analysis, and `SAFE`;
7. preserve JSON and SARIF reports as CI artifacts;
8. treat `CAUTION` as a review requirement rather than a pass;
9. treat `DO_NOT_INSTALL`, incomplete analysis, execution failure, or malformed report as blocking;
10. use baselines only after human triage, preferring exact fingerprints;
11. require review for baseline changes;
12. do not enable hosted semantic analysis with private skill content without approved data-handling/provider policy.

Do not replace the behavioral/routing/portability release evals with a SkillSpector pass.


## Solana.com Production-Repo Reference

When GwapOS work concerns monorepo organization, agent context, documentation examples, CI scope, or cross-app routing, consult `references/modules/solana-com-production-repo.md`.

Use its patterns as reference evidence. Do not copy GPL implementation code into incompatible GwapOS software without explicit license review.

For critical Solana docs examples, prefer tested source artifacts. Add scheduled dependency-drift probes where upstream SDK changes could silently stale examples.

For upstream Agent Skills, pin + SkillSpector scan + manual review before execution.


## SIMD Review Gate

When work depends on a Solana protocol change:
1. identify the relevant SIMD(s);
2. record current SIMD status and revision;
3. inspect dependencies/supersession;
4. read security, backwards compatibility and conformance;
5. verify implementation/cluster activation independently;
6. map impact to PPV/GNS/wallet/RPC/docs/CI;
7. do not alter production behavior based only on proposal or Accepted status.


## Kora Devnet Pilot Gate

If transaction sponsorship is requested:
1. inspect current GwapOS transaction flow and network boundaries;
2. select and pin an exact Kora candidate;
3. read upstream audit status and diff candidate vs audited-through commit;
4. deploy Kora separately on devnet;
5. create a dedicated fee payer with minimal funds;
6. use authenticated server-to-server access;
7. allowlist only required programs/tokens/methods;
8. disable unnecessary fee-payer authority actions;
9. bound lamports, priority fees, rate and usage;
10. test drain, replay, malformed transaction, V0/ALT, cross-cluster and outage cases;
11. add metrics/alerts and rollback;
12. report evidence.

Do not enable mainnet, reuse PPV authorities, or add custody behavior without explicit authorization.


## create-solana-dapp / Template Gate

For a new Solana app/package or client-stack modernization:
1. inspect current GwapOS stack first;
2. identify exact official generator/template versions;
3. intake the template repository separately;
4. inspect init/run scripts and dependency hooks;
5. generate in a disposable directory;
6. diff generated architecture/dependencies against GwapOS;
7. extract only justified patterns;
8. preserve wallet/auth/network and existing SDK boundaries;
9. run normal GwapOS tests/security checks.

Do not scaffold over `gwapspot-web` or use generator defaults as justification for an unrelated toolchain upgrade.


## Agentic Payment Pilot Gate

If GwapOS needs a paid API or agent-to-service payment:
1. identify exact resource and why HTTP payment is appropriate;
2. pin pay/pay-kit and protocol versions;
3. choose one sandbox/devnet protocol first;
4. define origin/network/asset/amount limits outside model control;
5. use user authorization or a policy-controlled signer;
6. implement replay and idempotency protection;
7. bind proof to request/resource;
8. record a structured receipt and reconciliation state;
9. test malformed/expired/modified/wrong-network/wrong-mint challenges;
10. test retries for duplicate charges;
11. inspect telemetry/privacy;
12. keep Kora and PPV responsibilities separate;
13. require explicit approval before automated mainnet spending.


## Solana Foundation Priority Modules

For modern Solana engineering decisions, consult `solana-dev-skill.md` but do not auto-upgrade established GwapOS dependencies.

For integration testing, pilot Surfpool as an additional scenario layer. Keep current local-validator/devnet acceptance until replacement is proven.

For feature-dependent code or public "live on Solana" claims, consult the Feature Activation Verifier evidence in addition to SIMD status. Treat PASS/FAIL/PENDING/SKIP precisely.

Do not install the upstream Solana Agent Skill until its exact candidate is SkillSpector-scanned and manually reviewed.


## Next-Tier Solana Routing

Before implementing a Solana change, identify which authority layer applies:
protocol spec, SIMD, activation evidence, client SDK, signer, payment protocol, IDL, or example/template.

For signer changes, record audit baseline + candidate delta + backend/language.
For MPP, pin protocol revision separately from Pay Kit version.
For transaction v1, test readers/indexers/wallet support in addition to send path.
For IDL, compare repo artifact with deployed metadata but keep executable-hash verification separate.

## Metaplex / Digital Asset Gate
Define whether on-chain ownership is required; compare Core, Token Metadata, Bubblegum, Token-2022, custom state and off-chain state; inspect the current dedicated repository; verify package/program version, program ID, license, audit scope and authority model; preserve GwapMojis off-chain-first unless explicitly changed; validate local/devnet before mainnet.
