# Reflective Morphing Protocol
# 反射性结构变形协议

## 1. Introduction (简介)
This document outlines the Reflective Morphing Protocol, defining how the deterministic system alters its own structural knowledge when operating under self-observation (the Gaseous Phase).
本文档概述了反射性结构变形协议，定义了确定性系统在自我观察下（气态）运行时如何改变其自身的结构化知识。

## 2. Deterministic Generation and Verification (确定性生成与验证)
Unlike probabilistic evolutionary systems that rely on iterative sampling and neural evaluators, structural morphing in the Reflective Continuum operates through exact generation and deterministic verification.
与依赖于迭代采样和神经评估器的概率进化系统不同，反射连续体中的结构变形通过精确生成和确定性验证来进行运作。

### 2.1 The Morphing Cycle (变形循环)
1. **State Fork (状态分叉):** The system isolates its current knowledge snapshot via a deterministic `multiprocessing` fork or identical database transaction isolation.
   **状态分叉：** 系统通过确定性的 `multiprocessing` 分叉（fork）或完全一致的数据库事务隔离，来隔离其当前的知识快照。
2. **Constraint Application (约束施加):** The system applies the formal rules defined in the ADR corpus to the isolated state.
   **约束施加：** 系统将ADR语料库中定义的正式规则应用于隔离的状态。
3. **Difference Measurement (差分测量):** The Structural, Rank, and Semantic Deltas are computed strictly according to ADR-003.
   **差分测量：** 严格按照 ADR-003 计算结构、排名和语义差分。
4. **Consensus Merge (共识合并):** If and only if the Delta satisfies all consistency verification protocols (ADR-004), the forked state is merged back into the main continuum.
   **共识合并：** 当且仅当差分满足所有自洽性验证协议（ADR-004）时，分叉的状态才被合并回主连续体中。

## 3. Strict Prohibitions (严格禁令)
- **No Probabilistic Candidate Generation:** The system does not "guess" structural changes. It deduces them via boolean logic from existing constraints.
  **禁止概率性候选生成：** 系统不“猜测”结构变化。它通过布尔逻辑从现有约束中推导它们。
- **No Hallucinated Evaluations:** Evaluators must be exact rules. If a rule does not exist to evaluate a morph, the morph is rejected.
  **禁止幻觉评估：** 评估器必须是精确的规则。如果不存在评估某种变形的规则，则拒绝该变形。
