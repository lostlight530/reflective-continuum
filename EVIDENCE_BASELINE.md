# 2026 Evidence Baseline

- Retrieval date: 2026-08-17
- Rule: primary/official sources bound implementation and claim language; they do not certify this repository

## Runtime and storage

- [Python 3.14 documentation](https://docs.python.org/3.14/whatsnew/) identifies the current 3.14 documentation line used by this baseline. CI also retains 3.12 as the older supported compatibility line; support status must be rechecked when this matrix changes.
- [SQLite foreign-key documentation](https://www.sqlite.org/foreignkeys.html) states that applications must enable foreign-key enforcement per connection. `GraphDB` enables and verifies it.
- [SQLite FTS5 external-content documentation](https://www.sqlite.org/fts5.html#external_content_tables) explains that the application must keep the content table and FTS index consistent, commonly with triggers. This supports explicit insert/update/delete triggers and avoiding replace-style hidden deletes.
- [SQLite in-memory database documentation](https://www.sqlite.org/inmemorydb.html) states that a bare `:memory:` database is private to the connection that opened it, every bare `:memory:` connection creates an independent database, and that database ceases to exist when the connection closes.

## Automation and supply chain

- [GitHub secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) says a full-length commit SHA is the immutable action reference and recommends least `GITHUB_TOKEN` permissions. Workflows pin official actions and separate read-only build from Pages deployment authority.
- [SLSA v1.2](https://slsa.dev/spec/v1.2/) informs provenance vocabulary, but this repository does not claim an SLSA build level.

## AI/agent claim boundaries

- [NIST AI 600-1](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence), updated 2026-04-08, is a voluntary generative-AI risk profile. It motivates lifecycle risk records; it does not validate a local “cognitive” architecture.
- [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) covers goal hijacking, tool misuse, privilege, supply chain, unexpected execution, and memory/context poisoning. This library exposes no agent tools; callers still own these controls.
- [OpenAI’s 2026 third-party evaluation playbook](https://openai.com/index/trustworthy-third-party-evaluations-foundations/) explains that harness, tools, retries, scoring, budgets, and validity checks affect measured capability. Therefore every result is scoped to its evaluation system.
- [Anthropic, Trustworthy agents in practice (2026-04-09)](https://www.anthropic.com/research/trustworthy-agents) states that layered safeguards are not a guarantee and emphasizes tool/data/permission/environment choices. This supports least authority and accountable approvals.
- [Anthropic’s 2026 constitution announcement](https://www.anthropic.com/news/claude-new-constitution) explicitly notes model outputs may not always adhere to intended ideals. Prose policy is not an executable guarantee.
- [Google DeepMind AlphaEvolve](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/) combines LLM proposals with automated evaluators in domains with executable metrics. It is evidence for evaluator-backed search, not deterministic cognition or universal convergence.

## Ingestion, truth, and source authority

Reflective Continuum separates three independent axes:

1. `INGESTION_OUTCOME`: whether a signal passed the repository ingestion/reflection path.
2. `SOURCE_CREDIBILITY`: whether the source is primary research, an institutional publication, a vendor/blog source, secondary material, or unverified.
3. `EPISTEMIC_SUPPORT`: what exact proposition the source supports under its assumptions.

`ACCEPTED` is an ingestion result. It does not mean `TRUE`, `AUTHORITATIVE`, `IMPLEMENTED`, or `REPRODUCED`.

`REJECTED_FROM_INGESTION` is also an ingestion result. It does not mean the source proposition is false. A rejected signal remains useful audit evidence when its source and rejection reason are preserved.

## Database-state semantics

Database observations are scoped to the database path and connection actually inspected.

For a bare SQLite `:memory:` database:

- each independent connection receives a distinct database
- another task/process/connection must not be assumed to observe the same state
- closing the owning connection destroys that in-memory database

Therefore an R1 statement such as `written to graph` and a later R2 observation such as `Nodes=0 / Edges=0` do not, by themselves, prove either successful durable persistence or failed ingestion unless the same persistent database identity/path is verified.

Use `PERSISTENCE_LINK_NOT_VERIFIED` when the R1→R2 storage relationship is unknown.

## Health and empty-state semantics

Module-local checks and system-level state are different.

- successful import/init may be reported as module-local success
- rule-engine fixture success may be reported as rule-engine-local success
- integrity/foreign-key/FTS checks establish only their named contract
- `Nodes=0 / Edges=0` does not prove persistence health, successful Daily ingestion, or semantic correctness

When the database is empty and the cause is not established, use `INDETERMINATE_EMPTY_STATE`. Do not collapse empty state into global `HEALTHY` or global `FAILED` without additional evidence.

## Drift and transition semantics

A drift label belongs to the data and transition set actually inspected.

- `STABLE` must not imply that uncomputed operational transitions were stable.
- If no drift is detected only inside the available weekly audit surface, prefer `NO_DRIFT_DETECTED_WITHIN_AUDIT_SCOPE`.
- Synthetic/test transitions and operational/runtime transitions are separate evidence classes.
- Synthetic transitions must never be counted as observed production transitions.
- If event origin cannot be separated, operational transition count remains `NOT_COMPUTED`.

## Daily-to-Weekly inheritance

Weekly reports preserve Daily uncertainty and failure history.

- a later 27/27 test snapshot does not erase an earlier Daily error
- `Missing dates: NONE` does not mean every field was computed
- rejected signals remain visible in the weekly state
- Weekly summaries may aggregate or downgrade Daily evidence but may not strengthen an uncertain Daily observation without a new, explicit evidence record

## Source reuse and novelty

Repeated primary papers or signals are allowed when deliberate. Label the reason when research novelty matters:

- `REVALIDATED_SOURCE`
- `REPEATED_CONTROL_SIGNAL`
- `NEW_CLAIM_FROM_EXISTING_SOURCE`
- `DUPLICATE_NO_NEW_EVIDENCE`

Repeated ingestion must not be presented as independent corroboration merely because it occurred on another date.

## Correction policy

Historical R1–R4 artifacts are execution evidence. When a claim is materially over-strong but the original record remains useful, prefer an explicit calibration/erratum that states precedence, corrected interpretation, and unresolved uncertainty.

Do not repair an audit finding merely to make the audit green. Orphans, ghost chains, missing mappings, and uncomputed state stay unresolved until a separate intentional architecture task addresses them.

## Review trigger

Recheck this file when the Python matrix, SQLite storage model, schema, action major versions, AI risk model, R1/R2 persistence architecture, drift semantics, or repository claim scope changes. A stale link is a maintenance issue; a source update does not silently change code policy.