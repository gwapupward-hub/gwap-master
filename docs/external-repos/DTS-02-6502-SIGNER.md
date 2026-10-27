# DTS-02 65C02 Ed25519 Signer — External Repository Intake

**Status:** REFERENCE_ONLY  
**Reviewed:** 2026-10-27  
**Upstream:** https://github.com/aeyakovenko/dts02-6502-signer  
**Default branch:** `main`  
**Repository owner:** `aeyakovenko`  
**Primary language:** Python (repository metadata); simulation includes C and 65C02 assembly components.

## What it is

The upstream README describes DTS-02 as a 65C02-based desktop/offline Ed25519 signer concept intended to act as a third offline signer in a 2-of-3 Squads multisig. The design includes a W65C02S CPU, SRAM and OTP ROM, glue logic, physical controls, a display, and hardware message/result bank locks plus a fault latch.

The repository includes a revision 0.4 breadboard specification, a pure-Python pin-level simulation, timing and electrical checks, generated wiring documentation, and emulated signing firmware. The README describes tests against RFC 8032/OpenSSL and Solana transfer messages. These are upstream claims and are not an independent GWAP audit or physical-device validation.

## GWAP disposition

- **Classification:** `REFERENCE_ONLY`
- **Potential relevance:** Research into offline signing, signer isolation, human-readable transaction review, fault handling, and multisig operational design.
- **Not adopted:** No code, firmware, circuit, signing workflow, or hardware is approved for use in GWAP products by this intake record.
- **No authorization change:** This repository does not grant transaction authority and does not change GWAP's signer, custody, treasury, PPV, Squads, or mainnet policies.
- **No deployment approval:** Do not connect a prototype or emulated signer to production keys or treat simulation results as hardware assurance.

## Required checks before any pilot or code reuse

1. Pin and record an exact reviewed commit; do not rely on a moving `main` branch.
2. Verify repository license and redistribution rights before copying or adapting any code or design.
3. Independently review the spec, simulator, firmware, cryptographic implementation, and test methodology.
4. Threat-model physical access, supply-chain tampering, firmware replacement, key generation/import, side channels, fault injection, recovery, and operator error.
5. Verify message construction and transaction-display semantics against the exact Solana transaction formats GWAP intends to sign.
6. Establish key-generation, backup, recovery, revocation, and signer-loss procedures.
7. If hardware is built, perform independent electrical, timing, fault-injection, and physical security testing; simulation alone is insufficient.
8. Require an explicit GWAP decision record and security review before any pilot, custody role, or production use.

## Re-review triggers

- A specific GWAP use case is proposed.
- Upstream publishes a tagged release or material spec/firmware changes.
- License information or independent audit evidence becomes available.
- A proposal is made to use the design in a Squads multisig or any production signing path.

## Source

Upstream README: https://github.com/aeyakovenko/dts02-6502-signer  
This intake records repository metadata and README-level claims only; it does not certify the design or its security.
