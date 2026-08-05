# Bounded reflective transformation

- Method version: 2026-08-05

## Objective

Produce reviewable evidence for bounded reflective transformation without treating project metaphors as cognitive or safety facts.

## Inputs

validated input, transaction, RuleConfig, reflector hook, max depth, version. Inputs are untrusted until type, range, provenance, version, and authority checks pass.

## Procedure

open validated savepoint; insert versioned state; validate snapshot; calculate boundary; for each depth invoke hook and recompute; commit on acceptance; rollback/release on rejection or exception. Record each material choice and stop on invalid state.

## Outputs

ProcessResult plus durable state only when accepted. Distinguish observation, source support, proposal, and uncertainty.

## Failure conditions

Fail closed when hook hides failure, depth does not advance/recompute, DB error swallowed, savepoint remains open, or exhausted state commits. Partial output cannot trigger consequential automation.

## Measures

Track accept/reject counts, actual depth, rollback success, hook error types. Metrics diagnose this method; no metric alone proves truth, safety, alignment, or convergence.

## Reproduction and review

Record commit SHA, Python/SQLite versions, sanitized fixture or digest, command, UTC time, exit code, artifact, and untested boundary. Review after schema/contract change, material failure, or evidence expiry.
