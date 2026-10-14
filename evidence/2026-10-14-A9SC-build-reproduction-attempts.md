# A9SC source-to-deployed binary reproduction attempts — 2026-10-14

**Workflow / owner:** S (release-integrity investigation only) / **GNS**. This is evidence only: no source, configuration, account, authority, PR, deployment, or external-resource change was made. It implements the B gate in `lead-brief.md` and is governed by `GWAP-GNS-001` (PILOT).

## Result and claim boundary

**A job-owned, isolated source build at `d95efbf5f95179eaf9bf89d58abe67ca06db10ec` reproduces the observed deployed devnet ProgramData bytes exactly.** Its `gwap_names.so` is 571,816 bytes with raw SHA-256 `1c9d70e441733e7cb965fd460d28587b000222aed34769c0d46be5af4940fcc2`; this equals the unsigned public-RPC ProgramData extraction. The trailing-zero-stripped hash also equals `03423a501a9d6ee06faaf3d2bf4a1232936e00c7214f87e209953162ec3ba8f4`.

The one permitted CI-provenance tie-breaker, PR #77 merge pseudo-commit `ffdb2d5a656755b1a6dad66553bce1963c8c6bc9`, independently reproduced the same bytes. The `cc1ff123c0b0122b873ad64388c036bfb5804379` baseline did **not** reproduce them.

> This is a **source-build raw-byte hash match**, not authorization to deploy, upgrade, use an authority, submit remote verification, or begin C. B remains **NOT_READY** until an independent `gwap-reviewer` returns **PASS**.

## Frozen target and controls

| Field | Frozen value / evidence |
|---|---|
| Governance checkout at start | `de593044d103eeadb1c71f4b5aefaeb6a4f030dd`, branch `docs/record-fresh-start-decisions`, clean before this evidence file was created |
| GNS owner / target program | GNS; `A9SCN6tgaoAEorFzY5ZPinruk8LCttmrAEU9JoAmUKUH` on **devnet** |
| Program library / workspace | `gwap_names`; mount/workspace path `programs` |
| Target ProgramData account | `qtpT6S2Ntw9VYBnXrjBf8XUG83wmM54TFtHyAQCz2q4` |
| Public deployment transaction | [`5XS977E8UWHLwfZn5ZopmMjUGmAX2cmCsJsd5EzKuP4A3WrfiM7da66e9ovBjc3EeHt8XrNLrgQRfroxLQK16pme`](https://explorer.solana.com/tx/5XS977E8UWHLwfZn5ZopmMjUGmAX2cmCsJsd5EzKuP4A3WrfiM7da66e9ovBjc3EeHt8XrNLrgQRfroxLQK16pme?cluster=devnet) |
| Public RPC observation | `https://api.devnet.solana.com`, unsigned `getTransaction` and `getAccountInfo` only, captured 2026-10-14T23:28:24Z |
| Transaction evidence | Slot `511059525`, block time `2026-10-14T17:17:24Z`, `meta.err = null`; instruction 0 is System `createAccount`, instruction 1 is upgradeable-loader `deployWithMaxDataLen`; log: `Deployed program A9SC...` |
| ProgramData comparison method | Decode account base64; upgradeable-loader ProgramData bytecode begins at offset 45 (4-byte discriminant + 8-byte slot + 1-byte COption + 32-byte authority). Hash byte range `[45:]`; account size 571,861, program bytes 571,816, stripped length 571,801. |
| Observed deployed raw SHA-256 | `1c9d70e441733e7cb965fd460d28587b000222aed34769c0d46be5af4940fcc2` (571,816 bytes) |
| Observed deployed trailing-zero-stripped SHA-256 | `03423a501a9d6ee06faaf3d2bf4a1232936e00c7214f87e209953162ec3ba8f4` (571,801 bytes) |
| Upgrade authority | Not read or used. No signer, `~/.config/solana/**`, keypair, or secret was accessed. |

The retained job-local public-RPC inputs are `/home/ubuntu/jobs/job_Z3RVQV9k/rpc/getTransaction.json`, `getAccountInfo.json`, and `public-deployment-summary.json`. The concise instruction/log extraction is `/home/ubuntu/jobs/job_Z3RVQV9k/rpc/public-transaction-instruction-summary.txt`.

## Candidate provenance and clean isolation

At 2026-10-14T23:28:02Z, both required source commits existed and were confirmed non-ancestral in both directions:

- `cc1ff123c0b0122b873ad64388c036bfb5804379` (the supplied clean detached GNS checkout)
- `d95efbf5f95179eaf9bf89d58abe67ca06db10ec` (the supplied clean detached reset worktree)

`d95efbf` was **not reset into or checked out in** the shared `cc1ff12` worktree. Instead, job-owned, detached/isolated source copies were created under `/home/ubuntu/jobs/job_Z3RVQV9k/sources/`. Initial clean-tree and final clean-tree records are in:

- `/home/ubuntu/jobs/job_Z3RVQV9k/sources/job-owned-source-freeze.txt`
- `/home/ubuntu/jobs/job_Z3RVQV9k/logs/final-integrity-checks.txt`

The shared inputs remained clean after all job-owned builds:

- `/home/ubuntu/continuation/gns-cc1ff12` at `cc1ff123c0b0122b873ad64388c036bfb5804379`
- `/home/ubuntu/worktrees/gns-reset-d95efbf` at `d95efbf5f95179eaf9bf89d58abe67ca06db10ec`

## Exact source build inputs

The following are SHA-256 hashes of the exact input files exported from the named commit before the build (the program `Cargo.toml` is included in addition to the required `Anchor.toml`, workspace `Cargo.lock`, and CI workflow):

| Candidate | `programs/Anchor.toml` | `programs/gwap_names/Cargo.toml` | `programs/Cargo.lock` | `.github/workflows/program-build.yml` |
|---|---|---|---|---|
| `cc1ff123c0b0122b873ad64388c036bfb5804379` | `a15a336148c94e7132124ff75081d5f2a5d10f5c390e826b3d408f0416412923` | `516ae86c1a6521f5163d3b9bd12d18281e41e6fd5d0b179593d9ba3d619b03c4` | `4c96a4140d124295ed3a3a8b3dad94d9213484539358b64bb7828c0fd40b9b20` | `3161c9fdde3ed3ce20dc35e17bd174ef1efbb3a219cedfa609d2e32943ef402b` |
| `d95efbf5f95179eaf9bf89d58abe67ca06db10ec` | `fe6a1f6480faee81f812702b7ce3bb5ef1c3c0f42cf6bb86bcaa3196d9cf3016` | `516ae86c1a6521f5163d3b9bd12d18281e41e6fd5d0b179593d9ba3d619b03c4` | `4c96a4140d124295ed3a3a8b3dad94d9213484539358b64bb7828c0fd40b9b20` | `db23db5206ca11de66dfe12311dd04ded938b2155a2467c6c4d3050568df1e7b` |
| `ffdb2d5a656755b1a6dad66553bce1963c8c6bc9` (tie-breaker) | `fe6a1f6480faee81f812702b7ce3bb5ef1c3c0f42cf6bb86bcaa3196d9cf3016` | `516ae86c1a6521f5163d3b9bd12d18281e41e6fd5d0b179593d9ba3d619b03c4` | `4c96a4140d124295ed3a3a8b3dad94d9213484539358b64bb7828c0fd40b9b20` | `db23db5206ca11de66dfe12311dd04ded938b2155a2467c6c4d3050568df1e7b` |

Relevant inspected values were:

- All three `Anchor.toml` files pin `anchor_version = "0.30.1"`; all program manifests require `anchor-lang 0.30.1` with `init-if-needed`.
- All three lockfiles resolve `anchor-lang`/`anchor-syn` `0.30.1` and `solana-program`/`solana-frozen-abi` `1.18.26`.
- `cc1ff12` configures both localnet and devnet `gwap_names` as legacy `6cDCrNYmasd1qmnvdLf8jyt9iFa3jW9VLzJhrb7X7SEH`; the reset commit and its CI merge configure both as A9SC.
- The baseline workflow sets `PROGRAM_ID` to 6cDC and uses `--bpf-program`; the reset/tie-breaker workflow sets it to A9SC and uses `--upgradeable-program`. All workflows pin `SOLANA_VERSION: "1.18.26"`, invoke `cargo-build-sbf --manifest-path gwap_names/Cargo.toml --sbf-out-dir target/deploy` from `programs`, calculate `sha256sum`, and upload the `.so` plus hash file.

Frozen file copies and their checksum records are job-local at `/home/ubuntu/jobs/job_Z3RVQV9k/inputs/` (`SHA256SUMS.txt`, `program-Cargo.toml-SHA256SUMS.txt`, and `input-version-summary.txt`).

## Tool preflight and Anchor requirement

Preflight at 2026-10-14T23:28:02Z used absolute paths and succeeded:

```text
/home/ubuntu/.avm/bin/anchor-0.30.1 --version
anchor-cli 0.30.1

/home/ubuntu/.cargo/bin/cargo --version
cargo 1.99.0 (5f94df478 2026-08-27)

/home/ubuntu/.cargo/bin/rustc --version
rustc 1.99.0 (b940084d7 2026-09-28)

/home/ubuntu/.local/share/solana/install/active_release/bin/solana --version
solana-cli 1.18.26 (src:c2b35002; feat:3241752014, client:Agave)

/home/ubuntu/.local/share/solana/install/active_release/bin/cargo-build-sbf --version
solana-cargo-build-sbf 1.18.26
platform-tools v1.41
rustc 1.75.0
```

The mandatory-install fallback was **not invoked**: the exact, requested Anchor 0.30.1 executable was present and usable at the parent-supplied absolute path. Therefore running `cargo install --git https://github.com/coral-xyz/anchor --tag v0.30.1 anchor-cli --locked` would have been a redundant installation, contrary to the task direction to reuse the installed matching Anchor. No alternative Anchor version or installer was used.

Full preflight record: `/home/ubuntu/jobs/job_Z3RVQV9k/logs/freeze-and-tool-preflight.txt`.

## Public GitHub Actions provenance

Both named GitHub Actions runs are successful `pull_request` executions for PR #77, but their `headSha` is **not** the source actually checked out by `actions/checkout@v4`. The build logs show the true checkout SHA and each downloaded CI artifact contains the raw-hash-matching `gwap_names.so`.

| Run | Public run facts | API `headSha` | Actual CI checkout from build log | Artifact / outcome |
|---|---|---|---|---|
| [`38593918475`](https://github.com/gwapupward-hub/GNS-decent-deploy/actions/runs/38593918475) | Created 2026-10-14T15:57:36Z; conclusion `success`; workflow `Program build` | `3e31a74439f92fa47cdc895c8b841815c54d56ef` | `56aa264685925eb3050ea47e0c6828cfb92340f2`, a PR-merge pseudo-commit with parents `cc5d9b6d34b58ceb4854c1a993a18575c2afbfce` and `3e31a74439f92fa47cdc895c8b841815c54d56ef` | `gwap_names-sbf-56aa264685925eb3050ea47e0c6828cfb92340f2`; CI logged raw SHA-256 `1c9d70e...`; downloaded binary is 571,816 bytes and has that same raw hash. |
| [`38598151830`](https://github.com/gwapupward-hub/GNS-decent-deploy/actions/runs/38598151830) | Created 2026-10-14T16:26:56Z; conclusion `success`; workflow `Program build` | `d95efbf5f95179eaf9bf89d58abe67ca06db10ec` | `ffdb2d5a656755b1a6dad66553bce1963c8c6bc9`, a PR-merge pseudo-commit with parents `cc5d9b6d34b58ceb4854c1a993a18575c2afbfce` and `d95efbf5f95179eaf9bf89d58abe67ca06db10ec` | `gwap_names-sbf-ffdb2d5a656755b1a6dad66553bce1963c8c6bc9`; CI logged raw SHA-256 `1c9d70e...`; downloaded binary is 571,816 bytes and has that same raw hash. |

Run 38598151830’s merge pseudo-commit was selected as the **single provenance-backed tie-breaker** because it is the actual CI checkout for the required reset candidate `d95efbf`. It was fetched directly into a job-owned detached repository, then built locally. Run 38593918475’s separate pseudo-commit `56aa264...` was not built locally: the bounded investigation performed exactly the required baseline build, the requested reset build, and one CI-checkout tie-breaker. Its published CI artifact was nevertheless downloaded and byte-compared as independent provenance.

The logs show `cargo-build-sbf` at the CI-equivalent command, recorded its raw SHA, and recorded 11 local-validator checks passed / 0 failed in each run. Public metadata, logs, downloaded artifacts, and checksum evidence are retained outside governance at `/home/ubuntu/jobs/job_Z3RVQV9k/ci/`; the key checkout extracts are `run-38593918475-provenance-extract.txt` and `run-38598151830-provenance-extract.txt`.

## Bounded local build attempts

Every local build used only a job-owned source directory and the CI-equivalent command below, from that directory’s `programs` subdirectory:

```bash
PATH=/home/ubuntu/.cargo/bin:/home/ubuntu/.local/share/solana/install/active_release/bin:/usr/bin:/bin \
  /home/ubuntu/.local/share/solana/install/active_release/bin/cargo-build-sbf \
  --manifest-path gwap_names/Cargo.toml --sbf-out-dir target/deploy
```

| Attempt | UTC interval / exit | Isolated source | Output preserved outside governance | Bytes | Raw SHA-256 vs deployed | Trailing-zero-stripped SHA-256 vs deployed | Result |
|---|---|---|---|---:|---|---|---|
| 1 — required baseline | Started `2026-10-14T23:30:21Z`; exit 0 (compiler completed in 2m04s; log mtime `2026-10-14T23:32:32Z`) | `cc1ff123c0b0122b873ad64388c036bfb5804379`, clean | `/home/ubuntu/jobs/job_Z3RVQV9k/artifacts/cc1ff12/gwap_names.so` | 565,144 | `a298548714b3f2792f7ee066622ca8c9807e6448a2a9ba83ffbe4e766011ab17` — **different** | `fbc782e50d4f24a5a519650e176bec15733fcff97f55f0363017113887cbe237` — **different** | MISMATCH; no release claim from this baseline. |
| 2 — required reset candidate | `2026-10-14T23:32:48Z`–`2026-10-14T23:34:49Z`; exit 0 | `d95efbf5f95179eaf9bf89d58abe67ca06db10ec`, clean | `/home/ubuntu/jobs/job_Z3RVQV9k/artifacts/d95efbf/gwap_names.so` | 571,816 | `1c9d70e441733e7cb965fd460d28587b000222aed34769c0d46be5af4940fcc2` — **MATCH** | `03423a501a9d6ee06faaf3d2bf4a1232936e00c7214f87e209953162ec3ba8f4` — **MATCH** | **SOURCE-TO-DEPLOYED RAW-BYTE MATCH**. |
| 3 — single CI-merge tie-breaker | `2026-10-14T23:34:49Z`–`2026-10-14T23:36:54Z`; exit 0 | `ffdb2d5a656755b1a6dad66553bce1963c8c6bc9`, clean, job-owned detached fetch of PR #77 merge ref | `/home/ubuntu/jobs/job_Z3RVQV9k/artifacts/ffdb2d5/gwap_names.so` | 571,816 | `1c9d70e441733e7cb965fd460d28587b000222aed34769c0d46be5af4940fcc2` — **MATCH** | `03423a501a9d6ee06faaf3d2bf4a1232936e00c7214f87e209953162ec3ba8f4` — **MATCH** | **SOURCE-TO-DEPLOYED RAW-BYTE MATCH** and exact local reproduction of the reset CI checkout. |

The d95 and ffdb source-built binaries were byte-identical (`cmp -s`) to all three of: the preserved historical `/home/ubuntu/deploy-d95efbf/gwap_names.so`, the downloaded CI artifact for run 38593918475, and the downloaded CI artifact for run 38598151830. The cc1ff12 build was different from each. Full comparison evidence is `/home/ubuntu/jobs/job_Z3RVQV9k/logs/final-integrity-checks.txt`; per-attempt logs and both-form hash files are under `/home/ubuntu/jobs/job_Z3RVQV9k/logs/` and `/home/ubuntu/jobs/job_Z3RVQV9k/artifacts/`.

No binary or log was placed in the governance repository; this record stores only provenance, commands, paths, sizes, hashes, and results. No `solana-verify` remote action was run or submitted.

```text
STATUS=NOT_READY
SCOPE=B only — bounded devnet source-to-deployed binary reproduction evidence; no deployment or source change
REPO_SHA=governance de593044d103eeadb1c71f4b5aefaeb6a4f030dd; baseline cc1ff123c0b0122b873ad64388c036bfb5804379; reset d95efbf5f95179eaf9bf89d58abe67ca06db10ec; CI merge tie-breaker ffdb2d5a656755b1a6dad66553bce1963c8c6bc9
UPSTREAM_SOURCE=https://github.com/gwapupward-hub/GNS-decent-deploy; Actions runs 38593918475 (actual 56aa264685925eb3050ea47e0c6828cfb92340f2) and 38598151830 (actual ffdb2d5a656755b1a6dad66553bce1963c8c6bc9)
NETWORK=devnet read-only public JSON-RPC only
PROGRAM_ID=A9SCN6tgaoAEorFzY5ZPinruk8LCttmrAEU9JoAmUKUH
PROGRAM_LIB=gwap_names
ARTIFACT=/home/ubuntu/jobs/job_Z3RVQV9k/artifacts/d95efbf/gwap_names.so; corroborated by /home/ubuntu/jobs/job_Z3RVQV9k/artifacts/ffdb2d5/gwap_names.so
ARTIFACT_SHA256=1c9d70e441733e7cb965fd460d28587b000222aed34769c0d46be5af4940fcc2
EXECUTABLE_HASH=1c9d70e441733e7cb965fd460d28587b000222aed34769c0d46be5af4940fcc2 (raw source-build artifact SHA-256; solana-verify not run)
ONCHAIN_HASH=1c9d70e441733e7cb965fd460d28587b000222aed34769c0d46be5af4940fcc2 (raw ProgramData bytes, 571816 bytes); stripped=03423a501a9d6ee06faaf3d2bf4a1232936e00c7214f87e209953162ec3ba8f4
HASH_MATCH=yes (d95efbf and ffdb2d5 raw source-build bytes match observed devnet ProgramData; cc1ff12 does not)
PUBLIC_VERIFICATION=local-only; unsigned public RPC comparison and public CI artifact/log inspection; no remote submission
TESTS=three cargo-build-sbf attempts exited 0; public CI runs 38593918475 and 38598151830 succeeded and each recorded 11 local-validator checks passed, 0 failed; no local test suite rerun in this evidence-only B task
SECURITY_GATES=direct Anchor 0.30.1 preflight passed; absolute pinned tool paths used; no Anchor reinstall required; no keypair/config/secret read; no signer, transaction, deploy, authority, mainnet, account/config, DNS, or PR mutation; shared source worktrees remained clean
BLOCKERS=Independent gwap-reviewer PASS is pending. Until then B is NOT_READY and C–G remain held under the serial stop instruction.
NEXT=Have gwap-reviewer independently validate this record, the three job-local artifacts/logs, public-RPC method, and clean-state evidence; only a PASS may clear B for the lead.
```

## Independent adjudication — 2026-10-14T23:41:50Z

**gwap-reviewer verdict: PASS, scoped to B reproduction and A governance-sync facts.** The reviewer independently rehashed all local and CI artifacts, inspected source SHAs and clean worktrees, verified pinned input hashes and actual Actions checkout provenance, and fetched finalized ProgramData and the deployment transaction with unsigned public devnet RPC. Both `d95efbf` and `ffdb2d5` reproduce the deployed raw bytes. The intentionally nonmatching `cc1ff12` baseline remains a documented mismatch.

This supersedes the pending-review status recorded above: **B is cleared for draft-only C work**. It does not authorize any on-chain mutation, signing, upgrade, release, or PR readiness promotion. It is not a broad protocol security audit or a whole-PR #3 review. The duplicate `GWAP-OWN-004` records are preserved, not resolved. Review noted only the expected newly created untracked evidence file; it must be committed before a whole-PR audit.

```text
STATUS=READY (B evidence-only gate)
HASH_MATCH=yes (d95efbf and ffdb2d5; cc1ff12=no)
PUBLIC_VERIFICATION=local-only
TESTS=three successful local SBF builds; independent byte/hash comparisons and unsigned finalized devnet RPC; no local behavioral suite rerun under B
SECURITY_GATES=gwap-reviewer PASS; no project keys, chain writes, deployment, or external resource changes
BLOCKERS=none within scoped B; separate C/release gates still apply
NEXT=Prepare the program-ID consistency change as a draft PR, retaining deployed SPA-001 behavior and legacy history
```
