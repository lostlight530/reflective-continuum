# Reflective Continuum maintenance contract

Status: `CANONICAL_PUBLIC_MAINTENANCE_CONTRACT`

Effective: 2026-09-17

## Scope

This contract governs repository maintenance, native producer-generated maintenance inputs, including current GPT Native prospective production and retained historical Jules outputs, Independent GPT recovery/review, cadence interpretation, checker ownership, and delivery discipline. It does not authorize a maintenance agent to redesign research content, rewrite historical research artifacts, change `CODE/**`, change dependencies, alter `.github/**` runner/deployment surfaces, or promote private control-plane instructions into the public repository unless a separate repository-native authority explicitly requires that change.

## Cadence and independent evidence

R1 and R2 are independent Daily surfaces. R3/R4 Weekly inherit Daily observations; R5 Monthly closes only after the natural month ends. Source authority, claim support, ingestion outcome, store identity, run identity, transition origin, and test result are separate evidence classes. None substitutes for another.

A 30-day provisional audit may summarize 30 retained logical dates, but it is not a natural-month closure. Keep `MONTH_OPEN` until the final calendar date is retained or explicitly classified as missing after it becomes due.

Retain source/version/retrieval time; accepted/rejected signal and rollback reason; database path/URI/connection identity; run/log identity when claimed; nodes/edges; passed/failed/errors/skipped; failure identity; transition origin; and whether drift was computed. `INDETERMINATE_EMPTY_STATE`, failed/error tests, rollback, rejected signals, `NOT_COMPUTED`, and unresolved identity survive aggregation.

Shared persistence requires a named common store plus evidence that both tasks opened it. Same logical date, matching digest, or one task's local acceptance is insufficient. A repeated placeholder such as `Run ID: auto` is not independent-run evidence.

Semantic drift is limited to implemented structural deltas, FTS5 top-result identity, and PageRank score deltas. Entropy is PageRank-derived Shannon entropy. Convergence is fixed-fixture repeatability. Reflection/rollback is local to a SQLite savepoint. These surfaces do not establish cognition, safety, semantic truth, global stability, alignment, or durable cross-task memory.

A passing test suite is revision/environment-scoped evidence for the tests that ran. It does not establish shared persistence, source truth, non-empty graph state, operational transition provenance, or architecture-wide health.

## 2026-10-26 forward producer-attribution reconciliation

Status: `CURRENT_CONTROL_PLANE_RECONCILIATION / HISTORICAL_A2_PRESERVED`. This later correction of interpretation is not an edit to the original native run or merged A2 snapshot.

- The merged 2026-10-25 month-relation A2 record (`historical-audits/2026-10/2026-10-25-a2-month-relation.md`, blob `2921495d0d2a8aecd4edfee03824d67951e297ac`) globally says `Source Native producer Jules`.
- Its own October 25 source references are `RESEARCH/daily/2026-10-25-dehydrated-report.md` (blob `28ffa22866eec3606c6268bebea0383b1e0b5cb5`) and `RESEARCH/daily/2026-10-25-cortex-selfcheck.md` (blob `a6cee7e4900d745e6464845343de94ecdc011d6c`). Both explicitly state `Producer: GPT-6 prospective native / NOT Jules`.
- Correct current interpretation: one global Jules label cannot represent all October native records. Attribute R1 and R2 separately, per original producer identity and exact source revision; preserve genuinely Jules-produced historical records and any Independent GPT maintenance identity.
- Both October 25 native R1 ingestion and R2 selfcheck remain `NOT_EXECUTED`; actual accepted/rejected counts and same-store proof were not computed. No current graph-health or drift success is inferred from this reconciliation.
- Preserve the merged A2 as point-in-time evidence rather than silently rewriting it. Carry the corrected attribution into future monthly relation/correction work without increasing independent-run counts.

## Maintenance identity and concurrency

A maintenance run is identified by repository, task/surface, logical period when applicable, producer, base `main` revision, observed branch/ref when availability is branch-relative, and run identifier when one exists. Before any write, recover the current default branch, latest merged `main`, relevant open pull requests, active maintenance branches, and recent merged changes.

If another open PR or active branch owns the same maintenance surface or logical period, coordinate instead of manufacturing a parallel repair. Sibling branches sharing one base revision remain separate evidence snapshots after divergence. A later `main` revision invalidates earlier delivery assumptions until the aggregate diff is rechecked.

Use writes only for confirmed maintenance changes. Never create or mutate a branch merely to test write permission.

## Historical and document governance

Historical research and archived audit artifacts are point-in-time evidence, not routine edit targets. A maintenance correction changes the current owning maintenance/control document or creates an explicit successor only when repository truth requires it; it does not silently rewrite historical execution.

A current owning maintenance source may be corrected when it is internally contradictory, provided the prior value remains recoverable in Git history and the correction is explicitly identified. Do not create parallel reconciliation documents when the owning current maintenance source can be corrected safely and provenance remains preserved.

Native producer-generated records are repository inputs, not self-authenticating conclusions. Retained Jules records preserve their original provenance and are not relabeled by later GPT Native or Independent GPT maintenance. Public code and local targeted checks establish only their tested surfaces; Independent GPT calibrates maintenance interpretation; a human merges. This contract does not authorize direct writes to `main`, history rewriting, force pushes, auto-merge, or silent promotion of research output into executable capability.

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


## Branch/ref evidence boundary — 2026-10-04 special calibration

When a Weekly or downstream task evaluates same-period Daily inputs, capture branch/ref visibility separately from eventual repository state.

Required distinction when material:

```text
BASE_REVISION
BRANCH_OR_REF
VISIBLE_PATHS_AT_SNAPSHOT
SIBLING_BRANCH_PATHS
EVENTUAL_MAIN_PATHS
STORE_IDENTITY
RUN_IDENTITY
```

None of these fields substitutes for another.

A later merge can justify a successor/reconciliation. It cannot turn an earlier branch-relative absence into an earlier observed input.

This maintenance rule does not authorize rewriting R1/R2/R3/R4 history or promoting a path-presence check into runtime/store validation.
