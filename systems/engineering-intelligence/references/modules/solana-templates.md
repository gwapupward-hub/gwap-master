# Module: Solana Templates
Source: https://github.com/solana-foundation/templates
Reviewed: 2026-09-29
Pinned commit: `9e4bbfc948dfb0086bb1d4ff9cc5feec14dc29c6`
Trust: T1_OFFICIAL_DEVELOPER_TOOLING
License: MIT
Status: ADOPTED_REFERENCE_ONLY

Official templates for `create-solana-dapp`, including Kit, legacy Web3.js, mobile and community templates.

## GwapOS use
- reference modern project layout;
- inspect official Kit/Next.js examples;
- bootstrap only genuinely new isolated apps/packages.

## Supply-chain gate
Every template is still executable input:
1. pin exact template commit/path;
2. inspect package/init scripts;
3. generate outside the production repo;
4. diff output;
5. security/dependency review;
6. promote selected patterns only.

Community templates remain lower trust than Foundation-maintained templates.
