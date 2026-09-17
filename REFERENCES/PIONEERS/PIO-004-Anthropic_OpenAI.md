> [!NOTE]
> **Current architecture interpretation — 2026-09-18**
> - **Subject class:** `EXTENSION / NON-NORMATIVE REFERENCE`
> - **Role:** Active external reference map for **Anthropic OpenAI**
> - **Authority:** Non-normative research context: useful for tracing external ideas and comparisons but not an implementation or capability authority
> - **Current meaning:** External mechanisms remain external. Similarity, inspiration, or interpretive mapping must not be promoted into a claim that Reflective Continuum implements the cited system
> - **Evidence / implementation boundary:** Paper/company statements, analogy, and source prestige do not establish local reflection, semantic search, persistence, rollback, or convergence behavior
> - **Cross-document relation:** Current Specification/code and ADR/Methodology outrank this reference map for repository facts; external facts require proposition-specific source support
> - **Update trigger:** Update for source-identity correction, materially changed external interpretation, broken current reference, or explicit new comparison—not for routine style modernization
> - **Preservation rule:** Existing subject prose remains part of the repository record. This pass narrows current interpretation without erasing earlier framing or source history

# Anthropic and OpenAI: agent evaluation and control boundaries

- Reviewed: 2026-08-05
- Evidence state: SUPPORTED summaries of official 2026 publications

OpenAI’s [trustworthy third-party evaluations playbook](https://openai.com/index/trustworthy-third-party-evaluations-foundations/) explains that harness, tools, context handling, retries, scoring, resource budget, and validity checks materially affect measured agent capability. Reflective consequence: every behavioral or repeatability report names the tested system and budget; a score is not a context-free property.

Anthropic’s [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) discusses multi-turn, tool-using, state-changing agents and the need for evaluation strategies matching system complexity. [Trustworthy agents in practice](https://www.anthropic.com/research/trustworthy-agents) states layered safeguards are not guarantees and emphasizes careful tool, data, permission, and environment choices. The [2026 Claude constitution announcement](https://www.anthropic.com/news/claude-new-constitution) notes outputs may not always adhere to intended ideals.

Reflective Continuum therefore does not parse prose principles into executable guarantees. `RuleConfig`, database constraints, tests, permissions, and caller approvals are distinct controls. Even together they support bounded evidence, not perfect alignment or safety.

Review trigger: update when an official source changes the stated boundary or when this repository adds model/tool execution.