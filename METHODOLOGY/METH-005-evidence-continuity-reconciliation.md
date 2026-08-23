# Evidence continuity and reconciliation

- Method version: 2026-08-24
- Authority: ADR-010

## Objective

Determine whether two observations can legitimately be treated as evidence about the same continuing state, transition, artifact lifecycle, or execution history.

## Inputs

- logical date / ISO week
- execution timestamp and revision when available
- artifact path and current repository presence
- generation / commit / PR / merge evidence when available
- storage identity, database path, connection identity, or equivalent persistence locator
- transition/event origin class
- original R1/R2/R3/R4 status fields
- later reconciliation or errata records

## Procedure

1. Name the exact continuity claim.
2. Identify the object whose continuity is asserted.
3. Record both endpoint observations and their times/revisions.
4. Establish the identity link between endpoints.
5. Separate current path presence from original execution evidence.
6. Separate synthetic/test state from operational/runtime state.
7. Preserve historical failures, rejected signals, `NOT_COMPUTED`, and unknown runtime states.
8. When a later artifact resolves delivery but not original runtime, update only delivery state.
9. When a later source corrects interpretation, write an erratum or reconciliation rather than rewriting the past as if the later knowledge existed then.
10. Aggregate to Weekly/Monthly only after retaining unresolved dimensions.

## Required state distinctions

### Persistence

- `PERSISTENCE_LINK_VERIFIED`
- `PERSISTENCE_LINK_NOT_VERIFIED`
- `INDETERMINATE_EMPTY_STATE`

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

## Failure conditions

Do not claim continuity when:

- the database or store identity is not verified
- the event origin class cannot be separated
- a later replacement value is the only evidence for an earlier interval
- a reconciliation file is being mistaken for an original execution artifact
- a current test result is used to erase a historical error

## Reference case: 2026-08-06 R2

The current repository contains a 2026-08-06 `cortex-selfcheck` path, but it was created later as a historical reconciliation record. The original R2 runtime result and metrics are not recoverable from repository evidence.

Correct interpretation:

- current path presence: `PRESENT`
- historical original R2 artifact: `NOT_RETAINED`
- historical runtime result: `HISTORICAL_RUNTIME_UNKNOWN`
- reconstructed metrics: `NOT_AUTHORIZED`

This is the canonical example of why path coverage cannot substitute for execution evidence.

## Boundary

This methodology is documentation/review procedure only. It does not alter runtime storage, R1-R5 execution, Jules prompts, CI, Actions, or frontend behavior.
