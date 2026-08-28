# R3 Weekly Alignment Report: 2026-W32

> **Post-hoc calibration — 2026-08-28**
>
> - Original record: `PRESERVED`
> - Original execution state: `WEEKLY_ALIGNMENT_RESULT_RETAINED`
> - Current disposition: `NOT_ALL_GREEN / PERSISTENCE_LINK_NOT_VERIFIED`
> - Reason: 26 passed / 1 error days survive weekly aggregation; repeated digests prove fixture repeatability only.
> - Evidence boundary: no durable R1↔R2 continuity, semantic stability, or general alignment is established.
> - Canonical authority: [`2026-08-through-27-stage-audit.md`](../monthly/2026-08-through-27-stage-audit.md)
> - Execution replayed for this annotation: `NO`

## Semantic Drift
- **Drift Status:** STABLE
- **Drifted Nodes:** NONE

## Phase Boundaries
- **Synthetic Transitions:** 6
- **Operational Transitions:** NOT_COMPUTED
- **Reason:** Event origin cannot be separated

## Ingestion Metrics
- **Hard Rollback:** PRESENT
- **Daily report-level rollback dates:** 2026-08-05, 2026-08-06, 2026-08-07, 2026-08-08, 2026-08-09
- **Daily report-level rollback count:** 5
- **Counting rule:** one daily R1 report with a rejected ingestion / `HARD_ROLLBACK` block counts as one report-level rollback event. Repeated or duplicated raw `ingestion.log` blocks are not counted as independent events.
- **Daily Convergence:**
  - 2026-08-03: SUCCESS
  - 2026-08-04: SUCCESS
  - 2026-08-05: SUCCESS_WITH_REJECTED_SIGNAL
  - 2026-08-06: SUCCESS_WITH_REJECTED_SIGNAL
  - 2026-08-07: SUCCESS_WITH_REJECTED_SIGNAL
  - 2026-08-08: SUCCESS_WITH_REJECTED_SIGNAL
  - 2026-08-09: SUCCESS_WITH_REJECTED_SIGNAL
- **Missing R1 Dates:** NONE

## R2 Selfcheck Coverage
- 2026-08-03: ARTIFACT_PRESENT
- 2026-08-04: ARTIFACT_PRESENT
- 2026-08-05: ARTIFACT_PRESENT
- 2026-08-06: ORIGINAL_ARTIFACT_MISSING; historical result unknown; reconciliation record added 2026-08-10
- 2026-08-07: ARTIFACT_PRESENT
- 2026-08-08: ARTIFACT_PRESENT
- 2026-08-09: ARTIFACT_PRESENT
- **Interpretation:** R1 daily convergence coverage is complete for W32, while R2 artifact coverage has one historical gap. The R2 gap must not be rewritten as a historical success using a later execution.

## Data Source Boundaries
- Data boundaries for R1 external signals required exact source, verifiable URL, specific content, and check time. Failure to verify any signal results in SOURCE_UNAVAILABLE and ingestion BLOCKED.
- A rejected signal with `Write Status: NOT_EXECUTED` is preserved as a hard rollback / rejection event; it does not turn the whole daily convergence run into a failure.

## Test Results
- **Total:** 27
- **Passed:** 27
- **Failed:** 0
- **Errors:** 0
- **Skipped:** 0
- **Scope:** these are the test results recorded by the W32 R3 weekly run itself. They do not reconstruct the missing historical 2026-08-06 R2 selfcheck test counts.

## Reconciliation Note — 2026-08-10
- The original W32 report said `Hard Rollback: NONE` while simultaneously noting that rollback events were logged in daily ingestion events. Current daily R1 artifacts show five report-level hard rollbacks, so `NONE` was semantically incorrect.
- The corrected weekly summary preserves successful daily convergence while separately recording rejected signals and the R2 historical artifact gap.
