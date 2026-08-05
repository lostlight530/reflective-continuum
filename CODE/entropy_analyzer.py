"""Validated PageRank and Shannon entropy utilities."""
from __future__ import annotations
import math
from collections.abc import Iterable


def compute_pagerank(nodes: list[str], edges: list[tuple[str, str]], damping: float = 0.85, max_iterations: int = 100, tol: float = 1e-9) -> dict[str, float]:
    ordered = tuple(sorted(set(nodes)))
    if len(ordered) != len(nodes):
        raise ValueError("nodes must be unique")
    if not 0 < damping < 1 or max_iterations < 1 or tol <= 0:
        raise ValueError("invalid PageRank configuration")
    if not ordered:
        return {}
    known = set(ordered)
    clean_edges = sorted(set(edges))
    if any(source not in known or target not in known for source, target in clean_edges):
        raise ValueError("edge references an unknown node")
    count = len(ordered)
    rank = {node: 1.0 / count for node in ordered}
    outgoing = {node: 0 for node in ordered}
    incoming = {node: [] for node in ordered}
    for source, target in clean_edges:
        outgoing[source] += 1
        incoming[target].append(source)
    for _ in range(max_iterations):
        dangling = math.fsum(rank[node] for node in ordered if outgoing[node] == 0)
        updated = {}
        for node in ordered:
            contribution = math.fsum(rank[source] / outgoing[source] for source in incoming[node])
            updated[node] = (1 - damping) / count + damping * (dangling / count + contribution)
        delta = math.fsum(abs(updated[node] - rank[node]) for node in ordered)
        rank = updated
        if delta <= tol:
            break
    total = math.fsum(rank.values())
    return {node: rank[node] / total for node in ordered}


def calculate_topological_entropy(scores: Iterable[float]) -> float:
    values = [float(value) for value in scores]
    if any(not math.isfinite(value) or value < 0 for value in values):
        raise ValueError("scores must be finite and non-negative")
    total = math.fsum(values)
    if total <= 0:
        return 0.0
    return -math.fsum((value / total) * math.log(value / total) for value in values if value > 0)


def check_phase_boundary(pagerank: dict[str, float], threshold: float) -> bool:
    if not math.isfinite(threshold) or threshold < 0:
        raise ValueError("threshold must be finite and non-negative")
    return calculate_topological_entropy(pagerank.values()) > threshold