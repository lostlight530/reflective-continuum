# Phase boundary detection

- Method version: 2026-08-05

## Objective

Produce reviewable evidence for phase boundary detection without treating project metaphors as cognitive or safety facts.

## Inputs

version-scoped nodes/edges, PageRank configuration, entropy threshold with owner and calibration. Inputs are untrusted until type, range, provenance, version, and authority checks pass.

## Procedure

validate graph; collapse duplicate edges; iterate PageRank; normalize; compute Shannon entropy in nats; compare to predeclared threshold; retain convergence tolerance and iterations. Record each material choice and stop on invalid state.

## Outputs

rank distribution, entropy, threshold, boundary boolean, scope/limitations. Distinguish observation, source support, proposal, and uncertainty.

## Failure conditions

Fail closed when unknown node, duplicate node id, invalid numeric config, uncalibrated/post-hoc threshold, or cognitive/safety conclusion. Partial output cannot trigger consequential automation.

## Measures

Track rank sum, iteration delta, threshold crossing rate, calibration drift. Metrics diagnose this method; no metric alone proves truth, safety, alignment, or convergence.

## Reproduction and review

Record commit SHA, Python/SQLite versions, sanitized fixture or digest, command, UTC time, exit code, artifact, and untested boundary. Review after schema/contract change, material failure, or evidence expiry.
