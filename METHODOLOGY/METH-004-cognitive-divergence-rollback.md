# METH-004: Cognitive Divergence Alert and Hard Rollback
# METH-004：认知发散警报与硬回滚

## 1. Introduction (简介)
**English:**
Building upon ADR-009, this methodology formalizes the mechanical process for detecting semantic drift during deep autonomous reasoning and executing an absolute Hard Rollback. This protocol ensures that any generated hallucination chain is instantly severed before impacting the Liquid (execution) phase.

**中文 (Chinese):**
基于 ADR-009，本方法论形式化了在深度自主推理期间检测语义漂移以及执行绝对硬回滚的机械过程。该协议确保任何生成的幻觉链在影响液态（执行）相之前被立即切断。

## 2. Triggering the Alert (触发警报)
**English:**
The "Cognitive Divergence Alert" is not based on a neural reward model. It is triggered deterministically if any of the following boundaries are breached during the Gaseous (Reflection) Phase:
1. **Convergence Failure:** The Cryptographic State Lock (Convergence hash) fails to reach a zero-entropy state after $N$ iterations (typically 100).
2. **Entropy Threshold Exceeded:** Topological entropy ($H$) remains $> 1.0$ after the allocated Gas duration.
3. **FTS5 Validation Failure:** The resulting Structural Delta violates constraints parsed by the `Reflective Validator` from the ADR corpus.

**中文 (Chinese):**
“认知发散警报”不是基于神经奖励模型。如果在气态（反射）阶段违反了以下任何边界，它将被确定性地触发：
1. **收敛失败：** 密码学状态锁（收敛哈希）在 $N$ 次迭代（通常为100次）后未能达到零熵状态。
2. **超过熵阈值：** 在分配的气态持续时间之后，拓扑熵 ($H$) 仍然 $> 1.0$。
3. **FTS5 验证失败：** 生成的结构差分违反了 `Reflective Validator` 从 ADR 语料库解析的约束。

## 3. The Hard Rollback Mechanism (硬回滚机制)
**English:**
Upon triggering a Cognitive Divergence Alert, the system executes an immediate and strict Hard Rollback:
1. The execution pipeline is halted; no further state transitions are considered.
2. The SQLite SAVEPOINT for the current iteration is unequivocally rolled back (`ROLLBACK TO SAVEPOINT current_reflection`).
3. The rejected Structural Delta is purged from memory and is strictly recorded as 'NONE' (if no data was committed) or logged in the Hard Rollback Log for forensic phase transition analysis.
4. The system is structurally prevented from attempting to probabilistically "re-reason" or self-correct the discarded state. It forces a return to the last mathematically proven zero-entropy state.

**中文 (Chinese):**
在触发认知发散警报时，系统将执行立即且严格的硬回滚：
1. 停止执行管道；不再考虑进一步的状态转换。
2. 明确回滚当前迭代的 SQLite SAVEPOINT (`ROLLBACK TO SAVEPOINT current_reflection`)。
3. 从内存中清除被拒绝的结构差分，并严格记录为 'NONE'（如果未提交数据）或将其记录在硬回滚日志中以进行法医相变分析。
4. 系统在结构上被禁止尝试概率性地“重新推理”或自我纠正被丢弃的状态。它强制返回到最后一个经过数学证明的零熵状态。
