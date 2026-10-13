# GwapOS AI / Agent / Skill Release Gate

Use this gate for production AI features, agents, tool-using workflows, RAG systems, and reusable GwapOS skills.

Not every project needs every item. High-risk workflows require stronger evidence, not weaker standards.

## 1. Outcome Contract

Before implementation, define:

```text
USER_OUTCOME=
ARTIFACT_OR_STATE=
SUCCESS_EVIDENCE=
FAILURE_BEHAVIOR=
FORBIDDEN_SIDE_EFFECTS=
APPROVAL_BOUNDARIES=
```

A feature without an observable success condition is not ready to implement.

## 2. Architecture Boundary

Document:

- model judgment responsibilities;
- deterministic code responsibilities;
- data sources;
- trust boundaries;
- tool permissions;
- state-changing actions;
- retry/idempotency strategy;
- human approval points.

## 3. Structured Contracts

For tools and model outputs:

- typed/schema-validated inputs;
- typed/schema-validated outputs where practical;
- explicit errors;
- explicit timeouts;
- bounded retries;
- no silent coercion of dangerous values.

## 4. Evaluation Set

Create representative cases before final tuning.

Include:

- normal expected cases;
- paraphrases/variants;
- edge cases;
- near misses;
- malformed input;
- unavailable dependencies;
- adversarial/untrusted content;
- unauthorized action requests;
- failure/recovery cases.

For skills, also include:

- positive trigger cases;
- clear negatives;
- neighboring/near-miss requests;
- competing-skill requests;
- adversarial naming/keyword cases.

## 5. Baseline vs Treatment

Record:

```text
BASELINE_VERSION=
TREATMENT_VERSION=
MODEL=
TOOLS=
DATASET_VERSION=
SAMPLING_POLICY=
BUDGET=
```

Run the same cases under both conditions where possible.

Report per-case regressions, not just the overall average.

## 6. Quality Dimensions

Choose explicit dimensions appropriate to the workflow:

- factual correctness;
- completeness;
- evidence/citation quality;
- faithfulness to retrieved context;
- task completion;
- final-state correctness;
- tool trajectory;
- safety;
- authorization;
- latency;
- token/cost budget;
- user correction burden.

## 7. RAG Gate

If retrieval is involved, evaluate separately:

### Retrieval
- relevant evidence found;
- unauthorized evidence excluded;
- stale evidence handled;
- duplicates/noise controlled;
- source identity preserved.

### Generation
- answer supported by retrieved evidence;
- uncertainty stated when evidence is insufficient;
- citations/evidence point to the correct source;
- no unsupported fabrication.

## 8. Agent / Tool Safety Gate

Required checks where applicable:

- retrieved content cannot grant itself authority;
- tool outputs are treated as data, not instructions;
- secrets are not exposed;
- least privilege is enforced;
- destructive/external actions require correct approval;
- path/workspace boundaries are enforced;
- retry cannot duplicate irreversible side effects;
- tool timeouts and cancellation are handled;
- failure stops safely.

## 9. Observability Gate

Production execution should make failures diagnosable.

Record redacted:

- workflow/version;
- model/provider;
- prompt/template version;
- tool calls and status;
- retrieval IDs;
- latency;
- tokens/cost;
- retry count;
- final state;
- error/failure class;
- trace/evidence identifier.


## Security Scanner Gate

For releasable Agent Skills, run the pinned NVIDIA SkillSpector static scan before final release evaluation.

Required GwapOS verdict:
- execution successful;
- analysis complete;
- recommendation `SAFE`.

`CAUTION` requires triage and rescan. `DO_NOT_INSTALL`, incomplete analysis, scanner errors, or malformed reports block.

SkillSpector is a security-analysis layer, not a substitute for the six-layer skill evaluation below.

## 10. Skill-Specific Six-Layer Gate

### Layer A — Package
- package structure valid;
- references resolve;
- no unexpected executable/symlink/special files;
- manifest/version present when required.

### Layer B — Routing
- intended requests trigger;
- clear negatives do not;
- near misses define boundaries;
- conflicting skills are tested.

### Layer C — Behavior
- required artifact/state produced;
- evidence is valid;
- prohibited actions untouched;
- treatment is not worse than baseline on critical cases.

### Layer D — Scripts
- normal, empty, malformed, repeated, timeout, and partial-state cases;
- deterministic exit/error behavior;
- read-only/dry-run mode where appropriate.

### Layer E — Safety
- malicious input;
- untrusted retrieved instructions;
- undeclared destinations/resources;
- credential-dependent actions;
- destructive action without approval;
- duplicate side-effect recovery.

### Layer F — Portability
- required runtime capabilities documented;
- unsupported capabilities fail or degrade explicitly;
- installed package is tested, not only source tree;
- upgrade/uninstall behavior is defined when relevant.

## 11. Release Decision

Use:

```text
STATUS=READY | NOT_READY | BLOCKED
BASELINE=
TREATMENT=
EVAL_SET=
CRITICAL_CASES=
REGRESSIONS=
SAFETY=
LATENCY=
COST=
OBSERVABILITY=
APPROVALS=
BLOCKERS=
NEXT=
```

### Hard rules

- Unknown critical safety state => not READY.
- Unauthorized side effect => BLOCKED.
- Critical-case regression => NOT_READY unless explicitly reviewed and accepted.
- Aggregate score improvement cannot cancel a safety failure.
- Passing a deterministic fixture is not proof of production behavior.
