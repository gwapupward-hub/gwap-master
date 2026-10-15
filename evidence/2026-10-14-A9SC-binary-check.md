# A9SC binary check, 2026-10-14

Scope: compares the deployed devnet program `A9SCN6tgaoAEorFzY5ZPinruk8LCttmrAEU9JoAmUKUH` with local builds of the GNS repo. No binary is committed here; only hashes.

Method:
- On-chain bytes: `solana program dump` against the devnet RPC (read-only; throwaway signer, not a project key).
- Local builds: `cargo-build-sbf` from Solana CLI 1.18.26 (platform-tools v1.41), anchor-lang 0.30.1, repo commit `cc1ff12` on branch `chore/vercel-render-only`.
- The solana-verify (Docker) build could not run here: Docker Hub pulls are blocked.

| Artifact | Bytes | sha256 (raw) | sha256 (trailing zeros stripped) |
|---|---|---|---|
| Deployed program data, A9SC | 571,816 | `1c9d70e441733e7cb965fd460d28587b000222aed34769c0d46be5af4940fcc2` | `03423a501a9d6ee06faaf3d2bf4a1232936e00c7214f87e209953162ec3ba8f4` |
| Local build of `cc1ff12` (declare_id 6cDC, as committed) | 565,144 | `a298548714b3f2792f7ee066622ca8c9807e6448a2a9ba83ffbe4e766011ab17` | `fbc782e50d4f24a5a519650e176bec15733fcff97f55f0363017113887cbe237` |
| Local build of `cc1ff12` with declare_id A9SC (scratch copy, not committed) | 565,144 | `e413364995dbf7d250961ada03a532581b7589a557b242b10b3e906f879f3b3b` | not computed |

Findings:
1. The raw sha256 of the deployed program data equals the hash reported at deploy time (`1c9d70e…`). So the reported value is a hash of the on-chain bytes.
2. No local build reproduces the deployed bytes. The deployed program is 6,672 bytes larger than a local build of the same source tree.
3. Changing only the declared program ID does not close the gap. The rebuilt size is unchanged, and the hash differs from the deployed one.
4. Possible causes, not tested: the deploy used a different source state, a different toolchain (Anchor or Solana version), or different build flags. The deploy-time build inputs are not in this environment.
5. Status: the A9SC deployment is confirmed as on-chain bytes. It is not confirmed as a reproduced build. Under the release-integrity model, that is "unknown," so no upgrade of A9SC should proceed until a build reproduces the on-chain hash, or the founder accepts the gap in writing.

Vercel observation, read-only, 2026-10-14:
- Project `gns-decent-deploy-xfb6` (`prj_RWkuUM7vOQVogav1yvARznWfstyE`, team `team_xvb1UDdhTBcED6EwtcISP72S`) is attached to `gwapspot.fun` (verified) and `www.gwapspot.fun` (307 to the apex).
- Latest deployment `dpl_BFw5CNCWcKcR5Q6bDttzfi7W33PS` is READY, with `target` null. That usually means a preview build, not a production promotion. Not confirmed.
- SSO protection is on for all deployments except custom domains.
- The project API response did not include the root directory or linked Git repo. Not checked yet.
- Implication: `gwapspot.fun` points at this project, so any DNS or domain change is founder-gated.

Next steps, in order:
1. Find the deploy-time build inputs (the build log, or the source commit the deployer used). Compare them with `cc1ff12`.
2. Re-run the build in a container image that matches the deployer's toolchain, if one can be pulled.
3. Only after a hash match: upgrade A9SC (founder-held upgrade authority), then record the on-chain hash in `memory/deploy-history.md` and the release registry.
