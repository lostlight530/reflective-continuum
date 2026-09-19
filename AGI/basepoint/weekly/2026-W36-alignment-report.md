# Weekly Alignment Report — 2026-W36

## 数据来源边界 (Data source boundaries)

- ISO week: 2026-W36
- Window: 2026-08-31 through 2026-09-06
- R1 paths: 7/7
- R2 paths: 7/7
- 缺失日期 (Missing dates): none

## Drift 状态 (Drift and phase boundary)

- Drift 状态: STABLE
- Drifted Nodes: none
- Synthetic Transitions: NOT_COMPUTED
- Operational Transitions: NOT_COMPUTED
- Replay Transitions: NOT_COMPUTED
- Unknown-Origin Transitions: NOT_COMPUTED
- Reason: Event origin cannot be separated

## Daily Convergence

- 2026-08-31: SUCCESS_WITH_REJECTED_SIGNAL
- 2026-09-01: SUCCESS
- 2026-09-02: SUCCESS_WITH_REJECTED_SIGNAL
- 2026-09-03: SUCCESS_WITH_REJECTED_SIGNAL
- 2026-09-04: SUCCESS
- 2026-09-05: SUCCESS_WITH_REJECTED_SIGNAL
- 2026-09-06: SUCCESS_WITH_REJECTED_SIGNAL

## Hard Rollback

- 2026-08-31: arxiv-2605-17292 | reflection_depth_exhausted
- 2026-09-01: Agent_Safety_1 | reflection_depth_exhausted
- 2026-09-02: arxiv-2606-14315 | reflection_depth_exhausted
- 2026-09-03: signal_2026_03 | reflection_depth_exhausted
- 2026-09-05: arxiv-2608-27910 | reflection_depth_exhausted
- 2026-09-06: signal_futureagi_safety_3 | reflection_depth_exhausted

## 测试结果 (Test Results)

- 2026-08-31: 27/27 Passed
- 2026-09-01: 27/27 Passed
- 2026-09-02: 27/27 Passed
- 2026-09-03: 27/27 Passed
- 2026-09-04: 27/27 Passed
- 2026-09-05: 27/27 Passed
- 2026-09-06: 27/27 Passed

## AGI_BASEPOINT_2026-09-19

Basepoint State: WEEKLY_ALIGNMENT_BOUNDED
Origin Continuity: PRESERVED

- `STABLE` is bounded to the semantic-drift audit surface; it is not a whole-system health conclusion.
- W36 includes a 2026-09-05 selfcheck with two module-level failures while separately recording 27/27 tests; weekly test aggregation must not erase that parallel evidence.
- Transition metrics remain `NOT_COMPUTED`; Daily Hard Rollbacks remain valid rejected-ingestion events.
