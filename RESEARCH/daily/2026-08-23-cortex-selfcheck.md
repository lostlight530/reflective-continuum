# Cortex Selfcheck Report

## Module Health
- Module Import/Init/Execution: SUCCESS

## Rule Engine
- Status: HEALTHY

## DB State
- Nodes: 0
- Edges: 0
- Context: INDETERMINATE_EMPTY_STATE
- Possible causes:
  - 没有有效摄入
  - 数据库刚初始化
  - 持久化路径错误
  - 写入失败
  - 当前数据库路径并非预期路径

## Incremental Drift
- Status: NOT_COMPUTED

## 状态解释
由于数据库中 Nodes=0 且 Edges=0，当前无法确认其为空的具体原因，不排除数据库刚初始化、写入失败或未发生有效摄入的可能性。

## 测试统计
- Total: 27
- Passed: 26
- Failed: 1
- Errors: 0
- Skipped: 0
