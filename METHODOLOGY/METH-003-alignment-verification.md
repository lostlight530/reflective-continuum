> [!NOTE]
> **Current architecture interpretation — 2026-09-18**
> - **Subject class:** `METHOD`
> - **Role:** Current methodology: **Claim and source support review**
> - **Authority:** Repository-native method authority for the exact procedure, observation rule, assumptions and limits stated by this file
> - **Current meaning:** Treat the named method as a repeatable interpretation/checking contract. Method definition does not imply execution on the current revision, and historical examples do not become current state by proximity
> - **Evidence / implementation boundary:** FTS lexical change is not semantic truth; reflector callback behavior is not autonomous cognition; SQLite savepoint rollback is local transaction rollback; persistence and convergence require explicit store/run evidence rather than terminology alone
> - **Cross-document relation:** Specification/runtime code bound mechanics; ADRs explain durable choices; dated evidence records observations; Reproducibility owns revision/store/replay identity
> - **Update trigger:** Update when procedure, threshold, implementation mapping, historical evidence range or failure/reconciliation semantics materially changes
> - **Preservation rule:** Existing method procedure and examples remain in place; current clarification does not rewrite earlier execution evidence

# Claim and source support review

## 中文专业内容定位 / Chinese technical counterpart

**研究或方法的真实对象 / Object:** 来源支持与 claim 对齐需可复核来源、确切版本与反证，FTS5 命中并不证明语义一致

**Original English title:** Claim and source support review

**可执行证明 / Execution evidence:** 只以已发生的精确版本与 Store/输入/命令收据支持运行声明，外部论文与 references 属于非规范上下文，历史记录不得由后来 main 自动覆盖 / Only exact revision, store, input and command receipts support execution, while external references stay non-normative and historic artifacts retain their original cutoffs

| English section / 原章 | 中文对应说明 / Chinese section |
| --- | --- |
| Objective | 目标 |
| Inputs | 输入 |
| Procedure | 方法步骤 |
| Outputs | 输出 |
| Failure conditions | 失败条件 |
| Required distinctions | 主题的具体条件与非声明 |
| Evidence boundary | 证据边界 |
| Typed counterexamples for alignment language | 主题的具体条件与非声明 |

**审查规则 / Review:** 本节提供中文阅读而不新增方法运行、Graph 测试或跨存储持久化证据 / This bilingual layer adds no method execution, graph test or cross-store continuity proof


- Method version: 2026-08-24
- Scope: repository behavior, research records, and external-source propositions

## Objective

Determine what an exact evidence surface supports without collapsing ingestion, local execution, persistence, source authority, and factual support into one “alignment” result.

## Inputs

- exact claim/proposition
- repository artifact or implementation surface relevant to the claim
- source identity/version when external evidence is used
- observation/revision/time boundary
- known counterevidence or unresolved fields

## Procedure

1. Classify the claim as local implementation, local observation, external proposition, inference, or continuity claim.
2. Select the evidence surface that actually bears on that claim.
3. For external material, separate source identity/authority from whether the source supports the exact proposition.
4. For local behavior, keep store/query/version/fixture scope explicit.
5. Preserve rejected signals, errors, missing fields, and conflicting evidence.
6. Narrow the wording when the evidence supports only a weaker proposition.
7. Use `SOURCE_CLAIM_MISMATCH` when the cited source does not support the stored proposition.
8. Use an unresolved state rather than inferring persistence when object identity is not linked.

## Outputs

- bounded claim text
- evidence surface
- claim-support state
- local implementation/observation state where relevant
- unresolved/untested dimensions

## Failure conditions

The procedure fails closed when the compared versions, query, PageRank configuration, threshold, or retained output is missing, or when a structural/lexical/rank result is promoted into semantic truth, safety, or general alignment.

## Required distinctions

- `ACCEPTED` != source truth
- `REJECTED_FROM_INGESTION` != source falsification
- selfcheck pass != historical health
- lexical top-result stability != semantic equivalence
- repeated snapshot digest != durable memory
- source reachability != proposition support

## Evidence boundary

This method bounds evidence strength. It does not make the repository an alignment evaluator or prove a global safety property.

## Typed counterexamples for alignment language

A returned `ProcessResult(accepted=True)` is evidence only that node/content validation and local transaction flow accepted the signal. It is **not** evidence that the proposition described in `content` is supported by a source.

A `compute_semantic_delta(...)=False` result can arise when **both FTS5 searches return no top match**. It therefore does not support a statement of semantic stability, even if both graph versions are otherwise non-identical. Likewise `compute_structural_delta` does not inspect edge-only changes. When evaluating an "alignment" claim, name the proposition and source-support surface independently of these two local signals; retain a `SOURCE_CLAIM_MISMATCH` or `UNRESOLVED` disposition where appropriate.
