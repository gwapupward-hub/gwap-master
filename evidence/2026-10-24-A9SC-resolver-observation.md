# A9SC resolver observation, 2026-10-24

**Owner:** GNS. **Decision:** GWAP-GNS-001. Read-only HTTPS requests to the public backend; no key, signer or transaction was used.

## What was asked

Whether the live backend resolves a name that exists on the A9SC program, after GNS-decent-deploy PR #81 made the resolver fall through to the chain on an index miss. The test name is `vfye6gghqie.gwap`, registered by the verifier on 2026-10-15 (GNS `memory/deploy-history.md`). On that date, before PR #81, the backend returned `found: false` for it.

## Observations

`GET https://gns-backend-zh4o.onrender.com/api/config`, 2026-10-24T09:12:01Z:

```text
program_id A9SCN6tgaoAEorFzY5ZPinruk8LCttmrAEU9JoAmUKUH, network devnet, protocol_version 2,
name_policy 0, emoji_enabled false, fee_lamports 10000000,
resolution_tiers ["cache", "index", "chain"]
```

`GET https://gns-backend-zh4o.onrender.com/api/v2/resolve/vfye6gghqie.gwap`:

| UTC time | HTTP | Result |
|---|---|---|
| 2026-10-24T09:12:01Z | none | Client timeout after 30 s, no bytes received. Not diagnosed. The `/api/config` request right after it answered at once. |
| 2026-10-24T09:12:37Z | 200 | `found: true`, `source: "chain"`, `latency_ms` 413.9, owner and target `5DhdwqCjYUWQEMALGd7cUWHnHWNxV8z1q9LpzRFJ5orJ`, PDA `4hWvvFdhWEfyFPVSWGDNL8ypMr2ggKuVPyhHG8eHpqns`, `stale: false` |
| 2026-10-24T09:12:38Z | 200 | Same record, `source: "cache"`, `latency_ms` 0.03 |

The owner matches the verifier's throwaway payer recorded in GNS `memory/deploy-history.md`.

## Claim boundary

This shows that the V2 resolver answers an index miss from the chain on the live backend. It says nothing about the V1 `/api/resolve`, which is still Mongo-only, or about names that exist only in Mongo (see GWAP-GNS-001 implementation). The first request's timeout is unexplained; one observation does not establish availability.
