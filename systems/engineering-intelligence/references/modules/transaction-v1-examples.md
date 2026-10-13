# Module: Transaction v1 Examples
Source: https://github.com/solana-foundation/transaction-v1-examples
Reviewed: 2026-09-29
Pinned commit: `bb7e4f6dfe1fb6cb2a0385f05b7f10048d268216`
Trust: T1_OFFICIAL_COMPATIBILITY_REFERENCE
License: MIT
Status: ADOPTED_REFERENCE_ONLY

Focused examples for SIMD-0385 transaction v1 across Rust, TypeScript, Python and Go.

High-value compatibility facts:
- v1 uses `TransactionConfig` instead of ComputeBudget instructions;
- priority fee is total lamports rather than micro-lamports per CU;
- ALT is v0-only;
- readers/indexers must raise `maxSupportedTransactionVersion` to 1;
- stale gRPC protobufs may silently discard the v1 config field;
- wallet support must be checked;
- local validators may activate features differently from public clusters.

GwapOS must verify target-cluster activation before relying on v1 and add reader/indexer compatibility tests before migration.
