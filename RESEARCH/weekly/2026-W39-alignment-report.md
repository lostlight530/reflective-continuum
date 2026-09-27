## Drift 状态
STABLE

Scope: `STABLE` is limited to the executed in-memory semantic audit (`database: :memory:`), FTS5 lexical ranking, and caller-selected queries recorded in `semantic_drift_audit.log`. It does **not** establish persistent GAS-store stability, shared R1/R2 state, repository-wide health, or absence of untested drift.

## Drifted Nodes
None

## Synthetic Transitions
NOT_COMPUTED

## Operational Transitions
Operational Metrics: NOT_COMPUTED
Reason: Event origin cannot be separated

## Replay Transitions
NOT_COMPUTED

## Unknown-Origin Transitions
NOT_COMPUTED

## Hard Rollback
### 2026-09-21
```
RUN_BEGIN
Run ID: 00713897-172c-4952-8a7a-5bbb6eca2b09
HARD_ROLLBACK
Signal ID: signal_ai_safety
Reason: reflection_depth_exhausted
Observer Output: ProcessResult(accepted=False, phase='LIQUID', reflection_depth=3, entropy_nats=1.0986122886681096, reasons=('reflection_depth_exhausted',))
Graph Write Status: False
Next Action: Do not retry. Report as REJECTED_FROM_INGESTION.
RUN_END
```
### 2026-09-22
```
RUN_BEGIN
Run ID: 8abb0411-f6c3-4c6d-82d5-376e5d010e5c
HARD_ROLLBACK
Signal ID: signal_ai_alignment
Reason: reflection_depth_exhausted
Observer Output: ProcessResult(accepted=False, phase='LIQUID', reflection_depth=3, entropy_nats=1.0986122886681096, reasons=('reflection_depth_exhausted',))
Graph Write Status: False
Next Action: REJECTED_FROM_INGESTION
RUN_END
```
### 2026-09-23
```
RUN_BEGIN
HARD_ROLLBACK
Run ID: b8b4a072-80d1-414d-b88b-f0df1ec24b0a
Signal ID: signal_metacognition_003
Reason: reflection_depth_exhausted
Observer Output: ProcessResult(accepted=False, phase='LIQUID', reflection_depth=3, entropy_nats=1.0986122886681096, reasons=('reflection_depth_exhausted',))
Graph Write Status: False
Next Action: Do not retry. Report as REJECTED_FROM_INGESTION.
RUN_END
```
### 2026-09-24
```
HARD_ROLLBACK
Run ID: auto_generated
Signal ID: signal_ai_safety_df569ab9
Rejection Reasons: reflection_depth_exhausted
Observer Output: {"accepted": false, "id": "signal_ai_safety_df569ab9", "reasons": ["reflection_depth_exhausted"]}
Graph Write Status: False
Subsequent Action: Signal Discarded
```
### 2026-09-25
```
RUN_BEGIN
HARD_ROLLBACK
Run ID: 911bde12-a54b-4f6f-b06f-83affac6eed8
Signal ID: signal_determinism
Reason: reflection_depth_exhausted
Observer Output: ProcessResult(accepted=False, phase='LIQUID', reflection_depth=3, entropy_nats=1.0986122886681096, reasons=('reflection_depth_exhausted',))
Graph Write Status: False
Next Action: Do not retry. Report as REJECTED_FROM_INGESTION.
RUN_END
```
### 2026-09-26
```
HARD_ROLLBACK
Run ID: 65d2c6b9-b9f2-4a8c-8621-df2dd3b7aad2
RUN_BEGIN
Signal ID: signal_3
Reason: reflection_depth_exhausted
Observer Output: ProcessResult(accepted=False, phase='LIQUID', reflection_depth=3, entropy_nats=1.0986122886681096, reasons=('reflection_depth_exhausted',))
Graph Write Status: False
Next Action: Do not retry. Report as REJECTED_FROM_INGESTION.
RUN_END
```
### 2026-09-27
```
HARD_ROLLBACK
Run ID: e33d4392-b16c-4d97-aca5-8dcadb5c863e
RUN_BEGIN
Signal ID: signal_3
Reason: reflection_depth_exhausted
Observer Output: ProcessResult(accepted=False, phase='LIQUID', reflection_depth=3, entropy_nats=1.0986122886681096, reasons=('reflection_depth_exhausted',))
Graph Write Status: False
Next Action: Do not retry. Report as REJECTED_FROM_INGESTION.
RUN_END
```

## Daily Convergence
- 2026-09-21: SUCCESS_WITH_REJECTED_SIGNAL
- 2026-09-22: SUCCESS_WITH_REJECTED_SIGNAL
- 2026-09-23: {"distinct_snapshots": 1, "iterations": 100, "repeatable": true, "scope": "fixed local SQLite fixture"}
- 2026-09-24: SUCCESS_WITH_REJECTED_SIGNAL
- 2026-09-25: SUCCESS_WITH_REJECTED_SIGNAL
- 2026-09-26: FIXED_FIXTURE_REPEATABILITY_OBSERVED
- 2026-09-27: FIXED_FIXTURE_REPEATABILITY_OBSERVED

## 缺失日期
None

## 数据来源边界
- https://en.wikipedia.org/api/rest_v1/page/summary/AI_alignment
- https://en.wikipedia.org/api/rest_v1/page/summary/AI_safety
- https://en.wikipedia.org/api/rest_v1/page/summary/Metacognition
- https://en.wikipedia.org/wiki/AI_alignment
- https://en.wikipedia.org/wiki/AI_safety
- https://en.wikipedia.org/wiki/Determinism
- https://en.wikipedia.org/wiki/Metacognition

## 测试结果
- Total: 189
- Passed: 182
- Failed: 7
- Errors: 0
- Skipped: 0
- Interpretation: `182/189 != full PASS`. The retained aggregate does not identify the seven failed tests, so their exact failure causes remain `UNKNOWN` in this weekly artifact.
