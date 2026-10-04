# Open Research / 开放科研

Status: durable open-research production guide
Scope: repository-level research positioning, research-production method, scholarly-metadata boundaries, and semantic-drift governance

## Language policy / 语言政策

English is the canonical and default language for this open-research contract. Chinese text is provided as an accessibility and interpretation aid. If wording diverges, the English normative text governs; repository evidence and current owning contracts remain authoritative over both.

英文是本开放科研契约的默认与规范语言；中文用于辅助理解与可访问性。若中英文表述有差异，以英文规范文本为准；仓库事实与当前 owning contract 的权威仍高于任何翻译。


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

## Research scope and workflows / 科研范围与工作流

Repository positioning follows its declared purpose, implemented or studied research objects, and applicable public contracts. Existing canonical positioning remains unchanged.

Repository-owned workflows may implement research methods and produce bounded observations. Their substantive research role remains intact; the execution mechanism alone does not establish a research domain or scientific validity.

仓库现有定位保持不变；自有工作流的科研作用保留，执行机制本身不构成研究领域或科学有效性的证明

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


## 中文摘要

本文件定义仓库的长期开放科研方法：共同骨架要求研究问题、可证伪假设、证据/来源身份、固定对象/版本/环境、实际执行程序、原始观测、反例检查、有界结论、研究增量与复验条件。

仓库自身的 implementation、Specification/Methodology/ADR、evidence、history 等原生 authority 仍然拥有最终语义。外部 scholarly graph 或分类器只属于派生表示，不能反向定义仓库身份。

未来 scholarly metadata 重点保持 canonical type、one-line positioning、primary domains、non-goals、少量准确 subjects 与 5–7 个定义性 keywords；若外部分类漂移，先修 owning metadata 的真实歧义，否则记录 classifier noise。
