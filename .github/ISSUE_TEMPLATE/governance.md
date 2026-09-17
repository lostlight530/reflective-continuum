---
name: Maintenance or governance correction
about: Report a bounded maintenance/control-plane defect, authority drift, or recovery inconsistency
labels: documentation
assignees: ""
title: "[Governance] "
---

## Owning maintenance/control surface

## Current repository fact

Include current `main` revision and the exact file/rule that is inconsistent, stale, ambiguous, or missing.

## Historical / prior interpretation

State the prior value only when it matters. Do not rewrite point-in-time history to make current state look cleaner.

## Evidence and authority

Separate repository fact, revision-matched execution/runner evidence, primary external evidence, inference, and unknown state.

## Concurrency

List overlapping open PRs / active maintenance branches for the same surface or logical period. Use `COORDINATE` when another live change owns the repair.

## Proposed bounded correction

Identify the owning file(s) and direct synchronized projections. Do not manufacture unrelated cleanup.

## Verification

List checks actually executed and their outcomes. Mark unrun checks `NOT_EXECUTED`.

## Privacy / Jules boundary

Do not paste private Jules prompts, hidden memory, credentials, or unrelated operator context into this issue.

## Rollback and maintainer decision

Final doctrine and merge authority remains with the maintainer.
