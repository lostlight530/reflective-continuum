# Open Research / 开放科研

Status: durable open-research production guide
Scope: repository-level research positioning, research-production method, scholarly-metadata boundaries, and semantic-drift governance

## Authority

This guide does not replace implementation, active methodology, ADRs, reproducibility contracts, evidence baselines, maintenance, release, or historical research.

```text
current repository truth
→ implementation / methodology / ADR / evidence
→ OPEN_RESEARCH.md
→ RESEARCH_TEMPLATE.md
→ prospective research records
→ scholarly metadata / downstream indexes
```

A stricter repository-native contract wins.

## Canonical positioning

**Canonical Type:** Versioned graph-state and bounded-analysis research software

**One-line positioning:** Standard-library Python research software for versioned graph storage, lexical retrieval, bounded graph analysis, transactional ingestion, and explicit evidence continuity

**Primary domains:** graph storage; information retrieval; graph analysis; reproducibility; data provenance

**Non-goals:** cognitive system; semantic embedding model; physics model; mathematical bounded-function theory; truth engine

```text
External Classification != Repository Identity
Inferred Topic != Canonical Research Domain
Keyword Match != Project Purpose
Scholarly Graph Representation != Repository Self-Definition
```

## Research-production method

The shared ten-repository epistemic skeleton requires recoverable question, falsifiability, evidence identity, fixed object/revision/environment identity, executed procedure, raw observation, counterexample, bounded conclusion, research increment, and retest condition. Reflective Continuum keeps its own graph/store/evidence semantics.

Negative, empty-state, indeterminate, rejected-signal, degraded, or refuted outcomes remain valid when that is what execution supports.

## Repository-specific method

Record when relevant
- database/store identity
- graph/version identity
- fixture or input identity
- query and threshold identity
- Git revision and branch/ref snapshot
- Python/SQLite environment
- snapshot digest and executed command

`same logical date != same Git snapshot != same persistent store`

Do not collapse logical date, Git snapshot, store state, fixture identity, graph version, or runtime environment.

## Evidence and execution discipline

```text
same logical date != same Git snapshot
same Git snapshot != same persistent store
empty graph != proven data loss
test source != test execution
bounded semantic audit != persistent-store proof
```

Raw observations stay separate from interpretation. Unknown/unexecuted states remain explicit.

## Open-science file responsibilities

- `README.md` — public orientation and stable entry points.
- `OPEN_RESEARCH.md` — durable research-production method and positioning.
- `RESEARCH_TEMPLATE.md` — prospective bounded research records.
- `AUTHORS`, `LICENSE`, `CITATION.cff`, `codemeta.json` — authorship, reuse, citation/software metadata.
- `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md` — contribution/community/security governance.
- `RELEASE_POLICY.md` — release/archive semantics.
- `.github/ISSUE_TEMPLATE/**` and pull-request template — reviewable intake.

These support openness and reuse; they do not establish scientific validity.

## Scholarly metadata discipline

Preserve Canonical Type, One-line Positioning, Primary Domains, Non-goals, accurate subjects, and 5–7 defining keywords before future metadata publication. Avoid classifier-facing marketing copy and keyword stuffing.

## Shadow classification

Candidate title + abstract/description may be checked against downstream topic/keyword inference.

```text
ALIGNED
PARTIALLY_ALIGNED
MISCLASSIFIED
CLASSIFIER_NOISE
```

Execution state is separately `RUN` or `NOT_RUN`. Repair owning metadata only for genuine upstream ambiguity; otherwise record classifier noise.

## Semantic drift audit

Compare canonical positioning against `CITATION.cff`, CodeMeta, archive/DOI metadata, OpenAIRE, and OpenAlex.

- **CANONICAL_DRIFT**
- **TRANSPORT_DRIFT**
- **DERIVATION_DRIFT**
- **VERSION_SKEW**

`DERIVATION_DRIFT != REPOSITORY_DEFECT`.

## History and correction

```text
CURRENT_STATE != TASK_TIME_STATE
LATER_SUCCESS != EARLIER_SUCCESS
PUBLICATION_IDENTITY != CURRENT_MAIN
RESEARCH_PRODUCTION != MAINTENANCE != PERIODIC_AUDIT
```

Preserve point-in-time history. Correct forward through explicit correction, reconciliation, or new timepoint records.

## Contribution and review

Use `OPEN_RESEARCH.md` for method/positioning changes and `RESEARCH_TEMPLATE.md` for new research records. State store/graph/revision/environment identity, evidence actually executed or inspected, unresolved boundaries, and historical impact. Do not retrofit historical records to match the current template.

## Permanent boundary

```text
research record != capability claim
publication != validation
usage != adoption
citation != reproduction
metadata consistency != scientific correctness
external indexing != repository self-definition
```
