# AI Use Disclosure

AI assistance may draft text/code, suggest tests, translate, discover sources, summarize runs, or review repository state. The human contributor owns every claim, source, license, permission, security decision, merge decision, and verification result.

## Scope and control-plane boundary

This file governs accountable AI-assisted repository work, including Independent GPT maintenance review. It does not reveal or replace private Jules task prompts, hidden memory, credentials, or operator context.

Jules-generated artifacts may be reviewed after generation, but post-hoc review is not evidence that Jules consumed this file or followed its rules. Private Jules controls remain private unless the maintainer explicitly publishes them.

The repository currently has no public `AGENTS.md`; AI assistance must not infer one from private automation or prior conversations.

## Repository truth first

Before an AI-assisted maintenance change, recover the current default branch, latest merged `main`, relevant open pull requests, active maintenance branches, recent merged changes, and the current owning contract. A stale local clone, prior handoff SHA, old chat, or model recollection is not current repository truth.

When no confirmed maintenance defect exists, the correct maintenance action is `NO_CHANGE_REQUIRED`. Do not create activity-only edits or branches merely to prove that an AI agent acted.

## Assistance record

For a material AI-assisted pull request, record when known and relevant:

- affected repository surfaces;
- assistance category;
- model/service and date;
- data supplied to the model;
- primary-source checks performed;
- commands/checkers/workflows actually executed and their outcomes;
- checks not executed;
- unresolved uncertainty or coordination state.

Do not send secrets, private graph content, embargoed vulnerabilities, third-party confidential material, credentials, or private prompts to a model unless an explicit authorized workflow requires it.

## Verification discipline

Generated output is untrusted until reviewed. Verify the aggregate diff, source claims, calculations, migrations, and executable behavior that materially support the change.

Keep these distinctions explicit:

```text
contract review != checker execution
workflow file exists != workflow ran
passing test != universal correctness
model agreement != independent evidence
current path presence != earlier execution
later success != earlier success
correction != history rewrite
```

If a check was not run, record `NOT_EXECUTED`. Do not convert document inspection into PASS.

## State interpretation boundary

AI-generated summaries must not collapse independent runtime facts into one global state.

- module import/init success is not persistence proof;
- an R1 ingestion acceptance is not evidence that R2 observed the same graph;
- a bare SQLite `:memory:` database is connection-local unless a shared-store mechanism is evidenced;
- `Nodes=0 / Edges=0` must not be labelled globally healthy or failed without causal evidence;
- synthetic transitions must not be described as operational transitions;
- `NOT_COMPUTED`, `MISSING_DATA`, rejected signals, failed tests, and unresolved identity survive summarization.

If the storage identity linking observations is unknown, use `PERSISTENCE_LINK_NOT_VERIFIED` rather than inventing continuity.

## Source and ingestion boundary

AI assistance must preserve the distinction between:

1. what a source says;
2. how authoritative that source is;
3. whether the repository accepted the signal;
4. whether a graph write executed;
5. whether the written state was later observed.

`REJECTED_FROM_INGESTION` is not a claim that the source is false. `ACCEPTED` is not a claim that the source is true. Vendor posts, manifestos, draft standards, and position papers retain their source class unless stronger evidence independently changes the interpretation.

## Historical and maintenance corrections

Historical research and archived audit records are point-in-time evidence. AI assistance must not silently rewrite them to make later state look cleaner.

Maintenance corrections should update the current owning maintenance/control source or create an explicit successor when necessary. Preserve the prior value in Git history and describe the correction boundary. Do not create parallel reconciliation files when the current owning maintenance source can safely carry the correction.

## Delivery discipline

For a justified AI-assisted maintenance repair:

1. branch from exact fresh `main`;
2. avoid overlapping live ownership or use `COORDINATE`;
3. change the owning file(s) and direct synchronized projections only;
4. run available targeted validation and preserve its real result;
5. refresh `main` and overlap state before delivery;
6. inspect the aggregate diff;
7. open one Draft PR and stop for maintainer review.

Do not push directly to `main`, force-push history, auto-merge, or claim a checker/CI PASS that was not actually observed.

Final merge, doctrine, release, destructive operations, permission changes, and external commitments remain accountable human decisions.
