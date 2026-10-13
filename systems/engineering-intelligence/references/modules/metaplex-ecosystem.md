# Module: Metaplex Ecosystem and Digital Asset Routing
Source: https://github.com/metaplex-foundation/metaplex
Reviewed: 2026-09-30
Pinned directory commit: `4eefb4eae49c83b4c5a732b27e1d369d7ff8b951`
Trust: T2_ESTABLISHED_ECOSYSTEM_MAINTAINER
Directory license: Apache-2.0
Status: ADOPTED_REFERENCE_ONLY

## Freshness finding
The supplied repository is a project directory, not the current canonical implementation monorepo. Its default branch is `master`, it routes to separate programs/SDKs/tools, and its latest observed push was in 2024. Use it for ecosystem relationships, not current implementation authority.

## Current routing observed during intake
- MPL Core: https://github.com/metaplex-foundation/mpl-core — reviewed commit `e72d63e4118a0a95ac9b40221e81b19d49e1e102`; digital assets/collections with plugins; program ID observed in its README: `CoREENxT6tW1HoK8ypY1SxRMZTcVPm7R94rH4PZNhX7d`; README reports Mad Shield audit completed 2024-05-03. Status: PILOT_REFERENCE.
- MPL Token Metadata: https://github.com/metaplex-foundation/mpl-token-metadata — metadata for fungible/non-fungible SPL tokens. Status: ADOPTED_REFERENCE.
- MPL Bubblegum: https://github.com/metaplex-foundation/mpl-bubblegum — reviewed commit `ad7d32b477625190704eb204741667b5df15221d`; compressed NFTs/assets. Status: PILOT_REFERENCE.

## GWAP decision gate
Before selecting Metaplex, determine whether the object needs on-chain ownership, transferability, collection semantics, royalties/creator metadata, plugins/custom behavior, massive-scale compression, or marketplace interoperability. Compare MPL Core, Token Metadata, Bubblegum, Token-2022, custom program state, and off-chain records.

Do not start from “NFT” as the requirement.

## GwapMojis
Preserve the existing architecture: off-chain gifts by default, optional mint later.
`Gift Studio object -> off-chain ownership/gifting -> explicit mint request -> selected Solana asset primitive`

For a future optional mint, evaluate MPL Core before assuming legacy Token Metadata. Evaluate Bubblegum when scale/storage economics justify compression.

## Security / release
- Pin exact program/client versions and verify canonical program IDs.
- Audit scope must match the exact revision; an older audit is not blanket approval of current main.
- Test update authority, delegates/plugins, transfers, burns, collection verification, royalties, and relevant freeze controls.
- Treat metadata URIs/JSON as untrusted content.
- Protect collection/update authorities; use appropriate managed/hardware/multisig controls.
- Local/devnet before mainnet; preserve wallet/cluster/transaction-version compatibility.
- Metaplex repositories use differing licenses. Review the exact target repo/file/package license before copying or adopting code.

## Authority
For Metaplex implementation: current dedicated repo/release -> current Metaplex docs -> deployed program/state -> current client docs -> this directory -> old tutorials.
Underlying Solana runtime/spec/activation evidence still outranks Metaplex documentation.
