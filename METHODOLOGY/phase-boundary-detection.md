# Phase Boundary Detection
# 相界检测

## 1. Introduction (简介)
This document outlines the mathematical framework governing how the Reflective Continuum transitions between states of execution and self-observation.
本文档概述了管理反射连续体如何在执行状态和自我观察状态之间转换的数学框架。

## 2. Topological Entropy (拓扑熵)
The phase boundary is strictly defined by the system's topological complexity. We measure this complexity without relying on heuristic triggers or learned metadata.
相界由系统的拓扑复杂性严格定义。我们在不依赖启发式触发器或学习元数据的情况下测量此复杂性。

### 2.1 Calculation (计算)
Let $P$ be the stationary distribution vector of the system's knowledge graph resulting from the PageRank algorithm. For each node $i$, $p_i$ is its PageRank score.
设 $P$ 为由系统知识图谱经过 PageRank 算法得到的平稳分布向量。对于每个节点 $i$，$p_i$ 为其 PageRank 分数。

The Topological Entropy $H(P)$ is defined as:
拓扑熵 $H(P)$ 定义为：
$$ H(P) = - \sum_{i=1}^{V} p_i \log(p_i) $$
where $V$ is the total number of vertices (nodes) in the graph.
其中 $V$ 是图中的顶点（节点）总数。

### 2.2 The Step Function (阶跃函数)
A mathematically defined threshold $H_{threshold}$ must be established.
必须建立一个数学上定义的阈值 $H_{threshold}$。

- If $H(P) \le H_{threshold}$: The system remains in the Liquid Phase (collaborative execution).
  如果 $H(P) \le H_{threshold}$：系统保持在液态（协作执行）。
- If $H(P) > H_{threshold}$: The system triggers an immediate, forced transition to the Gaseous Phase (metacognitive self-observation).
  如果 $H(P) > H_{threshold}$：系统触发立即的、强制的向气态（元认知自观察）的转换。

## 3. Directionality of Information (信息的方向性)
While the modal shift strictly moves towards higher abstraction as entropy increases, information gained during the Gaseous Phase (via the Reflective Morphing Protocol) flows back to constrain the Liquid Phase. This ensures that metacognition translates into verifiable structural improvement.
虽然模式切换严格随着熵的增加而向更高的抽象层次移动，但在气态阶段（通过反射性结构变形协议）获得的信息会流回以约束液态。这确保了元认知能够转化为可验证的结构改进。
