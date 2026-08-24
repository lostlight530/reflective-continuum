# Claim-scoped verification

- Method version: 2026-08-24

## Objective

Produce reviewable evidence for claim-scoped verification without treating project metaphors, ingestion outcomes, or source prestige as cognitive or safety facts.

## Inputs

Exact claim, artifact revision, fixture/query, environment, harness/tools, budget, expected result, disconfirming condition, source class when external evidence is involved, and the proposition the source is expected to support. Inputs are untrusted until type, range, provenance, version, and authority checks pass.

## Procedure

1. Separate integrity, repeatability, persistence, drift, security, source-support, and behavioral claims.
2. Choose evidence/tests appropriate to the exact claim.
3. For external material, classify source authority independently from ingestion outcome and extract only the proposition actually supported.
4. Record invalid cases, counterevidence, unresolved fields, and scope limitations.
5. Run or inspect the selected evidence surface; preserve outputs/digests when applicable.
6. Compare the observed evidence with both the claim and its disconfirming condition.
7. State the untested boundary and stop on material evidence mismatch.

## Outputs

An evidence bundle supporting, contesting, or leaving the claim unresolved. Keep these dimensions separate when relevant:

- `INGESTION_OUTCOME`
- `SOURCE_CREDIBILITY`
- `SOURCE_CLAIM_SUPPORT`
- `EXECUTION_RESULT`
- `PERSISTENCE_LINK`
- `UNTESTED_BOUNDARY` / unresolved evidence

`ACCEPTED` does not mean a source claim is true. `REJECTED_FROM_INGESTION` does not mean it is false.

## Source authority rule

Primary/current evidence SHOULD be preferred when a material factual or implementation claim depends on it. Secondary or contextual sources are not automatically invalid; they may support clearly labelled secondary/contextual claims when their authority is adequate for that claim.

Fail the claim rather than the source class when the available authority is insufficient for the proposition being asserted.

If the cited source does not actually support the persisted proposition, classify the item as `SOURCE_CLAIM_MISMATCH` until corrected or independently supported.

## Failure conditions

Fail closed when:

- a score lacks the relevant harness/budget
- one metric substitutes for another claim
- a failed or unrun test is reported as complete
- evidence is presented outside its observed revision/environment/fixture scope
- a source class is promoted beyond its authority
- a source is current/reachable but does not support the extracted proposition
- ingestion acceptance is used as epistemic validation
- a persistence claim lacks object identity linking its endpoints

Partial output cannot trigger consequential automation.

## Measures

Track validity failures, reproduction rate, fixture coverage, unresolved claims, source-claim mismatches, and evidence-authority downgrades. Metrics diagnose this method; no metric alone proves truth, safety, alignment, persistence, or convergence.

## Reproduction and review

Record commit SHA, Python/SQLite versions when relevant, sanitized fixture or digest, command/evidence path, UTC time, result/exit code when applicable, source version/check time, artifact, and untested boundary. Review after schema/contract change, material failure, source conflict, or evidence expiry.
