Reflective Continuum

Formal specification of reflective state transitions in deterministic continua

Statement

This repository defines reflective state transitions — the protocol by which a deterministic system observes, evaluates, and corrects its own cognitive processes without probability, without neural inference, and without human intervention.

It does not implement. It constrains.

Core Definitions

1. Metacognition (Definition 1.1)

A deterministic observation and rule-driven self-correction of the system's own cognitive state. Contains no probabilistic sampling. Contains no neural network inference.

2. Reflection Depth Constraint (Definition 1.2)

The number of reflective layers is bounded by a deterministic constant N. Exceeding N without convergence is classified as Cognitive Rejection — the system does not recurse indefinitely.

3. Cognitive Delta Protocol (Definition 1.3)

Deterministic difference detection between two knowledge graph snapshots. Implemented via SQL diff + PageRank rank shift + FTS5 semantic drift. No embedding. No vector similarity.

4. Self-Consistency Verification (Definition 1.4)

System output must pass deterministic validation against its own constraint set (ADR corpus). Inconsistency triggers rollback, not "rethinking."

5. Phase Boundary Detection (Definition 1.5)

When the PageRank topological entropy of the knowledge state exceeds a threshold, the system transitions from execution mode to reflection mode — a phase change in the continuum.

Phase Topology

plaintext
  Solid ──── Liquid ──── Gas ──── Plasma
   │           │          │          │
 welcome    zero      this repo   Axiom-0
   │           │          │          │
 daily      weekly    zero+auto   full-auto
 human      human     self-obs     rule-only
 alive     efficient  reflective   axiomatic


This repository occupies the Gas phase — diffusive, self-observing, filling the gap between collaborative execution and pure constraint.

What This Repository Is Not

Not a library. Not a framework. Not a tool.
Not an implementation of probabilistic metacognition — it is the specification and structural scaffold of how metacognition must behave under strictly deterministic constraints.
Not dependent on any external package. Python stdlib + SQLite + pure mathematics only.

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
- `src/reflective_continuum/`: The core deterministic routines (`delta`, `phase`, `morph`).
- `tests/`: Pure `unittest` modules verifying invariants without external frameworks.
- `ADR/` & `METHODOLOGY/`: The binding architectural constraints.

## Deterministic Workflow (确定性工作流)

To run the verification suite and ensure no constraint violations exist:
运行验证套件以确保不存在违反约束的情况：
```bash
python -m unittest discover tests/
```

What This Repository Answers

Can a system know what it knows — without probability?

The answer is a protocol, not an experiment.

"Build it Brutally, Run it Deterministically"
