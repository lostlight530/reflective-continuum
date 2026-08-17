# AI Use Disclosure

AI assistance may draft text/code, suggest tests, translate, discover sources, summarize runs, or review. The human contributor owns every claim, source, license, permission, security decision, and verification result.

A material AI-assisted pull request records affected artifacts, assistance category, model/service and date when known, data supplied, primary-source checks, commands/results, and uncertainty. Do not send secrets, private graph content, embargoed vulnerabilities, or third-party confidential material to a model.

Generated output is untrusted. Review the diff; verify primary sources; reproduce calculations and migrations; test invalid input, rollback, and resource bounds when executable behavior changes; and label proposals/hypotheses. Model agreement is not independent evidence. Releases, permissions, destructive operations, and external commitments need accountable human review.

## State interpretation boundary

AI-generated summaries must not collapse independent runtime facts into one global state.

- module import/init success is not persistence proof
- an R1 ingestion acceptance is not evidence that R2 will observe the same graph
- a bare SQLite `:memory:` database must not be assumed to persist across independent connections/tasks
- `Nodes=0 / Edges=0` must not be labelled globally healthy or failed without causal evidence
- synthetic transitions must not be described as operational transitions
- `NOT_COMPUTED`, `MISSING_DATA`, rejected signals, and unresolved topology findings survive summarization

If the storage identity linking two observations is unknown, use `PERSISTENCE_LINK_NOT_VERIFIED` rather than inventing continuity.

## Source and ingestion boundary

AI assistance must preserve the distinction between:

- what a source says
- how authoritative that source is
- whether the repository accepted the signal
- whether the graph write executed
- whether the written state was later observed

`REJECTED_FROM_INGESTION` is not a claim that the source is false. `ACCEPTED` is not a claim that the source is true.

Vendor posts, manifestos, draft standards, and position papers must retain those source classes. A confident synthesis does not upgrade them into universal guarantees.

## Derived reports and correction

Weekly or monthly AI-generated summaries inherit Daily uncertainty. A later successful snapshot does not erase an earlier error, and a higher-level report may not strengthen evidence without a new explicit source or observation.

Retain privacy-safe run identifiers when policy permits, not full prompts by default. Correct false or over-strong generated material through an ordinary reviewed change with an explanation of the prior evidence failure.

When the original generated artifact is part of the historical R1–R4 record, prefer a visible calibration/erratum over a silent rewrite and state which prior interpretation it supersedes.