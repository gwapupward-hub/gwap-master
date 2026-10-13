# Module: MPP Specifications
Source: https://github.com/solana-foundation/mpp-specs
Reviewed: 2026-09-29
Pinned commit: `a938bfdd443a9683aa0fcbeae487ed4ffadfe4be`
Trust: T1_PROTOCOL_REFERENCE_FORK
Status: ADOPTED_PROTOCOL_REFERENCE

Solana Foundation fork of the Machine Payments Protocol specifications. The upstream protocol is co-maintained by Tempo and Stripe and uses HTTP 402 plus `WWW-Authenticate: Payment`.

## Authority rule
For MPP semantics, use the actual current MPP/IETF specification as authority. This Foundation fork is a convenient reviewed mirror/reference, not permission to invent Solana-specific semantics.

Key concepts adopted:
- payment-method-agnostic core;
- explicit intents vs concrete methods;
- replay protection as first-class;
- extensions separated from stable core;
- network/currency agnostic design.

Before production, pin exact draft/spec version and test against it.
