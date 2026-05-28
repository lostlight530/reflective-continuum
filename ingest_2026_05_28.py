import sys
from CODE.tasks.insight_morpher import InsightMorpher

signals = [
    {
        "id": "SIG_2026_0528_001",
        "content": "Ecosystem Signal: The cloner-to-visitor ratio has stabilized at 92:1, indicating silent but massive ingestion of deterministic protocols by major institutions.",
        "edges": []
    },
    {
        "id": "SIG_2026_0528_002",
        "content": "Industry Analysis: Leading AI players are quietly migrating away from pure probabilistic RL frameworks towards hybrid systems where deterministic metacognition acts as the final constraint layer.",
        "edges": [("SIG_2026_0528_002", "SIG_2026_0528_001", "correlates_with")]
    },
    {
        "id": "SIG_2026_0528_003",
        "content": "A 'cognitive divergence alert' mechanism is now formally recognized as superior to standard reward models for preventing catastrophic hallucination chains during deep autonomous reasoning.",
        "edges": [("SIG_2026_0528_003", "SIG_2026_0528_002", "validates_migration")]
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
