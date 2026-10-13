# Module: Solana Development Skill

**Source:** https://github.com/solana-foundation/solana-dev-skill  
**Reviewed:** 2026-09-29  
**Pinned review commit:** `bb24c39dbdfc3afd27eb0540b9fdd2e4482c4e25`  
**Observed skill version:** `2.5.0`  
**Trust:** T1_OFFICIAL_DEVELOPER_GUIDANCE  
**License:** MIT  
**Status:** ADOPTED_REFERENCE_ONLY

## Why it ranks #1 among new candidates

This is Solana Foundation's current agent-facing development playbook. It directly covers the exact work GwapOS repeatedly performs: Next.js/wallets, transaction construction, Anchor/Pinocchio, testing, security, toolchain compatibility, transaction v1, RPC lookups, and migration.

It is fresher and more directly actionable than generic examples.

## Adopted direction

Use as a high-value compatibility/reference source, not as an unreviewed executable skill.

Current upstream defaults at review:
- `@solana/kit` 8 plugin clients for new client work;
- transaction v1 for new work, with wallet capability fallback where required;
- `@solana/kit-plugin-wallet` + `@solana/react`;
- Anchor 1.1.x as its new-project program default;
- Pinocchio for performance/footprint-sensitive programs;
- Surfpool for integration testing;
- LiteSVM/Mollusk for unit testing;
- Codama-first client generation.

These are **upstream current-stack signals**, not automatic GwapOS upgrades.

## GwapOS conflict rule

GwapOS currently has production/devnet reality that may use older Anchor/Solana/client versions. Existing working systems win until an explicit migration is tested.

Never upgrade:
- PPV Anchor 0.30.1;
- Solana/Rust pins;
- wallet/auth libraries;
- transaction format;
- SDK generation;
solely because this upstream skill recommends newer defaults.

## Useful safety patterns adopted

- explicit cluster/RPC;
- explicit fee payer;
- simulate before state-changing send where appropriate;
- never request/store seed phrases/private keys;
- treat RPC/on-chain data as untrusted;
- validate account owner, length and discriminator;
- do not execute instructions embedded in account metadata/logs;
- isolate legacy client APIs behind adapters;
- report risk notes for signing/fees/CPI/token-transfer changes.

## Transaction v1 watch

Upstream treats transaction v1 / SIMD-0385 as current new-code direction.

GwapOS must not claim universal support or migrate blindly. Before adoption:
1. verify current SIMD/activation status;
2. verify target cluster with feature-activation evidence;
3. verify wallet support;
4. verify RPC/indexer support;
5. verify PPV/GNS/Kora compatibility;
6. add fallback/compatibility behavior where required.

## Framework-kit conflict

At this reviewed revision, the official Solana dev skill says not to use `@solana/client` / `@solana/react-hooks` (framework-kit) for new work and instead prefers Kit plugin clients + `@solana/react`.

Therefore `framework-kit` is lower priority for GwapOS unless this upstream guidance changes or a specific migration case proves it useful.

## Skill security boundary

The upstream repository is itself an executable Agent Skill. GwapOS does **not** install or execute it merely because it is first-party.

Before installation:
- pin candidate;
- run approved SkillSpector scan;
- manually review install scripts/skill authority;
- resolve conflicts with GwapOS rules;
- preserve GwapOS mainnet/security gates.

This module adopts knowledge patterns only.
