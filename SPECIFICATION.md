# Reflective Continuum: Formal Specification
# 反射连续体：形式化规范

This document defines the deterministic metacognition protocol. It outlines the rules by which a system observes, evaluates, and corrects its own cognitive processes.
本文档定义了确定性元认知协议。它概述了系统观察、评估和纠正自身认知过程的规则。

---

## 1. Metacognition as Deterministic Self-Observation (元认知即确定性自观察)

**Formal Definition (形式化定义):**
Metacognition is the deterministic observation and rule-driven self-correction of the system's own cognitive state. It contains zero probabilistic sampling, zero neural network inference, and requires zero human intervention.
元认知是对系统自身认知状态的确定性观察和规则驱动的自我纠正。它包含零概率采样，零神经网络推断，且需要零人工干预。

**Architectural Constraints (架构约束):**
- All introspective actions must be computable via standard graph queries (e.g., SQL), matrix operations (e.g., PageRank), or deterministic string/AST matching.
- 所有内省行为必须可以通过标准图查询（如SQL）、矩阵运算（如PageRank）或确定性字符串/AST匹配来计算。
- The system must mathematically prove its state changes, rather than predicting or estimating them.
- 系统必须在数学上证明其状态的变化，而不是预测或估计它们。

**Invariants (不变量):**
- The probability of an introspective state transition is either exactly `0` or `1`.
- 内省状态转换的概率必须且只能是 `0` 或 `1`。

---

## 2. Reflection Depth Constraint (反射深度约束) - ADR-002

**Formal Definition (形式化定义):**
The recursive depth of metacognitive self-evaluation is strictly bounded by a deterministic constant $N$. If convergence is not achieved within $N$ layers, the system executes a Cognitive Rejection.
元认知自我评估的递归深度严格受限于一个确定性常数 $N$。如果在 $N$ 层内未达到收敛，系统将执行认知拒绝（Cognitive Rejection）。

**Invariants (不变量):**
- $D_{current} \le N$, where $D_{current}$ is the current reflection depth.
- $D_{current} \le N$，其中 $D_{current}$ 为当前反射深度。

---

## 3. Cognitive Delta Protocol (认知差分协议) - ADR-003

**Formal Definition (形式化定义):**
The quantitative and qualitative measurement of changes between two knowledge state snapshots, relying purely on deterministic signals without vector embeddings or neural similarities.
在无向量嵌入或神经相似度的情况下，纯粹依靠确定性信号对两个知识状态快照之间的变化进行定量和定性的测量。

**Components (组成部分):**
1. **Structural Delta (结构差分):** Evaluated via exact SQL diffs.
   **结构差分：** 通过精确 SQL 差异评估。
2. **Rank Delta (排名差分):** Evaluated via the shift in entity PageRank scores.
   **排名差分：** 通过实体 PageRank 分数的偏移评估。
3. **Semantic Delta (语义差分):** Evaluated via FTS5 query result drift.
   **语义差分：** 通过 FTS5 搜索结果漂移评估。

---

## 4. Phase Boundary Detection (相界检测) - ADR-005

**Formal Definition (形式化定义):**
The deterministic identification of topological complexity tipping points that mandate a shift from standard execution (Liquid Phase) to metacognitive self-observation (Gaseous Phase).
确定性地识别拓扑复杂性临界点，该临界点要求系统从标准执行态（液态）切换到元认知自观察态（气态）。

**Measurement (测量):**
- Boundary detection is computed via the topological entropy $H(P)$ of the knowledge graph (based on the PageRank distribution).
- 边界检测通过知识图谱的拓扑熵 $H(P)$（基于 PageRank 分布）来计算。
