import sys
from CODE.tasks.insight_morpher import InsightMorpher

# 构建 3 条涵盖元认知、确定性和 AI 对齐领域的核心信号
signals = [
    {
        "id": "SIG_2026_0522_001",
        "content": "Google DeepMind publishes new paper on deterministic metacognitive limits, arguing against purely probabilistic scaling models for true AGI.",
        "edges": []
    },
    {
        "id": "SIG_2026_0522_002",
        "content": "NVIDIA releases strict state-lock hardware modules aiming at zero-entropy reflection for AI alignment enforcement.",
        "edges": [("SIG_2026_0522_002", "SIG_2026_0522_001", "enables")]
    },
    {
        "id": "SIG_2026_0522_003",
        "content": "OpenAI research highlights edge-case failures in test-time compute scaling, pivoting focus toward reflective architectural rules over larger parameter counts.",
        "edges": [("SIG_2026_0522_003", "SIG_2026_0522_001", "validates"), ("SIG_2026_0522_003", "SIG_2026_0522_002", "aligns_with")]
    }
]

morpher = InsightMorpher()
success = morpher.morph_signals(signals)

if success:
    print("\n[SUCCESS] All signals ingested and synthesized into the Knowledge Graph deterministically.")
else:
    print("\n[WARNING] Some signals were rejected by Cortex Observer and underwent Hard Rollback.")
