# Cortex Selfcheck Report

## Module Health
- continuum_db: SUCCESS
- cortex_observer: SUCCESS
- drift_detector: SUCCESS
- reflective_validator: SUCCESS
- entropy_analyzer: SUCCESS

## Rule Engine
- foreign_keys: true
- fts5: true
- initialization: true
- integrity: true
- rule_engine: true

## DB State
- edges: 0
- nodes: 0

## Incremental Drift
NOT_COMPUTED

## 状态解释
Context: INDETERMINATE_EMPTY_STATE

Possible causes:
- 没有有效摄入
- 数据库刚初始化
- 持久化路径错误
- 写入失败
- 当前数据库路径并非预期路径

## Test Statistics
- Total: 27
- Passed: 26
- Failed: 1
- Errors: 0
- Skipped: 0
