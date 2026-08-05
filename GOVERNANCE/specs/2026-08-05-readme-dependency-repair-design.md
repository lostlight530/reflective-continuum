# Reflective README and Dependency Repair Design

Date: 2026-08-05
Status: approved design baseline
Base: `main@6ee6e27bc5076606444da220c230dea26b90c304`

## Objective

Replace the obsolete metacognition narrative with a bilingual, executable-contract description and update the GitHub Actions runtime dependencies while preserving the standard-library Python boundary, homepage, and Jules research stream.

## Verified starting point

The implemented system is a SQLite graph/FTS5 reference with versioned storage, deterministic deltas, PageRank-derived Shannon entropy, content validation, transactional ingestion, and bounded reflection hooks. The root README instead presents it as a deterministic metacognitive observer and implies cognitive rollback and phase transitions beyond the repository's evidence.

Dependabot PRs for checkout 7.0.1 and setup-python 7.0.0 passed both Python jobs, then were closed without merge. The Python project has no runtime package dependencies; the remaining dependency work concerns immutable GitHub Action references and their maintenance policy.

## README design

The replacement README will contain:

1. purpose, implemented scope, and non-goals;
2. storage, search/delta, analysis, validation, observation, and task capability matrix;
3. minimal local verification commands;
4. persistence and migration warnings;
5. evidence, reproducibility, security, and specification links;
6. a clear distinction between project vocabulary and measured quantities;
7. limitations stating that entropy thresholds and bounded hooks do not prove cognition, semantic truth, convergence, or safety.

English and Chinese sections must remain claim-equivalent.

## Dependency and ownership design

Update:

- `actions/checkout` to 7.0.1 at `3d3c42e5aac5ba805825da76410c181273ba90b1`;
- `actions/setup-python` to 7.0.0 at `5fda3b95a4ea91299a34e894583c3862153e4b97`.

Apply the checkout update to verification and Pages workflows. Preserve full-SHA pinning, least privilege, Python 3.12/3.14, and the existing Pages actions already at their verified tags. Group compatible GitHub Actions updates in Dependabot.

`scope_guard.py` gains a repeatable exact-file allowance. `README.md` remains protected unless the PR has the maintainer-applied `scope:approved-readme` label. `RESEARCH/**`, homepage, license, and `.nojekyll` receive no exemption.

## Verification and acceptance

Both Python matrix jobs, the full unit/contract suite, observable selfcheck, 100-iteration repeatability drill, scope-guard regression tests, and Pages artifact preparation must pass. Action SHAs must resolve to their declared official tags. README links and paths must exist, and superseded cognitive or absolute claims must be absent.

## Non-goals and rollback

No Python package dependency, database schema change, homepage change, Jules path change, research rewrite, or new agent runtime. Delivery uses one PR from `codex/scientific-closure-20260805`. Rollback is a merge-commit revert.
