# Module: Solana.com Production Repository

**Source:** https://github.com/solana-foundation/solana-com  
**Reviewed:** 2026-09-29  
**Pinned review commit:** `fdd3cbc7c84cf909637875973aef9d088fd1f856`  
**Authority:** Solana Foundation  
**Trust tier:** T1_OFFICIAL  
**License:** GPL-3.0-or-later  
**Integration pattern:** ARCHITECTURE_REFERENCE + SOLANA_DOCS_REFERENCE + AGENT_WORKFLOW_REFERENCE  
**GwapOS status:** ADOPTED_REFERENCE_ONLY

## Why This Repository Matters

`solana-com` is the production monorepo behind solana.com. At review time it is an actively maintained pnpm/Turborepo repository containing multiple separately deployed Next.js applications plus shared packages.

The useful lesson for GwapOS is not "copy Solana's website." It is how a large public Solana property organizes:

- multiple Next.js surfaces behind one public domain;
- shared UI, navigation, i18n, monitoring and sitemap packages;
- route ownership across separately deployed applications;
- agent-facing repository context;
- affected-only CI;
- security scanning;
- executable documentation examples;
- scheduled dependency-drift testing.

Because the repository is GPL-3.0-or-later, GwapOS treats it as a reference source by default. Do not copy implementation code into differently licensed/proprietary GwapOS code without explicit license review.

## Observed Architecture

```text
solana.com monorepo
├── apps/web
├── apps/docs
├── apps/media
├── apps/templates
├── apps/accelerate
├── apps/breakpoint
└── packages/
    ├── config-eslint
    ├── config-typescript
    ├── docs-examples
    ├── ecosystem-data
    ├── fab-menu
    ├── i18n
    ├── sentry
    ├── sitemap
    ├── ui
    └── ui-chrome
```

The repo uses:
- Node.js 24.x;
- pnpm 11.13.1;
- Turborepo;
- Next.js App Router;
- TypeScript;
- Vitest;
- Playwright;
- shared packages for cross-app concerns.

Do not adopt these exact versions merely because Solana.com uses them. Use them as compatibility/reference evidence and compare against GwapOS requirements.

## Pattern 1 — Agent Context Is Maintained Infrastructure

The repository contains root and app-level `AGENTS.md` files. The root guide acts as a routing map for coding agents:

```text
request
  ↓
identify owning app/workspace
  ↓
open app AGENTS.md
  ↓
open package.json
  ↓
inspect routing/config
  ↓
make targeted change
```

The repo also carries a `refresh-agent-context` Agent Skill that audits workspace structure and refreshes agent-facing docs when apps, packages, ports, routes, or tooling change.

### GwapOS adaptation

Adopt the pattern, not the GPL text/code.

GwapOS repositories with multiple products/packages should maintain concise agent context covering:
- workspace ownership;
- route ownership;
- validation commands;
- shared packages;
- environment/network boundaries;
- high-risk files;
- deployment ownership.

Agent docs should be refreshed when repository topology changes.

Do not turn `AGENTS.md` into an architecture encyclopedia. It should reduce exploration time.

## Pattern 2 — Targeted / Affected CI

Solana.com uses Turborepo affected execution for type checking and tests.

GwapOS principle:

```text
small change
   ↓
targeted workspace checks
   ↓
required global/security/release gates
```

Prefer the smallest trustworthy validation scope during development while preserving full release/security gates where required.

This reduces unnecessary CI cost without weakening release policy.

## Pattern 3 — Executable Documentation

`packages/docs-examples` contains tested cookbook source snippets. CI validates TypeScript and Rust examples rather than assuming documentation remains correct.

### GwapOS rule

For documentation containing copy/paste-critical:
- Solana transactions;
- SDK usage;
- PPV calls;
- GNS resolution;
- wallet/network examples;
- CLI commands that can be executed safely in test environments;

prefer executable/testable source artifacts that documentation imports or references.

```text
tested source
   ↓
documentation snippet
```

is stronger than:

```text
handwritten docs snippet
   ↓
hope it still works
```

Do not execute examples that can move real funds, mutate mainnet state, expose secrets, or perform destructive actions merely to keep docs fresh.

## Pattern 4 — Scheduled Dependency Drift Tests

Solana.com runs a scheduled job that updates documentation-example JavaScript dependencies to latest and executes the suite. This detects SDK breakage before a user encounters stale cookbook code.

### GwapOS adaptation

For selected non-production compatibility suites:

```text
scheduled job
   ↓
install baseline lockfile
   ↓
update selected SDK dependencies in ephemeral CI
   ↓
show resolved versions
   ↓
run compatibility tests
   ↓
report failure
```

Important:
- never auto-merge dependency changes solely because the drift test passes;
- never mutate the production lockfile from the scheduled probe;
- pin production dependencies independently;
- use the probe to surface compatibility work.

High-value targets include:
- Solana client SDKs;
- Anchor tooling;
- wallet adapters/auth libraries;
- PPV SDK;
- GNS SDK;
- RPC/provider compatibility.

## Pattern 5 — Security Jobs Are Independent of Product Tests

The repository runs:
- Gitleaks secret scanning;
- production dependency auditing;
- scheduled full scans;
- supply-chain protections around package installation.

### GwapOS adaptation

Keep distinct gates for:
1. product correctness;
2. secrets;
3. dependency vulnerability policy;
4. Agent Skill security;
5. Solana program provenance/verifiable builds.

One green test suite must not imply the other security layers passed.

## Pattern 6 — Shared Cross-App Infrastructure

Solana.com centralizes common concerns such as:
- UI primitives;
- global chrome/navigation;
- i18n;
- Sentry helpers;
- sitemap generation;
- ecosystem metadata.

GwapOS should use the same architectural principle when duplication appears across:
- public gateway;
- OS/app;
- GNS/profile surfaces;
- documentation;
- Marketplace;
- Daily Ideas.

Extract a shared package only when ownership and reuse are real. Do not create packages merely to imitate a monorepo.

## Pattern 7 — Cross-App Routing Is an Explicit Boundary

Solana.com has separately deployed apps surfaced behind a common public domain using rewrites/asset prefixes and shared navigation logic.

This is directly relevant to GwapSpot's public-domain/application separation.

GwapOS rule:
- document which app owns each route;
- distinguish internal client navigation from cross-app navigation;
- test rewrites/redirects at deployment boundaries;
- keep shared navigation aware of application boundaries;
- validate asset paths when a separately deployed app is mounted below another public route.

Do not transplant Solana.com's exact routing implementation; derive the GwapOS version from its own Vercel/domain topology.

## Agent Skills Found Upstream

At review time the repository contains repo-scoped Agent Skills including:
- `llms-txt-generator`;
- `localize-page`;
- `refresh-agent-context`;
- `review-external-prs`;
- `wallet-filter-research`;
- `youtube-to-links`.

These are evidence that repository-local skills can encode repeatable engineering procedures.

They are **not automatically approved GwapOS skills**.

Before installing/executing an upstream skill:
1. pin the exact candidate;
2. apply license review;
3. run the approved SkillSpector process;
4. manually review authority/behavior;
5. adapt/reimplement when GPL boundaries require it.

## Hard Rules

1. Treat this repository as T1 official Solana Foundation evidence for how solana.com is implemented at the pinned review commit.
2. Do not treat website content as protocol consensus/specification when a more authoritative protocol source exists.
3. Do not copy GPL-licensed implementation code into incompatible GwapOS code without license review.
4. Prefer pattern-level reimplementation.
5. Do not install upstream Agent Skills merely because they are first-party.
6. Use SkillSpector before executing/installing third-party/upstream skill packages.
7. Do not automatically adopt Solana.com's dependency versions.
8. Keep mainnet-mutating examples out of automated documentation tests unless explicitly designed and authorized for that environment.

## Recommended GwapOS Actions

- Maintain concise repo-level and workspace-level agent context.
- Add a deterministic agent-context drift audit for large monorepos.
- Make critical Solana documentation examples executable/testable.
- Add scheduled SDK dependency-drift compatibility probes.
- Keep secrets/dependency/security/provenance gates independent.
- Apply explicit route ownership to multi-app GwapSpot surfaces.

