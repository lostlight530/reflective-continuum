# Independent GPT Governance — Continuum Airlock

Status: current public recovery kernel  
Calibration: 2026-09-17  
Scope: repository-local maintenance recovery, independent review handoff, reconciliation, and bounded repair

This directory is the public handoff point for a memoryless Independent GPT reviewer. It is deliberately smaller than the repository's native research system and does not replace research, implementation, evidence, reviewer-state semantics, or private Jules task controls.

## Recovery order

Recover current state from current merged `main` first. For the maintenance subject under review, use the most specific current repository contract. Dated maintenance records and historical audits are point-in-time evidence for their own windows.

At start record the current date, default branch, current `main` SHA, relevant open pull requests, active maintenance branches, recent merged changes, and checks actually executed. Do not treat a stale local clone or prior handoff SHA as current state.

## Repository map

1. Current implementation and current repository structure only as needed to understand maintenance ownership.
2. `GOVERNANCE/MAINTENANCE.md` — canonical public maintenance contract.
3. `GOVERNANCE/README.md` — governance/control-plane router.
4. `GOVERNANCE/INDEPENDENT_REVIEW.md` — non-operative reviewer-side interpretation state machine. It can establish review dispositions such as `CALIBRATION_REQUIRED`, but it does not itself authorize writes or delivery.
5. Current repository-native maintenance/reviewer documents that directly own the subject.
6. Current `RESEARCH/` and historical records only as evidence inputs when they are needed to test a maintenance claim; they are not default edit targets for this maintenance task.
7. Git history, PR chronology, revision-matched execution evidence, and Actions evidence when timing, ownership, producer identity, or delivery state is disputed.

## Task identity and idempotency

Treat a maintenance run as a tuple of repository, maintenance surface/task, logical period when applicable, producer, base revision, and run identifier when available.

Before writing:

- confirm fresh `main`;
- inspect overlapping open PRs and active maintenance branches;
- determine the owning maintenance/control file;
- check whether the same logical repair already exists or has already merged.

If the same maintenance defect is already owned by another live PR/branch, use `COORDINATE` rather than creating a parallel repair. If current `main` has advanced materially, refresh assumptions before delivery.

Never write merely to test whether writes are possible.

## Evidence boundaries

Keep repository fact, runner evidence, external evidence, historical evidence, review disposition, and inference separate. A current file's existence does not prove an earlier execution. Later success does not erase earlier failure. A correction does not rewrite history. Unknown remains unknown.

Native Jules records remain native Jules records. Independent GPT may use them as repository-visible evidence but does not expose or reconstruct private Jules prompts, hidden memory, credentials, or unrelated operator context.

A passing test, checker, or workflow is evidence only for the exact revision/environment/surface it actually checked. Contract review is not checker execution. Unrun validation is `NOT_EXECUTED`.

`GOVERNANCE/INDEPENDENT_REVIEW.md` and this recovery kernel have different jobs:

```text
review state != maintenance action
CALIBRATED != repair delivered
ACCEPTED_FOR_REPOSITORY_KNOWLEDGE != merged
```

## Maintenance decision

Use one of these states when useful:

- `HEALTHY` — reviewed maintenance surface has no confirmed defect;
- `REPAIR` — a confirmed maintenance defect has a safe owning-file repair;
- `COORDINATE` — another live change owns the same surface or period;
- `BLOCKED` — authority, current state, or safe delivery cannot be established.

When no confirmed maintenance defect or drift exists, the action is `NO_CHANGE_REQUIRED`: no activity-only edit, branch, or PR.

If repair is justified, change only the owning current maintenance/control file(s) and direct synchronized projections. Research content, historical research records, implementation, and unrelated governance are outside this kernel unless a current repository-native maintenance contract explicitly makes them part of the repair.

## Delivery discipline

For a justified repair:

1. branch from the exact fresh `main` revision;
2. make the bounded control-plane change;
3. run only available targeted validation and preserve its real outcome;
4. refresh `main` and overlap state before delivery;
5. inspect the aggregate `main...branch` diff;
6. open one Draft PR;
7. stop for maintainer review.

Do not push directly to `main`, force-push history, auto-merge, or claim a checker/CI PASS that was not actually observed.

## Handoff minimum

A durable handoff should make it possible to recover:

- base `main` SHA and current delivery head;
- maintenance scope and owning files;
- relevant logical period if any;
- overlapping PR/branch state;
- review disposition when one exists;
- checks actually run and checks not run;
- confirmed defect or `NO_CHANGE_REQUIRED` basis;
- unresolved items and negative evidence;
- whether the Draft PR is clean against current `main`.

No separate audit artifact is required merely to prove that review happened. Prefer correcting the owning maintenance source and using the Draft PR description as the delivery summary.

Final merge and doctrine authority remains with the maintainer.
