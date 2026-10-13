# Module: Solana Feature Activation Verifier

**Source:** https://github.com/solana-foundation/feature-activation-verifier  
**Reviewed:** 2026-09-29  
**Pinned review commit:** `0b356c740991a5903cf24a643b461cb1c6dce2cf`  
**Trust:** T1_OFFICIAL_PROTOCOL_VERIFICATION_TOOLING  
**Status:** ADOPTED_REFERENCE + PILOT_TOOL

## Why it ranks #3

This closes the exact evidence gap identified by the SIMD module: proposal/implementation status is not enough to prove a feature is usable on devnet/testnet/mainnet.

The verifier maintains feature-centric activation metadata and behavioral tests, including E2E checks that can require both feature gates and deployed program hashes.

## Evidence model

For protocol-sensitive GwapOS work:

```text
SIMD design/status
      +
feature-gate activation metadata
      +
behavioral/E2E verification
      +
target-cluster evidence
      =
usable production evidence
```

Do not reduce this to a single boolean.

## Outcomes

Use upstream semantics:
- PASS — requirements met and behavior verified;
- FAIL — requirements met but behavior is broken;
- PENDING — prerequisites not met;
- SKIP — no test implementation.

GwapOS rule:
- PASS can support a compatibility claim for the tested behavior/network;
- FAIL blocks relying on that behavior;
- PENDING means do not assume availability;
- SKIP is unknown, not success.

## High-value uses

Before GwapOS adopts a feature-dependent behavior:
- transaction v1 / larger transaction behavior;
- new syscalls;
- Token-2022/confidential-transfer behavior;
- runtime/CPI changes;
- feature-gated transaction/account behavior;

record target network and verifier evidence.

## Current limitation

At review the repository warns that building requires a local Surfpool clone until Surfpool crates are regularly published again.

Therefore do not make this an unconditional CI dependency yet.

Pilot it as:
1. pinned reference manifest;
2. manual/release-candidate verification;
3. optional CI job when dependency setup is reproducible.

## Mainnet safety

The CLI supports testnet/mainnet and requires a keypair for those runs. GwapOS must not supply a privileged production keypair automatically.

For mainnet:
- prefer read-only/behavior checks that cannot move value;
- use dedicated minimal-authority test identities if signing is required;
- never use PPV upgrade/custody/treasury authority;
- require explicit authorization for state-changing tests.

## Integration with SIMD intelligence

Every time-sensitive protocol claim should ideally capture:

```text
SIMD_STATUS=
FEATURE_GATE=
TARGET_NETWORK=
ACTIVATION_METADATA=
BEHAVIOR_TEST=
OUTCOME=
VERIFIED_AT=
SOURCE_COMMIT=
```

This evidence can feed engineering decisions and GwapSpot news/content claim checks.
