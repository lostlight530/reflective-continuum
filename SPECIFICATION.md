# Reflective Continuum Engineering Specification

- Version: 2026.08
- Status: implemented reference contract

## Purpose and non-goals

Reflective Continuum is a standard-library Python reference for versioned graph storage in SQLite, synchronized FTS5 lexical search, structural/search-result/rank deltas, PageRank-derived Shannon entropy, explicit content validation, transactional ingestion, and bounded reflection hooks.

It is not a cognitive system, semantic embedding model, truth engine, safety proof, autonomous researcher, distributed database, or production service. “Liquid”, “gaseous”, “cortex”, “reflection”, “entropy”, and “convergence” are project labels. Claims apply only to declared fixtures, versions, queries, thresholds, and environments.

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

Background and methodological sources are indexed in [`REFERENCES/INDEX.md`](REFERENCES/INDEX.md). They are non-normative context unless a specific requirement is separately adopted by this specification or an ADR.

## Runtime and persistence

CI verifies Python 3.12 and 3.14. SQLite must provide FTS5. Every connection enables and verifies `PRAGMA foreign_keys=ON`.

`nodes` is keyed by `(node_id, version)`. `edges` is keyed by `(source_id, target_id, relationship, version)` and each endpoint references a node at the same version. Node upsert uses `ON CONFLICT DO UPDATE`; it must not use `REPLACE`, because external-content FTS5 synchronization depends on the update/delete triggers. Existing databases with the prior edge schema require an explicit migration before use.

## Transaction contract

Savepoint names match `[A-Za-z_][A-Za-z0-9_]{0,63}` and are quoted. Rollback always releases the savepoint. The context manager commits only a successful block and re-raises unexpected failures. Database integrity errors are not converted into success or hidden.

## Search and delta contracts

FTS5 search treats caller text as a quoted lexical phrase, accepts an optional version, limits results to 1..100, and orders deterministically by BM25 score then identifiers. It does not measure semantic equivalence.

Structural delta returns sorted added/removed/content-modified node identifiers between two versions. Semantic delta reports whether the top lexical result changed for the same declared query. Rank delta reports nodes whose absolute score shift exceeds a caller-declared non-negative threshold.

## Analysis contract

PageRank requires unique known nodes, validated configuration, and known edge endpoints; duplicate edges are collapsed. Output is normalized. Entropy normalizes finite non-negative scores and reports nats. A boundary check is a threshold comparison, not evidence of cognition, instability, or safety.

## Validation and observation

`RuleConfig` is executable policy. ADR prose is never parsed for runtime constants. Python import checking uses the AST and current interpreter’s standard-library module set.

`CortexObserver.process_input` validates caller data, uses one transaction, returns `ProcessResult` for accepted or policy-rejected input, and propagates unexpected database/programming errors. When the boundary is exceeded, it invokes an optional reflector once per depth and recomputes state; unchanged high entropy exhausts the real configured loop and rolls back.

## Task contract

Tasks are importable libraries plus bounded CLIs. They do not seed unsupported external claims, scan the entire repository, read ad-hoc logs, or write under `RESEARCH/**`. Default output is structured JSON on stdout. `semantic_drift_audit` and `cortex_selfcheck` write only to an explicitly supplied path.

## Security and ownership

Callers own database-file permissions, authentication, authorization, isolation, backups, encryption, retention, quotas, and incident response. FTS query limits do not prevent all resource abuse. Separately owned README, homepage, `.nojekyll`, RESEARCH, and license paths are protected by CI.

## Acceptance

Compile and tests pass on Python 3.12/3.14; selfcheck observes enabled foreign keys, FTS5 availability, integrity, and validator behavior; the 100-iteration fixture produces one snapshot digest; actions use least privilege and immutable SHAs; PR diff contains no protected path. These checks support only the tested revision and configuration.
