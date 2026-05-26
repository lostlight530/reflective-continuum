import sys
from CODE.tasks.insight_morpher import InsightMorpher

signals = [
    {
        "id": "SIG_2026_0526_001",
        "content": "Recent research reveals deterministic frameworks offer superior alignment scaling vs probabilistic models.",
        "edges": []
    },
    {
        "id": "SIG_2026_0526_002",
        "content": "Metacognition requires hard mathematical boundaries to escape hallucinatory cycles in deep reflection.",
        "edges": [("SIG_2026_0526_002", "SIG_2026_0526_001", "extends")]
    },
    {
        "id": "SIG_2026_0526_003",
        "content": "Industry shift: Top labs replacing probabilistic safety filters with absolute state constraint validators.",
        "edges": [("SIG_2026_0526_003", "SIG_2026_0526_002", "supports")]
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
