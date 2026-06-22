import sys
from CODE.tasks.insight_morpher import InsightMorpher

signals = [
    {"id": "S_001", "content": "DeepMind releases paper on deterministic agent alignment.", "edges": [("S_001", "Determinism", "relates_to")]},
    {"id": "S_002", "content": "OpenAI research shows metacognition layers improve safety constraints.", "edges": [("S_002", "Metacognition", "relates_to")]},
    {"id": "S_003", "content": "New framework proposes zero-entropy architectures for recursive self-improvement.", "edges": [("S_003", "Zero_Entropy", "relates_to")]}
]
morpher = InsightMorpher()
success = morpher.morph_signals(signals)

if success:
    print("\n[SUCCESS] All signals successfully ingested into the continuum deterministically.")
    sys.exit(0)
else:
    print("\n[FAILURE] Cognitive rejection occurred. Cortical rollback triggered. Terminating.")
    sys.exit(1)
