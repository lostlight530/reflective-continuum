# Reflective Continuum maintenance contract

Status: `CANONICAL_PUBLIC_MAINTENANCE_CONTRACT`

Effective: 2026-09-17

## Scope

This contract governs repository maintenance, Jules-produced maintenance inputs, Independent GPT recovery/review, cadence interpretation, checker ownership, and delivery discipline. It does not authorize a maintenance agent to redesign research content, rewrite historical research artifacts, change `CODE/**`, change dependencies, alter `.github/**` runner/deployment surfaces, or promote private control-plane instructions into the public repository unless a separate repository-native authority explicitly requires that change.

## Cadence and independent evidence

R1 and R2 are independent Daily surfaces. R3/R4 Weekly inherit Daily observations; R5 Monthly closes only after the natural month ends. Source authority, claim support, ingestion outcome, store identity, run identity, transition origin, and test result are separate evidence classes. None substitutes for another.

A 30-day provisional audit may summarize 30 retained logical dates, but it is not a natural-month closure. Keep `MONTH_OPEN` until the final calendar date is retained or explicitly classified as missing after it becomes due.

Retain source/version/retrieval time; accepted/rejected signal and rollback reason; database path/URI/connection identity; run/log identity when claimed; nodes/edges; passed/failed/errors/skipped; failure identity; transition origin; and whether drift was computed. `INDETERMINATE_EMPTY_STATE`, failed/error tests, rollback, rejected signals, `NOT_COMPUTED`, and unresolved identity survive aggregation.

Shared persistence requires a named common store plus evidence that both tasks opened it. Same logical date, matching digest, or one task's local acceptance is insufficient. A repeated placeholder such as `Run ID: auto` is not independent-run evidence.

Semantic drift is limited to implemented structural deltas, FTS5 top-result identity, and PageRank score deltas. Entropy is PageRank-derived Shannon entropy. Convergence is fixed-fixture repeatability. Reflection/rollback is local to a SQLite savepoint. These surfaces do not establish cognition, safety, semantic truth, global stability, alignment, or durable cross-task memory.

A passing test suite is revision/environment-scoped evidence for the tests that ran. It does not establish shared persistence, source truth, non-empty graph state, operational transition provenance, or architecture-wide health.

## Maintenance identity and concurrency

A maintenance run is identified by repository, task/surface, logical period when applicable, producer, base `main` revision, and run identifier when one exists. Before any write, recover the current default branch, latest merged `main`, relevant open pull requests, active maintenance branches, and recent merged changes.

If another open PR or active branch owns the same maintenance surface or logical period, coordinate instead of manufacturing a parallel repair. A later `main` revision invalidates earlier delivery assumptions until the aggregate diff is rechecked.

Use writes only for confirmed maintenance changes. Never create or mutate a branch merely to test write permission.

## Historical and document governance

Historical research and archived audit artifacts are point-in-time evidence, not routine edit targets. A maintenance correction changes the current owning maintenance/control document or creates an explicit successor only when repository truth requires it; it does not silently rewrite historical execution.

A current owning maintenance source may be corrected when it is internally contradictory, provided the prior value remains recoverable in Git history and the correction is explicitly identified. Do not create parallel reconciliation documents when the owning current maintenance source can be corrected safely and provenance remains preserved.

Jules-generated records are historical inputs, not self-authenticating conclusions. Public code and local targeted checks establish only their tested surfaces; Independent GPT calibrates maintenance interpretation; a human merges. This contract does not authorize direct writes to `main`, history rewriting, force pushes, auto-merge, or silent promotion of research output into executable capability.

## Independent repair decision

Use repository truth first. For maintenance outcomes:

- no confirmed maintenance defect or drift → `NO_CHANGE_REQUIRED` and no activity-only commit or PR;
- confirmed maintenance defect with safe local ownership → repair the minimum synchronized maintenance/control surfaces;
- overlapping ownership or unresolved concurrent state → `COORDINATE`;
- missing authority, unrecoverable state, or unsafe delivery boundary → `BLOCKED`.

`HEALTHY` or `NO_CHANGE_REQUIRED` is a statement about the reviewed maintenance surface, not a universal correctness certificate.

## Verification and delivery

Verification claims are limited to what was actually executed. Distinguish contract review from checker execution. If a repository checker, test, workflow, or local command was not run, record it as `NOT_EXECUTED`; never convert document inspection into a PASS.

For a justified repair:

1. start from the exact fresh `main` revision;
2. change only the owning maintenance/control files and direct synchronized projections;
3. preserve unknown, failure, missing, rejected, provisional, and blocked states;
4. run available targeted validation that is actually supported by the environment;
5. re-read fresh `main` before delivery and recheck aggregate diff/overlap;
6. open one Draft PR and stop for maintainer review.

Done requires aligned maintenance links/indexes, preserved negative evidence, a clean aggregate diff against current `main`, explicit executed/unexecuted validation, and no hidden scope expansion.

Final doctrine and merge authority remains with the maintainer.
