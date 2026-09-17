> [!NOTE]
> **Current architecture interpretation — 2026-09-18**
> - **Subject class:** `METHOD`
> - **Role:** Current methodology for **cognitive divergence rollback**
> - **Authority:** Repository-native method authority for the procedure, measurement, reconciliation rule, assumptions, and failure semantics explicitly defined here
> - **Current meaning:** Treat the procedure as a method contract, not evidence that it ran at the current revision. Historical R2/failure ranges remain historical ranges rather than present-state guarantees
> - **Evidence / implementation boundary:** Detection, drift, alignment, rollback, or reconciliation vocabulary is bounded by implemented mechanics: lexical search is not semantic proof, savepoints are not external rollback, and repeated digests are not convergence evidence
> - **Cross-document relation:** Specification/runtime code bound mechanics; ADRs explain decisions; Evidence Baseline and periodic artifacts provide dated observations without redefining the method
> - **Update trigger:** Update when mechanics, thresholds, evidence ranges, or reconciliation semantics materially change
> - **Preservation rule:** Existing subject history and dated examples retain their original time boundary. This pass clarifies current interpretation and corrects only confirmed current-authority drift

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