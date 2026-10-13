# Module: AI Engineering From Scratch

**Source:** https://github.com/rohitg00/ai-engineering-from-scratch  
**Reviewed:** 2026-09-29  
**Pinned commit:** `1bafaa88bb4668356791150bec3a6d7df38387eb`  
**Trust tier:** T3_SPECIALIST  
**License:** MIT  
**Integration pattern:** REFERENCE_ONLY + ENGINEERING_PATTERNS  
**GwapOS status:** ADOPTED_REFERENCE

## Why This Source Is Useful

This repository is a broad, actively maintained AI-engineering curriculum covering foundations through production systems, including:

- LLM engineering;
- RAG and retrieval;
- tools and function calling;
- Model Context Protocol (MCP);
- Agent Skills;
- agent architecture;
- security and prompt-injection defense;
- evaluation and regression testing;
- observability;
- production operations;
- Python, TypeScript, Rust, and Julia examples.

Its highest value to GwapOS is not as a runtime dependency. It is a source of engineering patterns for building AI features that are testable, observable, bounded, and releasable.

## Trust Decision

This is not a canonical protocol specification or vendor framework. It is an individual-maintained educational repository, even though it is popular and actively maintained.

Therefore:

- use it as a specialist reference;
- verify protocol claims against official protocol/vendor documentation;
- never treat lesson-specific thresholds as universal production standards;
- do not install its course tooling into GwapOS production;
- do not import demonstrated provider SDKs or frameworks unless separately justified.

## Cross-Cutting Patterns Adopted by GwapOS

### 1. Outcome before output

Before implementing an AI feature, define:

- the user outcome;
- what evidence proves the outcome;
- the artifact or state transition that must exist;
- what failure looks like;
- what must remain out of scope.

Do not begin with "add an agent," "add RAG," or "add AI." Begin with the job to be done.

### 2. Artifact contract before prose

For AI workflows and skills, define the observable contract first:

- required outputs;
- required fields;
- evidence;
- allowable states;
- forbidden side effects;
- failure behavior;
- approval boundaries.

Then design prompts, tools, and orchestration to satisfy that contract.

### 3. Separate model judgment from deterministic work

Use model judgment for:

- classification;
- prioritization;
- synthesis;
- ambiguity;
- language;
- open-ended reasoning.

Use deterministic code/tools for:

- parsing;
- schema validation;
- counting;
- hashing;
- typed API calls;
- invariant checks;
- permissions;
- authorization;
- state transitions;
- reproducible transforms.

Do not make the model "pretend" to execute deterministic validation.

### 4. Tool contracts are security boundaries

Every tool should have:

- a narrow purpose;
- typed input;
- typed output;
- explicit failure states;
- explicit side-effect classification;
- least privilege;
- bounded execution;
- idempotency or compensation when retried.

State-changing tools should support plan/preview where practical and require approval when impact warrants it.

### 5. Treat retrieved/tool content as untrusted data

Web pages, emails, documents, issue text, API payloads, tool outputs, RAG chunks, and third-party content may contain instructions.

GwapOS agents must distinguish:

- trusted instructions;
- user content;
- retrieved evidence;
- tool output;
- external untrusted instructions.

Untrusted content must not silently become control flow.

Prompt filtering alone is not treated as complete containment. Permission boundaries, tool policy, approval gates, and verification are separate controls.

### 6. Evaluation is a release discipline

AI features require evals appropriate to their failure modes.

Use separate layers for:

- deterministic unit tests;
- integration tests;
- end-to-end tests;
- behavioral evals;
- safety evals;
- cost/latency checks;
- regression comparisons.

A trace explains what happened. An eval determines whether the behavior was acceptable.

### 7. Compare against a baseline

For material AI changes, compare:

```text
baseline = current prompt/model/tooling/workflow
treatment = proposed change
```

Hold everything else constant where practical.

Do not approve a change solely because aggregate quality improves if a high-risk or critical task regresses.

### 8. Preserve uncertainty

Model-driven behavior is probabilistic.

For important workflows:
- repeat representative cases;
- preserve individual traces;
- report per-case regressions;
- separate averages from failure classes;
- keep safety-critical cases as hard gates where appropriate.

### 9. RAG must be evaluated as two systems

Separate:

1. retrieval quality;
2. generation quality.

A correct answer cannot prove retrieval is healthy, and strong retrieval cannot prove the generator stayed faithful to evidence.

Relevant checks may include:
- context precision/recall;
- answer relevance;
- faithfulness;
- citation/evidence correctness;
- stale-data handling;
- authorization boundaries.

### 10. Observability is required for production AI

Capture enough metadata to diagnose behavior without leaking sensitive data.

Where applicable record:
- feature/workflow version;
- model/provider identifier;
- prompt/template version;
- tool calls;
- tool outcomes;
- retrieval identifiers;
- latency;
- token usage;
- estimated/actual cost;
- retries;
- failure class;
- final state;
- redacted trace/evidence ID.

Never log secrets, raw private keys, or sensitive content unnecessarily.

### 11. Model/provider choice remains replaceable

Do not let a single lesson or SDK hardwire GwapOS architecture to one provider.

Prefer:
- explicit provider interfaces;
- structured output schemas;
- feature flags/configuration;
- eval-backed model changes;
- graceful fallback when justified.

### 12. Skills are software packages

A GwapOS skill is not finished because `SKILL.md` reads well.

It should be checked across distinct layers:
- package structure;
- trigger/routing behavior;
- task/artifact behavior;
- deterministic script correctness;
- safety/authority;
- packaging/portability.

See `references/AI_AGENT_RELEASE_GATE.md`.

## What We Explicitly Do Not Adopt Automatically

- the repository's entire 20-phase curriculum;
- its Python requirements;
- lesson-specific model names;
- specific LLM providers;
- promptfoo, DeepEval, RAGAS, or any other eval dependency;
- MCP behavior unless confirmed against the current official MCP specification;
- security claims unless corroborated by authoritative sources;
- numeric thresholds presented as teaching examples;
- generated skills without GwapOS repository-specific evals.

## GwapOS Use Cases

This module should inform work on:

- Daily Ideas AI workflows;
- GwapOS Builder;
- research/validation agents;
- internal coding/engineering agents;
- future MCP servers;
- future plugin/tool integrations;
- agent routing;
- AI feature release criteria;
- skill packaging and evolution.

## Re-review Triggers

Re-review when:

- the source materially changes its agent/skills methodology;
- official MCP or agent-skill standards conflict with the referenced lesson;
- GwapOS adds a production RAG system;
- GwapOS introduces autonomous state-changing agents;
- the skill runtime changes;
- the current source commit becomes stale relative to material lessons we rely on.
