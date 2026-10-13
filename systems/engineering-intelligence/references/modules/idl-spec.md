# Module: Solana IDL Specification
Source: https://github.com/solana-foundation/idl-spec
Reviewed: 2026-09-29
Pinned commit: `7a7b5acdfd75a101e86117ee3a9b1cf178ff8a48`
Current spec: `0.1.0`
Trust: T1_OFFICIAL_INTERFACE_SPEC
License: MIT
Status: ADOPTED_REFERENCE

Framework-agnostic IDL standard for instructions, accounts, types, events, errors and constants.

## GwapOS use
Use as the interoperability reference when comparing:
- Anchor-generated IDLs;
- native/Pinocchio/Codama-generated clients;
- deployed Program Metadata;
- frontend/SDK schemas.

For PPV release integrity, an IDL comparison should identify:
repo IDL -> deployed metadata IDL -> generated SDK/client expectations.

IDL equality does not prove program binary equality; verifiable builds remain a separate gate.
