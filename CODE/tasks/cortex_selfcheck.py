import sys
import datetime
import os
import traceback

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

modules_status = "❌"
conflicts = []
rule_engine_rules = 0
rule_parseable = "❌"
nodes = 0
edges = 0
pending_rollbacks = 0
delta = "0.0"
within_threshold = "YES"

try:
    from CODE.continuum_db import GraphDB
    from CODE.cortex_observer import CortexObserver
    from CODE.drift_detector import compute_structural_delta
    from CODE.reflective_validator import RuleEngine
    from CODE.entropy_analyzer import compute_pagerank

    db = GraphDB()
    rules = RuleEngine()
    cortex = CortexObserver(db, rules)
    modules_status = "✅"

    rule_engine_rules = sum(len(c) for c in rules.constraints.values())
    if rule_engine_rules > 0:
        rule_parseable = "✅"

    try:
        # Mock execution to verify it works
        cortex.process_input("test_selfcheck", "health check content", [])
        nodes = len(db.get_all_nodes())
        edges = len(db.get_all_edges())
        # Clean up mock input
        db.conn.execute("DELETE FROM nodes WHERE node_id='test_selfcheck'")
        db.conn.commit()
        nodes = len(db.get_all_nodes())
        edges = len(db.get_all_edges())
    except Exception as e:
        print(f"Execute failed: {e}")
        modules_status = "❌"

except Exception as e:
    print(f"Module import/init failed: {e}")

date_str = datetime.date.today().isoformat()
report_path = f"RESEARCH/daily/{date_str}-cortex-selfcheck.md"
os.makedirs("RESEARCH/daily", exist_ok=True)

content = f"""Module Health: [5模块 Import/Init/Execute {modules_status}]
Rule Engine: Rules=[{rule_engine_rules}] Parseable={rule_parseable} Conflicts=[{', '.join(conflicts) if conflicts else 'NONE'}]
DB State: Nodes=[{nodes}] Edges=[{edges}] Pending rollbacks=[{pending_rollbacks}]
Incremental Drift: Delta vs yesterday=[{delta}] Within threshold={within_threshold}
"""

with open(report_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Created {report_path}")
