# Module: Surfpool

**Source:** https://github.com/solana-foundation/surfpool  
**Reviewed:** 2026-09-29  
**Pinned review commit:** `2ce9b9e019517881911dafca5871afc13f45a192`  
**Observed stable release:** `v1.6.0`  
**Trust:** T1_OFFICIAL_DEVELOPER_TOOLING  
**License:** Apache-2.0  
**Status:** PILOT_APPROVED_LOCAL_CI

## Why it ranks #2

Surfpool can materially improve PPV/GNS/GwapOS integration testing by providing a local Solana environment that can mirror/fork relevant mainnet state, manipulate test state, replay/debug transactions, and define reproducible scenarios without touching production.

It is a stronger fit than adding more unit-test examples because GwapOS already has substantial local-validator testing; the missing value is richer realistic scenario testing.

## Adopted use

Pilot Surfpool as an **additional integration/scenario layer**, not an immediate replacement for all existing `solana-test-validator` CI.

Initial targets:
1. PPV Core transaction scenarios;
2. PPV Commerce scenarios;
3. wallet/network mismatch regression;
4. V0/ALT and transaction-version compatibility;
5. Token/Token-2022 state cases where relevant;
6. RPC/account-state edge cases;
7. feature-gated behavior when needed.

## Safe rollout

```text
existing unit/Rust/TS tests
        ↓
existing local-validator acceptance
        ↓
Surfpool scenario suite (pilot)
        ↓
devnet acceptance
        ↓
verifiable build / release gates
```

Do not delete proven CI until Surfpool demonstrates equivalent or better fidelity for that test class.

## Reproducibility

Prefer:
- pinned Surfpool release/artifact;
- checksum verification where release digest is available;
- scenario/config committed to repo;
- deterministic account/program fixtures;
- CI-friendly noninteractive mode;
- recorded upstream/fork source;
- explicit cluster assumptions.

Do not use `curl | bash` in CI.

## Mainnet-state rule

Forking or reading mainnet state is **read/reference input**, not permission to send transactions to mainnet.

Surfpool simulations never authorize:
- mainnet deployment;
- custody activation;
- authority changes;
- treasury movement.

## Cheatcode safety

Cheatcodes are test-only state manipulation. A passing test that depends on impossible production state must not be presented as production proof.

Label tests that use synthetic state and maintain at least one realistic acceptance path for critical flows.

## MCP boundary

Surfpool exposes MCP tooling. Treat MCP commands as tools with side effects:
- local network start/stop is allowed when requested by test workflow;
- file/config changes require normal repo review;
- never let MCP-selected network silently become mainnet;
- no state-changing external cluster action without explicit approval.

## Promotion gate

Pilot succeeds when:
- PPV/GNS scenario setup is simpler or more realistic;
- CI is reproducible;
- failures are diagnosable;
- runtime is acceptable;
- no network-boundary regressions occur.

Only then consider replacing specific local-validator jobs.
