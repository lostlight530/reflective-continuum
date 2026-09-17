# Reflective Continuum Architecture Decision Index

Status: architecture and implementation-boundary map  
Current calibration: 2026-09-17

ADR numbering is an identifier sequence. A decision supersedes another only when explicitly stated.

## Decision map

| ADR | Current architectural meaning | Concrete repository surface |
|---|---|---|
| [ADR-001](./ADR-001.md) | Standard-library runtime with explicit local contracts | `CODE/**` core modules |
| [ADR-002](./ADR-002.md) | Bounded reflection is a transactional observer loop | `cortex_observer.py`, `continuum_db.py`, `reflective_validator.py` |
| [ADR-003](./ADR-003.md) | Structural, lexical top-result, and rank deltas are distinct | `drift_detector.py` |
| [ADR-004](./ADR-004.md) | Versioned SQLite graph storage has connection/store scope | `continuum_db.py` |
| [ADR-005](./ADR-005.md) | PageRank-derived Shannon entropy is a graph statistic | `entropy_analyzer.py` |
| [ADR-006](./ADR-006.md) | Ingestion outcome and source support are independent | `tasks/insight_morpher.py`, `cortex_observer.py`, retained research evidence |
| [ADR-007](./ADR-007.md) | Executable policy lives in `RuleConfig`/`RuleEngine`, not prose | `reflective_validator.py` |
| [ADR-008](./ADR-008.md) | Task wrappers operate only on explicit inputs/outputs | `CODE/tasks/**` |
| [ADR-009](./ADR-009.md) | Evaluation claims stay inside the exact evidence surface | tasks, storage, analysis, research artifacts |
| [ADR-010](./ADR-010.md) | State continuity requires explicit object identity | storage/task/research history |

## Implementation map

### Storage

`CODE/continuum_db.py`: versioned nodes/edges, per-connection foreign keys, FTS5 triggers, savepoints, lexical search, snapshot digest.

### Graph analysis

`CODE/entropy_analyzer.py`: PageRank, Shannon entropy in nats, local threshold comparison.

`CODE/drift_detector.py`: structural delta, top FTS5 lexical-result change, PageRank-score delta.

### Validation and transactional observation

`CODE/reflective_validator.py`: explicit `RuleConfig`, node/content validation, AST-based stdlib import-root check.

`CODE/cortex_observer.py`: one-savepoint tentative graph update, snapshot validation, entropy boundary, bounded reflector hook, commit/reject/rollback semantics.

### Task wrappers

`CODE/tasks/**`: connection-local selfcheck, selected-version lexical/structural drift audit, fixed-fixture repeatability drill, caller-provided signal ingestion.

## Repository knowledge layers

- `SPECIFICATION.md` describes current engineering behavior and compatibility boundaries.
- `ADR/**` records durable decisions and non-capability boundaries.
- `METHODOLOGY/**` records measurement and interpretation procedures.
- `EVIDENCE_BASELINE.md` is a dated 2026-08-27 calibration and remains point-in-time evidence.
- `REPRODUCIBILITY.md` owns current revision/environment/store/fixture/run provenance requirements.
- retained research/audit records are historical evidence for their declared cutoff.
- `GOVERNANCE/**` owns public maintenance/review rules, not graph/runtime semantics.
- `CITATION.cff`, `codemeta.json`, and `RELEASE_POLICY.md` identify scholarly publication/release surfaces; they do not prove runtime or scientific validity.

## Cross-layer rules

1. Code defines implemented behavior; project vocabulary does not add capability.
2. FTS5 lexical-result change is not general semantic change.
3. Graph-derived entropy is not cognition or safety.
4. Local ingestion acceptance is not source truth.
5. A default `:memory:` store is not durable cross-task memory.
6. A repeated snapshot digest is not persistence through time without store identity.
7. Same-day R1 acceptance and R2 empty state do not establish persistence or data loss without shared store identity.
8. Periodic summaries do not erase Daily failures/errors or historical runtime gaps.
9. External protocols/papers remain reference material unless a local implementation exists.
10. An archived DOI identifies a publication object; it does not identify every later `main` revision, database state, or successful replay.

## Status

Accepted canonical membership index for 10 ADRs.

## Context

Stable ADR paths are required for historical research references and structural review.

## Decision

Membership is defined by the ten entries above; numbering and paths are not reused.

## Consequences

Adding, retiring, or superseding an ADR requires synchronized index and authority-link review.

## Verification

Compare indexed paths with repository files and review each ADR's implementation and evidence boundary; path agreement does not prove semantics.

## Current navigation

- [Engineering specification](../SPECIFICATION.md)
- [Methodology index](../METHODOLOGY/INDEX.md)
- [Evidence baseline](../EVIDENCE_BASELINE.md)
- [Reproducibility](../REPRODUCIBILITY.md)
- [Release policy](../RELEASE_POLICY.md)

## Historical calibration references

- [August stage audit through 2026-08-27](../historical-audits/03-stage-and-period-audits/2026-08-27--august-through-27--stage-audit.md)
- [Prior cutoff audit through 2026-08-23](../historical-audits/03-stage-and-period-audits/2026-08-23--august-through-23--stage-audit.md)
