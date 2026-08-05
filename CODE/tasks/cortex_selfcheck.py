"""Observable health checks without fabricated metrics or test-suite recursion."""
from __future__ import annotations
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from CODE.continuum_db import GraphDB
from CODE.reflective_validator import RuleEngine


def selfcheck(db_path: str = ":memory:") -> dict:
    checks: dict[str, bool] = {}
    try:
        with GraphDB(db_path) as db:
            checks["foreign_keys"] = db.conn.execute("PRAGMA foreign_keys").fetchone()[0] == 1
            checks["fts5"] = db.conn.execute("SELECT count(*) FROM semantic_idx").fetchone()[0] >= 0
            checks["integrity"] = db.conn.execute("PRAGMA integrity_check").fetchone()[0] == "ok"
            checks["rule_engine"] = RuleEngine().validate({"node_id": "health", "content": "fixture"}).accepted
            counts = {"nodes": db.conn.execute("SELECT count(*) FROM nodes").fetchone()[0], "edges": db.conn.execute("SELECT count(*) FROM edges").fetchone()[0]}
    except Exception as exc:
        checks["initialization"] = False
        counts = {}
        error_type = type(exc).__name__
    else:
        checks["initialization"] = True
        error_type = None
    return {"observed_at": datetime.now(timezone.utc).isoformat(timespec="microseconds"), "database": str(db_path), "checks": checks, "counts": counts, "healthy": all(checks.values()), "error_type": error_type}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--database", default=":memory:")
    parser.add_argument("--output")
    args = parser.parse_args()
    result = selfcheck(args.database)
    text = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True)
    if args.output:
        Path(args.output).write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0 if result["healthy"] else 1


if __name__ == "__main__":
    raise SystemExit(main())