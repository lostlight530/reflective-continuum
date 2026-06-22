import sys
from CODE.tasks.insight_morpher import InsightMorpher

signals = [
    {
        "id": "SIG_2026_0525_001",
        "content": "The integration of deterministic AST constraints drastically reduces probabilistic hallucination in neural systems, enforcing zero-entropy boundaries.",
        "edges": []
    },
    {
        "id": "SIG_2026_0525_002",
        "content": "Probabilistic base models from pioneering labs exhibit architectural limitations in maintaining Zero-Entropy States during deep reflection without an external Observer layer.",
        "edges": [("SIG_2026_0525_002", "SIG_2026_0525_001", "validates")]
    },
    {
        "id": "SIG_2026_0525_003",
        "content": "Industrial metacognitive alignment frameworks are prioritizing absolute state validation over RLHF, enforcing rigid phase transitions through PageRank topology.",
        "edges": [("SIG_2026_0525_003", "SIG_2026_0525_002", "extends")]
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
