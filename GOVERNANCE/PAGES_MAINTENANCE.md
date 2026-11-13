# Reflective public homepage — current, historical and implementation boundaries

The only deployed page source is root `index.html`, copied by `.github/workflows/pages.yml`. No frontend bundler or external npm dependency is required to publish it

## Current publication

The front page explains **two independent implemented references** in one place: Axiom-0's canonical inputs / numerical contract / guarded local transitions, and Reflective Continuum's versioned SQLite graphs / search / delta / entropy / bounded transactions

This is a unified **explanation**, not an executed cross-repository integration or shared state machine. The repository's `CODE/**` and `SPECIFICATION.md` remain authoritative for Reflective runtime behavior; Axiom's linked code and specification remain authoritative for Axiom behavior

## Preserved history

- The five-repository phase analogy and sealed traffic snapshot through 2026-08-31 remain dated, separate material in the lower page
- Prior to UI restructuring, the repository base main was `c095610473c790eeda96edd097d651d395db9293`; immediately before the latest repair the homepage was `758fd575b688b721dd8c49a7e556225dd57c3cd7`
- Retrieve old page text from Git history for comparison; do not maintain a second competing entrypoint or erase old evidence
- Original numbers, entropy explanation and code identifiers should not be modified by copy or layout changes

## Frontend release checklist

Review independent-runtime language, clear Chinese title/section navigation, bilingual switching, no displayed Chinese `U+3002`, all internal anchors, 390px/mobile long content and Pages deployment. Tests of SQLite Python are separate from this static page's visual checks

Previous scope: [PR #609](https://github.com/lostlight530/reflective-continuum/pull/609)
