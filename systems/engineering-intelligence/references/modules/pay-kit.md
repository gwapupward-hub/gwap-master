# Module: Pay Kit
Source: https://github.com/solana-foundation/pay-kit
Reviewed: 2026-09-29
Pinned commit: `c294f8903f18efc746584e3cc2961d6033b8365c`
Observed TS release: `pay-kit-v0.7.0`
Trust: T1_OFFICIAL_PAYMENT_TOOLING
License: MIT
Status: PILOT_REFERENCE

Multi-language building blocks for MPP/x402 stablecoin paywalls, clients, servers, splits, fee accounting, gasless patterns, sessions and subscriptions.

## GwapOS use
This is the implementation layer beneath the `pay` concepts already adopted.

Best fit:
- future paid GwapOS APIs;
- Marketplace platform-fee flows;
- agentic service payments;
- controlled sandbox experiments.

## Guardrails
- protocol spec outranks SDK behavior;
- pin exact language package/version;
- no subscriptions/stateful sessions in first pilot;
- deterministic price/challenge;
- strict replay/idempotency;
- allowlisted assets/networks;
- reconciliation separate from chain confirmation;
- no autonomous mainnet spending without explicit authorization.
