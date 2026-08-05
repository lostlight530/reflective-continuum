# 2026 Evidence Baseline

- Retrieval date: 2026-08-05
- Rule: primary/official sources bound implementation and claim language; they do not certify this repository

## Runtime and storage

- [Python 3.14 documentation](https://docs.python.org/3.14/whatsnew/) identifies the current 3.14 documentation line. CI also retains 3.12 as the older supported compatibility line; support status must be rechecked when this matrix changes.
- [SQLite foreign-key documentation](https://www.sqlite.org/foreignkeys.html) states that applications must enable foreign-key enforcement per connection. `GraphDB` enables and verifies it.
- [SQLite FTS5 external-content documentation](https://www.sqlite.org/fts5.html#external_content_tables) explains that the application must keep the content table and FTS index consistent, commonly with triggers. This supports explicit insert/update/delete triggers and avoiding replace-style hidden deletes.

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

## Review trigger

Recheck this file when the Python matrix, SQLite schema, action major versions, AI risk model, or repository claim scope changes. A stale link is a maintenance issue; a source update does not silently change code policy.