# Reflective Continuum (反射连续体)

## Formal specification of reflective state transitions in deterministic continua (确定性连续体中反射状态转换的形式化规范)

### Statement (声明)

This repository defines reflective state transitions — the protocol by which a deterministic system observes, evaluates, and corrects its own cognitive processes without probability, without neural inference, and without human intervention.
本仓库定义了反射状态转换——这是一种协议，确定性系统通过该协议观察、评估并纠正其自身的认知过程，且不包含概率、没有神经推理、无需人工干预。

It does not implement. It constrains.
它不负责实现。它负责约束。

### Core Definitions (核心定义)

#### 1. Metacognition (Definition 1.1) | 元认知（定义 1.1）
A deterministic observation and rule-driven self-correction of the system's own cognitive state. Contains no probabilistic sampling. Contains no neural network inference.
对系统自身认知状态的确定性观察和规则驱动的自我纠正。不包含概率采样。不包含神经网络推理。

#### 2. Reflection Depth Constraint (Definition 1.2) | 反射深度约束（定义 1.2）
The number of reflective layers is bounded by a deterministic constant N. Exceeding N without convergence is classified as Cognitive Rejection — the system does not recurse indefinitely.
反射层数受限于确定性常数 N。如果不收敛而超过 N，则被归类为认知拒绝——系统不会无限递归。

#### 3. Cognitive Delta Protocol (Definition 1.3) | 认知差分协议（定义 1.3）
Deterministic difference detection between two knowledge graph snapshots. Implemented via SQL diff + PageRank rank shift + FTS5 semantic drift. No embedding. No vector similarity.
两个知识图谱快照之间的确定性差异检测。通过 SQL 差异、PageRank 排名偏移和 FTS5 语义漂移实现。无嵌入。无向量相似度。

#### 4. Self-Consistency Verification (Definition 1.4) | 自洽性验证（定义 1.4）
System output must pass deterministic validation against its own constraint set (ADR corpus). Inconsistency triggers rollback, not "rethinking."
系统输出必须通过针对其自身约束集（ADR 语料库）的确定性验证。不一致会触发回滚，而不是“重新思考”。

#### 5. Phase Boundary Detection (Definition 1.5) | 相界检测（定义 1.5）
When the PageRank topological entropy of the knowledge state exceeds a threshold, the system transitions from execution mode to reflection mode — a phase change in the continuum.
当知识状态的 PageRank 拓扑熵超过阈值时，系统从执行模式转换到反思模式——连续体中的相变。

### Phase Topology (相态拓扑)

```plaintext
  Solid ──── Liquid ──── Gas ──── Plasma
   │           │          │          │
 welcome    zero      this repo   Axiom-0
   │           │          │          │
 daily      weekly    zero+auto   full-auto
 human      human     self-obs     rule-only
 alive     efficient  reflective   axiomatic

  固态 ──── 液态 ──── 气态 ──── 等离子态
   │           │          │          │
 welcome    zero      本仓库      Axiom-0
   │           │          │          │
 每日人工    每周人工  零人工自动   全自动
 鲜活       高效       自检反思    纯粹公理
```

This repository occupies the Gas phase — diffusive, self-observing, filling the gap between collaborative execution and pure constraint.
本仓库占据气态相——扩散性、自我观察，填补了协作执行和纯粹约束之间的空白。

### What This Repository Is Not (本仓库不是什么)

Not a library. Not a framework. Not a tool.
不是库。不是框架。不是工具。

Not an implementation of probabilistic metacognition — it is the specification and structural scaffold of how metacognition must behave under strictly deterministic constraints.
不是概率元认知的实现——它是关于在严格的确定性约束下元认知必须如何运行的规范和结构支架。

Not dependent on any external package. Python stdlib + SQLite + pure mathematics only.
不依赖于任何外部包。仅使用 Python 标准库 + SQLite + 纯数学。

## Homage & Coordinates (致敬与坐标)

We stand on the shoulders of giants. This repository specifically pays profound respect to the pioneers of Meta-Learning and Metacognition:
我们站在巨人的肩膀上。本仓库向元学习与元认知领域的先驱们表达最深切的敬意：
- **Google DeepMind:** For AlphaEvolve, Meta-RL (LAMER), and Demis Hassabis' vision that true introspection is the final piece of the AGI puzzle.
- **Jürgen Schmidhuber:** For the foundational "Learning to Learn" architectures.
- **OpenAI:** For pioneering test-time reflection limits.

*See `REFERENCES/PIONEERS/` for our full acknowledgments and how our deterministic approach serves as a strict mathematical counterpart to their probabilistic and Reinforcement Learning achievements.*
*详见 `REFERENCES/PIONEERS/` 了解我们完整的致敬内容，以及我们如何将这种确定性方法作为他们概率与强化学习成就的严格数学对应物。*

## Engineering Architecture (工程架构)

While defining the formal continuum, this repository also houses the zero-dependency structural scaffolding needed to execute the proofs:
在定义形式化连续体的同时，本仓库还包含了执行这些证明所需的零依赖结构脚手架：
- `CODE/`: The core deterministic routines including `continuum_db.py`, `cortex_observer.py`, `drift_detector.py`, `entropy_analyzer.py`, `reflective_validator.py`. (核心确定性例程，采用硬核赛博命名法)
- `CODE/tasks/`: Specialized task executors (`entropy_collapse_drill.py`, `cognition_dehydrator.py`, `axiom_decay_scanner.py`) intended ONLY for external Agent execution. (特化任务执行器，仅限外部 Agent 运行)
- `tests/`: Pure `unittest` modules verifying invariants without external frameworks. (验证不变量的纯 `unittest` 模块)
- `ADR/` & `METHODOLOGY/`: The binding architectural constraints. (具有约束力的架构决策记录和方法论)

## Deterministic Workflow (确定性工作流)

To run the verification suite and ensure no constraint violations exist:
运行验证套件以确保不存在违反约束的情况：
```bash
python3 -m unittest discover tests/
```

*Note: Daily CI runs via GitHub Actions automatically enforce these invariants.*
*注意：通过 GitHub Actions 运行的日常 CI 自动强制执行这些不变量约束。*

### What This Repository Answers (本仓库回答了什么)

Can a system know what it knows — without probability?
一个系统能否在没有概率的情况下，知道它自己所知道的？

The answer is a protocol, not an experiment.
答案是一个协议，而不是一场实验。

**"Build it Brutally, Run it Deterministically"**
**“以暴力美学构建，以确定性法则运行”**
