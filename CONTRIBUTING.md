# Contributing

Reflective Continuum welcomes bounded contributions to its graph-state implementation, tests, ADRs, methodology, evidence documentation, reproducibility rules, and repository infrastructure.

## Start from the owning surface

Before changing anything, identify what currently owns the behavior or interpretation:

- `CODE/` and `tests/` own executable behavior and regression evidence;
- `ADR/` records architectural decisions and consequences;
- methodology/evidence documents own interpretation and research boundaries;
- `REPRODUCIBILITY.md` owns revision, environment, database, and replay requirements;
- root metadata, `.github/`, security, citation, and release files are repository infrastructure;
- historical research and audit material remains point-in-time evidence unless a correction explicitly owns it.

## Implementation changes

For executable behavior:

1. reproduce the defect or define the new contract at a named revision;
2. identify storage identity, schema/version, inputs, outputs, and failure behavior;
3. add or update proportionate regression coverage;
4. document migrations or compatibility effects when persistent state changes;
5. update the owning ADR or method only when the architectural or methodological contract actually changes.

Runtime code is standard-library only. A proposed dependency needs a technical reason, security/license review, update policy, and rollback path.

## Evidence and state claims

Reflective Continuum deliberately separates local state observations from stronger semantic claims.

```text
connection-local state != cross-run persistence
snapshot digest != semantic equivalence
repeatability drill != long-horizon convergence
local ingestion acceptance != source truth
lexical top-result stability != semantic stability
archived publication != later main revision
```

When a result depends on a database, identify the database path/URI or other storage identity and the revision/environment used to observe it. Preserve unknown, rejected, failed, missing, and not-computed states instead of strengthening them for readability.

## Verification

Use checks relevant to the changed surface. Current targeted entry points include:

```bash
python -m unittest discover -s tests -v
python -m CODE.tasks.cortex_selfcheck
python -m CODE.tasks.convergence_drill --iterations 100
```

Record exact commands and observed results in the pull request. A check that was not run is not a pass.

For database changes, include the relevant schema/state assumptions and use copies or temporary fixtures for destructive or migration testing. Never include private production data in public artifacts.

## Documentation, ADRs, and corrections

Prefer the smallest current owning document. Do not rewrite historical Daily/Weekly/Monthly or archived audit material merely because current terminology or interpretation has improved. Correct current documentation forward while preserving the earlier record's recoverable meaning.

AI assistance may support drafting or consistency review, but generated text is not independent evidence. Contributors remain responsible for code, claims, citations, and verification.

## Pull requests

Use the repository pull-request template and include:

- the problem and bounded change;
- affected implementation, storage, ADR/method, evidence, or metadata surfaces;
- verification actually performed;
- checks or environments not exercised;
- compatibility, migration, and historical impact;
- security/privacy implications;
- a practical rollback.

## Security, privacy, license, and attribution

Follow `SECURITY.md` for sensitive reports. Do not publish credentials, private data, or exploit details requiring coordinated disclosure.

Contributions to repository-owned work are submitted under the current `LICENSE`. Third-party material retains its own attribution and licensing, and Git/PR history remains the source of contribution attribution.
