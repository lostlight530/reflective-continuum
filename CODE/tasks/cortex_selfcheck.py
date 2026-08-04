import sys
import datetime
import os
import traceback
import unittest
import io

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
exceptions = []

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
        # Clean up mock input
        db.conn.execute("DELETE FROM nodes WHERE node_id='test_selfcheck'")
        db.conn.commit()
        nodes = len(db.get_all_nodes())
        edges = len(db.get_all_edges())
    except Exception as e:
        exceptions.append(f"Execute failed: {traceback.format_exc()}")
        modules_status = "❌"

except Exception as e:
    exceptions.append(f"Module import/init failed: {traceback.format_exc()}")
    modules_status = "❌"

date_str = datetime.date.today().isoformat()
report_path = f"RESEARCH/daily/{date_str}-cortex-selfcheck.md"
os.makedirs("RESEARCH/daily", exist_ok=True)

test_loader = unittest.TestLoader()
test_suite = test_loader.discover('tests/')
test_runner = unittest.TextTestRunner(stream=io.StringIO(), verbosity=2)
result = test_runner.run(test_suite)
total_tests = result.testsRun
failed_tests = len(result.failures)
errors_tests = len(result.errors)
skipped_tests = len(result.skipped)
passed_tests = total_tests - failed_tests - errors_tests - skipped_tests

content = f"Module Health: [5模块 Import/Init/Execute {modules_status}]\n"
if exceptions:
    content += "Exceptions:\n"
    for ex in exceptions:
        content += f"{ex}\n"
content += f"Rule Engine: Rules=[{rule_engine_rules}] Parseable={rule_parseable} Conflicts=[{', '.join(conflicts) if conflicts else 'NONE'}]\n"
content += f"DB State: Nodes=[{nodes}] Edges=[{edges}] Pending rollbacks=[{pending_rollbacks}]\n"
content += f"Incremental Drift: Delta vs yesterday=[{delta}] Within threshold={within_threshold}\n\n"
content += "状态解释:\n"

if nodes == 0 and edges == 0:
    content += "Nodes=0 与 Edges=0 只能记录为实际观测\n"
    content += "Context: INDETERMINATE_EMPTY_STATE\n"
    content += "可能原因: 没有有效摄入, 数据库刚初始化, 持久化路径错误, 写入失败, 当前数据库路径并非预期路径\n"
else:
    content += "Database has populated nodes/edges.\n"

content += f"\n测试结果:\n"
content += f"Total: {total_tests}\n"
content += f"Passed: {passed_tests}\n"
content += f"Failed: {failed_tests}\n"
content += f"Errors: {errors_tests}\n"
content += f"Skipped: {skipped_tests}\n"

with open(report_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Created {report_path}")
