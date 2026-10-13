# Module: Solana Verified Builds

**Source:** https://github.com/solana-foundation/solana-verifiable-build  
**Official docs:** Solana program verified-build documentation  
**Reviewed:** 2026-09-29  
**Trust tier:** T1_OFFICIAL  
**Integration pattern:** CI_TOOL + WORKFLOW  
**GwapOS status:** ADOPTED

## Problem It Solves

Normal program tests can prove that source code behaves as expected, but they do not by themselves prove that the bytecode deployed to a Solana Program ID came from the exact reviewed source commit.

This module adds release provenance:

```text
source commit
   ↓
deterministic build
   ↓
exact .so artifact
   ↓
executable hash
   ↓
deployment of same artifact
   ↓
onchain program hash
   ↓
repository / commit verification
```

## GwapOS Use

Use this module for deployable Solana programs such as GwapOS protocol components, PPV, GNS, or future programs when they reach a release candidate.

Do not use it as a reason to upgrade a working Anchor/Rust/Solana stack.

## What We Adopt

- `solana-verify build`
- program-specific `--library-name`
- exact artifact preservation
- `get-executable-hash`
- `get-program-hash`
- pinned `verify-from-repo`
- `--mount-path` for nested workspaces
- verification-data/PDA workflow
- `remote submit-job` for approved mainnet public verification
- multisig-aware verification flow

## What We Do Not Adopt Blindly

- unpinned CLI versions in production;
- a forced Anchor migration;
- automatic mainnet deployment;
- automatic authority changes;
- automatic signing;
- claims that verified builds equal a security audit;
- deprecated `verify-from-repo --remote`.

## Required Release Sequence

### A. Preflight

Capture:

```text
repo SHA
network
program ID
program library name
workspace root
mount path
upgrade authority / multisig public key
solana-verify version
```

Require Docker, Cargo, lockfile, and passing normal tests.

For programs that do not expose a Solana version through the dependencies the verifier inspects (for example some SDK v3 / Pinocchio setups), explicitly configure the CLI version in the root workspace metadata when required by the current upstream tool:

```toml
[workspace.metadata.cli]
solana = "<PINNED_SOLANA_CLI_VERSION>"
```

Do not invent this value. Derive it from the repository's actual supported toolchain.

### B. Build

```bash
solana-verify build --library-name "$PROGRAM_LIB_NAME"
```

Then:

```bash
solana-verify get-executable-hash \
  "target/deploy/${PROGRAM_LIB_NAME}.so"
```

Also record a normal SHA-256 checksum for artifact storage/provenance.

### C. Preserve

Upload the exact `.so` as an immutable CI artifact.

**Never run a later build command that overwrites the deployable `.so`.**

### D. Deploy

Deploy the preserved artifact only.

### E. Compare

```bash
solana-verify get-program-hash \
  -u "$NETWORK_URL" \
  "$PROGRAM_ID"
```

Executable hash must equal onchain program hash.

Mismatch = release blocked.

### F. Verify Repository

```bash
solana-verify verify-from-repo \
  -u "$NETWORK_URL" \
  --program-id "$PROGRAM_ID" \
  "$PUBLIC_REPO_URL" \
  --commit-hash "$COMMIT_SHA" \
  --library-name "$PROGRAM_LIB_NAME" \
  --mount-path "$MOUNT_PATH"
```

### G. Remote Mainnet Verification

After approved verification data/PDA upload by the correct authority:

```bash
solana-verify remote submit-job \
  --program-id "$PROGRAM_ID" \
  --uploader "$UPLOADER_PUBKEY"
```

Track the returned job ID and record final status.

## Multi-Program Workspaces

Do not assume package name equals library name.

For each deployable program, keep separate metadata:

```yaml
programs:
  - library: ppv_core
    program_id: ...
    mount_path: ...
  - library: ppv_commerce
    program_id: ...
    mount_path: ...
```

Build, preserve, hash, and verify each artifact independently.

## Public vs Private Repositories

Trustless repository verification requires public source.

If GwapOS has a private program repository:
- internal deterministic build controls may still be useful;
- artifact hashes may still be compared;
- do not describe it as publicly source-verified.

## Mainnet / Devnet Distinction

Local/devnet:
- deterministic build
- exact artifact deploy
- local hash comparison
- pinned repository verification where supported
- no claim of remote mainnet verification

Mainnet:
- all of the above
- approved authority/multisig verification-data flow
- remote verification submission
- status tracking

## Multisig

For multisig-controlled upgrade authority:
- verify locally before exporting/submitting authority-controlled verification transactions;
- inspect the exported transaction;
- ensure only intended verification-related instructions are present;
- route approval through the existing multisig process;
- never replace a multisig with a hot-key flow for convenience.

## Upstream Caveat

The reviewed upstream README states that build images are selected by pinned digest and Solana/Agave installer scripts in generated Dockerfiles are checksum-pinned, while post-install verification of installed toolchain/platform-tools remains follow-up work.

Therefore GwapOS treats verified builds as a major provenance improvement, not an absolute guarantee of every build-system component.

## Re-review Triggers

Re-review this module when:
- `solana-verify` releases a new production version used by GwapOS;
- Solana changes the verification PDA/API workflow;
- remote verification expands beyond mainnet;
- the deprecated flag behavior changes;
- GwapOS upgrades Solana/Agave, Anchor, or Rust;
- reproducibility unexpectedly fails.
