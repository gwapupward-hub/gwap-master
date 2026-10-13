# Solana Foundation Repository Relevance Audit — GwapOS

Reviewed: 2026-09-29

Purpose: triage the public `solana-foundation` organization by **GwapOS implementation value**, not stars. Ranking considers direct fit with PPV/GNS/GwapOS, current maintenance, authority, security/release value, overlap with modules already adopted, and implementation risk.

This is an organization-level triage. Tier A candidates received deeper source inspection. Lower tiers are prioritization, not security approval.

## Tier 0 — Already incorporated / core intelligence
These were already present before this organization-wide audit:
- solana-verifiable-build
- solana-improvement-documents
- kora
- create-solana-dapp
- pay
- solana-com

## Tier A — Highest-value new implementation/reference candidates
1. **solana-dev-skill** — current Solana agent-development guidance; modern Kit/transaction/testing/security/toolchain routing. **Added in v1.9.0.**
2. **surfpool** — realistic local/forked-state integration and scenario testing. **Added in v1.9.0.**
3. **feature-activation-verifier** — target-network activation + behavioral evidence; closes SIMD-to-runtime gap. **Added in v1.9.0.**
4. framework-kit — wallet/transaction/reactive data framework; lower priority because current official solana-dev-skill prefers Kit plugin clients for new work.
5. templates — official app templates; useful for isolated new apps, not established gwapspot-web.
6. program-examples — useful program/reference implementations and testing patterns.
7. solana-keychain — signer/key-management architecture; especially relevant to Kora/pay, but security/audit status requires dedicated intake.
8. pay-kit — underlying MPP/x402 payment SDK; relevant when moving from pay reference to actual paid API implementation.
9. mpp-specs — protocol-level MPP evidence; required before production MPP integration.
10. solana-program-library — foundational program/token reference; large/legacy surface requires scoped intake rather than blanket adoption.
11. solana-web3.js — migration/compatibility intelligence for legacy clients.
12. solana-mcp — current Solana docs/expert MCP surface; useful but external MCP authority requires separate security review.
13. transaction-v1-examples — focused compatibility examples for v1 transactions.
14. specs — protocol/specification material; inspect when a concrete dependency points to it.
15. idl-spec — useful for IDL/codegen compatibility decisions.
16. idl — IDL tooling/reference; relevant to Anchor/Codama client generation.

## Tier B — Strongly useful when the matching GwapOS feature is active
- solana-attestation-service — attestations/identity proofs; potentially relevant to GNS/GwapScore.
- solana-record-service — record primitives; potentially relevant to naming/profile data.
- commerce-kit — commerce/payment composition.
- escrow — escrow reference patterns; PPV Escrow requires security-specific comparison before any reuse.
- subscriptions — recurring payment patterns.
- payment-channels — payment-channel research/implementation.
- x402 — x402 ecosystem/protocol implementation; relevant to pay integration.
- x402-sdk — x402 SDK-specific integration.
- mpp — MPP implementation/reference.
- pay-skills — paid API catalog/agent skills; only when agentic purchasing launches.
- pay-vercel-template — tiny deployment template; useful only for a pay pilot.
- solana-payments-app — payment application reference.
- token-acl — token access-control patterns.
- token-acl-gate — token ACL gateway patterns.
- tokens — token tooling/data relevant to payment/asset UX.
- token-helpers — token convenience tooling.
- Confidential-Balances-Sample — confidential balances examples.
- crypto-primitives-examples — cryptographic primitive examples.
- noir-examples — ZK/Noir examples.
- solana-private-channels — privacy/channel research relevant only if product requires it.
- solana-attestation-site — UI/reference for attestation service.
- solana-record-site — UI/reference for record service.
- explorer — transaction/account UX and parsing reference.
- solana-developer-platform — developer platform patterns.
- connectorkit — connector patterns if GwapOS expands integrations.
- mosaic — inspect if its capability matches a future feature.
- vault — vault/custody reference; high risk, feature-triggered only.
- rewards — rewards/incentive patterns.
- portfolio — portfolio UI/data patterns.
- trading-portfolio — trading/portfolio-specific patterns.
- rpc-latency-monitor — RPC observability/selection.
- solana-data-aggregator — ecosystem data aggregation.
- solana-developer-data — developer/ecosystem data.
- design-system — Solana UI system reference; GwapSpot keeps its own brand system.
- github-workflows — shared CI patterns.
- github-actions — reusable action patterns.
- squads-program-action — multisig/program release automation reference.
- testnet-testsuite — cluster testing reference.
- SIMD-implementations — SIMD implementation tracking bridge.
- anchor-audits — Anchor audit evidence/reference.
- leanprover-solanalib — formal verification research when warranted.
- litesvm-docs — testing docs reference.
- solana-invoke — program invocation tooling/reference.
- txtx — infrastructure/deployment orchestration reference.
- txtx-supervisor-ui — UI for txtx operations.
- solana-ms-tools — Microsoft/cloud tooling if that deployment path is chosen.
- solana-ms-scaffold-kit — Microsoft-oriented scaffolding if needed.
- no-dna — non-human CLI behavior convention; useful for agent automation but not core runtime.

## Tier C — Educational, operational, ecosystem, or specialized value
- solana-bootcamp-2026 — current education/examples, not production authority.
- curriculum — learning material.
- solana-enterprise-training — enterprise education.
- awesome-solana-ai — discovery list, not authority for included projects.
- solana-playground — browser development environment reference.
- solana-microscope — specialized inspection/debug tooling.
- surfpool-web-ui — optional UI companion to Surfpool.
- core-community-call — ecosystem/core discussion archive.
- solana-governance — governance tooling/reference.
- solana-governance-proposals — governance proposal data.
- stake-o-matic — validator/staking operations, outside current product core.
- solana-validator-client-ids — validator metadata.
- validator-apis — validator-specific API surface.
- solana-go — Go client; GwapOS does not currently center Go.
- vector — specialized project; low direct fit absent a matching requirement.
- dvp — specialized project; intake only if a concrete GwapOS dependency emerges.
- fiber — specialized/new infrastructure; monitor rather than integrate now.
- SRFCs — process/spec material with lower immediate relevance than SIMDs.
- solana-gym-env — research/training environment.
- ping-api — utility service.
- buffer-layout-utils — legacy/specialized JS layout utility.
- raydium-clmm — DEX/CLMM-specific reference, not current GwapOS core.
- compressed-nfts — NFT/compression-specific material, not current core.
- conf-speakers — conference/content data, no engineering priority.
- no-dna — agent CLI convention (also noted in Tier B as a workflow reference; implementation priority remains low).

## Tier D — Legacy, superseded, archived, or low current GwapOS value
- developer-content — archived; prefer current solana-com/docs sources.
- templates-site — archived; use templates/create-solana-dapp instead.
- moneymq — archived.
- confidential-balances-exploration — archived; prefer current confidential balance examples/specs.
- explorer-fork-old — old fork; prefer explorer.
- homebrew-core — packaging mirror/fork; not GwapOS application intelligence.
- lastline — no current direct GwapOS implementation need identified.

## Notes
- A repository appearing in Tier B/C is **not rejected**. It means “review when a concrete feature needs it.”
- Security-sensitive repositories (vault, escrow, keychain, payment protocols) require their own deep intake before runtime adoption.
- The top-three additions are intentionally complementary: engineering guidance, realistic testing, and runtime feature verification.
