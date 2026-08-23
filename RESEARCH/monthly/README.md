# Monthly Research Records

This directory contains Reflective Continuum monthly synthesis and explicitly labeled provisional stage audits.

Monthly aggregation must preserve the distinction between **current repository coverage** and **historical execution evidence**.

## Record classes

### Formal R5 monthly lifecycle

A formal R5 phase-evolution record belongs to the natural-month lifecycle and may close only on the evidence available to that lifecycle.

It should preserve unresolved persistence, transition-origin, drift, rejected-signal, and delivery states rather than normalizing them into a single success label.

### Provisional stage audit

A file such as [`2026-08-through-23-stage-audit.md`](./2026-08-through-23-stage-audit.md) is a `PROVISIONAL_STAGE_AUDIT`.

It may:

- inventory current R1/R2 paths and R3/R4 Weekly records
- distinguish original artifacts from later reconciliation records
- identify continuity and identity gaps
- narrow over-broad stability or persistence claims
- promote recurring evidence rules into ADR/methodology layers
- record open month-end work

It must not:

- impersonate the formal R5 monthly closure
- reconstruct missing runtime metrics without evidence
- turn a later reconciliation file into an original run
- treat a current successful selfcheck as proof of historical persistence
- collapse synthetic/test transitions into operational transitions
- erase rejected, blocked, unknown, or `NOT_COMPUTED` states

## Continuity rule

ADR-010 and METH-005 govern continuity interpretation.

A continuity claim should identify:

- the object whose continuity is claimed
- both endpoint observations
- time/revision boundaries
- identity evidence linking the endpoints
- transition/event origin class where relevant
- unresolved alternatives

Current path presence alone is not identity evidence.

## August 2026 reference boundary

The current repository contains an R2 path for 2026-08-06, but that file is a later reconciliation record. The original runtime artifact was not retained and the historical runtime result remains unknown.

Therefore the correct combined state is:

- current path coverage: complete for the audited 2026-08-01 through 2026-08-23 window
- historical execution evidence: not uniformly complete

This distinction must survive Weekly and Monthly aggregation.

## Closure rule

A monthly synthesis should report, where relevant:

- R1/R2 logical-date coverage
- R3/R4 weekly coverage
- original-vs-reconciliation artifact identity
- persistence-link status
- transition-origin status
- drift observation surface and scope
- rejected/rollback history
- missing, blocked, unknown, or uncomputed evidence
- carry-forward questions

Prefer scoped language such as `NO_DRIFT_DETECTED_WITHIN_AUDIT_SCOPE` over an unqualified global `STABLE` claim when the observation surface is limited.

## Authority

When records differ, read them in this order:

1. original R1–R5 artifact for point-in-time execution evidence
2. explicit reconciliation/erratum for later interpretation
3. accepted ADR and methodology for durable repository rules
4. monthly synthesis for bounded aggregation

This directory is documentation/evidence only. It does not modify Jules R1–R5 prompts or memory, scheduler, storage/runtime behavior, frontend, `.github/**`, Actions, CI, deployment, or merge gates.