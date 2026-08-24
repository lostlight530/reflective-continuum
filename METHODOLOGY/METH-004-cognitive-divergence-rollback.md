# Transactional rejection and rollback

- Method version: 2026-08-24
- Implementation anchors: `CODE/cortex_observer.py`, `CODE/continuum_db.py`
- Historical filename retained for continuity

## Objective

Interpret the repository's actual rollback behavior when a tentative graph update is rejected inside the observer transaction.

This is not “cognitive divergence rollback”; rollback is a SQLite savepoint operation triggered by local validation/boundary logic.

## Inputs

- identified `GraphDB` store
- tentative node/edge update
- graph version
- `RuleConfig`
- optional reflector hook

## Procedure

1. Open the observer savepoint.
2. Apply the tentative update within that savepoint.
3. Validate the version snapshot.
4. Compute graph metrics and apply the configured entropy boundary.
5. If reflection is entered, invoke the bounded hook/recompute loop.
6. On validation rejection or depth exhaustion, raise the internal rejection path.
7. Roll back to the savepoint and release it.
8. Return the rejected `ProcessResult` with the local reason/depth information.
9. For unexpected exceptions, roll back/release and propagate the exception.

## Outputs

- accepted/rejected local result
- rejection reason where available
- reflection depth
- graph-derived entropy at the relevant observation
- resulting store state within the same identified database

## Failure conditions

Do not claim rollback success from a rejection label alone when the store/result cannot be identified. Do not combine `drift_detector.py` outputs with rollback semantics: structural/lexical/rank deltas are separate analysis functions and do not trigger this transaction rollback path.

## Evidence boundary

Rollback means the tentative SQLite changes in that savepoint were reverted. It does not prove restoration of external systems, semantic correctness, durable recovery, or cognitive alignment.