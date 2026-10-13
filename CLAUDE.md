# GWAP Master: agent instructions

This repository is the canonical decision and evidence layer for the GWAP ecosystem.

## Read first

1. `MASTER.md`: source-of-truth order, system map, and decision flow.
2. `registries/PRODUCT_TRUTH.yaml`: which system owns what.
3. `registries/DECISION_REGISTRY.yaml`: locked decisions. Do not contradict a `PRODUCTION` decision without a new decision record.
4. `runbooks/AGENT_WORKFLOWS.md`: how to route a task and which workflow to run.

## Hard rules

- No mainnet deployment, upgrade-authority change, custody activation, or automated mainnet spending without explicit founder approval.
- A signer is not an authorization system.
- External technology informs GWAP; it does not control it. Repo reality outranks upstream defaults.
- "Live" protocol claims need target-cluster evidence. Accepted is not implemented, and implemented is not activated.
- Never print, commit, or log secrets.
- Executable third-party skills pass the SkillSpector gate before installation.

## Agent team

Subagents are defined in `.claude/agents/`:

- `gwap-lead`: routes the task and integrates results. Start here for anything beyond a single small edit.
- `gwap-solana`: Anchor/Rust programs and wallet transaction code.
- `gwap-backend`: services, Workers, bots, MCP server, data.
- `gwap-frontend`: Next.js, Tauri UI, wallet UX.
- `gwap-devops`: CI, releases, environments, verified builds.
- `gwap-reviewer`: read-only quality gate. Nothing is done until it returns PASS.

## Engineering intelligence

`systems/engineering-intelligence/SKILL.md` is the senior engineering gate. It covers Solana release integrity, the AI release gate, the trust policy, and the final report format.

It is not yet installed at `.claude/skills/gwapos-engineering-intelligence/`. That install is gated by its own implementation prompt and the SkillSpector scan. Until then, read it directly from its path.

## Commands

No build or test commands are defined yet for this repository. Add them here when a product repository lands.
