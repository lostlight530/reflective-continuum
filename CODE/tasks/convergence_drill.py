"""Repeatability drill for a fixed local fixture; not a convergence proof."""
from __future__ import annotations
import argparse
import json
from CODE.continuum_db import GraphDB

FIXTURE = (("Node_A", "Deterministic fixture A", ()), ("Node_B", "Deterministic fixture B", (("Node_A", "Node_B", "depends_on"),)))


def run_drill(iterations: int = 100) -> dict:
    if not 1 <= iterations <= 1000:
        raise ValueError("iterations must be within 1..1000")
    digests = []
    for _ in range(iterations):
        with GraphDB() as db:
            for node_id, content, edges in FIXTURE:
                db.insert_node(node_id, content)
                for edge in edges:
                    db.insert_edge(*edge)
            digests.append(db.snapshot_digest())
    return {"iterations": iterations, "distinct_snapshots": len(set(digests)), "repeatable": len(set(digests)) == 1, "scope": "fixed local SQLite fixture"}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--iterations", type=int, default=100)
    result = run_drill(parser.parse_args().iterations)
    print(json.dumps(result, sort_keys=True))
    return 0 if result["repeatable"] else 1


if __name__ == "__main__":
    raise SystemExit(main())