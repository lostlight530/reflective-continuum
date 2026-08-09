# Cortex Selfcheck

## Module Health
- `continuum_db`: Import, Init, Execution Success
- `cortex_observer`: Import, Init, Execution Success
- `drift_detector`: Import, Init, Execution Success
- `reflective_validator`: Import, Init, Execution Success
- `entropy_analyzer`: Import, Init, Execution Success

## Rule Engine
- Status: Healthy
- Checks:
  - initialization: true
  - foreign_keys: true
  - fts5: true
  - integrity: true
  - rule_engine: true

## DB State
- Nodes: 0
- Edges: 0

## Incremental Drift
NOT_COMPUTED

## 状态解释
Context: INDETERMINATE_EMPTY_STATE

可能原因可包括：
- 没有有效摄入
- 数据库刚初始化
- 持久化路径错误
- 写入失败
- 当前数据库路径并非预期路径

## Test Statistics
- Total: 27
- Passed: 26
- Failed: 0
- Errors: 1
- Skipped: 0
