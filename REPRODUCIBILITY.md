# Reproducibility

Record commit SHA, Python and SQLite versions, operating system, database schema version, sanitized fixture or digest, query/version/threshold, command array, UTC times, exit code, artifact digest, and untested boundary. Never retain credentials or unnecessary content.

The convergence drill is intentionally a repeatability test: a fixed local fixture is rebuilt and snapshot digests are compared. It does not test model sampling, distributed scheduling, production databases, semantic truth, or long-term convergence.

Database tests use temporary or in-memory files. Production reproductions should work on a copy, record `PRAGMA integrity_check`, foreign-key state, schema SQL, journal mode, and backup/restore procedure, and avoid uploading private content.

Passing results are revision-specific. If reproduction differs, first separate environment drift, schema mismatch, fixture change, nondeterministic external dependency, and a contract regression. Mark skipped checks explicitly.