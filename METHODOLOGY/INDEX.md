# Reflective Continuum Methodology Index

Status: procedure and evidence-surface map

`METHODOLOGY/**` explains how concrete repository properties are measured or interpreted. A methodology does not create a runtime capability.

## Method map

| Method | Current meaning | Concrete surface |
|---|---|---|
| [METH-001](./METH-001-phase-boundary-detection.md) | Evaluate graph-derived entropy boundary | `CODE/entropy_analyzer.py` |
| [METH-002](./METH-002-reflective-morphing-protocol.md) | Observe one transactional bounded reflection path | `cortex_observer.py`, `continuum_db.py`, `reflective_validator.py` |
| [METH-003](./METH-003-alignment-verification.md) | Review exact claim/source support | repository evidence + research sources |
| [METH-004](./METH-004-cognitive-divergence-rollback.md) | Interpret SQLite savepoint rejection/rollback | `cortex_observer.py`, `continuum_db.py` |
| [METH-005](./METH-005-evidence-continuity-reconciliation.md) | Reconcile persistence/artifact/source continuity by identity | storage + task + research history |

## Method contract

Each methodology identifies:

1. exact implementation/evidence surface
2. real inputs
3. procedure actually performed
4. output the surface can support
5. failure or unresolved conditions
6. explicit non-claims

## Cross-method boundaries

- graph entropy threshold != cognition/safety
- local reflection hook != semantic improvement
- FTS5 top-result change != general semantic drift
- ingestion acceptance != source truth
- SQLite rollback != external-system rollback
- fixed-fixture repeatability != durable persistence
- current path presence != historical runtime success
- Weekly/Monthly snapshot != replacement for Daily error/failure history

METH-005 operationalizes ADR-010's identity requirement for continuity claims.

## Related navigation

- [ADR index](../ADR/INDEX.md)
- [Engineering specification](../SPECIFICATION.md)
- [Evidence baseline](../EVIDENCE_BASELINE.md)
- [August stage audit](../RESEARCH/monthly/2026-08-through-23-stage-audit.md)