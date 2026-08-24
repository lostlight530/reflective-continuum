# Evidence continuity and reconciliation

- Method version: 2026-08-24
- Authority: ADR-010

## Objective

Determine whether two observations can legitimately be treated as evidence about the same continuing state, transition, artifact lifecycle, source proposition, or execution history without rewriting point-in-time evidence.

## Inputs

- logical date / ISO week
- execution timestamp and revision when available
- artifact path and current repository presence
- generation / commit / PR / merge evidence when available
- storage identity, database path, connection identity, run/session/task identity, or equivalent persistence locator
- graph/snapshot digest plus the fixture/store identity that produced it
- transition/event origin class
- original R1/R2/R3/R4 status fields
- Daily test/error/failure/rejection states
- external source class, exact persisted proposition, and source text when claim support is disputed
- later reconciliation or errata records

## Procedure

1. Name the exact continuity or support claim.
2. Identify the object whose continuity/support is asserted.
3. Record both endpoint observations and their times/revisions.
4. Establish the identity link between endpoints; a matching value or digest alone is insufficient.
5. Separate current path presence from original execution evidence.
6. Separate run-local fixture repeatability from durable persistence.
7. Separate synthetic/test state from operational/runtime state.
8. Separate ingestion outcome from source credibility and source-claim support.
9. Preserve historical errors, failures, rejected signals, `NOT_COMPUTED`, and unknown runtime states.
10. When a later artifact resolves delivery but not original runtime, update only delivery state.
11. When a source does not support the proposition persisted in an R1 signal, record `SOURCE_CLAIM_MISMATCH`; do not use ingestion acceptance to rescue the claim.
12. When a later source or architecture rule corrects interpretation, write an erratum/reconciliation rather than rewriting the past as if the later knowledge existed then.
13. Aggregate to Weekly/Monthly only after retaining unresolved dimensions and Daily failures/errors.

## Required state distinctions

### Persistence

- `PERSISTENCE_LINK_VERIFIED`
- `PERSISTENCE_LINK_NOT_VERIFIED`
- `INDETERMINATE_EMPTY_STATE`
- `RUN_LOCAL_REPEATABILITY_ONLY`

A bare SQLite `:memory:` database is connection-local. Cross-task/process/day persistence cannot be inferred from it without explicit shared-store identity evidence.

A repeated graph/snapshot hash can demonstrate repeatability for the same declared fixture/revision; it does not by itself prove durable memory or state continuity.

### Transition origin

- `OPERATIONAL_TRANSITION_OBSERVED`
- `SYNTHETIC_TRANSITION_OBSERVED`
- `TRANSITION_ORIGIN_NOT_COMPUTED`

### Artifact history

- `AVAILABLE_AT_AGGREGATION_SNAPSHOT`
- `LATE_AVAILABLE_AFTER_SNAPSHOT`
- `BLOCKED_AT_EXECUTION`
- `UNRESOLVED_DELIVERY_HISTORY`
- `HISTORICAL_RUNTIME_UNKNOWN`

These states are independent of whether a file currently exists.

### Source support

- `SOURCE_CLAIM_SUPPORTED_WITHIN_SCOPE`
- `SOURCE_CLAIM_MISMATCH`
- `SOURCE_AUTHORITY_INSUFFICIENT_FOR_CLAIM`
- `SOURCE_SUPPORT_UNRESOLVED`

`ACCEPTED` / `REJECTED_FROM_INGESTION` remain separate control-flow states and must not substitute for these source-support states.

### Test/history aggregation

Keep independently:

- weekly task's own test snapshot
- each Daily R2 failed/error state
- missing original runtime artifacts
- rejected R1 signals / hard rollbacks
- uncomputed drift or transition dimensions

A later or higher-level all-pass snapshot does not erase earlier Daily error/failure evidence.

## Failure conditions

Do not claim continuity or resolved support when:

- the database/store/run identity is not verified
- a bare `:memory:` observation is being treated as durable cross-run state without shared-store evidence
- a repeated digest is the only alleged persistence link
- the event origin class cannot be separated
- a later replacement value is the only evidence for an earlier interval
- a reconciliation file is being mistaken for an original execution artifact
- a current/weekly test result is used to erase a historical Daily error or failure
- R1 ingestion acceptance is used as proof that the external proposition is true
- the cited source does not support the proposition recorded in the signal

## August 2026 reference cases

### 2026-08-06 R2

The current repository contains a 2026-08-06 `cortex-selfcheck` path, but it was created later as a historical reconciliation record. The original R2 runtime result and metrics are not recoverable from repository evidence.

Correct interpretation:

- current path presence: `PRESENT`
- historical original R2 artifact: `NOT_RETAINED`
- historical runtime result: `HISTORICAL_RUNTIME_UNKNOWN`
- reconstructed metrics: `NOT_AUTHORIZED`

### R1 ↔ R2 persistence

Multiple August R1 reports record accepted/written graph signals while R2 repeatedly observes `Nodes=0 / Edges=0`; several R2 artifacts explicitly use `Database: :memory:`. Neither side proves the other failed or persisted because the shared storage identity is not established.

Correct status: `PERSISTENCE_LINK_NOT_VERIFIED`.

### Historical R2 failures/errors

- 2026-08-07 through 2026-08-10 each preserve `26 passed / 1 error`
- 2026-08-17 through 2026-08-23 each preserve `26 passed / 1 failed`

Weekly R3 snapshots must preserve those Daily states even when the weekly task has its own passing snapshot.

### 2026-08-23 R1 source support

The R1 signal citing Wikipedia `AI_alignment` persists the proposition that maintaining deterministic boundaries is essential for safety. The cited page supports AI-alignment and safety-constraint concepts but does not support that deterministic-boundary proposition as written.

Correct status for reuse of that signal claim: `SOURCE_CLAIM_MISMATCH` unless independent evidence supports the exact proposition.

## Boundary

This methodology is documentation/review procedure only. It does not alter runtime storage, R1-R5 execution, Jules prompts, CI, Actions, or frontend behavior.
