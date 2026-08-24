# Reflective Continuum Engineering Specification

- Version: 2026.08
- Review calibration: 2026-08-24
- Status: implemented reference contract with evidence-scoped interpretation

## Purpose and non-goals

Reflective Continuum is a standard-library Python reference for:

- versioned graph storage in SQLite
- synchronized FTS5 lexical search
- transactional node/edge updates through savepoints
- structural, lexical-result, and PageRank-score deltas
- PageRank-derived Shannon entropy
- explicit content validation
- bounded reflection hooks around transactional ingestion
- small task wrappers for selfcheck, drift audit, convergence drills, and insight transformation

It is not a cognitive system, semantic embedding model, truth engine, safety proof, autonomous researcher, distributed database, or production service.

“Liquid”, “gaseous”, “cortex”, “reflection”, “entropy”, “semantic drift”, and “convergence” are project labels whose meaning is limited by the concrete implementation described below.

This specification records public repository architecture only. It does not encode private prompts, hidden reasoning, unpublished maintenance strategy, or future artifact-production instructions.

## Repository realization map

### `CODE/continuum_db.py` — versioned graph/store boundary

`GraphDB` implements the current storage core.

- default database argument is `:memory:`
- SQLite foreign-key enforcement is enabled and verified per connection
- `nodes` is keyed by `(node_id, version)`
- `edges` is keyed by `(source_id, target_id, relationship, version)`
- edge endpoints reference nodes at the same version
- FTS5 uses an external-content table synchronized through insert/delete/update triggers
- node conflict handling uses `ON CONFLICT ... DO UPDATE`, avoiding replace-style hidden delete semantics
- explicit savepoints provide fork/commit/rollback behavior
- snapshot digests hash sorted node/edge content for one declared version

A bare `:memory:` database is connection-local and disappears with that connection. Therefore a default selfcheck or task-local observation over `:memory:` cannot prove cross-task, cross-process, or cross-day persistence.

### `CODE/entropy_analyzer.py` — graph-metric boundary

The analysis module implements:

- validated PageRank over a declared node/edge graph
- normalized rank output
- Shannon entropy in nats over normalized non-negative score values
- a threshold comparison through `check_phase_boundary`

The entropy value is a mathematical summary of the supplied rank distribution. It is not a measure of semantic truth, safety, cognition, or global system disorder.

### `CODE/drift_detector.py` — delta boundary

The drift module keeps three different comparisons separate:

- `compute_structural_delta` — node additions/removals/content modifications between two declared versions
- `compute_semantic_delta` — whether the **top FTS5 lexical result** changes for the same caller-provided query
- `compute_rank_delta` — nodes whose PageRank score moves beyond a caller-provided threshold

The function named `compute_semantic_delta` is therefore a lexical top-result change detector, not an embedding-based or general semantic-equivalence detector.

`verify_self_consistency` delegates to the generic `RuleEngine` validation surface. It must not be cited as a dedicated proof that an arbitrary drift report is self-consistent unless the supplied object actually satisfies the rule engine's declared input schema.

### `CODE/reflective_validator.py` — executable rule boundary

`RuleConfig` defines executable local limits such as reflection depth, entropy threshold, and maximum content length.

`RuleEngine` validates state-delta structure and can check Python content for standard-library-only imports using the current interpreter's AST and `sys.stdlib_module_names`.

ADR prose is retained for architecture explanation; it is not parsed into runtime constants.

### `CODE/cortex_observer.py` — transactional observation boundary

`CortexObserver.process_input`:

1. validates the incoming node/content object
2. opens one savepoint
3. inserts/updates the node and requested edges
4. re-validates the version snapshot
5. computes PageRank and entropy
6. returns immediately when the configured boundary is not exceeded
7. otherwise enters a bounded reflector loop
8. recomputes validation and graph metrics after each reflector step
9. rolls back the savepoint when policy rejection or reflection-depth exhaustion occurs

`ProcessResult.accepted` means the local validation/transaction path accepted the input under the current executable rules. It does **not** mean the input is externally true, authoritative, safe, or durably persisted beyond the database identity actually used.

### `CODE/tasks/**` — bounded task wrappers

Current task modules include:

- `cortex_selfcheck.py`
- `semantic_drift_audit.py`
- `convergence_drill.py`
- `insight_morpher.py`

`cortex_selfcheck.py` checks the specific database connection it opens: foreign-key state, FTS5 availability, SQLite integrity result, rule-engine fixture acceptance, and node/edge counts. Its default `:memory:` database is a fresh connection-local store.

`semantic_drift_audit.py` compares declared versions and caller-selected queries. Its own limitations explicitly identify `FTS5 lexical ranking` and `caller-selected queries`.

Task output is evidence about the task's declared inputs and checked properties only.

## Decision and reference topology

The engineering decisions that narrow this specification are indexed in [`ADR/INDEX.md`](ADR/INDEX.md). ADR numbers are identifiers, not a sequential supersession chain.

| Specification surface | Governing ADRs |
|---|---|
| Runtime dependency and explicit-contract boundary | [ADR-001](ADR/ADR-001.md), [ADR-007](ADR/ADR-007.md) |
| Versioned persistence and transaction behavior | [ADR-004](ADR/ADR-004.md) |
| Structural / lexical / rank delta separation | [ADR-003](ADR/ADR-003.md) |
| Entropy and phase-label interpretation | [ADR-005](ADR/ADR-005.md) |
| Bounded reflection and rollback loop | [ADR-002](ADR/ADR-002.md) |
| External-signal provenance before synthesis | [ADR-006](ADR/ADR-006.md) |
| Task ownership and explicit output boundary | [ADR-008](ADR/ADR-008.md) |
| Evaluation and completion-claim scope | [ADR-009](ADR/ADR-009.md) |
| State, persistence, transition, and historical continuity | [ADR-010](ADR/ADR-010.md) |

Background and methodological sources are indexed in [`REFERENCES/INDEX.md`](REFERENCES/INDEX.md). They are non-normative context unless a specific requirement is separately adopted by this specification or an ADR.

## Runtime and persistence contract

Runtime code uses the Python standard library. Python-version compatibility is claimed only for a revision/environment with retained execution evidence for that version.

SQLite must provide FTS5. Every `GraphDB` connection enables and verifies `PRAGMA foreign_keys=ON`.

Existing databases with an incompatible historical schema require an explicit migration before they can be assumed to satisfy the current versioned edge/node contract.

A continuity claim MUST identify the store whose state is said to persist.

Useful identities may include:

- filesystem database path
- SQLite URI/shared-memory identity where explicitly used
- connection/run/task identity
- graph version
- snapshot digest plus the store/revision that produced it

A repeated digest without shared durable-store identity demonstrates repeatability of the represented snapshot, not persistence through time.

## Transaction contract

Savepoint names match `[A-Za-z_][A-Za-z0-9_]{0,63}` and are quoted.

Rollback releases the savepoint after rollback. The context manager releases a successful savepoint and re-raises unexpected failures after rollback.

Database integrity/programming exceptions are not converted into successful `ProcessResult` states.

## Search and delta contracts

FTS5 search treats caller text as a quoted lexical phrase, accepts an optional version, limits results to `1..100`, and orders by BM25 score then identifiers.

It does not measure general semantic equivalence.

Structural delta returns sorted added/removed/content-modified node identifiers between two versions.

The current “semantic delta” reports whether the top lexical FTS5 result changed for the same declared query.

Rank delta reports nodes whose absolute score shift exceeds a caller-declared non-negative threshold.

Synthetic/test transitions and operational/runtime transitions are distinct evidence classes. A transition count with unresolved origin MUST NOT be promoted to an operational-transition claim.

## Analysis contract

PageRank requires unique known nodes, validated configuration, and known edge endpoints; duplicate edges are collapsed.

Entropy normalizes finite non-negative scores and reports nats. A boundary check is a threshold comparison over that graph-derived quantity.

A repeated snapshot/hash demonstrates repeatability only for the declared fixture/store/revision that produced it. Matching hashes alone do not prove cross-run, cross-task, or cross-day memory continuity.

## Validation and observation contract

`RuleConfig` is executable policy. ADR prose is not runtime configuration.

`RuleEngine.verify_stdlib_only()` establishes only that the parsed import roots are members of the current interpreter's standard-library module set. It is not a security sandbox or behavioral validator for the Python program.

`CortexObserver.process_input()` returns `ProcessResult` for accepted or policy-rejected input and propagates unexpected database/programming failures.

Keep these states separate:

- module import/init success
- database initialization/integrity
- local validation acceptance
- transaction commit/rollback
- source/claim support
- durable persistence continuity
- higher-level research conclusion

## External-signal and source contract

A research signal has at least two independent statuses:

1. repository ingestion/control-flow outcome
2. source/claim support

`ACCEPTED` does not mean `TRUE` or `AUTHORITATIVE`.

`REJECTED_FROM_INGESTION` does not mean `FALSE`.

The exact proposition attributed to an external source must be supportable by that source at the declared authority level. If the source is reachable but does not support the proposition as recorded, use `SOURCE_CLAIM_MISMATCH`.

Secondary/contextual material may support explicitly secondary/contextual claims. Primary/current material should be preferred for material factual, implementation, or scientific claims.

## State continuity contract

A continuity claim names the object whose state is said to continue and the evidence linking both observations.

Depending on the claim, this may require:

- database/store identity
- connection/run/session/task identity
- graph/schema/revision identity
- transition origin
- artifact generation/delivery history
- aggregation snapshot identity

Current path presence is not historical execution evidence. A later reconciliation file is not an original run artifact. A successful current selfcheck does not erase a historical error/failure or prove an unobserved persistence interval.

When linkage is absent, use states such as:

- `PERSISTENCE_LINK_NOT_VERIFIED`
- `TRANSITION_ORIGIN_NOT_COMPUTED`
- `HISTORICAL_RUNTIME_UNKNOWN`

## Task contract

Tasks are importable libraries plus bounded command-line wrappers. They do not own `RESEARCH/**` history and do not silently convert task output into research truth.

Default task output is structured JSON on stdout where implemented. Tasks that accept an explicit output path write only to that caller-supplied destination.

Periodic `RESEARCH/**` artifacts are separately owned research records.

## Evidence boundary

A claim is accepted only to the extent supported by evidence actually produced for the relevant revision/configuration.

Examples:

- a selfcheck observing foreign keys, FTS5, integrity, and rule-engine fixture acceptance supports those named checks for the database it opened
- a 100-iteration fixed fixture producing one snapshot digest supports run-local repeatability for that fixture
- a lexical drift audit supports the selected queries and versions it records
- a current successful task does not erase an earlier Daily error/failure
- a source-ingestion success does not prove the source claim is correct

File presence, historical prose, and a later aggregate are not substitutes for the exact execution/source evidence needed by the claim.

## Security and ownership

Callers own database-file permissions, authentication, authorization, isolation, backups, encryption, retention, quotas, and incident response.

FTS query limits and standard-library-only import checks do not provide a security sandbox.

Separately owned README, homepage, `.nojekyll`, `RESEARCH/**`, references, and license surfaces remain outside incidental runtime maintenance.

This specification changes no runtime code, presentation behavior, dependency set, deployment state, or artifact-production configuration.
