# Architecture Decision Index

Status: active topology map

## Jules automation boundary

This topology map serves human and independent repository maintenance outside the Jules scheduled automation stream. It documents durable decisions and reference relationships; it is not a Jules task prompt, Jules memory entry, or `AGENTS.md` instruction and does not change existing Jules R1/R2/R3/R4/R5 behavior.

Jules-produced research or audits may later be interpreted against this topology, but that post-hoc review does not mean Jules consumed this index while generating them.

The nine ADRs accepted on 2026-08-05 are **parallel decisions**, not a sequential supersession chain. Numerical order is an identifier/order convention only.

No ADR in this index is declared to supersede another unless its own `Status` section names one explicitly. At this revision every ADR records `Supersedes named ADR: NONE`.

## Decision map

| ADR | Decision | Primary specification surface |
|---|---|---|
| [ADR-001](./ADR-001.md) | Standard-library runtime and explicit contracts | Runtime, security/ownership, verification boundary |
| [ADR-002](./ADR-002.md) | Bounded reflection is a real loop | Validation and observation |
| [ADR-003](./ADR-003.md) | Separate structural, lexical, and rank drift | Search and delta contracts |
| [ADR-004](./ADR-004.md) | Transactional versioned graph schema | Runtime/persistence and transaction contract |
| [ADR-005](./ADR-005.md) | Entropy is a graph statistic, not cognition | Analysis contract |
| [ADR-006](./ADR-006.md) | Provenance before synthesis | Task/input provenance and claim boundary |
| [ADR-007](./ADR-007.md) | Prose is not runtime policy | Validation/configuration contract |
| [ADR-008](./ADR-008.md) | Tasks do not own research records | Task contract and ownership boundary |
| [ADR-009](./ADR-009.md) | Evaluation and claim scope | Acceptance/evaluation and evidence scope |

## Relationship semantics

- `Implements/defines`: the ADR narrows a part of `SPECIFICATION.md`.
- `Related`: two decisions interact, but neither supersedes the other.
- `Supersedes`: reserved for an explicitly named predecessor ADR or document. Absence means no supersession edge.

### Related decisions

- ADR-001 ↔ ADR-007: standard-library/runtime boundary and separation of prose from executable policy
- ADR-002 ↔ ADR-005: bounded reflection uses the configured entropy/boundary statistic but does not turn that statistic into cognition
- ADR-003 ↔ ADR-009: drift measurements are evidence with scoped claim semantics
- ADR-004 ↔ ADR-008: storage transactions and task ownership remain separate concerns
- ADR-006 ↔ ADR-009: provenance constrains what evaluation/synthesis may claim

These are topical relationships, not dependency or supersession edges.

## Historical correction semantics

Each ADR formerly contained the phrase `Supersedes absolute or unverifiable language in the prior file` without naming that file. The W33 reference audit correctly identified those as ghost chains.

This index does not invent missing predecessors. Each ADR now states the historical claim class it corrects and explicitly records that no named predecessor ADR is asserted.

## Reference topology

Background and methodological references are indexed separately in [`../REFERENCES/INDEX.md`](../REFERENCES/INDEX.md). Their presence provides context or source support; it does not make them executable policy or normative ADR dependencies.

This topology repair is independent repository governance. It does not modify Jules automation instructions.