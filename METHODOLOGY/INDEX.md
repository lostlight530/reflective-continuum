# Reflective Continuum Methodology Index

Status: procedure and evidence-surface map  
Current calibration: 2026-09-17

`METHODOLOGY/**` explains how concrete repository properties are measured or interpreted. A methodology does not create a runtime capability.

## Method map

| Method | Current meaning | Concrete surface |
|---|---|---|
| [METH-001](./METH-001-phase-boundary-detection.md) | Evaluate graph-derived entropy boundary | `CODE/entropy_analyzer.py` |
| [METH-002](./METH-002-reflective-morphing-protocol.md) | Observe one transactional bounded reflection path | `cortex_observer.py`, `continuum_db.py`, `reflective_validator.py` |
| [METH-003](./METH-003-alignment-verification.md) | Review exact claim/source support | repository evidence + research sources |
| [METH-004](./METH-004-cognitive-divergence-rollback.md) | Interpret SQLite savepoint rejection/rollback | `cortex_observer.py`, `continuum_db.py` |
| [METH-005](./METH-005-evidence-continuity-reconciliation.md) | Reconcile persistence/artifact/source continuity by identity | storage + task + retained research history |

## Method contract

Each methodology identifies:

1. exact implementation/evidence surface;
2. real inputs;
3. procedure actually performed;
4. output the surface can support;
5. failure or unresolved conditions;
6. explicit non-claims.

## Cross-method boundaries

- graph entropy threshold != cognition/safety
- local reflection hook != semantic improvement
- FTS5 top-result change != general semantic drift
- ingestion acceptance != source truth
- SQLite rollback != external-system rollback
- fixed-fixture repeatability != durable persistence
- same logical date != shared database identity
- R1 accepted signal + R2 empty store != persistence proof or data-loss proof
- current path presence != historical runtime success
- periodic snapshot != replacement for Daily error/failure history

METH-005 operationalizes ADR-010's identity requirement for continuity claims.

## Periodic and historical evidence relation

This index is a durable method map, not a live week/month status surface.

- R1/R2 Daily records remain independent task observations unless a common store identity is retained.
- R3/R4 Weekly synthesis may aggregate or downgrade inherited evidence but cannot erase failures or manufacture continuity.
- R5 stage/monthly synthesis must declare a cutoff and preserve unresolved state.
- Open/closed state for a named week/month belongs to its time-scoped record, not to this methodology index.
- The historical 2026-08-27 statement that W35/formal August R5 were open remains valid at that cutoff and is not rewritten here.

## Repository evidence identity

Keep these identities separate when a method or result is cited:

```text
Git revision
!= Python/SQLite environment
!= database/store identity
!= fixture/input identity
!= snapshot digest
!= executed command/result
!= archived publication DOI
```

A repeatable fixed fixture can support repeatability at a recorded revision/environment. It does not prove long-horizon persistence, semantic convergence, or equivalence with a Zenodo archive or later `main`.

## Current navigation

- [ADR index](../ADR/INDEX.md)
- [Engineering specification](../SPECIFICATION.md)
- [Evidence baseline](../EVIDENCE_BASELINE.md)
- [Reproducibility](../REPRODUCIBILITY.md)
- [Release policy](../RELEASE_POLICY.md)

## Historical calibration references

- [August stage audit through 2026-08-27](../historical-audits/03-stage-and-period-audits/2026-08-27--august-through-27--stage-audit.md)
- [Prior cutoff audit through 2026-08-23](../historical-audits/03-stage-and-period-audits/2026-08-23--august-through-23--stage-audit.md)
