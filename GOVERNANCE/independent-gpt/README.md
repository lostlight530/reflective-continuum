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

## Public-release privacy preflight — 2026-10-26

This is a publication-safety procedure for Independent GPT maintenance handoffs, not a new research producer, runtime gate, or permission to disclose private control text.

1. **Allowlist:** publish only repository-visible task/cadence identity, Git refs, non-sensitive file scope, scoped findings, bounded validation results, risks, rollback, conflicts, and explicit unknowns. A public rule may state the boundary without reproducing the private instruction behind it.
2. **Inspect outgoing surfaces before publication:** check the complete `main...branch` diff and proposed PR title/body/comments, linked issues, generated reports/attachments and quoted Action logs for sensitive content. Review incoming third-party snippets before propagating them. Searching for terms such as `private memory` is only a lead, not proof of disclosure; a passing pattern scan is not a clean-history certificate.
3. **Withhold private material:** never copy credentials, tokens, session values, private prompts, private agent memory, hidden reasoning, personal or private operator details, nonpublic URLs, or off-repository confidential SOP/source text. Do not include suspect values, reversible redactions, or secret-derived fingerprints in public diagnosis, tests, screenshots or receipts.
4. **Fail closed:** if identity or publication authorization is uncertain, stop the affected write/PR/log publication; report `PUBLICATION_BLOCKED_PRIVATE_MATERIAL` using category and affected public-surface type only, with no value or private-text excerpt. Coordinate privately with the authorized maintainer; a missing or unexecuted check remains `NOT_EXECUTED`.
5. **If exposure is confirmed:** do not assume a later edit or PR close removes Git history, caches, forks or logs. Escalate privately, contain distribution, revoke/rotate affected credentials where applicable, and arrange platform-appropriate remediation with the maintainer. Preserve only non-sensitive incident/correction evidence, not the exposed payload.

This preflight does not establish that all repository history was scanned, any secret was found, or a private scheduler was shut down. Historical producer provenance and sealed research/maintenance artifacts retain their original identity.

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

## 2026-11-11 scoped independent A1/A2 acceptance clarification

This public recovery note records an evidence-based interpretation correction for the Nov01–11, 2026 window. See [dated original-PR reconciliation](../../historical-audits/2026-11/2026-11-11-a1a2-effective-pr-acceptance-reconciliation.md). It does not amend native production authority, retroactively modify PRs, or replace the independent periodic audit.

- Independent A1 = complete applicable MonthStart..N−1 source/artifact coverage, evidence inspection and per-file disposition, not merely a yesterday note.
- Independent A2 = complete MonthStart..N relationship/current-state version, starting only after its original A1 is merged and freshly reread from main.
- Real, non-duplicated custody rows, source identity, exact SHA/path references, per-file decisions, NO_FOLLOW_UP with examined basis, provenance deltas, relationship revisions, negative evidence and correction records are valid maintenance content.
- An effective 100-line PR does **not** require 100 distinct novel scientific claims, 100 independent external issuers or invented daily changes.
- GitHub original PR additions >=100 remains a separate hard numeric check; count at its own final merged head, never across successors, cleanup, other PRs or repositories.
- Do not count boilerplate, filler, repeated text inserted only to inflate additions, fake checks or unsupported scientific assertions as effective content.
- Review task coverage, semantic quality, Git merge, native production state, actual execution checks and current main retention as distinct evidence dimensions.
- Early Draft NOT_MET may describe an earlier head; after same-original-PR supplementation inspect final diff and record final-head assessment without erasing the Draft event.
- A numerically short original can still be a real merged maintenance delivery; preserve NUMERIC_NOT_MET while stating the actual completed scope accurately.
- Actual BLOCKED/PARTIAL/UNKNOWN native gaps remain unresolved unless direct native/runner evidence shows otherwise; maintenance never invents host execution.
- D7/D10/D14/D30 are separate periodic audits; source-level A1/A2 cannot falsely claim these checks or Human Review.
- November is OPEN at the 2026-11-11 evidence cut; W45 closed, W46 open; do not make period-final claims before due.
- This repository's original Nov02–11 ledger contains 20 merged original PRs, 11 with >=100 additions and 9 numeric NOT_MET; substantive acceptance is not inferred solely from these numbers.
