import sqlite3
import typing

def compute_structural_delta(conn: sqlite3.Connection, v1: int, v2: int) -> typing.Dict[str, typing.List[str]]:
    """
    Computes exact Structural Delta using SQL difference across two version snapshots.
    Determines nodes added, removed, or content-modified between v1 and v2.
    """
    cursor = conn.cursor()

    # Nodes in V1 but not in V2 (Removed)
    cursor.execute("""
        SELECT node_id FROM nodes WHERE version = ?
        EXCEPT
        SELECT node_id FROM nodes WHERE version = ?
    """, (v1, v2))
    removed = [row['node_id'] for row in cursor.fetchall()]

    # Nodes in V2 but not in V1 (Added)
    cursor.execute("""
        SELECT node_id FROM nodes WHERE version = ?
        EXCEPT
        SELECT node_id FROM nodes WHERE version = ?
    """, (v2, v1))
    added = [row['node_id'] for row in cursor.fetchall()]

    # Nodes in both but modified content
    cursor.execute("""
        SELECT n1.node_id
        FROM nodes n1
        JOIN nodes n2 ON n1.node_id = n2.node_id
        WHERE n1.version = ? AND n2.version = ? AND n1.content != n2.content
    """, (v1, v2))
    modified = [row['node_id'] for row in cursor.fetchall()]

    return {
        "added": added,
        "removed": removed,
        "modified": modified
    }

def compute_semantic_delta(conn: sqlite3.Connection, query: str, v1: int, v2: int) -> bool:
    """
    Evaluates Semantic Delta via FTS5 result set drift (ADR-003).
    Returns True if the top result changed between versions for the exact same query.
    """
    cursor = conn.cursor()

    def get_top_result(version: int):
        cursor.execute("""
            SELECT n.node_id
            FROM semantic_idx s
            JOIN nodes n ON s.rowid = n.rowid
            WHERE s.semantic_idx MATCH ? AND n.version = ?
            ORDER BY s.rank LIMIT 1
        """, (query, version))
        res = cursor.fetchone()
        return res['node_id'] if res else None

    top_v1 = get_top_result(v1)
    top_v2 = get_top_result(v2)

    return top_v1 != top_v2

def compute_rank_delta(pr1: typing.Dict[str, float], pr2: typing.Dict[str, float], threshold: float) -> typing.List[str]:
    """
    Identifies nodes with significant PageRank shift between two states (ADR-003).
    """
    significant_shifts = []
    all_nodes = set(pr1.keys()).union(set(pr2.keys()))

    for node in all_nodes:
        score1 = pr1.get(node, 0.0)
        score2 = pr2.get(node, 0.0)
        if abs(score1 - score2) > threshold:
            significant_shifts.append(node)

    return significant_shifts

def verify_self_consistency(delta: dict, rule_engine: typing.Any) -> bool:
    """
    Verifies state mutations against internal architectural decision records (ADR-004).
    Returns True if valid (deterministic Boolean output), False if contradiction found.
    """
    return rule_engine.verify_consistency(delta)
