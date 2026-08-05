# Divergence rejection and rollback

- Method version: 2026-08-05

## Objective

Produce reviewable evidence for divergence rejection and rollback without treating project metaphors as cognitive or safety facts.

## Inputs

versioned baseline/candidate, declared drift measures/thresholds, transaction, owner, recovery objective. Inputs are untrusted until type, range, provenance, version, and authority checks pass.

## Procedure

compute structural/lexical/rank measures separately; validate thresholds; determine policy result; rollback and release on rejection; verify integrity/FTS and state digest; retain privacy-safe event. Record each material choice and stop on invalid state.

## Outputs

accepted commit or structured rejection with measures, reason, and recovery evidence. Distinguish observation, source support, proposal, and uncertainty.

## Failure conditions

Fail closed when baseline missing, query/threshold changes after observation, rollback not released, FTS inconsistent, or raw sensitive content logged. Partial output cannot trigger consequential automation.

## Measures

Track rollback latency/success, post-rollback integrity, false rejection review, threshold expiry. Metrics diagnose this method; no metric alone proves truth, safety, alignment, or convergence.

## Reproduction and review

Record commit SHA, Python/SQLite versions, sanitized fixture or digest, command, UTC time, exit code, artifact, and untested boundary. Review after schema/contract change, material failure, or evidence expiry.
