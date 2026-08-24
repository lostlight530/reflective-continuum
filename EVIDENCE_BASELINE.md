# 2026 Evidence Baseline

- Retrieval date: 2026-08-24
- Rule: primary/official sources bound implementation and claim language; they do not certify this repository

This baseline records public evidence semantics for the repository. It does not encode private prompts, hidden reasoning, unpublished maintenance strategy, or future artifact-production instructions.

## Repository implementation anchor

Current evidence claims are interpreted through the implementation that actually exists:

- `CODE/continuum_db.py` — versioned SQLite graph, foreign keys, external-content FTS5, savepoints, lexical search, snapshot digest
- `CODE/entropy_analyzer.py` — PageRank and Shannon entropy over graph-rank values
- `CODE/drift_detector.py` — structural delta, top-FTS-result change, rank delta
- `CODE/reflective_validator.py` — explicit local validation rules and standard-library import-root checking
- `CODE/cortex_observer.py` — transactional observation and bounded reflector loop
- `CODE/tasks/cortex_selfcheck.py` — connection-local database selfcheck
- `CODE/tasks/semantic_drift_audit.py` — declared-version structural and lexical-result comparison for caller-selected queries

External papers, standards, protocols, or SDK documentation remain `REFERENCE_ONLY` unless a corresponding repository implementation surface exists.

## Runtime and storage references

- [SQLite foreign-key documentation](https://www.sqlite.org/foreignkeys.html) states that applications must enable foreign-key enforcement per connection. `GraphDB` enables and verifies it on the connection it opens.
- [SQLite FTS5 external-content documentation](https://www.sqlite.org/fts5.html#external_content_tables) explains that the application must keep the content table and FTS index synchronized. `GraphDB` uses insert/delete/update triggers for this purpose.
- [SQLite in-memory database documentation](https://www.sqlite.org/inmemorydb.html) states that a bare `:memory:` database is private to the connection that opened it and disappears when the connection closes.

Python-version compatibility is revision-specific. A version may be described as verified only when relevant executable behavior was actually run in that environment and the result was retained for the reviewed revision.

## AI/agent claim boundaries

- [NIST AI 600-1](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence), updated 2026-04-08, is a voluntary generative-AI risk profile. It motivates lifecycle risk records; it does not validate a local “cognitive” architecture.
- [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) describes agentic risk classes. This repository is not a full agent tool/runtime boundary.
- [OpenAI’s 2026 third-party evaluation playbook](https://openai.com/index/trustworthy-third-party-evaluations-foundations/) emphasizes harness, tools, retries, scoring, budgets, and validity checks. Results remain scoped to the tested system.
- [Anthropic, Trustworthy agents in practice](https://www.anthropic.com/research/trustworthy-agents) treats layered safeguards as engineering controls rather than guarantees.
- [Anthropic’s 2026 constitution announcement](https://www.anthropic.com/news/claude-new-constitution) notes that model outputs may not always adhere to intended ideals. Prose policy is not an executable guarantee.
- [Google DeepMind AlphaEvolve](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/) is a design reference for evaluator-backed search, not deterministic cognition or universal convergence.

## 2026 state, protocol, and observability calibration

The following sources are `REFERENCE_ONLY`. They sharpen state and evidence vocabulary but do not add dependencies or prove that Reflective Continuum implements the referenced framework.

### Model Context Protocol 2026-07-28

- Primary release: https://blog.modelcontextprotocol.io/posts/2026-07-28/
- The named protocol version adopts a stateless protocol core and removes the previous required protocol-level initialization/session mechanism.
- The release does not require applications above that protocol core to be stateless.

Reflective use: protocol/session scope and application-state scope are different objects.

### A2A Protocol v1.0

- Specification: https://a2a-protocol.org/latest/specification/
- Stable release note: https://a2a-protocol.org/latest/announcing-1.0/
- A2A distinguishes Agent Cards, Tasks, Messages, Artifacts, Context, streaming/push mechanisms, negotiation, and extensions.

Reflective use: external example of explicit lifecycle identity. No A2A runtime is implemented here.

### Google ADK conversational context

- Primary documentation: https://adk.dev/sessions/
- ADK distinguishes Session, session State, and searchable Memory that may span sessions.

Reflective use: current-session state and cross-session memory must not be collapsed into an unqualified persistence claim.

### OpenAI Agents SDK tracing

- Tracing guide: https://openai.github.io/openai-agents-python/tracing/
- Tracing API reference: https://openai.github.io/openai-agents-python/ref/tracing/
- A trace is represented as related operation spans rather than as a single proof of successful outcome.

Reflective use: trace/span evidence describes recorded execution structure; it does not independently prove persistence continuity, final environment state, or semantic correctness.

### Anthropic agent-evaluation decomposition

- Primary guidance: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- The guidance separates task, trial, grader, transcript/trajectory, outcome, evaluation harness, and agent harness.

Reflective use: trajectory, final outcome, grader judgment, and harness assumptions remain complementary evidence surfaces.

## Ingestion, truth, and source authority

Reflective Continuum separates four independent axes:

1. `INGESTION_OUTCOME`: whether a signal passed the repository ingestion/reflection path
2. `SOURCE_CREDIBILITY`: primary research, institutional publication, vendor/blog, secondary material, or unverified
3. `SOURCE_CLAIM_SUPPORT`: whether the source supports the exact persisted proposition
4. `EPISTEMIC_SUPPORT`: how strongly that proposition is supported under the source's assumptions and scope

`ACCEPTED` is a local ingestion/control-flow result. It does not mean `TRUE`, `AUTHORITATIVE`, `IMPLEMENTED`, or `REPRODUCED`.

`REJECTED_FROM_INGESTION` does not mean the source proposition is false.

If a source is reachable but does not support the proposition attributed to it, use `SOURCE_CLAIM_MISMATCH`.

### August reference case: 2026-08-23

The R1 signal citing Wikipedia `AI_alignment` states that maintaining deterministic boundaries is essential for safety. The cited page supports alignment/safety-constraint concepts but does not support that deterministic-boundary proposition as written.

Current state:

`SOURCE_CLAIM_MISMATCH`.

## Database-state semantics

Database observations are scoped to the database identity actually inspected.

For bare SQLite `:memory:`:

- each independent connection receives a distinct database
- another task/process/connection must not be assumed to observe the same state
- closing the owning connection destroys that database

Therefore an R1 statement such as `written to graph` and a later R2 observation such as `Nodes=0 / Edges=0` do not by themselves prove successful durable persistence or failed ingestion unless the same store identity is established.

Use:

`PERSISTENCE_LINK_NOT_VERIFIED`.

A repeated snapshot digest demonstrates identity/repeatability of the represented graph snapshot for its declared fixture/store/revision. It is not memory-continuity evidence by itself.

## Selfcheck semantics

`CODE/tasks/cortex_selfcheck.py` checks the database connection it opens.

Its named surfaces are:

- foreign-key setting
- FTS5 accessibility
- `PRAGMA integrity_check`
- rule-engine fixture acceptance
- node/edge counts
- initialization success

With the default `:memory:` argument, these are observations of a fresh connection-local store.

A healthy selfcheck does not establish:

- cross-run persistence
- successful earlier Daily ingestion
- source truth
- semantic correctness
- absence of historical failures

## Search and drift semantics

Reflective's implemented search is lexical FTS5 search, not embedding search.

`compute_semantic_delta()` compares the identity of the **top FTS5 result** for the same query across two declared versions.

Therefore use:

`LEXICAL_TOP_RESULT_CHANGED`

rather than an unqualified claim that semantic meaning changed.

`semantic_drift_audit.py` explicitly records these limitations:

- `FTS5 lexical ranking`
- `caller-selected queries`

Structural delta, lexical top-result delta, and PageRank/rank delta are different evidence surfaces.

`verify_self_consistency()` delegates to the generic rule engine. It does not independently establish that an arbitrary drift report satisfies a dedicated drift schema.

## Entropy and phase semantics

`calculate_topological_entropy()` computes Shannon entropy in nats over normalized non-negative input scores, commonly the current PageRank distribution.

A higher/lower value describes that mathematical distribution only.

`check_phase_boundary()` is a threshold comparison. It does not prove cognition, instability, safety, semantic drift, or convergence.

`LIQUID` and `GASEOUS` are local operational labels used by the observation loop.

## Health and empty-state semantics

Module-local checks and system-level state are different.

- successful import/init may be module-local success
- rule-engine fixture success is rule-engine-local success
- integrity/foreign-key/FTS checks establish only their named contract
- `Nodes=0 / Edges=0` does not prove persistence health, successful Daily ingestion, or semantic correctness

When the database is empty and the cause is not established, use:

`INDETERMINATE_EMPTY_STATE`.

## Drift and transition semantics

A drift label belongs to the data and transition set actually inspected.

- `STABLE` must not imply that uncomputed operational transitions were stable
- if no drift is detected only inside the available audit surface, prefer `NO_DRIFT_DETECTED_WITHIN_AUDIT_SCOPE`
- synthetic/test transitions and operational/runtime transitions are separate evidence classes
- if transition origin cannot be separated, operational transition count remains `NOT_COMPUTED`

## Daily-to-Weekly inheritance

Weekly summaries preserve Daily uncertainty and failure history unless new evidence directly resolves it.

- a Weekly task's own passing snapshot does not erase an earlier Daily error/failure
- `Missing dates: NONE` does not mean every field was computed
- rejected signals remain part of the historical state
- a Weekly summary may aggregate or downgrade Daily evidence but may not strengthen an uncertain Daily observation without new evidence

August R2 history that remains visible:

- 2026-08-07 through 2026-08-10: each persisted `26 passed / 1 error`
- 2026-08-17 through 2026-08-23: each persisted `26 passed / 1 failed`

W32/W33/W34 R3 snapshots describe their own execution surfaces. They do not reconstruct or replace those Daily R2 states.

## Historical continuity and availability

Current path presence, original execution, persistence identity, transition origin, generation/delivery history, and aggregation-snapshot visibility are separate dimensions.

The 2026-08-06 R2 case is the canonical August example:

- the repository now contains an R2 path for that logical date
- that path is a later reconciliation artifact
- the original R2 artifact was not retained
- the original runtime result remains `HISTORICAL_RUNTIME_UNKNOWN`
- missing original metrics are not reconstructed

A later file may repair current interpretation or delivery coverage. It cannot manufacture an earlier runtime observation or prove an unobserved persistence interval.

Use [ADR-010](ADR/ADR-010.md) for the continuity decision and [METH-005](METHODOLOGY/METH-005-evidence-continuity-reconciliation.md) for the reconciliation method.

## Source reuse and novelty

Repeated primary papers or signals are allowed when deliberate. Label the reason when novelty matters:

- `REVALIDATED_SOURCE`
- `REPEATED_CONTROL_SIGNAL`
- `NEW_CLAIM_FROM_EXISTING_SOURCE`
- `DUPLICATE_NO_NEW_EVIDENCE`

Repeated ingestion must not be presented as independent corroboration merely because it occurred on another date.

## Reference-topology snapshot semantics

A Weekly R4 topology audit is a point-in-time observation. Later documentation changes can resolve an orphan or mapping without making the earlier audit false.

The W33/W34 audits recorded the PIONEERS files as `UNRESOLVED_ORPHAN` in their audit snapshots. The current reference topology connects those files as non-normative references.

Current interpretation:

`DOCUMENTATION_ORPHAN_RESOLVED_WITHOUT_NORMATIVE_PROMOTION`.

## Correction policy

Historical R1–R4 artifacts are point-in-time evidence.

When a claim is materially over-strong but the original record remains useful, prefer explicit calibration that states:

- original state
- current interpretation
- new evidence
- unresolved uncertainty
- precedence scope

Do not alter a historical audit merely to make the earlier snapshot appear clean.
