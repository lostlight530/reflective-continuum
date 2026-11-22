# GAS Native Daily R2 — 2026-11-22 / selfcheck must identify enforced invariants as well as store identity

## Task and source identity
- Repository: `lostlight530/reflective-continuum`
- Canonical task: `reflective/gas/R2`, independent Daily Cortex Selfcheck, 2026-11-22, Asia/Shanghai
- Producer: GPT-6 / GPT_NATIVE / HUMAN_REQUESTED / NOT_JULES_REPLAY
- Base main: `7a26a8c9806393a41795cff0900ecd57da0c6a1f`
- Run identity: `reflective-continuum/gas/R2/2026-11-22/GPT_NATIVE/7a26a8c/fk-selfcheck-boundary-01`
- Owning contracts: `GOVERNANCE/MAINTENANCE.md` blob `7c6ffcf5b8156fa96dc8d4b7187756c7434bd28a`; `RESEARCH/daily/README.md` blob `29e0b9869fcbb7dab9dd0d0e7e45442633af4ac5`
- Canonical path: `RESEARCH/daily/2026-11-22-cortex-selfcheck.md`
- Sibling R1 original file: `RESEARCH/daily/2026-11-22-dehydrated-report.md`, formal ingestion `NOT_EXECUTED`, named GAS store `NOT_ESTABLISHED`
- Formal R2 status: `BLOCKED_NO_IDENTIFIED_GAS_STORE / CORTEX_SELFCHECK_NOT_EXECUTED / DRIFT_NOT_COMPUTED`

## Observed versus inherited experiment evidence
- R1 owns one independently executed **standalone SQLite fixture**: `STANDALONE_SQLITE_CONNECTION_LOCAL_FK_2026_11_22_01`.
- This R2 **did not execute** a second SQLite test, did not run its own GAS selfcheck, and receives no duplicate empirical run credit.
- R1's control observed one named temporary SQLite DB with two connections: A `foreign_keys=1`, B `foreign_keys=0`. B committed a child pointing at an absent parent, both connections read the same child; `integrity_check=ok` but `foreign_key_check` returned `[["children",1,"parents",0]]`.
- Observed implication for R2 **only as a candidate verification requirement**: claiming relational graph integrity from a generic SQLite `integrity_check` is incomplete when the actual graph schema uses declared SQL foreign keys and writers can disable enforcement.
- The experiment does not establish that the actual GAS GraphDB uses these declarations, nor that native R2 lacks other graph-level checks. The repository's already declared structural checks may be independently stronger; their execution is not shown.
- Proposed R2 evidence fields: `opened_store_uri`, `store_revision/snapshot`, `connection_id`, `schema_revision`, `foreign_key_list`, `PRAGMA_foreign_keys_value`, `foreign_key_check_result`, `graph_edge_reference_check`, `integrity_check_result`, `readback_keys`, `R1_commit_receipt`.
- A store path without a matching transaction view is not enough (November 21 WAL control); a matching snapshot without enforcing the specific invariants is also not enough (November 22 FK control).

## Formal R2 execution ledger
- Intended command: `PYTHONPATH=. python3 CODE/tasks/cortex_selfcheck.py --database <named verified GAS store>` — **NOT_EXECUTED**; CLI arguments must be confirmed against real runner before invocation.
- Intended regression: `PYTHONPATH=. python3 -m unittest discover tests/ -v` — **NOT_EXECUTED**
- Actual formal R2 stdout, stderr, exit, R2 opened-store identity, full test totals and failing test IDs: **NOT_AVAILABLE**
- GAS schema details, graph nodes/edges, store persistence, initialization, FTS5, structural/foreign-key verification, PageRank, entropy, phase and convergence: **NOT_COMPUTED**
- R1 formal ingestion accepted/rejected evidence: **NOT_AVAILABLE**; no shared GraphDB can be inferred
- R1/R2 `SAME_STORE`: **NOT_ESTABLISHED**; actual comparable graph states: **NOT_AVAILABLE**
- Semantic/structural drift and topology health: **NOT_COMPUTED**, neither zero nor positive
- Independent formal R2 execution count: **0**; source review and inherited external SQLite receipt only

## Adversarial verification cases for a later native run
- Positive P1: actual R1 ingests accepted graph edges in a named persisted GraphDB, R2 opens an explicitly documented compatible snapshot and confirms each edge's endpoints and any policy-managed referential constraints.
- Negative N1: writer connection has `PRAGMA foreign_keys=0` while reader checks generic `integrity_check=ok`; reject any conclusion of enforced SQL references without `foreign_key_check`.
- Negative N2: schema has no FOREIGN KEY declarations; do **not** interpret the absence of foreign-key violations as proof all application-managed graph edge references are valid.
- Negative N3: two snapshots on same filename differ due WAL, even though the FK enforcement policy matches; compare transaction/store identity before calculating drift.
- Negative N4: an R2 selfcheck creates a new empty DB and green component list; this is `INDETERMINATE_EMPTY_STATE`, not a healthy graph.
- Scope caveat: a SQLite PRAGMA result alone cannot prove source truth, state-transition legitimacy, durable cross-run memory or full graph topology correctness.

## EVIDENCE_DELTA
- NEW_EVIDENCE: inherited **one** R1 standalone connection-mode/orphan contrast as a stronger comparator design input, not as an independent R2 run.
- CORRECTED_INTERPRETATION: R2 must check the graph's actual referential invariant, not assume generic SQLite file integrity implies edge validity.
- UNCHANGED_BOUNDARY: SAME_DATE != SAME_STORE; same store != same snapshot or same constraint enforcement; R1 receipt != R2 result.
- NEW_COUNTEREVIDENCE: if graph edges are not backed by FOREIGN KEY constraints, `foreign_key_check` is an inadequate oracle by itself.
- UNKNOWN_RETAINED: real GraphDB schema, actual selfcheck invocation and store, test totals, observed graph, comparable drift, persistence continuity.
- NEXT_RETEST_CONDITION: on a complete checkout, run R1 and independent R2 against an explicitly named and versioned store, inspect actual schema and implementation-driven graph referential checks and capture both raw executions. Only compute drift for comparable states.

## Delivery and governance boundary
- One original R2 Daily record in the same scoped Native PR as R1, with **separate** canonical task and run identities.
- No code, data store, automatic ingest, GraphDB health, Weekly/Monthly, Jules history, independent maintenance or governance mutation is implied.
- Human Maintainer review and merge are distinct; current Draft PR is not a runtime PASS or stored GAS graph receipt.
