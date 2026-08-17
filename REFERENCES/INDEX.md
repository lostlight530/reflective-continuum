# Reference Topology Index

Status: active non-normative reference map

`REFERENCES/**` contains background, historical, and methodological context. A reference is **not** executable policy, a specification requirement, or evidence that Reflective Continuum implements the cited external system.

## Pioneers collection

| Reference | Role | Normative status | Repository mapping |
|---|---|---|---|
| [PIO-001 — Google DeepMind](./PIONEERS/PIO-001-Google_DeepMind.md) | First-party AlphaEvolve context for proposal/evaluator separation | `BACKGROUND_SUPPORTED` | Evaluator-backed search is an analogy only; local fixtures/validators are not an AlphaEvolve implementation |
| [PIO-002 — Google paper interpretations](./PIONEERS/PIO-002-Google_Paper_Interpretations.md) | Method for interpreting research claims without importing mythology | `METHODOLOGY_CONTEXT` | Source/claim/evaluator/budget/limitations discipline |
| [PIO-003 — Other pioneers](./PIONEERS/PIO-003-Other_Pioneers.md) | Foundational mechanisms: Shannon entropy, PageRank, SQLite, FTS5 | `MECHANISM_BACKGROUND` | Supports bounded interpretation of graph statistics/storage/search; not cognition |
| [PIO-004 — Anthropic/OpenAI](./PIONEERS/PIO-004-Anthropic_OpenAI.md) | Official agent-evaluation and control-boundary context | `BACKGROUND_SUPPORTED` | Supports scoped evaluation and separation of prose principles from executable controls |

## Topology resolution

The W33 R4 audit identified all four PIONEERS files as `UNRESOLVED_ORPHAN` because they were not connected to a repository-level reference index or to the engineering decision topology.

This index resolves the **documentation orphan** without inventing normative dependencies:

- `SPECIFICATION.md` links to this reference map for non-normative context
- `ADR/INDEX.md` links to this reference map and keeps ADR decisions separate from background material
- individual PIONEERS files remain unchanged historical/reference artifacts

## Authority rules

- First-party or primary material can support only the proposition actually stated by the source.
- An external architecture does not certify local architecture.
- A mathematical mechanism retains its original domain and assumptions.
- Surveys, interpretations, analogies, and contextual summaries do not override `SPECIFICATION.md` or ADR decisions.
- If a reference conflicts with executable repository evidence, record the conflict and narrow the claim; do not silently rewrite runtime facts.

## Ownership

Reference maintenance may update links, source versions, interpretation boundaries, and disconfirming conditions. Runtime policy changes require an explicit ADR/specification change and executable verification where applicable.
