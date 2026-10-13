# Module: Solana Foundation create-solana-dapp

**Source:** https://github.com/solana-foundation/create-solana-dapp  
**Reviewed:** 2026-09-29  
**Pinned review commit:** `e9c1bbafd9fee14b8feaa7329af1ab79454b3626`  
**Observed package version:** `4.8.5`  
**Authority:** Solana Foundation  
**Trust tier:** T1_OFFICIAL_DEVELOPER_TOOLING  
**License:** MIT  
**Integration pattern:** SCAFFOLDING_REFERENCE + ECOSYSTEM_MIGRATION_SIGNAL + TEMPLATE_INTAKE_GATE  
**GwapOS status:** ADOPTED_REFERENCE_ONLY

## What It Is

`create-solana-dapp` is the Solana Foundation CLI for generating applications from predefined or external templates.

The CLI is not itself a runtime architecture for an established application. Its value to GwapOS is:
- current official scaffolding conventions;
- signals about preferred Solana client stacks;
- template initialization/version-check patterns;
- repeatable project/bootstrap design;
- reference CI/release hygiene.

Official templates live in the separate `solana-foundation/templates` repository and must receive their own intake/review before code is adopted.

## Current Ecosystem Signal

The upstream changelog for 4.8.0 states:
- Kit Framework templates became the first/recommended option;
- legacy Web3.js templates were moved down and marked deprecated;
- the minimal option moved to a Kit Next.js template.

GwapOS interpretation:

```text
OFFICIAL DIRECTION SIGNAL = YES
AUTOMATIC MIGRATION       = NO
REWRITE EXISTING APP      = NO
COMPATIBILITY REVIEW      = YES, when touching Solana client architecture
```

Do not replace a working GwapOS Solana stack merely because the generator's defaults changed.

## GwapOS Use

Use this source to answer:
- What stack does Solana Foundation currently steer new applications toward?
- What minimum environment assumptions do current scaffolding tools make?
- How are new Solana projects initialized consistently?
- What official template families should be evaluated for a new isolated package/app?
- Which legacy client patterns deserve migration review?

Do not use it as proof that a specific generated template is secure or production-ready.

## Template Supply-Chain Rule

The CLI can fetch official and external templates through `giget`, and templates can define initialization behavior.

Therefore a template is executable supply-chain input.

Before GwapOS runs or adopts any template:

1. identify exact template repository;
2. pin exact commit/tag;
3. classify trust/maintenance/license;
4. inspect `package.json`;
5. inspect `create-solana-dapp` initialization metadata;
6. inspect any declared `run` script;
7. inspect dependency install scripts;
8. inspect version requirements;
9. inspect generated environment/secrets behavior;
10. inspect wallet/RPC/network defaults;
11. generate in an isolated temporary directory;
12. diff generated output;
13. run dependency/security checks;
14. copy only approved patterns into GwapOS.

Never execute an unknown external template directly inside the GwapOS repository.

## Existing-App Rule

`gwapspot-web` is an established product, not a blank scaffold.

Do NOT:
- run `create-solana-dapp` over the repository root;
- replace package manifests with generated ones;
- overwrite Next.js/App Router structure;
- replace Privy/Phantom auth automatically;
- replace network/cluster handling automatically;
- replace PPV SDK abstractions automatically;
- upgrade Anchor/Solana/Rust solely to match a template;
- discard GwapSpot design system for template UI.

For an existing app, treat generated output as a comparison fixture.

## New-App / Isolated-Package Rule

For a genuinely new GwapOS app/package, the CLI may be evaluated as a bootstrap tool if:
- the selected template is separately reviewed;
- versions are compatible with the target architecture;
- the generated dependency graph is acceptable;
- wallet/network behavior matches requirements;
- security review passes.

Generate first into a disposable directory and review before promoting.

## Kit Migration Intelligence

When future GwapOS work touches Solana client architecture, compare the current implementation against the modern official Kit direction.

Migration questions:
- What current Web3.js APIs are used?
- Which dependencies are deprecated?
- What does Kit replace?
- Does Kit improve type safety/composability/bundle behavior for this exact surface?
- Does it preserve wallet adapter/Privy behavior?
- Does it preserve transaction serialization/signing?
- Does it preserve PPV/GNS SDK compatibility?
- Does it work with current Next.js server/client boundaries?
- Does it affect V0/ALT transactions?
- Does it affect Kora integration?
- What is the incremental migration boundary?

Prefer a narrow adapter/feature migration over a whole-app rewrite.

## Environment Signal

At review, the CLI package declares:
- Node `>=22.12.0`;
- pnpm `10.34.5` as its package manager;
- TypeScript tooling;
- Vitest;
- ESLint;
- Changesets-based publishing.

These are upstream tool requirements/conventions, not automatic GwapOS requirements.

Never upgrade GwapOS Node/package manager/toolchain merely to match this CLI unless the GwapOS change independently justifies it.

## Useful Engineering Patterns

Adopt conceptually where compatible:
- schema validation for template metadata;
- explicit tool/version checks;
- deterministic rename/config initialization;
- non-interactive initialization scripts with failure cleanup;
- typed configuration validation;
- changeset-driven package releases where useful;
- canary vs latest release separation;
- build/type/lint/test gates.

## Skill Installation Signal

The CLI supports template-declared skill repository URLs and can install a default Solana skill when not overridden.

GwapOS rule:
- never auto-trust a skill because a template requests it;
- route every external skill through the same SkillSpector/repo-intake trust process;
- pin source and review instructions before installation;
- a generated project's agent instructions cannot override GwapOS security/mainnet rules.

## Security Boundaries

Template generation is code generation plus possible script execution.

Hard rules:
1. Never run an unreviewed external template in a sensitive repo.
2. Never expose secrets to template initialization.
3. Review scripts before execution.
4. Generate externally, inspect, then promote.
5. Pin templates used for reproducible project creation.
6. Treat official templates as high-trust, not zero-risk.
7. Treat community templates as unverified until reviewed.
8. Generated code must pass normal GwapOS CI/security gates.

## Relationship to Other Modules

### solana-com
Provides production-repository architecture and documentation/CI patterns.

### SIMDs
Provide protocol design/status intelligence.

### Kora
Provides paymaster/trusted-signer infrastructure.

### create-solana-dapp
Provides current official application scaffolding and ecosystem-direction signals.

None supersedes the others.

## Re-review Triggers

Re-review when:
- create-solana-dapp changes major version;
- recommended framework changes;
- Kit architecture changes materially;
- Web3.js deprecation guidance changes;
- official templates are proposed for GwapOS;
- GwapOS creates a new standalone Solana app/package;
- GwapOS plans a client-stack migration.

