# Module: Program Examples
Source: https://github.com/solana-foundation/program-examples
Reviewed: 2026-09-29
Pinned commit: `de090195e4de698e150572c4f886c333323a64a5`
Trust: T1_OFFICIAL_EXAMPLE_REFERENCE
License: MIT
Status: ADOPTED_REFERENCE_ONLY

Current examples cover Anchor, Pinocchio and native Rust, including PDAs, CPI, account validation, closing/realloc, token flows, escrow and Token-2022.

## GwapOS rule
Examples teach patterns; they are not audited production code.

Before borrowing a pattern:
- compare with installed Anchor/Solana versions;
- verify account ownership/signers/writability;
- threat-model authority and token movement;
- add repo-native tests;
- prefer smallest independent implementation rather than wholesale copy.

Particularly relevant to PPV: account validation, CPI, PDA/rent, token transfer, escrow comparison and Token-2022 behavior.
