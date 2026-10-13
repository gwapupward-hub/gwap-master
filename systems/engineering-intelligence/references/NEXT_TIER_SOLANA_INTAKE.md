# Next-Tier Solana Foundation Intake Matrix — 2026-09-29

| Repository | GwapOS classification | Main use |
|---|---|---|
| framework-kit | REFERENCE_ONLY | compare wallet/reactive client architecture |
| templates | ADOPTED_REFERENCE_ONLY | isolated new-project patterns |
| program-examples | ADOPTED_REFERENCE_ONLY | Anchor/Pinocchio/native implementation patterns |
| solana-keychain | PILOT_REFERENCE | signer abstraction/backends/security |
| pay-kit | PILOT_REFERENCE | MPP/x402 implementation SDK |
| mpp-specs | ADOPTED_PROTOCOL_REFERENCE | normative MPP semantics |
| solana-program-library | REFERENCE_ONLY | historical/docs SPL context; verify canonical source separately |
| solana-web3.js | MIGRATION_REFERENCE | legacy v1 containment and v3 compatibility |
| solana-mcp | ADOPTED_REFERENCE + OPTIONAL_TOOL | current docs/RAG/program checks |
| transaction-v1-examples | ADOPTED_REFERENCE_ONLY | tx-v1 compatibility and indexer/wallet gotchas |
| specs | ADOPTED | consensus/runtime/API normative reference |
| idl | PILOT_REFERENCE | deployed IDL/security metadata retrieval |
| idl-spec | ADOPTED_REFERENCE | framework-agnostic IDL interoperability |

## Priority order inside this group

1. specs
2. solana-keychain
3. pay-kit + mpp-specs
4. transaction-v1-examples
5. idl + idl-spec
6. solana-mcp
7. program-examples
8. templates
9. solana-web3.js
10. framework-kit
11. solana-program-library Foundation docs fork

This order is about GwapOS implementation value, not repository popularity.
