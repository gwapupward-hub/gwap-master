# Release Workflow

## Web/application
Record repo SHA, lint/type/build/tests, environment/config, preview/staging evidence, deployment target, rollback target and approval.

## Solana programs
Freeze repo SHA/cluster/program ID/library/authority; complete tests; build deterministically/verifiably where applicable; preserve exact `.so`; record SHA-256/executable hash; deploy exact artifact; compare on-chain hash; verify IDL/interface independently; record authority/cluster evidence. Block when critical evidence is unknown.

Mainnet, custody, authority changes, and automated spending require explicit approval.
