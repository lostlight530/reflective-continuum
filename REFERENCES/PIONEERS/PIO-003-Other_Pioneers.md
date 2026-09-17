> [!NOTE]
> **Current architecture interpretation — 2026-09-18**
> - **Subject class:** `EXTENSION / NON-NORMATIVE REFERENCE`
> - **Role:** Active external reference map for **Other Pioneers**
> - **Authority:** Non-normative research context: useful for tracing external ideas and comparisons but not an implementation or capability authority
> - **Current meaning:** External mechanisms remain external. Similarity, inspiration, or interpretive mapping must not be promoted into a claim that Reflective Continuum implements the cited system
> - **Evidence / implementation boundary:** Paper/company statements, analogy, and source prestige do not establish local reflection, semantic search, persistence, rollback, or convergence behavior
> - **Cross-document relation:** Current Specification/code and ADR/Methodology outrank this reference map for repository facts; external facts require proposition-specific source support
> - **Update trigger:** Update for source-identity correction, materially changed external interpretation, broken current reference, or explicit new comparison—not for routine style modernization
> - **Preservation rule:** Existing subject prose remains part of the repository record. This pass narrows current interpretation without erasing earlier framing or source history

# Foundational mechanisms and their boundaries

- Reviewed: 2026-08-05

## Shannon entropy

Shannon entropy quantifies uncertainty of a probability distribution. In this repository it is calculated over normalized PageRank scores and reported in nats. That choice does not measure meaning, consciousness, truth, or safety. Source: C. E. Shannon, [A Mathematical Theory of Communication](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf) (1948).

## PageRank

PageRank provides a graph-ranking mechanism based on link structure and damping. This implementation is a small validated reference, not a web-scale reproduction. Source: Page, Brin, Motwani, Winograd, [The PageRank Citation Ranking](https://ilpubs.stanford.edu:8090/422/) (Stanford technical report, 1999).

## SQLite and FTS5

SQLite supplies transactional storage; FTS5 supplies lexical full-text indexing and BM25 ranking. Applications must enable foreign keys and synchronize external-content indexes. Sources: [SQLite foreign keys](https://www.sqlite.org/foreignkeys.html) and [FTS5 external-content tables](https://www.sqlite.org/fts5.html#external_content_tables).

These mechanisms are composable engineering tools. Combining them does not create an independent cognitive architecture. Their failure modes—schema mismatch, disabled constraints, malformed queries, stale indexes, threshold misuse—remain explicit test targets.