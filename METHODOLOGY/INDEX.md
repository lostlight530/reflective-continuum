# Reflective Continuum Methodology Index

Status: procedure and evidence-surface map  
Current calibration: 2026-10-04

`METHODOLOGY/**` explains how concrete repository properties are measured or interpreted. A methodology does not create a runtime capability.

## Method map

## 方法、状态与证据速览 / Method, state and evidence guide

| 分界 / Boundary | 本仓可支持 / Supported here | 不能替代 / Does not establish |
| --- | --- | --- |
| `METH-001` | PageRank-derived 图熵与图规模共同解释 / Graph entropy interpreted together with graph population | 零熵表示安全、收敛或非空状态 / Safety, convergence or a non-empty graph |
| `METH-002`, `METH-004` | 单次 SQLite savepoint 事务与局部观察者路径 / One-savepoint transaction and a local observer path | Python 内存状态及外部效果自动回滚 / Automatic rollback of in-memory fields or external effects |
| `METH-003` | 结构、FTS5 top result、排名差值的限定比较 / Scoped structural, lexical top-result and rank comparisons | 广义语义等价或来源事实正确 / General semantic equivalence or source truth |
| `METH-005` | 版本、Git ref、真实 Store、运行身份的显式比对 / Explicit revision, Git ref, store and run identity comparison | 同日记录或相同摘要意味着同一持久化数据库 / Same-day artifacts or equal digests prove the same durable store |

**复验边界 / Replay boundary:** Existing November 15 code-inspection negative cases support these documentary interpretations only, not newly executed R1/R2 ingestion, R3 drift, graph-health checks or long-term persistence / 本次没有重跑 Native 或模拟新的 Store 状态


| Method | Current meaning | Concrete surface |
|---|---|---|
| [METH-001](./METH-001-phase-boundary-detection.md) | Evaluate graph-derived entropy boundary | `CODE/entropy_analyzer.py` |
| [METH-002](./METH-002-reflective-morphing-protocol.md) | Observe one transactional bounded reflection path | `cortex_observer.py`, `continuum_db.py`, `reflective_validator.py` |
| [METH-003](./METH-003-alignment-verification.md) | Review exact claim/source support | repository evidence + research sources |
| [METH-004](./METH-004-cognitive-divergence-rollback.md) | Interpret SQLite savepoint rejection/rollback | `cortex_observer.py`, `continuum_db.py` |
| [METH-005](./METH-005-evidence-continuity-reconciliation.md) | Reconcile store/run/revision/ref/artifact/source continuity by identity | storage + task + retained research history |

## Method contract

Each methodology identifies:

1. exact implementation/evidence surface;
2. real inputs;
3. procedure actually performed;
4. output the surface can support;
5. failure or unresolved conditions;
6. explicit non-claims.

## Cross-method boundaries

- graph entropy threshold != cognition/safety
- local reflection hook != semantic improvement
- FTS5 top-result change != general semantic drift
- ingestion acceptance != source truth
- SQLite rollback != external-system rollback
- fixed-fixture repeatability != durable persistence
- same logical date != shared database identity
- R1 accepted signal + R2 empty store != persistence proof or data-loss proof
- current path presence != historical runtime success
- sibling-branch path presence != observed-branch input visibility
- eventual main visibility != earlier branch-snapshot visibility
- periodic snapshot != replacement for Daily error/failure history

METH-005 operationalizes ADR-010's identity requirement for continuity claims.

## Periodic and historical evidence relation

This index is a durable method map, not a live week/month status surface.

- R1/R2 Daily records remain independent task observations unless a common store identity is retained.
- R3/R4 Weekly synthesis may aggregate or downgrade inherited evidence but cannot erase failures or manufacture continuity.
- R5 stage/monthly synthesis must declare a cutoff and preserve unresolved state.
- Open/closed state for a named week/month belongs to its time-scoped record, not to this methodology index.
- The historical 2026-08-27 statement that W35/formal August R5 were open remains valid at that cutoff and is not rewritten here.

## Repository evidence identity

Keep these identities separate when a method or result is cited:

```text
Git revision
!= Git branch/ref snapshot
!= Python/SQLite environment
!= database/store identity
!= fixture/input identity
!= snapshot digest
!= executed command/result
!= archived publication DOI
```

A repeatable fixed fixture can support repeatability at a recorded revision/environment. It does not prove long-horizon persistence, semantic convergence, or equivalence with a Zenodo archive or later `main`.

## Current navigation

- [ADR index](../ADR/INDEX.md)
- [Engineering specification](../SPECIFICATION.md)
- [Evidence baseline](../EVIDENCE_BASELINE.md)
- [Reproducibility](../REPRODUCIBILITY.md)
- [Release policy](../RELEASE_POLICY.md)

## Historical calibration references

- [August stage audit through 2026-08-27](../historical-audits/03-stage-and-period-audits/2026-08-27--august-through-27--stage-audit.md)
- [Prior cutoff audit through 2026-08-23](../historical-audits/03-stage-and-period-audits/2026-08-23--august-through-23--stage-audit.md)


## 2026-10-04 special calibration

Repository-snapshot identity is now part of continuity reconciliation when one task's evidence depends on whether another artifact was visible from the exact observed branch/ref.

This does not weaken the stronger persistence rule: Git identity and database/store identity remain independent.

## 2026-11-15 concrete method counterexamples

The current method members remain unchanged. Source-path comparison at `0abc7321f17853fcd6874ad81ee98f6ffb48e899` identifies four cases where a scalar or status cannot replace its underlying object identity:

- METH-001: zero graph entropy can represent either no probability mass or a singleton distribution; graph size is required.
- METH-002 / METH-004: SQLite savepoint rollback does not necessarily restore `CortexObserver.phase/current_depth` after unexpected reflector exceptions.
- METH-003: unchanged lexical top result when both queries miss does not prove semantic equivalence; a node-only structural delta can miss edge-only changes.
- METH-005: identical sorted-content digests can occur at different version numbers and do not prove continuity of a durable SQLite store.

These are repository-source interpretations, not fresh experiment claims. Each owning method above now contains its relevant negative-case design.
