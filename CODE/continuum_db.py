import sqlite3
import typing

class GraphDB:
    """
    Deterministic Knowledge Graph storage and semantic engine.
    Uses SQLite with FTS5 for zero-dependency Semantic Delta calculations.
    """

    def __init__(self, db_path: str = ":memory:"):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self._initialize_schema()

    def _initialize_schema(self):
        """Initializes the exact schema required for structural and semantic storage."""
        cursor = self.conn.cursor()

        # Structural Nodes
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS nodes (
                node_id TEXT,
                version INTEGER DEFAULT 1,
                content TEXT NOT NULL,
                PRIMARY KEY (node_id, version)
            )
        ''')

        # Structural Edges (Directed)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS edges (
                source_id TEXT,
                target_id TEXT,
                relationship TEXT,
                version INTEGER DEFAULT 1,
                PRIMARY KEY (source_id, target_id, relationship),
                FOREIGN KEY (source_id) REFERENCES nodes(node_id) ON DELETE CASCADE,
                FOREIGN KEY (target_id) REFERENCES nodes(node_id) ON DELETE CASCADE
            )
        ''')

        # FTS5 External Content Table for Semantic Drift detection
        cursor.execute('''
            CREATE VIRTUAL TABLE IF NOT EXISTS semantic_idx USING fts5(
                content,
                content='nodes',
                content_rowid='rowid'
            )
        ''')

        # Triggers to keep FTS5 synchronized deterministically
        cursor.executescript('''
            CREATE TRIGGER IF NOT EXISTS nodes_ai AFTER INSERT ON nodes BEGIN
                INSERT INTO semantic_idx(rowid, content) VALUES (new.rowid, new.content);
            END;
            CREATE TRIGGER IF NOT EXISTS nodes_ad AFTER DELETE ON nodes BEGIN
                INSERT INTO semantic_idx(semantic_idx, rowid, content) VALUES('delete', old.rowid, old.content);
            END;
            CREATE TRIGGER IF NOT EXISTS nodes_au AFTER UPDATE ON nodes BEGIN
                INSERT INTO semantic_idx(semantic_idx, rowid, content) VALUES('delete', old.rowid, old.content);
                INSERT INTO semantic_idx(rowid, content) VALUES (new.rowid, new.content);
            END;
        ''')
        self.conn.commit()

    def insert_node(self, node_id: str, content: str, version: int = 1, commit: bool = True):
        """Inserts a node. Trigger automatically updates FTS5."""
        self.conn.execute("INSERT OR REPLACE INTO nodes (node_id, content, version) VALUES (?, ?, ?)",
                          (node_id, content, version))
        if commit:
            self.conn.commit()

    def insert_edge(self, source: str, target: str, relationship: str, version: int = 1, commit: bool = True):
        """Inserts a directed edge."""
        self.conn.execute("INSERT OR REPLACE INTO edges (source_id, target_id, relationship, version) VALUES (?, ?, ?, ?)",
                          (source, target, relationship, version))
        if commit:
            self.conn.commit()

    def fork(self, name: str):
        """Creates a named savepoint for transactional isolation (ADR-004)."""
        self.conn.execute(f"SAVEPOINT {name}")

    def commit_fork(self, name: str):
        """Releases the named savepoint, committing changes."""
        self.conn.execute(f"RELEASE SAVEPOINT {name}")

    def rollback_fork(self, name: str):
        """Rolls back to the named savepoint."""
        self.conn.execute(f"ROLLBACK TO SAVEPOINT {name}")

    def get_all_nodes(self, version: int = 1):
        cursor = self.conn.cursor()
        cursor.execute("SELECT node_id FROM nodes WHERE version = ?", (version,))
        return [row['node_id'] for row in cursor.fetchall()]

    def get_all_edges(self, version: int = 1):
        cursor = self.conn.cursor()
        cursor.execute("SELECT source_id, target_id FROM edges WHERE version = ?", (version,))
        return [tuple(row) for row in cursor.fetchall()]

    def semantic_search(self, query: str) -> typing.List[dict]:
        """Performs a deterministic FTS5 search."""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT nodes.node_id, nodes.content
            FROM semantic_idx
            JOIN nodes ON nodes.rowid = semantic_idx.rowid
            WHERE semantic_idx MATCH ?
            ORDER BY rank
        """, (query,))
        return [dict(row) for row in cursor.fetchall()]

    def close(self):
        self.conn.close()
