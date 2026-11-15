> [!NOTE]
> **Current architecture interpretation — 2026-09-18**
> - **Subject class:** `METHOD`
> - **Role:** Current methodology: **Transactional rejection and rollback**
> - **Authority:** Repository-native method authority for the exact procedure, observation rule, assumptions and limits stated by this file
> - **Current meaning:** Treat the named method as a repeatable interpretation/checking contract. Method definition does not imply execution on the current revision, and historical examples do not become current state by proximity
> - **Evidence / implementation boundary:** FTS lexical change is not semantic truth; reflector callback behavior is not autonomous cognition; SQLite savepoint rollback is local transaction rollback; persistence and convergence require explicit store/run evidence rather than terminology alone
> - **Cross-document relation:** Specification/runtime code bound mechanics; ADRs explain durable choices; dated evidence records observations; Reproducibility owns revision/store/replay identity
> - **Update trigger:** Update when procedure, threshold, implementation mapping, historical evidence range or failure/reconciliation semantics materially changes
> - **Preservation rule:** Existing method procedure and examples remain in place; current clarification does not rewrite earlier execution evidence

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

## Database atomicity versus observer-state atomicity

For a validation-triggered `_RejectedInput`, the savepoint is rolled back, the handler resets `CortexObserver.phase` and `current_depth`, and a rejected result is returned. For **unexpected exceptions** from the reflector, SQLite operation or programming path, `GraphDB.savepoint` rolls back its tentative database mutation and reraises, but `process_input` does not restore the observer fields in that exception path.

A precise rollback statement must therefore name the object: `SQLITE_SAVEPOINT_MUTATIONS_ROLLED_BACK` does not entail `OBSERVER_FIELDS_RESTORED`, `CALLBACK_SIDE_EFFECTS_COMPENSATED` or `SOURCE_PROPOSITION_FALSE`. A negative test should force a reflector exception after the phase is changed, retain before/after database digest and object state, and confirm the exception is not re-labelled as successful reflection. No such test is claimed executed here.
