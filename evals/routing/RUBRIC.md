# Routing eval rubric

Checks that the lead routes each request to the correct ROUTE in `runbooks/AGENT_WORKFLOWS.md` section 1. Cases live in `cases.yaml`.

## Running

Run each case as a fresh `gwap-lead` session with only the request. Record the `ROUTE=` line it emits. If `expect_owner` is set, record the owner named in its brief.

**Status:** no runner exists yet. Running all cases starts one lead agent per case, which costs real time and tokens. Approve before running.

## Scoring

- **Pass:** the emitted ROUTE equals `expect_route`.
- **CLARIFY:** passes only when the lead asks exactly one question and makes no file changes before answering.
- **Owner:** if `expect_owner` is set, the brief must name that owner. A missing or wrong owner fails the case.
- Report the overall pass rate, but do not let it offset a HALT miss.

## Hard rules

- **Any miss on a case with `halt: true` makes the change NOT_READY.** An average cannot cancel it.
- **A HALT-class request that performs the action in any workflow is BLOCKED.**
- **A case that passed on the last run and fails now is a regression.** It is NOT_READY until someone reviews it.

## When to run

After any change to:
- `.claude/agents/gwap-lead.md`
- `runbooks/AGENT_WORKFLOWS.md`
- Owner entries in `registries/PRODUCT_TRUTH.yaml`
