# Module: Solana Improvement Documents (SIMDs)

**Source:** https://github.com/solana-foundation/solana-improvement-documents  
**Reviewed:** 2026-09-29  
**Pinned review commit:** `4b643ca8746742183a469681765e694b385bb315`  
**Authority:** Solana Foundation  
**Trust tier:** T1_OFFICIAL_PROTOCOL_DESIGN  
**Repository package license:** ISC  
**Integration pattern:** PROTOCOL_DESIGN_REFERENCE + CHANGE_INTELLIGENCE + COMPATIBILITY_WATCH  
**GwapOS status:** ADOPTED

## Purpose

SIMDs describe proposed and accepted changes to the Solana protocol, interfaces, networking, and Solana processes. SIMD-0001 governs the process.

This source is more authoritative for the *design and lifecycle of proposed protocol changes* than marketing/site content. It is not, by itself, proof that a feature is active on a specific cluster.

## SIMD Types

Standard:
- Core
- Networking
- Interfaces

Meta:
- process/governance/environment changes

Advisory:
- clarifications, errata, deprecation notices and similar non-consensus-breaking notices

## Lifecycle — Critical GwapOS Rule

```text
Idea
 ↓
Draft
 ↓
Review
 ↓
Accepted
 ↓
Implemented
 ↓
Activated
```

Other states include Living, Stagnant and Withdrawn.

Per SIMD-0001, **Activated** means the proposal has been implemented, tested, and finally activated on mainnet-beta.

Therefore:

| SIMD status | What GwapOS may conclude |
|---|---|
| Idea | discussion only |
| Draft | proposal under development |
| Review | proposal under review |
| Accepted | design accepted; NOT proof of implementation/activation |
| Implemented | implementation completed; NOT proof of mainnet activation |
| Activated | SIMD process says activated on mainnet-beta |
| Living | continuously maintained process/spec document |
| Stagnant | inactive/stale |
| Withdrawn | proposal withdrawn |

## Evidence Rule: Design Status != Cluster Reality

Never infer cluster activation from:
- merged proposal;
- Accepted status;
- implementation PR;
- release notes alone;
- social posts;
- website copy.

For a GwapOS production decision, corroborate relevant SIMD claims with the strongest available runtime evidence, such as:
- official Agave/validator implementation and feature tracking;
- official cluster feature activation data;
- RPC/feature-set evidence;
- official release/cluster documentation.

For high-impact claims, record both:

```text
SIMD_STATUS=
IMPLEMENTATION_STATUS=
DEVNET_STATUS=
TESTNET_STATUS=
MAINNET_BETA_STATUS=
EVIDENCE_TIME=
```

If activation cannot be verified, say so.

## Protocol Change Impact Review

When a relevant SIMD appears or changes, classify impact on GwapOS:

```text
NONE
WATCH
TEST_REQUIRED
MIGRATION_REQUIRED
SECURITY_REVIEW
RELEASE_BLOCKER
```

Review at minimum:
- transaction format/limits;
- account locking;
- compute/runtime behavior;
- CPI/instruction behavior;
- syscalls;
- sBPF;
- fees;
- RPC/interface changes;
- validator/network behavior relevant to clients;
- feature gates;
- deprecations;
- backwards compatibility.

Map effects to:
- PPV programs/SDK;
- GNS;
- GwapScore data sources where applicable;
- wallet/auth/transaction construction;
- RPC/indexing;
- docs/examples;
- CI/local validator;
- release toolchain.

## SIMD Template as Engineering Review Discipline

The official template requires useful review dimensions:
- Summary
- Motivation
- Dependencies
- Detailed Design
- Edge Cases
- Validator Components Affected
- Alternatives
- Impact
- Security Considerations
- Drawbacks
- Backwards Compatibility
- Conformance

GwapOS should reuse these *review dimensions* for major protocol-sensitive architecture decisions without copying unnecessary ceremony.

## Conformance

SIMDs may define conformance evidence for client implementations.

When a SIMD affects GwapOS behavior:
1. read its conformance section;
2. identify official implementation/test vectors/fixtures if present;
3. add a compatible GwapOS test where materially relevant;
4. preserve cluster/version assumptions;
5. do not mark support complete until the required behavior is demonstrated.

## Monitoring Rule

SIMDs are living engineering intelligence. A pinned commit records what was reviewed, but protocol-change monitoring should check newer upstream state before making current production decisions.

Watch especially:
- status transitions;
- amendments;
- supersedes/superseded-by;
- extends/dependencies;
- feature identifiers;
- activation guidance;
- security/backwards-compatibility changes.

## Source Hierarchy Update

For Solana protocol-change questions:

1. current observed cluster/runtime evidence;
2. official implementation/feature tracking for the relevant release;
3. applicable SIMD at current/pinned revision;
4. official Solana developer documentation;
5. official production website content;
6. third-party analysis.

A SIMD is authoritative design/process evidence, but current cluster state wins for claims about what is live.

## Social / News Claim Guardrail

Before GwapSpot publishes claims such as:
- "Solana now supports X";
- "X is live";
- "mainnet upgraded to X";
- "the limit is now X";

require a cluster-state check.

Allowed wording when not activated:
- "proposed in SIMD-…"
- "under review"
- "accepted but not yet verified active"
- "implemented, with mainnet activation not yet verified"

Do not convert roadmap/proposal language into present-tense production claims.

## Hard Rules

1. Proposal existence is not activation.
2. Accepted is not activated.
3. Implemented is not activated.
4. Mainnet claims require current cluster evidence.
5. Check superseding/extending SIMDs before relying on an older design.
6. Security and backwards-compatibility sections are mandatory reading for affected GwapOS components.
7. Do not change production behavior solely because a SIMD is proposed or accepted.
8. Re-check upstream before time-sensitive release decisions.

