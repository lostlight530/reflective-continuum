# GAS R4 Weekly Reference and Graph Topology Audit — 2026-W47

## Contract and identity
- Repository: lostlight530/reflective-continuum
- Closed ISO week: `2026-W47`, 2026-11-16 through 2026-11-22 inclusive, `Asia/Shanghai`; actual synthesis date 2026-11-23
- Producer: GPT-6 / GPT_NATIVE / HUMAN_REQUESTED / NOT_JULES_REPLAY
- Base Main SHA: `9a8d31c85bedee98e5a03dd0ce6490eb75feee67`
- Owning boundary: `GOVERNANCE/MAINTENANCE.md`, `RESEARCH/daily/README.md`; R1, R2, R3 and R4 maintain independent task and execution identities
- Input corpus: exact 7/7 R1 and 7/7 R2 merged-main file reads, 14 source blobs in matrix below; inheritance from same experimental receipt is **not** independent replication
- Full native GAS worktree, `CODE/tasks/cortex_selfcheck.py`, actual R1 ingestion, store comparisons and end-to-end tests were NOT_EXECUTED in this audit environment
- Canonical Task: `reflective/gas/R4` / Weekly
- Run Identity: `reflective-continuum/gas/R4/2026-W47/GPT_NATIVE/9a8d31c85bedee98e5a03dd0ce6490eb75feee67/w47-reference-invariant-audit-01`
- Task Status: `DOCUMENTARY_REFERENCE_CONTRACT_AUDIT / GRAPH_TOPOLOGY_NOT_COMPUTED`
- Write Scope: `RESEARCH/weekly/2026-W47-reference-audit.md`

## W47 exact documentary source matrix
| Logical date | R1 original path and blob | R2 original path and blob | Reference-evidence boundary |
|---|---|---|---|
| 2026-11-16 | `RESEARCH/daily/2026-11-16-dehydrated-report.md` @ `0c384a591072f12b802ab56dd90fd6d6729f1c21` | `RESEARCH/daily/2026-11-16-cortex-selfcheck.md` @ `1c29891b5103f57a8836a9dc537dd2615df88acc` | source-only intake; no named R1 GraphDB and no R2 selfcheck |
| 2026-11-17 | `RESEARCH/daily/2026-11-17-dehydrated-report.md` @ `f77dd69cb141aee81c6f8f43ea03a747cce36ccc` | `RESEARCH/daily/2026-11-17-cortex-selfcheck.md` @ `dd370cf3a762784dc58b4b7d69d124485d765983` | event-order source candidate; no named GraphDB execution |
| 2026-11-18 | `RESEARCH/daily/2026-11-18-dehydrated-report.md` @ `0b21ecbeacbc964d8c3ce04b55edbf4c05dbea79` | `RESEARCH/daily/2026-11-18-cortex-selfcheck.md` @ `b50ce51993a6dded04ec86296c2e783aa2d53035` | CLI default in-memory versus named persistence source boundary |
| 2026-11-19 | `RESEARCH/daily/2026-11-19-dehydrated-report.md` @ `b084ebab4b7cdd1d124df466e0d5ba3bbe07b774` | `RESEARCH/daily/2026-11-19-cortex-selfcheck.md` @ `373ac7bbb913d63d060788eb3d3d07bf469dc289` | standalone stdlib SQLite close/reopen control, separate from GAS |
| 2026-11-20 | `RESEARCH/daily/2026-11-20-dehydrated-report.md` @ `7d50219d4b26e7f539268a4fc1f0ad1dcaa8058b` | `RESEARCH/daily/2026-11-20-cortex-selfcheck.md` @ `0d2dcc6f8fdc4fd756c26cf13bfba1220927f7d3` | standalone SQLite same-path same-count file replacement counterexample |
| 2026-11-21 | `RESEARCH/daily/2026-11-21-dehydrated-report.md` @ `3e00d017a7dba17ba950b2563a8f6964e9ae1668` | `RESEARCH/daily/2026-11-21-cortex-selfcheck.md` @ `dfe879ff0f3438a3b4a19f212007f7877113cdc9` | standalone SQLite WAL old/new snapshot divergence |
| 2026-11-22 | `RESEARCH/daily/2026-11-22-dehydrated-report.md` @ `80daa87a4a264f8667c0b1aa95c31d8ad24452a5` | `RESEARCH/daily/2026-11-22-cortex-selfcheck.md` @ `f47fe42b3cb2b040472c0b67e20c57037b8a26bb` | standalone SQLite per-connection FK mode and orphan contrast |

## Reference, orphan and topology evidence
- The R4 task requires current actual graph node/edge identifiers, references, missing endpoints, stale links, index state and a named comparable store snapshot. The W47 R1/R2 originals do not contain a native executed GAS GraphDB state with independently opened current-week R2 verification.
- Nov16 source proposal, Nov17 event order and Nov18 memory-versus-durable-file inspection are hypotheses, not accepted node IDs. No entity graph can be reconstructed from a dated Markdown record alone.
- Nov19 separate stdlib SQLite persistence control shows that a named file can outlive a connection; it does not exercise `GraphDB` or `CODE/**` schemas.
- Nov20 separate synthetic replaced-file control shows path equality and row-count equality are inadequate to establish the historical graph identity used for a reference audit.
- Nov21 separately executed WAL control shows transaction-view divergence even while same path/inode/file main hash hold. An R4 broken-reference result on one snapshot must not be assigned to another snapshot without a recorded migration or state transition.
- Nov22 one separate per-connection FK control shows a writer with `PRAGMA foreign_keys=0` can commit a child lacking a parent; `PRAGMA integrity_check=ok` is not adequate to rule out declared-FK violations. For graphs with application-managed edges and no declared SQL FKs, `foreign_key_check` alone is likewise insufficient.
- These four controls were authored under independent R1 experiment identities on distinct days and discussed in R2; R4 **inherits** them without adding four new runs or claiming that all controls tested real GAS schema.
- W47 actual graph edges, node references, orphan counts, disconnected-component count, external link freshness, FTS5 index health, topology revision and PageRank/centrality: `NOT_COMPUTED` rather than zero.
- Prior W46 ephemeral two-node, zero-edge same-job fixtures do not provide today's graph identity or cross-day reference graph.
- Direct latest [scheduled CodeQL run 45084680250](https://github.com/lostlight530/reflective-continuum/actions/runs/45084680250) job-step inspection shows CodeQL analysis only. This does not establish R1/R2 native GraphDB execution or live reference validation.

## Verification requirements and negative controls
- A legitimate R4 positive case must bind `run_id`, `store_id`, actual opened URI, snapshot/transaction revision, node/edge primary-key set, reference-check algorithm and raw stdout/stderr/exit.
- Negative N1: identical source path/row count but different file inode/digest/row IDs after replacement; reject store equivalence.
- Negative N2: WAL old reader and post-commit new reader; reject equal-snapshot inference from unchanged main DB file digest.
- Negative N3: SQL FK defined but disabled on writer; `integrity_check=ok` and missing parent co-occur; use exact schema and per-connection mode.
- Negative N4: application-managed references without a SQL FOREIGN KEY; require independent edge endpoint and source-link verification.
- Negative N5: two independent `:memory:` R2 checks could be green and unrelated to R1. Same date and green status do not identify shared state.
- Negative N6: source URLs can become stale with SQLite structure healthy; external reference reachability needs a separately timestamped network check and authoritative target identity.
- A valid edge set in one store cannot by itself establish semantic truth or phase transition, and a missing executable run cannot be called healthy, degraded, or empty.

## R4 disposition and counterevidence
- Documentary coverage: 7/7 R1 + 7/7 R2 canonical main blobs.
- Independent native reference checker execution: `NOT_EXECUTED`.
- Comparable current graph store: `NOT_ESTABLISHED`.
- Current orphan/missing external reference counts and graph topology: `NOT_COMPUTED`.
- Reference-health decision: `NO_DECISION / HOLD_FOR_NAMED_GRAPH_STATE`.
- Counterevidence: path/count equality, stale WAL readers and disabled foreign-key enforcement are concrete demonstrated failure modes of shortcut oracles, but **not observed GAS incidents**.

## EVIDENCE_DELTA
- NEW_EVIDENCE: exact R1/R2 W47 source custody and explicit graph-reference oracle completeness requirements.
- CORRECTED_INTERPRETATION: `sqlite3.integrity_check`, declared foreign keys, application-managed graph edges, external URLs, and snapshot revision each test different predicates.
- UNCHANGED_BOUNDARY: R1 ingestion != R2 structural check != R4 reference validity; an inherited standalone control is not a newly executed R4 experiment.
- NEW_COUNTEREVIDENCE: identical path with replaced file, WAL snapshot mismatch and per-connection FK disablement invalidate naive graph-health promotions.
- UNKNOWN_RETAINED: actually stored reference IDs, reachable targets, orphan count, graph revision and persistence identity.
- NEXT_RETEST_CONDITION: first establish native R1 persisted store and separate R2 exact snapshot receipt; then inspect real CODE GraphDB schema and run R4 node/edge/URL reference checks with positive and negative fixtures.

## Delivery and checks
- Actual performed: exact 14 remote W47 source reads and preflight; scheduled CodeQL job-step classification.
- NOT_EXECUTED: actual R4 topology checker, GAS ingestion/selfcheck, network reference checks and full local tests.
- R3/R4 form one weekly delivery but are two independent task/run identities with no pooled execution credit.
- Only W47 weekly canonical record changes proposed. November R5 NOT_DUE; Human Maintainer review/merge PENDING.
