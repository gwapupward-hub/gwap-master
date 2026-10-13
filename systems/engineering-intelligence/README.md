# GwapOS Engineering Intelligence Skill v2.1.0

A reusable GwapOS engineering skill for safely turning high-value external GitHub repositories into **versioned capability modules**.

Current modules:

- **Solana Foundation — `solana-verifiable-build`**
- **Ionic Team — `ionic-framework`**
  - mobile/cross-platform UI architecture reference
  - interaction, accessibility, theming, and E2E patterns
  - future native-shell pilot trigger
  - intentionally **not** installed into the current Next.js shell by default
  - deterministic program builds
  - exact artifact preservation
  - executable/onchain hash comparison
  - pinned GitHub commit verification
  - mainnet remote verification workflow
  - multisig-aware verification guardrails

## Why this exists

GwapOS will continue discovering useful repositories. The wrong way to scale that is to keep pasting README instructions into prompts until the agent has a giant, contradictory rulebook.

This package uses a controlled model:

```text
External repository
        ↓
Repo intake / trust review
        ↓
Pinned source registry
        ↓
Capability module
        ↓
GwapOS integration boundary
        ↓
Implementation + verification evidence
```

Each new repo is evaluated before it becomes part of the operating skill.

- **Rohit Goyal — `ai-engineering-from-scratch`**
  - AI/agent production engineering reference
  - outcome-first and artifact-contract design
  - tool/trust boundaries and prompt-injection defense patterns
  - baseline-vs-treatment eval discipline
  - RAG, observability, cost/latency, and skill release gates
  - intentionally **reference-only**, not a production dependency bundle

- **NVIDIA — `SkillSpector`**
  - pinned skill-security scanner
  - prompt-injection / exfiltration / privilege / supply-chain / MCP checks
  - strict SAFE + complete + successful GwapOS gate
  - JSON/SARIF CI evidence
  - auditable baseline/suppression policy

- **Solana Foundation — `solana-com`**
  - production Solana web architecture reference
  - multi-app Next.js/Turborepo patterns
  - maintained agent-context documentation
  - executable docs + dependency-drift testing
  - GPL reference-only boundary

## Package

```text
GwapOS-Engineering-Intelligence-Skill-v2.1.0/
├── SKILL.md
├── README.md
├── manifest.json
├── CHANGELOG.md
├── Implementation-Prompt.md
├── references/
│   ├── SOURCE_REGISTRY.yaml
│   ├── REPO_INTAKE_PROTOCOL.md
│   ├── TRUST_AND_CONFLICT_POLICY.md
│   └── modules/
│       ├── solana-verifiable-build.md
│       ├── ionic-framework.md
│       ├── ai-engineering-from-scratch.md
│       ├── nvidia-skillspector.md
│       ├── solana-com-production-repo.md
│       ├── solana-improvement-documents.md
│       ├── solana-kora.md
│       ├── create-solana-dapp.md
│       └── solana-pay.md
├── templates/
│   ├── ai-feature-eval.yaml
│   └── skillspector-baseline.example.yaml
├── workflows/
│   ├── solana-verifiable-build-gate.yml
│   └── skillspector-security-gate.yml
└── scripts/
    ├── verified_build_preflight.py
    └── skillspector_gate.py
```

## Recommended repository placement

Use this as a repository-local skill, for example:

```text
.claude/skills/gwapos-engineering-intelligence/
```

or the equivalent skill directory used by your engineering agent.

Do not delete specialized GwapOS skills. This package is intended to orchestrate and strengthen them.

## Adding the next repo

When you find another repository:

1. Do **not** paste its README into `SKILL.md`.
2. Run the repository through `references/REPO_INTAKE_PROTOCOL.md`.
3. Add one entry to `references/SOURCE_REGISTRY.yaml`.
4. Add a focused module under `references/modules/`.
5. Update `SKILL.md` only if the new repo changes a cross-cutting operating rule.
6. Increment the skill version.
7. Add a changelog entry.
8. Verify the new module against current GwapOS repository reality.

That keeps the skill strong as it grows instead of turning it into prompt spaghetti.

## Current source facts

As reviewed on 2026-09-29, the upstream Solana Verified Builds documentation says:

- deterministic builds are performed with `solana-verify build`;
- production use should prefer a tagged `solana-verify` release;
- the exact verified `.so` should be deployed rather than rebuilding with Anchor/Cargo afterward;
- `verify-from-repo` supports pinning a commit and library/mount-path metadata;
- remote verification is mainnet-only;
- the old `verify-from-repo --remote` flow is deprecated in favor of `solana-verify remote submit-job`;
- verified builds improve transparency/provenance but do not replace security review.

See `references/modules/solana-verifiable-build.md` for the GwapOS interpretation.


## Ionic Framework intake decision

Ionic Framework `v9.0.5` is registered as an official Tier-1 source and pinned to release commit `b86733f289642a2ae27440bef4145a8359153a50`.

For the existing GwapOS Next.js application, the module is **reference-only**. It can improve how the engineering agent designs mobile-first UI, overlays, gestures, accessible controls, responsive behavior, CSS-variable theming, and Playwright/mobile testing without forcing an Ionic runtime dependency.

If GwapOS later creates a dedicated iOS/Android/native-shell app, the skill will reopen Ionic as a runtime candidate and require an isolated pilot before adoption.


## AI Engineering reference intake decision

`rohitg00/ai-engineering-from-scratch` is registered as a specialist reference at commit `1bafaa88bb4668356791150bec3a6d7df38387eb`.

The source is useful because it brings together production-minded patterns for LLM applications, RAG, tools, MCP, agents, security, observability, evaluation, and Agent Skills. GwapOS adopts those engineering principles selectively.

The package does **not** install the curriculum, its Python dependencies, model providers, or eval frameworks. Official protocol/vendor sources remain authoritative where applicable.

New cross-cutting additions:
- outcome-first AI feature design;
- artifact contracts before prompt orchestration;
- judgment vs deterministic-work separation;
- untrusted-content / prompt-injection boundary;
- baseline-vs-treatment AI evaluation;
- RAG retrieval/generation separation;
- AI observability requirements;
- six-layer reusable-skill release gate;
- reusable `templates/ai-feature-eval.yaml`.


## SkillSpector security-gate decision

NVIDIA SkillSpector is the first external source promoted from reference intelligence into a concrete skill-security CI gate.

GwapOS pins stable `v2.11.2` (`69dcdfb74487d361ba4c811d088cfdea2ff3a9dc`) and verifies the official wheel SHA-256 before installation.

The latest observed `v2.12.0` is intentionally not pinned because its upstream release notes describe it as a candidate pending publication.

Routine policy:
- static scan with `--no-llm`;
- preserve JSON/SARIF evidence;
- require `execution_successful=true`;
- require `analysis_completeness.is_complete=true`;
- require `recommendation=SAFE`;
- CAUTION requires review/rescan;
- DO_NOT_INSTALL blocks;
- scanner errors/incomplete reports block.

This scanner supplements the existing six-layer Agent Skill release gate; it does not replace behavioral or routing evals.


## Solana.com repository intake decision

`solana-foundation/solana-com` is adopted as an official production architecture/reference source, pinned for review at `fdd3cbc7c84cf909637875973aef9d088fd1f856`.

It is not imported as a code dependency. The repository is GPL-3.0-or-later, so GwapOS defaults to pattern-level learning and independent implementation.

Most valuable adopted patterns:
- maintained root/workspace `AGENTS.md` context;
- targeted/affected monorepo CI;
- executable documentation examples;
- scheduled dependency-drift probes;
- independent secret/dependency security jobs;
- explicit cross-app route ownership.

The upstream repository also contains Agent Skills. They are not automatically trusted or installed; SkillSpector and manual authority review remain required before execution.


## SIMD protocol intelligence

The Solana Improvement Documents repository is now a T1 protocol-design source.

GwapOS explicitly tracks the difference between proposal status and cluster reality:

`Idea → Draft → Review → Accepted → Implemented → Activated`

Only activation plus current runtime evidence should drive present-tense mainnet claims or production assumptions. This protects engineering decisions, documentation, and GwapSpot social/news content from announcing proposed or accepted Solana features as already live.


## Kora intake decision

Solana Foundation Kora is accepted as a **devnet paymaster/trusted-signer pilot candidate**.

The product fit is strong: it can remove the requirement that GwapOS users hold SOL for selected transactions and can support approved token-denominated fee flows. The security boundary is also substantial: Kora controls a funded signer.

Production adoption is intentionally withheld. Upstream states `main` may contain unaudited commits; its audit status is commit-based, and the README notes `solana-keychain` has not been audited.

GwapOS must pilot Kora as a separately deployed devnet service with a dedicated low-balance fee payer, narrow allowlists, authentication, bounded spend/rate/usage, external key management for production candidates, monitoring and explicit mainnet approval.


## create-solana-dapp intake decision

The official Solana application generator is adopted as scaffolding and ecosystem-migration intelligence, not as a runtime dependency.

The upstream 4.8.x direction makes Kit-based templates the recommended/default path and labels legacy Web3.js templates deprecated. GwapOS records that as a modernization signal while explicitly rejecting automatic rewrites of the established Next.js/wallet/PPV architecture.

Templates are separate supply-chain artifacts. Even official templates must be pinned and inspected; external templates must be generated in isolation and pass normal GwapOS security/CI gates before any code is promoted.


## Solana Foundation pay intake decision

The current `solana-foundation/pay` repository is adopted as a pilot/reference for agentic HTTP payments, not as a drop-in replacement for GwapOS commerce.

At review it centers on MPP and x402 payment challenges, stablecoin authorization/signing, MCP/ACP agent integrations, permission-scoped unattended payments and paywalled API gateways.

The key GwapOS rule is that model intent never equals financial authorization. A model can request a paid resource; deterministic policy and an approved signer/user decide whether value can move. `pay`, Kora, PPV Commerce and Stripe remain separate composable payment boundaries.


## Solana Foundation organization audit

v1.9.0 adds an organization-wide relevance audit and the top three previously missing capabilities:

1. **Solana Development Skill** — current official agent-facing Solana engineering guidance, adopted as reference only.
2. **Surfpool** — approved for a local/CI integration-testing pilot alongside existing validator tests.
3. **Feature Activation Verifier** — adopted as protocol activation/behavior evidence, initially as a pilot tool because its build currently depends on a local Surfpool clone.

See `references/SOLANA_FOUNDATION_REPO_RANKING.md` for the full tiered inventory.


## v2.0 — next-tier Solana Foundation intake

The full requested next group is now classified and represented:
Framework Kit, templates, program examples, Solana Keychain, Pay Kit, MPP specs, the Foundation SPL docs fork, solana-web3.js, Solana MCP, transaction-v1 examples, protocol specs, IDL tooling and the IDL specification.

Key upgrades:
- protocol specs now sit above examples/docs for normative runtime/API behavior;
- signer audit scope is tracked by commit and language;
- MPP spec is separated from Pay Kit implementation;
- transaction-v1 indexer/wallet/RPC compatibility is explicit;
- deployed IDL verification is separated from verifiable binary builds;
- Framework Kit remains reference-only due newer Kit-plugin guidance.

## v2.1 — Metaplex
Adds digital-asset routing across MPL Core, Token Metadata, Bubblegum, Token-2022, custom state and off-chain ownership. The old Metaplex directory is reference-only. GwapMojis remains off-chain by default with optional minting.
