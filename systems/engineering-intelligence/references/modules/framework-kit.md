# Module: Framework Kit
Source: https://github.com/solana-foundation/framework-kit
Reviewed: 2026-09-29
Pinned commit: `5021c445e25199b7d773a732d1c11498487696e5`
Trust: T1_OFFICIAL_DEVELOPER_TOOLING
Status: REFERENCE_ONLY

Framework Kit provides `@solana/client` and `@solana/react-hooks` for wallet orchestration, transactions and reactive Solana data.

## GwapOS decision
Keep as reference-only. The newer official `solana-dev-skill` explicitly prefers Kit plugin clients plus `@solana/react` for new work and says not to use Framework Kit packages for new work.

Use Framework Kit only when:
- comparing legacy/current architectural choices;
- maintaining code that already depends on it;
- a measured migration experiment shows specific value.

Do not introduce it into `gwapspot-web` as a parallel wallet/state framework without a deliberate migration plan.
