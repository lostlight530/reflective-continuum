import math
import typing

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

def check_phase_boundary(pagerank_scores: typing.List[float], threshold: float) -> bool:
    """
    Determines if the system must transition to the Gaseous Phase.
    Returns True if H(P) > threshold.
    """
    entropy = calculate_topological_entropy(pagerank_scores)
    return entropy > threshold
