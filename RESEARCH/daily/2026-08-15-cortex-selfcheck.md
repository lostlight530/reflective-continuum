# R2 Cortex Selfcheck Report

## Module Health

| Module | Status | Exception Type |
| :--- | :--- | :--- |
| `continuum_db` | SUCCESS | - |
| `cortex_observer` | SUCCESS | - |
| `drift_detector` | SUCCESS | - |
| `reflective_validator` | SUCCESS | - |
| `entropy_analyzer` | SUCCESS | - |

## Rule Engine

| Check | Result |
| :--- | :--- |
| `foreign_keys` | true |
| `fts5` | true |
| `initialization` | true |
| `integrity` | true |
| `rule_engine` | true |

## DB State

| Object | Count |
| :--- | :--- |
| nodes | 0 |
| edges | 0 |

## Incremental Drift

NOT_COMPUTED

## 状态解释

Context: INDETERMINATE_EMPTY_STATE

Possible Reasons:
- 没有有效摄入
- 数据库刚初始化
- 持久化路径错误
- 写入失败
- 当前数据库路径并非预期路径

## Test Execution

- **Total:** 27
- **Passed:** 27
- **Failed:** 0
- **Errors:** 0
- **Skipped:** 0
