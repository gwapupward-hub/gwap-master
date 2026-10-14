# Status report

Use the fields in this order. The source of the format is `systems/engineering-intelligence/SKILL.md`, Final Reporting Format.

```text
STATUS=READY | NOT_READY | BLOCKED
SCOPE=<what changed>
REPO_SHA=<commit>
UPSTREAM_SOURCE=<repo and pinned tag or SHA, or N/A>
NETWORK=<localnet | devnet | mainnet | N/A>
PROGRAM_ID=<id or N/A>
PROGRAM_LIB=<library or N/A>
ARTIFACT=<path or N/A>
ARTIFACT_SHA256=<hash or N/A>
EXECUTABLE_HASH=<hash or N/A>
ONCHAIN_HASH=<hash or N/A>
HASH_MATCH=yes | no | N/A
PUBLIC_VERIFICATION=verified | submitted | local-only | not-applicable | not-run
TESTS=<commands and results>
SECURITY_GATES=<what was checked and the result>
BLOCKERS=<none, or exact blockers>
NEXT=<one next action>
```

Rules:
- Claims use the precise terms: `tested locally`, `verified on devnet`, `hash matched`, `remote verification submitted`, `remote verification confirmed`.
- Any unknown, skipped, or contradictory gate means NOT_READY.
- A HALT-class action without approval means BLOCKED.
