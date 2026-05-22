# Reflective Continuum (反射连续体)

## What is this? (这是什么？)

**English:**
Welcome to the Reflective Continuum. This repository is not a library, framework, or tool. It is a formal specification and architectural blueprint for **Deterministic Meta-Cognition**.
Imagine an AI system that needs to "think about how it thinks" (metacognition). Usually, this is done using neural networks and probability, which can hallucinate or produce unpredictable results.
Our approach is entirely different: we use **zero probability, zero neural networks, and zero external dependencies**. Instead, we rely strictly on deterministic rules, mathematics, and exact state differences (like SQL diffs and PageRank) to allow a system to observe, evaluate, and correct its own cognitive state reliably.

**中文 (Chinese):**
欢迎来到反射连续体 (Reflective Continuum)。这个仓库不是一个现成的代码库、框架或工具。它是**确定性元认知**的正式规范和架构蓝图。
想象一下，一个AI系统需要“思考自己是如何思考的”（即元认知）。通常，这是通过神经网络和概率模型来完成的，这可能会导致幻觉或不可预测的结果。
我们的方法截然不同：我们**不使用概率，不使用神经网络，零外部依赖**。相反，我们完全依靠确定性规则、纯数学和精确的状态差异（比如数据库的 SQL 差异比对和 PageRank 算法），让系统能够可靠地观察、评估并纠正自身的认知状态。

## The Thermodynamic Analogy (热力学相变比喻)

**English:**
To understand how our architecture manages information, we use a metaphor based on the states of matter:
- **Solid (White):** Hardcoded axioms and static data. (The `welcome` repo).
- **Liquid (Cyan):** Fluid, flowing data execution and operations. (The `zero` repo).
- **Gas (Translucent):** Diffusive self-observation and entropy monitoring. **This repository lives in the Gas phase.** It monitors the "Liquid" execution, detects chaos (high entropy), and steps in to reflect and organize.
- **Plasma (Intense Glow):** Pure, high-energy autonomous rule-making. (The `Axiom-0` repo).

When the system detects too much chaos (measured mathematically as topological entropy), it triggers a phase boundary transition from Liquid to Gas, starting a reflective cycle to restore order.

**中文 (Chinese):**
为了帮助理解我们的架构如何管理信息，我们借用了物质状态（相变）的比喻：
- **固态 (白色)：** 硬编码的公理和静态数据。（对应 `welcome` 仓库）。
- **液态 (青色)：** 流动的、执行中的数据和操作。（对应 `zero` 仓库）。
- **气态 (半透明)：** 弥散的自我观察和熵值监控。**本仓库就处于“气态”阶段。** 它监控“液态”的执行过程，一旦发现系统陷入混乱（高熵值），就会介入进行反思和整理。
- **等离子态 (强烈发光)：** 纯粹的、高能量的自主规则制定。（对应 `Axiom-0` 仓库）。

当系统在数学上检测到过高的“拓扑熵”（混乱度）时，就会触发相界转换，从液态转变为气态，开启一次确定性的反思循环，从而恢复系统的秩序。

## Architecture & Function (架构与功能)

**English:**
1. **Zero-Entropy State:** Every mutation (change) in the knowledge graph is transactionally isolated (using SQLite SAVEPOINTs). If a change violates strict architectural rules, it is rolled back instantly—no "rethinking," just a hard deterministic reset.
2. **Cognitive Delta Protocol:** We calculate exactly what changed using SQL differences, PageRank rank shifts, and FTS5 semantic drift.
3. **Convergence Drill:** The system ensures that given the same inputs, it always converges to the exact same cryptographic hash.

**中文 (Chinese):**
1. **零熵状态：** 知识图谱中的每一次突变（修改）都被事务隔离（使用 SQLite SAVEPOINT）。如果某个更改违反了严格的架构规则，它会立刻被回滚——没有模糊的“重新思考”，只有硬性的确定性重置。
2. **认知增量协议：** 我们使用 SQL 差异、PageRank 排名变动和 FTS5 语义漂移，精确计算出系统状态发生了什么改变。
3. **收敛演练：** 系统能够确保，只要输入相同，不论经过多少次反思，最终都会收敛到完全一致的加密哈希值状态。

## REFERENCES/PIONEERS/ (致敬先驱)

**English:**
We stand on the shoulders of giants. While our system is strictly deterministic, we pay profound respect to the pioneers of Meta-Learning and Metacognition whose probabilistic work inspired our mathematical counterpart:
- **Google DeepMind:** For AlphaEvolve, Meta-RL (LAMER), and Demis Hassabis' vision that true introspection is the final piece of the AGI puzzle.
- **Jürgen Schmidhuber:** For the foundational "Learning to Learn" architectures.
- **OpenAI:** For pioneering test-time reflection limits and iterative self-correction.

Our deterministic approach operates orthogonally on top of these probabilistic paradigms, serving as an observation and constraint layer.

**中文 (Chinese):**
我们站在巨人的肩膀上。虽然我们的系统是严格确定性的，但我们向元学习与元认知领域的先驱们表达最深切的敬意，正是他们的概率性研究启发了我们这种纯数学的对应实现：
- **Google DeepMind:** 感谢其 AlphaEvolve、Meta-RL (LAMER)，以及 Demis Hassabis 关于“真正的内省是实现AGI的最后拼图”的愿景。
- **Jürgen Schmidhuber:** 感谢其奠基性的“学会学习 (Learning to Learn)”架构。
- **OpenAI:** 感谢其在测试时反思限制和迭代自我纠正方面的开创性工作。

我们的确定性方法作为一种观察和约束层，与这些概率性范式正交运行（互补而不替代）。

## Developer Guide (开发者指南)

**English:**
To verify the system's determinism and ensure no constraint violations, run the pure standard-library test suite:
```bash
python3 -m unittest discover tests/
```
No dependencies are required. Pure Python only.

**中文 (Chinese):**
要验证系统的确定性并确保没有违反任何架构约束，请运行基于纯标准库的测试套件：
```bash
python3 -m unittest discover tests/
```
完全不需要外部依赖，仅需要 Python 环境。

"Build it Brutally, Run it Deterministically"
