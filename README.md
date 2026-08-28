# Reflective Continuum | 反射连续体

Reflective Continuum is a standard-library Python reference for versioned graph storage and bounded analysis. It provides SQLite persistence, synchronized FTS5 lexical search, version deltas, PageRank-derived Shannon entropy, explicit validation, transactional ingestion, and optional bounded reflection hooks.

Reflective Continuum 是一个基于 Python 标准库的版本化图存储与有界分析参考实现。它提供 SQLite 持久化、同步的 FTS5 词法搜索、版本差异、由 PageRank 派生的 Shannon 熵、显式校验、事务式写入，以及可选的有界反射钩子。

## Executable contracts | 可执行合同

### Storage and search | 存储与搜索

Nodes are keyed by `(node_id, version)`. Edges are keyed by `(source_id, target_id, relationship, version)`, with both endpoints required at the same version. Every connection enables and verifies SQLite foreign keys. Insert, update, and delete triggers synchronize node content to an external-content FTS5 index. Node upserts use `ON CONFLICT DO UPDATE`, not `REPLACE`.

节点以 `(node_id, version)` 为键；边以 `(source_id, target_id, relationship, version)` 为键，两个端点必须位于同一版本。每个连接都会启用并验证 SQLite 外键。插入、更新和删除触发器把节点内容同步到外部内容 FTS5 索引。节点更新使用 `ON CONFLICT DO UPDATE`，不使用 `REPLACE`。

Search is quoted lexical phrase matching, optionally scoped to a version, limited to 1–100 results, and ordered deterministically by BM25 score and identifiers. It is lexical retrieval, not semantic equivalence.

搜索采用带引号的词法短语匹配，可限定版本和 1–100 条结果，并按 BM25 分数与标识符确定性排序。它是词法检索，不代表语义等价。

### Deltas and analysis | 差异与分析

The bounded comparison APIs are:

- Structural delta: sorted added, removed, and content-modified node identifiers between versions.
- Search-result delta: whether the top lexical result changes for the same caller-declared query.
- Rank delta: nodes whose absolute PageRank score shift exceeds a caller-declared non-negative threshold.

有界比较 API 包括：结构差异返回版本间新增、删除和内容修改的节点；搜索结果差异报告同一指定查询的首个词法结果是否变化；排名差异返回 PageRank 分数绝对变化超过调用者所设非负阈值的节点。

PageRank validates nodes, edges, and configuration, collapses duplicate edges, and normalizes output. Shannon entropy is computed from normalized finite non-negative PageRank scores and reported in nats. A threshold result applies only to the declared graph, configuration, and revision; it does not establish intelligence, instability, truth, or safety.

PageRank 会校验节点、边和配置，折叠重复边并归一化输出。Shannon 熵由有限、非负且归一化的 PageRank 分数计算，单位为 nat。阈值结果只对指定图、配置和版本成立，不能据此断言智能、不稳定性、真理或安全性。

### Validation, transactions, and hooks | 校验、事务与钩子

`RuleConfig` is executable policy. Content and identifiers are validated explicitly; Python source checks use the AST and the current interpreter's standard-library module set. ADR prose is documentation, not runtime configuration.

`RuleConfig` 是可执行策略。内容和标识符会被显式校验；Python 源码检查使用 AST 与当前解释器的标准库模块集合。ADR 文本是文档，不是运行时配置。

`CortexObserver.process_input` validates caller data and performs accepted ingestion in one savepoint-backed transaction. Policy rejection returns a structured `ProcessResult`; unexpected database and programming errors propagate. Above the configured entropy threshold, an optional reflection hook runs at most once per configured depth before state is recomputed. Exhausting the configured bound rolls back the transaction.

`CortexObserver.process_input` 校验调用者数据，并在一个由保存点支持的事务中完成被接受的写入。策略拒绝返回结构化 `ProcessResult`；意外的数据库和编程错误会继续抛出。超过配置的熵阈值后，可选反射钩子在每一层最多执行一次，再重新计算状态；耗尽配置上限会回滚事务。

## Task entrypoints | 任务入口

Tasks are importable libraries with bounded CLIs. Default output is structured JSON on stdout. `semantic_drift_audit` and `cortex_selfcheck` write only when an explicit `--output` path is supplied.

任务既可作为库导入，也提供有界 CLI。默认在标准输出打印结构化 JSON；`semantic_drift_audit` 与 `cortex_selfcheck` 仅在显式提供 `--output` 路径时写文件。

```text
python -m CODE.tasks.insight_morpher signals.json
python -m CODE.tasks.semantic_drift_audit graph.db "declared query" --from-version 1 --to-version 2
python -m CODE.tasks.cortex_selfcheck --database graph.db
python -m CODE.tasks.convergence_drill --iterations 100
```

The convergence drill rebuilds a fixed local fixture and compares snapshot digests. It is a repeatability check, not a general convergence claim.

收敛演练会重建固定本地夹具并比较快照摘要；它是重复性检查，不是一般性的收敛证明。

## Migration warning | 迁移警告

Databases created with the earlier edge schema require an explicit migration before this revision is used. Do not silently reinterpret or overwrite rows. Back up the database, record schema and environment, migrate a copy, verify foreign keys and `PRAGMA integrity_check`, and test restore procedures before replacing an operational file.

使用旧版边结构创建的数据库必须先显式迁移。不要静默重释或覆盖数据。请先备份并记录结构与环境，在副本上迁移，验证外键和 `PRAGMA integrity_check`，并在替换运行文件前测试恢复流程。

## Verification | 验证

The commands below are local verification entry points and require SQLite with FTS5. The repository currently has no GitHub Actions workflow that runs Python tests; its workflow deploys the static Pages surface. A Pages deployment is not evidence for runtime behavior, research claims, or document semantics. From the repository root, run:

以下命令是本地验证入口，并要求 SQLite 支持 FTS5。仓库当前没有运行 Python 测试的 GitHub Actions 工作流；现有 workflow 只部署静态 Pages。Pages 发布不能作为 runtime、研究结论或文档语义的验证证据。在仓库根目录执行：

```text
python -m compileall -q CODE tests scope_guard.py
python -m unittest discover -s tests -v
python -m CODE.tasks.cortex_selfcheck
python -m CODE.tasks.convergence_drill --iterations 100
```

Record the commit SHA, Python and SQLite versions, fixture or digest, query/version/threshold, commands, exit codes, and untested boundaries. Passing results apply only to the tested revision and configuration.

请记录提交 SHA、Python 与 SQLite 版本、夹具或摘要、查询/版本/阈值、命令、退出码和未测试边界。通过结果只适用于被测试的版本与配置。

## Non-goals and ownership | 非目标与责任边界

This repository is not a cognitive system, semantic embedding model, truth engine, safety proof, autonomous researcher, distributed database, authentication or authorization service, or production service. Callers own database permissions, isolation, backups, encryption, retention, quotas, untrusted-input controls, and incident response.

本仓库不是认知系统、语义嵌入模型、真理引擎、安全证明、自主研究者、分布式数据库、认证授权服务或生产服务。数据库权限、隔离、备份、加密、保留策略、配额、不可信输入控制与事件响应均由调用者负责。

## Governing evidence | 规范与证据

- [Engineering specification](SPECIFICATION.md) | 工程规范
- [Evidence baseline](EVIDENCE_BASELINE.md) | 证据基线
- [Reproducibility](REPRODUCIBILITY.md) | 可复现性
- [Security policy](SECURITY.md) | 安全策略
- [Long-term maintenance contract](GOVERNANCE/MAINTENANCE.md) | 长期维护契约
