> [!NOTE]
> **Current architecture interpretation — 2026-10-04**
> - **Subject class:** `METHOD`
> - **Role:** Current methodology: **Evidence continuity and historical reconciliation**
> - **Authority:** Repository-native method authority for the exact procedure, observation rule, assumptions and limits stated by this file
> - **Current meaning:** Treat the named method as a repeatable interpretation/checking contract. Method definition does not imply execution on the current revision, and historical examples do not become current state by proximity
> - **Evidence / implementation boundary:** FTS lexical change is not semantic truth; reflector callback behavior is not autonomous cognition; SQLite savepoint rollback is local transaction rollback; persistence and convergence require explicit store/run evidence rather than terminology alone
> - **Cross-document relation:** Specification/runtime code bound mechanics; ADRs explain durable choices; dated evidence records observations; Reproducibility owns revision/store/replay identity
> - **Update trigger:** Update when procedure, threshold, implementation mapping, historical evidence range or failure/reconciliation semantics materially changes
> - **Preservation rule:** Existing method procedure and examples remain in place; current clarification does not rewrite earlier execution evidence

# Evidence continuity and historical reconciliation

- Method version: 2026-10-04
- Governing decision: ADR-010

## Objective

Determine whether two observations can legitimately be treated as evidence about the same continuing store, graph snapshot, transition, artifact lifecycle, source proposition, or execution history without rewriting point-in-time evidence.

## Inputs

- logical date / ISO period
- exact Git base revision
- exact branch/ref identity when repository visibility is material
- original execution status and timestamp when available
- artifact path and current repository presence
- generation / commit / delivery evidence when material
- database path/URI, connection/run/task identity, graph version, or equivalent persistence locator
- snapshot digest plus the store/fixture identity that produced it
- transition/event origin class
- original R1/R2/R3/R4 evidence fields
- external source identity and exact persisted proposition when source support is disputed
- later reconciliation/errata evidence

## Procedure

1. Name the exact continuity/support claim.
2. Identify the object whose continuity/support is asserted.
3. Record both endpoint observations and their time/revision boundaries.
4. Establish an identity link; matching values/digests alone are insufficient.
5. When repository-path availability is part of the claim, establish the exact branch/ref snapshot; sibling-branch presence is not observed-path availability.
6. Separate current path presence from original execution evidence.
7. Separate fixed-fixture repeatability from durable persistence.
8. Separate synthetic/test transitions from operational transitions.
9. Separate local ingestion outcome from external source support.
10. Preserve errors, failures, rejected signals, `NOT_COMPUTED`, and historical-runtime gaps.
11. If later evidence resolves only delivery/path presence, update only that dimension.
12. If a cited source does not support the stored proposition, record `SOURCE_CLAIM_MISMATCH`.
13. Use reconciliation rather than silently making corrected knowledge appear contemporaneous with the original run.

## Persistence states

- `PERSISTENCE_LINK_VERIFIED`
- `PERSISTENCE_LINK_NOT_VERIFIED`
- `INDETERMINATE_EMPTY_STATE`
- `RUN_LOCAL_REPEATABILITY_ONLY`

A bare SQLite `:memory:` database is connection-local. Cross-task/day continuity is unverified without an explicit shared/durable-store identity.

`convergence_drill.py` creates a fresh default `GraphDB()` on every iteration and rebuilds one fixed fixture. A repeated digest from that task is therefore run-local fixture repeatability, not durable memory.

## Transition states

- `OPERATIONAL_TRANSITION_OBSERVED`
- `SYNTHETIC_TRANSITION_OBSERVED`
- `TRANSITION_ORIGIN_NOT_COMPUTED`

## Artifact-history states

- `AVAILABLE_AT_AGGREGATION_SNAPSHOT`
- `BRANCH_VISIBLE_AT_OBSERVED_REF`
- `SIBLING_BRANCH_PRESENT_NOT_OBSERVED`
- `EVENTUALLY_VISIBLE_ON_MAIN`
- `LATE_AVAILABLE_AFTER_SNAPSHOT`
- `BLOCKED_AT_EXECUTION`
- `UNRESOLVED_DELIVERY_HISTORY`
- `HISTORICAL_RUNTIME_UNKNOWN`

## Source-support states

- `SOURCE_CLAIM_SUPPORTED_WITHIN_SCOPE`
- `SOURCE_CLAIM_MISMATCH`
- `SOURCE_AUTHORITY_INSUFFICIENT_FOR_CLAIM`
- `SOURCE_SUPPORT_UNRESOLVED`

Local `ACCEPTED` / `REJECTED_FROM_INGESTION` remain separate control-flow states.

## August reference cases

The cases below are historical examples at their own August 2026 dates. They do not define current September runtime or periodic status.

### 2026-08-06 R2

- current path: `PRESENT`
- original R2 artifact: `NOT_RETAINED`
- original runtime result: `HISTORICAL_RUNTIME_UNKNOWN`
- reconstructed original metrics: not supported

### R1 ↔ R2 storage identity

R1 reports local graph writes while multiple R2 records observe empty databases, often explicitly `:memory:`. Without one verified shared store identity:

`PERSISTENCE_LINK_NOT_VERIFIED`.

### Historical R2 results

- 2026-08-07 through 2026-08-10: `26 passed / 1 error`
- 2026-08-17 through 2026-08-27: `26 passed / 1 failed`

The second range is the current retained historical interpretation through the 2026-08-27 evidence cutoff. Later Weekly results and later successful tasks do not erase those Daily states, and this methodology does not infer post-cutoff results from the range.

### 2026-08-23 source support

The cited Wikipedia `AI_alignment` page does not support the exact persisted deterministic-boundary-for-safety proposition.

Current status:

`SOURCE_CLAIM_MISMATCH`.

## Outputs

- preserved original artifact plus current disposition
- explicit store/source/test/transition identity state
- unresolved conflict, missing evidence, and canonical authority
- replay status for any post-hoc annotation

## Failure conditions

Reconciliation fails when it invents a shared store, erases a failed/error result, converts ingestion into source truth, backfills a future date, or treats path presence as execution evidence.

## Evidence boundary

This methodology reconciles documentary/state evidence. It does not create missing execution, a shared database, source truth, or durable persistence.

Historical reference ranges inside this methodology remain point-in-time examples rather than a live status dashboard.


## 2026-10-04 reference case — branch snapshot versus eventual main

Use the R1/R2/R3 W40 sequence as the current repository-native reference case.

A valid reconstruction records at least:

- R1 branch/ref and base revision;
- R2 branch/ref and base revision;
- R3 branch/ref and base revision;
- which same-day paths were visible from the R3 observed snapshot;
- later merge state on current `main`;
- whether a later R3 correction consumed the now-visible evidence;
- store identity separately from Git identity;
- test/failure/rejection states separately from path availability.

The allowed interpretation is:

```text
R1_OR_R2_EXISTS_ON_SIBLING_BRANCH
!= R3_INPUT_VISIBLE_AT_THAT_SNAPSHOT

R1_OR_R2_LATER_MERGED
!= R3_EARLIER_SNAPSHOT_COMPLETE

R3_LATER_RECONCILED
!= ORIGINAL_BRANCH_OBSERVATION_FALSE

SAME_DATE
!= SAME_STORE
!= SAME_GIT_SNAPSHOT
```

Repository-snapshot reconciliation is documentary evidence handling. It does not create a shared database, replay R1/R2, or prove durable persistence.
