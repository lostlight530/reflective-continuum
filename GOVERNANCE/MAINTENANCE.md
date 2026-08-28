# Reflective Continuum maintenance contract

Status: `CANONICAL_PUBLIC_MAINTENANCE_CONTRACT`  
Effective: 2026-08-28

## Cadence and independent evidence

R1 and R2 are independent Daily surfaces. R3/R4 Weekly inherit Daily observations; R5 Monthly closes only after the natural month ends. Source authority, claim support, ingestion outcome, store identity, and test result are five separate evidence classes. None substitutes for another.

Retain source/version/retrieval time; accepted/rejected signal and rollback reason; database path/URI/connection identity; nodes/edges; passed/failed/errors/skipped; failure identity; and whether drift was computed. `INDETERMINATE_EMPTY_STATE`, failed/error tests, rollback, and rejected signals survive aggregation. Shared persistence requires a named common store plus evidence that both tasks opened it.

Semantic drift is limited to implemented structural deltas, FTS5 top-result identity, and PageRank score deltas. Entropy is PageRank-derived Shannon entropy. Convergence is fixed-fixture repeatability. Reflection/rollback is local to a SQLite savepoint. These surfaces do not establish cognition, safety, semantic truth, global stability, alignment, or durable cross-task memory.

## Historical and document governance

Post-hoc calibration preserves the original body and adds disposition, reason, evidence boundary, authority, and replay status. Weekly may aggregate, preserve, or downgrade but cannot erase Daily failures. Monthly cannot create future dates. ADR/Methodology identifiers remain stable; update text when its implementation mapping, input/output, procedure, failure condition, or evidence boundary changes.

Jules-generated records are historical inputs, not self-authenticating conclusions. Public code and local targeted checks establish only their tested surfaces; independent review calibrates claims; a human merges. This contract does not authorize changes to `CODE/**`, dependencies, frontend, `.github/**`, CI, or private control planes.

## Done, rollback, escalation

Done requires aligned indexes/links, retained negative evidence, passing targeted local checks with environment and exit code, a clean protected-path review, and explicit unrun tests. Revert the maintenance commit if an authority link or public contract breaks. Escalate missing store identity, source mismatch, disappearing failures, or scope promotion to human review.
