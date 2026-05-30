import sys
import datetime
import os
import re
from CODE.continuum_db import GraphDB
from CODE.drift_detector import compute_semantic_delta, compute_structural_delta

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
        self.db.insert_node("Axiom_Metacognition", "Metacognition is self-observation.", version=1)

        self.db.insert_node("Axiom_Deterministic", "Determinism is the foundation of cognitive safety.", version=2)
        self.db.insert_node("Axiom_Safety", "Safety is achieved via hard rollback and zero entropy.", version=2)
        self.db.insert_node("Axiom_Metacognition", "Metacognition is the gaseous phase of deterministic logic.", version=2)

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

        delta = compute_structural_delta(self.db.conn, 1, 2)
        added_nodes = delta["added"]

        liquid_count = 0
        gaseous_count = 0
        rejected_inputs = []

        if os.path.exists("ingestion.log"):
            with open("ingestion.log", "r", encoding="utf-8") as log_file:
                for line in log_file:
                    if "Phase: LIQUID" in line:
                        liquid_count += 1
                    elif "Transitioning to GASEOUS PHASE" in line:
                        gaseous_count += 1
                    elif "Cognitive rejection occurred. Cortical rollback triggered." in line or "Rejecting input" in line or "rejected by Cortex constraints" in line:
                        match = re.search(r"input\s+(\S+)", line)
                        if match:
                            rejected_inputs.append(match.group(1))
                        else:
                            match2 = re.search(r"Signal\s+(\S+)", line)
                            if match2:
                                rejected_inputs.append(match2.group(1))
                            else:
                                rejected_inputs.append("Unknown_Input")

        ratio = f"{liquid_count}:{gaseous_count}" if gaseous_count > 0 else f"{liquid_count}:0"

        # Evaluate Phase Boundaries by scanning entropy logs (all dehydrated reports in RESEARCH/daily/ and *.log)
        entropy_alerts = 0
        total_entropy_logs = 0
        for root, _, files in os.walk("."):
            for file in files:
                if file.endswith(".md") or file.endswith(".log"):
                    filepath = os.path.join(root, file)
                    try:
                        with open(filepath, "r", encoding="utf-8") as ef:
                            for line in ef:
                                if "Phase Boundary Detected (H >" in line or "entropy thresholds being exceeded (H >" in line:
                                    entropy_alerts += 1
                    except Exception:
                        pass

        boundary_eval = "拓扑熵过高导致气态反思时间过长" if entropy_alerts > 5 else "未因拓扑熵过高导致异常停留"

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
            status = "检测到漂移" if res["drifted"] else "相界稳定"
            content.append(f"| {res['query']} | {status} | {res['timestamp']} |")

        content.append("\n## 3. Drift Analysis (漂移分析)")
        content.append(f"- **Drifted Added Nodes / 导致漂移的新增节点**: {', '.join(added_nodes) if added_nodes else 'None'}")
        content.append(f"- **Rejected Inputs (Hard Rollback) / 触发硬回滚拒绝的输入**: {', '.join(rejected_inputs) if rejected_inputs else 'None'}")
        content.append(f"- **Liquid to Gas Phase Transition Ratio / 液态至气态相变比例**: {ratio}")
        content.append(f"- **Phase Boundary Evaluation / 相界边界评估**: {boundary_eval}")

        content.append("\n## 4. Conclusion (结论)")
        any_drift = any(r["drifted"] for r in results)
        if any_drift:
            content.append("System requires GASEOUS recalibration due to semantic drift. | 由于语义漂移，系统需要进行气态重新校准。")
        else:
            content.append("Semantic stability maintained. System remains in LIQUID phase. | 保持语义稳定。系统保持在液态。")

        with open(report_path, "w", encoding="utf-8") as f:
            f.write("\n".join(content))
        print(f"[SemanticDriftAudit] Report generated: {report_path}")

if __name__ == "__main__":
    audit = SemanticDriftAudit()
    r1 = audit.run_audit("determinism")
    r2 = audit.run_audit("safety")
    r3 = audit.run_audit("metacognition")
    audit.generate_report([r1, r2, r3])
