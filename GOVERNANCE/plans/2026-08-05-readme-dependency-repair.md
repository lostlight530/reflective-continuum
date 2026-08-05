# Reflective README and Dependency Repair Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the obsolete metacognition narrative and finish the already-green GitHub Actions dependency upgrades.

**Architecture:** Keep the standard-library Python and SQLite contracts unchanged. Add an exact README review gate, update immutable action pins, group future updates, and make the README mirror the engineering specification.

**Tech Stack:** Python 3.12/3.14, unittest, SQLite/FTS5, GitHub Actions, Markdown.

## Global Constraints

- No database schema, Python dependency, homepage, `RESEARCH/**`, Jules, or Pages-content change.
- README remains protected by default.
- Full-SHA action pins and least privilege remain mandatory.
- Implement on `codex/scientific-closure-20260805`.

---

### Task 1: Protected README allowance

**Files:**
- Modify: `scope_guard.py`
- Create: `tests/test_scope_guard.py`
- Modify: `.github/workflows/ci.yml`

**Interfaces:**
- Produces: `blocked_paths(paths: list[str], allowed_files: set[str]) -> list[str]`
- Produces: repeatable `--allow-file PATH`

- [ ] **Step 1: Write failing tests**

Cover default README denial, exact README allowance, continued denial for `index.html`, `.nojekyll`, `LICENSE`, and `RESEARCH/daily/x.md`.

- [ ] **Step 2: Run focused test**

Run: `python -m unittest tests.test_scope_guard -v`  
Expected: FAIL before implementation.

- [ ] **Step 3: Implement exact allowance and label gate**

Use a pure `blocked_paths` function and `argparse action="append"`. The workflow passes `--allow-file README.md` only when `scope:approved-readme` is present.

- [ ] **Step 4: Verify**

Run: `python -m unittest tests.test_scope_guard tests.test_repository -v`  
Expected: PASS.

- [ ] **Step 5: Commit**

Commit message: `test: preserve exact reflective ownership gates`.

### Task 2: Immutable action upgrades and grouping

**Files:**
- Modify: `.github/workflows/ci.yml`
- Modify: `.github/workflows/pages.yml`
- Modify: `.github/dependabot.yml`
- Modify: `tests/test_repository.py`

- [ ] **Step 1: Add failing action-contract tests**

Require checkout `3d3c42e5aac5ba805825da76410c181273ba90b1` in both workflows and setup-python `5fda3b95a4ea91299a34e894583c3862153e4b97` in CI. Require an actions update group.

- [ ] **Step 2: Run tests to prove old pins fail**

Run: `python -m unittest tests.test_repository -v`  
Expected: FAIL on the old SHAs.

- [ ] **Step 3: Update pins, comments, and Dependabot grouping**

Keep configure/upload/deploy Pages action pins unchanged because they already resolve to their declared versions.

- [ ] **Step 4: Run repository tests**

Run: `python -m unittest tests.test_repository -v`  
Expected: PASS.

- [ ] **Step 5: Commit**

Commit message: `chore(deps): update verified action runtimes`.

### Task 3: Evidence-scoped README

**Files:**
- Modify: `README.md`
- Modify: `tests/test_repository.py`

- [ ] **Step 1: Add failing narrative tests**

Reject `metacognitive observer`, `cognitive rollback`, `Gaseous Phase`, `元认知观察器`, and any claim that PageRank entropy proves cognition. Require links to specification, evidence baseline, reproducibility, and security.

- [ ] **Step 2: Rewrite bilingual content**

Describe storage, FTS5 search, deltas, PageRank-derived Shannon entropy, validation, transactions, bounded hooks, task entrypoints, migration warning, verification commands, and non-goals.

- [ ] **Step 3: Run complete verification**

Run: `python -m compileall -q CODE tests scope_guard.py && python -m unittest discover -s tests -v && python -m CODE.tasks.cortex_selfcheck && python -m CODE.tasks.convergence_drill --iterations 100`  
Expected: every command exits 0.

- [ ] **Step 4: Commit**

Commit message: `docs: align Reflective README with executable contracts`.

### Task 4: Cloud PR and main verification

- [ ] **Step 1: Create/apply `scope:approved-readme` and open one PR**
- [ ] **Step 2: Require Python 3.12/3.14, selfcheck, drill, and Pages-related checks to pass**
- [ ] **Step 3: Merge, verify main CI and Pages, or revert the merge commit on failure**
