# Changelog

## 2.1.0 — 2026-09-30
- Added Metaplex ecosystem/digital-asset routing.
- Added current routing to MPL Core, Token Metadata and Bubblegum.
- Added digital-asset primitive decision gate and per-target license/audit checks.
- Preserved GwapMojis off-chain-first architecture.
- Marked `metaplex-foundation/metaplex` as an older directory, not current implementation authority.

## 2.0.0 — 2026-09-29

### Added — full next-tier Solana Foundation intake
- Framework Kit
- official templates
- program-examples
- solana-keychain
- pay-kit
- MPP specs
- Solana Program Library Foundation docs fork
- solana-web3.js
- official Solana MCP
- transaction-v1-examples
- Solana protocol specs
- Solana IDL tooling
- Solana IDL specification

### Important corrections / policy upgrades
- `solana-keychain` now has an Accretion audit baseline for Rust/TypeScript through a pinned commit; later commits plus Python/Go remain outside that reviewed scope.
- protocol specs outrank examples for normative runtime/API semantics.
- MPP protocol semantics are separated from Pay Kit SDK behavior.
- IDL compatibility is a separate release gate from executable binary provenance.
- transaction-v1 support requires sender, wallet, RPC reader and indexer compatibility.
- Framework Kit remains reference-only under current Kit-first guidance.

## 1.9.0 — 2026-09-29

### Organization audit
- triaged the public `solana-foundation` repository set by GwapOS implementation value;
- added `references/SOLANA_FOUNDATION_REPO_RANKING.md`.

### Added — top three missing capabilities
1. `solana-dev-skill` — official current agent-development guidance, reference-only pending executable-skill security scan.
2. `surfpool` — local/CI scenario-testing pilot, pinned to reviewed main and stable v1.6.0 signal.
3. `feature-activation-verifier` — feature-gate + behavioral verification to bridge SIMD status and target-cluster reality.

### Hardening
- modern Solana defaults are migration signals, not forced upgrades;
- Surfpool does not replace proven CI until validated;
- PENDING/SKIP feature-verifier outcomes are not success;
- no upstream Agent Skill execution before SkillSpector + manual review.

## 1.8.0 — 2026-09-29

### Added
- current Solana Foundation `pay` as T1 official agentic-payment intelligence;
- MPP/x402 HTTP 402 payment model;
- deterministic agent spending-permission contract;
- prompt-injection/payment-authority boundary;
- replay/idempotency/double-charge requirements;
- stablecoin allowlist and token-substitution checks;
- MCP/ACP payment safety boundary;
- payment receipt/reconciliation requirements;
- sandbox/devnet paid-API pilot path;
- explicit separation among pay, Kora, PPV Commerce and Stripe.

### Decision
Pilot/reference. The technology is directly relevant to future paid GwapOS APIs and agentic commerce, but automated value movement requires deterministic policy, bounded signer authority and explicit mainnet approval.

## 1.7.0 — 2026-09-29

### Added
- Solana Foundation `create-solana-dapp` as T1 official developer-tooling intelligence;
- official Kit-over-legacy-Web3.js migration signal;
- established-app no-overwrite rule;
- isolated template generation/intake gate;
- external-template executable supply-chain policy;
- template-declared skill review policy;
- current scaffolding/toolchain conventions as reference-only evidence;
- incremental Solana client migration guidance.

### Decision
Adopt the intelligence, not the scaffold. GwapOS is an established application; generator defaults inform modernization decisions but do not justify a rewrite.

## 1.6.0 — 2026-09-29

### Added
- Solana Foundation Kora as a T1 official paymaster/trusted-signer module;
- devnet-only pilot classification;
- audit-baseline and unaudited-delta gate;
- dedicated fee-payer identity requirement;
- fail-closed program/token/method policy;
- signer-backend/key-management guidance;
- rate/spend/usage/monitoring requirements;
- Lighthouse delayed-signing caveat;
- V0/ALT validation requirement;
- explicit separation from PPV upgrade/custody authorities;
- production promotion evidence template.

### Decision
Kora strongly matches GwapOS gas-abstraction goals, but a paymaster is a funded trusted signer. Pilot on devnet first. Production/mainnet adoption requires separate security review and explicit authorization.

## 1.5.0 — 2026-09-29

### Added
- Solana Improvement Documents as T1 official protocol-design intelligence;
- pinned review commit `4b643ca8746742183a469681765e694b385bb315`;
- explicit SIMD lifecycle model;
- proposal-status vs cluster-activation guardrail;
- protocol-change impact classification;
- security/backwards-compatibility/conformance review requirements;
- supersession/dependency tracking;
- present-tense mainnet claim guardrail for engineering, docs and GwapSpot news/content.

### Core rule
`Accepted` does not mean `Implemented`; `Implemented` does not mean `Activated`. Current cluster/runtime evidence is required for live/mainnet claims.

## 1.4.0 — 2026-09-29

### Added
- Solana Foundation `solana-com` as a T1 official production architecture/reference module;
- pinned review commit `fdd3cbc7c84cf909637875973aef9d088fd1f856`;
- GPL/copy-left intake boundary;
- agent-context maintenance pattern;
- targeted/affected monorepo CI guidance;
- executable documentation example policy;
- scheduled dependency-drift compatibility probe pattern;
- explicit cross-app route-ownership guidance;
- rule that upstream Agent Skills require SkillSpector + manual review before execution.

### Decision
Adopt architecture/process patterns, not repository code. `solana-com` is GPL-3.0-or-later and remains reference-only unless a separate license review approves code reuse.

## 1.3.0 — 2026-09-29

### Added
- NVIDIA SkillSpector as an adopted CI/security module;
- stable pin `v2.11.2` / commit `69dcdfb74487d361ba4c811d088cfdea2ff3a9dc`;
- official wheel SHA-256 integrity pin;
- strict `SAFE + complete + successful` GwapOS security policy;
- read-only JSON security-gate parser;
- SkillSpector GitHub Actions reference workflow;
- JSON/SARIF artifact retention;
- baseline/suppression governance;
- pre-install scanning rule for third-party executable Agent Skills;
- SkillSpector layer inside the AI/Agent/Skill release gate.

### Decision
Do not pin upstream `v2.12.0` yet because its release notes currently describe it as `candidate; publication pending`. Static scanning is required in routine CI; semantic LLM scanning is optional defense-in-depth.

## 1.2.0 — 2026-09-29

### Added
- `rohitg00/ai-engineering-from-scratch` specialist-reference intake;
- pinned source commit `1bafaa88bb4668356791150bec3a6d7df38387eb`;
- cross-cutting AI / agent engineering policy;
- outcome-first and artifact-contract rules;
- deterministic-work vs model-judgment separation;
- untrusted-content / prompt-injection trust boundary;
- baseline-vs-treatment evaluation requirement;
- RAG retrieval/generation split;
- production AI observability expectations;
- six-layer AI/Agent/Skill release gate;
- reusable AI feature evaluation template.

### Decision
The repository is `ADOPTED_REFERENCE`, not a production dependency or protocol authority. Lesson-specific tools, providers, thresholds, and frameworks must be independently justified before runtime adoption.

## 1.1.0 — 2026-09-29

### Added
- Ionic Framework repository intake;
- official source pin for `v9.0.5` / commit `b86733f289642a2ae27440bef4145a8359153a50`;
- mobile/cross-platform UI reference module;
- Next.js compatibility boundary;
- future GwapOS mobile/native-shell pilot criteria;
- rules preventing automatic replacement of Next.js App Router or GwapSpot design tokens;
- explicit requirement to evaluate Capacitor separately before native-runtime adoption.

### Decision
Ionic is **REFERENCE_ONLY** for the current GwapOS Next.js shell. Its strongest immediate value is mobile UX, component architecture, accessibility, theming, and testing guidance. Runtime adoption is deferred until an isolated mobile/native-shell pilot proves compatibility.

## 1.0.0 — 2026-09-29

Initial GwapOS Engineering Intelligence release.

### Added
- extensible external-repository intake model;
- source trust/conflict policy;
- versioned source registry;
- Solana Verified Builds capability module;
- deterministic release-artifact guardrails;
- build-once / deploy-same-artifact rule;
- executable vs onchain hash hard gate;
- pinned repository/commit verification workflow;
- mainnet remote-verification guardrail;
- multisig-aware verification guidance;
- read-only preflight script;
- GitHub Actions reference workflow;
- paste-ready implementation prompt.

### Architecture decision
Future repositories are added as focused modules rather than pasted into the root skill. Cross-cutting rules belong in `SKILL.md`; source-specific details belong in `references/modules/`.
