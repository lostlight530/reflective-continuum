"""Transactional observation with explicit rejection and bounded reflection."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Callable

from .continuum_db import GraphDB
from .entropy_analyzer import calculate_topological_entropy, check_phase_boundary, compute_pagerank
from .reflective_validator import RuleEngine

Reflector = Callable[[int, GraphDB, int], None]


@dataclass(frozen=True, slots=True)
class ProcessResult:
    accepted: bool
    phase: str
    reflection_depth: int
    entropy_nats: float
    reasons: tuple[str, ...] = ()


class _RejectedInput(Exception):
    def __init__(self, result: ProcessResult) -> None:
        self.result = result


class CortexObserver:
    def __init__(self, db: GraphDB, rule_engine: RuleEngine, max_depth: int | None = None, entropy_threshold: float | None = None, *, reflector: Reflector | None = None) -> None:
        self.db = db
        self.rules = rule_engine
        self.max_depth = self.rules.config.max_reflection_depth if max_depth is None else max_depth
        self.entropy_threshold = self.rules.config.entropy_threshold if entropy_threshold is None else entropy_threshold
        if not isinstance(self.max_depth, int) or not 1 <= self.max_depth <= 100:
            raise ValueError("max_depth must be within 1..100")
        if not isinstance(self.entropy_threshold, (int, float)) or self.entropy_threshold < 0:
            raise ValueError("entropy_threshold must be non-negative")
        self.reflector = reflector
        self.current_depth = 0
        self.phase = "LIQUID"
        self._savepoint_counter = 0

    def _state(self, version: int) -> tuple[dict[str, float], float]:
        rank = compute_pagerank(self.db.get_all_nodes(version), self.db.get_all_edges(version))
        return rank, calculate_topological_entropy(rank.values())

    def _validate_snapshot(self, version: int) -> tuple[str, ...]:
        reasons: list[str] = []
        for row in self.db.conn.execute("SELECT node_id,content FROM nodes WHERE version=? ORDER BY node_id", (version,)):
            result = self.rules.validate({"node_id": row[0], "content": row[1]})
            reasons.extend(f"{row[0]}:{reason}" for reason in result.reasons)
        return tuple(reasons)

    def process_input(self, node_id: str, content: str, edges: list[tuple[str, str, str]], version: int = 1) -> ProcessResult:
        validation = self.rules.validate({"node_id": node_id, "content": content})
        if not validation.accepted:
            return ProcessResult(False, "LIQUID", 0, 0.0, validation.reasons)
        if not isinstance(edges, list) or any(not isinstance(edge, (tuple, list)) or len(edge) != 3 for edge in edges):
            raise TypeError("edges must be a list of (source, target, relationship)")
        self._savepoint_counter += 1
        savepoint = f"input_{self._savepoint_counter}"
        try:
            with self.db.savepoint(savepoint):
                self.db.insert_node(node_id, content, version, commit=False)
                for source, target, relationship in edges:
                    self.db.insert_edge(source, target, relationship, version, commit=False)
                reasons = self._validate_snapshot(version)
                if reasons:
                    raise _RejectedInput(ProcessResult(False, "LIQUID", 0, 0.0, reasons))
                rank, entropy = self._state(version)
                if not check_phase_boundary(rank, float(self.entropy_threshold)):
                    self.phase, self.current_depth = "LIQUID", 0
                    return ProcessResult(True, self.phase, 0, entropy)
                self.phase = "GASEOUS"
                for depth in range(1, self.max_depth + 1):
                    self.current_depth = depth
                    if self.reflector is not None:
                        self.reflector(depth, self.db, version)
                    reasons = self._validate_snapshot(version)
                    if reasons:
                        raise _RejectedInput(ProcessResult(False, "LIQUID", depth, entropy, reasons))
                    rank, entropy = self._state(version)
                    if not check_phase_boundary(rank, float(self.entropy_threshold)):
                        self.phase, self.current_depth = "LIQUID", 0
                        return ProcessResult(True, self.phase, depth, entropy)
                raise _RejectedInput(ProcessResult(False, "LIQUID", self.max_depth, entropy, ("reflection_depth_exhausted",)))
        except _RejectedInput as rejected:
            self.phase, self.current_depth = "LIQUID", 0
            return rejected.result