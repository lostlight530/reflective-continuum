# Graph-derived entropy boundary evaluation

- Method version: 2026-08-24
- Implementation anchor: `CODE/entropy_analyzer.py`

## Objective

Evaluate the repository's configured graph-entropy boundary for one declared graph without interpreting the result as cognition, safety, semantic truth, or global convergence.

## Inputs

- unique node IDs
- edges whose endpoints belong to the declared node set
- PageRank damping / iteration / tolerance configuration
- non-negative entropy threshold
- graph version/store identity when the result is tied to persisted state

## Procedure

1. Validate node uniqueness and PageRank configuration.
2. Reject edges referencing unknown nodes.
3. Collapse duplicate edges as implemented.
4. Compute normalized PageRank.
5. Compute Shannon entropy in nats over the normalized rank values.
6. Compare the entropy with the declared threshold through `check_phase_boundary()`.
7. Record the graph/version identity, rank distribution or reproducible snapshot identity, entropy value, threshold, and boolean boundary result.

## Outputs

- normalized PageRank mapping
- Shannon entropy in nats
- declared threshold
- boundary boolean
- graph/version/store scope

## Failure conditions

Do not report a valid boundary result when graph identity is ambiguous, nodes are duplicated, an edge references an unknown node, configuration is invalid, or the threshold is missing from a threshold-dependent claim.

## Evidence boundary

A threshold crossing means only:

`GRAPH_DERIVED_ENTROPY > DECLARED_THRESHOLD`.

It does not prove instability, cognition, alignment, semantic drift, or a physical phase transition.
