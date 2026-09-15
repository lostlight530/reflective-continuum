# Independent GPT Governance — Continuum Airlock

Status: current public recovery kernel
Scope: repository-local recovery, independent audit, reconciliation, and bounded repair

This directory is the public handoff point for a memoryless independent reviewer. It is deliberately smaller than the repository’s native research and maintenance contracts and does not replace them.

## Recovery order

Recover current state from current merged `main` first. For the subject under review, use current implementation and the most specific current repository contract. Dated maintenance and historical audit records are point-in-time evidence for their own windows.

At audit start record the current date, default branch, `main` SHA, relevant open pull requests, recent merged changes, and checks actually executed.

## Repository map

1. Current implementation, stores, tests, and active source under `CODE/` and other current implementation surfaces.
2. `GOVERNANCE/MAINTENANCE.md` for the canonical public maintenance contract.
3. Current evidence baseline, methodologies, ADRs, and repository-native reviewer / governance documents for subject-specific authority.
4. Current `RESEARCH/` Daily / Weekly / Monthly artifacts for repository-visible research execution evidence.
5. `historical-audits/INDEX.md` and referenced records for corrections, period audits, maintenance, and reconciliation history.
6. Git history, PR chronology, and revision-matched execution evidence when store identity, timing, producer identity, or historical state is disputed.

## Evidence boundaries

Keep source authority, claim support, ingestion outcome, store identity, and test result separate. R1 and R2 are independent Daily surfaces unless repository evidence explicitly links them.

A shared store requires a named common store plus evidence that the relevant tasks opened it. Passed tests do not establish semantic truth, cognition, safety, global stability, alignment, or durable cross-task memory. Rejected signals, rollback, failed tests, skipped tests, and indeterminate empty states remain evidence and survive aggregation.

Native Jules records remain native Jules records. Independent review calibrates interpretation; it does not rewrite historical execution.

## History discipline

Historical artifacts are immutable point-in-time evidence. Use dated correction or reconciliation records when later evidence changes current interpretation. Preserve failure, rollback, rejected, missing, provisional, blocked, insufficient-evidence, and unknown states. Archive relocation is not semantic replacement.

If historical store identity, runtime environment, or execution cannot be recovered from repository-visible evidence, keep it `UNKNOWN` rather than reconstructing it from later state.

## Independent audit outcome

Separate current facts, historical facts, corrections, external claims, execution evidence, inference, and unknown state. When a concise governance status is useful, use:

- `HEALTHY`
- `REPAIR`
- `COORDINATE`
- `BLOCKED`

`HEALTHY` means no repair is required for the audited surface; it is not a universal correctness certificate.

If repair is justified, change only the owning current file(s) and the contracts, indexes, or projections that must remain synchronized. Respect protected implementation and control-plane boundaries declared by current repository contracts. Do not create activity-only edits or fabricated backfill.

## Public boundary

This recovery kernel is intentionally repository-bounded. It relies on repository-visible evidence and public sources where needed. It does not require reconstruction of unavailable operator context, credentials, hidden memory, or unrelated orchestration.

## Handoff minimum

A durable independent audit should leave the next reviewer able to identify the base `main` SHA, scope and evidence window, authority used, checks run, checks not run, current findings, historical findings, corrections, unresolved items, and whether history and negative evidence were preserved.

Independent governance may recommend or prepare bounded changes. Final merge and doctrine authority remains with the maintainer.
