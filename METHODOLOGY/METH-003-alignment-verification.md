# Claim-scoped verification

- Method version: 2026-08-05

## Objective

Produce reviewable evidence for claim-scoped verification without treating project metaphors as cognitive or safety facts.

## Inputs

exact claim, artifact revision, fixture/query, environment, harness/tools, budget, expected result, disconfirming condition. Inputs are untrusted until type, range, provenance, version, and authority checks pass.

## Procedure

separate integrity, repeatability, drift, security, and behavioral claims; choose matching tests; record invalid cases and counterevidence; run; preserve outputs/digests; state untested boundary. Record each material choice and stop on invalid state.

## Outputs

evidence bundle supporting, contesting, or leaving claim unresolved. Distinguish observation, source support, proposal, and uncertainty.

## Failure conditions

Fail closed when score lacks harness/budget, one metric substitutes for another claim, failed/unrun test reported complete, or source not primary/current. Partial output cannot trigger consequential automation.

## Measures

Track validity failures, reproduction rate, fixture coverage, unresolved claims. Metrics diagnose this method; no metric alone proves truth, safety, alignment, or convergence.

## Reproduction and review

Record commit SHA, Python/SQLite versions, sanitized fixture or digest, command, UTC time, exit code, artifact, and untested boundary. Review after schema/contract change, material failure, or evidence expiry.
