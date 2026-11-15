> [!NOTE]
> **Current architecture interpretation — 2026-09-18**
> - **Subject class:** `METHOD`
> - **Role:** Current methodology: **Graph-derived entropy boundary evaluation**
> - **Authority:** Repository-native method authority for the exact procedure, observation rule, assumptions and limits stated by this file
> - **Current meaning:** Treat the named method as a repeatable interpretation/checking contract. Method definition does not imply execution on the current revision, and historical examples do not become current state by proximity
> - **Evidence / implementation boundary:** FTS lexical change is not semantic truth; reflector callback behavior is not autonomous cognition; SQLite savepoint rollback is local transaction rollback; persistence and convergence require explicit store/run evidence rather than terminology alone
> - **Cross-document relation:** Specification/runtime code bound mechanics; ADRs explain durable choices; dated evidence records observations; Reproducibility owns revision/store/replay identity
> - **Update trigger:** Update when procedure, threshold, implementation mapping, historical evidence range or failure/reconciliation semantics materially changes
> - **Preservation rule:** Existing method procedure and examples remain in place; current clarification does not rewrite earlier execution evidence

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

## Entropy degeneracy and strict-threshold interpretation

`compute_pagerank` uses sorted unique node IDs, collapses duplicate edge tuples, handles dangling mass and normalizes the final score map. `calculate_topological_entropy` computes `-sum(p_i * ln(p_i))` after normalization and returns `0.0` for non-positive total mass. Consequently an empty score collection and a singleton nonzero rank distribution both return zero entropy although they represent different graph conditions.

`check_phase_boundary` compares this value with the caller threshold using **strict greater-than**. Equality does not trigger `GASEOUS`; neither low entropy nor a non-trigger proves semantic stability, convergence, safety or persistence. Preserve node count, graph version, edge set, damping/tolerance configuration and score vector alongside the scalar when a research interpretation depends on these distinctions.

A useful unexecuted counterexample pairs an empty graph with a one-node graph, then compares their entropy scalar and their separately computed snapshot data. The scalar alone is insufficient to classify graph equivalence.

## Relationship-projection and termination boundary

`GraphDB.get_all_edges(version)` returns only `(source_id, target_id)`, not the persisted `relationship` label. `compute_pagerank` then computes `sorted(set(edges))`; two distinct persisted relationships with identical endpoints count as **one** directed edge in the current rank graph. Therefore the PageRank/entropy calculation is on a **simple directed projection** of the stored relationship multigraph, not on all stored relation types or multiplicities. Preserve the projection rule when comparing versions.

The iteration stops either when the L1 score delta meets `tol` or when `max_iterations` is exhausted. The public function returns only the normalized mapping, not a `converged` flag or residual. A bounded iteration count must not be described as independently certified convergence. For a negative fixture, vary relationship labels while preserving source/target pairs, and compare stored edge counts with the rank-projection inputs. This is a static source-derived design, not executed here.

`RuleConfig` validates its numeric entropy threshold for negativity, but does not check finiteness at construction; `check_phase_boundary` rejects non-finite thresholds when the value reaches the analysis function. Record the actual rejection point when discussing invalid configurations.
