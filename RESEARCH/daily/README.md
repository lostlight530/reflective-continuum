# Daily observation contract

Each logical day retains two independent observation surfaces:

- R1 `YYYY-MM-DD-dehydrated-report.md`: fixed-fixture repeatability, source identity/support, signal ingestion outcome, rollback reason, local entropy/phase, and store identity when retained.
- R2 `YYYY-MM-DD-cortex-selfcheck.md`: opened database identity, initialization/integrity checks, nodes/edges, test totals, drift state, and persistence link when retained.

The governing invariants are:

```text
CHECK_PROGRAM_EXECUTED != CHECKED_SYSTEM_HEALTHY
MAJORITY_TESTS_PASSED != ALL_GREEN
EMPTY_STATE != HEALTHY
INGESTION_ACCEPTED != SOURCE_TRUE
SAME_DATE != SAME_STORE
```

`Nodes=0 / Edges=0` is `INDETERMINATE_EMPTY_STATE`. Possible explanations remain concurrent: no valid ingestion, a new database, a wrong persistence path, a failed write, an unexpected database path/connection, or separate temporary stores for R1 and R2. A 26/27 result is retained as `26 passed / 1 failed` (or error), never summarized as healthy/all green. If the failing test identity was not retained, use `FAILURE_IDENTITY_NOT_RETAINED`.

`ACCEPTED` describes local control flow; `REJECTED_FROM_INGESTION` describes policy/transaction outcome. Neither establishes external truth. Same date or digest does not prove shared persistence; retain path/URI/connection/store identity.

R3/R4 Weekly may inherit or downgrade Daily evidence, never erase it. R5 Monthly closes only after the natural month ends. See the [August ledger](../monthly/2026-08-through-27-stage-audit.md) and [maintenance contract](../../GOVERNANCE/MAINTENANCE.md).
