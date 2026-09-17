# Reproducibility

Record commit SHA, Python and SQLite versions, operating system, database schema version, sanitized fixture or digest, query/version/threshold, command array, UTC times, exit code, artifact digest, and untested boundary. Never retain credentials or unnecessary content.

The convergence drill is intentionally a repeatability test: a fixed local fixture is rebuilt and snapshot digests are compared. It does not test model sampling, distributed scheduling, production databases, semantic truth, or long-term convergence.

Database tests use temporary or in-memory files. Production reproductions should work on a copy, record `PRAGMA integrity_check`, foreign-key state, schema SQL, journal mode, and backup/restore procedure, and avoid uploading private content.

## Archived software publication and exact replay identity

The repository has a public Zenodo software publication identified by DOI `10.5281/zenodo.22791141` and publication date 2026-09-16.

The DOI identifies an archived software publication. It does not replace the exact Git revision, Python/SQLite environment, database/store identity, fixture/query, thresholds, command, and observed result needed to reproduce a revision-specific claim.

Keep these identities distinct:

```text
Zenodo publication identity != current main revision
Git commit identity != database/store identity
snapshot digest != semantic equivalence
repeatability != long-horizon convergence
archive presence != reproduction
later main state != archived publication contents
```

When a result depends on exact implementation or database state, retain the Git revision and storage identity in addition to any publication citation. Do not infer an exact archive-to-commit mapping unless the repository or publication metadata explicitly records and verifies it.

Passing results are revision-specific. If reproduction differs, first separate environment drift, schema mismatch, fixture change, nondeterministic external dependency, storage-identity mismatch, and a contract regression. Mark skipped checks explicitly.
