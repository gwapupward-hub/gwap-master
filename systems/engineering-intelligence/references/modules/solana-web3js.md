# Module: solana-web3.js
Source: https://github.com/solana-foundation/solana-web3.js
Reviewed: 2026-09-29
Pinned main commit: `4b6bd6efd464e40420217cd77c2a58a10eefddce`
Trust: T1_OFFICIAL_CLIENT_SDK
License: MIT
Status: MIGRATION_REFERENCE

Main now hosts v3+ development. Legacy v1.x is on `maintenance/v1.x` and receives critical fixes only.

## GwapOS decision
- Do not introduce new v1 dependencies.
- Contain existing v1 usage behind adapters.
- New work should follow current Kit-first guidance unless compatibility requires web3.js.
- Treat v3 as a migration compatibility target where appropriate, not an automatic whole-app rewrite.

Migration requires wallet, serialization, signing, transaction-version and SDK compatibility tests.
