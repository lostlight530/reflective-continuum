# Evidence continuity and historical reconciliation

- Method version: 2026-08-24
- Governing decision: ADR-010

## Objective

Determine whether two observations can legitimately be treated as evidence about the same continuing store, graph snapshot, transition, artifact lifecycle, source proposition, or execution history without rewriting point-in-time evidence.

## Inputs

- logical date / ISO period
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
5. Separate current path presence from original execution evidence.
6. Separate fixed-fixture repeatability from durable persistence.
7. Separate synthetic/test transitions from operational transitions.
8. Separate local ingestion outcome from external source support.
9. Preserve errors, failures, rejected signals, `NOT_COMPUTED`, and historical-runtime gaps.
10. If later evidence resolves only delivery/path presence, update only that dimension.
11. If a cited source does not support the stored proposition, record `SOURCE_CLAIM_MISMATCH`.
12. Use reconciliation rather than silently making corrected knowledge appear contemporaneous with the original run.

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
- 2026-08-17 through 2026-08-23: `26 passed / 1 failed`

Later Weekly results do not erase those Daily states.

### 2026-08-23 source support

The cited Wikipedia `AI_alignment` page does not support the exact persisted deterministic-boundary-for-safety proposition.

Current status:

`SOURCE_CLAIM_MISMATCH`.

## Evidence boundary

This methodology reconciles documentary/state evidence. It does not create missing execution, a shared database, source truth, or durable persistence.