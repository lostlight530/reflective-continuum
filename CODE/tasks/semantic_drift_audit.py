"""Version-scoped drift audit; writes only when an output path is explicitly supplied."""
from __future__ import annotations
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from CODE.continuum_db import GraphDB
from CODE.drift_detector import compute_semantic_delta, compute_structural_delta


def run_audit(db_path: str, queries: list[str], v1: int, v2: int) -> dict:
    if not queries or any(not query.strip() for query in queries):
        raise ValueError("at least one non-empty query is required")
    with GraphDB(db_path) as db:
        structural = compute_structural_delta(db.conn, v1, v2)
        semantic = [{"query": query, "top_result_changed": compute_semantic_delta(db.conn, query, v1, v2)} for query in queries]
    return {"observed_at": datetime.now(timezone.utc).isoformat(timespec="microseconds"), "database": str(db_path), "versions": [v1, v2], "structural": structural, "semantic": semantic, "limitations": ["FTS5 lexical ranking", "caller-selected queries"]}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("database")
    parser.add_argument("query", nargs="+")
    parser.add_argument("--from-version", type=int, default=1)
    parser.add_argument("--to-version", type=int, default=2)
    parser.add_argument("--output")
    args = parser.parse_args()
    report = run_audit(args.database, args.query, args.from_version, args.to_version)
    text = json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True)
    if args.output:
        Path(args.output).write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 1 if any(item["top_result_changed"] for item in report["semantic"]) else 0


if __name__ == "__main__":
    raise SystemExit(main())