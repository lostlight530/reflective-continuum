# R3 Weekly Alignment Report: 2026-W33

## Drift Status
- **Drift Status:** NO_DRIFT_DETECTED_WITHIN_R3_AVAILABLE_AUDIT_SCOPE
- **Drifted Nodes:** NONE_OBSERVED_WITHIN_AUDIT_SCOPE
- **Scope Note:** This status is bounded to the dimensions and evidence available to R3. It does not establish global semantic stability, persistent-storage continuity, or operational-transition absence.

## Phase Boundaries
- **Synthetic Transitions:** 6
- **Operational Transitions:** NOT_COMPUTED
- **Reason:** Event origin cannot be separated
- **Interpretation:** Synthetic/test transitions are not counted as observed operational phase changes.

## Convergence Metrics
- **Hard Rollback:** PRESENT
- **Daily Convergence:**
  - 2026-08-10: SUCCESS
  - 2026-08-11: SUCCESS_WITH_REJECTED_SIGNAL
  - 2026-08-12: SUCCESS_WITH_REJECTED_SIGNAL
  - 2026-08-13: SUCCESS_WITH_REJECTED_SIGNAL
  - 2026-08-14: SUCCESS_WITH_REJECTED_SIGNAL
  - 2026-08-15: SUCCESS_WITH_REJECTED_SIGNAL
  - 2026-08-16: SUCCESS_WITH_REJECTED_SIGNAL
- **Missing Dates:** NONE
- **Aggregation Boundary:** A Daily `REJECTED_FROM_INGESTION` remains visible in Weekly status and is not erased by an otherwise successful run.

## Data Source Boundaries
- exact source
- verifiable URL
- specific content
- check time
- ingestion acceptance is not a truth label
- source credibility and epistemic support are assessed separately

## Test Results
- **Snapshot Type:** R3_EXECUTION_TEST_SNAPSHOT
- **Total:** 27
- **Passed:** 27
- **Failed:** 0
- **Errors:** 0
- **Skipped:** 0
- **Historical Boundary:** This 27/27 result describes the test snapshot associated with the R3 run. It does not overwrite the 2026-08-10 R2 historical result of 26 passed / 1 error, nor does it imply every R2 run in W33 was 27/27.

## Persistence Boundary
- R1 graph-write/ingestion statements and R2 database observations are not assumed to refer to the same persistent storage identity unless that identity is explicitly verified.
- A bare SQLite `:memory:` database is connection-local and ceases to exist when its connection closes; therefore `Nodes=0 / Edges=0` in an R2 run cannot by itself prove that an earlier R1 ingestion failed or persisted.
- **W33 Cross-Task Persistence Status:** PERSISTENCE_LINK_NOT_VERIFIED
