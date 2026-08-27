# 2026 Evidence Baseline

- Retrieval/calibration date: 2026-08-27
- Rule: external evidence can bound a repository claim; it does not certify a local implementation by itself

## Repository implementation anchors

Current claims are interpreted through the code that actually exists:

- `CODE/continuum_db.py` — versioned SQLite graph storage, per-connection foreign keys, external-content FTS5, savepoints, lexical search, snapshot digest
- `CODE/entropy_analyzer.py` — PageRank and Shannon entropy over normalized graph-rank values
- `CODE/drift_detector.py` — structural delta, top-FTS-result change, PageRank-score delta
- `CODE/reflective_validator.py` — explicit local validation rules and AST-based standard-library import-root checking
- `CODE/cortex_observer.py` — savepoint-scoped tentative update, validation, entropy boundary, bounded reflector loop, commit/rejection rollback
- `CODE/tasks/cortex_selfcheck.py` — named checks for one opened database
- `CODE/tasks/semantic_drift_audit.py` — selected-version structural and lexical-result comparison for caller-selected queries
- `CODE/tasks/convergence_drill.py` — repeated rebuild of one fixed local SQLite fixture
- `CODE/tasks/insight_morpher.py` — caller-provided JSON signal ingestion through `CortexObserver`

External papers, protocols, standards, SDKs, or generated research remain `REFERENCE_ONLY` unless a corresponding implementation surface exists.

## Storage identity and persistence evidence

A bare SQLite `:memory:` database belongs to the connection that opened it and disappears when that connection closes.

Therefore:

- one connection's successful write/read is evidence about that connection/store
- another default `:memory:` task is a different store unless shared identity is established
- `Nodes=0 / Edges=0` in R2 is not proof that a separate R1 ingestion failed
- R1 acceptance does not imply R2 must observe the same node
- same logical date is not a persistence identity
- repeated snapshot digest alone is not durable-memory evidence

Use:

`PERSISTENCE_LINK_NOT_VERIFIED`

or, for same-day R1/R2 comparisons:

`SAME_DAY_OBSERVATIONS / SHARED_STORE_IDENTITY_NOT_ESTABLISHED`.

A continuity claim must identify the store/process/connection/path/URI whose state is said to persist.

## Selfcheck evidence

`cortex_selfcheck.py` observes the database it actually opens, including named initialization/integrity/rule-engine surfaces and node/edge counts.

With default `:memory:` behavior, a result concerns a fresh connection-local store.

A successful named check does not establish cross-run persistence, earlier R1 ingestion success, source truth, semantic correctness, or absence of historical failures.

An empty store is interpreted as:

`INDETERMINATE_EMPTY_STATE`

unless stronger state identity and history resolve why it is empty.

## Repeatability evidence

`convergence_drill.py` is a fixed-fixture repeatability drill, not a convergence proof.

Each iteration rebuilds the same local fixture in a fresh default store and computes a snapshot digest.

One distinct digest across repeated iterations means the same represented fixture serialized to the same snapshot identity under that implementation.

Current interpretation:

`RUN_LOCAL_REPEATABILITY_ONLY`.

Historical R1 labels such as `Convergence State: SUCCESS...` are read through this executable boundary. They do not establish convergence of an adaptive system across time.

## Signal-ingestion evidence

`insight_morpher.py` validates caller-provided JSON signal shape and submits signals to `CortexObserver`.

Keep separate:

- `INGESTION_OUTCOME`
- `SOURCE_IDENTITY`
- `SOURCE_CREDIBILITY`
- `SOURCE_CLAIM_SUPPORT`
- `PERSISTENCE_LINK`

`ACCEPTED != TRUE`.

`REJECTED_FROM_INGESTION != FALSE`.

A local savepoint rollback establishes rollback of tentative SQLite changes in that savepoint only. It does not establish rollback of external files, messages, services, or world-state effects.

## Search and drift evidence

Reflective search is FTS5 lexical search, not embedding search.

The historically named `compute_semantic_delta()` asks whether the **top FTS5 lexical result** for the same query changes between two versions.

Current interpretation:

`LEXICAL_TOP_RESULT_CHANGED`.

Structural delta, lexical top-result delta, and PageRank-score delta are separate evidence surfaces.

An unchanged top lexical result is not semantic equivalence. A rank shift is not correctness or instability proof.

## Entropy and phase evidence

`calculate_topological_entropy()` computes Shannon entropy in nats over normalized finite non-negative scores, typically a PageRank distribution.

`LIQUID` and `GASEOUS` are local control labels around a configured threshold.

These values do not independently establish cognition, source truth, safety, alignment, durable memory, or global convergence.

## Source authority and claim support

Source access, source identity, source authority, exact claim support, local ingestion outcome, and broader research interpretation remain separate dimensions.

If a source is reachable but does not support the proposition attributed to it, use:

`SOURCE_CLAIM_MISMATCH`.

The 2026-08-23 Wikipedia `AI_alignment` deterministic-boundary proposition remains the explicit August reference case. Later use of the same reachable page does not upgrade that unsupported proposition or create independent corroboration.

## Historical Daily evidence through 2026-08-27

Preserve:

- 2026-08-06 original R2 runtime: `HISTORICAL_RUNTIME_UNKNOWN`
- 2026-08-07 through 2026-08-10: each R2 `26 passed / 1 error`
- 2026-08-17 through 2026-08-23: each R2 `26 passed / 1 failed`
- 2026-08-24 through 2026-08-27: each R2 `26 passed / 1 failed`, `Nodes=0`, `Edges=0`, incremental drift `NOT_COMPUTED`

Thus the retained failed-test run now extends continuously from 2026-08-17 through 2026-08-27.

Later success, path completeness, or R1 ingestion acceptance does not erase this history.

## Daily → Weekly → Monthly SOP

### R1 Daily

Interpret separately:

1. fixed-fixture repeatability result
2. signal/source identity
3. local ingestion acceptance/rejection
4. rollback reason where rejected
5. local graph-derived entropy/phase
6. source-claim support
7. persistence identity only when actually evidenced

### R2 Daily

Interpret separately:

1. opened store identity/path when available
2. module/init status
3. named database/rule-engine checks
4. node/edge counts for that store
5. complete test totals including failures/errors
6. drift as `NOT_COMPUTED` when not computed
7. empty state as `INDETERMINATE_EMPTY_STATE`

### R3/R4 Weekly

Weekly synthesis may aggregate or downgrade Daily evidence but cannot:

- erase Daily failed/error days
- convert ingestion acceptance into source truth
- convert repeated digest into durable persistence
- infer R1↔R2 continuity without shared store identity
- promote lexical stability into semantic stability
- convert `NOT_COMPUTED` transitions into a no-drift theorem

W34 `STABLE` remains bounded as:

`NO_DRIFT_DETECTED_WITHIN_R3_AVAILABLE_AUDIT_SCOPE`.

At the 2026-08-27 cutoff W35 is in progress; no final W35 result is inferred.

### R5 Monthly

Formal August R5 closure remains `OPEN` until the natural monthly lifecycle has actual retained evidence. A stage audit cannot manufacture 2026-08-28 through 2026-08-31 evidence.

## Continuity and availability

Keep separate when materially different:

- logical date/period
- original execution state
- generation/delivery state
- aggregation-snapshot visibility
- current repository presence
- database/store/run identity
- evidence completeness

A later reconciliation can repair current interpretation or path coverage. It cannot manufacture an earlier runtime result.

## External architecture references

MCP, A2A, ADK state/memory documentation, agent tracing, and evaluation literature are used only to sharpen vocabulary around state scope, trajectory/outcome, and lifecycle identity unless local implementation exists.

## Current evidence summary

The strongest repository-wide interpretation through 2026-08-27 is:

- storage behavior: implemented and connection/store scoped
- graph entropy: implemented mathematical statistic
- drift: structural / lexical-top-result / rank surfaces
- observer reflection/rollback: bounded local transaction loop
- selfcheck: task-local named checks
- convergence drill: fixed-fixture repeatability only
- signal ingestion: local acceptance/rejection only
- durable R1↔R2 persistence: not verified
- retained R2 failures: preserved through 2026-08-27
- source mismatch history: preserved
- formal August R5 closure: open

Canonical current stage record: `RESEARCH/monthly/2026-08-through-27-stage-audit.md`.
