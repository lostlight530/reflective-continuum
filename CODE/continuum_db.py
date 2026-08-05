"""Versioned SQLite graph storage with enforced foreign keys and synchronized FTS5."""
from __future__ import annotations
import contextlib
import hashlib
import json
import re
import sqlite3
from pathlib import Path
from typing import Iterator

_SAVEPOINT = re.compile(r"^[A-Za-z_][A-Za-z0-9_]{0,63}$")


class GraphDB:
    def __init__(self, db_path: str | Path = ":memory:") -> None:
        path_text = str(db_path)
        self.conn = sqlite3.connect(path_text, uri=path_text.startswith("file:"))
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA foreign_keys = ON")
        if self.conn.execute("PRAGMA foreign_keys").fetchone()[0] != 1:
            self.conn.close()
            raise RuntimeError("SQLite foreign-key enforcement is unavailable")
        self._initialize_schema()

    def _initialize_schema(self) -> None:
        self.conn.executescript("""
        CREATE TABLE IF NOT EXISTS nodes (
            node_id TEXT NOT NULL CHECK(length(node_id) BETWEEN 1 AND 200),
            version INTEGER NOT NULL CHECK(version >= 1),
            content TEXT NOT NULL CHECK(length(content) > 0),
            PRIMARY KEY (node_id, version)
        );
        CREATE TABLE IF NOT EXISTS edges (
            source_id TEXT NOT NULL,
            target_id TEXT NOT NULL,
            relationship TEXT NOT NULL CHECK(length(relationship) BETWEEN 1 AND 100),
            version INTEGER NOT NULL CHECK(version >= 1),
            PRIMARY KEY (source_id, target_id, relationship, version),
            FOREIGN KEY (source_id, version) REFERENCES nodes(node_id, version) ON DELETE CASCADE,
            FOREIGN KEY (target_id, version) REFERENCES nodes(node_id, version) ON DELETE CASCADE
        );
        CREATE VIRTUAL TABLE IF NOT EXISTS semantic_idx USING fts5(
            content, content='nodes', content_rowid='rowid'
        );
        CREATE TRIGGER IF NOT EXISTS nodes_ai AFTER INSERT ON nodes BEGIN
            INSERT INTO semantic_idx(rowid, content) VALUES (new.rowid, new.content);
        END;
        CREATE TRIGGER IF NOT EXISTS nodes_ad AFTER DELETE ON nodes BEGIN
            INSERT INTO semantic_idx(semantic_idx, rowid, content) VALUES('delete', old.rowid, old.content);
        END;
        CREATE TRIGGER IF NOT EXISTS nodes_au AFTER UPDATE OF content ON nodes BEGIN
            INSERT INTO semantic_idx(semantic_idx, rowid, content) VALUES('delete', old.rowid, old.content);
            INSERT INTO semantic_idx(rowid, content) VALUES (new.rowid, new.content);
        END;
        """)
        self.conn.commit()

    @staticmethod
    def _identifier(value: str) -> str:
        if not isinstance(value, str) or not _SAVEPOINT.fullmatch(value):
            raise ValueError("savepoint name must match [A-Za-z_][A-Za-z0-9_]{0,63}")
        return '"' + value + '"'

    def insert_node(self, node_id: str, content: str, version: int = 1, *, commit: bool = True) -> None:
        if not isinstance(node_id, str) or not node_id or len(node_id) > 200:
            raise ValueError("node_id must contain 1..200 characters")
        if not isinstance(content, str) or not content:
            raise ValueError("content must be a non-empty string")
        if isinstance(version, bool) or not isinstance(version, int) or version < 1:
            raise ValueError("version must be a positive integer")
        self.conn.execute("""INSERT INTO nodes(node_id, version, content) VALUES (?, ?, ?)
            ON CONFLICT(node_id, version) DO UPDATE SET content=excluded.content""", (node_id, version, content))
        if commit:
            self.conn.commit()

    def insert_edge(self, source: str, target: str, relationship: str, version: int = 1, *, commit: bool = True) -> None:
        if not all(isinstance(item, str) and item for item in (source, target, relationship)):
            raise ValueError("edge values must be non-empty strings")
        if isinstance(version, bool) or not isinstance(version, int) or version < 1:
            raise ValueError("version must be a positive integer")
        self.conn.execute("""INSERT INTO edges(source_id, target_id, relationship, version) VALUES (?, ?, ?, ?)
            ON CONFLICT(source_id, target_id, relationship, version) DO NOTHING""", (source, target, relationship, version))
        if commit:
            self.conn.commit()

    def fork(self, name: str) -> None:
        self.conn.execute(f"SAVEPOINT {self._identifier(name)}")

    def commit_fork(self, name: str) -> None:
        self.conn.execute(f"RELEASE SAVEPOINT {self._identifier(name)}")

    def rollback_fork(self, name: str) -> None:
        quoted = self._identifier(name)
        self.conn.execute(f"ROLLBACK TO SAVEPOINT {quoted}")
        self.conn.execute(f"RELEASE SAVEPOINT {quoted}")

    @contextlib.contextmanager
    def savepoint(self, name: str) -> Iterator[None]:
        self.fork(name)
        try:
            yield
        except BaseException:
            self.rollback_fork(name)
            raise
        else:
            self.commit_fork(name)

    def get_all_nodes(self, version: int = 1) -> list[str]:
        return [row[0] for row in self.conn.execute("SELECT node_id FROM nodes WHERE version=? ORDER BY node_id", (version,))]

    def get_all_edges(self, version: int = 1) -> list[tuple[str, str]]:
        return [tuple(row) for row in self.conn.execute("SELECT source_id,target_id FROM edges WHERE version=? ORDER BY source_id,target_id,relationship", (version,))]

    def semantic_search(self, query: str, *, version: int | None = None, limit: int = 20) -> list[dict]:
        if not isinstance(query, str) or not query.strip():
            raise ValueError("query must be non-empty")
        if not 1 <= limit <= 100:
            raise ValueError("limit must be between 1 and 100")
        phrase = '"' + query.strip().replace('"', '""') + '"'
        sql = """SELECT n.node_id,n.version,n.content,bm25(semantic_idx) AS score FROM semantic_idx
                 JOIN nodes n ON n.rowid=semantic_idx.rowid WHERE semantic_idx MATCH ?"""
        params: list[object] = [phrase]
        if version is not None:
            sql += " AND n.version=?"
            params.append(version)
        sql += " ORDER BY score,n.node_id,n.version LIMIT ?"
        params.append(limit)
        return [dict(row) for row in self.conn.execute(sql, params)]

    def snapshot_digest(self, version: int = 1) -> str:
        nodes = [tuple(row) for row in self.conn.execute("SELECT node_id,content FROM nodes WHERE version=? ORDER BY node_id", (version,))]
        edges = [tuple(row) for row in self.conn.execute("SELECT source_id,target_id,relationship FROM edges WHERE version=? ORDER BY source_id,target_id,relationship", (version,))]
        payload = json.dumps({"nodes": nodes, "edges": edges}, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()

    def close(self) -> None:
        self.conn.close()

    def __enter__(self) -> "GraphDB":
        return self

    def __exit__(self, *args: object) -> None:
        self.close()
