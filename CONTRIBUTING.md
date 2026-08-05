# Contributing

Reflective Continuum accepts small changes that strengthen versioned storage, bounded analysis, provenance, and reproducibility.

Before coding, identify the governing ADR/method, define inputs/outputs/errors/migration, add a regression test, and preserve separately owned README, homepage, `.nojekyll`, RESEARCH, and license paths. Database schema changes require a migration and compatibility note; never silently reinterpret existing rows.

Use Python 3.12 or 3.14:

```text
python -m unittest discover -s tests -v
python -m CODE.tasks.cortex_selfcheck
python -m CODE.tasks.convergence_drill --iterations 100
```

Runtime code is standard-library only. A proposed dependency needs owner, threat/license review, alternative analysis, lock/update policy, and rollback. AI-assisted work follows `AI_USE_DISCLOSURE.md`; generated output is untrusted until reviewed and tested.

Pull requests must state exact revision, commands/results, unrun checks, security/privacy/retention impact, and rollback. Failed or unavailable required checks prevent completion claims.