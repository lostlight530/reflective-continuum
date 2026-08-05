"""Version-scoped structural, search-result, and rank deltas."""
from __future__ import annotations
import math
import sqlite3
from typing import Any


def compute_structural_delta(conn: sqlite3.Connection, v1: int, v2: int) -> dict[str, list[str]]:
    removed = sorted(row[0] for row in conn.execute("SELECT node_id FROM nodes WHERE version=? EXCEPT SELECT node_id FROM nodes WHERE version=?", (v1, v2)))
    added = sorted(row[0] for row in conn.execute("SELECT node_id FROM nodes WHERE version=? EXCEPT SELECT node_id FROM nodes WHERE version=?", (v2, v1)))
    modified = sorted(row[0] for row in conn.execute("""SELECT a.node_id FROM nodes a JOIN nodes b ON a.node_id=b.node_id
        WHERE a.version=? AND b.version=? AND a.content<>b.content""", (v1, v2)))
    return {"added": added, "removed": removed, "modified": modified}


def compute_semantic_delta(conn: sqlite3.Connection, query: str, v1: int, v2: int) -> bool:
    if not isinstance(query, str) or not query.strip():
        raise ValueError("query must be non-empty")
    phrase = '"' + query.strip().replace('"', '""') + '"'
    def top(version: int) -> str | None:
        row = conn.execute("""SELECT n.node_id FROM semantic_idx JOIN nodes n ON n.rowid=semantic_idx.rowid
            WHERE semantic_idx MATCH ? AND n.version=? ORDER BY bm25(semantic_idx),n.node_id LIMIT 1""", (phrase, version)).fetchone()
        return row[0] if row else None
    return top(v1) != top(v2)


def compute_rank_delta(pr1: dict[str, float], pr2: dict[str, float], threshold: float) -> list[str]:
    if not math.isfinite(threshold) or threshold < 0:
        raise ValueError("threshold must be finite and non-negative")
    return sorted(node for node in set(pr1) | set(pr2) if abs(pr1.get(node, 0.0) - pr2.get(node, 0.0)) > threshold)


def verify_self_consistency(delta: dict[str, Any], rule_engine: Any) -> bool:
    return bool(rule_engine.verify_consistency(delta))