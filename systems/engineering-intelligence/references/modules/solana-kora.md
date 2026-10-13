# Module: Solana Foundation Kora

**Source:** https://github.com/solana-foundation/kora  
**Reviewed:** 2026-09-29  
**Pinned review commit:** `f652c29d2d293f045f6d7a0c83589735c095e7c5`  
**Authority:** Solana Foundation  
**Trust tier:** T1_OFFICIAL  
**License:** MIT  
**Integration pattern:** SERVICE_PILOT + PAYMASTER_REFERENCE + TRUSTED_SIGNER_BOUNDARY  
**GwapOS status:** PILOT_DEVNET_ONLY

## What Kora Is

Kora is Solana signing/paymaster infrastructure. It exposes JSON-RPC and a TypeScript SDK and can act as a fee payer/trusted signer so users can transact without holding SOL, including flows where fees are collected in supported SPL tokens.

This directly aligns with the GwapOS product principle that ordinary users should not need to understand or acquire gas tokens merely to use an application.

## Why It Matters to GwapOS

Potential uses:
- sponsor selected GwapOS transactions;
- allow approved fees to be paid in USDC or another explicitly supported token;
- hide SOL fee-payer complexity behind a controlled service;
- improve onboarding for GNS/PPV/Marketplace flows;
- centralize transaction sponsorship policy, rate limits and observability.

Kora is not "free gas." Someone funds the fee-payer account and assumes operational/security risk.

## Current Upstream State at Review

- `main` commit reviewed: `f652c29d2d293f045f6d7a0c83589735c095e7c5`
- Rust workspace reports `2.2.0-beta.8`
- TypeScript SDK reports `0.3.0-beta.4`
- MIT licensed
- supports API key/HMAC/reCAPTCHA authentication controls
- supports multiple signer backends including memory/private key, Turnkey, Privy, Vault and Openfort
- includes rate limiting, usage limits, validation rules, metrics and Redis integration
- includes Token-2022 filtering/policy
- includes fuzz, Rust, TypeScript and integration workflows
- upstream states that `main` may contain audited and unaudited commits

### Audit boundary

Upstream `audits/AUDIT_STATUS.md` (last updated 2026-03-18 at review) records:
- auditor: Runtime Verification
- audited-through commit: `8c592591debd08424a65cc471ce0403578fd5d5d`
- commits after that SHA are considered unaudited until the status file is updated
- stable production releases are intended to come from immutable tagged snapshots

`solana-keychain` now tracks an Accretion audit baseline for its Rust and TypeScript implementations through commit
`475beb7c372e805e081ebcd85d84923460267da6`. Current keychain `main` is newer than that baseline; Python and Go are explicitly outside that audit scope as of review.

Therefore **do not deploy a current signer stack merely because an audit exists**. Verify exact language/backend/version and the unaudited delta.

## GwapOS Decision

```text
REFERENCE       = ADOPT
DEVNET PILOT    = APPROVED PATTERN
PRODUCTION      = NOT APPROVED
MAINNET SIGNER  = EXPLICIT SECURITY/FOUNDER GATE
```

Do not integrate Kora directly into PPV program logic. Treat it as a separately deployed infrastructure/service boundary.

## Recommended Architecture

```text
GwapOS client
     ↓
GwapOS server/API
     ↓ authenticated + policy-scoped request
Kora paymaster service
     ↓
transaction validation
     ↓
approved signer backend
     ↓
Solana RPC
```

The browser must not receive Kora signer secrets.

Prefer a dedicated service boundary rather than embedding a hot fee-payer private key in the Next.js application.

## Devnet Pilot Gate

Before any GwapOS pilot:

1. Pin an exact Kora tag/commit.
2. Check `audits/AUDIT_STATUS.md`.
3. Compare candidate commit against audited-through SHA.
4. Review the unaudited delta.
5. Pin container/crate/SDK artifacts.
6. Use devnet only.
7. Use a dedicated low-balance fee-payer identity.
8. Use HMAC or API-key authentication; never expose privileged credentials to the client.
9. Restrict CORS to GwapOS origins.
10. Set conservative rate and usage limits.
11. Allowlist only required programs.
12. Allowlist only required payment tokens.
13. Disable unnecessary RPC methods.
14. Configure fee-payer policy fail-closed.
15. Add metrics/alerts.
16. Test replay/abuse/drain scenarios.
17. Verify cluster/network separation.
18. Add kill switch/rollback.
19. Document who funds and controls the fee payer.
20. No mainnet promotion without separate approval.

## Policy Design

Start from **deny**, then allow only what a specific GwapOS flow needs.

Bad:
```text
allow every program
allow every token
allow every signer action
public unauthenticated RPC
```

Preferred:
```text
flow = GNS claim
programs = exact required program set
tokens = exact supported payment token set
lamport ceiling = bounded
priority fee = bounded
rate = bounded
usage = bounded
methods = minimum necessary
```

Repeat independently for PPV or Marketplace flows.

## Fee-Payer Safety

Kora has granular policy around actions where the fee payer is also an authority/source/payer.

GwapOS rule: never inherit permissive example values blindly.

For every enabled fee-payer action answer:
- Why must the fee payer perform this action?
- Which GwapOS flow requires it?
- What maximum value can move?
- What account/program/token constraints apply?
- Can a user redirect value?
- Can authority change?
- Can an account be closed?
- Can a delegate be approved?
- Can tokens be minted/burned/frozen?
- What happens under malformed V0/ALT transactions?

Default-deny anything without a concrete product requirement.

## Lighthouse Caveat

Upstream documents that Lighthouse fee-payer assertions apply to delayed-signing flows such as `signTransaction`/`signBundle`, but not `signAndSendTransaction`/`signAndSendBundle`, because modifying the message invalidates existing client signatures.

Do not advertise Lighthouse as universal drain protection.

If GwapOS relies on this protection, choose a transaction flow where the assertion is actually applied and test it.

## V0 / Address Lookup Tables

Upstream agent context warns that V0 transactions must resolve lookup-table addresses before validation/pricing; static keys alone are incomplete.

GwapOS acceptance tests must include V0/ALT cases if sponsored flows support them.

## Signer Policy

Production preference:
1. managed/external signer with explicit policy and audit trail;
2. hardened secret manager/Vault-class backend;
3. local memory/private-key signer only for local/devnet testing unless separately approved.

Never:
- commit a private key;
- expose signer material to Vercel/browser logs;
- reuse PPV program upgrade authority as Kora fee payer;
- reuse treasury/custody authority casually;
- place production signer secrets in example configuration.

Use a dedicated identity with the minimum required balance/authority.

## Authentication and Abuse Controls

Production candidate must include:
- authenticated requests;
- timestamp/replay protections where supported;
- rate limits;
- per-user/app usage limits where applicable;
- bounded lamports/priority fees;
- explicit CORS;
- monitoring;
- alerting on balance/spend anomalies;
- fail-closed behavior when policy/cache/price dependencies are unavailable where appropriate.

A public paymaster endpoint is an economic abuse surface.

## Economic Model

Kora can enable:
- GwapOS-sponsored transactions;
- fee-in-token UX;
- markup/margin models.

Do not enable monetization merely because Kora supports it.

Any fee model must be designed with:
- transparent user quote;
- max fee/slippage;
- token pricing source;
- stale-price handling;
- failed-transaction behavior;
- refunds/retries;
- accounting/reconciliation;
- legal/compliance review where applicable.

## PPV Boundary

Kora may improve PPV UX by sponsoring approved transaction fees, but it must not weaken PPV's current safety model.

Keep separate:
- PPV program authority
- PPV escrow/custody authority
- Kora fee payer
- Kora service authentication
- GwapOS application auth

No mainnet PPV custody behavior is enabled by adopting Kora.

## Production Promotion Gate

Before `PILOT_DEVNET_ONLY → PRODUCTION_CANDIDATE` require:

```text
KORA_VERSION=
KORA_COMMIT=
AUDITED_THROUGH=
UNAUDITED_DELTA_REVIEW=
SIGNER_BACKEND=
FEE_PAYER_PUBKEY=
NETWORK=
AUTH=
CORS=
ALLOWED_PROGRAMS=
ALLOWED_TOKENS=
ENABLED_METHODS=
LAMPORT_LIMIT=
PRIORITY_FEE_LIMIT=
RATE_LIMIT=
USAGE_LIMIT=
METRICS=
DRAIN_TESTS=
V0_ALT_TESTS=
FAIL_CLOSED_TESTS=
ROLLBACK=
SECURITY_REVIEW=
```

Any unknown security-critical field means NOT READY.

## Re-review Triggers

Re-review when:
- new Kora stable/audited release appears;
- audit baseline changes;
- `solana-keychain` audit status changes;
- signer backend changes;
- GwapOS adds sponsored mainnet transactions;
- payment token changes;
- Token-2022 behavior changes;
- transaction v1/V0/ALT behavior changes;
- Kora major/minor upgrade changes policy semantics.

