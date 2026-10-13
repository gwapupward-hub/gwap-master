# Module: Solana IDL Tooling
Source: https://github.com/solana-foundation/idl
Reviewed: 2026-09-29
Pinned commit: `87fd989174bb221dd74ccfe4e7620d67165f3793`
Trust: T1_OFFICIAL_TOOLING
License: MIT
Status: PILOT_REFERENCE

`@solana/idl` fetches/reconstructs program IDLs from Program Metadata (PMP) and legacy Anchor sources. The repo also scaffolds `@solana/security-txt`.

## GwapOS use
Potential release/integration verification:
- fetch deployed program IDL;
- compare deployed metadata against repo artifact;
- detect stale frontend/SDK IDL assumptions;
- surface security.txt where available.

Prefer PMP first; legacy injected Anchor IDL is deprecated for security reasons according to the related IDL spec guidance.

Do not trust fetched IDL blindly: bind it to the expected program ID, source, cluster and deployment evidence.
