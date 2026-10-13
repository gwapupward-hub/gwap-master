# Module: Solana Protocol Specs
Source: https://github.com/solana-foundation/specs
Reviewed: 2026-09-29
Pinned commit: `136feee5d5b126dbfd351258ea621200346c84b1`
Trust: T1_OFFICIAL_PROTOCOL_SPEC
Status: ADOPTED

This repository aims to be a single source of truth for consensus-critical Solana protocol rules across core, gossip, consensus, runtime, p2p and API.

## Source hierarchy update
For consensus/runtime/API semantics:
1. current observed runtime/cluster evidence for what is active;
2. official protocol spec for normative behavior;
3. implementation source for exact release behavior;
4. SIMD for proposal/design rationale and lifecycle;
5. developer docs/examples.

Use specs when GwapOS behavior depends on wire format, runtime semantics, RPC/API behavior or consensus-critical interpretation.
