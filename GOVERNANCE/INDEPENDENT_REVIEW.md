# Independent Review Contract

Status: public post-hoc review contract  
Calibration: 2026-09-17

## Purpose

This document defines the reviewer-side state machine for independently evaluating committed Reflective Continuum artifacts and repository claims.

It is distinct from repository runtime, Jules R1/R2/R3/R4/R5 production, GitHub Actions, deployment, and scheduled execution. It is also distinct from the Independent GPT maintenance delivery kernel in `GOVERNANCE/independent-gpt/README.md`:

- this file defines **review interpretation states**;
- the Independent GPT kernel defines **maintenance recovery, repair, concurrency, and Draft-PR delivery discipline**;
- neither becomes runtime authority or proves what Jules privately consumed.

This document is not a Jules task prompt, repository-memory entry, public `AGENTS.md`, executable policy, workflow, or CI gate.

The review layer may inspect committed research, specifications, ADRs, references, explicit run evidence, maintenance records, Git/PR chronology, and public sources. It may calibrate current interpretation without changing the historical fact that an artifact was produced.

## Recovery prerequisite

Before assigning a current review state, recover repository truth from current merged `main` and identify the exact artifact/revision under review. When delivery or maintenance state matters, also inspect relevant open pull requests, active branches, and revision-matched runner evidence.

A stale clone, prior handoff SHA, later path presence, or model recollection cannot establish current or historical state by itself.

## Public review states

These states describe review status only. They are not graph/runtime states and they do not expose private reasoning.

1. `REVIEW_PENDING`
   - artifact or claim has entered independent review
2. `SOURCE_SCOPED`
   - source identity, source class, and supported proposition are bounded
3. `STATE_SCOPED`
   - storage/run/task identity and observed state are separated where material
4. `PERSISTENCE_NOT_VERIFIED`
   - observations cannot be tied to the same persistent storage identity
5. `CONFLICT_OPEN`
   - credible evidence or repository records disagree
6. `INSUFFICIENT_EVIDENCE`
   - evidence cannot support the requested claim strength
7. `CALIBRATION_REQUIRED`
   - historical output remains useful but current interpretation must be narrowed or corrected
8. `CALIBRATED`
   - an explicit current correction records the supported interpretation without erasing historical output
9. `ACCEPTED_FOR_REPOSITORY_KNOWLEDGE`
   - the reviewed proposition fits current repository evidence and authority boundaries

Reviewer confidence alone is never a transition condition.

## Transition discipline

A normal supported path is:

`REVIEW_PENDING → SOURCE_SCOPED → STATE_SCOPED → ACCEPTED_FOR_REPOSITORY_KNOWLEDGE`

When storage continuity is unresolved:

`REVIEW_PENDING → SOURCE_SCOPED → STATE_SCOPED → PERSISTENCE_NOT_VERIFIED`

A correction path is:

`REVIEW_PENDING → SOURCE_SCOPED → STATE_SCOPED → CALIBRATION_REQUIRED → CALIBRATED → ACCEPTED_FOR_REPOSITORY_KNOWLEDGE`

A contested path is:

`REVIEW_PENDING → SOURCE_SCOPED → CONFLICT_OPEN`

An evidence-limited path is:

`REVIEW_PENDING → SOURCE_SCOPED → INSUFFICIENT_EVIDENCE`

Every transition must be justified by public, reviewable material such as a primary source, repository artifact, explicit command/result, named storage/run identity, Git/PR chronology, or explicit calibration record.

## History and correction discipline

Keep these statements independent:

```text
historical artifact != current state
current path presence != earlier execution
later success != earlier success
correction != history rewrite
unknown != inferred success
```

Historical research and archived audits remain point-in-time evidence. A review finding normally changes current interpretation or the owning current maintenance/control source. It does not silently rewrite historical execution.

When a historical artifact itself is the object under review, record the supported disposition and correction pointer rather than manufacturing missing runtime facts.

## Reflective-specific review checks

When applicable, independent review checks that:

- `ACCEPTED` and `REJECTED_FROM_INGESTION` remain control-flow outcomes rather than truth labels;
- source credibility and epistemic support remain separate from ingestion outcome;
- R1 graph-write statements are not assumed to persist into R2 unless the same storage identity is verified;
- a bare SQLite `:memory:` database is not treated as durable cross-task state;
- `Nodes=0 / Edges=0` remains `INDETERMINATE_EMPTY_STATE` when cause is unresolved;
- module-local success is not promoted into system-wide persistence or semantic-health claims;
- synthetic/test transitions are not counted as operational transitions;
- `STABLE` or equivalent labels are limited to the dimensions actually audited;
- earlier errors, rejected signals, `NOT_COMPUTED`, and missing fields survive aggregation;
- ADR, specification, and reference relationships are explicit rather than inferred from numbering or proximity;
- non-normative references remain background/methodology context rather than executable policy.

## Authority boundary

Independent review reads the existing public repository topology but does not become runtime authority.

- current implementation/tests provide revision-specific executable evidence;
- `SPECIFICATION.md`, `ADR/**`, and `METHODOLOGY/**` define subject-specific engineering/method boundaries;
- `EVIDENCE_BASELINE.md` defines repository evidence semantics;
- `RESEARCH/**` preserves generated/current/historical research artifacts;
- `GOVERNANCE/MAINTENANCE.md` owns public maintenance policy;
- `GOVERNANCE/independent-gpt/README.md` owns memoryless maintenance recovery/delivery discipline.

An audit finding may identify a mismatch. It must not fabricate a predecessor, dependency, persistent database, operational event, successful test, workflow run, or producer intent to make the repository appear consistent.

## Relationship to maintenance repair

Independent review can establish that a maintenance/control-plane defect exists. Actual repair then follows the maintenance contract and Independent GPT recovery kernel.

If no confirmed maintenance defect exists, use `NO_CHANGE_REQUIRED`; review completion alone is not a reason to create an edit or PR.

If repair is justified, change the owning current maintenance/control file(s) and direct synchronized projections. If another live PR/branch owns the same surface or logical period, use `COORDINATE`. If authority or safe delivery cannot be established, use `BLOCKED`.

Review state and maintenance delivery state must not be collapsed into one label.

## Global-practice alignment

This reviewer contract borrows selected public principles from international and industry guidance. It does **not** claim certification, formal conformity, or a NIST/ISO/OECD/SLSA/OWASP level.

- NIST AI RMF: risk measurement should document uncertainty and unmeasured dimensions, and independent review can improve testing effectiveness while mitigating internal bias and conflicts of interest.
- ISO/IEC 42001: traceability, transparency, risk management, defined responsibility, and continual improvement are useful governance patterns; no ISO certification or conformity is claimed.
- OECD AI Principles: accountability benefits from lifecycle traceability and records sufficient for inquiry while disclosure remains appropriate to context.
- SLSA: provenance is not assurance until a verifier checks it against expectations; Reflective claims no SLSA level.
- Public evaluation guidance from major AI labs supports identifying the tested system, harness, environment, budget, and validity hazards rather than treating an outcome as context-free.
- OWASP agentic-risk guidance reinforces explicit state boundaries, least privilege, and reviewer/executor separation.

External frameworks calibrate vocabulary and review discipline only. They do not certify this repository or replace repository-native authority.

## Privacy and non-public reasoning boundary

The public repository stores review outcomes and evidence, not private cognition or private operating context.

Do not commit, reconstruct, or summarize in revealing detail:

- private task prompts or full private conversation prompts;
- Jules repository-memory text or other private agent-memory content;
- hidden reasoning traces, chain-of-thought, scratchpads, or internal deliberation;
- personal context, private correspondence, private account metadata, or non-public relationship information;
- credentials, tokens, session secrets, private URLs, or confidential third-party material;
- internal strategy whose disclosure is unnecessary to reproduce the public evidence decision.

A public rationale should state only the evidence boundary needed to understand the disposition.

## Minimal review record

A durable review may record:

- artifact or claim under review;
- exact repository revision;
- current review state;
- public sources and repository evidence used;
- storage/run identity or persistence uncertainty when material;
- supported proposition and scope;
- missing or conflicting evidence;
- correction/erratum pointer when required;
- safe validation commands and observed results when relevant;
- checks not executed;
- final public disposition.

No private prompt, private memory, hidden reasoning, workflow, or CI field is required in this public schema.

## Automation isolation

This review contract is non-operative. It does not trigger, modify, gate, or replace Jules, Independent GPT execution, GitHub Actions, deployment, runtime code, schedules, or repository memory.

Those systems may produce artifacts that are reviewed here later. A review result never becomes evidence that a producer consumed this contract.

Final doctrine and merge authority remains with the maintainer.
