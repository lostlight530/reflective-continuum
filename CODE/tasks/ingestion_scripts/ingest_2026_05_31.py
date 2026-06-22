import sys
from CODE.tasks.insight_morpher import InsightMorpher

signals = [
    {
        "id": "SIG_2026_0531_001",
        "content": "Leading AI research organizations assert that deterministic verification structures guarantee zero structural drift, overriding pure probabilistic alignment methods.",
        "edges": []
    },
    {
        "id": "SIG_2026_0531_002",
        "content": "Metacognitive architectures leveraging strict state isolation are empirically demonstrating immunity to deep reflective hallucinations.",
        "edges": [("SIG_2026_0531_002", "SIG_2026_0531_001", "validates_determinism")]
    },
    {
        "id": "SIG_2026_0531_003",
        "content": "The transition toward zero-entropy constraints signals a paradigm shift: autonomous behavior must be mathematically bound, not merely reward-optimized.",
        "edges": [("SIG_2026_0531_003", "SIG_2026_0531_002", "structural_implication")]
    }
]

morpher = InsightMorpher()
success = morpher.morph_signals(signals)

if success:
    print("\n[SUCCESS] All signals successfully ingested into the continuum deterministically.")
    sys.exit(0)
else:
    print("\n[FAILURE] Cognitive rejection occurred. Cortical rollback triggered. Terminating.")
    sys.exit(1)
