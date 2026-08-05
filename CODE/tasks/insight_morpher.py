"""Validated ingestion of caller-provided JSON signals."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from typing import Any
from CODE.continuum_db import GraphDB
from CODE.cortex_observer import CortexObserver
from CODE.reflective_validator import RuleEngine


class InsightMorpher:
    def __init__(self, db_path: str = ":memory:") -> None:
        self.db = GraphDB(db_path)
        self.cortex = CortexObserver(self.db, RuleEngine())

    @staticmethod
    def _signal(value: Any) -> tuple[str, str, list[tuple[str, str, str]], int]:
        if not isinstance(value, dict) or set(value) - {"id", "content", "edges", "version"}:
            raise ValueError("signal must contain only id, content, edges, and optional version")
        node_id, content = value.get("id"), value.get("content")
        edges = value.get("edges", [])
        version = value.get("version", 1)
        if not isinstance(node_id, str) or not isinstance(content, str) or not isinstance(edges, list):
            raise TypeError("invalid signal field type")
        parsed = []
        for edge in edges:
            if not isinstance(edge, list) or len(edge) != 3 or not all(isinstance(part, str) and part for part in edge):
                raise ValueError("each edge must be a three-string JSON array")
            parsed.append(tuple(edge))
        return node_id, content, parsed, version

    def morph_signals(self, raw_signals: list[Any]) -> dict:
        if not isinstance(raw_signals, list) or not raw_signals:
            raise ValueError("signals must be a non-empty list")
        results = []
        for raw in raw_signals:
            node_id, content, edges, version = self._signal(raw)
            result = self.cortex.process_input(node_id, content, edges, version)
            results.append({"id": node_id, "accepted": result.accepted, "reasons": list(result.reasons)})
        return {"total": len(results), "accepted": sum(item["accepted"] for item in results), "results": results}

    def morph_from_file(self, file_path: str | Path) -> dict:
        with Path(file_path).open("r", encoding="utf-8") as handle:
            return self.morph_signals(json.load(handle))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("signals")
    args = parser.parse_args()
    morpher = InsightMorpher()
    result = morpher.morph_from_file(args.signals)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0 if result["accepted"] == result["total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())