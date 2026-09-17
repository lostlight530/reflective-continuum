## Summary

What problem does this change address, and what changed?

## Change type

- [ ] implementation / bug fix
- [ ] tests / validation
- [ ] ADR / methodology / evidence
- [ ] storage / schema / migration
- [ ] repository infrastructure / metadata
- [ ] maintenance / governance

## Affected surfaces

List the code, database/state, ADR/method, evidence, documentation, or metadata affected. Note related surfaces intentionally left unchanged.

## State and evidence impact

Describe the storage identity, schema/version, inputs, observations, and interpretation affected when relevant.

Keep connection-local state, cross-run persistence, repeatability, source support, and semantic claims separate.

## Verification performed

List exact commands/checks actually run and their observed results.

## Known limits / verification not performed

List material checks, environments, storage identities, or evidence questions not exercised or unresolved.

## Compatibility, migration, and historical impact

Describe schema/data migration, compatibility, reproducibility, or point-in-time evidence impact. Preserve historical records when a forward correction is sufficient.

## Security and privacy

Describe impact on database contents, external inputs, permissions, public exposure, dependencies, or sensitive data. Follow `SECURITY.md` for sensitive reports.

## Publication / metadata impact

State whether README, citation metadata, release metadata, or other public discovery surfaces must remain synchronized.

## Rollback

Describe the smallest safe rollback.

## Review checklist

- [ ] The diff is limited to the stated purpose.
- [ ] Tests/checks described as passing were actually executed.
- [ ] State identity and evidence scope are explicit where material.
- [ ] Historical evidence was not silently rewritten to match later state.
- [ ] No credentials, private data, caches, or unrelated generated/local state is included.
