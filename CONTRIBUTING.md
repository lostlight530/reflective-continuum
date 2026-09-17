# Contributing

Reflective Continuum accepts bounded changes that strengthen repository correctness, maintenance discipline, reproducibility, and inspectable evidence without silently expanding capability claims.

## Authority and maintenance boundary

Before changing anything, recover current repository truth from the latest merged `main`. Identify the owning implementation or contract, relevant open pull requests, active maintenance branches, and the exact base revision used for the work.

Repository maintenance is governed by `GOVERNANCE/MAINTENANCE.md`. Memoryless Independent GPT recovery is governed by `GOVERNANCE/independent-gpt/README.md`. Private Jules task prompts and repository memory are producer-side controls and are not reconstructed or copied into public files unless the maintainer explicitly publishes them.

This repository currently has no public `AGENTS.md`. Do not infer one from private automation, prior chats, or model memory.

A maintenance/review task may read research, implementation, evidence, ADR, methodology, and historical records when needed to establish repository truth. Those surfaces are not automatically edit targets. Change them only when the current owning contract explicitly makes them part of the repair.

## Change ownership

For any proposed change:

1. identify the owning file or implementation surface;
2. distinguish current state from historical point-in-time evidence;
3. preserve failure, unknown, missing, rejected, provisional, and blocked states;
4. avoid parallel fixes when another live PR or branch owns the same surface or logical period;
5. keep the aggregate diff bounded to the justified repair.

Do not create activity-only commits. When no confirmed maintenance defect exists, the correct maintenance outcome is `NO_CHANGE_REQUIRED`.

## Jules and Independent GPT

Jules-produced artifacts are repository inputs, not self-authenticating conclusions. Independent GPT review may calibrate maintenance interpretation, detect drift, and prepare bounded repairs, but it does not prove what Jules privately consumed or intended.

Keep these planes distinct:

```text
Jules producer execution != Independent GPT review
Independent GPT review != GitHub Actions
workflow definition != workflow execution
current path presence != earlier execution
later success != earlier success
correction != history rewrite
```

No public contribution should disclose private prompts, credentials, hidden memory, or unrelated operator context.

## Executable changes

Before changing executable behavior, identify the governing ADR/method, define inputs/outputs/errors/migration, add a regression test, and preserve separately owned paths unless the change explicitly owns them. Database schema changes require a migration and compatibility note; never silently reinterpret existing rows.

Use the repository-supported Python environment for executable-path verification. Current targeted commands include:

```text
python -m unittest discover -s tests -v
python -m CODE.tasks.cortex_selfcheck
python -m CODE.tasks.convergence_drill --iterations 100
```

Run only checks supported by the actual environment. Record exact commands and outcomes. A documentation-only or governance-only change may intentionally leave runtime checks unrun; report those checks as `NOT_EXECUTED`, never as passed.

Runtime code is standard-library only. A proposed dependency needs owner, threat/license review, alternative analysis, lock/update policy, and rollback.

## Evidence and state claims

A state claim must name the storage identity and observation boundary that support it.

- Do not infer that two tasks use the same database merely because both use `GraphDB`.
- A bare SQLite `:memory:` database is connection-local; cross-task persistence must be independently established.
- `Nodes=0 / Edges=0` is not a global health verdict when cause and persistence path are unresolved.
- Import/init success, rule-engine success, integrity checks, persistence success, and semantic correctness are separate claims.
- Use `INDETERMINATE_EMPTY_STATE` when an empty database has multiple plausible causes that have not been discriminated.
- Use `PERSISTENCE_LINK_NOT_VERIFIED` when an R1 graph-write statement cannot be tied to the exact storage inspected by R2.

`ACCEPTED` and `REJECTED_FROM_INGESTION` describe repository control flow, not truth value. Source class/authority, exact proposition support, ingestion result, graph-write result, and later persistence observation remain separate evidence dimensions.

Synthetic/test transitions and operational transitions remain separate. If event origin cannot be established, retain `NOT_COMPUTED` rather than inventing an operational count. `STABLE` must be scoped to the exact audited surface.

## Historical and periodic records

Historical research and archived audit records are point-in-time evidence. Do not silently rewrite them to make them agree with later knowledge. Corrections belong in the current owning maintenance/control source or an explicit successor when the owning source cannot safely carry the correction.

Weekly/Monthly aggregation must not erase Daily failures, rejected signals, missing fields, or unresolved identity. A later successful run does not retroactively prove an earlier unobserved run.

## AI-assisted work

AI-assisted work follows `AI_USE_DISCLOSURE.md`. Generated output is untrusted until reviewed against repository truth and, when material, primary sources. Model agreement is not independent evidence.

## Pull requests

A repair PR must state:

- exact base `main` revision and current head;
- owning maintenance/implementation scope;
- overlapping PR/branch check;
- changed files and deliberately unchanged boundaries;
- commands/checkers/workflows actually executed and their outcomes;
- checks not executed;
- security/privacy/retention impact when applicable;
- rollback boundary;
- unresolved evidence or coordination state.

Before delivery, refresh current `main`, recheck overlap, inspect the aggregate `main...branch` diff, open one Draft PR, and stop for maintainer review unless a different repository-native workflow explicitly applies.

Do not push directly to `main`, force-push history, auto-merge, or claim universal health from a local check.
