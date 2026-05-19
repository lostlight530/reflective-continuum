import math
import typing

def compute_pagerank(
    nodes: typing.List[str],
    edges: typing.List[typing.Tuple[str, str]],
    damping: float = 0.85,
    max_iterations: int = 100,
    tol: float = 1.0e-6
) -> typing.Dict[str, float]:
    """
    Pure Python, zero-dependency PageRank implementation.
    Operates on a graph defined by a list of nodes and directed edges (source, target).
    """
    N = len(nodes)
    if N == 0:
        return {}

    # Initialize dictionary
    pr = {node: 1.0 / N for node in nodes}

    # Precompute out-degree for each node
    out_degree = {node: 0 for node in nodes}
    in_edges = {node: [] for node in nodes}

    for u, v in edges:
        if u in out_degree and v in in_edges:
            out_degree[u] += 1
            in_edges[v].append(u)

    # Iterative calculation
    for _ in range(max_iterations):
        new_pr = {}
        diff = 0.0

        # Handle dangling nodes (nodes with 0 out-degree)
        dangling_sum = sum(pr[node] for node in nodes if out_degree[node] == 0)

        for node in nodes:
            # Base teleportation + dangling node distribution
            rank = (1.0 - damping) / N + damping * (dangling_sum / N)

            # Add contributions from incoming edges
            for incoming_node in in_edges[node]:
                rank += damping * (pr[incoming_node] / out_degree[incoming_node])

            new_pr[node] = rank
            diff += abs(new_pr[node] - pr[node])

        pr = new_pr

        if diff < tol:
            break

    return pr

def calculate_topological_entropy(pagerank_scores: typing.List[float]) -> float:
    """
    Calculates the Shannon Entropy based on PageRank distributions (ADR-005).
    H(P) = - sum(p * log(p))
    """
    entropy = 0.0
    for score in pagerank_scores:
        if score > 0:
            entropy -= score * math.log(score)
    return entropy

def check_phase_boundary(pagerank_dict: typing.Dict[str, float], threshold: float) -> bool:
    """
    Determines if the system must transition to the Gaseous Phase.
    Returns True if H(P) > threshold.
    """
    scores = list(pagerank_dict.values())
    entropy = calculate_topological_entropy(scores)
    return entropy > threshold
