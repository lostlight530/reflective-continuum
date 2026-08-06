# Cortex Selfcheck Report

**Date:** 2026-08-06
**Observation Time:** 2026-08-06T10:18:08.076327+00:00

## Module Health

- **CODE.continuum_db**: FAIL
  - Stage: Import/Init
  - Exception Type: OperationalError
  - Exception Message: no such savepoint: test
  - Traceback:
    ```
    Traceback (most recent call last):
      File "/app/RESEARCH/daily/temp_module_test.py", line 21, in <module>
        with db.savepoint("test"):
             ^^^^^^^^^^^^^^^^^^^^
      File "/home/jules/.pyenv/versions/3.12.13/lib/python3.12/contextlib.py", line 144, in __exit__
        next(self.gen)
      File "/app/CODE/continuum_db.py", line 106, in savepoint
        self.commit_fork(name)
      File "/app/CODE/continuum_db.py", line 90, in commit_fork
        self.conn.execute(f"RELEASE SAVEPOINT {self._identifier(name)}")
    sqlite3.OperationalError: no such savepoint: test
    ```

- **CODE.cortex_observer**: FAIL
  - Stage: Import/Init
  - Exception Type: TypeError
  - Exception Message: CortexObserver.__init__() missing 2 required positional arguments: 'db' and 'rule_engine'
  - Traceback:
    ```
    Traceback (most recent call last):
      File "/app/RESEARCH/daily/temp_module_test.py", line 33, in <module>
        obs = CortexObserver()
              ^^^^^^^^^^^^^^^^
    TypeError: CortexObserver.__init__() missing 2 required positional arguments: 'db' and 'rule_engine'
    ```

- **CODE.drift_detector**: OK
- **CODE.reflective_validator**: OK
- **CODE.entropy_analyzer**: OK

## Rule Engine

- Healthy: true
- Checks:
  - foreign_keys: true
  - fts5: true
  - initialization: true
  - integrity: true
  - rule_engine: true

## DB State

- Nodes: 0
- Edges: 0

## Incremental Drift

- Status: NOT_COMPUTED

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