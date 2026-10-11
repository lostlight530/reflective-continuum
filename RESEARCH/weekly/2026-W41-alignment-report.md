# 2026-W41 Alignment Report

## Drift 状态
STABLE

Scope: `STABLE` is limited to the executed semantic audit against `cortex.db`, FTS5 lexical ranking, and the caller-selected queries recorded in `semantic_drift_audit.log`. It does **not** establish repository-wide semantic stability, absence of untested drift, or correctness outside those queries.

## Drifted Nodes
None

Scope: no changed top result was observed for the four recorded audit queries. This is not a claim that every node or every possible query was checked.

## Synthetic Transitions
NOT_COMPUTED
Reason: Event origin cannot be separated

## Operational Transitions
NOT_COMPUTED
Reason: Event origin cannot be separated

## Replay Transitions
NOT_COMPUTED
Reason: Event origin cannot be separated

## Unknown-Origin Transitions
NOT_COMPUTED
Reason: Event origin cannot be separated

## Hard Rollback
68 occurrences observed in the inspected `ingestion.log`.

Scope: this is a log occurrence count. It is not a count of unique causal incidents unless separately deduplicated.

## Daily Convergence
Observed statuses: SUCCESS, SUCCESS_WITH_REJECTED_SIGNAL, FIXED_FIXTURE_REPEATABILITY_OBSERVED

Scope: status presence is retained as producer evidence; it is not promoted to repository-wide convergence or external-system correctness.

## 缺失日期
None observed within the W41 report window: 2026-10-05 through 2026-10-11.

This statement is intentionally limited to the W41 window and does not assert complete daily coverage from 2026-05-20 through 2026-10-11.

## 数据来源边界
- `RESEARCH/daily/`
- `ingestion.log`
- `semantic_drift_audit.log`
- `cortex.db` as the executed semantic-audit database
- Same-repository artifacts are execution evidence, not independent external corroboration

## 测试结果
- Total: 27
- Passed: 27
- Failed: 0
- Errors: 0
- Skipped: NOT_REPORTED

Scope: the reported unit-test result establishes the executed test-suite outcome for this producer run. It does not establish exhaustive runtime, integration, or deployment validation.

## Governance disposition
- Report week: 2026-W41
- Historical W40 report: NOT_REWRITTEN
- Semantic conclusion: BOUNDED_TO_EXECUTED_AUDIT
- Transition origin separation: NOT_COMPUTED
- Runtime/global stability promotion: NONE
- Independent-source credit: NONE
- Forward correction applied before merge: YES
