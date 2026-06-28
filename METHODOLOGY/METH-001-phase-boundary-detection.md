# Phase Boundary Detection | 相界检测

## Introduction (简介)
**English:**
This document outlines the mathematical framework governing how the Reflective Continuum transitions between states of execution and self-observation. It provides the formal basis for ADR-005.

**Chinese (中文):**
本文档概述了管理反射连续体如何在执行状态和自我观察状态之间转换的数学框架。它为 ADR-005 提供了正式基础。

## 2. Topological Entropy (拓扑熵)
**English:**
The phase boundary is strictly defined by the system's topological complexity. We measure this complexity without relying on heuristic triggers or learned metadata.

**Chinese (中文):**
相界由系统的拓扑复杂性严格定义。我们在不依赖启发式触发器或学习元数据的情况下测量此复杂性。

### 2.1 Calculation (计算)
**English:**
Let $P$ be the stationary distribution vector of the system's knowledge graph resulting from the PageRank algorithm. For each node $i$, $p_i$ is its PageRank score.

The Topological Entropy $H(P)$ is defined as:
$$ H(P) = - \sum_{i=1}^{V} p_i \log(p_i) $$
where $V$ is the total number of vertices (nodes) in the graph. This value represents the "structural uncertainty" or "diffusion" of authority within the graph. High entropy indicates that knowledge is broadly distributed and complexly interconnected, necessitating a metacognitive shift.

**Chinese (中文):**
设 $P$ 为由系统知识图谱经过 PageRank 算法得到的平稳分布向量。对于每个节点 $i$, $p_i$ 为其 PageRank 分数。

拓扑熵 $H(P)$ 定义为：
$$ H(P) = - \sum_{i=1}^{V} p_i \log(p_i) $$
其中 $V$ 是图中的顶点（节点）总数。该值代表图中权威的“结构不确定性”或“弥散性”。高熵表示知识广泛分布且复杂互联，因此需要进行元认知转换。

### 2.2 The Step Function (阶跃函数)
**English:**
A mathematically defined threshold $H_{threshold}$ is established. The system state follows a strict step-function:
- If $H(P) \le H_{threshold}$: The system remains in the **Liquid Phase** (collaborative execution).
- If $H(P) > H_{threshold}$: The system triggers an immediate, forced transition to the **Gaseous Phase** (metacognitive self-observation).

**Chinese (中文):**
建立一个数学上定义的阈值 $H_{threshold}$。系统状态遵循严格的阶跃函数：
- 如果 $H(P) \le H_{threshold}$：系统保持在**液态**（协作执行）。
- 如果 $H(P) > H_{threshold}$：系统触发立即的、强制的向**气态**（元认知自观察）的转换。

## 3. Physical Analogy (物理类比)
**English:**
Think of the system as a thermodynamic body. As "heat" (complexity/data) is added, the information density increases until the structure can no longer be managed by simple execution. At the boiling point ($H_{threshold}$), it vaporizes into a gaseous state where every "molecule" (node) can be observed in relation to the whole.

**Chinese (中文):**
将系统想象为一个热力学实体。随着“热量”（复杂性/数据）的增加，信息密度增加，直到结构不再能通过简单的执行来管理。在沸点（$H_{threshold}$）时，它汽化为气态，在这种状态下，每个“分子”（节点）都可以相对于整体被观察。

## 5. Temporal Durations (时间持续度)
**English:**
The temporal duration spent in the Gaseous (reflective) state must be strictly monitored via the `Gas duration=[hours]` metric. Extended gas phases trigger the cognitive divergence alert if entropy fails to reach zero across sequential cycles.

**Chinese (中文):**
在气态（反射）状态下度过的时间必须通过 `Gas duration=[hours]` 指标进行严格监控。如果熵在连续周期中无法降至零，延长的气态阶段将触发“认知发散警报”（cognitive divergence alert）。
