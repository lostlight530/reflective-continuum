# Reflective Continuum Engineering Specification

- Version: 2026.08
- Review calibration: 2026-08-24
- Status: implemented reference contract with evidence-scoped verification

## Purpose and non-goals

Reflective Continuum is a standard-library Python reference for versioned graph storage in SQLite, synchronized FTS5 lexical search, structural/search-result/rank deltas, PageRank-derived Shannon entropy, explicit content validation, transactional ingestion, and bounded reflection hooks.

It is not a cognitive system, semantic embedding model, truth engine, safety proof, autonomous researcher, distributed database, or production service. “Liquid”, “gaseous”, “cortex”, “reflection”, “entropy”, and “convergence” are project labels. Claims apply only to declared fixtures, versions, queries, thresholds, environments, and evidence surfaces.

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

## Runtime and persistence

Runtime code uses the Python standard library. Python-version compatibility is claimed only for revisions/configurations with retained execution evidence for that version; this specification does not imply a CI or test matrix.

SQLite must provide FTS5. Every connection enables and verifies `PRAGMA foreign_keys=ON`.

`nodes` is keyed by `(node_id, version)`. `edges` is keyed by `(source_id, target_id, relationship, version)` and each endpoint references a node at the same version. Node upsert uses `ON CONFLICT DO UPDATE`; it must not use `REPLACE`, because external-content FTS5 synchronization depends on the update/delete triggers. Existing databases with the prior edge schema require an explicit migration before use.

A bare SQLite `:memory:` database is connection-local. An observation from one such connection MUST NOT be interpreted as durable state shared with another task/process/connection unless an explicit shared-store identity is established.

## Transaction contract

Savepoint names match `[A-Za-z_][A-Za-z0-9_]{0,63}` and are quoted. Rollback always releases the savepoint. The context manager commits only a successful block and re-raises unexpected failures. Database integrity errors are not converted into success or hidden.

## Search and delta contracts

FTS5 search treats caller text as a quoted lexical phrase, accepts an optional version, limits results to 1..100, and orders deterministically by BM25 score then identifiers. It does not measure semantic equivalence.

Structural delta returns sorted added/removed/content-modified node identifiers between two versions. Semantic delta reports whether the top lexical result changed for the same declared query. Rank delta reports nodes whose absolute score shift exceeds a caller-declared non-negative threshold.

Synthetic/test transitions and operational/runtime transitions are distinct evidence classes. A transition count with unresolved origin MUST NOT be promoted to an operational-transition claim.

## Analysis contract

PageRank requires unique known nodes, validated configuration, and known edge endpoints; duplicate edges are collapsed. Output is normalized. Entropy normalizes finite non-negative scores and reports nats. A boundary check is a threshold comparison, not evidence of cognition, instability, safety, or global convergence.

A repeated snapshot/hash demonstrates repeatability only for the declared fixture/revision that produced it. Matching hashes alone do not prove cross-run, cross-task, or cross-day memory continuity.

## Validation and observation

`RuleConfig` is executable policy. ADR prose is never parsed for runtime constants. Python import checking uses the AST and current interpreter’s standard-library module set.

`CortexObserver.process_input` validates caller data, uses one transaction, returns `ProcessResult` for accepted or policy-rejected input, and propagates unexpected database/programming errors. When the boundary is exceeded, it invokes an optional reflector once per depth and recomputes state; unchanged high entropy exhausts the configured loop and rolls back.

Module import/init success, database integrity, ingestion acceptance, source truth, persistence continuity, and overall system health remain separate observations.

## External-signal and source contract

An R1-style signal has at least two independent statuses:

1. repository ingestion/control-flow outcome
2. source/claim support

`ACCEPTED` does not mean `TRUE` or `AUTHORITATIVE`. `REJECTED_FROM_INGESTION` does not mean `FALSE`.

The exact proposition attributed to an external source must be supportable by that source at the declared authority level. If the source is reachable but does not support the proposition as recorded, use `SOURCE_CLAIM_MISMATCH` rather than upgrading the claim through synthesis.

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

When linkage is absent, use states such as `PERSISTENCE_LINK_NOT_VERIFIED`, `TRANSITION_ORIGIN_NOT_COMPUTED`, or `HISTORICAL_RUNTIME_UNKNOWN`.

## Task contract

Tasks are importable libraries plus bounded CLIs. They do not seed unsupported external claims, scan the entire repository, read ad-hoc logs, or write under `RESEARCH/**`. Default output is structured JSON on stdout. `semantic_drift_audit` and `cortex_selfcheck` write only to an explicitly supplied path.

Periodic `RESEARCH/**` artifacts are separately owned research records. Scheduler/cadence decisions are external to the runtime task contract.

## Security and ownership

Callers own database-file permissions, authentication, authorization, isolation, backups, encryption, retention, quotas, and incident response. FTS query limits do not prevent all resource abuse.

Separately owned README, homepage, `.nojekyll`, `RESEARCH/**`, references, and license surfaces are outside incidental runtime maintenance. Scope review must explicitly distinguish allowed documentation/evidence changes from runtime/frontend/automation changes. This specification does not create a merge gate or CI policy.

## Verification and acceptance evidence

A claim is accepted only to the extent supported by evidence actually produced for the relevant revision/configuration.

For executable behavior, relevant evidence may include recorded compile/test/selfcheck commands, environment and Python/SQLite versions, fixtures/digests, exit/results, invalid cases, and untested boundaries.

For documentation/evidence-only changes, record that no tests were run when that is the case; do not invent execution evidence.

A selfcheck observing foreign keys, FTS5, integrity, or validator behavior supports only those named checks. A 100-iteration fixed fixture producing one snapshot digest supports run-local repeatability for that fixture. It does not prove durable persistence, semantic truth, alignment, or universal determinism.

Historical Daily failures/errors remain part of Weekly/Monthly truth even when a higher-level task has a later passing snapshot.
