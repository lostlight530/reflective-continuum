# Reflective Continuum Engineering Specification

- Version: 2026.08-r2
- Review calibration: 2026-08-27
- Status: implemented reference contract with evidence-scoped interpretation

## Purpose and non-goals

Reflective Continuum is a standard-library Python reference for versioned SQLite graph storage, FTS5 lexical search, savepoint-scoped updates, graph-derived metrics, explicit validation, bounded reflection hooks, and small task wrappers.

It is not a cognitive system, semantic embedding model, truth engine, safety proof, autonomous researcher, distributed database, or production service.

“Liquid”, “gaseous”, “cortex”, “reflection”, “entropy”, “semantic drift”, and “convergence” are project labels whose meaning is limited by the concrete implementation below.

## Repository realization map

### `CODE/continuum_db.py`

`GraphDB` implements versioned SQLite storage.

- default database argument: `:memory:`
- foreign keys: enabled and verified per connection
- node key: `(node_id, version)`
- edge key: `(source_id, target_id, relationship, version)`
- FTS5: external-content index with synchronization triggers
- explicit savepoints: fork/commit/rollback behavior
- snapshot digest: sorted content identity for one declared version

A bare `:memory:` database is connection-local. A default task observation cannot prove cross-task, cross-process, or cross-day persistence.

### `CODE/entropy_analyzer.py`

Implements PageRank, normalized rank output, Shannon entropy in nats, and a configured entropy-threshold comparison.

The resulting entropy is a graph statistic, not semantic truth, cognition, safety, or global system disorder.

### `CODE/drift_detector.py`

Keeps three comparisons separate:

- structural node delta
- historically named `compute_semantic_delta()` = **top FTS5 lexical-result identity change** for the same query
- PageRank-score delta above a supplied threshold

The lexical result is not an embedding/general semantic-equivalence measure.

### `CODE/reflective_validator.py`

`RuleConfig` and `RuleEngine` define executable local validation policy. ADR prose does not become runtime configuration.

The standard-library import-root check is not a sandbox or behavioral proof.

### `CODE/cortex_observer.py`

`CortexObserver.process_input()` validates an input, opens a savepoint, mutates the local graph tentatively, recomputes validation/metrics, optionally invokes a bounded reflector, and commits or rolls back the local savepoint.

`ProcessResult.accepted` means only that this local control-flow/transaction path accepted the input under the current rules and opened store.

It does not establish external truth, source authority, safety, durable persistence, or convergence.

### `CODE/tasks/**`

Current bounded wrappers include:

- `cortex_selfcheck.py`
- `semantic_drift_audit.py`
- `convergence_drill.py`
- `insight_morpher.py`

A task result is evidence about its declared inputs/store and checked properties only.

## Runtime and persistence contract

Runtime code uses the Python standard library. SQLite must provide FTS5.

A continuity claim MUST identify the store whose state is said to persist. Useful identity evidence may include:

- filesystem DB path
- explicit SQLite URI/shared-memory identity
- connection/process/run/task identity
- graph version
- snapshot digest together with the store/revision that produced it

A repeated digest without shared durable-store identity demonstrates represented-content repeatability, not persistence through time.

## Transaction contract

Savepoints are local SQLite transaction boundaries. Rejection/rollback applies to tentative graph changes inside that savepoint.

It does not establish rollback of external services, messages, files, or world-state side effects.

Unexpected database/programming failures propagate rather than becoming successful `ProcessResult` states.

## Search and delta contracts

FTS5 search is lexical and caller-query scoped.

- structural delta → added/removed/content-modified node IDs
- lexical top-result delta → whether top FTS5 result identity changes
- rank delta → PageRank score shifts above caller threshold

Synthetic/test transitions and operational transitions are distinct evidence classes. An unresolved transition origin is not promoted into an operational-transition claim.

## Analysis contract

PageRank requires a declared valid graph. Entropy normalizes finite non-negative scores and reports nats.

A phase threshold is a local policy condition, not a physical/cognitive phase theorem.

`convergence_drill.py` rebuilds a fixed local fixture and compares snapshot digests. Its strongest supported interpretation is:

`FIXED_FIXTURE_REPEATABILITY_OBSERVED`.

Not:

`SYSTEM_CONVERGENCE_PROVED`.

## Validation and source contract

Keep these states separate:

- module import/init success
- database initialization/integrity
- local validation acceptance
- transaction commit/rollback
- source identity/authority
- exact source-claim support
- durable persistence continuity
- higher-level research conclusion

`ACCEPTED != TRUE`.

`REJECTED_FROM_INGESTION != FALSE`.

If a reachable source does not support the proposition attributed to it, current interpretation uses `SOURCE_CLAIM_MISMATCH` regardless of ingestion outcome.

## State continuity contract

A continuity claim names the object whose state is said to continue and evidence linking both observations.

Same logical date is not enough.

In particular, if R1 reports accepted signals and R2 reports `Nodes=0 / Edges=0`, do not infer either persistence or data loss until a shared database/store identity is established.

Current required label:

`SAME_DAY_OBSERVATIONS / SHARED_STORE_IDENTITY_NOT_ESTABLISHED`.

When linkage is absent, use states such as:

- `PERSISTENCE_LINK_NOT_VERIFIED`
- `TRANSITION_ORIGIN_NOT_COMPUTED`
- `HISTORICAL_RUNTIME_UNKNOWN`

## Daily / Weekly / Monthly research SOP

Historical research artifacts remain point-in-time records. This SOP governs current interpretation and future canonical reconciliation; it does not rewrite old artifacts.

### R1 Daily

A current R1 interpretation records separately:

1. fixed-fixture repeatability result
2. signal and source identity
3. local ingestion acceptance/rejection
4. rollback reason where rejected
5. graph-derived entropy/phase as local metrics
6. exact source-claim support as a separate evidence judgment
7. persistence identity only when actually evidenced

Do not use `Convergence State` as a global convergence claim.

### R2 Daily

A current R2 interpretation records separately:

1. opened-store identity/path when available
2. module/init status
3. named DB/rule checks actually performed
4. node/edge counts for that store
5. complete test totals including failed/errors
6. drift as `NOT_COMPUTED` when not computed
7. empty DB as `INDETERMINATE_EMPTY_STATE`

A selfcheck with 26 passing and 1 failed check is not an all-pass selfcheck.

### R3/R4 Weekly

Weekly synthesis may aggregate, preserve, or downgrade Daily evidence but cannot:

- erase Daily failed/error days
- convert R1 acceptance into source truth
- convert repeated digest into durable memory
- infer R1↔R2 persistence without shared store identity
- promote lexical stability into semantic stability
- convert `NOT_COMPUTED` operational transitions into a no-drift theorem

Historical W34 `STABLE` remains bounded as:

`NO_DRIFT_DETECTED_WITHIN_R3_AVAILABLE_AUDIT_SCOPE`.

At the 2026-08-27 cutoff W35 is still in progress; no final W35 result is inferred.

### R5 Monthly

A partial stage audit may reconcile evidence to its cutoff. Formal monthly closure requires actual natural-month evidence and must not create future-day history.

Formal August R5 status at 2026-08-27: `OPEN`.

## Historical August evidence boundary

Preserve at minimum:

- 2026-08-06 original R2 runtime unknown
- 2026-08-07 through 2026-08-10: `26 passed / 1 error`
- 2026-08-17 through 2026-08-27: `26 passed / 1 failed`
- R1↔R2 persistence link not verified
- 2026-08-23 source-claim mismatch

Later successful tasks or complete path inventory do not erase these records.

Current stage authority: `RESEARCH/monthly/2026-08-through-27-stage-audit.md`.

## Security and ownership

Callers own database-file permissions, authentication, authorization, isolation, backups, encryption, retention, quotas, and incident response.

FTS query limits and standard-library-only import checks do not provide a security sandbox.

This specification changes no runtime implementation, dependency set, presentation behavior, deployment state, or private automation/control strategy.
