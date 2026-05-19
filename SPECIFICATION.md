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

**Phase Transition Interface (相变接口):**
- Triggers transition into the Gaseous Phase (self-observation) when state complexity exceeds the deterministic baseline.
- 当状态复杂性超过确定性基线时，触发进入气态（自我观察）的转换。

---

## 2. Reflection Depth Constraint (反射深度约束)

**Formal Definition (形式化定义):**
The recursive depth of metacognitive self-evaluation is strictly bounded by a deterministic constant $N$. If convergence is not achieved within $N$ layers, the system executes a Cognitive Rejection.
元认知自我评估的递归深度严格受限于一个确定性常数 $N$。如果在 $N$ 层内未达到收敛，系统将执行认知拒绝（Cognitive Rejection）。

**Architectural Constraints (架构约束):**
- The system shall not support unconstrained Test-Time Compute expansions.
- 系统不得支持无约束的测试时计算（Test-Time Compute）扩展。
- Exceeding depth $N$ must immediately halt the current reflection cycle and trigger a rollback to the last verified stable state.
- 超过深度 $N$ 必须立即中止当前反思周期，并触发回滚至上一个已验证的稳定状态。

**Invariants (不变量):**
- $D_{current} \le N$, where $D_{current}$ is the current reflection depth.
- $D_{current} \le N$，其中 $D_{current}$ 为当前反射深度。

**Phase Transition Interface (相变接口):**
- Halts self-observation loops (Gaseous Phase) and forces a return to execution (Liquid Phase) or pure constraint (Plasma Phase) upon Cognitive Rejection.
- 一旦发生认知拒绝，立即中止自我观察循环（气态），并强制返回执行态（液态）或纯约束态（等离子态）。

---

## 3. Cognitive Delta Protocol (认知差分协议)

**Formal Definition (形式化定义):**
The quantitative and qualitative measurement of changes between two knowledge state snapshots, relying purely on deterministic signals without vector embeddings or neural similarities.
在无向量嵌入或神经相似度的情况下，纯粹依靠确定性信号对两个知识状态快照之间的变化进行定量和定性的测量。

**Architectural Constraints (架构约束):**
- **Structural Delta (结构差分):** Evaluated via exact SQL diffs on the knowledge graph schema (nodes added/removed/modified).
- **结构差分：** 通过知识图谱模式上的精确 SQL 差异（节点的增/删/改）进行评估。
- **Rank Delta (排名差分):** Evaluated via the shift in entity PageRank scores. A shift exceeding threshold $\tau$ indicates a significant state mutation.
- **排名差分：** 通过实体 PageRank 分数的偏移进行评估。偏移量超过阈值 $\tau$ 表示发生了显著的状态突变。
- **Semantic Delta (语义差分):** Evaluated via FTS5 query result drift on identical queries across temporal snapshots.
- **语义差分：** 通过在不同时间快照上对相同查询的 FTS5 搜索结果漂移来评估。

**Invariants (不变量):**
- $\Delta(S_{t}, S_{t-1})$ is a deterministic function mapping two states to a precise mathematical difference.
- $\Delta(S_{t}, S_{t-1})$ 是一个确定性函数，将两个状态映射到精确的数学差异。

**Phase Transition Interface (相变接口):**
- Provides the fundamental signals required to determine if the system should persist in execution or trigger a phase boundary check.
- 提供基础信号以决定系统是继续执行还是触发相界检查。

---

## 4. Self-Consistency Verification (自洽性验证)

**Formal Definition (形式化定义):**
Every state mutation or output proposed by the system must be deterministically validated against its own internal corpus of constraints (Architectural Decision Records).
系统提出的每一个状态突变或输出都必须针对其内部约束语料库（架构决策记录）进行确定性的验证。

**Architectural Constraints (架构约束):**
- Inconsistency must trigger a hard rollback. The system does not "rethink"; it enforces.
- 不一致必须触发硬回滚。系统不进行“重新思考”；它只执行约束。
- Verification is an exact matching process (boolean logic) against formalized constraints, avoiding LLM-as-a-judge probabilistic grading.
- 验证是针对形式化约束的精确匹配过程（布尔逻辑），避免使用 LLM 作为裁判的概率性评分。

**Invariants (不变量):**
- $Output \models Constraints$. Any proposed state where this evaluates to `False` is void.
- $输出 \models 约束$。任何评估结果为 `False` 的拟议状态均无效。

**Phase Transition Interface (相变接口):**
- Serves as the ultimate gatekeeper for phase transitions; transitions are only permitted if self-consistency invariant holds.
- 作为相变的最终守门人；只有在自洽性不变量成立的情况下，才允许进行相变。

---

## 5. Phase Boundary Detection (相界检测)

**Formal Definition (形式化定义):**
The deterministic identification of topological complexity tipping points that mandate a shift from standard execution (Liquid Phase) to metacognitive self-observation (Gaseous Phase).
确定性地识别拓扑复杂性临界点，该临界点要求系统从标准执行态（液态）切换到元认知自观察态（气态）。

**Architectural Constraints (架构约束):**
- Boundary detection is computed via the topological entropy of the knowledge graph (based on the PageRank distribution).
- 边界检测通过知识图谱的拓扑熵（基于 PageRank 分布）来计算。
- When entropy $H(PageRank) > H_{threshold}$, the system acknowledges sufficient structural complexity and triggers a phase transition.
- 当熵 $H(PageRank) > H_{threshold}$ 时，系统确认已积累足够的结构复杂性，并触发相变。

**Invariants (不变量):**
- The phase transition function is a strict step function dependent solely on graph topology, completely independent of heuristics or learned policies.
- 相变函数是一个严格的阶跃函数，仅依赖于图拓扑，完全独立于启发式或学习策略。

**Phase Transition Interface (相变接口):**
- Executes the modal shift from collaborative execution to pure self-observation.
- 执行从协作执行到纯粹自观察的模式切换。
