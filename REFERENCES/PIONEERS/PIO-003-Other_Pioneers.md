# Foundational mechanisms and their boundaries

- Reviewed: 2026-08-05

## Shannon entropy

Shannon entropy quantifies uncertainty of a probability distribution. In this repository it is calculated over normalized PageRank scores and reported in nats. That choice does not measure meaning, consciousness, truth, or safety. Source: C. E. Shannon, [A Mathematical Theory of Communication](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf) (1948).

## PageRank

PageRank provides a graph-ranking mechanism based on link structure and damping. This implementation is a small validated reference, not a web-scale reproduction. Source: Page, Brin, Motwani, Winograd, [The PageRank Citation Ranking](https://ilpubs.stanford.edu:8090/422/) (Stanford technical report, 1999).

## SQLite and FTS5

SQLite supplies transactional storage; FTS5 supplies lexical full-text indexing and BM25 ranking. Applications must enable foreign keys and synchronize external-content indexes. Sources: [SQLite foreign keys](https://www.sqlite.org/foreignkeys.html) and [FTS5 external-content tables](https://www.sqlite.org/fts5.html#external_content_tables).

These mechanisms are composable engineering tools. Combining them does not create an independent cognitive architecture. Their failure modes—schema mismatch, disabled constraints, malformed queries, stale indexes, threshold misuse—remain explicit test targets.