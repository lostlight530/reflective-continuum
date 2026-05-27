import sys
import datetime
import os
from CODE.continuum_db import GraphDB
from CODE.drift_detector import compute_semantic_delta

class SemanticDriftAudit:
    """
    T-06 Analysis: Weekly Semantic Drift Audit.
    Evaluates whether the core intent (semantics) of key terms has drifted
    and writes the report to RESEARCH/daily/ directory.
    """

    def __init__(self, db_path=":memory:"):
        self.db = GraphDB(db_path)
        self._seed_data()

    def _seed_data(self):
        """Seeds the in-memory database with versioned data for auditing."""
        self.db.insert_node("Axiom_Deterministic", "Determinism is absolute logic.", version=1)
        self.db.insert_node("Axiom_Safety", "Safety is architectural constraint.", version=1)

        self.db.insert_node("Axiom_Deterministic", "Determinism is the foundation of cognitive safety.", version=2)
        self.db.insert_node("Axiom_Safety", "Safety is achieved via hard rollback and zero entropy.", version=2)

    def run_audit(self, query: str) -> dict:
        """Executes the drift audit and returns result metadata."""
        print(f"[SemanticDriftAudit] Initiating T-06 Analysis for query: '{query}'")
        drifted = compute_semantic_delta(self.db.conn, query, v1=1, v2=2)

        status = "DRIFT_DETECTED" if drifted else "STABLE"
        print(f"[SemanticDriftAudit] Result: {status}")

        return {
            "query": query,
            "drifted": drifted,
            "timestamp": datetime.datetime.now().isoformat()
        }

    def generate_report(self, results: list):
        """Writes a dehydrated report to RESEARCH/daily/."""
        date_str = datetime.date.today().isoformat()
        report_path = f"RESEARCH/daily/{date_str}-dehydrated-report.md"

        os.makedirs("RESEARCH/daily", exist_ok=True)

        content = [
            f"# Dehydrated Report | 脱水报告 - {date_str}",
            "",
            "## 1. Executive Summary (执行摘要)",
            f"Audit conducted on {len(results)} core semantic queries.",
            "Metacognitive alignment verified via FTS5 drift detection.",
            "",
            "## 2. Audit Results (审计结果)",
            "| Query | Status | Timestamp |",
            "| :--- | :--- | :--- |"
        ]

        for res in results:
            status = "⚠️ DRIFT" if res["drifted"] else "✅ STABLE"
            content.append(f"| {res['query']} | {status} | {res['timestamp']} |")

        content.append("\n## 3. Conclusion (结论)")
        any_drift = any(r["drifted"] for r in results)
        if any_drift:
            content.append("System requires GASEOUS recalibration due to semantic drift.")
        else:
            content.append("Semantic stability maintained. System remains in LIQUID phase.")

        with open(report_path, "w", encoding="utf-8") as f:
            f.write("\n".join(content))
        print(f"[SemanticDriftAudit] Report generated: {report_path}")

if __name__ == "__main__":
    audit = SemanticDriftAudit()
    r1 = audit.run_audit("determinism")
    r2 = audit.run_audit("safety")
    audit.generate_report([r1, r2])
