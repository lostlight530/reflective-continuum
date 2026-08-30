# Weekly Alignment Report — 2026-W35

> **Post-hoc calibration — 2026-08-31**
>
> - Original record: `PRESERVED_BY_GIT_HISTORY`
> - Original execution state: `STABLE / 27 PASSED`
> - Current disposition: `WEEKLY_CLOSED_WITH_ALL_ROLLBACKS_AND_SCOPE_BOUNDARIES_RETAINED`
> - Reason: the original report omitted three of seven R1 rollback events and did not bound `STABLE` or the latest 27/27 result.
> - Evidence boundary: this record aggregates existing R1/R2 files; it does not replay tasks or establish shared-store continuity.
> - Canonical authority: [`../monthly/2026-08-through-30-stage-audit.md`](../monthly/2026-08-through-30-stage-audit.md)
> - Execution replayed for this annotation: `NO`

## Window and coverage

- ISO week: `2026-W35`
- Window: 2026-08-24 through 2026-08-30
- R1 paths: `7/7`
- R2 paths: `7/7`
- Missing dates: none
- Weekly lifecycle: `CLOSED`

## Drift and phase boundary

- Drift state: `NO_DRIFT_DETECTED_WITHIN_AVAILABLE_R3_AUDIT_SCOPE`
- Drifted nodes: none reported
- Synthetic transitions: `NOT_COMPUTED`
- Operational transitions: `NOT_COMPUTED`
- Replay transitions: `NOT_COMPUTED`
- Unknown-origin transitions: `NOT_COMPUTED`
- Reason: event origin cannot be separated from retained material

`STABLE` is not a global semantic, persistence, health, or convergence claim.

## Daily R1 outcomes and rollbacks

Every day reports `SUCCESS_WITH_REJECTED_SIGNAL`: two accepted local outcomes and one rejected local outcome. All seven rejected signals remain visible.

| Date | Rejected signal | Reason |
| --- | --- | --- |
| 08-24 | `AI_ALIGN_260614315` | `reflection_depth_exhausted` |
| 08-25 | `sig-metacognition-neurosymbolic` | `reflection_depth_exhausted` |
| 08-26 | retained third signal | `reflection_depth_exhausted` |
| 08-27 | `signal_3` | `reflection_depth_exhausted` |
| 08-28 | `signal_wiki_ai_safety` | `reflection_depth_exhausted` |
| 08-29 | `ai_safety_wiki` | `reflection_depth_exhausted` |
| 08-30 | `metacognition_llms_loose_coupling` | `reflection_depth_exhausted` |

`SUCCESS_WITH_REJECTED_SIGNAL` is a composite local control-flow outcome, not an all-green health state.

## Daily R2 inheritance

| Date range | Nodes / Edges | Test result | Current interpretation |
| --- | --- | --- | --- |
| 08-24–08-27 | 0 / 0 | 26 passed / 1 failed each day | `NOT_ALL_GREEN; INDETERMINATE_EMPTY_STATE` |
| 08-28–08-30 | 0 / 0 | 27 passed each day | `RUN_LOCAL_ALL_PASS; INDETERMINATE_EMPTY_STATE` |

Later 27/27 observations do not rewrite earlier failures. Same date does not prove that R1 and R2 opened the same store.

## Weekly verdict

`WEEKLY_CLOSED_WITH_7_ROLLBACKS_4_FAILED_SELFTEST_DAYS_3_RUN_LOCAL_ALL_PASS_DAYS_EMPTY_STATE_INDETERMINATE_AND_SHARED_STORE_UNVERIFIED`
