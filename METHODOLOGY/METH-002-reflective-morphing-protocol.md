# Transactional bounded observer loop

- Method version: 2026-08-24
- Implementation anchors: `CODE/cortex_observer.py`, `CODE/continuum_db.py`, `CODE/reflective_validator.py`

## Objective

Observe how one caller-provided graph update is validated, tentatively written, measured, optionally reflected, accepted, or rolled back under the implemented local rules.

## Inputs

- `GraphDB` store identity
- `RuleEngine` / `RuleConfig`
- node ID and content
- version
- list of `(source, target, relationship)` edges
- optional reflector hook

## Procedure

1. Validate the incoming node/content.
2. Validate edge list structure.
3. Open one uniquely named savepoint.
4. Insert/update the node and edges without committing outside that savepoint.
5. Validate the full version snapshot.
6. Compute PageRank and entropy.
7. If the entropy boundary is not exceeded, accept and release the savepoint.
8. Otherwise invoke the optional reflector at each bounded depth.
9. Revalidate and recompute after every reflector call.
10. If the boundary clears, accept; if validation fails or maximum depth is exhausted, reject and roll back.
11. Preserve unexpected database/programming exceptions as exceptions after rollback.

## Outputs

`ProcessResult` containing:

- `accepted`
- local phase label
- reflection depth
- graph-derived entropy
- rejection reasons when applicable

plus the resulting database state only within the identity/lifetime of the store used.

## Failure conditions

A rejected `ProcessResult` is not a source-falsification result. An exception is not silently converted to rejection success. A default in-memory store does not support cross-run persistence claims.

## Evidence boundary

This method measures one local transaction/observer path. It does not establish semantic improvement, reflector quality, durable memory, safety, or convergence.