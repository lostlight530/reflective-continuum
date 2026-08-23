# Reflective Continuum Methodology Index

Status: active procedure map

## Authority

`METHODOLOGY/**` describes analytical procedures. It is subordinate to `SPECIFICATION.md` and must remain consistent with accepted ADRs. It does not create runtime policy or modify Jules automation.

## Procedures

| Method | Topic | Primary role |
|---|---|---|
| [METH-001](./METH-001-phase-boundary-detection.md) | Phase-boundary detection | Detect and bound phase transitions |
| [METH-002](./METH-002-reflective-morphing-protocol.md) | Reflective morphing | Controlled transformation procedure |
| [METH-003](./METH-003-alignment-verification.md) | Alignment verification | Scoped comparison and verification |
| [METH-004](./METH-004-cognitive-divergence-rollback.md) | Cognitive-divergence rollback | Bounded rollback procedure |
| [METH-005](./METH-005-evidence-continuity-reconciliation.md) | Evidence continuity and reconciliation | Identity, delivery, persistence, and historical-state reconstruction |

## Cross-method rules

- a metric belongs to the data and transition set actually inspected
- ingestion outcome is not a truth label
- a current successful selfcheck does not erase a historical error or missing artifact
- path presence, execution success, persistence continuity, transition origin, and evidence completeness are separate dimensions
- synthetic/test transitions remain separate from operational transitions
- a later reconciliation may supersede interpretation without pretending to be the original run

METH-005 operationalizes ADR-010 for post-hoc evidence review.

## Jules automation boundary

This file is a human/independent-maintenance navigation surface. It is not a Jules task prompt, Jules memory entry, scheduler rule, CI gate, or runtime instruction.
