# Independent Review Contract

Status: public post-hoc review contract

## Purpose

This document defines a reviewer-side state machine for independently auditing committed Reflective Continuum artifacts after they are produced.

It is deliberately outside the repository runtime, Jules R1/R2/R3/R4/R5 automation, GPT/cloud maintenance sessions, GitHub Actions, CI, deployment, and scheduled execution. It is not a task prompt, repository-memory entry, `AGENTS.md` instruction, executable policy, workflow, or CI gate.

The review layer may inspect committed research, specifications, ADRs, references, explicit run evidence, and public sources. It may calibrate the interpretation of an artifact without changing the historical fact that the artifact was produced.

## Public review states

These states describe review status only. They are not graph/runtime states and they do not expose private reasoning.

1. `REVIEW_PENDING`
   - artifact has entered independent review
2. `SOURCE_SCOPED`
   - source identity, source class, and supported proposition are bounded
3. `STATE_SCOPED`
   - storage identity, connection/task boundary, and observed state are separated where material
4. `PERSISTENCE_NOT_VERIFIED`
   - two observations cannot be tied to the same persistent storage identity
5. `CONFLICT_OPEN`
   - credible evidence or repository records disagree
6. `INSUFFICIENT_EVIDENCE`
   - evidence cannot support the requested claim strength
7. `CALIBRATION_REQUIRED`
   - historical output remains useful but its interpretation must be narrowed or corrected
8. `CALIBRATED`
   - an explicit correction records the supported interpretation without erasing historical output
9. `ACCEPTED_FOR_REPOSITORY_KNOWLEDGE`
   - the reviewed proposition fits the repository evidence and authority boundaries

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

Every transition must be justified by public, reviewable material such as a primary source, repository artifact, explicit command/result, named storage identity, or calibration record.

## Reflective-specific review checks

When applicable, independent review checks that:

- `ACCEPTED` and `REJECTED_FROM_INGESTION` remain control-flow outcomes rather than truth labels
- source credibility and epistemic support remain separate from ingestion outcome
- R1 graph-write statements are not assumed to persist into R2 unless the same storage identity is verified
- a bare SQLite `:memory:` database is not treated as durable cross-task state
- `Nodes=0 / Edges=0` remains `INDETERMINATE_EMPTY_STATE` when cause is unresolved
- module-local success is not promoted into system-wide persistence or semantic-health claims
- synthetic/test transitions are not counted as operational transitions
- `STABLE` or equivalent labels are limited to the dimensions actually audited
- earlier errors, rejected signals, `NOT_COMPUTED`, and missing fields survive Weekly/Monthly aggregation
- ADR, specification, and reference relationships are explicit rather than inferred from numbering or proximity
- non-normative references remain background/methodology context rather than executable policy

## Authority boundary

Independent review reads the existing public repository topology but does not become part of runtime authority.

- `SPECIFICATION.md` defines engineering contracts
- `ADR/**` records durable decisions
- `REFERENCES/**` supplies non-normative background and methodological context
- executable code/tests provide revision-specific runtime evidence
- `EVIDENCE_BASELINE.md` defines reviewer-side evidence semantics
- `RESEARCH/**` preserves generated/historical research artifacts

An audit finding may identify a mismatch. It must not fabricate a predecessor, dependency, persistent database, operational event, or successful test to make the repository appear consistent.

## Global-practice alignment

This reviewer contract borrows selected public principles from international and industry guidance. It does **not** claim certification, formal conformity, or a NIST/ISO/OECD/SLSA/OWASP level.

- NIST AI RMF: risk measurement should document uncertainty and unmeasured dimensions, and independent review can improve testing effectiveness while mitigating internal bias and conflicts of interest. This directly supports scoped state labels and explicit unresolved persistence. Reference: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
- ISO/IEC 42001: traceability, transparency, risk management, defined responsibility, and continual improvement are useful governance patterns. They inform documentation and review only; no ISO certification or conformity is claimed. Reference: https://www.iso.org/standard/42001
- OECD AI Principles: accountability depends on lifecycle traceability and records sufficient for inquiry, while responsible disclosure should remain appropriate to context. This supports auditability without publishing unnecessary private operating context. References: https://oecd.ai/en/dashboards/ai-principles/P9 and https://oecd.ai/en/dashboards/ai-principles/P7
- SLSA v1.2: provenance does not become assurance until a verifier checks it against expectations. Reflective applies that distinction to graph/run provenance and review evidence only; it claims no SLSA level. References: https://slsa.dev/spec/v1.2/provenance and https://slsa.dev/spec/v1.2/verifying-source
- OpenAI third-party evaluation guidance: claims should identify the tested system, harness, budget, and validity hazards rather than treating a score or outcome as context-free. Reflective reuses this principle when interpreting R1/R2/R3/R4 evidence; it adds no automated evaluator. Reference: https://openai.com/index/trustworthy-third-party-evaluations-foundations/
- Anthropic agent-evaluation guidance: agent evaluations should isolate trials, distinguish task/grader/environment effects, and use multiple evidence layers with periodic human calibration. This reinforces the separation of synthetic transitions, operational observations, and storage state. It is not a CI requirement. Reference: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- OWASP Agentic Top 10: memory/context poisoning, cascading failures, tool misuse, privilege abuse, and human-agent trust exploitation support keeping the reviewer outside execution authority and treating persistent state as an explicit security/evidence surface. Reference: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/

The shared pattern is: **separate producer and reviewer, preserve provenance, verify storage/state identity before inferring continuity, keep uncertainty visible, minimize sensitive disclosure, and never turn the review channel into an execution channel.**

## Privacy and non-public reasoning boundary

The public repository stores review outcomes and evidence, not private cognition or private operating context.

Do not commit, reconstruct, or summarize in revealing detail:

- private task prompts or full private conversation prompts
- Jules repository-memory text or other private agent-memory content
- hidden reasoning traces, chain-of-thought, scratchpads, or internal deliberation
- personal context, private correspondence, private account metadata, or non-public relationship information
- credentials, tokens, session secrets, private URLs, or confidential third-party material
- internal strategy whose disclosure is unnecessary to reproduce the public evidence decision

A public rationale should state only the evidence boundary needed to understand the disposition. It should not expose private reasoning traces.

## Minimal review record

A durable review may record:

- artifact or claim under review
- current review state
- public sources and repository evidence used
- storage identity or persistence uncertainty when material
- supported proposition and scope
- missing or conflicting evidence
- correction/erratum pointer when required
- safe validation commands and observed results when relevant
- final public disposition

No timestamp is required. No private prompt, private memory, hidden reasoning, workflow, or CI field exists in this public schema.

## Automation isolation

This contract is intentionally non-operative.

It does not trigger, modify, gate, or replace Jules, GPT/cloud maintenance, GitHub Actions, CI, deployment, runtime code, schedules, or repository memory. No new CI or workflow is implied by this document.

Those systems may produce artifacts that are reviewed here later, but review never becomes evidence that the producer consumed this contract.