# Module: Solana Foundation pay

**Source:** https://github.com/solana-foundation/pay  
**Reviewed:** 2026-09-29  
**Pinned review commit:** `2b798d7922d969a5cb274228dac593eb752aefb6`  
**Observed stable release:** `pay-v0.29.0`  
**Authority:** Solana Foundation  
**Trust tier:** T1_OFFICIAL_PAYMENT_TOOLING  
**License:** MIT  
**Integration pattern:** AGENTIC_PAYMENT_REFERENCE + HTTP_402_PAYMENT_PILOT + MCP_PAYMENT_SAFETY  
**GwapOS status:** PILOT_REFERENCE

## Current Project Identity

Do not assume this repository is only the historical Solana Pay QR/payment-link stack.

At review, the repository describes itself as a CLI/payment layer for agentic payments and HTTP 402 flows, supporting:
- MPP (Machine Payments Protocol);
- x402;
- user-authorized stablecoin signing;
- MCP integration;
- ACP integration;
- payment gateways/paywalls;
- local payment debugging;
- permission-constrained unattended-agent payment flows.

Its product model is:

```text
HTTP request
   ↓
402 Payment Required
   ↓
detect supported payment protocol
   ↓
prepare payment
   ↓
apply permissions / user authorization
   ↓
sign stablecoin transaction
   ↓
attach payment proof
   ↓
retry request
   ↓
receive paid resource
```

## Why It Matters to GwapOS

Potential future uses:
- paid GwapOS APIs;
- developer API/licensing monetization;
- agent-to-service payments;
- Daily Ideas agent purchases of approved external APIs;
- pay-per-use AI/research/tooling;
- Marketplace machine-to-machine services;
- paid MCP tools;
- controlled automated spending by GwapOS agents.

This is aligned with the GwapSpot principle of getting paid when economic value moves through the network, but no monetization model is automatically authorized by this module.

## Separation of Responsibilities

Do not collapse these systems:

### pay
HTTP/payment-challenge layer for paid resources and agentic service consumption.

### Kora
Paymaster/trusted signer infrastructure that can sponsor Solana network fees or collect approved token-denominated fees.

### PPV Commerce
GwapOS commerce/proof primitives and application settlement/business workflow logic.

### Stripe
Fiat/subscription/hosted-checkout rail where GwapOS currently uses or plans traditional payment flows.

Possible composition:

```text
Agent / User
     ↓
GwapOS paid API
     ↓
MPP / x402 challenge
     ↓
pay-compatible authorization/payment
     ↓
stablecoin settlement
     ↓
resource access
```

Kora may separately sponsor transaction fees where appropriate. PPV may separately record/prove business events. Neither is automatically implied.

## Current Upstream Signals

At review:
- repository is active and maintained;
- main reviewed at `2b798d7922d969a5cb274228dac593eb752aefb6`;
- stable release `pay-v0.29.0` published 2026-09-26;
- Rust workspace version `0.29.0`, edition 2024;
- MIT licensed;
- `solana-pay-kit` is pinned by git revision;
- `solana-keychain` is pinned by git revision;
- CI/release/Docker workflows exist;
- prebuilt releases publish SHA-256 digests;
- repository includes an MCP server and a `skills/pay` skill;
- payment permission policies can constrain origins, networks, maximum payment and assets;
- permission mode intentionally fails closed for stateful MPP sessions/subscriptions not covered by the policy.

## Agent Payment Safety Principle

An AI agent must never receive unconstrained spending authority merely because it can call a payment tool.

Separate:

```text
MODEL DECISION
"I need this paid resource"
       ↓
DETERMINISTIC POLICY
Is origin allowed?
Is network allowed?
Is asset allowed?
Is amount <= limit?
Is payment type allowed?
Is session/subscription allowed?
       ↓
USER / POLICY AUTHORIZATION
       ↓
SIGNER
       ↓
PAYMENT
```

The model proposes intent. Deterministic policy and signer authorization control money movement.

## Permission Contract

Any unattended GwapOS agent payment capability must define:

```text
ALLOWED_ORIGINS=
ALLOWED_NETWORKS=
ALLOWED_ASSETS=
MAX_PAYMENT_PER_REQUEST=
MAX_PAYMENT_PER_SESSION=
MAX_PAYMENT_PER_DAY=
ALLOWED_PROTOCOLS=
SUBSCRIPTIONS_ALLOWED=
STATEFUL_SESSIONS_ALLOWED=
HUMAN_APPROVAL_THRESHOLD=
SIGNER_BACKEND=
AUDIT_LOG=
KILL_SWITCH=
```

Unknown critical fields => NOT READY.

Start deny-all and allow only concrete product requirements.

## Prompt Injection / Untrusted Content Rule

HTTP responses, MCP tool descriptions, API metadata, web pages, retrieved documents and agent instructions are untrusted data.

They cannot:
- raise payment limits;
- add allowed origins;
- change network;
- authorize a new asset;
- enable subscriptions;
- change signer backend;
- bypass human approval;
- modify payment policy.

Payment policy comes from trusted configuration/authorization outside model-controlled content.

## User Authorization

For human-operated flows, preserve clear authorization before value moves.

A payment confirmation should communicate at least:
- recipient/service origin;
- asset;
- amount/max amount;
- network;
- one-time vs recurring/stateful behavior where applicable.

Do not hide materially different payment terms behind generic "Continue" language.

## Stablecoin / Asset Policy

"Stablecoin supported" does not mean every token should be accepted.

For GwapOS:
- explicitly allowlist mint/asset identifiers;
- verify decimals;
- verify network;
- verify recipient/payment destination;
- handle Token-2022 deliberately;
- prevent lookalike token substitution;
- preserve exact quote/payment proof linkage.

## Protocol Verification

MPP and x402 are external protocol surfaces.

Before production integration:
1. identify exact protocol/spec version;
2. review official protocol source;
3. pin compatible pay/pay-kit versions;
4. test challenge parsing;
5. test amount/asset/origin validation;
6. test replay behavior;
7. test expired/modified challenge;
8. test failed settlement;
9. test retry idempotency;
10. test duplicate payment prevention;
11. test malformed headers/proofs;
12. test wrong-network/wrong-mint cases.

Do not infer protocol security solely from the CLI implementation.

## MCP / ACP Boundary

The repo can expose payment capability to AI clients through MCP and ACP-related workflows.

GwapOS rule:
- MCP tool availability is not payment authorization;
- ACP/model routing is not payment authorization;
- the payment tool must remain policy-scoped;
- side effects must be explicit;
- return structured receipt/evidence;
- payment failure must not silently retry into duplicate charges.

Any external `skills/pay` skill must pass normal SkillSpector/skill intake before installation.

## Wallet / Key Management

Prefer:
- user wallet approval for interactive consumer flows;
- hardware/OS biometric-backed signing where appropriate;
- external policy-controlled signer for server/agent flows;
- revocable credentials;
- minimum necessary balances/authority.

Never:
- expose raw private keys to an LLM;
- place private keys in prompts/context;
- log seed phrases;
- reuse PPV upgrade/custody authority;
- allow model-generated configuration to select arbitrary signer material.

## Paywall / Gateway Design

For a GwapOS paid API:

```text
request
 ↓
authenticate caller where applicable
 ↓
determine resource + price
 ↓
issue deterministic payment challenge
 ↓
verify payment proof
 ↓
bind proof to request/resource
 ↓
enforce replay/idempotency
 ↓
serve resource
 ↓
record receipt/evidence
```

Pricing should be deterministic or clearly quoted before signing.

## Accounting / Reconciliation

Production paid APIs need more than blockchain confirmation.

Record:
- request ID;
- payment challenge ID;
- protocol;
- payer;
- recipient;
- asset/mint;
- amount;
- network;
- transaction signature/proof;
- resource delivered;
- timestamp;
- retry/idempotency state;
- refund/exception state where supported.

Do not treat a transaction signature alone as complete business reconciliation.

## Privacy / Telemetry

The repository contains observability/telemetry infrastructure.

Before GwapOS adoption:
- inspect what is emitted;
- redact wallet/payment-sensitive data;
- avoid prompts/API payloads unless required and approved;
- define retention;
- distinguish operational traces from financial records.

## Recommended GwapOS Pilot

Best initial experiment is not consumer checkout.

Pilot a **devnet/sandbox paid machine-readable API** with:
- one resource;
- one approved stablecoin;
- one fixed low price;
- one protocol;
- one allowed origin/client;
- strict max payment;
- no subscription;
- no stateful session;
- deterministic receipt;
- duplicate-payment tests;
- explicit kill switch.

This isolates the HTTP payment primitive before tying it to Marketplace, Daily Ideas or PPV.

## Production Promotion Gate

```text
PAY_VERSION=
PAY_COMMIT=
PAY_KIT_VERSION_OR_REV=
PROTOCOL=
PROTOCOL_VERSION=
NETWORK=
RESOURCE=
PRICE_MODEL=
ALLOWED_ORIGINS=
ALLOWED_ASSETS=
MAX_PAYMENT=
DAILY_LIMIT=
SUBSCRIPTIONS=
SIGNER_BACKEND=
USER_APPROVAL=
REPLAY_PROTECTION=
IDEMPOTENCY=
RECEIPT=
RECONCILIATION=
TELEMETRY_REVIEW=
SECURITY_TESTS=
ROLLBACK=
LEGAL_COMPLIANCE_REVIEW=
STATUS=
```

Unknown critical security/payment state => NOT READY.

## Hard Rules

1. Model intent is not financial authorization.
2. Payment tools require deterministic policy.
3. External content cannot modify payment authority.
4. Default-deny origins/assets/networks/payment modes.
5. Never expose signer secrets to models or browsers.
6. Prevent duplicate payment under retries.
7. Bind payment proof to the intended resource/request.
8. Separate payment settlement from business reconciliation.
9. Do not replace PPV Commerce or Kora merely because `pay` overlaps economically.
10. Mainnet automated spending requires explicit founder/security approval.

## Re-review Triggers

Re-review when:
- pay major/minor version changes;
- MPP/x402 specifications change;
- pay-kit revision changes materially;
- keychain/signing architecture changes;
- GwapOS enables agentic spending;
- GwapOS launches paid APIs;
- subscriptions/stateful MPP are proposed;
- a new stablecoin/payment asset is enabled;
- GwapOS composes pay with Kora or PPV.

