# GWAP MASTER

**Version:** 1.0.0  
**Role:** Canonical decision and evidence layer for the GWAP ecosystem.  
**Status:** ACTIVE

## Mission

GWAP MASTER is the single front door for serious product, engineering, protocol, security, deployment, payment, identity, reputation, proof, and digital-asset decisions across the GWAP ecosystem.

> **Source authority + GWAP reality + explicit decision + implementation evidence + verification evidence = GWAP truth.**

External technology informs GWAP. It does not control GWAP.

## Source-of-truth order

1. Explicit founder/product decisions.
2. Current GWAP repository and deployed-system reality.
3. GWAP security, authority, mainnet, custody, and release gates.
4. Current official protocol/specification evidence matching the installed environment.
5. Pinned official upstream repositories and releases.
6. Established ecosystem documentation and audited implementation references.
7. Examples, templates, community guidance, tutorials, and generated code.

When sources conflict, higher-authority evidence wins unless a formally recorded decision says otherwise.

## GWAP system map

```text
                         GWAP MASTER
                              |
      +-----------------------+-----------------------+
      |                       |                       |
 PRODUCT TRUTH          ENGINEERING TRUTH       RELEASE TRUTH
      |                       |                       |
      +-----------+-----------+-----------+-----------+
                  |                       |
             GWAPOS / APP             SOLANA
                  |                       |
   +--------------+--------------+        |
   |              |              |        |
  GNS         GwapScore         PPV       |
identity       reputation     proof/      |
                           commerce       |
                              |           |
                 +------------+-----------+
                 |
          PAYMENTS / VALUE
     Stripe | MPP/x402 | Kora
                 |
              SOLANA
                 |
      +----------+-----------+
      |                      |
DIGITAL ASSETS          PROTOCOL STATE
Metaplex/Token-2022     Specs/SIMDs/
                         Activation
```

## Core ownership boundaries

### GNS
Owns identity and `.gwap` naming/profile resolution.

### GwapScore
Owns social reputation and trust signals.

### PPV
Owns proof, commerce evidence, receipts, and eventually explicitly authorized escrow/custody.

### GwapOS
Owns user orchestration, application UX, routing, wallet/auth experience, and cross-product integration.

### Payment layer
- **Stripe:** fiat/subscription/hosted checkout.
- **MPP/x402 + Pay/Pay Kit:** machine/API payment challenge flows.
- **Kora:** fee sponsorship/paymaster/trusted signer boundary.
- **PPV:** business evidence and commerce state surrounding value movement.

These are complementary, not interchangeable.

### Digital asset layer
Before tokenizing anything, compare:
- stay off-chain;
- custom program state;
- Token-2022;
- MPL Core;
- Token Metadata;
- Bubblegum/compressed assets;
- Metaplex Inscriptions when specifically validated for the use case.

GwapMojis remains **off-chain by default, optional mint later** unless that product decision is explicitly superseded.

## Engineering decision flow

```text
1. Define user/product outcome
        |
2. Identify owning GWAP subsystem
        |
3. Inspect current repo/deployed reality
        |
4. Identify authoritative source layer
        |
5. Pin exact upstream versions/commits
        |
6. Threat-model authority/value/data
        |
7. Implement smallest correct change
        |
8. Unit + integration + realistic scenario tests
        |
9. Devnet / target-environment verification
        |
10. Release artifact / IDL / hash verification
        |
11. Record evidence in registries
        |
12. Promote status deliberately
```

## Required decision record

Every material architectural or production decision should be expressible as:

```text
DECISION_ID=
TITLE=
STATUS=
OWNER_SYSTEM=
USER_OUTCOME=
DECISION=
WHY=
ALTERNATIVES=
AUTHORITATIVE_SOURCES=
PINNED_VERSIONS=
SECURITY_BOUNDARY=
IMPLEMENTATION=
TEST_EVIDENCE=
DEPLOYMENT_EVIDENCE=
ROLLBACK=
REVIEW_TRIGGER=
APPROVED_BY=
APPROVED_AT=
```

Valid lifecycle statuses: PROPOSED, RESEARCHED, PILOT, DEVNET_VERIFIED, RELEASE_CANDIDATE, PRODUCTION, DEPRECATED, SUPERSEDED, BLOCKED.

## Protocol evidence model

```text
Official protocol specs
        +
SIMD design/status
        +
Feature activation evidence
        +
Observed target-cluster behavior
        =
Usability evidence
```

A proposal being accepted does not prove activation. A local validator passing does not prove mainnet support. A public announcement does not replace target-cluster verification.

## Testing model

```text
Unit tests
    |
Local deterministic tests
    |
Local validator
    |
Surfpool realistic scenarios
    |
Devnet acceptance
    |
Release-candidate verification
```

Do not delete a proven test layer merely because a newer tool exists. Replace only after measured equivalence or improvement.

## Release-integrity model

For Solana programs:

```text
Repo commit
   -> tests
   -> deterministic/verifiable build
   -> preserved .so
   -> executable hash
   -> deploy exact artifact
   -> on-chain hash
   -> hash comparison
   -> deployed IDL/interface comparison
   -> release evidence
```

IDL verification and binary verification are independent gates.

## Signer and authority model

A signer is not an authorization system.

```text
User/GWAP policy
   -> deterministic transaction policy
   -> transaction construction
   -> simulation/review
   -> signer adapter
   -> signer backend
   -> broadcast
```

Keep separate: user wallet, Kora fee payer, PPV program upgrade authority, PPV custody authority, GWAP treasury, and automation/agent credentials.

## Agentic-payment model

```text
Model proposes need
   -> deterministic payment policy
   -> challenge validation
   -> human/policy authorization
   -> signer
   -> settlement
   -> resource delivery
   -> receipt/reconciliation
```

Model intent is never financial authorization.

## Digital-asset model

Do not begin with “make it an NFT.” Begin with the user outcome and decide whether on-chain ownership, transferability, collection semantics, royalties, plugins, compression, permanence, or marketplace interoperability are actually required.

## Directory

- `registries/PRODUCT_TRUTH.yaml` — product/system ownership and locked decisions.
- `registries/DECISION_REGISTRY.yaml` — architectural and implementation decisions.
- `registries/RELEASE_REGISTRY.yaml` — release/deployment evidence records.
- `registries/SOURCE_REGISTRY.yaml` — top-level source routing and links into engineering intelligence.
- `schemas/decision-record.schema.json` — decision record structure.
- `schemas/release-record.schema.json` — release evidence structure.
- `scripts/validate_registries.py` — checks the registries against the schemas.
- `runbooks/DECISION_WORKFLOW.md` — how to process a new decision.
- `runbooks/RELEASE_WORKFLOW.md` — how to promote a change.
- `runbooks/NEW_REPO_INTAKE.md` — how new external repositories enter MASTER.
- `examples/EXAMPLE_DECISIONS.md` — sample records.
- `systems/engineering-intelligence/` — GwapOS Engineering Intelligence v2.1.0.
- `CLAUDE.md` — agent instructions for this repository.
- `.claude/agents/` — GWAP agent team definitions.
- `runbooks/AGENT_WORKFLOWS.md` — task routing and workflows for the agent team.

## Rule for future work

New repositories, standards, SDKs, tools, audits, protocols, and product decisions enter MASTER through intake and decision records rather than disconnected notes.

MASTER is not “everything we know.” MASTER is **everything we are willing to rely on, with provenance and status attached.**
