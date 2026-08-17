# Contributing

Reflective Continuum accepts small changes that strengthen versioned storage, bounded analysis, provenance, and reproducibility.

Before coding, identify the governing ADR/method, define inputs/outputs/errors/migration, add a regression test for executable behavior, and preserve separately owned README, homepage, `.nojekyll`, RESEARCH, and license paths unless the change explicitly owns them. Database schema changes require a migration and compatibility note; never silently reinterpret existing rows.

Use Python 3.12 or 3.14 for executable-path verification:

```text
python -m unittest discover -s tests -v
python -m CODE.tasks.cortex_selfcheck
python -m CODE.tasks.convergence_drill --iterations 100
```

A documentation-only or evidence-only change may intentionally leave runtime checks unrun. In that case, report them as unrun rather than passed.

Runtime code is standard-library only. A proposed dependency needs owner, threat/license review, alternative analysis, lock/update policy, and rollback. AI-assisted work follows `AI_USE_DISCLOSURE.md`; generated output is untrusted until reviewed.

## State and persistence claims

A state claim must name the storage identity and observation boundary that support it.

- Do not infer that two tasks use the same database merely because both use `GraphDB`.
- A bare SQLite `:memory:` database is connection-local; cross-task persistence must be independently established.
- `Nodes=0 / Edges=0` is not a global health verdict when cause and persistence path are unresolved.
- Import/init success, rule-engine success, integrity checks, persistence success, and semantic correctness are separate claims.
- Use `INDETERMINATE_EMPTY_STATE` when an empty database has multiple plausible causes that have not been discriminated.
- Use `PERSISTENCE_LINK_NOT_VERIFIED` when an R1 graph-write statement cannot be tied to the exact storage inspected by R2.

## Ingestion and evidence claims

`ACCEPTED` and `REJECTED_FROM_INGESTION` describe repository control flow, not truth value.

For every material external signal, distinguish:

1. source class and authority
2. exact proposition supported by the source
3. ingestion result
4. graph-write result
5. later persistence observation, if any

A vendor framework or manifesto may support “the organization proposes X”; it does not automatically establish that X is a general law or a guarantee. A position paper remains a proposal/position unless stronger evidence is independently established.

## Drift and transition claims

Do not merge synthetic and operational transition evidence.

- test-generated/synthetic transitions stay synthetic
- runtime transitions require operational provenance
- if event origin cannot be separated, operational count stays `NOT_COMPUTED`
- `STABLE` must be scoped to the audited data; prefer `NO_DRIFT_DETECTED_WITHIN_AUDIT_SCOPE` when important dimensions remain uncomputed

## Daily → Weekly inheritance

Weekly artifacts preserve the Daily evidence history.

- a later successful test run does not erase an earlier Daily error
- rejected signals remain rejected in aggregate summaries
- missing or uncomputed fields remain visible
- Weekly reports may aggregate or downgrade Daily evidence but may not strengthen it without a new explicit evidence record

Repeated sources should be labelled as revalidation, control signals, new claims from an existing source, or duplicates when novelty matters.

## Corrections

Do not silently rewrite historical R1–R4 records solely to make them consistent with later knowledge. If the original artifact is part of the execution history, add a calibration or erratum that identifies the affected claim, corrected interpretation, precedence, and remaining uncertainty.

Do not modify `SPECIFICATION.md`, `ADR/**`, `METHODOLOGY/**`, or `REFERENCES/**` merely to eliminate an audit finding. Architectural repair must be a separate intentional change with its own evidence and review.

## Pull requests

Pull requests must state exact revision, commands/results when commands were run, unrun checks, security/privacy/retention impact, and rollback where applicable. Failed or unavailable required checks prevent completion claims.

Evidence-only pull requests should additionally state:

- evidence window
- source classes checked
- storage/persistence assumptions
- whether historical artifacts were preserved
- what claim strength changed
- unresolved state or topology debt
