# Solana Infrastructure Reference — v1.0.0

**Status:** RESEARCHED / REFERENCE_ONLY — not a deployment approval  
**Reviewed:** 2026-11-16  
**Owner:** GWAP MASTER  
**Machine-readable catalog:** [`registries/SOLANA_INFRASTRUCTURE.yaml`](../../registries/SOLANA_INFRASTRUCTURE.yaml)  
**Source entry:** [`registries/SOURCE_REGISTRY.yaml`](../../registries/SOURCE_REGISTRY.yaml)  
**Decision:** `GWAP-SOL-INFRA-001` in [`registries/DECISION_REGISTRY.yaml`](../../registries/DECISION_REGISTRY.yaml)

## Purpose and authority

This is a **dated, versioned inventory of upstream references** from [Solana's developer hub](https://solana.com/developers), organized by capability. It records what each resource could contribute to GWAP and what must be proven before adoption. It is **not** an installed-dependency inventory, production-support statement, security certification, or evidence of integration.

Apply the authority order in [MASTER.md](../../MASTER.md): founder decisions, current GWAP code/deployment reality, and GWAP release/security controls outrank upstream examples. Keep GNS identity, GwapScore reputation, PPV proof/commerce, GwapOS orchestration, OAR neutral registry/verification, and RoyaltyRails rights/payment workflows separate.

**Version contract:** `v1.0.0` versions **this GWAP reference document and catalog**, not upstream Solana software. Official URLs were inspected on 2026-11-16; they are living pages, not immutable upstream pins. `upstream_commit_or_release: null` explicitly means **not yet pinned**. No third-party source, SDK, executable skill, or deployment may advance to `PILOT` until its exact release/commit, license, security evidence, and compatibility are recorded.

## 1. Identity

### Agent Registry — `SOL-IDENTITY-001`
- **Primary source:** https://solana.com/agent-registry
- **Capability:** Published Solana-facing entry point for an onchain AI-agent identity, feedback/reputation, and validation registry, with ERC-8004 interoperability references.
- **Potential GWAP consumers:** OAR (discover/verify *external* agent registry claims), GNS (optional linking), GWAP agents (future). GwapScore does **not** automatically import third-party scores as authoritative reputation.
- **Boundary:** An agent registration is not proof that the operator controls a particular app/program/domain, and neither is a security audit or an endorsement. Assess registry authority, wallet/control proofs, replay, provenance, feedback abuse, and chain-specific semantics separately.
- **Disposition:** RESEARCHED; no OAR schema or agent registry integration approved.

### Solana Attestations (identity-adjacent) — `SOL-VERIFY-001`
- **Primary source:** https://solana.com/docs/tools/attestations
- **Capability:** Credentials, schemas, issuers, and attestations attach verifiable claims to onchain accounts.
- **Boundary:** An attestation only means what its schema, *actual subject*, credential authority, verified issuer, and target cluster support. Never present an arbitrary issuer's assertion as GWAP verified identity.

## 2. Verification

### Solana Attestations — `SOL-VERIFY-001` (canonical entry above)
- **Candidate consumers:** OAR verification primitives; optional GNS proof-of-control and GwapScore verified-evidence inputs.
- **Pilot prerequisites:** Evaluate issuer trust and revocation/expiry semantics; verify exact account/domain/program subject, schema and payload, attesting authority, proof-of-control, chain/cluster, replay protection and stale/cross-cluster claims. Decide how records are read and validated independently of UI badges.
- **OAR rule:** Verified control/association is **not** a code audit, exploit guarantee, scam determination, or permission for custody/mainnet deployment. Existing OAR production gates remain separate.
- **Acceptance evidence:** Threat model plus negative tests for wrong host, wrong cluster, unauthorized issuer, mismatched subject, revoked/expired claim, malformed payload, and replay; release evidence in the OAR repository if actually implemented.

## 3. Security

### Solana Keychain — `SOL-SEC-001`
- **Sources:** https://solana.com/docs/tools/keychain and https://solana.com/docs/tools/security
- **Capability:** Signing adapter across distinct key-management backends, subject to backend-specific signing capabilities.
- **Potential consumers:** PPV, RoyaltyRails, GwapOS server workflows, OAR issuance operations where authorized.
- **Hard rule:** A signer is **not** an authorization system. Maintain deterministic transaction policy, simulation/review, explicit signing scope, segregated keys, credential access logs, rotation, recovery, and human approval where required. No production key migration is authorized by this reference.
- **Pilot prerequisites:** Pin a version and backend, verify the selected backend's audit scope (do not generalize upstream audit claims), review signing API/capabilities, test deny paths and environment/key separation.

### Production readiness and security guidance — `SOL-SEC-002`
- **Sources:** https://solana.com/docs/tools/production-readiness and https://solana.com/docs/tools/security
- **Capability:** Baseline guidance for key management, production RPC/fallback, priority fees, retries, token/program address validation, monitoring, and load tests.
- **GWAP authority:** Supplemental checklist only. GWAP release integrity, onchain binary/IDL verification, signers, custody, treasury, OAR security review, and founder-only mainnet actions remain mandatory even if an upstream checklist is complete.

## 4. Testing

### Surfpool — `SOL-TEST-001`
- **Source:** https://solana.com/docs/tools/surfpool
- **Capability:** Local Solana testing with just-in-time fetched mainnet account state and infrastructure-as-code facilities.
- **Candidate consumers:** OAR, GNS, PPV, RoyaltyRails, GwapScore wallet intelligence.
- **Pilot prerequisites:** Pin exact tooling version; run deterministic fixtures, account/cluster mismatch scenarios and relevant adversarial tests. Fetched mainnet state is **test input**, not an authorization to transact on mainnet.
- **Evidence:** Saved commands, fixtures, test logs, and explicit comparison to existing validator/devnet tests.

### LiteSVM — `SOL-TEST-002`
- **Source:** https://solana.com/docs/tools/litesvm
- **Capability:** Fast in-process program tests; especially useful for regression and negative-path coverage.
- **Boundary:** LiteSVM complements, but does not replace, local-validator integration tests, Surfpool realistic tests, devnet acceptance, or release-artifact verification.

## 5. Monitoring

### Microscope — `SOL-MON-001`
- **Source:** https://solana.com/microscope
- **Upstream repository:** https://github.com/solana-foundation/solana-microscope
- **Capability:** Self-hosted IDL-decoded program activity and optional Squads multisig monitoring with dashboards and alert destinations.
- **Candidate consumers:** PPV upgrade/governance operations, OAR registry and issuer activity, RoyaltyRails settlement events, GNS program events.
- **Pilot prerequisites:** Validate exact program ID, cluster, IDL version, data pipeline, deployment infrastructure, access controls, log retention and alert correctness; test alerts for unexpected authority changes, sensitive instructions, failed operations and governance activity. Protect notification secrets.
- **Boundary:** A dashboard is not proof of uninterrupted coverage. Confirm indexing gaps, alert latency, alert routing and runbook ownership; do not claim live GWAP monitoring until deployed and tested.

## 6. Payments

### Kora — `SOL-PAY-001`
- **Source:** https://solana.com/docs/tools/kora
- **Capability:** Fee sponsorship/paymaster and trusted-signing infrastructure with configurable policies.
- **Candidate consumers:** GwapOS onboarding and selected GNS transactions, only if product economics justify sponsorship.
- **Hard rule:** A fee payer is separate from user consent, transaction authority, custody, and treasury. Sponsored signing must have policy allowlists, value/spend ceilings, RPC authentication, abuse protection, monitoring and reconciliation.
- **Pilot prerequisites:** Pin Kora release, exact signing backend, RPC/API integration and deployment architecture; threat-model fee drain, replay and transaction rewriting; test hard-deny cases.

### Solana Pay — `SOL-PAY-002`
- **Source:** https://solana.com/docs/tools/solana-pay
- **Capability:** Wallet-readable transfer and transaction requests for merchant/user-initiated payments.
- **Boundary:** Payment UX and request formats do not replace server-side confirmation, mint/recipient validation, quote expiry, idempotency, refunds or receipts. Existing Stripe and PPV responsibilities remain separate.

### x402 — `SOL-PAY-003`
- **Source:** https://solana.com/x402
- **Capability:** HTTP-native paid API/content access (ecosystem reference; not a claim that GWAP implements x402).
- **Boundary:** Keep the current MASTER distinction between API/payment challenges, Kora fee sponsorship, Stripe fiat settlement, and PPV commerce evidence. Agents cannot authorize spending merely by proposing it.

## Capability-to-product evaluation map

| Product | Strongest references to **evaluate** | Current disposition |
| --- | --- | --- |
| OAR | Attestations, Keychain, Surfpool/LiteSVM, Microscope | Research only; no verified production integration claimed |
| GNS | Attestations, Surfpool, optional Kora | Identity ownership stays with GNS; no new integration approved |
| GwapScore | Verified attestation inputs, testing tools | Scoring is GWAP policy, not delegated to an issuer or agent registry |
| PPV | Keychain, Microscope, Surfpool, production readiness | Devnet/custody/mainnet release gates remain unchanged |
| RoyaltyRails | Keychain, Microscope, Solana Pay/Kora as appropriate | Rights records, commerce, and settlement remain bounded |
| GwapOS | Kora, Solana Pay, account-linked verification | Optimize first-five-minute value only after policy/economic review |

## Required intake / promotion gate

1. **Propose outcome and owner** in the product/repository that would actually implement the capability.
2. **Pin immutable upstream commit/release** and record maintainer, license, audit *scope* and provenance; audit executable agent skills separately.
3. **Compare current GWAP implementation** and alternatives; document why this primitive reduces risk, improves value or removes maintenance.
4. **Threat-model** key, issuer, program, cluster, spend, privacy, security and authority boundaries; define deny/negative tests.
5. **Pilot narrowly** on a dedicated branch using realistic local tests; retain existing test layers until equivalent/improved.
6. **Collect GWAP-specific verification evidence** in owning repos and the relevant registries. Do not infer adoption from upstream documentation.
7. **Promote status separately** through GWAP decisions and release gates. Production, mainnet, custody, signer and spend authority always require their own approvals.

## Reference maintenance

- **Next review:** On a material upstream breaking change, audit/release, protocol activation change, new GWAP integration request, or no later than 2027-02-16.
- On review, record changed URLs, versions, capabilities, threat models and observed GWAP state. Publish **v1.0.1** for non-semantic corrections; **v1.1.0** for new optional resources/categories; **v2.0.0** for altered taxonomy/decision semantics.
- Versions here are documentary SemVer, not Git tags or upstream package versions. Tags/releases and pinned SDK versions require separate action.
