# Module: Solana Keychain
Source: https://github.com/solana-foundation/solana-keychain
Reviewed: 2026-09-29
Pinned commit: `8ea75de5c47fb3d22d704ab175cbe10483db2ff2`
Observed prerelease: `v2.0.0-beta.1`
Trust: T1_OFFICIAL_SECURITY_SENSITIVE
License: MIT
Status: PILOT_REFERENCE

Unified signer abstraction across Rust, TypeScript, Python and Go with backends including Vault, Privy, Turnkey, AWS/GCP KMS, Fireblocks, Openfort and others.

## Security/audit status
Accretion audit baseline:
`475beb7c372e805e081ebcd85d84923460267da6`

Audit scope covered Rust and TypeScript through that commit.
Current main is newer and therefore contains an unaudited delta.
Python and Go landed after the audited baseline and are explicitly unaudited as of review.

## Critical model
Keychain validates/adapts the signing hop; it does **not** decide whether a transaction is safe.

GwapOS must separate:
transaction policy -> transaction construction -> review/simulation -> signer adapter -> broadcast.

Never let signer abstraction become authorization abstraction.

Production selection requires:
- exact language/backend;
- exact version/commit;
- audited baseline comparison;
- provider policy review;
- redirect/network controls;
- transaction/message-version support;
- live integration tests;
- revocation/rotation procedure.
